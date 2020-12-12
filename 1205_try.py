
# 郵便番号API練習

import csv
import requests, json

def main():
  addresses = ["住所"]
  json_res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=4300942").text
  response = json.loads(json_res)
  # json型は辞書型みたいなの。ここのbreakpointで調べる。
  breakpoint()

  # 文字列にしているのは郵便番号APIにあるレスポンスパラメータ
  # formatを使って、コードをシンプルに！これで統一しよう。。。
  for address in response["results"]:
    add_info = "{0}-{1}-{2}".format(address["address1"],address["address2"],address["address3"])

    addresses.append(add_info)
    breakpoint()
    
    # ①.csvへの書き込み
    # with open("address.csv", "w") as f:
    #   writer = csv.writer(f)
    #   writer.writerows(addresses)

    # ②.txtへの書き込み(,区切りが無くなる。)
    path_w="address.txt"
    s = addresses
    with open(path_w, mode="w") as f:
      f.write(str(s))
    
    # 読み込んでターミナルに出力
    with open(path_w) as f:
      print(f.read())

  return print(addresses)

main()