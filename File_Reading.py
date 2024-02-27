import json

from Data_Structure import Record


class FileReader:

    def read_file(self) -> list[Record]:                    # 我们仅仅在这里定义了一个FileReader的抽象类或者说是接口
        pass


class TextFileReader(FileReader):

    def __init__(self, path):                               # 初始化我们的txt阅读类，将我们的文件url地址传参
        self.path = path

    def read_file(self) -> list[Record]:
        record_list: list[Record] = []
        with open(self.path, 'r', encoding="UTF-8") as f:
            for line in f.readlines():
                line = line.strip()                         # 首先去掉每行的\n换行符
                line_list = line.split(",")
                temp: Record = Record(line_list[0], line_list[1], line_list[2], line_list[3])
                record_list.append(temp)

            return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):  # 初始化我们的txt阅读类，将我们的文件url地址传参
        self.path = path

    def read_file(self) -> list[Record]:
        record_list: list[Record] = []
        with open(self.path, 'r', encoding="UTF-8") as f:

            for line in f.readlines():
                data_dict = json.loads(line)               # 先将json文件转换为字典格式
                record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
                record_list.append(record)

            return record_list


if __name__ == "__main__":

    text_reader = TextFileReader('D:/pyecharts data/2011年1月销售数据.txt')
    for element in text_reader.read_file():
        print(element.date)
        print(element.product_id)
        print(element.money)
        print(element.province)

    print("========================================================================")

    text_reader = JsonFileReader('D:/pyecharts data/2011年2月销售数据JSON.txt')
    for element in text_reader.read_file():
        print(element.date)
        print(element.product_id)
        print(element.money)
        print(element.province)
