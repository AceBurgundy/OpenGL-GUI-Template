# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
    from Program import App

from customtkinter import CTkFrame, CTkButton
from constants import *

class Navigation(CTkFrame):

    def __init__(self, parent: App, **kwargs):
        """
        Initializes the Navigation object.

        Arguments:
            parent (App): The parent CTk object.
            **kwargs: Additional keyword arguments to pass to the parent class initializer.

        Raises:
            TypeError: If the list of buttons is empty.
        """
        super().__init__(parent, **kwargs)
        self.configure(fg_color='transparent')
        self.parent = parent

        buttons: List[Any] = [
            CTkButton(self, width=80, height=20, text="Sample button", command=lambda: print("button clicked") )
        ]

        for button in buttons:
            button.pack(side="left", padx=LEFT_PADDING_ONLY, pady=DEFAULT_PADDING)