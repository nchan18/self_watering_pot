import os
import random
import json
def create_json_parameter_file(self,plant_name):
        #for each plant, create a json file with the parameters and add it to the dictionary
        read_filepath = "../parameters/plant_parameters.json"
        save_filepath = "../parameters/plants_in_pot_parameters.json"
        plant_parameters_list = json.load(open(read_filepath))
        plant_parameters = {plant: params for d in plant_parameters_list for plant, params in d.items()}

        if not os.path.exists(save_filepath):
            pot_parameters = []
            for plant in plant_name:
                parameters = { plant : plant_parameters[plant] }
                pot_parameters.append(parameters)
        with open(save_filepath, "w") as file:
            file.write(json.dumps(pot_parameters))
filepath = "../parameters/plant_parameters.txt"
plant_name = ['Apple','Apricot','Avocado','Banana','Blackberry','Blueberry','Boysenberry','Cantaloupe','Cherry','Clementine','Coconut','Cranberry','Date','Dragonfruit','Elderberry','Fig','Grape','Grapefruit','Guava','Honeydew','Kiwi','Kumquat','Lemon','Lime','Lychee','Mango','Mulberry','Nectarine','Orange','Papaya','Passion Fruit','Peach','Pear','Pineapple','Plum','Pomegranate','Raspberry','Red Currant','Starfruit','Strawberry','Tangerine','Ugli Fruit','Watermelon','White Currant','White Sapote','Yellow Watermelon','Yuzu','Zucchini (Courgette)','Quince','Persimmon','Artichoke','Arugula','Asparagus','Beetroot','Bell Pepper','Black-eyed Peas','Broccoli','Brussels Sprouts','Cabbage','Carrot','Cauliflower','Celery','Chard','Collards','Corn','Cucumber','Eggplant','Fennel','Garlic','Green Beans','Kale','Leek','Lettuce','Mushroom','Mustard Greens','Okra','Onion','Parsnip','Pea','Potato','Pumpkin','Radish','Rhubarb','Rutabaga','Spinach','Squash','Sweet Potato','Tomato','Turnip','Watercress','Yam','Zucchini','Acorn Squash','Butternut Squash','Chayote','Chicory','Daikon','Endive','Kohlrabi','Parsley Root']
# if not os.path.exists(filepath):
#     parameters_list = []
#     for plant in plant_name:
#         min_temp = random.randint(0, 20)
#         max_temp = random.randint(80, 110)
#         min_humid = random.randint(0, 50)
#         max_humid = random.randint(50,100)
#         min_water = random.randint(0, 20)
#         max_water = random.randint(20, 40)
#         target_soil_moisture = random.randint(0, 20)


#         # Create a dictionary
#         plant_parameters = {
#             plant:{
#                 "minimum_temp": min_temp,
#                 "maximum_temp": max_temp,
#                 "minimum_humidity": min_humid,
#                 "maximum_humidity": max_humid,
#                 "minimum_water": min_water,
#                 "maximum_water": max_water,
#                 "target_soil_moisture": target_soil_moisture
#             }
#         }
#         parameters_list.append(plant_parameters)
#     with open(filepath, "w") as file:
#         file.write(json.dumps(parameters_list))
plant_name = ['Apple','Apricot','Lemon','Starfruit','Black-eyed Peas','Eggplant','Squash','Sweet Potato','Tomato','Turnip']
create_json_parameter_file(filepath,plant_name)
