# Pyxi
[![PyPI version](https://badge.fury.io/py/pyxi.svg)](https://badge.fury.io/py/pyxi) [![Documentation Status](https://readthedocs.org/projects/pyxi/badge/?version=latest)](https://pyxi.readthedocs.io/en/latest/?badge=latest)

`pyxi` is a small library for interfacing with PyxelEdit `.pyxel` files in an object-oriented manner.
Currently it allows for viewing all attributes of a `.pyxel` file, modifying values, and repacking the file
into its original format for use within PyxelEdit.

### Examples
Editing tile width and height on an image.
```python
from pyxi import PyxelImage

p = PyxelImage('test_8px.pyxel')  # assume the tiles are 8x8
p.extract()  # extracts all the files into the converted/ directory (seperated layers, json data)
```

Loading a `.pyxel` file as a texture in `arcade`.
```python
import arcade
from pyxi import PyxelImage

p = PyxelImage('test_8px.pyxel')
texture = p.get_tile()  # returns a Pillow Image object
player = arcade.Sprite(scale=4)
player.texture = arcade.Texture(name='S8dhS7dja', image=texture)
```
