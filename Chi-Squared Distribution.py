from scipy import stats

# X ~ Chisq(10), where degrees of freedom = 10

# To find Pr(X <= 12), '
stats.chi2.cdf(12, 10)  # gives 0.714943

# To find pdf f(12), '
stats.chi2.pdf(12, 10)  # gives 0.0669263

# To find Pr(X > 12), '
1 - stats.chi2.cdf(12, 10)  # gives 0.285057

# To find x such that Pr(X <= x) = 0.05, '
stats.chi2.ppf(0.05, 10)  # gives 3.9403

# To find x such that Pr(X >= x) = 0.05, '
stats.chi2.ppf(0.95, 10)  # gives 18.307

print(stats.chi2.ppf(0.95, 24))