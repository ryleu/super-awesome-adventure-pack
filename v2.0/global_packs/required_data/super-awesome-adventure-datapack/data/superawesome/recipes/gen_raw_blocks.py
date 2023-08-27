#!/bin/env python3
import os

try:
    os.mkdir("generated")
except FileExistsError:
    pass

template = \
"""{
    "type": "minecraft:COOKINGTYPE",
    "ingredient": {
        "item": "NAMESPACE:raw_MATERIAL_block"
    },
    "result": "NAMESPACE:MATERIAL_block",
    "experience": EXPERIENCE,
    "cookingtime": COOKINGTIME
}
"""

materials = [
   ("minecraft", "copper", "6.3"),
    ("minecraft", "iron", "6.3"),
    ("minecraft", "gold", "9"),
    ("ad_astra", "desh", "6.3")
]

cooking_types = [
    ("smelting", "200"),
    ("blasting", "100")
]

for material in materials:
    for cooking_type in cooking_types:
        with open(f"generated/raw_{material[1]}_{cooking_type[0]}.json", "w") as file:
            file.write(template
                .replace("NAMESPACE", material[0])
                .replace("MATERIAL", material[1])
                .replace("EXPERIENCE", material[2])
                .replace("COOKINGTYPE", cooking_type[0])
                .replace("COOKINGTIME", cooking_type[1])
            )
