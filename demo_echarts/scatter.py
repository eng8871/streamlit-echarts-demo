from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


def render_scatter_simple():
    options = {
        "xAxis": {},
        "yAxis": {},
        "series": [
            {
                "symbolSize": 20,
                "data": [
                    [10.0, 8.04],
                    [8.07, 6.95],
                    [13.0, 7.58],
                    [9.05, 8.81],
                    [11.0, 8.33],
                    [14.0, 7.66],
                    [13.4, 6.81],
                    [10.0, 6.33],
                    [14.0, 8.96],
                    [12.5, 6.82],
                    [9.15, 7.20],
                    [11.5, 7.20],
                    [3.03, 4.23],
                    [12.2, 7.83],
                    [2.02, 4.47],
                    [1.05, 3.33],
                    [4.05, 4.96],
                    [6.03, 7.24],
                    [12.0, 6.26],
                    [12.0, 8.84],
                    [7.08, 5.82],
                    [5.02, 5.68],
                ],
                "type": "scatter",
            }
        ],
    }
    st_echarts(options=options, height="500px")


def render_anscombe_quartet():
    data = [
        [
            [10.0, 8.04],
            [8.0, 6.95],
            [13.0, 7.58],
            [9.0, 8.81],
            [11.0, 8.33],
            [14.0, 9.96],
            [6.0, 7.24],
            [4.0, 4.26],
            [12.0, 10.84],
            [7.0, 4.82],
            [5.0, 5.68],
        ],
        [
            [10.0, 9.14],
            [8.0, 8.14],
            [13.0, 8.74],
            [9.0, 8.77],
            [11.0, 9.26],
            [14.0, 8.10],
            [6.0, 6.13],
            [4.0, 3.10],
            [12.0, 9.13],
            [7.0, 7.26],
            [5.0, 4.74],
        ],
        [
            [10.0, 7.46],
            [8.0, 6.77],
            [13.0, 12.74],
            [9.0, 7.11],
            [11.0, 7.81],
            [14.0, 8.84],
            [6.0, 6.08],
            [4.0, 5.39],
            [12.0, 8.15],
            [7.0, 6.42],
            [5.0, 5.73],
        ],
        [
            [8.0, 6.58],
            [8.0, 5.76],
            [8.0, 7.71],
            [8.0, 8.84],
            [8.0, 8.47],
            [8.0, 7.04],
            [8.0, 5.25],
            [19.0, 12.50],
            [8.0, 5.56],
            [8.0, 7.91],
            [8.0, 6.89],
        ],
    ]

    line_opt = {
        "animation": False,
        "label": {"formatter": "y = 0.5 * x + 3", "align": "right"},
        "lineStyle": {"type": "solid"},
        "tooltip": {"formatter": "y = 0.5 * x + 3"},
        "data": [
            [{"coord": [0, 3], "symbol": None}, {"coord": [20, 13], "symbol": None}]
        ],
    }

    option = {
        "title": {"text": "Anscombe's quartet", "left": "center", "top": 0},
        "grid": [
            {"left": "7%", "top": "7%", "width": "38%", "height": "38%"},
            {"right": "7%", "top": "7%", "width": "38%", "height": "38%"},
            {"left": "7%", "bottom": "7%", "width": "38%", "height": "38%"},
            {"right": "7%", "bottom": "7%", "width": "38%", "height": "38%"},
        ],
        "tooltip": {"formatter": "Group {a}: ({c})"},
        "xAxis": [
            {"gridIndex": 0, "min": 0, "max": 20},
            {"gridIndex": 1, "min": 0, "max": 20},
            {"gridIndex": 2, "min": 0, "max": 20},
            {"gridIndex": 3, "min": 0, "max": 20},
        ],
        "yAxis": [
            {"gridIndex": 0, "min": 0, "max": 15},
            {"gridIndex": 1, "min": 0, "max": 15},
            {"gridIndex": 2, "min": 0, "max": 15},
            {"gridIndex": 3, "min": 0, "max": 15},
        ],
        "series": [
            {
                "name": "I",
                "type": "scatter",
                "xAxisIndex": 0,
                "yAxisIndex": 0,
                "data": data[0],
                "markLine": line_opt,
            },
            {
                "name": "II",
                "type": "scatter",
                "xAxisIndex": 1,
                "yAxisIndex": 1,
                "data": data[1],
                "markLine": line_opt,
            },
            {
                "name": "III",
                "type": "scatter",
                "xAxisIndex": 2,
                "yAxisIndex": 2,
                "data": data[2],
                "markLine": line_opt,
            },
            {
                "name": "IV",
                "type": "scatter",
                "xAxisIndex": 3,
                "yAxisIndex": 3,
                "data": data[3],
                "markLine": line_opt,
            },
        ],
    }
    st_echarts(options=option, height="600px")


