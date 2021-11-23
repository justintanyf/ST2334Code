from scipy import stats
# Given that a final success occurs, find odds of k success
# X ~ NB(4,0.55), where X = number of trials, with number of successes = 4 and prob of a success = 0.55

# To find Pr(X <= 6)
# stats.nbinom.cdf(2, 4, 0.55)  # gives 0.441518 , where 2 = number of failures
def findProbLessThanX(x, numberOfSuccesses, probOfSuccess):
    print(stats.nbinom.cdf(x - numberOfSuccesses, numberOfSuccesses, probOfSuccess))


# To find Pr(X = 6)
# stats.nbinom.pmf(2, 4, 0.55)  # gives 0.1853
def findProbEqualToX(x, numberOfSuccesses, probOfSuccess):
    print(stats.nbinom.pmf(x - numberOfSuccesses, numberOfSuccesses, probOfSuccess))

# To find Pr(X > 6)
# 1 - stats.nbinom.cdf(2, 4, 0.55)  # gives 0.558482
def findProbMoreThanX(x, numberOfSuccesses, probOfSuccess):
    print(1 - stats.nbinom.cdf(x - numberOfSuccesses, numberOfSuccesses, probOfSuccess))

# To find x such that Pr(X <= x) >= 0.25
# stats.binom.ppf(0.25, 4, 0.55)  # gives 1 which is the number of failures. Hence, x = 5
def findNumberOfFailures(probability, numberOfSuccesses, probOfSuccess):
    print(stats.binom.ppf(probability, numberOfSuccesses, probOfSuccess))

