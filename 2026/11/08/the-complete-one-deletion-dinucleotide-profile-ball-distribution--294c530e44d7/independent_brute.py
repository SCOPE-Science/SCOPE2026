#!/usr/bin/env python3
"""Independent direct enumeration of actual deletion outputs and pair profiles."""
from collections import Counter

def dinucleotide_profile(word):
    return tuple(sum(word[i:i+2]==pair for i in range(len(word)-1))
                 for pair in ('00','01','10','11'))

def main():
    expected={
     2:[4,0,0,0,0,0],3:[2,4,2,0,0,0],4:[2,6,8,0,0,0],
     5:[2,10,14,6,0,0],6:[2,16,26,16,4,0],
     7:[2,24,48,38,16,0],8:[2,38,86,76,54,0],
     9:[2,60,144,178,116,12],10:[2,94,252,360,280,36],
     11:[2,148,436,726,640,96],12:[2,234,760,1426,1446,228],
     13:[2,370,1318,2816,3154,532],14:[2,586,2294,5518,6792,1192]
    }
    for n,counts in expected.items():
        hist=Counter()
        for i in range(1<<n):
            word=format(i,'0%db'%n)
            shadow={dinucleotide_profile(word[:p]+word[p+1:])
                     for p in range(n)}
            hist[len(shadow)]+=1
        obs=[hist[j] for j in range(1,7)]
        assert obs==counts,(n,obs,counts)
        print(n,obs)
    print('BRUTE_OK')

if __name__=='__main__':main()
