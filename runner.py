import sys
import yaml
import click
import pandas as pd
from PIL import Image
from pychart import plot


def get_params(config, inline):
    if inline:
        return yaml.safe_load(inline)
    if config:
        with config as f:
            return yaml.safe_load(f)
    return {}


@click.command()
@click.option("-c", "--config", type=click.File("r"))
@click.option("-i", "--inline")
@click.option("-o", "--output", type=click.File("wb"))
def main(config, inline, output):
    params = get_params(config, inline)
    df = pd.read_csv(sys.stdin)
    image = plot(df, **params)
    image = Image.open(image)

    if output:
        image.save(output, format="png")
    else:
        image.show()


if __name__ == "__main__":
    main()
