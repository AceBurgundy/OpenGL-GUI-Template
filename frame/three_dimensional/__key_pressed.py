# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from frame.three_dimensional.canvas import Canvas

from .__key_status import get_key_status

from typing import Dict, List
from tkinter import Event

def handle_key_pressed(canvas_instance: Canvas, event: Event) -> None:
    """
    Handles key pressed events sent from main CTk frame

    Arguments:
        canvas_instance (Canvas): The current running instance of the Canvas
        event (Event): The Tkinter.Event that carries key pressed information
    """
    press_status: Dict[str, List[str]|str] = get_key_status(event)
    state: Union[List[str], str, None] = press_status.get('state', None)
    key: Union[List[str], str, None] = press_status.get('key', None)

    if type(key) != str:
        return

    if state:
        pressed_shift: bool = 'Shift' in state
        pressed_control: bool = 'Control' in state
        held_both: bool = pressed_shift and pressed_control

        if held_both:
            __handle_shift_and_control(canvas_instance, key)
            return

        elif pressed_shift:
            __handle_shift(canvas_instance, key)
            return

        elif pressed_control:
            __handle_control(canvas_instance, key)
            return

    if key:
        __handle_key(canvas_instance, key)

def __handle_shift(canvas_instance: Canvas, key: str) -> None:
    """
    Handles events where another key is pressed, while the shift key is being held down

    Arguments:
        canvas_instance (Canvas): The current running instance of the Canvas
        event (Event): The Tkinter.Event that carries key pressed information
    """
    pass

def __handle_shift_and_control(canvas_instance: Canvas, key: str) -> None:
    """
    Handles events where another key is pressed, while the shift key and control key is being held down

    Arguments:
        canvas_instance (Canvas): The current running instance of the Canvas
        event (Event): The Tkinter.Event that carries key pressed information
    """
    pass

def __handle_key(canvas_instance: Canvas, key: str) -> None:
    """
    Handles events where another key is being pressed.

    Arguments:
        canvas_instance (Canvas): The current running instance of the Canvas
        event (Event): The Tkinter.Event that carries key pressed information
    """
    pass

def __handle_control(canvas_instance: Canvas, key: str) -> None:
    """
    Handles events where another key is being pressed. While the control key is being held

    Arguments:
        canvas_instance (Canvas): The current running instance of the Canvas
        event (Event): The Tkinter.Event that carries key pressed information
    """
    pass