def render_scatter_single_axis():
    hours = [
        "12a",
        "1a",
        "2a",
        "3a",
        "4a",
        "5a",
        "6a",
        "7a",
        "8a",
        "9a",
        "10a",
        "11a",
        "12p",
        "1p",
        "2p",
        "3p",
        "4p",
        "5p",
        "6p",
        "7p",
        "8p",
        "9p",
        "10p",
        "11p",
    ]
    days = [
        "Saturday",
        "Friday",
        "Thursday",
        "Wednesday",
        "Tuesday",
        "Monday",
        "Sunday",
    ]
    data = [
        [0, 0, 5],
        [0, 1, 1],
        [0, 2, 0],
        [0, 3, 0],
        [0, 4, 0],
        [0, 5, 0],
        [0, 6, 0],
        [0, 7, 0],
        [0, 8, 0],
        [0, 9, 0],
        [0, 10, 0],
        [0, 11, 2],
        [0, 12, 4],
        [0, 13, 1],
        [0, 14, 1],
        [0, 15, 3],
        [0, 16, 4],
        [0, 17, 6],
        [0, 18, 4],
        [0, 19, 4],
        [0, 20, 3],
        [0, 21, 3],
        [0, 22, 2],
        [0, 23, 5],
        [1, 0, 7],
        [1, 1, 0],
        [1, 2, 0],
        [1, 3, 0],
        [1, 4, 0],
        [1, 5, 0],
        [1, 6, 0],
        [1, 7, 0],
        [1, 8, 0],
        [1, 9, 0],
        [1, 10, 5],
        [1, 11, 2],
        [1, 12, 2],
        [1, 13, 6],
        [1, 14, 9],
        [1, 15, 11],
        [1, 16, 6],
        [1, 17, 7],
        [1, 18, 8],
        [1, 19, 12],
        [1, 20, 5],
        [1, 21, 5],
        [1, 22, 7],
        [1, 23, 2],
        [2, 0, 1],
        [2, 1, 1],
        [2, 2, 0],
        [2, 3, 0],
        [2, 4, 0],
        [2, 5, 0],
        [2, 6, 0],
        [2, 7, 0],
        [2, 8, 0],
        [2, 9, 0],
        [2, 10, 3],
        [2, 11, 2],
        [2, 12, 1],
        [2, 13, 9],
        [2, 14, 8],
        [2, 15, 10],
        [2, 16, 6],
        [2, 17, 5],
        [2, 18, 5],
        [2, 19, 5],
        [2, 20, 7],
        [2, 21, 4],
        [2, 22, 2],
        [2, 23, 4],
        [3, 0, 7],
        [3, 1, 3],
        [3, 2, 0],
        [3, 3, 0],
        [3, 4, 0],
        [3, 5, 0],
        [3, 6, 0],
        [3, 7, 0],
        [3, 8, 1],
        [3, 9, 0],
        [3, 10, 5],
        [3, 11, 4],
        [3, 12, 7],
        [3, 13, 14],
        [3, 14, 13],
        [3, 15, 12],
        [3, 16, 9],
        [3, 17, 5],
        [3, 18, 5],
        [3, 19, 10],
        [3, 20, 6],
        [3, 21, 4],
        [3, 22, 4],
        [3, 23, 1],
        [4, 0, 1],
        [4, 1, 3],
        [4, 2, 0],
        [4, 3, 0],
        [4, 4, 0],
        [4, 5, 1],
        [4, 6, 0],
        [4, 7, 0],
        [4, 8, 0],
        [4, 9, 2],
        [4, 10, 4],
        [4, 11, 4],
        [4, 12, 2],
        [4, 13, 4],
        [4, 14, 4],
        [4, 15, 14],
        [4, 16, 12],
        [4, 17, 1],
        [4, 18, 8],
        [4, 19, 5],
        [4, 20, 3],
        [4, 21, 7],
        [4, 22, 3],
        [4, 23, 0],
        [5, 0, 2],
        [5, 1, 1],
        [5, 2, 0],
        [5, 3, 3],
        [5, 4, 0],
        [5, 5, 0],
        [5, 6, 0],
        [5, 7, 0],
        [5, 8, 2],
        [5, 9, 0],
        [5, 10, 4],
        [5, 11, 1],
        [5, 12, 5],
        [5, 13, 10],
        [5, 14, 5],
        [5, 15, 7],
        [5, 16, 11],
        [5, 17, 6],
        [5, 18, 0],
        [5, 19, 5],
        [5, 20, 3],
        [5, 21, 4],
        [5, 22, 2],
        [5, 23, 0],
        [6, 0, 1],
        [6, 1, 0],
        [6, 2, 0],
        [6, 3, 0],
        [6, 4, 0],
        [6, 5, 0],
        [6, 6, 0],
        [6, 7, 0],
        [6, 8, 0],
        [6, 9, 0],
        [6, 10, 1],
        [6, 11, 0],
        [6, 12, 2],
        [6, 13, 1],
        [6, 14, 3],
        [6, 15, 4],
        [6, 16, 0],
        [6, 17, 0],
        [6, 18, 0],
        [6, 19, 0],
        [6, 20, 1],
        [6, 21, 2],
        [6, 22, 2],
        [6, 23, 6],
    ]

    option = {
        "tooltip": {"position": "top"},
        "title": [
            {"textBaseline": "middle", "top": f"{(idx + 0.5) * 100 / 7}%", "text": day}
            for idx, day in enumerate(days)
        ],
        "singleAxis": [
            {
                "left": 150,
                "type": "category",
                "boundaryGap": False,
                "data": hours,
                "top": f"{(idx * 100 / 7 + 5)}%",
                "height": f"{(100 / 7 - 10)}%",
                "axisLabel": {"interval": 2},
            }
            for idx, _ in enumerate(days)
        ],
        "series": [
            {
                "singleAxisIndex": idx,
                "coordinateSystem": "singleAxis",
                "type": "scatter",
                "data": [],
                "symbolSize": JsCode(
                    "function(dataItem){return dataItem[1]*4}"
                ).js_code,
            }
            for idx, _ in enumerate(days)
        ],
    }
    for dataItem in data:
        option["series"][dataItem[0]]["data"].append([dataItem[1], dataItem[2]])
    st_echarts(options=option, height="600px")


ST_SCATTER_DEMOS = {
    "Scatter: Basic Scatter Chart": (
        render_scatter_simple,
        "https://echarts.apache.org/examples/en/editor.html?c=scatter-simple",
    ),
    "Scatter: Anscombe's Quartet": (
        render_anscombe_quartet,
        "https://echarts.apache.org/examples/en/editor.html?c=scatter-anscombe-quartet",
    ),
    "Scatter: Scatter Single Axis": (
        render_scatter_single_axis,
        "https://echarts.apache.org/examples/en/editor.html?c=scatter-single-axis",
    ),
}