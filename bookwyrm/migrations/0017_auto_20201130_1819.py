# Generated by Django 3.0.7 on 2020-11-30 18:19

import bookwyrm.models.base_model
import bookwyrm.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def copy_rsa_keys(app_registry, schema_editor):
    db_alias = schema_editor.connection.alias
    users = app_registry.get_model('bookwyrm', 'User')
    keypair = app_registry.get_model('bookwyrm', 'KeyPair')
    for user in users.objects.using(db_alias):
        if user.public_key or user.private_key:
            user.key_pair = keypair.objects.create(
                private_key=user.private_key,
                public_key=user.public_key
            )
            user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0016_auto_20201129_0304'),
    ]
    operations = [
        migrations.CreateModel(
            name='KeyPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('remote_id', bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id])),
                ('private_key', models.TextField(blank=True, null=True)),
                ('public_key', bookwyrm.models.fields.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(bookwyrm.models.base_model.ActivitypubMixin, models.Model),
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=bookwyrm.models.fields.ManyToManyField(related_name='following', through='bookwyrm.UserFollows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='book',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='connector',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='federatedserver',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='image',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='readthrough',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='shelf',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='shelfbook',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='status',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='tag',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=bookwyrm.models.fields.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bookwyrm_user',
            field=bookwyrm.models.fields.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='inbox',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, unique=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='user',
            name='local',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='manually_approves_followers',
            field=bookwyrm.models.fields.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=bookwyrm.models.fields.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='outbox',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, unique=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='user',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, unique=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='user',
            name='shared_inbox',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='user',
            name='summary',
            field=bookwyrm.models.fields.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=bookwyrm.models.fields.UsernameField(),
        ),
        migrations.AlterField(
            model_name='userblocks',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='userfollowrequest',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='userfollows',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AlterField(
            model_name='usertag',
            name='remote_id',
            field=bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id]),
        ),
        migrations.AddField(
            model_name='user',
            name='key_pair',
            field=bookwyrm.models.fields.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='bookwyrm.KeyPair'),
        ),
        migrations.RunPython(copy_rsa_keys),
    ]
