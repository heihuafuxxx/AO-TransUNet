# import numpy as np
# import cv2
#
# # 读取 .npz 文件
# data = np.load('0.npz')
#
# # 获取图像和标签数据
# image = data['image']
# label = data['label']
#
# # 将图像和标签保存为图像文件
# cv2.imwrite('image.png', image)
# cv2.imwrite('label.png', label)
# # 读取标签图像
# label = cv2.imread('label.png', cv2.IMREAD_GRAYSCALE)
#
# # 将像素值从 0 和 1 转换为 0 和 255
# label = label * 255
#
# # 保存转换后的标签图像
# cv2.imwrite('label_255.png', label)

import numpy as np
import cv2
import os

# 设置输入和输出文件夹路径
input_folder = 'C:/shizhan/TransUnet-gai/data/Synapse/test_vol_h5'
output_folder = 'C:/shizhan/TransUnet-gai/yuan'

# 遍历输入文件夹中的所有 .npz 文件
for filename in os.listdir(input_folder):
    if filename.endswith('.npz'):
        # 读取 .npz 文件
        data = np.load(os.path.join(input_folder, filename))

        # 获取图像和标签数据
        image = data['image']
        label = data['label']

        # 将图像和标签保存为图像文件
        cv2.imwrite(os.path.join(output_folder, f'{filename}_image.png'), image)
        cv2.imwrite(os.path.join(output_folder, f'{filename}_label.png'), label)

        # 读取标签图像
        label = cv2.imread(os.path.join(output_folder, f'{filename}_label.png'), cv2.IMREAD_GRAYSCALE)

        # 将像素值从 0 和 1 转换为 0 和 255
        label = label * 255

        # 保存转换后的标签图像
        cv2.imwrite(os.path.join(output_folder, f'{filename}_label_255.png'), label)


