# import the following library
from scipy import stats
# Boolean, to calculate odds of success
# X ~ B(10,0.4), where X = number of successes, with number of trials = 10 and prob of a success = 0.4

# To find Pr(X <= 5)
# stats.binom.cdf(5, 10, 0.4)  # gives 0.833761
def findProbLessThanX(x, trials, probOfSuccess):
    print(stats.binom.cdf(x, trials, probOfSuccess))


# To find Pr(X = 5)
# stats.binom.pmf(5, 10, 0.4)  # gives 0.200658
def findProbEqualToX(x, trials, probOfSuccess):
    print(stats.binom.pmf(x, trials, probOfSuccess))


# To find Pr(X > 5)
# 1 - stats.binom.cdf(5, 10, 0.4)  # gives 0.166239
def findProbMoreThanX(x, trials, probOfSuccess):
    print(1 - stats.binom.cdf(x, trials, probOfSuccess))


# To find x such that Pr(X <= x) >= 0.05
# stats.binom.ppf(0.05, 10, 0.4)  # gives 2
def findXLessThanProb(probability, trials, probOfSuccess):
    print(stats.binom.ppf(probability, trials, probOfSuccess))

# def findXMoreThanProb(probability, trials, probOfSuccess):
#     print(1 - stats.binom.ppf(probability, trials, probOfSuccess))

