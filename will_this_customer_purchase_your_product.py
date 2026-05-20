# Online shopping decisions rely on how consumers engage with online store content. You work for a new startup company that has just launched a new online shopping website. The marketing team asks you, a new data scientist, to review a dataset of online shoppers' purchasing intentions gathered over the last year. Specifically, the team wants you to generate some insights into customer browsing behaviors in November and December, the busiest months for shoppers. You have decided to identify two groups of customers: those with a low purchase rate and returning customers. After identifying these groups, you want to determine the probability that any of these customers will make a purchase in a new marketing campaign to help gauge potential success for next year's sales.

# Data description:
# You are given an online_shopping_session_data.csv that contains several columns about each shopping session. Each shopping session corresponded to a single user.

# Column	Description
# SessionID	unique session ID
# Administrative	number of pages visited related to the customer account
# Administrative_Duration	total amount of time spent (in seconds) on administrative pages
# Informational	number of pages visited related to the website and the company
# Informational_Duration	total amount of time spent (in seconds) on informational pages
# ProductRelated	number of pages visited related to available products
# ProductRelated_Duration	total amount of time spent (in seconds) on product-related pages
# BounceRates	average bounce rate of pages visited by the customer
# ExitRates	average exit rate of pages visited by the customer
# PageValues	average page value of pages visited by the customer
# SpecialDay	closeness of the site visiting time to a specific special day
# Weekend	indicator whether the session is on a weekend
# Month	month of the session date
# CustomerType	customer type
# Purchase	class label whether the customer make a purchase


# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load and view your data
shopping_data = pd.read_csv("online_shopping_session_data.csv")
shopping_data.head()

############################################################

# Start your code here!
# Use as many cells as you like
# by Elok Mutiaraningtyas
# elokmutiaraningtyas@gmail.com

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import binom

# Load data
shopping_data = pd.read_csv("online_shopping_session_data.csv")

# Filter for November and December
nov_dec = shopping_data[shopping_data['Month'].isin(['Nov', 'Dec'])]

# ── 1. Purchase rates by customer type ──────────────────────────────────────
purchase_rates_df = nov_dec.groupby('CustomerType')['Purchase'].mean()
print(purchase_rates_df)

purchase_rates = {
    "Returning_Customer": round(purchase_rates_df['Returning_Customer'], 3),
    "New_Customer": round(purchase_rates_df['New_Customer'], 3)
}
print(f"Purchase rates: {purchase_rates}")

# ── 2. Strongest correlation in time spent among page types ─────────────────
returning = nov_dec[nov_dec['CustomerType'] == 'Returning_Customer']

duration_cols = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration']
corr_matrix = returning[duration_cols].corr()

# Extract unique pairs
pairs = []
for i in range(len(duration_cols)):
    for j in range(i+1, len(duration_cols)):
        col1 = duration_cols[i]
        col2 = duration_cols[j]
        corr_val = corr_matrix.loc[col1, col2]
        pairs.append((col1, col2, corr_val))

# Find strongest correlation
strongest = max(pairs, key=lambda x: abs(x[2]))
top_correlation = {
    "pair": (strongest[0], strongest[1]),
    "correlation": round(strongest[2], 3)
}
print(f"Top correlation: {top_correlation}")

# ── 3. Probability of at least 100 sales out of 500 sessions ────────────────
base_rate = purchase_rates["Returning_Customer"]
boosted_rate = base_rate * 1.15  # 15% boost
n_sessions = 500
target_sales = 100

prob_at_least_100_sales = 1 - binom.cdf(target_sales - 1, n_sessions, boosted_rate)
print(f"Boosted purchase rate: {boosted_rate:.4f}")
print(f"Probability of at least 100 sales: {prob_at_least_100_sales:.4f}")

# ── Optional: Binomial distribution plot ────────────────────────────────────
x = np.arange(0, 201)
pmf = binom.pmf(x, n_sessions, boosted_rate)

plt.figure(figsize=(12, 5))
plt.bar(x, pmf, color='steelblue', alpha=0.7)
plt.axvline(target_sales, color='red', linestyle='--', label=f'Target = {target_sales}')
plt.fill_between(x, pmf, where=(x >= target_sales), color='orange', alpha=0.5, label=f'P(X ≥ {target_sales}) = {prob_at_least_100_sales:.4f}')
plt.xlabel('Number of Sales')
plt.ylabel('Probability')
plt.title('Binomial Distribution: Sales out of 500 Sessions (Boosted Rate)')
plt.legend()
plt.tight_layout()
plt.show()

#########################################
# Result:

# CustomerType
# New_Customer          0.273352
# Returning_Customer    0.195594
# Name: Purchase, dtype: float64
# Purchase rates: {'Returning_Customer': 0.196, 'New_Customer': 0.273}
# Top correlation: {'pair': ('Administrative_Duration', 'ProductRelated_Duration'), 'correlation': 0.417}
# Boosted purchase rate: 0.2254
# Probability of at least 100 sales: 0.9227
