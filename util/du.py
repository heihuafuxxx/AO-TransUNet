import glob
import os


# def du(x):
#     for i in range(x):
#         print(i)
# def write_name():
#     #npz文件路径
#     files = glob.glob(r'C:\shizhan\TransUnet-gai\data\Synapse\train_npz\*.npz')
#     #txt文件路径
#     f = open(r'C:\shizhan\TransUnet-gai\TransUNet-main\lists\lists_Synapse\train.txt','w')
#     for i in files:
#         name = i.split('\\')[-1]
#         name = name[:-4]+'\n'
#         f.write(name)
#     print("ok")
def write_name():
    dir_path = r'C:\shizhan\TransUnet-gai\data\Synapse\test_vol_h5'
    file_list = os.listdir(dir_path)
    file_list.sort(key=lambda x: int(x.split('.')[0])) #问题可能是由于字符串排序而不是数字排序引起的
    f = open(r'C:\shizhan\TransUnet-gai\TransUNet-main\lists\lists_Synapse\test_vol.txt','w')
    for i, name in enumerate(file_list):
        if name.endswith('.npz') and i != len(file_list) - 1:  # 判断是否是最后一行
            f.write(name[:-4] + '\n')
        else:
            f.write(name[:-4])
    print("ok")

if __name__ == '__main__':
    # du(999)
    write_name()