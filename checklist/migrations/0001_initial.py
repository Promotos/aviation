# Generated by Django 4.2.5 on 2024-11-05 20:29

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
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Der Name des Flugzeugs.', max_length=50)),
                ('callsign', models.CharField(help_text='Das Flugzeug Callsign.', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name der Checkliste.', max_length=50)),
                ('airplain', models.ForeignKey(help_text='Für welches Flugzeug diese Checkliste gilt.', on_delete=django.db.models.deletion.CASCADE, to='checklist.airplane')),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistItemGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name der Gruppe.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Der Name des Vereins.', max_length=50)),
                ('users', models.ManyToManyField(help_text='Mitglieder des Vereins.', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='Legt die Reihenfolge fest.')),
                ('name', models.CharField(help_text="Name des Eintrags. Bsp. 'Rettungsgerät gesichert.'", max_length=100)),
                ('description', models.TextField(blank=True, help_text='Beschreibung des Eintrags.', max_length=500)),
                ('hint', models.TextField(blank=True, help_text='Hilfestellung für diesen Eintrag', max_length=500)),
                ('checklist', models.ForeignKey(help_text='Zu welcher Checkliste dieser Eintrag gehört.', on_delete=django.db.models.deletion.CASCADE, to='checklist.checklist')),
                ('group', models.ForeignKey(help_text='Gruppe des Eintrags.', on_delete=django.db.models.deletion.CASCADE, to='checklist.checklistitemgroup')),
            ],
        ),
        migrations.AddField(
            model_name='airplane',
            name='clubs',
            field=models.ManyToManyField(help_text='Zu welchem Verein dieses Flugzeug gehört.', to='checklist.club'),
        ),
    ]
