# Generated by Django 4.1.7 on 2023-07-04 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=35)),
                ('category', models.CharField(choices=[('----------', '----------'), ('Anthropology', 'Anthropology'), ('Architecture', 'Architecture'), ('Art', 'Art'), ('Biology', 'Biology'), ('Business Administration', 'Business Administration'), ('Chemistry', 'Chemistry'), ('Communication', 'Communication'), ('Computer Science', 'Computer Science'), ('Criminal Justice', 'Criminal Justice'), ('Dance', 'Dance'), ('Economics', 'Economics'), ('Education', 'Education'), ('Engineering', 'Engineering'), ('English', 'English'), ('Environmental Science', 'Environmental Science'), ('Film Studies', 'Film Studies'), ('Food Science', 'Food Science'), ('Geology', 'Geology'), ('Graphic Design', 'Graphic Design'), ('History', 'History'), ('Information Technology', 'Information Technology'), ('International Relations', 'International Relations'), ('Journalism', 'Journalism'), ('Kinesiology', 'Kinesiology'), ('Linguistics', 'Linguistics'), ('Marketing', 'Marketing'), ('Mathematics', 'Mathematics'), ('Music', 'Music'), ('Nursing', 'Nursing'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Public Health', 'Public Health'), ('Religious Studies', 'Religious Studies'), ('Social Work', 'Social Work'), ('Sociology', 'Sociology'), ('Theater', 'Theater')], default='----------', max_length=25)),
                ('itemPhoto', models.ImageField(blank=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]