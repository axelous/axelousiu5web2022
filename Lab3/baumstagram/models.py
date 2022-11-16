from django.db import models

class Accounts(models.Model):
    idaccounts = models.AutoField(db_column='idAccounts', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    idphoto = models.ForeignKey('Photos', models.DO_NOTHING, db_column='idPhoto')  # Field name made lowercase.
    followerscount = models.IntegerField(db_column='FollowersCount')  # Field name made lowercase.

class Photos(models.Model):
    idphoto = models.AutoField(db_column='idPhoto', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=45)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=45)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.

class Users(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.

