import datetime


class Recipe:

    def __init__(self, name, lvl, time, ing, des, typ):
        self.name = name
        if 0 < lvl and lvl < 6:
            self.cooking_lvl = lvl
        else:
            print("{Level Error} (0 < lvl < 6)")
        if isinstance(time, int) and time >= 0:
            self.cooking_time = time
        else:
            print("{Time Error} (time >= 0)")
        if isinstance(ing, list) and all(isinstance(n, str) for n in ing):
            self.ingredients = ing
        else:
            print("{Ingredients Error} List of all"
                  "ingredients each represented by a string")
        if isinstance(des, str):
            self.description = des
        else:
            print("{Description Error} the description is only a string")
        if typ == "starter" or typ == "lunch" or typ == "dessert":
            self.recipe_type = typ
        else:
            print("{Recipe_type Error} Can be “starter”, “lunch” or “dessert”")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "name : {} \ntime: {} \ningredients: {} \n" \
              "description: {} \ntype: {}" \
            .format(self.name, self.cooking_time, self.ingredients,
                    self.description, self.recipe_type)
        return txt
