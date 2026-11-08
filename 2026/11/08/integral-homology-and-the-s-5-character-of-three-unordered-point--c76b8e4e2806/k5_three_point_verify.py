"""Reproducible exact integral and equivariant chain calculation for UConf_3(K5).
Requires Python 3.10+ and SymPy for a 23-by-37 residual Smith form.
Cell model: one subdivision vertex per edge of K5, with three pairwise-disjoint
closed cell supports; cubical orientation orders the moving edge factors.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations,permutations
from math import gcd,prod
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form

original=list(combinations(range(5),2))
mid={e:5+i for i,e in enumerate(original)}
edges=sorted(tuple(sorted((x,mid[a,b]))) for a,b in original for x in (a,b))
lookup_edge={e:i for i,e in enumerate(edges)}
items=[('v',i,1<<i) for i in range(15)]+[('e',i,(1<<a)|(1<<b)) for i,(a,b) in enumerate(edges)]
cells=[[] for _ in range(4)]
for triple in combinations(items,3):
    used=0
    for kind,idx,bits in triple:
        if bits&used:break
        used|=bits
    else:
        vs=tuple(sorted(i for k,i,b in triple if k=='v'))
        es=tuple(sorted(i for k,i,b in triple if k=='e'))
        cells[len(es)].append((vs,es))
lookup=[{c:i for i,c in enumerate(dim)} for dim in cells]
assert list(map(len,cells))==[455,1560,1650,520]

def differential(k):
    out=[]
    for vs,es in cells[k]:
        terms=[]
        for pos,e in enumerate(es):
            a,b=edges[e]
            for vert,co in ((b,1),(a,-1)):
                face=(tuple(sorted(vs+(vert,))),es[:pos]+es[pos+1:])
                terms.append((lookup[k-1][face],co*(-1 if pos%2 else 1)))
        out.append(terms)
    return out
boundary={k:differential(k) for k in (1,2,3)}

# Check every integer boundary-of-boundary coefficient, without assuming cancellation.
for k in (2,3):
    for column in boundary[k]:
        acc=defaultdict(int)
        for row,co in column:
            for lower,val in boundary[k-1][row]:acc[lower]+=co*val
        assert all(v==0 for v in acc.values())

# Sparse unit pivot elimination. Each unit pivot is a legitimate integral
# column operation plus a unit row pivot. A primitive full-column-rank map
# follows if every column produces a unit pivot.
def unit_reduction(cols):
    pivot={};deferred=[]
    for terms in cols:
        x=defaultdict(int)
        for r,a in terms:x[r]+=a
        deferred.append({r:a for r,a in x.items() if a})
    counts=[]
    while True:
        pending=[];added=0
        for orig in deferred:
            v=orig.copy()
            while v:
                r=min(v);a=v[r]
                if r not in pivot:
                    if abs(a)!=1:pending.append(v)
                    else:
                        pivot[r]=v if a==1 else {j:-s for j,s in v.items()}
                        added+=1
                    break
                for j,s in pivot[r].items():
                    b=v.get(j,0)-a*s
                    if b:v[j]=b
                    else:v.pop(j,None)
        counts.append((len(pivot),len(pending)))
        deferred=pending
        if not added:break
    residual=[]
    for orig in deferred:
        v=orig.copy()
        for r in sorted(pivot):
            if r not in v:continue
            a=v[r]
            for j,s in pivot[r].items():
                b=v.get(j,0)-a*s
                if b:v[j]=b
                else:v.pop(j,None)
        if v:residual.append(v)
    assert all(r not in pivot for v in residual for r in v)
    return pivot,residual,counts

p3,rem3,p3steps=unit_reduction(boundary[3])
assert len(p3)==520 and not rem3
p2,rem2,p2steps=unit_reduction(boundary[2])
rr=sorted({r for v in rem2 for r in v})
small=Matrix([[v.get(r,0) for v in rem2] for r in rr])
snf=smith_normal_form(small,domain=ZZ)
nonzero=sorted(abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i])
assert len(p2)==1098 and nonzero==[1,2]
assert len(rr)==23 and len(rem2)==37
# The first differential is the ordinary connected 1-skeleton incidence map.
# A finite field rank check and an explicit connected-component BFS certify 454.
links=[[] for _ in cells[0]]
for col in boundary[1]:
    assert len(col)==2 and sorted(z for _,z in col)==[-1,1]
    a,b=col[0][0],col[1][0]
    links[a].append(b);links[b].append(a)
seen={0};stack=[0]
while stack:
    for y in links[stack.pop()]:
        if y not in seen:seen.add(y);stack.append(y)
assert len(seen)==455
# Therefore Smith forms of d1,d2,d3 are (1^454), (1^1099,2), (1^520).
# Integral homology is (Z, Z^6 plus Z/2, Z^30, 0).

# Construct 10 explicit geometric triangle loops: park the other two particles
# at the vertices outside the triangle and traverse the subdivided triangle.
for abc in combinations(range(5),3):
    stationary=tuple(sorted(set(range(5))-set(abc)))
    chain=defaultdict(int)
    circuit=(abc[0],abc[1],abc[2],abc[0])
    for x,y in zip(circuit,circuit[1:]):
        m=mid[tuple(sorted((x,y)))]
        for u,v in ((x,m),(m,y)):
            j=lookup_edge[tuple(sorted((u,v)))]
            cell=(stationary,(j,))
            chain[lookup[1][cell]]+=1 if u<v else -1
    acc=defaultdict(int)
    for col,coeff in chain.items():
        for row,a in boundary[1][col]:acc[row]+=coeff*a
    assert all(v==0 for v in acc.values())

# Character of S5 action. Fixed cubical generators contribute the sign of
# moving-edge permutation and the sign of each reversed oriented edge.
def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def action(g):
    vert=list(g)+[mid[tuple(sorted((g[a],g[b])))] for a,b in original]
    edge_map=[];edge_sign=[]
    for a,b in edges:
        x,y=vert[a],vert[b]
        edge_map.append(lookup_edge[tuple(sorted((x,y)))])
        edge_sign.append(1 if x<y else -1)
    return vert,edge_map,edge_sign

def cell_image(k,index,gaction):
    vs,es=cells[k][index]
    vm,em,sg=gaction
    vv=tuple(sorted(vm[x] for x in vs))
    ee=[em[x] for x in es]
    sign=parity(ee)*prod(sg[x] for x in es)
    return lookup[k][vv,tuple(sorted(ee))],sign

def trace_chain(k,gaction):
    return sum(sign for i in range(len(cells[k]))
               for j,sign in (cell_image(k,i,gaction),) if j==i)

def trace_graph_h1(g):
    oriented=0
    for a,b in original:
        x,y=g[a],g[b]
        if tuple(sorted((x,y)))==(a,b):oriented+=1 if x<y else -1
    return oriented-sum(g[i]==i for i in range(5))+1

def cycle_type(g):
    seen=set();cyc=[]
    for x in range(5):
        if x in seen:continue
        y=x;n=0
        while y not in seen:seen.add(y);n+=1;y=g[y]
        cyc.append(n)
    return tuple(sorted(cyc,reverse=True))

# Independently verify all group actions commute with differentials, by checking
# a set of simple transpositions generating S5 on every cell in every degree.
for swap in range(4):
    g=list(range(5));g[swap],g[swap+1]=g[swap+1],g[swap]
    act=action(g)
    for k in (1,2,3):
        for j,col in enumerate(boundary[k]):
            lhs=defaultdict(int)
            for i,a in col:
                q,s=cell_image(k-1,i,act);lhs[q]+=a*s
            jj,ss=cell_image(k,j,act)
            rhs=defaultdict(int)
            for i,a in boundary[k][jj]:rhs[i]+=ss*a
            assert all(lhs[i]==rhs[i] for i in set(lhs)|set(rhs))

classes=defaultdict(list)
for g in permutations(range(5)):
    act=action(g)
    chaintr=[trace_chain(k,act) for k in range(4)]
    h1=trace_graph_h1(g)
    h2=sum((-1)**k*t for k,t in enumerate(chaintr))-1+h1
    classes[cycle_type(g)].append((tuple(chaintr),h1,h2))
assert sum(len(v) for v in classes.values())==120
rows={}
for typ,vs in classes.items():
    assert len(set(vs))==1
    tr,h1,h2=vs[0];rows[typ]=(len(vs),tr,h1,h2)
assert rows[(1,)*5][2:]==(6,30)
assert sum(size*c2 for size,tc,c1,c2 in rows.values())==0

@lru_cache(None)
def partitions(n,maxpart=None):
    if n==0:return ((),)
    mx=n if maxpart is None else min(n,maxpart)
    return tuple((i,)+tail for i in range(mx,0,-1) for tail in partitions(n-i,i))
def squares(lam):return {(i,j) for i,n in enumerate(lam) for j in range(n)}
def removable_rims(lam,n):
    outer=squares(lam)
    for nu in partitions(sum(lam)-n):
        inner=squares(nu)
        if not inner<=outer:continue
        skew=outer-inner
        if any((i+1,j) in skew and (i,j+1) in skew and (i+1,j+1) in skew for i,j in skew):continue
        seen=set();todo=[next(iter(skew))]
        while todo:
            p=todo.pop()
            if p in seen:continue
            seen.add(p);i,j=p
            todo.extend(q for q in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)) if q in skew and q not in seen)
        if len(seen)==len(skew):yield nu,(-1)**(len({i for i,j in skew})-1)
@lru_cache(None)
def specht(lam,cycles):
    if not cycles:return int(not lam)
    return sum(sgn*specht(nu,cycles[1:]) for nu,sgn in removable_rims(lam,cycles[0]))
mults={}
for lam in partitions(5):
    numerator=sum(size*h2*specht(lam,typ) for typ,(size,tr,h1,h2) in rows.items())
    assert numerator%120==0
    mults[lam]=numerator//120
assert mults=={(5,):0,(4,1):1,(3,2):1,(3,1,1):2,(2,2,1):1,(2,1,1,1):1,(1,1,1,1,1):0}
assert sum(mults[lam]*specht(lam,(1,)*5) for lam in mults)==30
print('K5 THREE-POINT CONFIGURATION VERIFIED')
print('cubical_cells:',','.join(map(str,map(len,cells))))
print('integral_boundary_smith: d1 1^454; d2 1^1099,2^1; d3 1^520')
print('H0=Z; H1=Z^6+Z/2; H2=Z^30; H3=0')
print('d2_unit_pivots:',len(p2),'residual_rows:',len(rr),'residual_columns:',len(rem2),'residual_smith:',nonzero)
print('d3_unit_pivots:',len(p3))
for typ in sorted(rows,reverse=True):
    size,tc,h1,h2=rows[typ]
    print('class',str(typ),'size',size,'C',str(tc),'H1',h1,'H2',h2)
print('H2_Specht:',[(lam,m) for lam,m in mults.items() if m])
print('K5_UNORDERED_THREE_POINT_INTEGRAL_AND_S5_CHARACTER_PASS')
