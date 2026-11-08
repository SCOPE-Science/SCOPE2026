"""Exact recurrence and direct exhaustive Greenberg--Hastings wheel checks.
Run with Python 3 and SymPy; no network or external files required.
"""
from itertools import product
from collections import Counter
from sympy import Matrix, Symbol, factor

x=Symbol('x')
S=Matrix([[1,1,1],[1,1,0],[1,0,1]])
pairs=[(a,b) for a in range(3) for b in range(3)]
T=Matrix([[int(b==bb and (b==2 or (b+1) in (a,c)))
           for bb,c in pairs] for a,b in pairs])
assert factor(S.charpoly(x).as_expr()) == (x-1)*(x*x-2*x-1)
assert factor(T.charpoly(x).as_expr()) == x**4*(x*x+x+1)*(x**3-2*x*x-1)

for n in range(3,11):
    # Wheel n rim vertices plus central hub; all configurations enumerated once.
    def step(state):
        hub, rim=state[0],state[1:]
        newhub = 2 if hub==1 else 0 if hub==2 else int(1 in rim)
        newrim=tuple(2 if a==1 else 0 if a==2 else int(
            hub==1 or rim[(i-1)%n]==1 or rim[(i+1)%n]==1)
            for i,a in enumerate(rim))
        return (newhub, *newrim)
    observed=Counter();periodic=Counter(); maximum_entry=0
    for state in product(range(3),repeat=n+1):
        p=state;seq=[p]
        for _ in range(7):
            p=step(p);seq.append(p)
        assert seq[7]==seq[4], (n,state)
        fixed=(p==(0,)*(n+1))
        # For a finite system with F^7=F^4, first periodic entry is first
        # t such that F^t=F^(t+3). The unique period-one orbit is all-rest.
        t=next(t for t in range(5) if seq[t]==seq[t+3])
        assert t<=4
        maximum_entry=max(maximum_entry,t)
        observed[1 if fixed else 3]+=1
        if t==0: periodic[1 if fixed else 3]+=1
    assert maximum_entry==(3 if n==3 else 4),(n, maximum_entry)
    expected_fix=3*int((S**n).trace())
    expected_periodic3=3*(int((T**n).trace())-1)
    assert observed[1]==expected_fix,(n, observed, expected_fix)
    assert observed[3]==3**(n+1)-expected_fix
    assert periodic[1]==1
    assert periodic[3]==expected_periodic3,(n,periodic,expected_periodic3)
    print(f'n={n} total={3**(n+1)} fixation_basin={observed[1]} period_three_states={periodic[3]} sharp_entry={maximum_entry}')
print('PASS wheel exact all-configuration checks and polynomial identities')
