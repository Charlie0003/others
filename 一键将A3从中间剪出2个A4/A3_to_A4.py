import os
from PIL import Image


class Cutphoto:
    def __init__(self):
        self.mkdir("E:\\待处理A3")
        input('东西放好了吗?好了就回车')
        self.mkdir("E:\\处理后A4")

        # path定义要获取的文件名称的目录
        pending_path = "E:\\待处理A3\\"

        # os.listdir()方法获取文件夹名字，返回数组
        file_name_list = os.listdir(pending_path)

        # 文件名的名称变量
        a = 1
        self.cut(pending_path, file_name_list, a)

    def cut(self, pending_path, file_name_list, a):
        for name in file_name_list:
            # 获取文件绝对路径
            file_location = f"{pending_path}{name}"
            # 打开文件
            image = Image.open(file_location)
            # 获取图片尺寸
            size = image.size
            # 剪辑尺寸
            rect1 = 0, 0, size[0] / 2, size[1]
            rect2 = size[0] / 2, 0, size[0], size[1]

            a = self.crop(rect1, a, name, image)
            a = self.crop(rect2, a, name, image)
            print((f"{(a - 1) / len(file_name_list) / 2 * 100}%"))

    def crop(self, rect, a, name, image):
        image1 = image.crop(rect)
        image1.save(f'E:\\处理后A4\\{a}{os.path.splitext(name)[1]}')
        return a + 1

    def mkdir(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)


if __name__ == '__main__':
    cp = Cutphoto()