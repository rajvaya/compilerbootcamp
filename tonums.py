
from typing import Tuple
def convert_nums(tree: tuple):
    convertedTuple = tuple()
    for x in tree:
        if(type(x) is str):
          convertedTuple += (x,)
          print(convertedTuple);
        if((type(x) is tuple)):
            if((len(x) == 2) and (x[0] == "num")):
                convertedTuple += ((x[0], int(x[1])),)
            elif((len(x) >= 2)):
                convertedTuple += (convert_nums(x),)
    return(convertedTuple)


myTree = ('assign', 'spam', ('binop', '+', ('name', 'x'),
          ('binop', '*', ('num', '34'), ('num', '567'))))
print(convert_nums(myTree))
