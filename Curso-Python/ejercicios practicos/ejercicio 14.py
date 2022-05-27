def num_max_min(a,b,c):
    if a > b and a > c:
        print("el mayor es", a, "y el menor es", c)
    elif b > a and b > c:
        print("el mayor es", b, "y el menor es", c)
    elif c > a and c > b:
        print("El mayor es", c, "y el menor es", b)
    else:
        print("son lo mismo")

num_max_min(5,4,3)
