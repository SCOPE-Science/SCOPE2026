"""Exact finite certificates for two random interval-reversal averaging laws."""
from fractions import Fraction
from math import lcm

EXPECTED={
 2:Fraction(0),3:Fraction(1,2),4:Fraction(5,8),5:Fraction(41,60),
 6:Fraction(271,360),7:Fraction(113,140),8:Fraction(2813,3360),
 9:Fraction(824,945),10:Fraction(5689,6300),
 11:Fraction(3254,3465),12:Fraction(322507,332640),
 13:Fraction(355991,360360),14:Fraction(5105521,5045040)}

def reverse_index(i,a,b):
    return a+b-i if a<=i<=b else i

def coefficient_direct(n, law):
    """Independent direct step-vector action, exact rational arithmetic."""
    if law=='interval': weights={(a,b):Fraction(2,n*(n+1)) for a in range(n) for b in range(a,n)}
    else: weights={(a,b):Fraction(1,n*(n-b+a)) for a in range(n) for b in range(a,n)}
    out=[]
    for k in range(1,n):
        q=[]
        for i in range(n):
            q.append(sum((w for (a,b),w in weights.items() if reverse_index(i,a,b)>=k),Fraction(0)))
        out.append(sum((abs(q[i+1]-q[i]) for i in range(n-1)),Fraction(0)))
    return out

def coefficient_matrix(n,law):
    """Independent construction of the full position transition matrix."""
    P=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(a,n):
            w=Fraction(2,n*(n+1)) if law=='interval' else Fraction(1,n*(n-b+a))
            for i in range(n):P[i][reverse_index(i,a,b)]+=w
    assert all(sum(row)==1 for row in P)
    vals=[]
    for k in range(1,n):
        v=[sum(P[i][j] for j in range(k,n)) for i in range(n)]
        vals.append(sum(abs(v[i+1]-v[i]) for i in range(n-1)))
    return vals

def count_interval_gradient(n,k,i):
    """Exact combinatorial kernel of D P H^k, one-based i and k."""
    if i<k: return n-k-min(i,n-k)
    if i>k: return k-min(k,n-i)
    return k*(k-1)//2+(n-k-1)*(n-k)//2+n-min(k,n-k)

for n in range(2,15):
    vals=coefficient_direct(n,'length')
    assert vals==coefficient_matrix(n,'length')
    assert max(vals)==EXPECTED[n],(n,max(vals))
    assert (max(vals)>1)==(n==14)
    print('LENGTH_UNIFORM_EXACT',n,max(vals),'max_step',1+vals.index(max(vals)))
print('FIRST_AMPLIFICATION_AT_N14_EXACT_PASS')

for n in range(2,31):
    grad=coefficient_direct(n,'interval')
    assert all(v==Fraction(n-1,n+1) for v in grad)
    for k in range(1,n):
        for i in range(1,n):
            c=count_interval_gradient(n,k,i)
            assert c>=0
            if n<=14:
                direct=0
                for a in range(1,n+1):
                    for b in range(a,n+1):
                        direct+=(reverse_index(i+1,a,b)>k)-(reverse_index(i,a,b)>k)
                assert c==direct,(n,k,i,c,direct)
    print('INTERVAL_UNIFORM',n,Fraction(n-1,n+1))
print('UNIFORM_INTERVAL_SHARP_CONTRACTION_COUNTS_PASS')

assert Fraction(5105521,5045040)-1==Fraction(60481,5045040)
print('EXPLICIT_N14_STEP_WITNESS_PASS')
print('ALL_INTERVAL_REVERSAL_CHECKS_PASS')
