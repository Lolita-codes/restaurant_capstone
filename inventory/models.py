from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=150, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return f'name={self.name}; quantity={self.quantity}; unit={self.unit}; unit_price={self.unit_price}'

    def get_absolute_url(self):
        return '/ingredients'


class Menu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f'title={self.item}; price={self.price}'

    def get_absolute_url(self):
        return '/menu'

    def is_available(self):
        return all(X.enough() for X in self.recipe_set.all())


class Recipe(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f'menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}'

    def get_absolute_url(self):
        return '/menu'

    def is_enough(self):
        return self.quantity <= self.ingredient.quantity


class Purchases(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    purchased_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'menu_item=[{self.menu_item.__str__()}]; time={self.purchased_on}'

    def get_absolute_url(self):
        return '/purchases'
