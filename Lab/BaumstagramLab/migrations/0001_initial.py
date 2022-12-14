# Generated by Django 4.1.1 on 2022-10-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('idaccounts', models.AutoField(db_column='idAccounts', primary_key=True, serialize=False)),
                ('followerscount', models.IntegerField(db_column='FollowersCount')),
            ],
            options={
                'db_table': 'accounts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('idphoto', models.AutoField(db_column='idPhoto', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=45)),
                ('path', models.CharField(db_column='Path', max_length=45)),
                ('date', models.DateField(db_column='Date')),
                ('description', models.CharField(blank=True, db_column='Description', max_length=100, null=True)),
            ],
            options={
                'db_table': 'photos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('iduser', models.AutoField(db_column='idUser', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('surname', models.CharField(db_column='Surname', max_length=45)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=45, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
