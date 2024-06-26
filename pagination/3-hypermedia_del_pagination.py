#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve hypermedia information for pagination based on index.

        Args:
            index (int): The start index of the page. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia information.

        Raises:
            AssertionError: If index is out of range.
        """
        assert index is None or (isinstance(index, int) and 0 <= index < len(self.indexed_dataset())), \
            "Index must be within range or None."

        indexed_dataset = self.indexed_dataset()
        if index is None:
            index = 0

        next_index = min(index + page_size, len(indexed_dataset))
        data = [indexed_dataset[i] for i in range(index, next_index)]

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }


if __name__ == "__main__":
    # Test cases
    server = Server()
    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server.indexed_dataset())))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server.indexed_dataset())))

    # 4- request again the initial index -> the first data retrieves is not the same as the first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
