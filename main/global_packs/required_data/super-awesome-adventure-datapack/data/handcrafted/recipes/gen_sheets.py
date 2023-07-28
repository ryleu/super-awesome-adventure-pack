#!/bin/env python3

template = \
"""{
    "type": "minecraft:crafting_shaped",
    "pattern": [
        "  W",
        " W ",
        "W  "
    ],
    "key": {
        "W": {
            "item": "minecraft:color_wool"
        }
    },
    "result": {
        "item": "handcrafted:color_sheet",
        "count": 8
    }
}"""

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "magenta",
    "light_blue",
    "cyan",
    "lime",
    "brown",
    "black",
    "white",
    "pink",
    "gray",
    "light_gray"
]

for i in colors:
    with open(f"{i}_sheet.json", "w") as file:
        file.write(template.replace("color", i))
