# Generated by Django 3.0.8 on 2020-07-31 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemCenter', '0003_submittedexams'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittedexams',
            name='user_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
