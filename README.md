# 🧱 OpenGL GUI Template

## 🎯 Project Purpose

This simple project was created as a **starter template** for students, hobbyists, or developers interested in learning how to embed OpenGL graphics within a Python GUI using **CustomTkinter**.
It is intentionally **minimal** and demonstrates just **one thing**: rendering a continuously **rotating cube** inside a GUI window.

## 🌀 What It Does

* Opens a GUI window using `customtkinter`
* Renders a 3D cube inside the GUI using `PyOpenGL`
* Rotates the cube continuously as a basic animation

That’s it — no controls, no interactivity, no extra features.
It’s designed to be clean, understandable, and extendable.

## 🖼️ Preview

| GUI Interface |
| ------------- |
| ![UI](UI.png) |

## 📦 Prerequisites

* **Python 3.8+**
* **pip** for dependency installation
* (Optional) A virtual environment for clean dependency management

## ⚙️ Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/your-username/opengl-gui-template.git
   cd opengl-gui-template
   ```

2. **Install required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the App

Launch the app with:

```bash
python app.py
```

You should see a window pop up with a **rotating 3D cube** rendered inside a GUI.

## 💡 How to Extend

This project is meant to be built upon. You can add:

* More OpenGL shapes or scenes
* GUI controls for camera or object interaction
* Texture mapping, lighting, or shading
* Event-driven actions like mouse or keyboard input

Modify the `OpenGLFrame` class to change what’s rendered or animated.

## 🧰 Technologies Used

* **Python**
* **PyOpenGL**
* **pyopengltk** – for embedding OpenGL into Tkinter
* **CustomTkinter** – for modern GUI layout

## 🙏 Acknowledgements

* [pyopengltk](https://github.com/jonwright/pyopengltk): Enables OpenGL to render inside a Tkinter frame.
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): Beautiful modern UI components for Python.

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for full details.

## 📚 Educational Use

This was created as a basic hands-on template to help students (ourselves included) understand:

* How OpenGL rendering works
* How to place OpenGL inside a GUI window
* How to structure a clean, minimal Python app with a GUI

We hope it helps you get started too.

Let me know if you'd like to add some beginner tips or a short customization guide inside a `docs/` folder.
