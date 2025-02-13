# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Refactor source code using the Strategy Pattern
class ItemBehavior(ABC):

    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update(self):
        pass

    def decrease_sell_in(self):
        self.item.sell_in -= 1


class NormalItem(ItemBehavior):

    def update(self):
        if self.item.quality > 0:
            self.item.quality -= 1
        self.decrease_sell_in()
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 1


class AgedBrie(ItemBehavior):

    def update(self):
        if self.item.quality < 50:
            self.item.quality += 1
        self.decrease_sell_in()


class BackstagePass(ItemBehavior):

    def update(self):
        if self.item.sell_in <= 0:
            self.item.quality = 0
        elif self.item.sell_in <= 5:
            self.item.quality = min(50, self.item.quality + 3)
        elif self.item.sell_in <= 10:
            self.item.quality = min(50, self.item.quality + 2)
        else:
            self.item.quality = min(50, self.item.quality + 1)
        self.decrease_sell_in()


class Sulfuras(ItemBehavior):

    def update(self):
        """ Sulfuras never changes quality or sell_in. """
        pass


class ConjuredItem(ItemBehavior):

    def update(self):
        if self.item.quality > 0:
            self.item.quality = max(0, self.item.quality - 2)
        self.decrease_sell_in()
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality = max(0, self.item.quality - 2)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            behavior = self.get_behavior(item)
            behavior.update()

    def get_behavior(self, item):
        if "Aged Brie" in item.name:
            return AgedBrie(item)
        elif "Backstage passes" in item.name:
            return BackstagePass(item)
        elif "Sulfuras" in item.name:
            return Sulfuras(item)
        elif "Conjured" in item.name:
            return ConjuredItem(item)
        else:
            return NormalItem(item)

    def get_all_the_item(self):
        return [item.name for item in self.items]
