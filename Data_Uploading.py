# 哎嘿，我们到这里就是定义我们的一个数据上传到MySQL当中的一个操作啦
from pymysql import Connection
from File_Reading import *


class Upload():
    def __init__(self, pre_uploaded_data: list[Record], month: int):
        self.pre_uploaded_data = pre_uploaded_data
        self.month = month
        print("成功初始化Upload进程")

    def upload_data(self):
        link = Connection(                      # 首先为Connection类创建一个link的对象
            host="localhost",                   # 主机名（IP）
            port=3306,                          # 端口
            user="root",                        # 账户
            password="pipinstalltqdm",          # 密码
            autocommit=True                     # 自动提交SQL命令
        )

        print(link.get_server_info())
        link.select_db("datas")                 # 统一使用我们的datas库来实现我们的功能
        cursor = link.cursor()                  # 实例化我们的游标对象
        cursor.execute(f"create table if not exists {self.month}月份数据("
                       f"日期 date,"
                       f"订单id varchar(50),"
                       f"销售额 int,"
                       f"销售省份 varchar(10)"
                       f")")                    # 在datas库当中创建一个符合我们规范的表结构
        link.commit()
        for record in self.pre_uploaded_data:   # 准备将我们传入的标准的数据插入到我们的
            cursor.execute(f"insert into {self.month}月份数据 values('{record.date}','{record.product_id}',"
                           f"'{record.money}','{record.province}')")
        link.commit()
        print("数据已经上传成功！")


