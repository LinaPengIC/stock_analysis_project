
import numpy as np
import pandas as pd
from scipy.stats import weibull_min

# 读取数据
df_stock_returns = pd.read_csv('data/stock_returns_600132.csv', index_col='Date', parse_dates=True)

# 使用 Weibull 分布的参数计算 1% 和 99% 分位数
def compute_tail_percentiles(c, loc, scale):
    lower_tail = weibull_min.ppf(0.01, c, loc=loc, scale=scale)
    upper_tail = weibull_min.ppf(0.99, c, loc=loc, scale=scale)
    return lower_tail, upper_tail

# 预警信号
def check_for_alerts(daily_return, lower_limit, upper_limit):
    if daily_return < lower_limit:
        return "Downside Alert: Potential significant loss ahead!"
    elif daily_return > upper_limit:
        return "Upside Alert: Potential significant gain ahead!"
    else:
        return "No alerts."

# 建议操作
def suggest_action(alert_message):
    if "Downside Alert" in alert_message:
        return "Consider hedging strategies, such as buying put options or increasing cash positions."
    elif "Upside Alert" in alert_message:
        return "Consider increasing exposure or ensuring you don't exit too early due to stop-loss strategies."
    else:
        return "Maintain current positions."

# 风险管理
def stop_loss(daily_return, threshold=-0.05):
    if daily_return < threshold:
        return "Triggered stop-loss! Consider selling part or all of the stock to prevent further losses."
    else:
        return "Within risk tolerance."

# 以下是模拟和策略应用的示例
if __name__ == "__main__":
    c = 1.0  # 从先前的分析中获取
    loc = 0
    scale = 1
    lower_tail, upper_tail = compute_tail_percentiles(c, loc, scale)
    daily_return_example = -0.06  # 模拟的某日收益率
    alert_message = check_for_alerts(daily_return_example, lower_tail, upper_tail)
    action_message = suggest_action(alert_message)
    risk_management_message = stop_loss(daily_return_example)
    print(alert_message)
    print(action_message)
    print(risk_management_message)
    