# Generated by Django 3.2.6 on 2021-08-16 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakeorder',
            name='cake_selected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cakeorder', to='cake_api.displaycakes'),
        ),
        migrations.AlterField(
            model_name='displaycakes',
            name='cake_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='displaycakes', to='cake_api.cakevariety'),
        ),
    ]
