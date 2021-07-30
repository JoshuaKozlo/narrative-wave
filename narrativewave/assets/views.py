import pandas as pd
import plotly
import plotly.express as px
from django.http import JsonResponse
from django.shortcuts import render
from plotly.offline.offline import plot

# Load Data

data = pd.read_parquet('../data/parquet')

def index(request, id):
  query = data.loc[data['asset'] == id.upper()]

  # Get request query params
  start_date = request.GET.get('start_date', None)
  end_date = request.GET.get('end_date', None)
  column = request.GET.get('column', None)

  # Validate start_date and end_date
  try:
    if start_date:
      query = query.loc[query['timestamp'] >= start_date]

    if end_date:
      query = query.loc[query['timestamp'] <= end_date]
  except:
    return JsonResponse({ "error": "invalid date format use (month-day-year)"}, status=400)

  # Validate column
  try:
    if column:
      query = query[['asset', 'timestamp', column]]
  except:
    return JsonResponse({ "error": f"no column {column}"}, status=400)

  # 200
  return JsonResponse({ "assets": query.to_dict('records') }, json_dumps_params={'indent': 2})




def home(request): 
  # Create plotly figure
  fig = px.line(
    data.loc[data['asset'] == 'WTG01'], 
    x='timestamp', 
    y='hvtrafo_phase2_temp_avg'
  )

  graph_div = plotly.offline.plot(fig, auto_open=False, output_type='div')

  return render(request, 'index.html', { 'graph_div': graph_div })