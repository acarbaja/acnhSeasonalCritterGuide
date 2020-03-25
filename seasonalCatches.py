# -*- coding: utf-8 -*-
import json
import sys

# Hershel Carbajal-Rodriguez
# 02-24-2020
# This file is used to process bug/fish dictionaries
# by changing the month numbers (0 indexed) into abbreviations.
# This file was supposed to be called in the insert.php file
# but due to some restrictions, I just copy/pasted my results over
# to the appropriate php files.

months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"];

#north
#bugs = {'Fly': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 60, 'location': 'On rotten fruit or garbage', 'time': 'All day'}, 'Rosalia Batsei Beetle': {'season': [4, 5], 'price': 3000, 'location': 'Tree stump', 'time': 'All day'}, 'Bagworm': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 600, 'location': 'Shake tree', 'time': 'All day'}, 'Scorpion': {'season': [4, 5, 6, 7, 8, 9], 'price': 8000, 'location': 'Ground', 'time': '6 PM - 5 AM'}, 'Paper Kite Butterfly': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1000, 'location': 'Flying', 'time': '8 AM - 7 PM'}, 'Mole Cricket': {'season': [10, 11, 0, 1, 2, 3, 4], 'price': 500, 'location': 'Underground', 'time': 'All day'}, 'Emperor Butterfly': {'season': [11, 0, 1, 2, 5, 6, 7, 8], 'price': 4000, 'location': 'Flying', 'time': '5 PM - 8 AM'}, 'Tarantula': {'season': [10, 11, 0, 1, 2, 3], 'price': 8000, 'location': 'Ground', 'time': '7 PM - 4 AM'}, 'Honeybee': {'season': [2, 3, 4, 5, 6], 'price': 200, 'location': 'Near flowers', 'time': '8 AM - 5 PM'}, 'Man-Faced Stink Bug': {'season': [2, 3, 4, 5, 6, 7, 8, 9], 'price': 1000, 'location': 'Flowers', 'time': '7 PM - 8 AM'}, 'Hermit Crab': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1000, 'location': 'Beach', 'time': '7 PM - 8 AM'}, 'Ladybug': {'season': [2, 3, 4, 5, 9], 'price': 200, 'location': 'Flowers', 'time': '8AM - 5PM'}, 'Cricket': {'season': [8, 9, 10], 'price': 130, 'location': 'Ground', 'time': '5 PM - 8 AM'}, 'Citrus Long-Horned Beetle': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 350, 'location': 'Tree stump', 'time': 'All day'}, 'Red Dragonfly': {'season': [8, 9], 'price': 180, 'location': 'Flying', 'time': '8 AM - 7 PM'}, 'Snail': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 250, 'location': 'Rock (rain)', 'time': 'All day'}, 'Violin Beetle': {'season': [4, 5, 8, 9, 10], 'price': 450, 'location': 'Tree stump', 'time': 'All day'}, 'Madagascan Sunset Moth': {'season': [3, 4, 5, 6, 7, 8], 'price': 2500, 'location': 'Flying', 'time': '8 AM - 4 PM'}, 'Monarch Butterfly': {'season': [8, 9, 10], 'price': 140, 'location': 'Flying', 'time': '4 AM - 5 PM'}, 'Earth-Boring Dung Beetle': {'season': [6, 7, 8], 'price': 300, 'location': 'Ground', 'time': 'All day'}, 'Wharf Roach': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 200, 'location': 'Beach (rocks)', 'time': 'All day'}, 'Flea': {'season': [3, 4, 5, 6, 7, 8, 9, 10], 'price': 70, 'location': 'On a flea-infested villager', 'time': 'All day'}, 'Peacock Butterfly': {'season': [2, 3, 4, 5], 'price': 2500, 'location': 'Near black, blue, or purple flowers', 'time': '4 AM - 7 PM'}, 'Common Butterfly': {'season': [8, 9, 10, 11, 0, 1, 2, 3, 4, 5], 'price': 160, 'location': 'Flying', 'time': '4 AM - 7 PM'}, 'Stinkbug': {'season': [2, 3, 4, 5, 6, 7, 8, 9], 'price': 120, 'location': 'Flowers', 'time': 'All day'}, 'Agris Butterfly': {'season': [3, 4, 5, 6, 7, 8], 'price': 3000, 'location': 'Flying', 'time': '8 AM - 5 PM'}, 'Rainbow Stag': {'season': [5, 6, 7, 8], 'price': 6000, 'location': 'Tree', 'time': '7 PM - 8 AM'}, 'Yellow Butterfly': {'season': [2, 3, 4, 5, 8, 9], 'price': 160, 'location': 'Flying', 'time': '4 AM - 7 PM'}, 'Darner Dragonfly': {'season': [3, 4, 5, 6, 7, 8, 9], 'price': 230, 'location': 'Flying', 'time': '8 AM - 5 PM'}, 'Walker Cicada': {'season': [7, 8], 'price': 400, 'location': 'Tree', 'time': '8 AM - 4 PM'}, 'Mantis': {'season': [2, 3, 4, 5, 6, 7, 8, 9, 10], 'price': 430, 'location': 'Flowers', 'time': '8 AM - 5 PM'}, 'Pondskater': {'season': [4, 5, 6, 7, 8], 'price': 130, 'location': 'River', 'time': '8 AM - 7 PM'}, 'Migratory Locust': {'season': [1, 2, 3, 4], 'price': 200, 'location': 'Ground', 'time': '8 AM - 7 PM'}, 'Centipede': {'season': [8, 9, 10, 11, 0, 1, 2, 3, 4, 5], 'price': 430, 'location': 'Hit rocks', 'time': '5 PM - 11 PM'}, 'Mosquito': {'season': [5, 6, 7, 8], 'price': 130, 'location': 'Flying', 'time': '5 PM - 4 AM'}, 'Rajah Brooke\xe2\x80\x99s Birdwing': {'season': [11, 0, 1, 3, 4, 5, 6, 7, 8], 'price': 2500, 'location': 'Near black, blue, or purple flowers', 'time': '8 AM - 5 PM'}, 'Orchid Mantis': {'season': [2, 3, 4, 5, 6, 7, 8, 9, 10], 'price': 2400, 'location': 'Flowers', 'time': '8 AM - 5 PM'}, 'Pill Bug': {'season': [8, 9, 10, 11, 0, 1, 2, 3, 4, 5], 'price': 250, 'location': 'Hit rocks', 'time': '11 PM - 4 PM'}, 'Damselfly': {'season': [10, 11, 0, 1], 'price': 500, 'location': 'Flying', 'time': 'All day'}, 'Queen Alexandra\xe2\x80\x99s Birdwing': {'season': [4, 5, 6, 7, 8], 'price': 4000, 'location': 'Flying', 'time': '8 AM - 4 PM'}, 'Moth': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 130, 'location': 'Lit windows', 'time': '7 PM - 4 AM'}, 'Wasp': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 2500, 'location': 'Shake tree', 'time': 'All day'}, 'Grasshopper': {'season': [6, 7, 8], 'price': 160, 'location': 'Ground', 'time': '8 AM - 5 PM'}, 'Spider': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 600, 'location': 'Shake tree', 'time': '7 PM - 8 AM'}, 'Tiger Butterfly': {'season': [2, 3, 4, 5, 6, 7, 8], 'price': 240, 'location': 'Flying', 'time': '4 AM - 7 PM'}, 'Ant': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 80, 'location': 'On rotten fruit and turnips', 'time': 'All day'}, 'Diving Beetle': {'season': [4, 5, 6, 7, 8], 'price': 800, 'location': 'River', 'time': '8 AM - 7 PM'}, 'Dung Beetle': {'season': [11, 0, 1], 'price': 2500, 'location': 'Snowballs', 'time': 'All day'}, 'Walking Leaf': {'season': [6, 7, 8], 'price': 600, 'location': 'Ground', 'time': 'All day'}, 'Tiger Beetle': {'season': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'price': 1500, 'location': 'Ground', 'time': 'All day'}, 'Long Locust': {'season': [3, 4, 5, 6, 7, 8, 9, 10], 'price': 200, 'location': 'Ground', 'time': '8 AM - 7 PM'}};
#south
bugs = {'Fly': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 60, 'location': 'On rotten fruit or garbage', 'time': 'All day'}, 'Rosalia Batsei Beetle': {'season': [10, 11], 'price': 3000, 'location': 'Tree stump', 'time': 'All day'}, 'Bagworm': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 600, 'location': 'Shake tree', 'time': 'All day'}, 'Scorpion': {'season': [10, 11, 0, 1, 2, 3], 'price': 8000, 'location': 'Ground', 'time': '7 PM - 4 AM'}, 'Paper Kite Butterfly': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1000, 'location': 'Flying', 'time': '8 AM - 7 PM'}, 'Mole Cricket': {'season': [4, 5, 6, 7, 8, 9, 10], 'price': 500, 'location': 'Underground', 'time': 'All day'}, 'Emperor Butterfly': {'season': [11, 0, 1, 2, 5, 6, 7, 8], 'price': 4000, 'location': 'Flying', 'time': '5 PM - 8 AM'}, 'Tarantula': {'season': [4, 5, 6, 7, 8, 9], 'price': 8000, 'location': 'Ground', 'time': '7 PM - 4 AM'}, 'Honeybee': {'season': [8, 9, 10, 11, 0], 'price': 200, 'location': 'Near flowers', 'time': '8 AM - 5 PM'}, 'Man-Faced Stink Bug': {'season': [8, 9, 10, 11, 0, 1, 2, 3], 'price': 1000, 'location': 'Flowers', 'time': '7 PM - 8 AM'}, 'Hermit Crab': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1000, 'location': 'Beach', 'time': '7 PM - 8 AM'}, 'Ladybug': {'season': [3, 8, 9, 10, 11], 'price': 200, 'location': 'Flowers', 'time': '8 AM - 5 PM'}, 'Cricket': {'season': [2, 3, 4], 'price': 130, 'location': 'Ground', 'time': '5 PM - 8 AM'}, 'Citrus Long-Horned Beetle': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 350, 'location': 'Tree stump', 'time': 'All day'}, 'Red Dragonfly': {'season': [2, 3], 'price': 180, 'location': 'Flying', 'time': '8 AM - 7 PM'}, 'Snail': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 250, 'location': 'Rock (rain)', 'time': 'All day'}, 'Atlas Moth': {'season': [9, 10, 11, 0, 1, 2], 'price': 3000, 'location': 'Tree', 'time': '7 PM - 4 AM'}, 'Madagascan Sunset Moth': {'season': [9, 10, 11, 0, 1, 2], 'price': 2500, 'location': 'Flying', 'time': '8 AM - 4 PM'}, 'Monarch Butterfly': {'season': [2, 3, 4], 'price': 140, 'location': 'Flying', 'time': '4 AM - 5 PM'}, 'Earth-Boring Dung Beetle': {'season': [0, 1, 2], 'price': 300, 'location': 'Ground', 'time': 'All day'}, 'Wharf Roach': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 200, 'location': 'Beach (rocks)', 'time': 'All day'}, 'Violin Beetle': {'season': [2, 3, 4, 10, 11], 'price': 450, 'location': 'Tree stump', 'time': 'All day'}, 'Flea': {'season': [9, 10, 11, 0, 1, 2, 3, 4], 'price': 70, 'location': 'On a flea-infested Villager', 'time': 'All day'}, 'Peacock Butterfly': {'season': [8, 9, 10, 11], 'price': 2500, 'location': 'Near black, blue, or purple flowers', 'time': '4 AM - 7 PM'}, 'Common Butterfly': {'season': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 160, 'location': 'Flying', 'time': '4 AM - 7PM'}, 'Stinkbug': {'season': [8, 9, 10, 11, 0, 1, 2, 3], 'price': 120, 'location': 'Flowers', 'time': 'All day'}, 'Agris Butterfly': {'season': [9, 10, 11, 0, 1, 2], 'price': 3000, 'location': 'Flying', 'time': '8 AM - 5 PM'}, 'Rainbow Stag': {'season': [11, 0, 1, 2], 'price': 6000, 'location': 'Tree', 'time': '7 PM - 8 AM'}, 'Yellow Butterfly': {'season': [2, 3, 8, 9, 10, 11], 'price': 160, 'location': 'Flying', 'time': '4 AM - 7 PM'}, 'Darner Dragonfly': {'season': [9, 10, 11, 0, 1, 2, 3], 'price': 230, 'location': 'Flying', 'time': '8 AM - 5 PM'}, 'Walker Cicada': {'season': [1, 2], 'price': 400, 'location': 'Tree', 'time': '8 AM - 4 PM'}, 'Mantis': {'season': [8, 9, 10, 11, 0, 1, 2, 3], 'price': 430, 'location': 'Flowers', 'time': '8 AM - 5 PM'}, 'Pondskater': {'season': [10, 11, 0, 1, 2], 'price': 130, 'location': 'River', 'time': '8 AM - 7 PM'}, 'Migratory Locust': {'season': [1, 2, 3, 4], 'price': 200, 'location': 'Ground', 'time': '8 AM - 7 PM'}, 'Centipede': {'season': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 430, 'location': 'Hit rocks', 'time': 'All day'}, 'Mosquito': {'season': [11, 0, 1, 2], 'price': 130, 'location': 'Flying', 'time': '5 PM - 4 AM'}, 'Walking Stick': {'season': [0, 1, 2, 3, 4], 'price': 600, 'location': 'Tree', 'time': '4 AM - 8 PM, 4 PM - 8 AM'}, 'Rajah Brooke\xe2\x80\x99s Birdwing': {'season': [5, 6, 7, 9, 10, 11, 0, 1, 2], 'price': 2500, 'location': 'Near black, blue, or purple flowers', 'time': '8 AM - 5 PM'}, 'Orchid Mantis': {'season': [8, 9, 10, 11, 0, 1, 2, 3, 4], 'price': 2400, 'location': 'Flowers', 'time': '8 AM - 5 PM'}, 'Pill Bug': {'season': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 250, 'location': 'Hit rocks', 'time': '11 PM - 4 PM'}, 'Damselfly': {'season': [4, 5, 6, 7], 'price': 500, 'location': 'Flying', 'time': 'All day'}, 'Queen Alexandra\xe2\x80\x99s Birdwing': {'season': [10, 11, 0, 1, 2], 'price': 4000, 'location': 'Flying', 'time': '8 AM - 4 PM'}, 'Moth': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 130, 'location': 'Lit windows', 'time': '7 PM - 4 AM'}, 'Wasp': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 2500, 'location': 'Shake Tree', 'time': 'All day'}, 'Grasshopper': {'season': [0, 1, 2], 'price': 160, 'location': 'Ground', 'time': '8 AM - 5 PM'}, 'Spider': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 600, 'location': 'Shake tree', 'time': '7 PM - 8 AM'}, 'Tiger Butterfly': {'season': [8, 9, 10, 11, 0, 1, 2], 'price': 240, 'location': 'Flying', 'time': '4 AM - 7 PM'}, 'Ant': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 80, 'location': 'Rotten fruit or turnips', 'time': 'All day'}, 'Diving Beetle': {'season': [10, 11, 0, 1, 2], 'price': 800, 'location': 'River', 'time': '8 AM - 7 PM'}, 'Dung Beetle': {'season': [5, 6, 7], 'price': 2500, 'location': 'Snowballs', 'time': 'All day'}, 'Walking Leaf': {'season': [0, 1, 2], 'price': 600, 'location': 'Ground', 'time': 'All day'}, 'Tiger Beetle': {'season': [7, 8, 9, 10, 11, 0, 1, 2, 3], 'price': 1500, 'location': 'Ground', 'time': 'All day'}, 'Long Locust': {'season': [9, 10, 11, 0, 1, 2, 3, 4], 'price': 200, 'location': 'Ground', 'time': '8 AM - 7 PM'}};

