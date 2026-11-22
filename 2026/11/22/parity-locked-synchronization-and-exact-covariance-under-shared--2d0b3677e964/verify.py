"""Exact finite-state checks for shared-noise sign updates on a diagonal quadratic.
Uses only the Python standard library; exhaustive over each enumerated state.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def ok(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1


def update(k, cell, m):
    # U=-m*delta + (cell+1/2)*delta, 0<=cell<2m.
    gradient_sign = 1 if 2*k + 2*cell + 1 > 4*m else -1
    return k-gradient_sign


def transitions(k, l, m):
    out = {}
    for j in range(2*m):
        a, b = update(k,j,m), update(l,j,m)
        out[(a,b)] = out.get((a,b),F(0)) + F(1,2*m)
    return out


for m in range(1,12):
    n=2*m
    pi = [F(comb(n,k),2**n) for k in range(n+1)]
    ok(sum(pi)==1, ('binomial normalizes',m))
    for k in range(n+1):
        tr=transitions(k,k,m)
        up=tr.get((k+1,k+1), F(0))
        down=tr.get((k-1,k-1), F(0))
        ok(up==F(n-k,n),('marginal up',m,k))
        ok(down==F(k,n),('marginal down',m,k))
        if k<n:
            ok(pi[k]*F(n-k,n)==pi[k+1]*F(k+1,n),('scalar balance',m,k))

    for k in range(n+1):
      for l in range(n+1):
        trans=transitions(k,l,m)
        ok(sum(trans.values())==1,('row stochastic',m,k,l))
        gap=abs(k-l)
        gapnext={abs(a-b):p for (a,b),p in trans.items()}
        if gap>=2:
            ok(sum(p for (a,b),p in trans.items() if abs(a-b)==gap-2)==F(gap,n),('gap reduction',m,k,l))
            ok(sum(p for (a,b),p in trans.items() if abs(a-b)==gap)==1-F(gap,n),('gap hold',m,k,l))
        else:
            ok(all(abs(a-b)==gap for a,b in trans),('absorb zero or one',m,k,l))

    # Unique adjacent-pair stationary law on labeled pairs of opposite parity.
    pi_pair={}
    for low in range(n):
        p=F(comb(n-1,low),2**(n-1)*2)
        pi_pair[(low,low+1)]=p
        pi_pair[(low+1,low)]=p
    ok(sum(pi_pair.values())==1,('pair normalizes',m))
    incoming={s:F(0) for s in pi_pair}
    for state,p in pi_pair.items():
        for next_state,q in transitions(*state,m).items():
            ok(next_state in incoming,('pair closure',m,state,next_state))
            incoming[next_state]+=p*q
    for state,p in pi_pair.items():
        ok(incoming[state]==p,('pair invariance',m,state))

    means=[sum(F(k)*p for (k,l),p in pi_pair.items()),sum(F(l)*p for (k,l),p in pi_pair.items())]
    cov=sum(F(k*l)*p for (k,l),p in pi_pair.items())-means[0]*means[1]
    va=sum(F(k*k)*p for (k,l),p in pi_pair.items())-means[0]*means[0]
    ok(means==[F(m),F(m)],('means',m))
    ok(va==F(m,2),('variance',m))
    ok(cov==F(m-1,2),('covariance',m))

    # Exact expected settling-time recursion by the pure-death gap law.
    for initial_gap in range(n+1):
        target = initial_gap%2
        expected=F(0)
        for g in range(initial_gap,target,-2):
            expected+=F(n,g)
        recursive=F(0)
        if initial_gap>1:
            # E_g=1+(1-g/n) E_g+(g/n) E_(g-2)
            def E(g):
                if g<=1: return F(0)
                return F(n,g)+E(g-2)
            recursive=E(initial_gap)
        ok(expected==recursive,('hitting mean',m,initial_gap))

# Exhaustive stationary invariance for every three-coordinate parity pattern.
for m in range(1,7):
    n=2*m
    for pattern in ((0,0,0),(0,0,1),(0,1,0),(0,1,1)):
        pi3={}
        if len(set(pattern))==1:
            for k in range(n+1):
                pi3[(k,k,k)]=F(comb(n,k),2**n)
        else:
            for low in range(n):
                for r in (0,1):
                    state=tuple(low+r if z==0 else low+1-r for z in pattern)
                    pi3[state]=F(comb(n-1,low),2**n)
        ok(sum(pi3.values())==1,('three-coordinate normalize',m,pattern))
        incoming={state:F(0) for state in pi3}
        for state,p in pi3.items():
            for cell in range(n):
                dst=tuple(update(k,cell,m) for k in state)
                ok(dst in pi3,('three-coordinate closure',m,pattern,state,cell))
                incoming[dst] += p*F(1,n)
        for state,p in pi3.items():
            ok(incoming[state]==p,('three-coordinate stationary',m,pattern,state))
        mu=sum(F(sum(state),3)*p for state,p in pi3.items())
        v=sum((F(sum(state),3)-mu)**2*p for state,p in pi3.items())
        r=pattern.count(0)
        expected = F(m,2)-F(r*(3-r),9)
        ok(v==expected,('three-coordinate mean variance',m,pattern,v,expected))

print('PASS', checks, 'exact-rational assertions; pair M=1..11 and three-coordinate M=1..6')
