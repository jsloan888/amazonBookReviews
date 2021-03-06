# Generated by Django 2.2 on 2021-02-07 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=35)),
                ('l_name', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=75)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('liked_by', models.ManyToManyField(related_name='comments_liked', to='Book_review_apps.User')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_posted', to='Book_review_apps.User')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_comments', to='Book_review_apps.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(related_name='books_liked', to='Book_review_apps.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_posted', to='Book_review_apps.User'),
        ),
    ]
