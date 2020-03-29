import datetime as dt
from config import (
    REGION_KEY, MAIN_TYPES, ITEN_MAP, DATE_FMT, PROVINCE_KEY
)


DATES = []
ICU = []
HOSP_W_SYMPTS = []
TOT_DEATHS = []
TOT_HOSP = []
SELF_ISOL = []
TOT_CURR_POS = []
NEW_CURR_POS = []
TOT_SWABS = []
HEALED = []
TOT_CASES = []


def get_provinces(provincial_data):
    return sorted({
        d[PROVINCE_KEY]
        for d in provincial_data if d[PROVINCE_KEY] != ""
    })


def get_regions(regional_data):
    """
    Return a sorted list of regions in regional_data
    :param regional_data: lisrt
    :return: list
    """
    return sorted({d[REGION_KEY] for d in regional_data})


def get_trend(data, province=False):
    """
    Return a list of dicts of the daily trend wrt to the previous day
    :param data: ascending sorted list of daily dicts
    :param province: bool
    :return: list of dicts
    """
    if not province:
        main_types = MAIN_TYPES
    else:
        main_types = ["totale_casi"]
    last = data[-1]
    penultimate = data[-2]
    trend = []
    for key in main_types:
        if penultimate[key] > last[key]:
            status = "happy"
        elif penultimate[key] == last[key]:
            status = "neutral"
        else:
            status = "sad"
        trend.append({
            "name": ITEN_MAP[key],
            "count": last[key],
            "status": status
        })
    return trend


def build_series(province=False):
    """
    Return the series array to be used in the chart
    :return: list
    """
    if not province:
        series1 = {
            "name": "New currently positive",
            "data": NEW_CURR_POS,
            "visible": "true"
        }
        series2 = {"name": "Intensive Care Unit", "data": ICU}
        series3 = {"name": "Currently positive", "data": TOT_CURR_POS}
        series4 = {"name": "Hospitalized with symptoms", "data": HOSP_W_SYMPTS}
        series5 = {"name": "Self Isolation", "data": SELF_ISOL}
        series6 = {"name": "Total Healed", "data": HEALED}
        series7 = {"name": "Total Hospitalized", "data": TOT_HOSP}
        series8 = {"name": "Total Deaths", "data": TOT_DEATHS}
        series9 = {"name": "Total Cases", "data": TOT_CASES}
        series10 = {"name": "Total Swabs", "data": TOT_SWABS}
        series = [
            series1, series2, series3, series4, series5,
            series6, series7, series8, series9, series10
        ]
    else:
        series = [{
            "name": "Total Cases",
            "data": TOT_CASES,
            "visible": "true"
        }]
    return series


def parse_data(data, region=None, province=None):
    """
    Return dates, series, trend, and regions
    :param data: dict
    :param region: str
    :param province: str
    :return:
        DATES: list,
        series: list,
        trend: list,
        regions: list
        province: list
    """
    regional_data = data["regional"]
    regions = get_regions(regional_data)
    provincial_data = data["provincial"]
    provinces = get_provinces(provincial_data)
    if region is None and province is None:
        national_data = data["national"]
        trend = get_trend(national_data)
        for d in national_data:
            fill_data(d)
    else:
        if province is None and region is not None:
            subset = [r for r in regional_data if r[REGION_KEY] == region]
            trend = get_trend(subset)
            for d in regional_data:
                if region == d[REGION_KEY]:
                    fill_data(d)
        else:
            subset = [r for r in provincial_data if r[PROVINCE_KEY] == province]
            trend = get_trend(subset, province=True)
            for d in provincial_data:
                if province == d[PROVINCE_KEY]:
                    fill_data(d, province=True)
    if province is None:
        series = build_series()
    else:
        series = build_series(province=True)
    return DATES, series, trend, regions, provinces


def fill_data(datum, province=False):
    """
    Fill the data series lists
    :param datum: dict
    :param province: bool
    :return: None
    """
    if not province:
        ICU.append(datum["terapia_intensiva"])
        HOSP_W_SYMPTS.append(datum["ricoverati_con_sintomi"])
        TOT_DEATHS.append(datum["deceduti"])
        HEALED.append(datum["dimessi_guariti"])
        TOT_HOSP.append(datum["totale_ospedalizzati"])
        SELF_ISOL.append(datum["isolamento_domiciliare"])
        TOT_CURR_POS.append(datum["totale_attualmente_positivi"])
        NEW_CURR_POS.append(datum["nuovi_attualmente_positivi"])
        TOT_SWABS.append(datum["tamponi"])
    date_dt = dt.datetime.strptime(datum["data"], DATE_FMT)
    date_str = date_dt.strftime("%d %b")
    DATES.append(date_str)
    TOT_CASES.append(datum["totale_casi"])


def init_data():
    """
    Empty data series lists
    :return: None
    """
    DATES.clear()
    ICU.clear()
    HOSP_W_SYMPTS.clear()
    TOT_DEATHS.clear()
    TOT_HOSP.clear()
    SELF_ISOL.clear()
    TOT_CURR_POS.clear()
    NEW_CURR_POS.clear()
    TOT_SWABS.clear()
    HEALED.clear()
    TOT_CASES.clear()


def init_chart(chart_id, chart_type, dates):
    """
    Return chart, x_axis, y_axis dicts to be served to the frontend
    :param chart_id: str
    :param chart_type: str
    :param dates: list
    :return:
        chart: dict,
        x_axis: dict,
        y_axis:  dict
    """
    chart = {"renderTo": chart_id, "type": chart_type}
    x_axis = {"categories": dates}
    y_axis = {"title": {"text": '# of people'}}
    return chart, x_axis, y_axis