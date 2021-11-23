from scipy import stats

# X ~ t(10), where degrees of freedom = 10

# To find Pr(X <= 1.5), '
stats.t.cdf(1.5, 10)  # gives 0.917746
#
# To find pdf f(1.5), '
stats.t.pdf(1.5, 10)  # gives 0.127445
#
# To find Pr(X > 1.5), '
1 - stats.t.cdf(1.5, 10)  # gives 0.0822537
#
# To find x such that Pr(X <= x) = 0.05, '
stats.t.ppf(0.05, 10)  # gives -1.81246
#
# To find x such that Pr(X >= x) = 0.05, '
stats.t.ppf(0.95, 10)  # gives 1.81246

print(stats.t.ppf(0.005, 9))
