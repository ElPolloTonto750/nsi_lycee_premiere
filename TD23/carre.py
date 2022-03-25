import tkinter as tk
def square_list(w: int, h: int):
    liste1 = []
    c = 0
    while w != 0 and h != 0:
        x, y = w, h
        if w > h:
            c = h
            w = w-h
        else:
            c = w
            h = h-w
        carre = (x, y, c)
        liste1.append(carre)
    return liste1


