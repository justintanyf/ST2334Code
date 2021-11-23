from scipy import stats


# X ~ N(mean, variance)
# Standard Normal = X ~ N(0, 1)

# X ~ N(50, 10^2), where mu=E(X)=50 and sigma^2=V(X)=10^2

# To find Pr(X <= 45), '
# stats.norm.cdf(45, 50, 10)  # gives 0.308538
def findProbLessThanX(x, mean, variance):
    returnThis = stats.norm.cdf(x, mean, variance ** 0.5)
    print(returnThis)
    return returnThis


# To find pdf f(45), '
# stats.norm.pdf(45, 50, 10)  # gives 0.0352065
def findProbEqualToX(x, mean, variance):
    returnThis = stats.norm.pdf(x, mean, variance ** 0.5)
    print(returnThis)
    return returnThis


# To find Pr(X > 45), '
# 1 - stats.norm.cdf(45, 50, 10)  # gives 0.691462
def findProbMoreThanX(x, mean, variance):
    returnThis = 1 - stats.norm.cdf(x, mean, variance ** 0.5)
    print(returnThis)
    return returnThis


# To find x such that Pr(X <= x) = 0.05, '
# stats.norm.ppf(0.05, 50, 10)  # gives 33.5515
def findXLessThanProb(prob, mean, variance):
    returnThis = stats.norm.ppf(prob, mean, variance ** 0.5)
    print(returnThis)
    return returnThis


# To find z such that Pr(Z >= z) = 0.05 with Z ~ N(0,1), '
# stats.norm.ppf(0.95, 0, 1)  # gives 1.64485
def findZLessThanProbStandardNormal(prob):
    returnThis = stats.norm.ppf(prob, 0, 1)
    print(returnThis)
    return returnThis


def findZMoreThanProbStandardNormal(prob):
    return findZLessThanProbStandardNormal(1 - prob)


# Find mean and variance and standard deviation
array = [72.5,36.5,132.1,129,54,104.6,119,81]
def findMeanAndVariance(array):
    print("Mean is: " + str(stats.tmean(array)))
    print("Variance is " + str(stats.tvar(array)))
    print("Standard Deviation is " + str(stats.tvar(array) ** 0.5))

