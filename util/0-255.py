# import numpy as np
# from PIL import Image
#
# # 打开图像文件
# image = Image.open("img.jpg")
#
# # 将图像转换为numpy数组
# image_array = np.array(image)
#
# # 将大于0的像素值设置为白色（255, 255, 255）
# new_image_array = np.where(image_array > 10, (255, 255, 255), image_array)
#
# # 将新的像素值重新设置到图像中
# new_image = Image.fromarray(new_image_array.astype(np.uint8))
#
# # 保存处理后的图像文件
# new_image.save("output_image.jpg")

import cv2
import numpy as np
"""
RGB.jpg图片转换255.jpg时一直出错！！！！！，改成灰度图.png后转换255.png才成功!!!!
"""
# 读取图像
image = cv2.imread('zzz1.png')

# 将图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 将大于0的像素值设置为白色（255）
new_image = np.where(gray_image > 0, 255, gray_image)

# 将新的像素值重新设置到图像中
new_image = cv2.cvtColor(new_image, cv2.COLOR_GRAY2BGR)

# 保存处理后的图像文件
cv2.imwrite('output_image7.png', new_image)

# from PIL import Image
# img=Image.open("xxx.png")
# for w in range(img.width):
# 	for h in range(img.height):
# 		if(img.getpixel((w,h))[1]>128):
# 			img.putpixel((w, h),(255, 255, 255))
# 		else :
# 			img.putpixel((w, h), (0, 0, 0))
# img.convert('RGB')  #转换为RGB格式
# img.save('mytest.png')
