#!/usr/bin/env python3
"""Independent state-by-state verification of period-one and period-three counts."""

RULE_BITS=(0,1,1,1,1,0,1,0) # rule 94, indexed by 000 through 111

def advance(x,n):
    bits=[(x>>j)&1 for j in range(n)]
    new=[RULE_BITS[4*bits[(i-1)%n]+2*bits[i]+bits[(i+1)%n]] for i in range(n)]
    return sum(v<<i for i,v in enumerate(new))

def predicted_counts(N):
    p=[0]*(N+1);q=[0]*(N+1)
    # -z D'/D coefficients: t_n = -n d_n - sum_{j=1}^{n-1} d_j t_{n-j}
    for d,t in [([1, -1, -1, 0, 1],p),([1,-1,-1,0,1,0,0,-3,3],q)]:
        for n in range(1,N+1):
            t[n]=-n*(d[n] if n<len(d) else 0)-sum(d[j]*t[n-j] for j in range(1,min(n,len(d)-1)+1))
    return p,q

def main():
    p,q=predicted_counts(16)
    for n in range(3,17):
        one=three=0
        for x in range(1<<n):
            y=advance(x,n)
            one+=(y==x)
            z=advance(y,n)
            three+=(advance(z,n)==x)
        assert one==p[n] and three==q[n]
        print(n,'fixed',one,'third-return',three,'primitive three orbits',(three-one)//3)
    print('exhaustive comparison passed through ring length 16')

if __name__=='__main__': main()
