# Kaggle_Hackathons_imailab
```
.
├── README.md  <-- here
└── hackathon
    ├── answer_files
    │   ├── answer.csv
    │   └── predict.csv
    ├── data
    │   ├── KaggleV2-May-2016.csv
    │   ├── test_data.csv
    │   └── train_data.csv
    ├── data_randomsampling.ipynb
    └── score_calculator.py
```

<b>Medical Appointment No Shows</b><br>
https://www.kaggle.com/joniarroba/noshowappointments

data/train_data: 80,570件<br>
data/test_data: 29,957件<br>

train_data を利用して作成したモデルを test_data に適用することで、
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
score_calculator.py は`No-show`列が全て空の場合のみランダムで 0, 1 を入力して<br>
answer.csv と比較した結果の正解率を出力します。ご自身の環境でちゃんと動くかのテストにお使いください。
