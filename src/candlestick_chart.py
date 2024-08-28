import plotly.graph_objs as go
from data_loader import load_data

def plot_candlestick_chart(data):
    # Create a candlestick chart of the historical stock prices
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
                
    fig.update_layout(title='Nifty 50 Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=False)
    fig.show()
    

