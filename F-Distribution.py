from scipy import stats

# X ~ F(12,10), where degrees of freedom are 12 and 10


# To find Pr(X <= 3), '
stats.f.cdf(3, 12, 10)  # gives 0.954299


# To find pdf f(3), '
stats.f.pdf(3, 12, 10)  # gives 0.046852


# To find Pr(X > 3), '
1 - stats.f.cdf(3, 12, 10)  # gives 0.0457007


# To find x such that Pr(X <= x) = 0.05, '
stats.f.ppf(0.05, 12, 10)  # gives 0.363189


# To find x such that Pr(X >= x) = 0.05, '
stats.f.ppf(0.95, 10)  # gives 2.91298
