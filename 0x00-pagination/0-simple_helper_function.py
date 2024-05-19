#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of start and end indexes for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


if __name__ == "__main__":
    pass
