import nbt
import os
import binascii

# open the schematic file
schematic = nbt.nbt.NBTFile('dispenser2x2x2.schem', 'rb')
palette = schematic['Palette']


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
        
    # write to hex file
    with open ("block_data", "wb") as f:
        f.write(binascii.unhexlify(block_data))
    
   
   
def block_placement():
    # for every hex value in block_data, print the corresponding block from palette
    width = schematic['Width'].value 
    height = schematic['Height'].value 
    length = schematic['Length'].value
    print(f"Dimensions: {width} x {height} x {length}")
    
    
    # Creates coordinates for each block
    x,z,y = 0,0,0
    arr = []
    for x in range(0, height):
        for z in range(0, width):
                for y in range(0, length):
                    arr.append((x, y, z))

                    
    
    # read block_data hex file and adds coordinates and blocktype to the [block class]
    with open ("block_data", "rb") as f:
        for line in f:
            for i in range(0, len(line)): #loops for each hex value in block
                for items in palette:
                    if schematic['Palette'][items].value == line[i]:
                        # formating
                        items = items[10:] 
                        if "[" in items:
                            items = items.split("[")[0]  
                        
                        # access x, y, z from array
                        x, y, z = arr[i]
                                                                  
                        block = Block_Plane(x, z, y, items)
                        # increment x by 1 until it reaches width, then increment y by 1 and reset x to 0, then increment z by 1 and reset x and y to 0
                        print(block)                


class Block_Plane:
    def __init__(self, x, y, z, block):
        self.block = block
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return (f"({self.x}, {self.y}, {self.z}) {self.block}")                

                        
def main():
    get_palette()
    get_block_data()
    block_placement()
    


if __name__ == "__main__":
    main()

