from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
# PStorage project's database model.


class locations(models.Model):
    class Meta:
        db_table = 'app_locations'

    name = models.TextField()  # location name

    active = models.BooleanField(default=True)
    comment = models.TextField()

class racks(models.Model):
    class Meta:
        db_table = 'app_racks'

    active = models.BooleanField(default=True)
    comment = models.TextField()

    locationID = models.ForeignKey(locations)

class places(models.Model):
    class Meta:
        db_table = 'app_places'

    column = models.IntegerField()
    row = models.IntegerField()
    position = models.IntegerField()
    capacity = models.IntegerField()

    active = models.BooleanField(default=True)
    comment = models.TextField()

    rackID = models.ForeignKey(racks)

class clients(models.Model):
    class Meta:
        db_table = 'app_clients'

    name = models.TextField()  # client name
    bulstat = models.TextField(unique=True)
    # bulstat = models.TextField()
    mol = models.TextField()
    address = models.TextField()
    city = models.TextField()
    postcode = models.TextField()

    active = models.BooleanField(default=True)
    comment = models.TextField(blank=True, null=True)

class archiveUnitTypes(models.Model):
    class Meta:
        db_table = 'app_archiveunittypes'

    name = models.TextField()  # archiveUnitType name
    active = models.BooleanField(default=True)
    comment = models.TextField()

class projects(models.Model):
    class Meta:
        db_table = 'app_projects'

    name = models.TextField()  # project name

    active = models.BooleanField(default=True)
    comment = models.TextField()

    archiveUnitTypeID = models.ForeignKey(archiveUnitTypes)
    clientID = models.ForeignKey(clients)

class usersInfo(models.Model):
    '''
    #TODO: Legacy code ... to be removed
    '''
    class Meta:
        db_table = 'app_usersinfo'

    firstName = models.TextField()
    middleName = models.TextField()
    LastName = models.TextField()
    lastName_is_familyName = models.BooleanField(default=True)
    email = models.EmailField()

    active = models.BooleanField(default=False)
    comment = models.TextField()

    projectID = models.ForeignKey(projects, blank=True, null=True)  # 2,3,5,7 - projects ID

    def __unicode__(self):
        return self.firstName

class requestDatabases(models.Model):
    class Meta:
        db_table = 'app_requestdatabases'

    databaseName = models.FileField(upload_to="documents/%y%m%d")

    active = models.BooleanField(default=True)
    comment = models.TextField()

class boxes(models.Model):
    class Meta:
        db_table = 'app_boxes'

    startDate = models.DateField()

    expireDate = models.DateField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    databaseFileID = models.ForeignKey(requestDatabases,blank=True, null=True)
    projectID = models.ForeignKey(projects)
    placeID = models.ForeignKey(places,blank=True, null=True)

class archiveUnits(models.Model):
    class Meta:
        db_table = 'app_archiveunits'

    """
    Class that is responsible for populating the ClientRequests table - requests from the Client to add new boxes to the storage.

    status = {  - in-client             - the AthiveUnit is in the client or traveling to or from him;
                - in-warehouse          - the AthiveUnit is in warehouse
                - destroyed             - the AthiveUnit is disintegrated (destroyed) or wrongly inserted
             }
    """

    status = models.TextField()  # in storage; sent to client; disintegrated
    comment = models.TextField()
    dateDestroyed = models.DateField(blank=True, null=True)
    boxid = models.ForeignKey(boxes)

class criteriaTypes(models.Model):
    class Meta:
        db_table = 'app_criteriatypes'

    name = models.TextField()  # criteriaType name

    active = models.BooleanField(default=True)
    comment = models.TextField()

    projectID = models.ForeignKey(projects)

class criteria(models.Model):
    class Meta:
        db_table = 'app_criteria'

    value = models.TextField()

    active = models.BooleanField(default=True)
    comment = models.TextField()

    criteriaTypeID = models.ForeignKey(criteriaTypes)
    archiveUnitID = models.ForeignKey(archiveUnits, related_name = 'units')

