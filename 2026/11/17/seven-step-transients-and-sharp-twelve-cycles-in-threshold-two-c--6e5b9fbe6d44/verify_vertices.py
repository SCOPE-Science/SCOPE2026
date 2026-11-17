"""Independent labelled-vertex verification of three-colour threshold-two CCA on K_(1,m,n).
Use: python verify_vertices.py. Only standard library.
"""
from itertools import product
from collections import Counter
from math import factorial

def neighbours(m,n):
    N = 1 + m + n
    part = (0,)+(1,)*m+(2,)*n
    return [tuple(j for j in range(N) if i != j and part[i] != part[j])
            for i in range(N)]

def advance(x,adj):
    y=[]
    for i,c in enumerate(x):
        nxt=(c+1)%3
        cnt=0
        for j in adj[i]:
            if x[j]==nxt:
                cnt+=1
                if cnt==2:break
        y.append(nxt if cnt==2 else c)
    return tuple(y)

def count_at_least_two_all(s):
    if s < 6:return 0
    z=0
    for a in range(2,s-3):
        for b in range(2,s-a-1):
            c=s-a-b
            if c>=2:z+=factorial(s)//(factorial(a)*factorial(b)*factorial(c))
    return z

def count_one_and_two_large(s):
    if s<5:return 0
    return sum(factorial(s)//(factorial(1)*factorial(b)*factorial(s-1-b))
               for b in range(2,s-2))

def predicted_period3(m,n):
    a,b=count_at_least_two_all(m),count_at_least_two_all(n)
    c,d=count_one_and_two_large(m),count_one_and_two_large(n)
    u=lambda k: 2 if k in (1,2) else 0
    return 3*((a+c)*(b+d)+u(m)*b+a*u(n))

def test(m,n):
    adj=neighbours(m,n)
    byperiod=Counter();entry=Counter();w12=None;w7=None
    for x in product(range(3),repeat=1+m+n):
        seq=[x]
        for _ in range(19):seq.append(advance(seq[-1],adj))
        assert seq[7]==seq[19]
        d=next(d for d in (1,2,3,4,6,12) if seq[7]==seq[7+d])
        assert d in (1,3,12)
        byperiod[d]+=1
        t=next(t for t in range(8) if seq[t]==seq[t+12])
        entry[t]+=1
        if d==12 and w12 is None:w12=''.join(map(str,x))
        if t==7 and w7 is None:w7=''.join(map(str,x))
    assert byperiod[3]==predicted_period3(m,n), (m,n,byperiod[3],predicted_period3(m,n))
    assert (byperiod[12]>0)==(min(m,n)>=4)
    print('K_1,%d,%d'% (m,n),'initial',3**(1+m+n),'attractors',dict(sorted(byperiod.items())),
          'max_entry',max(entry),'witness12',w12,'witness7',w7)

if __name__=='__main__':
    for m,n in [(1,1),(1,6),(2,6),(3,4),(4,4),(4,5),(5,5)]:
        test(m,n)
    print('INDEPENDENT_LABELLED_CHECKS_PASS')
