#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import sys

def main():
    # ファイルの読み込み
    adf = pd.read_csv('answer_files/answer.csv')
    pdf = pd.read_csv('answer_files/predict.csv')
    # 予測結果の名前変更
    pdf = pdf.rename(columns={'No-show': 'No-show-pre'})

    # テスト用
    if pdf['No-show-pre'].isnull().all():
        pdf['No-show-pre'] = np.random.randint(0,2, size=len(pdf['No-show-pre']))

    # AppointmentIDを利用してデータフレームを結合する
    try:
        df = pd.merge(adf, pdf, on='AppointmentID')
    except:
        sys.exit('DataFrame Merge Error! \n' +
        'Can not merge DataFrames with the AppointmentID. ' +
        'Please check your csv file.')
        
    # データフレームの長さがおかしいときにエラーを吐く
    assert len(df.index) == len(adf), 'DataFrame length Error!'

    # 正解率を計算してreturnする
    return len(df[df['No-show'] == df['No-show-pre']]) / len(df) * 100

if __name__ == '__main__':
    accuracy = main()

    print('Accuracy rate: {} %'.format(accuracy))
