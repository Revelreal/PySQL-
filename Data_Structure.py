# 我们首先在这里定义我们的一个类结构体
class Record:

    def __init__(self, date, product_id, money, province):                  # 定义Record类的初始化
        self.date = date
        self.product_id = product_id
        self.money = money
        self.province = province
