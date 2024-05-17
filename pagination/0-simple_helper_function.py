#!/usr/bin/env python3
"""
Module for simple helper functions.
"""

def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start and end indexes.

    Raises:
        ValueError: If page or page_size is less than 1.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be greater than or equal to 1.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
