# Quick Start

`git clone https://github.com/JoshuaKozlo/narrative-wave.git`

`cd narrative-wave`

## Virtual Environment

`python -m venv env`

`source env/Scripts/activate`

## Install dependencies

`pip install -r requirements.txt`

## Run app

`cd narrativewave`

`python manage.py runserver`

- localhost:8000 to view homepage with graph

## API

localhost:8000/assets/{asset}

### Query Params

- start_date
- end_date
- column

### Examples

- localhost:8000/assets/WTG01
- localhost:8000/assets/WTG01?start_date=10-10-20
- localhost:8000/assets/WTG02?column=gen_bear_temp_avg

# Run Notebook

`jupyter notebook`
