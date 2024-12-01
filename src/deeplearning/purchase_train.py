import pandas as pd
import numpy as np

np.random.seed(52)
rows = 1000
X_colums=["チョコ120円(個)",
          "アメ50円(個)",
          "ガム150円(個)"]
Y_colums=["合計金額(円)"]
df = {}
random_data = np.random.randint(0,10, size=(rows, len(X_colums)))
df = pd.DataFrame(random_data, columns=X_colums)

# 各商品の単価を設定
prices = [120, 50, 150]
# 合計金額を計算して新しい列を追加
df["合計金額(円)"] = (df * prices).sum(axis=1)

df.to_csv("purchase_test.csv", index=False, encoding="utf-8-sig")

