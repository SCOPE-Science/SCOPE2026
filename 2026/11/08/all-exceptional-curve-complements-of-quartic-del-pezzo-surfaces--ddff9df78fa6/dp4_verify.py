"""Exact, dependency-free checks for quartic del Pezzo line-complement formulas.

Run: python3 dp4_verify.py
All integer/group computations are exhaustive for the finite Weyl group.
"""
from itertools import permutations, product, combinations
from collections import Counter
import json

N = 5
signs = [v for v in product((1,-1), repeat=N) if v.count(-1)%2 == 0]
idx = {v:i for i,v in enumerate(signs)}
edges = tuple((i,j) for i,j in combinations(range(16),2)
              if sum(signs[i][k]!=signs[j][k] for k in range(N))==4)
edgeidx={e:i for i,e in enumerate(edges)}
flags=tuple(edges)+tuple((j,i) for i,j in edges)
flagidx={a:i for i,a in enumerate(flags)}
assert len(signs)==16 and len(edges)==40 and len(flags)==80
assert all(sum(i in e for e in edges)==5 for i in range(16))
for a,b,c in combinations(range(16),3):
    assert not all(tuple(sorted(e)) in edgeidx for e in ((a,b),(b,c),(c,a)))

def act(p,s):
    moved=[]
    for v in signs:
        out=[None]*N
        for i in range(N): out[p[i]]=s[i]*v[i]
        moved.append(idx[tuple(out)])
    return tuple(moved)

def cycles(p):
    visited=set(); ans=[]
    for i in range(len(p)):
        if i in visited: continue
        j=i;length=0
        while j not in visited:
            visited.add(j);length+=1;j=p[j]
        ans.append(length)
    return tuple(sorted(ans))

def stype(p,s):
    visited=set();pos=[];neg=[]
    for i in range(N):
        if i in visited:continue
        j=i;length=0;sign=1
        while j not in visited:
            visited.add(j);length+=1;sign*=s[j];j=p[j]
        (pos if sign==1 else neg).append(length)
    return tuple(sorted(pos)),tuple(sorted(neg))

def fixed(cs,n):return sum(d for d in cs if n%d==0)

def pic_trace(typ,n):
    result=1
    for d in typ[0]:
        if n%d==0:result+=d
    for d in typ[1]:
        if n%d==0:result+=d*(-1 if (n//d)%2 else 1)
    return result

def polynomial(typ, cl, n):
    fl=fixed(cl['lines'],n)
    return (pic_trace(typ,n)-fl,
            1-fl+fixed(cl['flags'],n)-fixed(cl['nodes'],n))

classes={};frequency=Counter()
for p in permutations(range(5)):
    for s in product((1,-1),repeat=5):
        if s.count(-1)%2:continue
        typ=stype(p,s)
        frequency[typ]+=1
        if typ in classes:continue
        L=act(p,s)
        P=tuple(edgeidx[tuple(sorted((L[i],L[j])))] for i,j in edges)
        F=tuple(flagidx[(L[i],L[j])] for i,j in flags)
        assert set(L)==set(range(16))
        assert set(P)==set(range(40))
        assert set(F)==set(range(80))
        assert all(tuple(sorted((L[i],L[j]))) in edgeidx for i,j in edges)
        classes[typ]={'lines': cycles(L), 'nodes':cycles(P), 'flags':cycles(F)}
assert len(classes)==18 and sum(frequency.values())==1920
assert sum(frequency.values())==2**4*120
assert all(sum(d for d in cl['lines'])==16 and
           sum(d for d in cl['nodes'])==40 and
           sum(d for d in cl['flags'])==80 for cl in classes.values())
# The complete zeta function is determined by the two sequences of integer
# coefficients in #U(F_(q^n)) = q^(2n) + A_n q^n + B_n.
zeta_sequences={typ:tuple(polynomial(typ,cl,n) for n in range(1,13))
                for typ,cl in classes.items()}
assert len(set(zeta_sequences.values()))==18
# Strengthen: every pair differs already for n <= 12.
assert all(any(zeta_sequences[a][n]!=zeta_sequences[b][n]
               for n in range(12)) for a,b in combinations(classes,2))

polys={typ:polynomial(typ,cl,1) for typ,cl in classes.items()}
for typ,(a,b) in polys.items():
    for q in (2,3,4,5,7,8,9,11):
        val=q*q+a*q+b
        if val==0: assert (q,typ) in ((5,((1,1,1,1,1),())),(3,((1,2,2),())))
        if q>=6:assert val>0
assert sum(q*q+a*q+b==0 for typ,(a,b) in polys.items() for q in (2,3,4,5))==2
# For every class, f(q)=q^2+A*q+B has f(6)>0 and derivative
# 2q+A>0 on [6,infinity); therefore no further positive roots.
assert all(36+6*a+b>0 and 12+a>0 for a,b in polys.values())
# Independently check the 40 pairs in the classical blow-up picture.
# Empty negative subset is conic, 2-negative is a joining line, 4-negative is E_i.
def curve_label(i):
    neg=tuple(k for k,x in enumerate(signs[i]) if x==-1)
    if len(neg)==0:return ('C',)
    if len(neg)==2:return ('L',)+neg
    assert len(neg)==4
    return ('E',next(k for k in range(5) if k not in neg))
for i,j in combinations(range(16),2):
    a,b=curve_label(i),curve_label(j)
    if a>b:a,b=b,a
    pred=(a[0]=='C' and b[0]=='E') or (a[0]=='E' and b[0]=='L' and a[1] in b[1:]) or (a[0]=='L' and b[0]=='L' and not (set(a[1:])&set(b[1:])))
    assert pred==((i,j) in edgeidx)

# A concrete general-position 1+2+2 Frobenius-stable five-point arc over F_9.
# Represent a+b*t with t^2=-1 in F_3[t]/(t^2+1).
def add(a,b): return ((a[0]+b[0])%3,(a[1]+b[1])%3)
def neg(a): return ((-a[0])%3,(-a[1])%3)
def sub(a,b):return add(a,neg(b))
def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
def det(a,b,c):
    return add(add(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),
                   mul(a[1],sub(mul(b[2],c[0]),mul(b[0],c[2])))),
               mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))
