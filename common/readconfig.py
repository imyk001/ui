import configparser

class readcongif(object):
    class readConfig(object):
        def __init__(self):
            # 创建对象
            self.conf = configparser.ConfigParser()
            # 读取文件
            self.conf.read(r'../config.ini', encoding='utf-8-sig')

        def get_emain(self, name):
            # 获取文件内容
            return self.conf.get('EMAIL', name)

    if __name__ == '__main__':
        re = readConfig()
        print(re.get_emain('mail_user'))