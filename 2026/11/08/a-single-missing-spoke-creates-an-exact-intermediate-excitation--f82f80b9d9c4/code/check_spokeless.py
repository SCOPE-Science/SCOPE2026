"""Exhaustive finite examples of missing-spoke wheel excitation rate census."""
from itertools import product
from fractions import Fraction

def step(s,A,model):
    if model=='CCA':
        return tuple((v+1)%3 if any(s[j]==(v+1)%3 for j in A[i]) else v for i,v in enumerate(s))
    return tuple(((v+1)%3 if v else int(any(s[j]==1 for j in A[i]))) for i,v in enumerate(s))

def G(n):
    # vertex 0 is hub; vertex 1 is missing its hub edge; rim 1..n
    return [tuple(range(2,n+1))]+[tuple(sorted(set([1+(i-1)%n,1+(i+1)%n]+([] if i==0 else [0])))) for i in range(n)]

def wheel_sums(n):
    T=((1,1,1),(1,1,0),(1,0,1))
    B=((0,1,1),(1,0,2),(1,2,0))
    A=((1,0,0),(0,1,0),(0,0,1))
    for _ in range(n-2):
        A=tuple(tuple(sum(A[i][k]*T[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    s=sum(map(sum,A));r=sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))
    return 9*s-3*r,3*r,3**(n+1)-9*s

for n in range(4,10):
    a=G(n)
    for model in ('CCA','GHM'):
        counts={}
        periods={}
        for init in product(range(3),repeat=n+1):
            seen={};orbit=[]; state=init
            while state not in seen:
                seen[state]=len(orbit);orbit.append(state);state=step(state,a,model)
            cyc=orbit[seen[state]:]; period=len(cyc)
            ex=0
            for st in cyc:
                out=step(st,a,model)
                if model=='CCA': ex+=out[0]!=st[0]
                else:ex+=(st[0]==0 and out[0]==1)
            rate=Fraction(ex,period)
            counts[rate]=counts.get(rate,0)+1
            periods[period]=periods.get(period,0)+1
        exp=wheel_sums(n)
        expected=dict(zip((Fraction(0),Fraction(3,4) if model=='CCA' else Fraction(1,4),Fraction(1) if model=='CCA' else Fraction(1,3)),exp))
        assert counts==expected,(n,model,counts,expected)
        print('n',n,model,'counts',str(counts),'periods',periods,'expected',exp)
print('PASS all orbit rate populations for missing-spoke wheels n=4..9, both rules')
