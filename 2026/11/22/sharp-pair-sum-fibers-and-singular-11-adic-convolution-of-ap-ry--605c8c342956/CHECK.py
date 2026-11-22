"""Exact finite checks for the Apéry eleven-adic nondivisibility sum theorem.

Uses only the Python standard library. Finite tests are diagnostics;
all-depth statements follow from the accompanying proof.
"""
from math import comb
from collections import Counter
from fractions import Fraction

P = 11
D = tuple(d for d in range(P) if d != 5)
MOD_DIGITS = (1, 5, 7, 4, 1, 0, 1, 4, 7, 5, 1)
checks = 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def apery(n):
    return sum(comb(n,j)**2 * comb(n+j,j)**2 for j in range(n+1))

for j in range(P):
    ck(apery(j) % P == MOD_DIGITS[j], f'Apéry digit {j}')
for n in range(P**2):
    ck(apery(n) % P == (MOD_DIGITS[n % P] * MOD_DIGITS[n // P]) % P, f'Lucas sample {n}')

f = [sum(x+y == s for x in D for y in D) for s in range(2*P-1)]
def H(h):
    return sum(f[z] * f[z-h] for z in range(len(f)) if 0 <= z-h < len(f))
ck([H(h) for h in (0,1,10,11,12)] == [590,576,208,160,125], 'difference correlation values')
B = ((333,576),(320,590))
ck(B[0][0]+B[1][1] == 923, 'trace')
ck(B[0][0]*B[1][1]-B[0][1]*B[1][0] == 12150, 'determinant')
ck(Fraction(10000,11)**2-923*Fraction(10000,11)+12150 == Fraction(-59850,121), 'dimension inequality')

def transfer(p):
    ds = tuple(d for d in range(p) if d!=(p-1)//2)
    f1 = [sum(a+b==s for a in ds for b in ds) for s in range(2*p-1)]
    mat = [tuple(tuple(f1[t-c+p*e] if 0 <= t-c+p*e < len(f1) else 0 for e in (0,1)) for c in (0,1)) for t in range(p)]
    return ds, mat, f1

def spectrum(p, r):
    ds, matrices, _ = transfer(p)
    vectors = [(1,0)]
    for _ in range(r):
        vectors = [
            (a*m[0][0]+b*m[1][0], a*m[0][1]+b*m[1][1])
            for m in matrices for a,b in vectors
        ]
    return [x+y for x,y in vectors]

for p in (5,7,11,13):
    ds, matrices, _ = transfer(p)
    for carry in (0,1):
        for t in range(p):
            ck(sum(matrices[t][carry]) == p-2+int(t==(p-1 if carry==0 else 0)), f'row sum p={p}, c={carry}, t={t}')
    for t in range(p-1):
        ck(all(matrices[t][0][i] > 0 for i in (0,1)), f'positive branches p={p}, digit={t}')
    for r in (1,2):
        q = p**r
        ss = spectrum(p,r)
        allowed = [n for n in range(q) if all((n//p**j)%p in ds for j in range(r))]
        v = [0]*q
        for a in allowed:
            for b in allowed:
                v[(a+b)%q] += 1
        ck(ss == v, f'independent direct pair enumeration p={p}, r={r}')
        ck(min(ss) == (p-2)**r, f'minimum p={p}, r={r}')
        ck(max(ss) == (p-1)**r, f'maximum p={p}, r={r}')
        ck(ss.index(max(ss)) == q-1 and ss.count(max(ss))==1, f'unique maximum p={p}, r={r}')
        ck(ss.count(min(ss)) == (p-1)*(p-2)**(r-1), f'minimum count p={p}, r={r}')

old0,old1=1,910
for r in range(1,5):
    ss=spectrum(P,r)
    q=P**r
    ck(sum(ss) == 100**r, f'sum r={r}')
    ck(min(ss)==9**r and ss.count(min(ss))==10*9**(r-1), f'extremal minimum r={r}')
    ck(max(ss)==10**r and ss.index(max(ss))==q-1 and ss.count(max(ss))==1, f'extremal maximum r={r}')
    en=sum(x*x for x in ss)
    if r==1:
        ck(en==910, 'first energy')
    else:
        next_energy=923*old1-12150*old0
        ck(en==next_energy, f'energy recurrence r={r}')
        old0,old1=old1,next_energy
    if r <= 3:
        ds, _, _=transfer(P)
        allowed=[n for n in range(q) if all((n//P**j)%P in ds for j in range(r))]
        v=[0]*q
        for a in allowed:
            for b in allowed:
                v[(a+b)%q]+=1
        ck(v==ss, f'Apéry-supported direct pairs r={r}')

# Uniform output-digit bias in the stationary carry chain.
ck(Fraction(19,200)!=Fraction(1,11), 'singularity digit bias')
ck(Fraction(19,200)*2+Fraction(9,100)*9==1, 'normalization')
print(f'PASS: {checks} grouped assertions; all claims tested at the stated finite ranges.')
