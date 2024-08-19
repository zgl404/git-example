import unittest
import requests

class BaiduMapAPITest(unittest.TestCase):
    BASE_URL = "http://api.map.baidu.com/geocoding/v3/"
    AK = "your_ak_here"  # 替换为你的百度地图API密钥

    def test_geocoding(self):
        address = "北京市海淀区中关村"
        params = {
            "address": address,
            "output": "json",
            "ak": self.AK
        }


     def test_reverse_geocoding(self):
        location = "39.983424,116.306477"
        params = {
            "location": location,
            "output": "json",
            "ak": self.AK
        }
        response = requests.get(self.BASE_URL, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], 0)
        self.assertIn("result", data)
        self.assertIn("addressComponent", data["result"])
        self.assertIn("city", data["result"]["addressComponent"])
    def test_reverse_geocoding(self):
        location = "39.983424,116.306477"
        params = {
            "location": location,
            "output": "json",
            "ak": self.AK
        }
        response = requests.get(self.BASE_URL, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], 0)
        self.assertIn("result", data)
        self.assertIn("addressComponent", data["result"])
        self.assertIn("city", data["result"]["addressComponent"])

if __name__ == '__main__':
    unittest.main()
