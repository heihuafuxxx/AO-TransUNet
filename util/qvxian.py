# from sklearn.metrics import precision_recall_curve, roc_curve, auc
# import matplotlib.pyplot as plt
#
# # 收集所有测试图像的预测结果和对应的真实标签
# all_gt = []
# all_pred = []
#
# # 在测试循环中添加以下代码
# all_gt.append(label.flatten())
# all_pred.append(prediction.flatten())
#
# # 将列表转换为数组
# all_gt = np.concatenate(all_gt)
# all_pred = np.concatenate(all_pred)
#
# # 计算整个测试集上的Precision-Recall曲线的平均值
# precision, recall, _ = precision_recall_curve(all_gt, all_pred)
#
# # 计算整个测试集上的ROC曲线的平均值
# fpr, tpr, _ = roc_curve(all_gt, all_pred)
#
# # 绘制Precision-Recall曲线
# plt.figure(figsize=(8, 4))
# plt.subplot(1, 2, 1)
# plt.plot(recall, precision, color='darkorange', lw=2)
# plt.xlabel('Recall')
# plt.ylabel('Precision')
# plt.title('Average Precision-Recall Curve')
#
# # 绘制ROC曲线
# plt.subplot(1, 2, 2)
# plt.plot(fpr, tpr, color='darkorange', lw=2)
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Average ROC Curve')
#
# # 调整布局并显示图形
# plt.tight_layout()
# plt.show()


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve,roc_curve

plt.figure()
plt.title('PR Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.grid()

#只是理解两种曲线的含义，所以数据简单的构造
confidence_scores = np.array([0.9,0.46,0.78,0.37,0.6,0.4,0.2,0.16])
confidence_scores=sorted(confidence_scores,reverse=True)#置信度从大到小排列
print(confidence_scores)

data_labels = np.array([1,1,0,1,0,0 ,1,1])#置信度所对应的标签

#精确率，召回率，阈值
precision,recall,thresholds = precision_recall_curve(data_labels,confidence_scores)
print(precision)
print(recall)
print(thresholds)
plt.plot(recall,precision)
plt.show()

#真正率，假正率
fpr, tpr, thresholds = roc_curve(data_labels, confidence_scores)
#print(fpr)
#print(tpr)
plt.figure()
plt.grid()
plt.title('Roc Curve')
plt.xlabel('FPR')
plt.ylabel('TPR')


