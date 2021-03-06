# Generated by Django 3.0.8 on 2020-07-16 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studyeng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название уровня')),
                ('code', models.IntegerField(verbose_name='код уровня')),
            ],
            options={
                'verbose_name': 'уровень',
                'verbose_name_plural': 'уровни',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название темы')),
                ('photo', models.ImageField(upload_to='themes')),
            ],
            options={
                'verbose_name': 'тема',
                'verbose_name_plural': 'темы',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='слово')),
                ('translation', models.CharField(max_length=50, verbose_name='перевод')),
                ('transcription', models.CharField(max_length=50, verbose_name='транскрипция')),
                ('example', models.TextField(max_length=200, verbose_name='пример')),
                ('sound', models.FileField(upload_to='sounds')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyeng.Theme', verbose_name='тема')),
            ],
            options={
                'verbose_name': 'тема',
                'verbose_name_plural': 'темы',
            },
        ),
        migrations.AddField(
            model_name='theme',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyeng.Category', verbose_name='категория'),
        ),
        migrations.AddField(
            model_name='theme',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyeng.Level', verbose_name='уровень'),
        ),
    ]
