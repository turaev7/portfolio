# Generated by Django 4.1.5 on 2023-02-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_photo', models.ImageField(upload_to='static/img')),
                ('blog_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.DateField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('email', models.CharField(max_length=30)),
                ('profile', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('about', models.TextField()),
                ('service_1', models.CharField(max_length=15)),
                ('service_1_info', models.CharField(blank=True, max_length=200, null=True)),
                ('service_2', models.CharField(max_length=15)),
                ('service_2_info', models.CharField(blank=True, max_length=200, null=True)),
                ('service_3', models.CharField(max_length=15)),
                ('service_3_info', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'My_info',
                'verbose_name_plural': 'My infos',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('p_photo', models.ImageField(upload_to='static/img')),
                ('p_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'My_Portfolio',
                'verbose_name_plural': 'My_Portfolios',
            },
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('works', models.IntegerField()),
                ('month_experience', models.IntegerField()),
                ('total_clients', models.IntegerField()),
                ('awards', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Total',
                'verbose_name_plural': 'Totals',
            },
        ),
    ]
