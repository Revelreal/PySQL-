
from Data_Uploading import *


text_reader = TextFileReader('D:/pyecharts data/2011年1月销售数据.txt')                   # 将我们的类实例化为对象
upload_text = Upload(text_reader.read_file(), 1)
upload_text.upload_data()

json_reader = JsonFileReader('D:/pyecharts data/2011年2月销售数据JSON.txt')               # 将我们的类实例化为对象
upload_json = Upload(json_reader.read_file(), 2)
upload_json.upload_data()
