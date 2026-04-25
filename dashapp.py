from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)
df_cleaned = pd.read_csv("cleaned_sales_data.csv")
df = pd.DataFrame(df_cleaned)
fig = px.scatter(df, x="date", y = "sales", color="region", title = "Sales by Year and Region")
app.layout = html.Div(children=[
    html.H1(children='Sales Dashboard'),
    html.Div(children='''
        A dashboard to visualize sales data.
    '''),
    html.Div(children=[
        html.Div(children=[
            html.H2(children='Sales by Year and Region'),
            html.Div(children='''
                This scatter plot shows the sales by year and region.
            '''),
            dcc.Graph(
                id='sales-scatter',
                figure=fig
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
