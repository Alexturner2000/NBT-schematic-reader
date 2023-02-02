import nbt

# open the schematic file
schematic = nbt.nbt.NBTFile('cath.schem', 'rb')

# dimension data
width = schematic['Width'].value
height = schematic['Height'].value
length = schematic['Length'].value
print(f"Dimensions: {width} x {height} x {length}")

# requested block name
palette = schematic['Palette']
requested_item_name = "minecraft:stone"

# print palette data in id order (most common to least common)
for i in range(0, len(palette)):
    for items in palette:
        if schematic['Palette'][items].value == i:
            print(f"Id: {schematic['Palette'][items].value} is {items} ")





