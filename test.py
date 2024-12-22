import riskfolio as rp

import matplotlib.pyplot as plt

ax = rp.jupyter_report(returns, w=w_rp, rm=rm, t_factor = 252, days_per_year = 365)
plt.show()

# Risk contribution constraints vector based on Industry Class
b = rp.risk_constraint(asset_classes,
                       kind='classes',
                       classes_col='Industry')