class requestTypes(models.Model):
    class Meta:
        db_table = 'app_requesttypes'

    """This model holds the request type:
    name = { - new-boxes-request                    - user request for push new boxes to the warehouse;
             - unit-pull-request                    - user request to pull {Archive Units};
             - unit-return-request                  - user request to return {Archive Units};
             - boxes-destroy-request                - user request to destroy a box with units;
             - unit-destroy-request                 - user request to destroy a unit;

      """
    name = models.TextField()  # requestTypes name -
    active = models.BooleanField(default=False)
    comment = models.TextField()

class deliverTypes(models.Model):
    class Meta:
        db_table = 'app_delivertypes'

    """ This model holds the Delivery type choosen by the client:

        : standart
        : express
        : email
    """
    name = models.TextField()  # deliverTypes name
    active = models.BooleanField(default=False)
    comment = models.TextField()

class Images(models.Model):
    class Meta:
        db_table = 'app_images'

    fileLocation = models.FileField(upload_to="scanned_images", blank=True, null=True)
    active = models.BooleanField(default=True)
    comment = models.TextField(blank=True, null=True)
    class Meta:
        managed = True

class ClientRequests(models.Model):
    class Meta:
        db_table = 'app_clientrequests'

    """
    Class that is responsible for populating the ClientRequests table - requests from the Client to add new boxes to the storage.

    status = {  - waiting-push-operator             - the package is in the client and waiting for courier;
                - waiting_courier                   - the task is given to courier
                - waiting-pull-client               - waiting for the client to confirm his request
                - confirmed-by-pull-client          - the request order is confirmed by pull-client and waiting the operator to process
                - email-sent                        - the requested Object (email with a link for the image) is send to the client
                - at-client                         - the document is at the client
                - waiting-pull-operator             - waiting for the operator to confirm that the document is ready for logistics
                - in-warehouse                      - the courier delivered the package to the warehouse
                - waiting-return-client             - waiting for the client to confirm his request to return documents
                - waiting-return-operator           - waiting for operator's action
                - waiting-return-courier            - waiting for courier to deliver units
                - waiting-placement                 - waiting for storage operator to place the units in warehouse
                - cancel-pull-operator              - request canceled by operator
                - user-cancel                       - request canceled by client

                - waiting-destroy-client            - waiting for the client to confirm that the document have to be destroyed
                - confirmed-by-destroy-client       - the request order is confirmed by destroy-client and waiting the operator to process
                - waiting-destroy-operator          - waiting for the operator to confirm that the document is destroyed
                - destroyed                         - document/box is destroyed
                #TODO

            #TODO- for_digitalisation               - in Roni
    RELATED_NAME:
    You can override the FOO_set name by setting the related_name parameter in the ForeignKey definition.
    For example, if the Entry model was altered to blog = ForeignKey(Blog, related_name='entries'),
    the above example code would look like this:

    >>> b = Blog.objects.get(id=1)
    >>> b.entries.all() # Returns all Entry objects related to Blog.

    b.entries is a Manager that returns QuerySets.
    >>> b.entries.filter(headline__contains='Lennon')
    >>> b.entries.count()
    """
    # RequestDate = models.DateField(auto_now=True)
    RequestDate = models.DateField()
    PickupDate = models.DateField(blank=True, null=True)
    AcknowledgeDate = models.DateField(blank=True, null=True)
    DoneDate = models.DateField(blank=True, null=True)
    boxCount = models.IntegerField(default = 0)
    digitalisation = models.BooleanField(default=False)
    status = models.TextField()
    comment = models.TextField()
    clientName = models.TextField(blank=True, null=True)
    projectName = models.TextField(blank=True, null=True)
    imageHash = models.TextField(blank=True, null=True)

    deliverTypeID = models.ForeignKey(deliverTypes,blank=True, null=True)
    requestTypeID = models.ForeignKey(requestTypes,blank=True, null=True)
    archiveUnitID = models.ForeignKey(archiveUnits,blank=True, null=True)
    boxID = models.ForeignKey(boxes,blank=True, null=True)

    imageID = models.ForeignKey(Images, blank=True, null=True)


    userID = models.ForeignKey(User, related_name='user',default=None)
    operatorStartID = models.ForeignKey(User, related_name='operatorStart', default=None,blank=True, null=True)
    operatorFinishID = models.ForeignKey(User, related_name='operatorFinish', default=None,blank=True, null=True)

    def __unicode__(self):
        return self.projectName