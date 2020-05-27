import datetime
from book import Book
from recipe import Recipe

now = datetime.datetime.now()

sandwich = Recipe("sandwich", 1, 10, ["ham", "bread", "cheese", "tomatoes"],
                  "So good sandwich", "lunch")

cake = Recipe("cake", 3, 60, ["flour", "sugar", "eggs"],
              "Beautiful cake", "dessert")

cake2 = Recipe("cake2", 3, 60, ["flour", "sugar", "eggs"],
               "Beautiful cake", "dessert")

salad = Recipe("salad", 2, 15, ["avocado", "arugula", "tomatoes", "spinach"],
               "amazing salad", "lunch")

recipes_list = {
    "starter": [],
    "lunch": [sandwich, salad],
    "dessert": [cake],
}

book = Book("Cookbook", now, now, recipes_list)
book.get_recipe_by_name("cake")
book.get_recipes_by_types("lunch")
book.add_recipe(cake2)
book.get_recipes_by_types("dessert")
print(book.creation_date)
print(book.last_update)

# TEST ERROR

book.add_recipe("salut")
test = Recipe("salad", 10, 15, [], "", "lunch")
