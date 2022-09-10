# mid2src

このプログラムは midi ファイル(コンピュータの演奏データファイル)から Arduino の tone 関数のブザープログラムを生成する Python プログラムである

## 1. Midi ファイルの作成

Midi ファイルの作成にはソフト Domino を用いる。他に midi ファイルを作成できるソフトがあればそれを使っても良い。

<http://takabosoft.com/domino>

![](media/image1.png)

Domino を用いて midi ファイルを書き出すには、SMF 書き出しを選ぶと良い。

このとき、mid2src.py があるフォルダに保存するようにする。format は 1 にする。

![](media/image2.png)
![](media/image3.png)

## 2. Python と必要なパッケージのインストール

- Windows

  1.  スタートメニューから Microsoft Store を起動する。

  ![](media/image4.png)

  2.  Python を検索し、インストールする。（3.x 系ならバージョンは何でもよい）

  ![](media/image5.png)
  ![](media/image6.png)
  ![](media/image7.png)

  3.  コマンドプロンプト or PowerShell を起動し、以下のコマンドを実行

  ```
  pip3 install mido
  ```

  ![](media/image8.png)

- Mac/Linux

  1.  Mac は homebrew、Linux の Ubuntu なら apt で Python をインストールする。
      コマンドは以下の通り

  - Mac
    ```
    brew install python
    pip3 install mido
    ```
  - Ubuntu 系

    ```
    sudo apt install python3
    pip3 install mido
    ```

    ![](media/image9.png)

## 3. 使い方

1.  cd コマンドを使って mid2src.py のあるフォルダに移動する。このとき、同じフォルダに midi ファイルを入れておく。

    ![](media/image10.png)

2.  以下のコマンドを実行する。

    ```
    python3 .\mid2src.py
    ```

3.  プログラムに従って入力する。トラックは打ち込みしたものを選ぶ。

    ![](media/image11.png)
