import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getRatio_calculateRatio(self):
    prices = [{"ABC": 119.2, "DEF": 121.68}, {"ABC": 121.2, "DEF": 120.48}]
    for price in prices:
      self.assertEqual(getRatio(price["ABC"], price["DEF"]), price["ABC"] / price["DEF"])

  def test_getRatio_calculateRatioPriceBIsZero(self):
    prices = [{"ABC": 119.2, "DEF": 0}, {"ABC": 121.2, "DEF": 0}]
    for price in prices:
      self.assertIsNone(getRatio(price["ABC"], price["DEF"]))

  def test_getRatio_calculateRatioPriceAIsZero(self):
    prices = [{"ABC": 0, "DEF": 121.68}, {"ABC": 0, "DEF": 120.48}]
    for price in prices:
      self.assertEqual(getRatio(price["ABC"], price["DEF"]), 0)

if __name__ == '__main__':
    unittest.main()
