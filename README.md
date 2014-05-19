#Bloom
花を咲かせたいらしい。（詳しいことは知らない）
for [@kazu_1995](https://twitter.com/kazu_1995)

## 用意するもの

- RPi

- PC

- 携帯（テザリングできるもの）

- お花


## 使い方

1. RPiとお花をつなぐ。 （GPIO23番と、テキトーなGNDにつなぐ。）
![RPiの図](http://openrtm.org/openrtm/sites/default/files/5274/raspberrypi_gpio_pinassign.png)

2. RPiとPCをテザリングにつなぐ。（3つの機器すべてが同じLAN内に無いといけない）

3. （携帯）RPiのIPアドレスを調べる。（携帯のテザリング画面からIPアドレス見えるよ。）

4. （PC）PCからRPiにTeraTerm使ってSSHでつなぐ

5. （PC）以下のコマンドを実行する。

```
cd bloom
sudo ./bloom.py
```

6. （携帯）携帯から http://RPiのIPアドレス:5000にアクセスする。（例： http://192.168.0.17:5000）

7. （携帯）信号を送りたい時に Bloom! ボタンを押す。

8. （携帯）信号を止めたくなったら Stop! ボタンを押す。

9. （携帯）6，7の繰り返しできるヨ

## 参考動画
[参考動画はコチラ](https://www.dropbox.com/s/yk51vr9xdgg6pz9/MOV_0159.mp4)

