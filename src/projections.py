import pandas as pd

def get_portfolio_data():
    """
    Load the portfolio data and the recession data.
    Doesn't do anything with them right now.

    :return: DataFrame with the portfolio data and the recession data
    """

    portfolio_data = pd.read_csv('data/portfolio.csv')
    recession_data = pd.read_csv('data/recessions.csv')

    return portfolio_data, recession_data


def get_projection_from_data(data):
    """
    Fit the projection method to the data and return the transformed data.

    :param data: The data to project
    :return: The transformed data
    """

    # return projection_method.fit_transform(data)
    return data