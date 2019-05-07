import os

# 获得文件夹下所有文件名称
def list_dir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            list_dir(file_path, list_name)
        else:
            temp = ''.join(file_path.split())
            os.rename(file_path, temp)
            list_name.append(file_path)
    print(list_name)


if __name__ == '__main__':
    result = []
    list_dir('E:\pictures', result)
