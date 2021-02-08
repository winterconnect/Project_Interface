
# Generated by Django 3.1.5 on 2021-02-07 06:38


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(blank=True, max_length=200)),
                ('hashtag', models.CharField(blank=True, max_length=200)),
                ('like', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('memberPW', models.CharField(max_length=50)),
                ('memberName', models.CharField(max_length=20)),
                ('memberAge', models.DateField()),
                ('memberEmail', models.CharField(max_length=50)),
                ('adopterHouse', models.CharField(blank=True, max_length=200)),
                ('adopterAddress', models.CharField(blank=True, max_length=200)),
                ('adopterFamily', models.CharField(blank=True, max_length=200)),
                ('authority', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petName', models.CharField(blank=True, max_length=50)),
                ('petBirth', models.DateField(blank=True, null=True)),
                ('petSex', models.NullBooleanField()),
                ('petSize', models.CharField(blank=True, max_length=50)),
                ('petLoc', models.CharField(blank=True, max_length=50)),
                ('petSpecies', models.CharField(blank=True, max_length=50)),
                ('petWeight', models.FloatField(blank=True, null=True)),
                ('petNeuter', models.NullBooleanField()),
                ('petColor', models.CharField(blank=True, max_length=50)),
                ('petImage', models.ImageField(upload_to='images/')),
                ('petAdoption', models.BooleanField(default=False)),
                ('memberID', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.SET_DEFAULT, to='yyApp.member')),
                ('postID', models.OneToOneField(default=' ', on_delete=django.db.models.deletion.SET_DEFAULT, to='yyApp.board')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=4000)),
                ('memberID', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.SET_DEFAULT, to='yyApp.member')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yyApp.board')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='memberID',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.SET_DEFAULT, to='yyApp.member'),
        ),
    ]
