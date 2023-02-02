import nbt
import os
import binascii

# open the schematic file
schematic = nbt.nbt.NBTFile('dispenser2x2x2.schem', 'rb')
palette = schematic['Palette']


def get_dimensions():
    width = schematic['Width'].value
    height = schematic['Height'].value
    length = schematic['Length'].value
    print(f"Dimensions: {width} x {height} x {length}")


def get_palette():
    if not os.path.exists("palette.txt"):
        with open ("palette.txt", "w") as f:
            for i in range(0, len(palette)):
                for items in palette:
                    if schematic['Palette'][items].value == i:
                        f.write(f"{schematic['Palette'][items].value} : {items} \n")
                        

# gets block data from BlockData hex
def get_block_data():
    block_data = (schematic['BlockData'].value).hex()
    # for every 2 hex values, add a space\
    block_data = " ".join(block_data[i:i+2] for i in range(0, len(block_data), 2))
    
    # write to text file
    with open("block_data.txt", "w") as f:
        f.write(block_data)
    
    # write to hex file
    with open("block_data.txt") as f, open ("block_data", "wb") as f2:
        for line in f:
            f2.write(binascii.unhexlify(''.join(line.split())))
    
   
   
def block_placement():
     return
   
            
def main():
    get_palette()
    get_dimensions()
    get_block_data()
    block_placement()
    


if __name__ == "__main__":
    main()

