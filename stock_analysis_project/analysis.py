
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# 读取数据
df_stock_returns = pd.read_csv('data/stock_returns_600132.csv', index_col='Date', parse_dates=True)

# Using Weibull distribution parameters to compute 1% and 99% percentiles
def compute_tail_percentiles(c, loc, scale):
    lower_tail = weibull_min.ppf(0.01, c, loc=loc, scale=scale)
    upper_tail = weibull_min.ppf(0.99, c, loc=loc, scale=scale)
    return lower_tail, upper_tail

# Plotting simulated returns with extreme value thresholds
def plot_simulated_returns(simulated_returns, lower_limit, upper_limit):
    plt.figure(figsize=(10, 6))
    plt.plot(simulated_returns, label='Simulated Returns')
    plt.axhline(y=lower_limit, color='r', linestyle='--', label='Lower Extreme Threshold')
    plt.axhline(y=upper_limit, color='g', linestyle='--', label='Upper Extreme Threshold')
    plt.title('Simulated Stock Returns with Extreme Value Thresholds')
    plt.xlabel('Days')
    plt.ylabel('Returns')
    plt.legend()
    plt.savefig('results/simulated_returns_plot.png')
    plt.close()

# Generating a summary report
def generate_summary_report(c, loc, scale, simulated_returns, lower_limit, upper_limit):
    extreme_lower_count = len(simulated_returns[simulated_returns < lower_limit])
    extreme_upper_count = len(simulated_returns[simulated_returns > upper_limit])
    with open('results/summary_report.txt', 'w') as f:
        f.write('Summary Report for Stock Return Analysis\n')
        f.write('==========================================\n\n')
        f.write(f'Weibull Distribution Parameters:\n')
        f.write(f'Shape (c): {c}\n')
        f.write(f'Location (loc): {loc}\n')
        f.write(f'Scale (scale): {scale}\n\n')
        f.write(f'Extreme Value Thresholds:\n')
        f.write(f'Lower Threshold (1% quantile): {lower_limit}\n')
        f.write(f'Upper Threshold (99% quantile): {upper_limit}\n\n')
        f.write(f'Count of Extreme Lower Values in Simulated Returns: {extreme_lower_count}\n')
        f.write(f'Count of Extreme Upper Values in Simulated Returns: {extreme_upper_count}\n')

# Main execution
if __name__ == "__main__":
    c = 1.0  # From previous analysis
    loc = 0
    scale = 1
    lower_tail, upper_tail = compute_tail_percentiles(c, loc, scale)
    
    # Simulate future returns
    forecast_period = 250
    simulated_returns = weibull_min.rvs(c, loc=loc, scale=scale, size=forecast_period)
    
    # Generate and save outputs
    plot_simulated_returns(simulated_returns, lower_tail, upper_tail)
    generate_summary_report(c, loc, scale, simulated_returns, lower_tail, upper_tail)

    print("Analysis completed. Check the 'results' directory for outputs.")
