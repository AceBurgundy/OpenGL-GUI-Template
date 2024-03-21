# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from frame.three_dimensional.canvas import Canvas

from tkinter import Event
from typing import List

def on_mouse_clicked(canvas_instance: Canvas, event: Event) -> None:
    """
    Handles mouse click events

    Arguments:
        canvas_instance (Canvas): The current instance of the canvas
        event (Event): A Tkinter event object representing the key press event.
    """
    click_types: List[str] = ["Left", "Scroll", "Right"]
    pass
