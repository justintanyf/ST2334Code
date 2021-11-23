from scipy import stats


# X ~ Exp(1/5), where E(X) = 5
#
# To find Pr(X <= 8)
# stats.expon.cdf(8, 0, 5)  # gives 0.798103 with the second argument being the lower limit of the x range and 3rd argument = E(X)
def findProbLessThanX(x, expectation):
    print(stats.expon.cdf(x, 0, expectation))


#
# To find pdf f(8)
# stats.expon.pdf(8, 0, 5)  # gives 0.0403793
def findProbAtX(x, expectation):
    print(stats.expon.pdf(x, 0, expectation))


#
# To find Pr(X > 8)
# 1 - stats.expon.cdf(8, 0, 5)  # gives 0.201897
def findProbMoreThanX(x, expectation):
    print(1 - stats.expon.cdf(x, 0, expectation))


#
# To find x such that Pr(X <= x) = 0.05
# stats.expon.ppf(0.05, 0, 5)  # gives 0.256466
def findXLessThanProb(prob, expectation):
    print(stats.expon.ppf(prob, 0, expectation))

# def findXMoreThanProb(prob, expectation):
#     print(1 - stats.expon.ppf(prob, 0, expectation))
