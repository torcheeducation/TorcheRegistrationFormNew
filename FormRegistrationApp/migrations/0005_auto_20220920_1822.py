# Generated by Django 3.1.1 on 2022-09-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormRegistrationApp', '0004_auto_20220915_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationdata',
            old_name='lampiran_invoice_assignment',
            new_name='lampiran_surat_tugas',
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='informasi_mengenai_torche',
            field=models.CharField(max_length=500),
        ),
    ]