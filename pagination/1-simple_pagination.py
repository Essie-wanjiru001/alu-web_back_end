#!/usr/bin/env python3
"""
Module for simple helper functions and Server class for pagination.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data from the dataset based on pagination parameters.

        Args:
            page (int): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows representing the data for the requested page.

        Raises:
            AssertionError: If page or page_size are not integers greater than 0.
        """
        assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]
