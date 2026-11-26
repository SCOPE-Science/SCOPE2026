"""Finite-prefix independent check for valuation words and asymptotic frequency table.
Run: python3 check_prefix.py
"""
from collections import Counter
from fractions import Fraction

def predicted(q,n):
    L=1<<(n-1).bit_length()
    M=L//4
    if n==1: return Counter({Fraction(1<<j,(1<<q)-1):1 for j in range(q)})
    if n==2: return Counter({Fraction(2,L*((1<<q)-1)):3,**{Fraction(1<<j,L*((1<<q)-1)):2 for j in range(2,q)}})
    a=max(0,3*M-n)
    c=max(0,n-3*M)
    b=M-a-c
    t=Counter()
    t[2]=4*b+6*c
    if q==2: t[4]=3*a+b
    else:
        t[4]=3*a+3*b+4*c
        for j in range(3,q): t[1<<j]=2*a+3*b+4*c
        t[1<<q]=2*a+b
    return Counter({Fraction(w,L*((1<<q)-1)):num for w,num in t.items() if num})

T=1<<17
cases=0
maxerr=0.0
for q in range(2,7):
    w=bytes((((x & -x).bit_length()-1) % q) for x in range(1,T+65))
    for n in range(1,29):
        obs=Counter(w[i:i+n] for i in range(T))
        theo=predicted(q,n)
        assert len(obs)==sum(theo.values()), (q,n,len(obs),theo)
        vals=sorted(float(z/T) for z in obs.values())
        expected=sorted(v for x,m in theo.items() for v in [float(x)]*m)
        err=max(abs(x-y) for x,y in zip(vals,expected))
        maxerr=max(maxerr,err)
        assert err<0.00015, (q,n,err)
        cases+=1
print(f'PASS: {cases} finite-prefix tests (q=2..6, n=1..28, {T} starts each); exact support and sorted frequencies within {maxerr:.8f} absolute error.')
print('Finite-prefix tests are approximations; all-length proof is separate.')
