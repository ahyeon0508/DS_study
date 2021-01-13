import requests
from bs4 import BeautifulSoup

# 키워드
keyword = ['전주', '서울', '방배동', '서신동']

# 지도 점유율
map_list = ['여행', '맛집', '마을', '네비게이션', '노선', 'other']
key_cnt = {}

for key in keyword:
    cnt = [0, 0, 0, 0, 0, 0]

    # 검색어 입력 후 뷰 타이틀 가져오기
    raw = requests.get("https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + key, headers={"User-Agent":"Mozilla/5.0"})

    html = BeautifulSoup(raw.text, 'html.parser')

    info = html.select("div._more_contents_event_base div.total_wrap")

    for i in info:
        title = i.select_one("a.api_txt_lines").text

        for j in range(5):
            if map_list[j] in title:
                cnt[j] = cnt[j] + 1

    map_cnt = sum(cnt)
    cnt[5] = len(info) - map_cnt

    # 딕셔너리
    key_cnt[key] = cnt

# 시각화
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, Legend
from bokeh.plotting import figure

output_file("miniProject_bar.html")

data = {'key' : keyword}

for i in range(len(map_list)):
    data_cnt = []

    for j in key_cnt.keys():
        data_cnt.append(key_cnt[j][i])

    data[map_list[i]] = data_cnt

p = figure(y_range=keyword, plot_height=400, plot_width=900, x_range=(0, 30), title="네이버 뷰 지도 카테고리", toolbar_location=None)

r = p.hbar_stack(map_list, y='key', height=0.5, color=('#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef'), source=ColumnDataSource(data))

legend = Legend(items=[(x, [r[i]]) for i, x in enumerate(map_list)], location=(250, 10))

p.add_layout(legend, 'above')

p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None

p.legend.orientation = "horizontal"
p.legend.label_text_font_size = '8pt'
p.legend.click_policy = "hide"

p.title.text_font_size = "15pt"
p.title.align = 'center'

show(p)