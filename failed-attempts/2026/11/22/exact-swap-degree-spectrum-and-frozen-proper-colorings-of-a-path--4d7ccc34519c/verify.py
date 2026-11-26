"""Independent exact tests for the proper-path adjacent-swap degree enumerator."""
from collections import Counter
from fractions import Fraction
from itertools import product
from random import Random


def direct_degree(w):
    n=len(w)
    outcomes=set()
    for i in range(n-1):
        x=list(w)
        x[i],x[i+1]=x[i+1],x[i]
        if all(x[j]!=x[j+1] for j in range(n-1)):
            outcomes.add(tuple(x))
    return len(outcomes)


def local_degree(w):
    n=len(w)
    if n==2: return 1
    a=[int(w[j]!=w[j+2]) for j in range(n-2)]
    return a[0]+a[-1]+sum(a[j]*a[j+1] for j in range(len(a)-1))


def polynomial(q,n):
    """Output list indexed by degree, from the theorem's transfer matrix."""
    if n==2: return [0,q*(q-1)]
    a=q-2
    # states: equality distance two absent or present, with weighted integer counts
    # after 1 bit: absent -> a choices, present -> 1 choice
    states=[[0,a], [1]]   # state 0: a*z; state 1: 1
    m=n-2
    for _ in range(m-1):
        nxt=[[0]*(m+3), [0]*(m+3)]
        for p, pol in enumerate(states):
            for j,c in enumerate(pol):
                if not c: continue
                nxt[0][j+int(p==0)]+=a*c
                nxt[1][j]+=c
        states=nxt
    degree=[0]*(n+1)
    for j,c in enumerate(states[0]):
        if c: degree[j+1]+=c # final endpoint contributes if state zero
    for j,c in enumerate(states[1]):
        if c: degree[j]+=c
    return [z*q*(q-1) for z in degree]


def enum(q,n):
    counts=Counter()
    for w in product(range(q),repeat=n):
        if any(w[i]==w[i+1] for i in range(n-1)): continue
        d=direct_degree(w)
        if d!=local_degree(w): raise AssertionError((q,n,w,d,local_degree(w)))
        counts[d]+=1
    return [counts[i] for i in range(n+1)]


def check():
    tested=0
    for q in range(2,6):
        for n in range(2,10):
            if q*(q-1)**(n-1)>120000: continue
            obs=enum(q,n)
            calc=polynomial(q,n)
            calc=calc+[0]*(len(obs)-len(calc))
            assert obs==calc,(q,n,obs,calc)
            assert sum(obs)==q*(q-1)**(n-1)
            a=q-2
            if n>=4:
                prev0,prev1=1,1+a
                for _ in range(n-4):
                    prev0,prev1=prev1,prev1+a*prev0
                assert obs[0]==q*(q-1)*prev0, (q,n,obs[0],prev0)
            if n>=3: assert obs[n-1]==q*(q-1)*a**(n-2)
            if q>=3 and n>=4:
                s=Fraction(q-2,q-1)
                m=n-2
                mean=2*s+(m-1)*s*s
                var=2*s*(1-s)+(m-1)*s*s*(1-s*s)+2*(m-2)*s**3*(1-s)+4*s*s*(1-s)
                total=sum(obs)
                emp_mean=sum(k*v for k,v in enumerate(obs))/total
                emp_var=sum(Fraction(v,total)*(k-mean)**2 for k,v in enumerate(obs))
                assert Fraction(sum(k*v for k,v in enumerate(obs)),total)==mean,(q,n,mean,emp_mean)
                assert emp_var==var,(q,n,var,emp_var)
            tested+=1
    rng=Random(5274)
    for q,n in [(3,200),(4,220),(9,160),(15,160)]:
        for _ in range(500):
            w=[rng.randrange(q)]
            for i in range(1,n):
                t=rng.randrange(q-1)
                w.append(t+int(t>=w[-1]))
            assert direct_degree(w)==local_degree(w)
    print('VERIFY_OK exact_strata='+str(tested)+' randomized_long_words=2000')

if __name__=='__main__':check()
