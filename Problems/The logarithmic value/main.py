import math
lg = float(input())
base = float(input())


if base > 1:
    print(round(math.log(lg, base), 2))
else:
    print(round(math.log(lg), 2))
