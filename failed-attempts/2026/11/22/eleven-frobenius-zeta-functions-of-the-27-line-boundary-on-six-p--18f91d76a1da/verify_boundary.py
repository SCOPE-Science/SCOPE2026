"""Exact orbit certificates for the 27 exceptional-line boundary of a cubic surface.

Run: python3 verify_boundary.py (writes 27_line_frobenius.csv in the same directory).
All operations are on integer intersection classes and finite permutations.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import gcd
import csv
from pathlib import Path

N=6
E0=[('E',(i,)) for i in range(N)]
L0=[('L',(i,j)) for i,j in combinations(range(N),2)]
Q0=[('Q',(i,)) for i in range(N)]
CURVES=tuple(E0+L0+Q0)
H=(1,)+(0,)*6

def class_of(v):
    kind, t=v
    if kind=='E':return (0,)+tuple(int(j==t[0]) for j in range(6))
    if kind=='L':return (1,)+tuple(-int(j in t) for j in range(6))
    return (2,)+tuple(-int(j!=t[0]) for j in range(6))

def dot(a,b):return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,7))

EDGES=tuple((a,b) for a,b in combinations(CURVES,2) if dot(class_of(a),class_of(b))==1)
EDGES_SET=set(EDGES)
assert len(CURVES)==27 and len(EDGES)==135
assert all(dot(class_of(c),class_of(c))==-1 for c in CURVES)
assert all(dot(class_of(a),class_of(b)) in (0,1) for a,b in combinations(CURVES,2))

# Independent direct combinatorial construction of the same 135 meeting pairs.
direct=set()
for a,b in combinations(CURVES,2):
    x,y=(a,b) if a[0]<=b[0] else (b,a)
    i,j=x[1],y[1]
    hit=(x[0],y[0])==('E','L') and i[0] in j
    hit|=(x[0],y[0])==('E','Q') and i!=j
    hit|=(x[0],y[0])==('L','L') and not(set(i)&set(j))
    hit|=(x[0],y[0])==('L','Q') and j[0] in i
    if hit:direct.add((a,b))
assert EDGES_SET==direct
assert all(sum(v in e for e in EDGES)==10 for v in CURVES)

# Connectedness, hence arithmetic genus 135-27+1=109.
reached={CURVES[0]}
while True:
    step=reached|{x for e in EDGES for x in e if e[0] in reached or e[1] in reached}
    if step==reached: break
    reached=step
assert len(reached)==27

BRANCHES=tuple((edge,endpoint) for edge in EDGES for endpoint in edge)

def orbit_decomp(objects,action):
    rem=set(objects);orbits=[]
    while rem:
        start=next(iter(rem));cur=start;orbit=[]
        while cur not in orbit:
            assert cur in rem
            rem.remove(cur);orbit.append(cur);cur=action(cur)
        assert cur==start
        orbits.append(orbit)
    return orbits

def cycles(counter): return tuple(sorted((k,v) for k,v in counter.items() if v))

def sigma_type(p):
    unused=set(range(6)); out=[]
    while unused:
        s=next(iter(unused));i=s;length=0
        while i in unused:
            unused.remove(i);length+=1;i=p[i]
        assert i==s
        out.append(length)
    return tuple(sorted(out))

def perm_of_type(parts):
    result=list(range(6));start=0
    for d in parts:
        for i in range(d):result[start+i]=start+(i+1)%d
        start+=d
    return tuple(result)

def data(p):
    def pv(v):return (v[0],tuple(sorted(p[i] for i in v[1])))
    def pe(edge):return tuple(sorted((pv(edge[0]),pv(edge[1]))))
    def pb(branch):return (pe(branch[0]),pv(branch[1]))
    vo=orbit_decomp(CURVES,pv)
    eo=orbit_decomp(EDGES,pe)
    bo=orbit_decomp(BRANCHES,pb)
    v=Counter(map(len,vo));e=Counter(map(len,eo));b=Counter(map(len,bo));pos=Counter();neg=Counter()
    for orbit in eo:
        d=len(orbit);root=orbit[0];end=root[0]
        for i in range(d):end=pv(end)
        if end==root[0]:pos[d]+=1
        else:
            assert end==root[1]
            neg[d]+=1
    assert sum(k*n for k,n in v.items())==27
    assert sum(k*n for k,n in e.items())==135
    assert sum(k*n for k,n in b.items())==270
    assert all(e[k]==pos[k]+neg[k] for k in e)
    assert all(b[k]==2*pos[k]+(neg[k//2] if k%2==0 else 0) for k in b)
    z=Counter({d:b[d]-e[d]-v[d] for d in set(v)|set(e)|set(b)})
    point= lambda q:(q+1)*v[1]+e[1]-b[1]
    assert point(7)>=0
    # Logarithmic coefficients of the zeta product versus direct fixed-point counts.
    for r in range(1,13):
        fixed_v=sum(d*n for d,n in v.items() if r%d==0)
        fixed_e=sum(d*n for d,n in e.items() if r%d==0)
        fixed_b=sum(d*n for d,n in b.items() if r%d==0)
        for q in (5,7):
            direct_q=(q**r+1)*fixed_v+fixed_e-fixed_b
            from_z=sum(d*((q**r)*v[d]-z[d]) for d in set(v)|set(z) if r%d==0)
            assert direct_q==from_z
    # Torus point count via integral graph-cycle representation.
    for q in (5,7):
        num=(q-1)
        for d,n in pos.items():num*=(q**d-1)**n
        for d,n in neg.items():num*=(q**d+1)**n
        den=1
        for d,n in v.items():den*=(q**d-1)**n
        assert num%den==0 and num//den>0
    return (cycles(v),cycles(e),cycles(b),cycles(pos),cycles(neg),cycles(z),point(0),point(1))

# Independent reference values, computed by the blow-up intersection classes.
EXPECTED={
(1,1,1,1,1,1):({1:27},{1:135},{1:270},{1:135},{},{1:108},(27,-108)),
(1,1,1,1,2):({1:15,2:6},{1:45,2:45},{1:90,2:90},{1:45,2:45},{},{1:30,2:39},(15,-30)),
(1,1,1,3):({1:9,3:6},{1:18,3:39},{1:36,3:78},{1:18,3:39},{},{1:9,3:33},(9,-9)),
(1,1,2,2):({1:7,2:10},{1:11,2:62},{1:18,2:126},{1:9,2:62},{1:2},{2:54},(7,0)),
(1,1,4):({1:5,2:1,4:5},{1:7,2:2,4:31},{1:12,2:3,4:63},{1:6,2:1,4:31},{1:1,2:1},{4:27},(5,0)),
(1,2,3):({1:3,2:3,3:4,6:1},{2:9,3:15,6:12},{2:18,3:30,6:24},{2:9,3:15,6:12},{},{1:-3,2:6,3:11,6:11},(3,3)),
(1,5):({1:2,5:5},{5:27},{5:54},{5:27},{},{1:-2,5:22},(2,2)),
(2,2,2):({1:3,2:12},{1:9,2:63},{1:6,2:132},{1:3,2:63},{1:6},{1:-6,2:57},(3,6)),
(2,4):({1:1,2:3,4:5},{1:1,2:5,4:31},{2:9,4:63},{2:4,4:31},{1:1,2:1},{1:-2,2:1,4:27},(1,2)),
(3,3):({3:9},{3:45},{3:90},{3:45},{},{3:36},(0,0)),
(6,):({3:1,6:4},{3:3,6:21},{3:2,6:44},{3:1,6:21},{3:2},{3:-2,6:19},(0,0)),
}
assert len(EXPECTED)==11
stats=Counter();rows=[];signatures=set()
for p in permutations(range(6)):
    part=sigma_type(p)
    result=data(p)
    expected=EXPECTED[part]
    assert result[:6]==tuple(cycles(Counter(d)) for d in expected[:6]),(part,result,expected)
    assert (result[7]-result[6],result[6])==expected[6]
    stats[part]+=1
    signatures.add((result[0],result[5]))
    if p==perm_of_type(part):
        def fmt(c):return ';'.join(f'{k}^{v}' for k,v in c)
        v,e,b,pos,neg,z,intercept,at1=result
        slope=at1-intercept
        formula=(str(intercept) if slope==0 else (('q' if slope==1 else f'{slope}q')+(f'{intercept:+d}' if intercept else '')))
        rows.append((part,fmt(v),fmt(e),fmt(b),fmt(pos),fmt(neg),fmt(z),formula,neg[0][1] if neg and neg[0][0]==1 else 0))
assert len(rows)==11 and len(signatures)==11
assert sum(stats.values())==720
assert {p for p in EXPECTED if EXPECTED[p][6]==(0,0)}=={(3,3),(6,)}
assert all(data(perm_of_type(p))[4][0][1]==EXPECTED[p][4][1] if (1 in EXPECTED[p][4]) else True for p in EXPECTED)
rows.sort(key=lambda r:(len(r[0]),r[0]),reverse=True)
path=Path(__file__).with_name('27_line_frobenius.csv')
with path.open('w',newline='',encoding='utf-8') as out:
    writer=csv.writer(out)
    writer.writerow(['six_point_cycle_type','line_orbits','node_orbits','branch_orbits','positive_node_orbits','negative_node_orbits','zeta_unit_exponents','D_Fq_points','nonsplit_rational_nodes'])
    for part,v,e,b,pos,neg,z,f,n in rows:
        writer.writerow(['+'.join(map(str,part)),v,e,b,pos,neg,z,f,n])
print('CUBIC_27_LINE_BOUNDARY_S6_ZETA_OK permutations=720 classes=11 distinct_zeta=11 point_free=3+3,6 graph_betti=109')
