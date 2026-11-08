"""Independent finite-state checker for period-three positions on friendship graphs."""
from itertools import product
from math import comb
from collections import Counter

def step(s,k):
    degree=(2*k,)+(2,)*(2*k)
    f=[int(x >= d) for x,d in zip(s,degree)]
    hub=sum(f[1:])
    out=[s[0]+hub-2*k*f[0]]
    for j in range(k):
        a,b=1+2*j,2+2*j
        out.append(s[a]+f[0]+f[b]-2*f[a])
        out.append(s[b]+f[0]+f[a]-2*f[b])
    return tuple(out)

def theorem(k):
    q=Counter()
    for j in range(k):
        count=3*sum(comb(k,a)*2**(k-a) for a in range(j+1))
        q[3*k+j]=count
        q[7*k-1-j]=count
    return q

def run():
    for k in range(1,5):
        count=Counter()
        checked=0
        for h in range(4*k):
            for leaves in product(range(4),repeat=2*k):
                s=(h,)+leaves
                t=step(s,k)
                if t==s: continue
                if step(step(t,k),k)==s:
                    count[sum(s)]+=1
                checked+=1
        expected=theorem(k)
        assert count == expected,(k,count,expected)
        assert sum(count.values())==12*k*3**(k-1)
        print(f'k={k} examined={4*k*4**(2*k)} primitive3={sum(count.values())} masses={sorted(count.items())}')
    print('EXHAUSTIVE PASS')

if __name__=='__main__':run()
