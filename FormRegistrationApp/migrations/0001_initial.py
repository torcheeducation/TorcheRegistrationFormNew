# Generated by Django 3.1.1 on 2022-09-15 07:00

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_code', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_invoice', models.CharField(max_length=254, unique=True)),
                ('tanggal', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('nama_lengkap', models.CharField(max_length=254)),
                ('nomor_telefon', models.CharField(max_length=254)),
                ('program_studi', models.CharField(max_length=254)),
                ('universitas', models.CharField(max_length=254)),
                ('informasi_mengenai_torche', models.CharField(max_length=254)),
                ('metode_pembelajaran', models.CharField(max_length=254)),
                ('mata_kuliah', models.CharField(max_length=254)),
                ('materi', models.CharField(max_length=5000)),
                ('aplikasi_simulasi', models.CharField(max_length=254)),
                ('jumlah_sesi_yang_diikuti', models.CharField(max_length=254)),
                ('jumlah_peserta', models.CharField(max_length=10)),
                ('lampiran_file_siswa', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(permissions=(gdstorage.storage.GoogleDriveFilePermission(gdstorage.storage.GoogleDrivePermissionRole['READER'], gdstorage.storage.GoogleDrivePermissionType['USER'], 'regiapriandi012@gmail.com'),)), upload_to='TorcheData/')),
                ('lampiran_invoice', models.URLField(max_length=1000)),
                ('lampiran_invoice_assignment', models.URLField(max_length=1000)),
                ('sesi_hari', models.CharField(max_length=254)),
                ('sesi_jam', models.CharField(max_length=254)),
                ('biaya', models.CharField(max_length=254)),
                ('notes_for_tutor', models.CharField(max_length=5000)),
                ('referral_code', models.CharField(max_length=254)),
                ('email_anggota_1', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_1', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_1', models.CharField(max_length=1000)),
                ('akun_discord_anggota_1', models.CharField(max_length=1000)),
                ('email_anggota_2', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_2', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_2', models.CharField(max_length=1000)),
                ('akun_discord_anggota_2', models.CharField(max_length=1000)),
                ('email_anggota_3', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_3', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_3', models.CharField(max_length=1000)),
                ('akun_discord_anggota_3', models.CharField(max_length=1000)),
                ('email_anggota_4', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_4', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_4', models.CharField(max_length=1000)),
                ('akun_discord_anggota_4', models.CharField(max_length=1000)),
                ('email_anggota_5', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_5', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_5', models.CharField(max_length=1000)),
                ('akun_discord_anggota_5', models.CharField(max_length=1000)),
                ('email_anggota_6', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_6', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_6', models.CharField(max_length=1000)),
                ('akun_discord_anggota_6', models.CharField(max_length=1000)),
                ('email_anggota_7', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_7', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_7', models.CharField(max_length=1000)),
                ('akun_discord_anggota_7', models.CharField(max_length=1000)),
                ('email_anggota_8', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_8', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_8', models.CharField(max_length=1000)),
                ('akun_discord_anggota_8', models.CharField(max_length=1000)),
                ('email_anggota_9', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_9', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_9', models.CharField(max_length=1000)),
                ('akun_discord_anggota_9', models.CharField(max_length=1000)),
                ('email_anggota_10', models.CharField(max_length=1000)),
                ('nama_lengkap_anggota_10', models.CharField(max_length=1000)),
                ('nomor_telefon_anggota_10', models.CharField(max_length=1000)),
                ('akun_discord_anggota_10', models.CharField(max_length=1000)),
            ],
        ),
    ]
