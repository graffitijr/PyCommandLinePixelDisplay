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


### ✍️ Authors

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
