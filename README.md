# </> PyCommandLinePixelDisplay

![Static Badge](https://img.shields.io/badge/License-MIT-blue) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/graffitijr/PyCommandLinePixelDisplay)


## 🌟 Highlights

-It is compatitble with popular online interpreters such as programiz

-It's a mix of elements from the command prompt and GUIs

-It is extremely lightweight 

-Simple to use as ease of use was one of my main priorities 

-Allows direct pixel control while still being fully command prompt

-Only one file ~2.2kb


## ℹ️ Overview

I wanted to make a free, easy for beginners intro to pixel control in the command prompt. I dont know but this could be used for simple non-GUI games, as it is very lightweight, simple and fast.


### 👨‍💻 Creator

I'm graffitjr. My Github is https://github.com/graffitijr


## 🚀 Usage

The base start that you will most likely use is this:

```py
gui = PyCommandLinePixelDisplay(10, 10, 0) # The first 2 values are width and height of the screen, and the 3rd value is the default background value/color
# Anything that runs at start, like variables and such

while True:
    gui.update_screen()
    
    # Put anything that should run with main loop, like controls
    
    gui.target_fps(5) # controls fps (if this is not here it will run without limits, which will make your cpu run at 100% so watch out)

```

This is all you need to start "Rendering".

The screen works with a pixel based system, where it goes 0, 0 to width - 1, height - 1, which means that you work with pixels as they you would with graphs, but the y value goes from top to bottom rather than bottom to top. 

To set a pixel you would use the set_pixel command, in practice that would look like this:

```py
gui.set_pixel(2, 3, 1)
```

This would set the pixel at 2, 3 to 1.

When running a function from the class that hold the lib (PyCommandLinePixelDisplay), you would first put the name you gave it when initializing it, which we did gui when we did:

```py
gui = PyCommandLinePixelDisplay(10, 10, 0)
```

Because this is a very simple library, there aren’t very many functions, just simple pixel commands.

### Custom Characters

The default values built in are 0 and 1, which correspond to shaded and filled. The way these pixel color values are stored are in integers, such as 0, 1, 2 and so on. The renderer decodes these with a dictionary that is either given to it, or just the default one. The way to format the dictionary is as such:

```py
value_dict = {
    0:" _",
    1:" #",
    2:" &"
}
```

The values that you set the pixel to will be decoded to these characters to be printed.

The way to give this for the program to reference is with the set_levels() function.

NOTE: v1.1.0 allows you to avoid working with the translation dictionary as it is done for you, but for more control, it is still useful.

### Console Clear Error

Some consoles dont allow the main clear type, and instead print a character of a box with an X. The way to get around this is using the fallback option, but this may cause flickering or a sliding effect and is not as good as the main one.

### Recommended Extras

PyCommandLinePixelDisplay doesn't yet have any built in input library but one is in the works, my recommendation is the "keyboard" library https://pypi.org/project/keyboard/

It is a very simple way in my opinion to get input. An example that would work well with PyCommandLinePixelDisplay is the following:

```py
import keyboard

if keyboard.is_pressed("a"):
    do_something()
```

## ⬇️ Installation

Minimum Python: 3.6

Install by downloading and moving PyCommandLinePixelDisplay.py to your python project folder.

At the top of your main python script, add:

```py
from PyCommandLinePixelDisplay import PyCommandLinePixelDisplay
```

Another option is to make your script right in the file, which isnt as organized, but will work.


## 💭 Feedback and Contributing

If you find any bugs or want any features, I would love to hear them and no ideas are bad.
