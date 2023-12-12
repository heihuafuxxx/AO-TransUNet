import os, random, shutil


def moveimg(fileDir, tarDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.3  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + "\\" + name)
    return


def movelabel(file_list, file_label_train, file_label_val):
    for i in file_list:
        if i.endswith('.png'):
            # filename = file_label_train + "\\" + i[:-4] + '.xml'  # 可以改成xml文件将’.txt‘改成'.xml'就可以了
            filename = file_label_train + "\\" + i[:-4] + '.png'  # 可以改成xml文件将’.txt‘改成'.xml'就可以了
            if os.path.exists(filename):
                shutil.move(filename, file_label_val)
                print(i + "处理成功！")


if __name__ == '__main__':
    fileDir = r"C:\shizhan\TransUnet-gai\CVC-ClinicDB_PNG_datasets\images" + "\\"  # 源图片文件夹路径
    tarDir = r'C:\shizhan\TransUnet-gai\CVC-ClinicDB_PNG_datasets\images-val'  # 图片移动到新的文件夹路径
    moveimg(fileDir, tarDir)
    file_list = os.listdir(tarDir)
    file_label_train = r"C:\shizhan\TransUnet-gai\CVC-ClinicDB_PNG_datasets\labels"  # 源图片标签路径
    file_label_val = r"C:\shizhan\TransUnet-gai\CVC-ClinicDB_PNG_datasets\labels-val"  # 标签
    # 移动到新的文件路径
    movelabel(file_list, file_label_train, file_label_val)
    '''
    代码的原理是将一个文件夹里面的图片按一定的比例（可以自己设定，修改第7行中的rate的值就可以了）
    抽取照片放入到一个新的文件夹里面（需要自己新建一个文件夹）。这样源文件夹就变成了训练集images，新建的为验证集images-val。
    然后代码会将抽取照片对应的标签文件labels放入到一个新建的文件夹中labels-val（该文件夹需要新建）。
    这样我们就有图片的训练集和验证集，还有其对应的标签文件。使用同样的代码还可以将数据集多划分一个测试集出来，这样方便测试用。
    '''