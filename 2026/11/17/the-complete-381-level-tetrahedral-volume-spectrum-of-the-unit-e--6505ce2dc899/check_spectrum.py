"""Exact census of tetrahedral volumes in the unit-edge truncated icosahedron.

Run: python check_spectrum.py spectrum.tsv
Only Python's standard library is required. The arithmetic ring is Z[phi],
phi=(1+sqrt(5))/2, represented as the integer pair (a,b)=a+b*phi.
"""
import collections
import csv
import itertools
import math
import sys
from functools import cmp_to_key

ZERO=(0,0)
def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def minus(x,y): return (x[0]-y[0],x[1]-y[1])
def times(x,y): return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def sign(x):
    # x=(p+q*sqrt(5))/2 where p=2*a+b and q=b.
    a,b=x; p=2*a+b
    if p==0: return (b>0)-(b<0)
    if b==0 or p*b>0: return (p>0)-(p<0)
    return ((p*p>5*b*b)-(p*p<5*b*b))*((p>0)-(p<0))
def positive_abs(x): return x if sign(x)>=0 else (-x[0],-x[1])
def compare(x,y): return sign(minus(x,y))
def determinant(x,y,z):
    a,b,c=x;d,e,f=y;g,h,i=z
    return plus(minus(times(a,minus(times(e,i),times(f,h))),times(b,minus(times(d,i),times(f,g)))),times(c,minus(times(d,h),times(e,g))))
def original_vertices():
    # Twelve icosahedral vertices (0,+/-1,+/-phi), etc.
    v=[]
    for s,t in itertools.product((-1,1),repeat=2):
        v.extend([((0,0),(s,0),(0,t)),((s,0),(0,t),(0,0)),((0,t),(0,0),(s,0))])
    return v
def distance2(x,y):
    result=ZERO
    for a,b in zip(x,y):
        u=minus(a,b); result=plus(result,times(u,u))
    return result
def scaled_vertices():
    v=original_vertices()
    edges=[(i,j) for i,j in itertools.combinations(range(12),2) if distance2(v[i],v[j])==(4,0)]
    assert len(edges)==30
    def point(a,b):return tuple(plus(times((2,0),u),w) for u,w in zip(v[a],v[b]))
    # Produced points are 3 times the one-third truncation, and twice
    # the coordinates of the solid with unit edge length.
    points=[point(i,j) for i,j in edges]+[point(j,i) for i,j in edges]
    assert len(points)==60 and len(set(points))==60
    assert all(distance2(v[i],v[j])==(4,0) for i,j in edges)
    return points

def census():
    v=scaled_vertices()
    diffs=[[tuple(minus(v[i][k],v[j][k]) for k in range(3)) for j in range(60)] for i in range(60)]
    counts=collections.Counter(); sample={}; selections={}
    for a in range(57):
        for b in range(a+1,58):
            x=diffs[b][a]
            for c in range(b+1,59):
                y=diffs[c][a]
                for d in range(c+1,60):
                    h=positive_abs(determinant(x,y,diffs[d][a]))
                    counts[h]+=1
                    if h not in sample: sample[h]=(a,b,c,d)
                    # Store selections only for the two highest levels separately below.
    levels=sorted(counts,key=cmp_to_key(lambda x,y:-compare(x,y)))
    return v,counts,levels,sample

def shape_signature(points, inds):
    ds={tuple(sorted((i,j))):distance2(points[i],points[j]) for i,j in itertools.combinations(inds,2)}
    return min(tuple(ds[tuple(sorted((p[i],p[j])))] for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))) for p in itertools.permutations(inds))

def main(path):
    points,counts,levels,sample=census()
    with open(path,encoding='utf-8',newline='') as f:
        rd=csv.reader(f,delimiter='\t'); head=next(rd)
        assert head==['det_phi_a','det_phi_b','multiplicity'],head
        stored=[(int(a),int(b),int(m)) for a,b,m in rd]
    expected=[(*k,counts[k]) for k in levels]
    assert stored==expected,'Census differs from supplied complete exact table'
    assert len(counts)==381 and sum(counts.values())==math.comb(60,4)==487635
    assert levels[:3]==[(100,164),(100,160),(96,160)]
    assert [counts[h] for h in levels[:3]]==[120,120,60]
    assert counts[ZERO]>0
    # Independent Cauchy--Binet squared-determinant identity:
    # 60 centered vectors of squared norm 10+9*phi have sum xx^T
    # equal to 20*(10+9*phi)*I. Consequently sum det^2=
    # 60*20^3*(10+9*phi)^3 for the augmented 60x4 matrix.
    sum_sq=ZERO
    for h,m in counts.items(): sum_sq=plus(sum_sq,times((m,0),times(h,h)))
    r=(10,9); expected_sq=times((480000,0),times(r,times(r,r)))
    assert sum_sq==expected_sq,(sum_sq,expected_sq)
    # Check radius exactly and centeredness without geometry assumptions.
    assert all(distance2(v,ZERO if False else ((0,0),)*3)==r for v in points)
    assert tuple((sum(v[k][0] for v in points),sum(v[k][1] for v in points)) for k in range(3))==(ZERO,ZERO,ZERO)
    for k in range(3):
        for j in range(3):
            dot=ZERO
            for v in points:dot=plus(dot,times(v[k],v[j]))
            assert dot==(times((20,0),r) if k==j else ZERO)
    # Top two congruence classes are also independently checked.
    top2=set(levels[:2]); sig={h:set() for h in top2}; hit=collections.Counter()
    for inds in itertools.combinations(range(60),4):
        a,b,c,d=inds
        da=tuple(minus(points[b][k],points[a][k]) for k in range(3))
        db=tuple(minus(points[c][k],points[a][k]) for k in range(3))
        dc=tuple(minus(points[d][k],points[a][k]) for k in range(3))
        h=positive_abs(determinant(da,db,dc))
        if h in top2:
            sig[h].add(shape_signature(points,inds));hit[h]+=1
    assert all(len(sig[h])==1 and hit[h]==120 for h in top2)
    print('SOCCER_TETRAHEDRON_SPECTRUM_PASS levels=381 combinations=487635')
    print('top',levels[:3], 'multiplicities',[counts[h] for h in levels[:3]])
    print('unit-edge maximum=(100+164*phi)/48, second=(100+160*phi)/48')
    print('sharp discrete gap=phi/12; each top shape one congruence class')
    print('sum_squared_raw_determinants=',sum_sq)

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python check_spectrum.py spectrum.tsv')
    main(sys.argv[1])
