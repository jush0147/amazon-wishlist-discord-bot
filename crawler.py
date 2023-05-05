import urllib.request as req
import bs4
from replit import db

id = "輸入你需要的id"

def crawler():

    url = "https://www.amazon.co.jp/hz/wishlist/ls/1RIS8BD1SC94Y?ref_=wl_share=" + id

    request = req.Request(
        url,
        headers={
            "User=Agnet":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
          

        })
 


    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all(
        "div",
        class_=
        "a-text-center a-fixed-left-grid-col g-itemImage wl-has-overlay g-item-sortable-padding a-col-right"
    )
    dates = root.find_all(
        "div", class_="a-fixed-right-grid-col dateAddedText a-col-right")

    title_list = []
    date_list = []

    for title in titles:
        title_list.append(title.a["title"])


    set_difference = list(set(title_list) - set(db['old_list'].value))
    db['old_list'] = title_list
    print('crawler ok')
    return set_difference