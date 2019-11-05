# Generated by Django 2.2.6 on 2019-11-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('Note', models.TextField()),
                ('Publisher', models.CharField(max_length=200)),
                ('Issued_to', models.CharField(max_length=200)),
                ('book_code', models.CharField(max_length=200)),
                ('Isuued_date', models.DateField(blank=True, null=True)),
                ('Return_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]