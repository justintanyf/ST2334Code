from scipy import stats

def getPooledVariance(sampleVarianceA, sampleSizeA, sampleVarianceB, sampleSizeB):
    return ((((sampleSizeA - 1) * sampleVarianceA) + ((sampleSizeB - 1) * sampleVarianceB))
                            / (sampleSizeA + sampleSizeB - 2)) ** 0.5

def differenceBetweenTwoMeans(sampleMeanA, sampleVarianceA, sampleSizeA, sampleMeanB, sampleVarianceB, sampleSizeB,
                              confidenceInterval):
    if (sampleSizeA < 30 and sampleSizeB < 30):
        spPooledVariance = getPooledVariance(sampleVarianceA, sampleSizeA, sampleVarianceB, sampleSizeB)
        differenceInMean = sampleMeanA - sampleMeanB
        magnitude = abs(stats.t.ppf((1 - confidenceInterval) / 2, sampleSizeA + sampleSizeB - 2)) * spPooledVariance * ((1/sampleSizeA)+(1/sampleSizeB)) ** 0.5
        upperLimit = differenceInMean + magnitude
        lowerLimit = differenceInMean - magnitude
        print(str(lowerLimit) + ", " + str(upperLimit))
    else:
        print("I did not plan for this")