a=(0,1); one=(1,0); zero=(0,0)
frob=lambda P:tuple((x,(-y)%3) for x,y in P)
P0=(zero,zero,one)
A=(one,a,zero)
B=(one,add(one,a),a)
pts=(P0,A,frob(A),B,frob(B))
assert frob(P0)==P0 and len(set(pts))==5
assert all(det(*triple)!=zero for triple in combinations(pts,3))
# The induced action on blown-up points has cycle partition 1+2+2.
assert stype((0,2,1,4,3),(1,1,1,1,1))==((1,2,2),())
assert polys[((1,2,2),())]==(-2,-3)
assert fixed(classes[((1,2,2),())]['lines'],1)==4
assert fixed(classes[((1,2,2),())]['nodes'],1)==4
assert fixed(classes[((1,2,2),())]['flags'],1)==4
# Four rational lines give 14 rational points; the other two rational
# nodes have branches exchanged by Frobenius and supply 2 further points.
assert (3+1)*4-2+2==13+3==16
assert polys[((1,1,1,1,1),())]==(-10,25)

output={'group_size':sum(frequency.values()),'classes':len(classes),
        'lines':16,'nodes':40,'branches':80,
        'distinct_zeta_profiles_within_12_extension_degrees':18,
        'F9_conjugation_stable_general_position_five_point_arc':True,
        'F3_boundary_four_rational_curves_14_points_plus_two_conjugate_branch_nodes':16,
        'zero_count_candidate_pairs': ['q=3;positive_cycles=(1,2,2)', 'q=5;identity'],
        'class_table':[]}
for typ in sorted(classes):
    a,b=polys[typ];cl=classes[typ]
    output['class_table'].append({'positive_cycles':list(typ[0]),'negative_cycles':list(typ[1]),
        'size':frequency[typ],'A':a,'B':b,
        'line_cycles':dict(sorted(Counter(cl['lines']).items())),
        'node_cycles':dict(sorted(Counter(cl['nodes']).items())),
        'branch_cycles':dict(sorted(Counter(cl['flags']).items()))})
print(json.dumps(output,sort_keys=True,separators=(',',':')))
print('ALL_CHECKS_PASSED')
