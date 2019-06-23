import io
import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = [
    "Hiragino Sans",
    "BIZ UDGothic",
    "Yu Gothic",
    "Meiryo",
    "Noto Sans CJK JP",
    "IPAexGothic",
    "DejaVu Sans",
]


def plot(df, **kwargs):
    plot = kwargs.get("plot", "line")
    args = kwargs.get("args", {})
    sort = kwargs.get("sort", {})
    font = kwargs.get("font", {})
    axes = kwargs.get("axes", {})
    figure = kwargs.get("figure", {})
    adjust = kwargs.get("adjust", [])

    if sort:
        df = df.sort_values(sort["column"], ascending=sort["asc"])

    for attr in font:
        plt.rcParams[f"font.{attr}"] = font[attr]

    ax = plt.figure(**figure).add_subplot()
    getattr(df.plot, plot)(ax=ax, **args)

    for func, arg in axes.items():
        if func == "legend":
            args = arg if type(arg) is list else [arg]
            ax.legend(args)
        elif func == "xlabel":
            ax.set_xlabel(arg)
        elif func == "ylabel":
            ax.set_ylabel(arg)
        elif func == "ticklabel":
            ax.ticklabel_format(**arg)
        elif func == "grid":
            ax.grid(**arg)

    if adjust:
        params = ("left", "right", "bottom", "top")
        params = dict(zip(params, adjust))
        plt.subplots_adjust(**params)
    else:
        plt.tight_layout()

    image = io.BytesIO()
    plt.savefig(image, format="png")
    return image
