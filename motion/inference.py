# -*- coding:utf-8 -*-

import os
import sys
import time
import csv

import torch
from torch import nn

from models.BiRNN import BiRNN
from data_utils import make_review_testset, read_vocab

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def infer(data_iter, net, device):
    total_result = []
    net = net.to(device)
    print("inferencing on ", device)
    for X, _ in data_iter:
        net.eval()
        results = net(X.to(device)).argmax(dim=1)
        # 记录结果
        total_result.extend(results.cpu().numpy().tolist())
    return total_result


def main(argv):
    # 载入词典并读取推理用数据
    test_file_path = "F:\\VSthings\\web-resume-resume-master\\web-resume-resume-master\\motion_classification\\reviewForInfer\\review.csv"

    vocab_path = "F:\\VSthings\\web-resume-resume-master\\web-resume-resume-master\\motion_classification\\output\\model.vocab"
    data_iter, vocab = make_review_testset(test_file_path, vocab_path)
    print("#vocab: ", len(vocab))
    print('#batches:', len(data_iter))

    # 载入模型
    model_path = "F:\\VSthings\\web-resume-resume-master\\web-resume-resume-master\\motion_classification\\output\\model.pt"
    net = torch.load(model_path)
    print("#model:", net)

    # 开始推理
    res = infer(data_iter, net, device)
    # print("#results : ", res)

    # 保存结果
    with open("F:\\VSthings\\web-resume-resume-master\\web-resume-resume-master\\motion_classification\\reviewForInfer\\review.csv", "w") as f:
        for r in res:
            f.write(str(r) + "\n")

    #合并结果
    filepath1 = 'F:\\VSthings\\web-resume-resume-master\\web-resume-resume-master\\motion_classification\\reviewForInfer\\review.csv'
    filepath2 = 'F:\\VSthings\\web-resume-resume-master\\web-resume-resume-master\\motion_classification\\reviewForInfer\\result.csv'
    # 读取result.csv文件和review.csv文件，将数据写入reviewResult.csv文件
    with open(filepath1, 'r', encoding='utf-8') as f1:
        reader1 = csv.reader(f1)
        result = list(reader1)
    with open(filepath2, 'r', encoding='utf-8') as f2:
        reader2 = csv.reader(f2)
        review = list(reader2)
    with open('reviewForInfer\\reviewResult.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['review', 'result'])
        for i in range(len(result)):
            writer.writerow([review[i][0], result[i][0]])


if __name__ == '__main__':
    main(sys.argv)
