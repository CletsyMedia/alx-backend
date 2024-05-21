#!/usr/bin/python3
"""LFU Caching"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Caching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.frequency[key] = 1
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_frequency]
                lru_key = min(lfu_keys, key=lambda k: self.cache_data[k])
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
