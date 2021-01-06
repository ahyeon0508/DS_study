from math import pi
import pandas as pd
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum

output_file("pie.html")

map_user = {
    '네이버 지도': 11125260,
    'T map': 7158903,
    'T map - 내비게이션': 5478352,
    '구글 지도': 5492460,
    '카카오맵': 5304915
}

data = pd.Series(map_user).reset_index(name='value').rename(columns={'index':'company'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(map_user)]

# 비율 데이터 추가
ratio = pd.Series(data["value"]/sum(data["value"])*100, name='ratio')
data = pd.concat([data, ratio], axis=1)

p = figure(plot_height=450, title="안드로이드OS 2020년 6월 사용자(MAU) 기준 지도 앱 사용량 분석", toolbar_location=None,
           tools="hover", tooltips="@company: @value명, @ratio%", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='company', source=data)

p.legend.label_text_font_size = '9pt'
p.legend.location = "center_right"
p.title.text_font_size = "15pt"
p.title.align = "center"

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)