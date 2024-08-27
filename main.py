# 目標網址
BASE_URL = 'https://www.ptt.cc/bbs/'

# 目標看板 (改成自己有興趣的看板)
target_board = 'Stock'

# 目標頁面
TARGET_PAGE = '/index'

# 目標頁面的頁數
page_num = ''

# 目標頁面的頁面的附屬檔名
HTML_EXT = '.html'

# 合併完整路徑
target = BASE_URL + target_board + TARGET_PAGE + page_num + HTML_EXT

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}