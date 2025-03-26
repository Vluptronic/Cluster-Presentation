import os

from matplotlib import pyplot as plt

from clusters import get_clusters
from projections import get_portfolio_data, get_projection_from_data

# Your methods here - you should use your imported methods to
# generate clusters and projections, then generate plots

def generate_plots():
    pass


# This runs when you run this file as a script, i.e. python src/visualizations.py
if __name__ == '__main__':
    data = get_portfolio_data()

    if os.path.exists('figures') is False:
        os.makedirs('figures')

    generate_plots()