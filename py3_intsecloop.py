# -*- coding: utf8 -*-

# --------    ここから 初期作業    --------
# 実行パスを追加(プログラム実行の一番最初でやるのが無難)
# モジュール検索パスは標準ライブラリのsysモジュールのsys.pathに格納されている
# プログラム終了後は、sys.pathはOSシステム等に残らない(確認済)。
# カレントディレクトリ変更(os.chdir)では「Emddable Python」ではうまくいかなかった
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# --------    ここまで 初期作業    --------


# --------    ここから 必要外部ライブラリ等の読込    --------
import time
import datetime
# --------    ここまで 必要外部ライブラリ等の読込    --------


def myfn_SecLoop(intSecLoop):

    # ベース時間を設定(現時刻をミリ秒以下を切り捨てて2秒足したところをスタートとする)
    # 以降このベース時間からサンプリングタイムを算出することで時間のズレを減らす。
    dt_0 = datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(seconds=2)


    # ループ(初回)
    cnt_lp = 1
    stopflg = True
    while stopflg:

        time.sleep(0.1)

        dt_1 = datetime.datetime.now()

        if dt_1 >= dt_0:
            # ここにループ(初回cnt_lp=1)で実施する内容を記載。
            result = 'Cnt：{}, Time：{}'.format(cnt_lp,dt_1)
            print(result)



            stopflg = False
            break


    # ループ(2回目以降)
    stopflg = True
    while stopflg:

        dt_0 = dt_0 + datetime.timedelta(seconds=intSecLoop)
        cnt_lp = cnt_lp + 1

        while True:

            time.sleep(0.1)

            dt_1 = datetime.datetime.now()

            if dt_1 >= dt_0:
                # ここにループ(2回目以降)で実施する内容を記載。
                result = 'Cnt：{}, Time：{}'.format(cnt_lp,dt_1)
                print(result)


                break


        # 動作確認用停止フラグ
        # ループが10まわったら止める
        if cnt_lp  == 10:
            stopflg = False
            break


myfn_SecLoop(5)


# スレッドを確実にKILLするのに書いておいたほうがいいかも？
sys.exit()


'''
Cnt：1, Time：2024-10-23 17:54:24.056441
Cnt：2, Time：2024-10-23 17:54:29.085310
Cnt：3, Time：2024-10-23 17:54:34.006672
Cnt：4, Time：2024-10-23 17:54:39.034618
Cnt：5, Time：2024-10-23 17:54:44.058470
Cnt：6, Time：2024-10-23 17:54:49.080702
Cnt：7, Time：2024-10-23 17:54:54.006482
Cnt：8, Time：2024-10-23 17:54:59.035126
Cnt：9, Time：2024-10-23 17:55:04.063461
Cnt：10, Time：2024-10-23 17:55:09.089821
'''

