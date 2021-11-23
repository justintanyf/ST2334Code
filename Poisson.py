from scipy import stats


# Given an average expectation, find odds of occurence
# X ~ P(8), where E(X) = lambda = 8

# To find Pr(X <= 6)
# stats.poisson.cdf(6, 8)  # gives 0.313374
def findProbLessThanX(x, expectation):
    returnThis = stats.poisson.cdf(x, expectation)
    print(returnThis)
    return returnThis


# To find Pr(X = 6)
# stats.poisson.pmf(6, 8)  # gives 0.122138
def findProbEqualToX(x, expectation):
    returnThis = stats.poisson.pmf(x, expectation)
    print(returnThis)
    return returnThis


# To find Pr(X > 6)
# 1 - stats.poisson.cdf(6, 8)  # gives 0.686626
def findProbMoreThanX(x, expectation):
    returnThis = 1 - stats.poisson.cdf(x, expectation)
    print(returnThis)
    return returnThis


# To find x such that Pr(X <= x) >= 0.25
# stats.poisson.ppf(0.25, 8)  # gives 6
def findXLessThanProb(prob, expectation):
    returnThis = stats.poisson.ppf(prob, expectation)
    print(returnThis)
    return returnThis


