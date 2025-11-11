# </> PyCommandLineGUI

![Static Badge](https://img.shields.io/badge/License-MIT-blue) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/graffitijr/PyCommandLineGUI)


## 🌟 Highlights

-Its a mix of elements from the command prompt and GUIs

-It is extreamly lightweight 

-Simple to use as ease of use was one of main priorities 

-Allows start to pixel control while still being fully command prompt

-Only one file ~2.2kb


## ℹ️ Overview

I wanted to make a free, easy for beginners intro to pixel control in the command prompt. I dont know but this could be used for simple non-GUI games, as it is very lightweight, simple and fast.


### 👨‍💻 Creator

I'm graffitjr. My Github is https://github.com/graffitijr


## 🚀 Usage

The base start that you will most likely use is this:

```py
gui = PyCommandLineGUI(10, 10, 0) # The first 2 values are width and height of the screen, and the 3rd value is the default background value/color
# Anything that runs at start, like variables and such

while True:
    gui.update_screen()
    
    # Put any thing that should run with main loop, like controls
    
    gui.target_fps(5) # controls fps (if this is not here it will run without limits, which will make your cpu run at 100% so watch out)

```

This is all you need to start "Rendering".

The screen works with a pixel based system, where it goes 0, 0 to width - 1, height - 1, which means that you work with pixels as they you would with graphs, but the y value goes from top to bottom rather than bottom to top. 

To set a pixel you would use the set_pixel command, in practice that would look like this:

```py
gui.set_pixel(2, 3, 1)
```

This would set the pixel at 2, 3 to 1.

When running a function from the class that hold the lib (PuCommandLineGUI), you would first put the name you gave it when innitializing it, which we did gui when we did:

```py
gui = PyCommandLineGUI(10, 10, 0)
```

Because this is a very simple library, there arent vary many function, just simple pixel commands.

### Custom Characters

The default values built in are 0 and 1, which corespond to shaded and filled. The way these values are stored are in intergers, such as 0, 1, 2 and so on. The renderer decodes these with a dictionary that is either given to it, or just the default one. The way to format the dictionary is as such:

```py
value_dict = {
    0:" _"
    1:" #"
    2:" &"
}
```

The values that you set the pixel to will be decoded to these characters to be printed.

The way to give this for the program to reference is with the set_levels() function.

### Every Function

set_levels(levels: dict)

Define how each value in the screen is displayed.

Parameters:

levels — dictionary mapping pixel values to strings

Example: {0: "░░ ", 1: "██ "}

Example:

## ⬇️ Installation

Simple, understandable installation instructions!

```bash
pip install my-package
```

And be sure to specify any other minimum requirements like Python versions or operating systems.

*You may be inclined to add development instructions here, don't.*


## 💭 Feedback and Contributing

Add a link to the Discussions tab in your repo and invite users to open issues for bugs/feature requests.

This is also a great place to invite others to contribute in any ways that make sense for your project. Point people to your DEVELOPMENT and/or CONTRIBUTING guides if you have them.
