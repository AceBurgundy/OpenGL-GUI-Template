# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Program import App

import OpenGL.GLU as GLU
import OpenGL.GL as GL

from tkinter import Event
from typing import List
import pyopengltk
import time

# key methods
from .__key_released import handle_key_released
from .__key_pressed import handle_key_pressed

# mouse methods
from .__on_release import on_mouse_released
from .__on_click import on_mouse_clicked
from .__on_move import on_mouse_move

class Canvas(pyopengltk.OpenGLFrame):

    width: int = 1270
    height: int = 685
    start_time: float = time.time()

    def __init__(self, parent: App, *args, **kwargs) -> None:
        """
        Initializes the App object.

        Arguments:
            parent (App): The parent MainApp object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.
        """
        super().__init__(parent, *args, **kwargs)

        self.bind("<Motion>", lambda event: on_mouse_move(self, event) )
        self.bind("<Button>", lambda event: on_mouse_clicked(self, event) )
        self.bind("<ButtonRelease>", lambda event: on_mouse_released(self, event) )

        self.parent: App = parent
        self.animate: int = 1

        self.dragging: bool = False
        self.mouse_pressed: str = ''

    def key_pressed(self, event: Event):
        """
        Handle key press events
        """
        handle_key_pressed(self, event)

    def key_released(self, event: Event):
        """
        Handle key press events
        """
        handle_key_released(self, event)

    def initgl(self) -> None:
        """
        Initializes the canvas and OpenGL.GL context
        """
        GL.glClearColor(0.17, 0.17, 0.17, 1)

    def cube(self) -> None:
        """
        Draws a cube and rotates it based on the elapsed time * 30 (to slow it down)
        """
        # Calculate rotation angle based on elapsed time
        elapsed_time = time.time() - self.start_time
        rotation_angle = elapsed_time * 30

        # Rotate the cube
        GL.glRotatef(rotation_angle, 0.0, 1.0, 0.0)

        vertices: List[List[int]] = [
            [-1, -1, -1],
            [ 1, -1, -1],
            [ 1,  1, -1],
            [-1,  1, -1],
            [-1, -1,  1],
            [ 1, -1,  1],
            [ 1,  1,  1],
            [-1,  1,  1]
        ]

        edges: List[List[int]] = [
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]
        ]

        GL.glColor3f(0.5, 0.5, 1.0)

        GL.glBegin(GL.GL_LINES)
        for edge in edges:
            for vertex in edge:
                GL.glVertex3fv(vertices[vertex])
        GL.glEnd()

        GL.glFlush()

    def redraw(self) -> None:
        """
        Draws elements to the canvas.
        """
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glClear(GL.GL_DEPTH_BUFFER_BIT)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()

        GLU.gluPerspective(45, (Canvas.width / Canvas.height), 1, 100)

        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()

        GL.glTranslatef(0.0, 0.0, -5.0)

        self.cube()