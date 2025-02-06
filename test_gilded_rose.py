# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # New test 1
    def test_normal_item_quality_decreases(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(999, items[0].quality, "Quality should decrease by 1 each day")

    # New test 2
    def test_quality_decreases_twice_as_fast_after_sellin(self):
        items = [Item("Normal Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(999, items[0].quality, "Quality should decrease by 2 after sell-by date")

    # New test 3
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(999, items[0].quality, "Aged Brie should increase in quality")

    # New test 4
    def test_backstage_passes_quality_drops_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(999, items[0].quality, "Backstage passes should drop to 0 after the concert")
    
    # New Test 5: Syntax Error Test: Call a non-existent method
    def test_gilded_rose_get_all_items(self):
        items = [Item("Normal Item", 5, 10)]
        gilded_rose = GildedRose(items)
        
        with self.assertRaises(AttributeError):
            gilded_rose.get_all_items()


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
