#!/usr/bin/env python3
"""Independent direct evaluation of the binary ring dynamics, without matrices."""
from collections import Counter

EXPECTED = (0,0,0,3,12,15,24,49,96,162,270,462,806,1378,2366,4105,7176,12512,21789)

def next_configuration(x,n):
    output=0
    for i in range(n):
        a=(x >> ((i-1)%n))&1
        b=(x >> i)&1
        c=(x >> ((i+1)%n))&1
        output|=(b^(a|c))<<i
    return output

def main():
    assert EXPECTED[0]==0  # empty words are outside the theorem
    for n in range(1,19):
        multiplicity=Counter(next_configuration(x,n) for x in range(1<<n))
        singleton_count=sum(value==1 for value in multiplicity.values())
        assert singleton_count==EXPECTED[n],(n,singleton_count,EXPECTED[n])
        assert sum(multiplicity.values())==1<<n
        # In particular, input/output indexing is not quotiented by rotations.
    print('DIRECT_OK', 'lengths=1..18', 'final_singletons=',EXPECTED[18])

if __name__=='__main__':main()
