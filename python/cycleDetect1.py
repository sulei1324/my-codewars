__author__ = 'Su Lei'


def cycle(sequence):
    for i in xrange(len(sequence)):
        subSeq = sequence[0:i]
        l = len(subSeq)
        ni = i
        for j in xrange(1, len(subSeq) + 1):
            testSeq1 = subSeq[l - j:l]
            nj = i + j
            if nj > len(sequence):
                break
            testSeq2 = sequence[ni:nj]
            # print testSeq1, testSeq2
            flag = 0
            for k in xrange(j):
                if testSeq1[k] is not testSeq2[k]:
                    flag = 1
                    break
            if flag is 0:
                #                print testSeq1
                return [l - j, len(testSeq1)]
    return []


print cycle([1,2,3,6,1,2,3,1,2,3,1,2,3])