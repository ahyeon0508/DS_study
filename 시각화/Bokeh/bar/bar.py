## 연속형 데이터
# vbar
from bokeh.plotting import figure, output_file, show

output_file('vbar.html')

p = figure(plot_width=500, plot_height=500)
p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
       top=[4, 6.2, 7.0], color="blue")

show(p)

# hbar
from bokeh.plotting import figure, output_file, show

output_file('hbar.html')

p = figure(plot_width=500, plot_height=500)
p.hbar(y=[1, 2, 3], height=0.5, left=0,
       right=[4, 6.2, 7.0], color="gray")

show(p)

## 범주형 데이터
# vbar
from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("bars.html")

fruits = ['Apples', 'Pears', 'bananas', 'lemons']
price = [5500, 3000, 4200, 2200]

p = figure(x_range=fruits, plot_height=250, title="Fruit Price",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=price, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)

# hbar
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure

output_file("stacked.html")

fruits = ['Apples', 'Pears', 'bananas', 'lemons']
years = ["2015", "2016", "2017"]

data = {'fruits' : fruits,
        '2015'   : [2000, 4000, 1600, 1500],
        '2016'   : [5000, 3200, 2400, 2000],
        '2017'   : [1500, 2500, 2000, 4000]}

p = figure(y_range=fruits, plot_height=300, plot_width=900, x_range=(0, 10000), title="Fruit Counts by Year",
           toolbar_location=None)

p.hbar_stack(years, y='fruits', height=0.9, color=GnBu3, source=ColumnDataSource(data), legend_label=years)

p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_right"

show(p)
