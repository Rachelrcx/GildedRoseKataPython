# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # New Test 1: Normal item quality decreases by 1 each day
    def test_normal_item_quality_decreases(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(19, items[0].quality, "Quality should decrease by 1 each day")

    # New Test 2: Quality decreases twice as fast after sell date passes
    def test_quality_decreases_twice_as_fast_after_sellin(self):
        items = [Item("Normal Item", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(8, items[0].quality, "Quality should decrease by 2 after sell-by date")

    # New Test 3: "Aged Brie" increases in quality over time
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(11, items[0].quality, "Aged Brie should increase in quality")

    # New Test 4: "Backstage passes" drop to 0 after the concert
    def test_backstage_passes_quality_drops_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality, "Backstage passes should drop to 0 after the concert")

    # New Test 5: Syntax Error Test: Call a non-existent method
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)

        with self.assertRaises(AttributeError):
            gilded_rose.get_item()  # ❌ This method does not exist, should raise an error

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)


if __name__ == '__main__':
    unittest.main()
