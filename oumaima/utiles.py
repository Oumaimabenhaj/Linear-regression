def max(liste):
    max_val = liste[0]
    for x in liste:
        if  x > max_val:
            max_val = x
    return max_val

