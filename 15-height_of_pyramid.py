blocks = int(input("Enter the number of blocks: "))


num=1
X=0
height=0
while X<=blocks:
    X=X+num
    num=num+1
    height=height+1
    
print("The height of the pyramid:", height-1)


# Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

# The figure illustrates the rule used by the builders:
        #                       ___
        #                     _|___|_                        |
        #                   _|___|___|_                      |
        #                 _|___|___|___|_                    | 5=height     15= blocks
        #               _|___|___|___|___|_                  |
        #              |___|___|___|___|___|                 |
        

# Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

# Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

# Test your code using the data we've provided.