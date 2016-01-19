from bokeh.charts import Bar, output_file, show, vplot
from numpy.random import rand
from pandas import DataFrame

N = 10
data = DataFrame({'A': rand(N), 'B': rand(N), 'C': rand(N)})
# Stack columns A,B,C and convert the multiindices to columns
sdata = data.stack().reset_index()
sdata.columns = ['labels', 'stack', 'values']

bar = Bar(sdata, values='values', label='labels', stack='stack', legend='top_right')
bar2 = Bar(sdata, values='values', label='labels', stack='stack', legend='top_right')
bar2.x_range = bar.x_range  # Link the x axes

output_file("stacked_bar.html")
show(vplot(bar, bar2))
