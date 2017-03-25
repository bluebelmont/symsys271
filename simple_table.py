# Get this figure: fig = py.get_figure("https://plot.ly/~bsheffer/0/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~bsheffer/0/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="simple_table", fileopt="extend")
# Get z data of first trace: z1 = py.get_figure("https://plot.ly/~bsheffer/0/").get_data()[0]["z"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "z": [
    [0, 0, 0], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.], 
  "colorscale": [
    [0, "#00083e"], [0.5, "#ededee"], [1, "#ffffff], 
  "hoverinfo": "none", 
  "opacity": 0.75, 
  "showscale": False, 
  "type": "heatmap", 
  "zsrc": "bsheffer:1:"
}
data = Data([trace1])
layout = {
  "annotations": [
    {
      "x": -0.45, 
      "y": 0, 
      "align": "left", 
      "font": {"color": "#ffffff"}, 
      "showarrow": False, 
      "text": "<b>Variable</b>", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 0, 
      "align": "left", 
      "font": {"color": "#ffffff"}, 
      "showarrow": False, 
      "text": "<b>Scale</b>", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 0, 
      "align": "left", 
      "font": {"color": "#ffffff"}, 
      "showarrow": False, 
      "text": "<b>Krippendorff's Alpha</b>", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 1, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DREF1", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 1, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Nominal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 1, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.620786516854", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 2, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DPART", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 2, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Interval", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 2, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.634688939193", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 3, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DFPART", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 3, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Interval", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 3, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.815218302187", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 4, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DRECI", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 4, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 4, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.190382758033", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 5, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DSYMM", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 5, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 5, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.319611043766", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 6, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DPOWER", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 6, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 6, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.372167455093", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 7, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DPSOUR", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 7, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Nominal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 7, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.394347240915", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 8, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DCOOP", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 8, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 8, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.589997698324", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 9, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DCONFL", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 9, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Nominal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 9, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.088200238379", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 10, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DUNCIV", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 10, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 10, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.840135010076", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 11, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DFOCUS", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 11, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 11, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.496912190034", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 12, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DATMO", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 12, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 12, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.625498255107", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 13, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DDECMOD", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 13, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Nominal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 13, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.345238095238", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 14, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DDECOUT", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 14, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Nominal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 14, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.417647058824", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 15, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DORIGIN", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 15, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Nominal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 15, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.014175257732", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 16, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DPRESS", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 16, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 16, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "-0.142866494483", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 17, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DDECORI", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 17, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 17, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.469210879142", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 18, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DMODERA", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 18, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Nominal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 18, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "-0.0227272727273", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": -0.45, 
      "y": 19, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "DMODDIS", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 0.55, 
      "y": 19, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "Ordinal", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }, 
    {
      "x": 1.55, 
      "y": 19, 
      "align": "left", 
      "font": {"color": "#000000"}, 
      "showarrow": False, 
      "text": "0.299794033405", 
      "xanchor": "left", 
      "xref": "x1", 
      "yref": "y1"
    }
  ], 
  "height": 650, 
  "margin": {
    "r": 0, 
    "t": 0, 
    "b": 0, 
    "l": 0
  }, 
  "xaxis": {
    "dtick": 1, 
    "gridwidth": 2, 
    "showticklabels": False, 
    "tick0": -0.5, 
    "ticks": "", 
    "zeroline": False
  }, 
  "yaxis": {
    "autorange": "reversed", 
    "dtick": 1, 
    "gridwidth": 2, 
    "showticklabels": False, 
    "tick0": 0.5, 
    "ticks": "", 
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)