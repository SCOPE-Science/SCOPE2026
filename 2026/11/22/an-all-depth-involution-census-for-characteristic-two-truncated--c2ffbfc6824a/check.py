"""Exhaustive finite checks for truncated substitution involution depth profiles.
Standard library only.  This program is evidence for small cases, not the infinite proof.
Run: python check.py
"""
from collections import Counter

IRREDUCIBLE = {2: 0b11, 4: 0b111, 8: 0b1011, 16: 0b10011}


def mult_table(q):
    degree = q.bit_length()-1
    polynomial = IRREDUCIBLE[q]
    table = [[0]*q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            v=0
            for i in range(degree):
                if (b>>i)&1:
                    v ^= a<<i
            for k in range(2*degree-2,degree-1,-1):
                if (v>>k)&1:
                    v ^= polynomial<<(k-degree)
            table[a][b]=v
    return table


def multiply(a,b,m,mult):
    o=[0]*m
    for i,x in enumerate(a):
        if x:
            for j in range(m-i):
                if b[j]:o[i+j]^=mult[x][b[j]]
    return o


def compose(f,m,mult):
    power=[0]*m
    power[0]=1
    out=[0]*m
    for c in f:
        if c:
            for j,v in enumerate(power):
                if v:out[j]^=mult[c][v]
        power=multiply(power,f,m,mult)
    return out


def predicted_depth(m,r,q):
    if r%2==0 and 2*r+1 < m:
        return 0
    if r%2:
        exponent=min((m-2)//2,m-r-2)
    else:
        exponent=m-r-2
    return (q-1)*q**exponent


def predicted_total(m,q):
    if m%2==0:
        h=m//2
        return q**(h-1)*(1+(q-1)*(h//2))
    h=(m-1)//2
    return q**(h-1)*(1+(q-1)*(h//2+1))


def enumerate_group(q,m):
    mul=mult_table(q)
    ct=Counter()
    for mask in range(q**(m-2)):
        f=[0,1]+[0]*(m-2)
        a=mask
        for j in range(2,m):
            f[j]=a%q
            a//=q
        if compose(f,m,mul)==[0,1]+[0]*(m-2):
            depth=next((j-1 for j in range(2,m) if f[j]),0)
            ct[depth]+=1
    return ct


def main():
    for q,last_m in [(2,15),(4,9),(8,7),(16,5)]:
        for m in range(3,last_m+1):
            actual=enumerate_group(q,m)
            expected={0:1}
            expected.update({r:predicted_depth(m,r,q) for r in range(1,m-1)})
            assert all(actual.get(r,0)==expected.get(r,0) for r in range(m-1)), (q,m,actual,expected)
            assert sum(actual.values())==predicted_total(m,q), (q,m,actual)
        print(f"q={q}, truncations m=3..{last_m}: depth and total counts verified")
    print("NOTTINGHAM_ALL_DEPTH_INVOLUTION_PROFILE_VERIFIED")

if __name__=='__main__':main()
