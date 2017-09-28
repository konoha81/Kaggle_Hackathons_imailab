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

正解データは answer_files 内の answer.csv に存在します。

hackathonディレクトリ上で score_calculator.py を実行すると、<br>
answer_files内のanswer.csvとpredict.csvのラベルを比較し、正解率を出力します。

```bash
$ python score_calculator.py
Accuracy rate: 49.808058216777376 %
```
