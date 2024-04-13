# DEMO
![]([https://i.imgur.com/0TW6FjR.png](https://i.imgur.com/0UdDOx4.png))
---
# HOW TO USE
---
需要準備帳號:
* [Discord](https://discord.com/)
* [replit](https://replit.com/)
* [UptimeRobot](https://uptimerobot.com/)
---
## **Step 1:**
---
>如果還沒有自己管理的伺服器，先創立一個
![](https://i.imgur.com/0TW6FjR.png)
>
>接著到[Discord Developer Portal](https://discord.com/developers/applications)創立Bot
點選New Application，輸入名稱後Create
![](https://i.imgur.com/PSp1fA0.png)
>
>到Bot介面
![](https://i.imgur.com/VZv4O78.png)
>
>把這三項打開
![](https://i.imgur.com/uWj2kDX.png)
>
>然後選取Administrator
![](https://i.imgur.com/hVWrIUh.png)
>
>再到OAuth2 -> URL Generator
![](https://i.imgur.com/uKUj0r1.png)
>
>選取bot與Administrator
![](https://i.imgur.com/hIneJUu.png)
>
>就會得到一串網址
![](https://i.imgur.com/8Zu12TW.png)
>
>進入網址後，選取要新增至哪個伺服器後繼續即可
![](https://i.imgur.com/MG8DQxM.png)
---
## **Step 2:**
---
>到[我的github](https://github.com/jush0147/discord-bot-with-crawler)把程式碼下載下來
![](https://i.imgur.com/Z8wjpHH.png)
>
>接著用記事本或vscode等文字編輯器打開main跟crawler，將id改成需要的
![](https://i.imgur.com/N0OWpz5.png)
![](https://i.imgur.com/AQtFEnk.png)
>
>就可以打開[replit](https://replit.com/) -> My Repls -> Create your first Repl，語言選擇Python並取個名稱
![](https://i.imgur.com/gFOOHZX.png)
>
>到file點右邊三個點，Upload file 把剛剛下載的程式碼上傳
![](https://i.imgur.com/Ump8g3j.png)
>
>再到左下tool點開Secrets
![](https://i.imgur.com/cKjpGQ3.png)
>
>這裡需要設定三個key，分別是TOKEN、CHANNEL_ANNOUNCE、CHANNEL_LOG
>
>TOKEN
>
>回到[Discord Developer Portal](https://discord.com/developers/applications) -> Bot -> Reset Token
![](https://i.imgur.com/ubZkkuE.png)
>
>複製貼到value即可
![](https://i.imgur.com/HkaSspL.png)
>
>CHANNEL_ANNOUNCE、CHANNEL_LOG
>
>先到discord伺服器創立兩個頻道，接著到設定->進階->打開開發者模式
![](https://i.imgur.com/QxxLnko.png)
>
>就可以到頻道上方按右鍵->複製頻道 ID貼到value
![](https://i.imgur.com/chnu8IH.png)
>
>一樣複製貼到value即可
>![](https://hackmd.io/_uploads/rJTANWENh.png)
>![](https://hackmd.io/_uploads/SkEgSWEVh.png)
>
>
>接著就可以按下Run來測試
如果是第一次Run，請先將項取消註解
![](https://hackmd.io/_uploads/rkxEEZN43.png)
>
>
>變成這樣
![](https://hackmd.io/_uploads/rk5HE-4E2.png)
>才能初始化資料庫
>Run第一次後再將那項註解，這樣就不會重複發送
>
>看到右下角的Console出現這段文字就表示成功了
>![](https://i.imgur.com/UP9AMaJ.png)
---
## **Step 3:**
>接下來要讓我們的機器人保持上線狀態，這樣wishlist有更新時才能即時收到
>這時候就要用到[UptimeRobot](https://uptimerobot.com/)
>
>點選左上角 Add New Monitor
![](https://i.imgur.com/lTykAPi.png)
>
>照著下圖設定
>![](https://i.imgur.com/m8wmj0t.png)
>
>其中URL是replit中右上方出現的網址
![](https://i.imgur.com/wekBE0T.png)
---

這樣就成功建立一個wishlist機器人了！
