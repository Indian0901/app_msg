import yaml, os


def get_data():
    # 返回 yaml文件数据 [(),(),()]
    # 存储读取数据
    data_list = []
    with open('E:\\就业班\\20190125\\me\\app_code08_3\\Data\\book.yml', "r") as f:
        data = yaml.load(f)
        for i in data.get("data"):
            # 数据组装
            data_list.append(i)
    return data_list


# print(get_data())