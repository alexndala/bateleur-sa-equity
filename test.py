import riskfolio as rp

import matplotlib.pyplot as plt

ax = rp.jupyter_report(returns, w=w_rp, rm=rm, t_factor = 252, days_per_year = 365)
plt.show()

# # Risk contribution constraints vector based on Industry Class
# b = rp.risk_constraint(asset_classes,
#                        kind='classes',
#                        classes_col='Industry')
ax = rp.plot_clusters(returns = returns,
                    codependence="spearman",
                    linkage="ward",
                    cmap="BrBG",
                    linecolor="blue",
                    title="XYZ BCI SA Equity Fund Clustermap (Spearman and Ward) \nJan-2024 - Dec-24\n Analyst: Mahlatse A. Ndala.",               
                    height=10,
                    width=12)