# Kaggle_Hackathons_imailab
```
.
├── README.md  <-- here
└── hackathon
    ├── answer_files
    │   ├── answer.csv  (正解データ)
    │   └── predict.csv  (予測データ)
    ├── data
    │   ├── KaggleV2-May-2016.csv  (元データ)
    │   ├── test_data.csv  (テストデータ)
    │   └── train_data.csv  (トレーニングデータ)
    ├── data_randomsampling.ipynb  (data作成用。データが書き変わるので実行しない！)
    └── score_calculator.py  (正解率計算用)
```

<b>Medical Appointment No Shows</b><br>
https://www.kaggle.com/joniarroba/noshowappointments

data/train_data.csv: 80,570件<br>
data/test_data.csv: 29,957件<br>

train_data.csv を利用して作成したモデルを test_data.csv に適用することで、
各`AppointmentID` に対する `No-show`ラベルを予想し、predict.csv を作成してください。

<b>answer_files/predict.csv</b>
- 1行目はHeaderで、その後に29,957行 x 2列のデータのcsv
- 1列目が予約IDを示す`AppointmentID`, 2列目が来院しなかったかを示す`No-show`

正解データは answer_files/answer.csv です。こちらの中身は見ないように気をつけてください。

hackathonディレクトリ上で score_calculator.py を実行すると、<br>
answer_files 内の answer.csv と predict.csv のラベルを比較し、以下のように正解率を出力します。

```bash
$ python score_calculator.py
Accuracy rate: 49.808058216777376 %
```

predict.csv はデフォルトでは`No-show`列が空となっています。<br>
score_calculator.py は predict.csv の`No-show`列が全て空の場合のみ、ランダムで 0, 1 を入力して<br>
answer.csv と比較した結果の正解率を出力します。ご自身の環境でちゃんと動くかのテストにお使いください。
