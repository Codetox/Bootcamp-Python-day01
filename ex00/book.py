import datetime
from recipe import Recipe


class Book:
    def __init__(self, name, update, date, recipes_list):
        self.name = name
        self.last_update = update
        self.creation_date = date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for types in self.recipes_list:
            for elem in self.recipes_list[types]:
                if name == elem.name:
                    print(str(elem))
                    return elem
        print("This recipe doesn't exist")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                print(recipe.name)
        else:
            print("This recipe_type is not available")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print("Only one recipe can be added")
