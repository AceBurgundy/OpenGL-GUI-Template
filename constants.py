from typing import Tuple, Literal

WINDOW_SIZE: str = "1080x720"

DEFAULT_PADDING: Literal[5] = 5

BOTTOM_PADDING_ONLY: Tuple[Literal[0], int] = (0, DEFAULT_PADDING)
RIGHT_PADDING_ONLY: Tuple[Literal[0], int] = (0, DEFAULT_PADDING)

TOP_PADDING_ONLY: Tuple[int, Literal[0]] = (DEFAULT_PADDING, 0)
LEFT_PADDING_ONLY: Tuple[int, Literal[0]] = (DEFAULT_PADDING, 0)