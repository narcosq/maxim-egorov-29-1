# Generated by Django 4.2.2 on 2023-06-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_product_created_at_alter_product_modified_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='hashtag',
            field=models.ManyToManyField(to='posts.hashtag'),
        ),
    ]