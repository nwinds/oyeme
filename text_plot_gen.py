"""
Worked in IDE like Canopy with python chosen as interpreter
Bugs in python command line mode
"""
# !/usr/local/bin/ python
__author__ = "nwinds"


import matplotlib.pyplot as plt

# texts generator


def cesar(shift):
    s = raw_input(
        'Enter a string(4 words with 3 space as seperator will be okay): ')
    cipherStr = ''
    for ch in s:
        if ch == ' ':
            cipherStr += ch
        elif ord(ch) + shift <= ord('z'):
            cipherStr += chr(ord(ch) + shift)
        else:
            cipherStr += chr(ord(ch) + shift - ord('z') + ord('a'))
    return cipherStr.split(' ')


cipher = cesar(3)


# rgb color scheme (blue, b0~b4, dark => light)
# from http://www.peise.net/2014/1118/4728.html
b0 = (0, 57 / 255.0, 179 / 255.0)
b1 = (79 / 255.0, 127 / 255.0, 232 / 255.0)
b2 = (104 / 255.0, 146 / 255.0, 237 / 255.0)
b3 = (151 / 255.0, 183 / 255.0, 252 / 255.0)
b4 = (190 / 255.0, 208 / 255.0, 247 / 255.0)


# base on http://matplotlib.org/examples/pylab_examples/fancytextbox_demo.html
# TODO: Gaussian distribution of boxes' position, much more good looking
plt.text(0.40, 0.6, cipher[0], size=60, rotation=-20.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=b0,
                   fc=b1,
                   )
         )

plt.text(0.35, 0.3, cipher[1], size=50, rotation=30,
         ha="center", va="center",
         bbox=dict(boxstyle="square",
                   ec=b0,
                   fc=b3,
                   )
         )

plt.text(0.85, 0.9, cipher[2], size=55, rotation=15,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=b0,
                   fc=b2,
                   )
         )

plt.text(0.9, 0.5, cipher[3], size=55, rotation=-30.,
         ha="right", va="top",
         bbox=dict(boxstyle="round",
                   ec=b0,
                   fc=b4,
                   )
         )


plt.draw()
plt.show()
