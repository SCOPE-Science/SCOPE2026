#!/usr/bin/env python3
"""Exact point-count certificate for genus-three quartics Y^4=X^3Z+aXZ^3+bZ^4 over F_7.

Python 3 standard library; no external dependencies or network.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

P = 7
MOD = {1:(0,1), 2:(1,0,1), 3:(1,1,0,1)}
EXPECTED = {
    (-5, 7):1, (5, 7):1,
    (-4,-14):1, (4,-14):1,
    (-4,14):3, (4,14):3,
    (-3,7):3, (3,7):3,
    (-2,0):6, (2,0):6,
    (-1,7):4, (1,7):4,
    (0,14):6,
}


def finite_field(n):
    """Base-7 coefficient representation in F_7[u]/(MOD[n])."""
    q=P**n
    if n == 2: assert all((r*r+1)%P != 0 for r in range(P))
    if n == 3: assert all((r**3+r+1)%P != 0 for r in range(P))
    coeff=[tuple((k//P**j)%P for j in range(n)) for k in range(q)]
    def enc(v):return sum(int(v[i])*P**i for i in range(n))
    add=[[enc([(x[i]+y[i])%P for i in range(n)]) for y in coeff] for x in coeff]
    mul=[]
    for x in coeff:
        row=[]
        for y in coeff:
            v=[0]*(2*n-1)
            for i,xi in enumerate(x):
                for j,yj in enumerate(y):v[i+j]=(v[i+j]+xi*yj)%P
            for k in range(2*n-2,n-1,-1):
                for i in range(n):v[k-n+i]=(v[k-n+i]-v[k]*MOD[n][i])%P
            row.append(enc(v[:n]))
        mul.append(row)
    def power(x,e):
        z=1
        while e:
            if e&1:z=mul[z][x]
            x=mul[x][x];e//=2
        return z
    return q,add,mul,power


def point_counts(n):
    q,add,mul,power=finite_field(n)
    fourth=Counter(power(y,4) for y in range(q))
    square=Counter(power(z,2) for z in range(q))
    xc=[power(x,3) for x in range(q)]
    counts={}; elliptic={}
    for a in range(P):
        for b in range(P):
            if (b*b-4*a*a*a)%P==0:continue
            vals=[add[add[xc[x]][mul[a][x]]][b] for x in range(q)]
            counts[(a,b)]=1+sum(fourth[v] for v in vals)
            elliptic[(a,b)]=1+sum(square[v] for v in vals)
            if n%2:assert counts[(a,b)]==elliptic[(a,b)]
    if n==2:
        # independent fourth-power subgroup test: 4 roots iff c^(12)=1.
        for a,b in counts:
            n2=1+sum(1 if (v:=add[add[xc[x]][mul[a][x]]][b])==0 else
                       (4 if power(v,12)==1 else 0) for x in range(q))
            assert n2==counts[(a,b)]
    return counts,elliptic


def main():
    C1,E1=point_counts(1)
    C2,E2=point_counts(2)
    C3,E3=point_counts(3)
    hist=Counter(); by_pair={}
    for a,b in sorted(C1):
        t=8-C1[(a,b)]
        z=C2[(a,b)]-64+t*t
        assert z%2==0
        u=z//2
        hist[t,u]+=1
        # Multiply factors rather than trusting a manually supplied formula.
        L=[0]*7
        for i,ci in enumerate([1,-t,7]):
            for j,cj in enumerate([1,0,u,0,49]):L[i+j]+=ci*cj
        # From roots, odd field-degree three trace is elliptic only.
        s3=t**3-3*7*t
        assert C3[(a,b)]==7**3+1-s3
        by_pair[(a,b)]={'a':a,'b':b,'N1':C1[(a,b)],'N2':C2[(a,b)],
                        'N3':C3[(a,b)],'t':t,'u':u,'weil_coefficients':L}
    assert len(by_pair)==42 and hist==EXPECTED,(len(by_pair),hist)
    data=json.loads(Path(__file__).with_name('SPECTRUM.json').read_text(encoding='utf-8'))
    assert data['field']=='F_7' and data['curve']=='y^4=x^3+a*x+b'
    assert data['smooth_models']==42 and data['distinct_weil_polynomials']==13
    assert data['prym_u_counts']=={'-14':2,'0':12,'7':16,'14':12}
    supplied={(r['t'],r['u']):r for r in data['spectrum']}
    assert len(supplied)==13
    for key,n in EXPECTED.items():
        assert supplied[key]['multiplicity']==n
        assert [tuple(z) for z in supplied[key]['parameters']]==[
            (a,b) for (a,b),record in by_pair.items()
            if (record['t'],record['u'])==key]
        assert supplied[key]['weil_coefficients']==next(
            z['weil_coefficients'] for z in by_pair.values() if (z['t'],z['u'])==key)
    print('VERIFY_CYCLIC4_F7_OK: 42 smooth models; 13 Weil polynomials; 4 rational Prym types')
    print('Independent F_49 fourth-power test passed; F_343 odd-degree/elliptic equality passed')

if __name__=='__main__':main()
