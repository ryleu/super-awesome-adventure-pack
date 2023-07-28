#!/bin/env python3

template = \
"""{
    "type": "minecraft:COOKINGTYPE",
    "ingredient": {
        "item": "minecraft:raw_MATERIAL_block"
    },
    "result": "minecraft:MATERIAL_block",
    "experience": EXPERIENCE,
    "cookingtime": COOKINGTIME
}
"""

materials = [
   ("copper", "6.3"),
    ("iron", "6.3"),
    ("gold", "9")
]

cooking_types = [
    ("smelting", "200"),
    ("blasting", "100")
]

for material in materials:
    for cooking_type in cooking_types:
        with open(f"raw_{material[0]}_{cooking_type[0]}.json", "w") as file:
            file.write(template
                .replace("MATERIAL", material[0])
                .replace("EXPERIENCE", material[1])
                .replace("COOKINGTYPE", cooking_type[0])
                .replace("COOKINGTIME", cooking_type[1])
            )
