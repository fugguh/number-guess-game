from datetime import date
import json
import os

DATA_FILE = "records.json"


def load_records():
    """起動時に記録をファイルから読み込む"""
    if not os.path.exists(DATA_FILE):
        return[]
    with open(DATA_FILE,"r",encoding="utf-8") as f:
        return json.load(f)
    
def save_records(records):
    """記録をファイルに保存する"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def add_record(records):
    while True:
        task = input("タスク内容を入力： ").strip()
        if task == "":
            print("タスク名を入力してください")
        else:
            break

    while True:
        try:
            minutes = int(input("時間（分）を入力： "))
            if minutes <= 0:
                print("1以上の整数を入力してください")
                continue
            break
        except ValueError:
            print("数字を入力してください")

    today = date.today().isoformat()
    record = {"date":today,"task":task,"minutes":minutes}
    records.append(record)
    save_records(records)

def list_records(records):
    if not records:
        print("まだ記録がありません")
        return
    for r in records:
            print(f"{r['date']} - {r['task']} - {r['minutes']}分")


records = load_records()

while True:
    print("\n--- メニュー ---")
    print("1: 記録を追加")
    print("2: 記録を一覧表示")
    print("q: 終了")

    cmd = input("コマンドを入力： ")


    if cmd == "1":
        add_record(records)    


    elif cmd == "2":
        list_records(records)

    elif cmd == "q":
        print("終了します。")
        break
    else:
        print("不明なコマンドです")