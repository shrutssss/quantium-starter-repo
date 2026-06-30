from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

DATA_PATH = "./formatted_data.csv"

data = pd.read_csv(DATA_PATH)
data = data.sort_values(by = "date")

app = Dash(__name__)

line_chart = px.line(data, x = "date", y = "sales", title = "Pink Morsel Sales")
line_chart.update_traces(line_color = 'pink')

app.layout = html.Div(
    children = [
        html.H1(children = 'Hello Soul Foods'),
        html.H3(children = "Visualizing Pink Morsel Sales: "),
        dcc.Graph(id="example-graph", figure = line_chart)
    ]
)

if __name__ == '__main__':
    app.run(debug = True)