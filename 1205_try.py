
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
    
    with open("address.csv", "w") as f:
      writer = csv.writer(f)
      writer.writerows(addresses)

  return print(addresses)

main()