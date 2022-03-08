import scraper


def calculate_average_return(returns: list) -> float:
    return sum(returns) / len(returns)


def calculate_covariance(stock_returns: list, index_returns: list) -> float:
    t1_average: float = calculate_average_return(stock_returns)
    t2_average: float = calculate_average_return(index_returns)
    covariance_sum: float = 0.0
    for i in range(len(stock_returns)):
        covariance_sum += (stock_returns[i] - t1_average) * (index_returns[i] - t2_average)
    return covariance_sum / (len(stock_returns) - 1)


def calculate_variance(index_returns: list) -> float:
    mean: float = calculate_average_return(index_returns)
    variance_sum: float = 0.0
    for i in range(len(index_returns)):
        variance_sum += pow((index_returns[i] - mean), 2)
    return variance_sum / (len(index_returns) - 1)


def calculate_beta(stock_returns: list, index_returns: list) -> float:
    # beta is calculated by dividing covariance of stock and index by variance of index
    covariance: float = calculate_covariance(stock_returns, index_returns)
    variance: float = calculate_variance(index_returns)
    return round((covariance / variance), 2)


def get_returns_list(closing_prices: list):
    # returns list of the assests returns over the desired time period
    returns_list: list = []
    last_close: float = closing_prices[0]
    for price in closing_prices[1:]:
        current_close: float = price
        period_return: float = ((current_close - last_close) / last_close) * 100
        returns_list.append(period_return)
        last_close = current_close
    return returns_list


def main(index: str, ticker: str, timeframe: str, frequency: str):
    stock_query = (ticker, timeframe, frequency)
    index_query = (index, timeframe, frequency)
    queries = [stock_query, index_query]

    dataframes = scraper.fetch_prices_csv(queries)
    stock_closing_prices = dataframes[0].Close[0: len(dataframes[0])]
    index_closing_prices = dataframes[1].Close[0: len(dataframes[0])]

    stock_returns = get_returns_list(stock_closing_prices)
    index_returns = get_returns_list(index_closing_prices)
    return calculate_beta(stock_returns, index_returns)
