"""Finite exact checks for the 29-adic first-shell law of Franel numbers.
Run: python3 verify.py. The universal proof uses Gessel--Lucas congruences.
"""
from math import comb
P=29
Z={12,14,16}
C={12:7,14:2,16:5}
B={12:3,14:4,16:18}
BAD={(12,17),(16,11)}

def direct(n):
    return sum(comb(n,j)**3 for j in range(n+1))

def classify(n):
    digits=[]
    while n:
        digits.append(n%P); n//=P
    digits.append(0)  # leading zero, needed for the top neighbor
    positions=[j for j,d in enumerate(digits) if d in Z]
    if not positions: return 0
    if len(positions)>1:return 2
    j=positions[0]
    return 2 if (digits[j],digits[j+1]) in BAD else 1

def main():
    exact=[1,2]
    for n in range(1,2600):
        numer=(7*n*n+7*n+2)*exact[-1]+8*n*n*exact[-2]
        assert numer % ((n+1)*(n+1)) == 0
        exact.append(numer//((n+1)*(n+1)))
    for n in range(58):
        assert exact[n] == direct(n),n
    roots=[d for d in range(P) if exact[d]%P==0]
    assert roots==[12,14,16],roots
    for d in roots:
        assert exact[d]%(P*P)==P*C[d],(d,exact[d]%(P*P))
        val=(exact[P+d]-2*exact[d])//P
        assert (exact[P+d]-2*exact[d])%P==0
        b=val*pow(2,-1,P)%P
        assert b==B[d],(d,b)
        assert {m for m in range(P) if (C[d]+m*B[d])%P==0}=={ {12:17,14:14,16:11}[d] }
    counts=[0,0,0]
    for n in range(2600):
        pred=classify(n)
        v=0 if exact[n]%P else (1 if exact[n]%(P*P) else 2)
        assert pred==v,(n,pred,v)
        if n<P*P:counts[v]+=1
    assert counts==[676,154,11],counts
    for L in (1,2):
        c=[0,0,0]
        for n in range(P**L):c[classify(n)]+=1
        N0=26**L
        N1=3*26**(L-1)+(76*(L-1)*26**(L-2) if L>=2 else 0)
        assert c==[N0,N1,P**L-N0-N1],(L,c)
    print('PASS: 58 independent direct sums, 29 digit residues, 3 derivative residues, 2600 all-index classifications, 841 complete two-digit fibers.')
    print('mod 29^2 histogram for n<841:',counts)
    print('critical pairs:',sorted(BAD))

if __name__=='__main__':main()