#north
#fish = {'Koi': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 4000, 'shadow': 'Large', 'location': 'Pond', 'time': '4 PM - 9 AM'}, 'Pond Smelt': {'season': [11, 0, 1], 'price': ' ', 'shadow': 'Small', 'location': 'River', 'time': 'All day'}, 'Suckerfish': {'season': [5, 6, 7, 8], 'price': 1500, 'shadow': '(Fin)', 'location': 'Ocean', 'time': 'All day'}, 'Loach': {'season': [2, 3, 4], 'price': 400, 'shadow': 'Small', 'location': 'River', 'time': 'All day'}, 'Horse Mackerel': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 150, 'shadow': 'Small', 'location': 'Ocean', 'time': 'All day'}, 'Mahi-mahi': {'season': [4, 5, 6, 7, 8, 9], 'price': 6000, 'shadow': 'Large', 'location': 'Ocean', 'time': 'All day'}, 'Crawfish': {'season': [3, 4, 5, 6, 7, 8], 'price': 200, 'shadow': 'Medium', 'location': 'Pond', 'time': 'All day'}, 'Coelacanth': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 15000, 'shadow': 'Largest', 'location': 'Sea (rainy days)', 'time': 'All day'}, 'Frog': {'season': [4, 5, 6, 7], 'price': ' ', 'shadow': 'Small', 'location': 'Pond', 'time': 'All day'}, 'Tadpole': {'season': [2, 3, 4, 5, 6], 'price': 100, 'shadow': 'Smallest', 'location': 'Pond', 'time': 'All day'}, 'Surgeonfish': {'season': [3, 4, 5, 6, 7, 8], 'price': 1000, 'shadow': 'Small', 'location': 'Ocean', 'time': 'All day'}, 'Catfish': {'season': [4, 5, 6, 7, 8, 9], 'price': 800, 'shadow': '', 'location': 'Pond', 'time': '4 PM - 9 AM'}, 'Salmon': {'season': [8], 'price': 700, 'shadow': 'Small', 'location': 'River (mouth)', 'time': 'All day'}, 'Bluegill': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 180, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Mitten Crab': {'season': [8, 9, 10], 'price': 2000, 'shadow': 'Small', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Soft-shelled Turtle': {'season': [7, 8], 'price': 3750, 'shadow': '', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Saw Shark': {'season': [5, 6, 7, 8], 'price': 12000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Snapping Turtle': {'season': [3, 4, 5, 6, 7, 8, 9], 'price': 5000, 'shadow': '', 'location': 'River', 'time': '9 AM - 4 AM'}, 'Clown Fish': {'season': [3, 4, 5, 6, 7, 8], 'price': 650, 'shadow': 'Smallest', 'location': 'Ocean', 'time': 'All day'}, 'Anchovy': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 200, 'shadow': 'Small', 'location': 'Ocean', 'time': '4 AM - 9 PM'}, 'Arowana': {'season': [5, 6, 7, 8], 'price': 10000, 'shadow': 'Large', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Dab': {'season': [9, 10, 11, 0, 1, 2, 3], 'price': 300, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Saddled Bichir': {'season': [11, 0, 1, 2], 'price': 4000, 'shadow': 'Large', 'location': 'River', 'time': '9 PM - 4 AM'}, 'Carp': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 300, 'shadow': 'Large', 'location': 'Pond', 'time': 'All day'}, 'Killifish': {'season': [3, 4, 5, 6, 7], 'price': 300, 'shadow': 'Smallest', 'location': 'Pond', 'time': 'All day'}, 'Barred Knifejaw': {'season': [2, 3, 4, 5, 6, 7, 8, 9, 10], 'price': 5000, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Gar': {'season': [6, 7, 8, 9], 'price': 6000, 'shadow': 'Largest', 'location': 'Pond', 'time': '4 PM - 9 AM'}, 'Ocean Sunfish': {'season': [6, 7, 8], 'price': 4000, 'shadow': '(Fin)', 'location': 'Ocean', 'time': '4 AM - 9 PM'}, 'Ribbon Eel': {'season': [5, 6, 7, 8, 9], 'price': 600, 'shadow': 'Narrow', 'location': 'Ocean', 'time': 'All day'}, 'Black Bass': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 400, 'shadow': 'Large', 'location': 'River', 'time': 'All day'}, 'Sea Butterfly': {'season': [11, 0, 1, 2], 'price': 1000, 'shadow': 'Smallest', 'location': 'Ocean', 'time': 'All day'}, 'Whale Shark': {'season': [5, 6, 7, 8], 'price': 13000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': 'All day'}, 'Dorado': {'season': [5, 6, 7, 8], 'price': 15000, 'shadow': 'X Large', 'location': 'River', 'time': '4 a.m - 9 PM'}, 'Goldfish': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1300, 'shadow': 'Smallest', 'location': 'Pond', 'time': 'All day'}, 'Pop-eyed Goldfish': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1300, 'shadow': 'Smallest', 'location': 'Pond', 'time': '9 AM - 4 PM'}, 'Stringfish': {'season': [11, 0, 1, 2], 'price': 15000, 'shadow': 'Largest', 'location': 'River (Clifftop)', 'time': '4 PM - 9 AM'}, 'Arapaima': {'season': [5, 6, 7, 8], 'price': 10000, 'shadow': '', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Hammerhead Shark': {'season': [5, 6, 7, 8], 'price': 8000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Pike': {'season': [8, 9, 10, 11], 'price': 1800, 'shadow': 'X Large', 'location': 'River', 'time': 'All day'}, 'Blowfish': {'season': [10, 11, 0, 1], 'price': ' ', 'shadow': 'Medium', 'location': 'Ocean', 'time': '6 PM - 4 AM'}, 'Butterfly Fish': {'season': [3, 4, 5, 6, 7, 8], 'price': 1000, 'shadow': 'Small', 'location': 'Ocean', 'time': 'All day'}, 'Freshwater Goby': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 400, 'shadow': 'Small', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Ranchu Goldfish': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 4500, 'shadow': 'Small', 'location': 'Pond', 'time': '9 AM - 4 PM'}, 'Betta': {'season': [4, 5, 6, 7, 8, 9], 'price': 2500, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Sea Bass': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 400, 'shadow': 'X Large', 'location': 'Ocean', 'time': 'All day'}, 'Dace': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 240, 'shadow': 'Medium', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Yellow Perch': {'season': [9, 10, 11, 0, 1, 2], 'price': 300, 'shadow': 'Medium', 'location': 'River', 'time': 'All day'}, 'Barreleye': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 15000, 'shadow': 'Small', 'location': 'Ocean', 'time': '9 PM - 4 AM'}, 'Sea Horse': {'season': [3, 4, 5, 6, 7, 8, 9, 10], 'price': 1100, 'shadow': 'Smallest', 'location': 'Ocean', 'time': 'All day'}, 'Giant Snakehead': {'season': [5, 6, 7], 'price': ' ', 'shadow': 'X Large', 'location': 'Pond', 'time': '9 AM - 4 PM'}, 'Puffer Fish': {'season': [6, 7, 8], 'price': 250, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Bitterling': {'season': [10, 11, 0, 1, 2], 'price': 900, 'shadow': 'Smallest', 'location': 'River', 'time': 'All day'}, 'Oarfish': {'season': [11, 0, 1, 2, 3, 4], 'price': 9000, 'shadow': 'Largest', 'location': 'Ocean', 'time': 'All day'}, 'Angelfish': {'season': [4, 5, 6, 7, 8, 9], 'price': 3000, 'shadow': 'Small', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Tuna': {'season': [10, 11, 0, 1, 2, 3], 'price': 7000, 'shadow': 'X Large', 'location': 'Pier', 'time': 'All day'}, 'Tilapia': {'season': [5, 6, 7, 8, 9], 'price': 800, 'shadow': '', 'location': 'River', 'time': 'All day'}, 'Giant Trevally': {'season': [4, 5, 6, 7, 8, 9], 'price': 4500, 'shadow': 'Large', 'location': 'Pier', 'time': 'All day'}, 'Sweetfish': {'season': [6, 7, 8], 'price': 900, 'shadow': 'Medium', 'location': 'River', 'time': 'All day'}, 'King Salmon': {'season': [8], 'price': 1800, 'shadow': 'Smallest', 'location': 'River (mouth)', 'time': 'All day'}, 'Blue Marlin': {'season': [0, 1, 2, 3, 6, 7, 8, 10, 11], 'price': 10000, 'shadow': 'X Large', 'location': 'Pier', 'time': 'All day'}, 'Rainbowfish': {'season': [4, 5, 6, 7, 8, 9], 'price': 800, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Olive Flounder': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 800, 'shadow': 'Large', 'location': 'Ocean', 'time': 'All day'}, 'Squid': {'season': [11, 0, 1, 2, 3, 4, 5, 6, 7], 'price': 500, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Zebra Turkeyfish': {'season': [3, 4, 5, 6, 7, 8, 9, 10], 'price': 500, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Napoleonfish': {'season': [6, 7], 'price': 10000, 'shadow': 'Largest', 'location': 'Ocean', 'time': '4 AM - 9 PM'}, 'Great White Shark': {'season': [5, 6, 7, 8], 'price': 15000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Nibble Fish': {'season': [4, 5, 6, 7, 8], 'price': 1500, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Char': {'season': [2, 3, 4, 5, 8, 9, 10], 'price': 3800, 'shadow': 'Medium', 'location': 'River/Pond', 'time': '4 PM - 9 AM'}, 'Pale Chub': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 160, 'shadow': 'Smallest', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Cherry Salmon': {'season': [2, 3, 4, 5, 8, 9, 10], 'price': 1000, 'shadow': 'Medium', 'location': 'River', 'time': 'All day'}, 'Football Fish': {'season': [10, 11, 0, 1, 2], 'price': 2500, 'shadow': 'Large', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Moray Eel': {'season': [7, 8, 9], 'price': 2000, 'shadow': 'X Large', 'location': 'Ocean', 'time': 'All day'}, 'Sturgeon': {'season': [8, 9, 10, 11, 0, 1, 2], 'price': 10000, 'shadow': 'Largest', 'location': 'River (mouth)', 'time': 'All day'}, 'Crucian Carp': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 160, 'shadow': 'Small', 'location': 'River', 'time': 'All day'}, 'Piranha': {'season': [5, 6, 7, 8], 'price': 2500, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM, 9 PM - 4 AM'}, 'Red Snapper': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 3000, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Guppy': {'season': [3, 4, 5, 6, 7, 8, 9, 10], 'price': 1300, 'shadow': 'Smallest', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Golden Trout': {'season': [2, 3, 4, 5, 8, 9, 10], 'price': 15000, 'shadow': 'Large', 'location': 'River (Clifftop)', 'time': '4 PM - 9 AM'}, 'Neon Tetra': {'season': [3, 4, 5, 6, 7, 8, 9, 10], 'price': 500, 'shadow': 'Smallest', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Ray': {'season': [7, 8, 9, 10], 'price': 3000, 'shadow': 'X Large', 'location': 'Ocean', 'time': '4 AM - 9 PM'}};
#south
fish = {'Koi': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 4000, 'shadow': 'Large', 'location': 'Pond', 'time': '4 PM - 9 AM'}, 'Pond Smelt': {'season': [5, 6, 7], 'price': ' ', 'shadow': 'Small', 'location': 'River', 'time': 'All day'}, 'Suckerfish': {'season': [11, 0, 1, 2], 'price': 1500, 'shadow': '(Fin)', 'location': 'Ocean', 'time': 'All day'}, 'Loach': {'season': [8, 9, 10], 'price': 400, 'shadow': 'Small', 'location': 'River', 'time': 'All day'}, 'Snapping Turtle': {'season': [9, 10, 11, 0, 1, 2, 3], 'price': 5000, 'shadow': '', 'location': 'River', 'time': '9 AM - 4 AM'}, 'Mahi-mahi': {'season': [10, 11, 0, 1, 2, 3], 'price': 6000, 'shadow': 'Large', 'location': 'Ocean', 'time': 'All day'}, 'Crawfish': {'season': [9, 10, 11, 0, 1, 2], 'price': 200, 'shadow': 'Medium', 'location': 'Pond', 'time': 'All day'}, 'Dace': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 240, 'shadow': 'Medium', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Frog': {'season': [10, 11, 0, 1], 'price': ' ', 'shadow': 'Small', 'location': 'Pond', 'time': 'All day'}, 'Tadpole': {'season': [8, 9, 10, 11, 0], 'price': 100, 'shadow': 'Smallest', 'location': 'Pond', 'time': 'All day'}, 'Surgeonfish': {'season': [9, 10, 11, 0, 1, 2], 'price': 1000, 'shadow': 'Small', 'location': 'Ocean', 'time': 'All day'}, 'Catfish': {'season': [10, 11, 0, 1, 2, 3], 'price': 800, 'shadow': '', 'location': 'Pond', 'time': '4 PM - 9 AM'}, 'Sea Butterfly': {'season': [5, 6, 7, 8], 'price': 1000, 'shadow': 'Smallest', 'location': 'Ocean', 'time': 'All day'}, 'Bluegill': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 180, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Pop-eyed Goldfish': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1300, 'shadow': 'Smallest', 'location': 'Pond', 'time': '9 AM - 4 PM'}, 'Nibble Fish': {'season': [10, 11, 0, 1, 2], 'price': 1500, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Horse Mackerel': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 150, 'shadow': 'Small', 'location': 'Ocean', 'time': 'All day'}, 'Stringfish': {'season': [5, 6, 7, 8], 'price': 15000, 'shadow': 'Largest', 'location': 'River (Clifftop)', 'time': '4 PM - 9 AM'}, 'Freshwater Goby': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 400, 'shadow': 'Small', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Dab': {'season': [3, 4, 5, 6, 7, 8, 9], 'price': 300, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Anchovy': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 200, 'shadow': 'Small', 'location': 'Ocean', 'time': '4 AM - 9 PM'}, 'Bitterling': {'season': [4, 5, 6, 7, 8], 'price': 900, 'shadow': 'Smallest', 'location': 'River', 'time': 'All day'}, 'Ribbon Eel': {'season': [11, 0, 1, 2, 3], 'price': 600, 'shadow': 'Narrow', 'location': 'Ocean', 'time': 'All day'}, 'King Salmon': {'season': [2], 'price': 1800, 'shadow': 'Smallest', 'location': 'River (mouth)', 'time': 'All day'}, 'Saddled Bichir': {'season': [5, 6, 7, 8], 'price': 4000, 'shadow': 'Large', 'location': 'River', 'time': '9 PM - 4 AM'}, 'Carp': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 300, 'shadow': 'Large', 'location': 'Pond', 'time': 'All day'}, 'Ocean Sunfish': {'season': [0, 1, 2], 'price': 4000, 'shadow': '(Fin)', 'location': 'Ocean', 'time': '4 AM - 9 PM'}, 'Salmon': {'season': [2], 'price': 700, 'shadow': 'Small', 'location': 'River (mouth)', 'time': 'All day'}, 'Gar': {'season': [0, 1, 2, 3], 'price': 6000, 'shadow': 'Largest', 'location': 'Pond', 'time': '4 PM - 9 AM'}, 'Oarfish': {'season': [5, 6, 7, 8, 9, 10], 'price': 9000, 'shadow': 'Largest', 'location': 'Ocean', 'time': 'All day'}, 'Soft-shelled Turtle': {'season': [1, 2], 'price': 3750, 'shadow': '', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Black Bass': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 400, 'shadow': 'Large', 'location': 'River', 'time': 'All day'}, 'Dorado': {'season': [11, 0, 1, 2], 'price': 15000, 'shadow': 'X Large', 'location': 'River', 'time': '4 a.m - 9 PM'}, 'Football Fish': {'season': [4, 5, 6, 7, 8], 'price': 2500, 'shadow': 'Large', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Goldfish': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 1300, 'shadow': 'Smallest', 'location': 'Pond', 'time': 'All day'}, 'Tuna': {'season': [4, 5, 6, 7, 8, 9], 'price': 7000, 'shadow': 'X Large', 'location': 'Pier', 'time': 'All day'}, 'Sweetfish': {'season': [0, 1, 2], 'price': 900, 'shadow': 'Medium', 'location': 'River', 'time': 'All day'}, 'Ranchu Goldfish': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 4500, 'shadow': 'Small', 'location': 'Pond', 'time': '9 AM - 4 PM'}, 'Hammerhead Shark': {'season': [11, 0, 1, 2], 'price': 8000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Pike': {'season': [2, 3, 4, 5], 'price': 1800, 'shadow': 'X Large', 'location': 'River', 'time': 'All day'}, 'Blowfish': {'season': [4, 5, 6, 7], 'price': 5000, 'shadow': 'Medium', 'location': 'Ocean', 'time': '6 PM - 4 AM'}, 'Butterfly Fish': {'season': [9, 10, 11, 0, 1, 2], 'price': 1000, 'shadow': 'Small', 'location': 'Ocean', 'time': 'All day'}, 'Clown Fish': {'season': [9, 10, 11, 0, 1, 2], 'price': 650, 'shadow': 'Smallest', 'location': 'Ocean', 'time': 'All day'}, 'Coelacanth': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 15000, 'shadow': 'Largest', 'location': 'Ocean (rainy days)', 'time': 'All day'}, 'Betta': {'season': [10, 11, 0, 1, 2, 3], 'price': 2500, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Sea Bass': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 400, 'shadow': 'X Large', 'location': 'Ocean', 'time': 'All day'}, 'Yellow Perch': {'season': [3, 4, 5, 6, 7, 8], 'price': 300, 'shadow': 'Medium', 'location': 'River', 'time': 'All day'}, 'Barreleye': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 15000, 'shadow': 'Small', 'location': 'Ocean', 'time': '9 PM - 4 AM'}, 'Mitten Crab': {'season': [2, 3, 4], 'price': 2000, 'shadow': 'Small', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Giant Snakehead': {'season': [11, 0, 1], 'price': ' ', 'shadow': 'X Large', 'location': 'Pond', 'time': '9 AM - 4 PM'}, 'Puffer Fish': {'season': [0, 1, 2], 'price': 250, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Arowana': {'season': [11, 0, 1, 2], 'price': 10000, 'shadow': 'Large', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Barred Knifejaw': {'season': [8, 9, 10, 11, 0, 1, 2, 3, 4], 'price': 5000, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Angelfish': {'season': [10, 11, 0, 1, 2, 3], 'price': 3000, 'shadow': 'Small', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Saw Shark': {'season': [11, 0, 1, 2], 'price': 12000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Whale Shark': {'season': [11, 0, 1, 2], 'price': 13000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': 'All day'}, 'Giant Trevally': {'season': [10, 11, 0, 1, 2, 3], 'price': ' ', 'shadow': 'Large', 'location': 'Pier', 'time': 'All day'}, 'Ray': {'season': [1, 2, 3, 4], 'price': 3000, 'shadow': 'X Large', 'location': 'Ocean', 'time': '4 AM - 9 PM'}, 'Tilapia': {'season': [11, 0, 1, 2, 3], 'price': 800, 'shadow': '', 'location': 'River', 'time': 'All day'}, 'Blue Marlin': {'season': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10], 'price': 10000, 'shadow': 'X Large', 'location': 'Pier', 'time': 'All day'}, 'Rainbowfish': {'season': [10, 11, 0, 1, 2, 3], 'price': 800, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Olive Flounder': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 800, 'shadow': 'Large', 'location': 'Ocean', 'time': 'All day'}, 'Squid': {'season': [5, 6, 7, 8, 9, 10, 11, 0, 1], 'price': 500, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Zebra Turkeyfish': {'season': [9, 10, 11, 0, 1, 2, 3, 4], 'price': 500, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Napoleonfish': {'season': [0, 1], 'price': 10000, 'shadow': 'Largest', 'location': 'Ocean', 'time': '4 AM - 9 PM'}, 'Great White Shark': {'season': [11, 0, 1, 2], 'price': 15000, 'shadow': 'Largest (fin)', 'location': 'Ocean', 'time': '4 PM - 9 AM'}, 'Golden Trout': {'season': [2, 3, 4, 8, 9, 10, 11], 'price': 15000, 'shadow': 'Large', 'location': 'River (Clifftop)', 'time': '4 PM - 9 AM'}, 'Char': {'season': [2, 3, 4, 8, 9, 10, 11], 'price': 3800, 'shadow': 'Medium', 'location': 'River/Pond', 'time': '4 PM - 9 AM'}, 'Pale Chub': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 160, 'shadow': 'Smallest', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Cherry Salmon': {'season': [2, 3, 4, 8, 9, 10, 11], 'price': 1000, 'shadow': 'Medium', 'location': 'River', 'time': 'All day'}, 'Sea Horse': {'season': [9, 10, 11, 0, 1, 2, 3, 4], 'price': 1100, 'shadow': 'Smallest', 'location': 'Ocean', 'time': 'All day'}, 'Arapaima': {'season': [11, 0, 1, 2], 'price': 10000, 'shadow': '', 'location': 'River', 'time': '4 PM - 9 AM'}, 'Moray Eel': {'season': [1, 2, 3], 'price': 2000, 'shadow': 'X Large', 'location': 'Ocean', 'time': 'All day'}, 'Crucian Carp': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 160, 'shadow': 'Small', 'location': 'River', 'time': 'All day'}, 'Piranha': {'season': [11, 0, 1, 2], 'price': 2500, 'shadow': 'Small', 'location': 'River', 'time': '9 AM - 4 PM, 9 PM - 4 AM'}, 'Red Snapper': {'season': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'price': 3000, 'shadow': 'Medium', 'location': 'Ocean', 'time': 'All day'}, 'Guppy': {'season': [9, 10, 11, 0, 1, 2, 3, 4], 'price': 1300, 'shadow': 'Smallest', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Killifish': {'season': [9, 10, 11, 0, 1], 'price': 300, 'shadow': 'Smallest', 'location': 'Pond', 'time': 'All day'}, 'Neon Tetra': {'season': [9, 10, 11, 0, 1, 2, 3, 4], 'price': 500, 'shadow': 'Smallest', 'location': 'River', 'time': '9 AM - 4 PM'}, 'Sturgeon': {'season': [2, 3, 4, 5, 6, 7, 8], 'price': 10000, 'shadow': 'Largest', 'location': 'River (mouth)', 'time': 'All day'}};

#replacing season codes with month abbreviations
for name,info in bugs.items():
    seasons = info['season'];
    bugs[name]['season'] = [months[s] for s in seasons];

for name,info in fish.items():
    seasons = info['season'];
    fish[name]['season'] = [months[s] for s in seasons];
    
# count the arguments in command line
arguments = len(sys.argv) - 1;


# if 0 arguments, print bugs. else return fish;
if __name__ == "__main__":
     if arguments == 0:
        print json.dumps(bugs);
     else:
         print json.dumps(fish);
    


