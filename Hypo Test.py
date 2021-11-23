from scipy import stats


def differentFromMean(actualMean, variance, sampleMean, sampleSize, alpha):
    if (sampleSize < 30):
        tObservation = abs((sampleMean - actualMean) / (variance ** 0.5 / sampleSize ** 0.5))
        tValue = abs(stats.t.ppf(alpha / 2, sampleSize - 1))
        if tObservation < tValue:
            print(str(tObservation) + "<" + str(tValue))
            print("Accepted. We do not reject null hypo.")
        else:
            print(str(tObservation) + ">" + str(tValue))
            print("Rejected. We reject null hypo.")
    else:
        numerator = (sampleMean - actualMean)
        denominator = (variance ** 0.5) / (sampleSize ** 0.5)
        zObservation = abs(numerator / denominator)
        zValue = abs(stats.norm.ppf(alpha / 2, 0, 1))
        if zObservation < zValue:
            print(str(zObservation) + "<" + str(zValue))
            print("Accepted. We do not reject null hypo.")
        else:
            print(str(zObservation) + ">" + str(zValue))
            print("Rejected. We reject null hypo.")

differentFromMean(179, 26 ** 2, 205, 10, 0.01)

def moreThanDifferenceBetweenTwoMeans(sampleAMean, sampleAVariance, sampleBMean, sampleBVariance, difference, sampleSizeA, sampleSizeB, significance):
    if (sampleSizeA >= 30 and sampleSizeB >= 30):
        zObservation = ((sampleAMean - sampleBMean) - (difference)) / ((sampleAVariance / sampleSizeA) + (sampleBVariance / sampleSizeB)) ** 0.5
        zValue = abs(stats.norm.ppf(significance, 0, 1))
        if zObservation < zValue:
            print(str(zObservation) + "<" + str(zValue))
            print("Accepted. We do not reject null hypo.")
        else:
            print(str(zObservation) + ">" + str(zValue))
            print("Rejected. We reject null hypo.")

def moreThanVariance(variance, sampleVariance, sampleSize, significance):
    chisquaredObservation = ((sampleSize - 1) * sampleVariance) / variance
    chisquaredCritical = stats.chi2.ppf(1 - significance, sampleSize - 1)
    if chisquaredObservation < chisquaredCritical:
        print(str(chisquaredObservation) + "<" + str(chisquaredCritical))
        print("Accepted. We do not reject null hypo.")
    else:
        print(str(chisquaredObservation) + ">" + str(chisquaredCritical))
        print("Rejected. We reject null hypo.")

def lessThanVariance(variance, sampleVariance, sampleSize, significance):
    chisquaredObservation = ((sampleSize - 1) * sampleVariance) / variance
    chisquaredCritical = stats.chi2.ppf(significance, sampleSize - 1)
    if chisquaredObservation < chisquaredCritical:
        print(str(chisquaredObservation) + "<" + str(chisquaredCritical))
        print("Accepted. We do not reject null hypo.")
    else:
        print(str(chisquaredObservation) + ">" + str(chisquaredCritical))
        print("Rejected. We reject null hypo.")

# moreThanDifferenceBetweenTwoMeans(86.7, 6.28**2, 77.8, 5.61**2, 12, 50, 50, 0.05)