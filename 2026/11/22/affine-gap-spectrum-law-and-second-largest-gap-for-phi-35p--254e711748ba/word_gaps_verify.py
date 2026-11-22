#!/usr/bin/env python3
"""Exact finite certificate for the gap law of Phi_{35p}; standard library only."""
from collections import Counter
from csv import DictReader
from pathlib import Path
from math import gcd

M = 35
C = [1,-1,0,0,0,1,-1,1,-1,0,1,-1,1,-1,1,0,-1,1,-1,1,0,0,0,-1,1]
U = [r for r in range(1,35) if gcd(r,35)==1]
EXPECTED_S = {1:23,2:22,3:21,4:20,6:18,8:16,9:15,11:13,12:12,13:11,16:8,17:7,18:7,19:8,22:11,23:12,24:13,26:15,27:16,29:18,31:20,32:21,33:22,34:23}
EXPECTED_AB={1:(8,0),2:(8,0),3:(8,0),4:(8,0),6:(8,0),8:(10,2),9:(8,2),11:(8,2),12:(8,2),13:(8,2),16:(10,4),17:(10,4),18:(10,6),19:(10,6),22:(8,6),23:(8,6),24:(8,6),26:(8,6),27:(10,8),29:(8,8),31:(8,8),32:(8,8),33:(8,8),34:(8,8)}

def h(t):
    t %= M
    return (t < 5) - (7 <= t < 12)

def word(j,r):
    return [sum(C[e]*h((j-e)*r+t) for e in range(j+1)) for t in range(M)]

def hist(vals, circular=False):
    positions = [i for i,v in enumerate(vals) if v]
    assert positions
    gaps = [b-a for a,b in zip(positions,positions[1:])]
    if circular: gaps.append(len(vals)+positions[0]-positions[-1])
    return Counter(gaps)

def direct_quotient(u):
    """Polynomial long division Phi_35(X**u)/Phi_35(X), independent of h."""
    d=24*(u-1)
    b=[0]*(d+1)
    for n in range(d+1):
        rhs = C[n//u] if n%u==0 and n//u < 25 else 0
        b[n] = rhs - sum(C[e]*b[n-e] for e in range(1,min(n,24)+1))
    # Entire product of denominator and b must equal Phi_35(X**u).
    for n in range(24*u+1):
        val=sum(C[e]*b[n-e] for e in range(25) if 0 <= n-e <= d)
        target=C[n//u] if n%u==0 and n//u<25 else 0
        assert val==target, (u,n,val,target)
    return b

def coeff_via_periodic(u):
    d=24*(u-1)
    return [sum(C[j]*h(n-j*u) for j in range(25) if n>=j*u) for n in range(d+1)]

def calc():
    table=[]
    for r in U:
        ws=[word(j,r) for j in range(24)]
        assert all(sum(v!=0 for v in w)>=4 for w in ws)
        slope=sum((hist(w, True) for w in ws),Counter())
        base_b=direct_quotient(35+r)
        assert base_b==coeff_via_periodic(35+r)
        base=hist(base_b)
        assert base[24]==2 and slope[24]==2
        g2=max(g for g in base.keys()|slope.keys() if g<24)
        assert g2==EXPECTED_S[r]==24-min(r,35-r)
        assert (slope[g2],base[g2]-slope[g2])==EXPECTED_AB[r]
        assert all(not (g2<g<24) for g in base.keys()|slope.keys())
        for q in (2,3):
            u=35*q+r
            b=direct_quotient(u)
            assert b==coeff_via_periodic(u)
            H=hist(b)
            expected=base+Counter({g:(q-1)*v for g,v in slope.items()})
            assert H==expected,(r,q,H,expected)
        assert sum(base.values()) == sum(1 for v in base_b if v)-1
        for g in range(1,25):
            table.append({'r':r,'gap':g,'base':base[g],'slope':slope[g]})
    return table

def write_csv(rows,path):
    from csv import DictWriter
    with open(path,'w',encoding='utf-8',newline='') as f:
        w=DictWriter(f,fieldnames=['r','gap','base','slope'],lineterminator='\n')
        w.writeheader();w.writerows(rows)

def verify_csv(rows,path):
    with open(path,encoding='utf-8',newline='') as f:
        actual=[{k:int(v) for k,v in a.items()} for a in DictReader(f)]
    assert actual==rows

if __name__=='__main__':
    rows=calc()
    csvpath=Path(__file__).with_name('gap_spectrum_35.csv')
    if not csvpath.exists(): write_csv(rows,csvpath)
    verify_csv(rows,csvpath)
    print('PASS: 24 unit classes; 576 (base,slope) pairs; quotient exact checks at 72 indices 35q+r (q=1,2,3).')
    print('PASS: all-word nonzero, second-gap formula and multiplicities, complete CSV verified.')
