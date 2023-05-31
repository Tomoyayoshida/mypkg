# ROSパッケージ
## リポジトリ概要　
**時計のような表示を行うROSパッケージ**

robosys2020 task2

## 改造内容
- 講義中に作成したROSを用いデジタル時計のような数値を返すように改造した。
## 動作環境
- Ubuntu 20.04
- Raspberry Pi 4 Model B

## インストール方法
`$ cd catkin_ws/src`に移動

`$ git clone　https://github.com/Tomoyayoshida/mypkg.git` しリポジトリをクローン

`$ cd mypkg/scripts`に移動

`$　chmod +x count.py`と`$　chmod +x time.py`を入力し実行可能にする

`$ cd ~/catkin_ws/`catkin_ws上に移動し`catkin_make`

## 使用方法
`$ roslaunch mypkg mypkg.launch`で起動

`$ rostopic echo /time`で時間のlaunchからの経過時間の確認

`data : 122`この場合は1分22秒を示す

## デモ動画
~~https://www.youtube.com/watch?v=H0TVblQgT6M~~ 大学の垢が使えなくなったため見れなくなりました。
## 作成者
Tomoya yoshida and Ryuichi Ueda 
## license
BSD-3-Clause-License
