# Generated by Django 3.2.6 on 2021-08-06 21:05

from django.db import migrations
from .. import data
class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0001_initial'),
    ]
    def getProductDetails(apps,schema_editor):
        Product=apps.get_model('homePage','allProducts')
        url="https://www.amazon.in/s?bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc"
        soup=data.getData(url)
        productList=data.findE(soup)
        for product in productList:
            product=Product(product_name=product.name,product_price=product.price,product_rating=product.rating)
            product.save()
    operations = [
        migrations.RunPython(getProductDetails),
    ]