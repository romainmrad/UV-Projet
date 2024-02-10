import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tools import get_company_name


def plot_portfolio_visualisation(portfolio_data: dict) -> None:
    """
    Visualise portfolio diversification using invested amount and number of shares
    :param portfolio_data: portfolio data
    """
    portfolio_stock_data = {
        'Company': [],
        'Amount': [],
        'Shares': []
    }
    for stock, stock_data in portfolio_data['Stocks'].items():
        portfolio_stock_data['Company'].append(get_company_name(stock))
        portfolio_stock_data['Amount'].append(round(stock_data['Amount'], 2))
        portfolio_stock_data['Shares'].append(stock_data['Shares'])

    df = pd.DataFrame(portfolio_stock_data)
    # Plotting
    plt.figure(figsize=(20, 10))
    colors = sns.color_palette('YlGnBu')[0:len(df)]

    # Pie chart for the Amount column
    plt.subplot(1, 2, 1)
    plt.pie(
        df['Amount'],
        labels=df['Company'],
        autopct=lambda x: '{:.0f}€'.format(x*df['Amount'].sum()/100),
        colors=colors,
        startangle=90
    )
    plt.title('Portfolio Composition by Amount', fontweight='bold')

    # Pie chart for the Shares column
    plt.subplot(1, 2, 2)
    plt.pie(
        df['Shares'],
        labels=df['Company'],
        autopct=lambda x: '{:.0f}'.format(x * df['Shares'].sum() / 100),
        colors=colors,
        startangle=90
    )
    plt.title('Portfolio Composition by Shares', fontweight='bold')

    # Check if the path exists
    if not os.path.exists('../graphs/portfolio/'):
        # Create the directory
        os.makedirs('../graphs/portfolio/')
    # Save the figure to a file path
    plt.savefig('../graphs/portfolio/initial_portfolio.png')
    plt.close()
