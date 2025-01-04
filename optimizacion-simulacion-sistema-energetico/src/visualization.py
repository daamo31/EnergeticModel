from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = Dash(__name__)

# Layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Sistema Energético Híbrido"),
    dcc.Graph(id='generacion-grafico'),
    dcc.Graph(id='consumo-grafico'),
    dcc.Graph(id='costos-emisiones-grafico'),
])

# Función para actualizar el gráfico de generación
@app.callback(
    Output('generacion-grafico', 'figure'),
    [Input('generacion-grafico', 'id')]
)
def update_generacion_graph(input_value):
    # Aquí se debe incluir la lógica para obtener los datos de generación
    # y crear el gráfico correspondiente
    figure = go.Figure()
    # Ejemplo de datos
    figure.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines+markers', name='Generación Solar'))
    figure.add_trace(go.Scatter(x=[1, 2, 3], y=[6, 5, 4], mode='lines+markers', name='Generación Eólica'))
    figure.update_layout(title='Generación de Energía', xaxis_title='Tiempo', yaxis_title='Energía (kWh)')
    return figure

# Función para actualizar el gráfico de consumo
@app.callback(
    Output('consumo-grafico', 'figure'),
    [Input('consumo-grafico', 'id')]
)
def update_consumo_graph(input_value):
    # Aquí se debe incluir la lógica para obtener los datos de consumo
    # y crear el gráfico correspondiente
    figure = go.Figure()
    # Ejemplo de datos
    figure.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 5], mode='lines+markers', name='Consumo Energético'))
    figure.update_layout(title='Consumo de Energía', xaxis_title='Tiempo', yaxis_title='Energía (kWh)')
    return figure

# Función para actualizar el gráfico de costos y emisiones
@app.callback(
    Output('costos-emisiones-grafico', 'figure'),
    [Input('costos-emisiones-grafico', 'id')]
)
def update_costos_emisiones_graph(input_value):
    # Aquí se debe incluir la lógica para obtener los datos de costos y emisiones
    # y crear el gráfico correspondiente
    figure = go.Figure()
    # Ejemplo de datos
    figure.add_trace(go.Bar(x=['Costo', 'Emisiones'], y=[1000, 200], name='Costos y Emisiones'))
    figure.update_layout(title='Costos y Emisiones de CO₂', yaxis_title='Valor')
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)