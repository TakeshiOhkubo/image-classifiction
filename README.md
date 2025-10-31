# image-classifiction
image classification using supervising images


仮想環境を使ったインストール：
py -3.9 -m pip install  --upgrade pip
py -3.9 -m venv ImageClassifier
cd ImageClassifier
cd Scripts
activate
python.exe -m pip install --upgrade pip
pip install image-classifier

Scritsフォルダの中に
imageclassify-2021-7-17.py
を置く。フォルダの中に教師画像を置く。

python imageclassify-2021-7-17.py


既に皮膚診断スマホアプリもありますが、opencvよりも用意する教師画像の数が大幅に減るのが利点でしょうか？
放射線科、皮膚科、眼科、病理診断科 等に役立つ事を願います。
アルゴリズムがk-meansなのか？CNNか？や、教師画像が何枚必要か？や、過学習にならないepoch数は？等は大学の研究者逹が検証してくれる筈です。
