"""Symbolic predecessor-set proof check for two-bridge AND cycles."""
from math import gcd,lcm

def symbolic(a,b,s):
    # Bitset for each output coordinate, each bit represents one original variable.
    src=[1<<i for i in range(a+b)]
    for _ in range(lcm(a,b)):
        nxt=[src[(i-1)%a] for i in range(a)]
        nxt.append(src[a+b-1] | src[0] | src[s])
        nxt.extend(src[a+j-1] for j in range(1,b))
        src=nxt
    return src

def expected(a,b,s):
    g=gcd(a,b)
    x=[1<<i for i in range(a)]
    for j in range(b):
        z=1<<(a+j)
        for k in range(a):
            if (k-j-1)%g==0 or (k-j-1-s)%g==0:z |= 1<<k
        x.append(z)
    return x

def main():
    cases=0
    for a in range(2,27):
        for b in range(1,27):
            for s in range(1,a):
                assert symbolic(a,b,s)==expected(a,b,s),(a,b,s)
                cases+=1
    print('PASS symbolic all',cases,'tuples, 2<=a<=26, 1<=b<=26, 1<=s<a')
if __name__=='__main__':main()
