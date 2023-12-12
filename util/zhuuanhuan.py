import glob

import cv2
import numpy as np


def npz():
    # 图像路径
    # path = r'C:/shizhan/TransUnet-gai/Kvasir-SEG/train/images/*.jpg'
    path = r'C:\shizhan\TransUnet-gai\CVC-ClinicDB_PNG_datasets\images-val\*.png'
    # 项目中存放训练所用的npz文件路径
    # path2 = r'C:/shizhan/TransUnet-gai/data/Synapse/train_npz//'
    path2 = r'C:\shizhan\TransUnet-gai\data\Synapse\test_vol_h5\\'

    # image1 = r'C:\shizhan\TransUnet-gai\kvasir-instrument\labels\*.'  如果光定义image1，因为下面没有使用所以是灰的而且*.png时不会自动补全！！
    for i, img_path in enumerate(glob.glob(path)):
        # 读入图像
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 读入标签
        """
        label_path = img_path.replace('images', 'labels')   #不是masks，读懂代码！！！！
        label_path = img_path.replace('jpg', 'png')       #不能分开替换！！！！要一起连续替换
        下面这个才对！！！
        label_path = img_path.replace('images', 'labels')  
        label_path = label_path.replace('jpg', 'png')
        或者label_path = img_path.replace('images', 'labels').replace('jpg', 'png')
        """

        label_path = img_path.replace('images', 'labels')
        # label_path = img_path.replace('images', 'labels').replace('jpg', 'png')

        label = cv2.imread(label_path, flags=0)
        # label = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)

        # 检查并调整像素值范围
        min_val = np.min(label)
        max_val = np.max(label)
        if min_val < 0 or max_val >= 2:
            label = np.clip(label, 0, 2 - 1)

        # # 处理标签，将像素值为255的改为1  试试这个？？？？
        # if label.max() > 1:
        #     label = label / 255

        # 保存npz
        np.savez(path2 + str(i), image=image, label=label)
        print('------------', i)

    #加载npz文件
        # data = np.load(r'C:\shizhan\TransUnet-gai\data\Synapse\train_npz\12.npz', allow_pickle=True)
        # image, label = data['image'], data['label']


        # print("image", image.size)
        # print("image", image.shape)
        # print("label", label.size)
        # print("label", label.shape)


    print('ok')

def xxx():
    data = np.load(r'C:\shizhan\TransUnet-gai\case0005_slice000.npz', allow_pickle=True)
    data1 = np.load(r'C:\shizhan\TransUnet-gai\data\Synapse\train_npz\12.npz', allow_pickle=True)
    image, label = data['image'], data['label']
    image1, label1 = data1['image'], data1['label']

    print("image", image.size)
    print("image", image.shape)
    print("label", label.size)
    print("label", label.shape)
    print("image", image1.size)
    print("image", image1.shape)
    print("label", label1.size)
    print("label", label1.shape)

npz()
# xxx()