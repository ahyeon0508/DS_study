import requests
from bs4 import BeautifulSoup

# 검색어 입력 후 네이버 뷰 내용 가져오기
# 크롤링
raw = requests.get("https://search.naver.com/search.naver?where=view&sm=tab_jum&query=지도", headers={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')

info = html.select("div._more_contents_event_base div.total_wrap")

# 카테고리
category = {
    '여행' : 0,
    '맛집' : 0,
    '마을' : 0,
    '네비게이션' : 0,
    '노선' : 0,
    'other' : 0
}

# 해당 카테고리 존재시
for i in info:
    title = i.select_one("a.api_txt_lines").text
    for ca, value in category.items():
        if ca in title:
            category[ca] += 1

# 카테고리에 해당 안 되는 것들
category['other'] = len(info)-sum(category.values())

# bokeh pie 시각화
from math import pi
import pandas as pd
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum

output_file("miniProject_pie.html")

data = pd.Series(category).reset_index(name='value').rename(columns={'index':'category'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(category)]

# 비율 데이터 추가
ratio = pd.Series(data["value"]/len(info)*100, name='ratio')
data = pd.concat([data, ratio], axis=1)

p = figure(plot_height=400, title="가장 많이 찾는 지도 카테고리", toolbar_location=None,
           tools="hover", tooltips="@category: @value, @ratio%", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field="category", source=data)

p.legend.label_text_font_size = '9pt'
p.legend.location = "center_right"
p.title.text_font_size = "14pt"
p.title.align = "center"

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)