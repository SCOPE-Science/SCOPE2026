"""Exact integral verification of the Segre-cubic node-plane graph and its Frobenius coinvariants.
Python 3.10+, SymPy >= 1.12.  Run: python verify_segre_graph.py
"""
from itertools import combinations, permutations
from collections import Counter
from math import prod
from sympy import Matrix, zeros, symbols, factor
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

E=tuple(range(6))
NODES=[]
for triple in combinations(E,3):
    comp=tuple(x for x in E if x not in triple)
    if triple<comp:NODES.append((triple,comp))
def matchings(vertices):
    if not vertices:
        yield ()
        return
    a=vertices[0]
    for b in vertices[1:]:
        rest=[x for x in vertices if x!=a and x!=b]
        for m in matchings(rest):yield ((a,b),)+m
PLANES=list(matchings(list(E)))
assert len(NODES)==10 and len(PLANES)==15
I=Matrix(10,15,lambda i,j:int(all((a in NODES[i][0])!=(b in NODES[i][0]) for a,b in PLANES[j])))
assert [sum(I.row(i)) for i in range(10)]==[6]*10
assert [sum(I.col(j)) for j in range(15)]==[4]*15
assert I*I.T==4*Matrix.eye(10)+2*Matrix.ones(10,10)
L=zeros(25,25)
for i in range(10):
    L[i,i]=6
    for j in range(15):
        if I[i,j]:L[i,10+j]=L[10+j,i]=-1
for j in range(15):L[10+j,10+j]=4
assert all(sum(L.row(i))==0 for i in range(25))
T=symbols('T')
assert factor(L.charpoly(T).as_expr())==T*(T-10)*(T-4)**5*(T*T-10*T+20)**9

EXPECTED={
(1,1,1,1,1,1):{2:6,10:2,20:1,40:1,80:4},
(2,1,1,1,1):{2:5,10:2,20:1,80:2},
(2,2,1,1):{2:4,20:1,40:1,80:2},
(2,2,2):{2:4,20:1,40:1,80:3},
(3,1,1,1):{2:4,20:1,40:1},
(3,2,1):{2:3,20:1},
(3,3):{4:1,8:1,80:2},
(4,1,1):{2:3,4:1,80:1},
(4,2):{2:3,20:1,80:1},
(5,1):{20:1,40:1},
(6,):{4:1,8:1,80:1}
}

def action(p):
    q=[]
    for a,b in NODES:
        aa=tuple(sorted(p[x] for x in a));bb=tuple(sorted(p[x] for x in b))
        q.append(NODES.index(tuple(sorted((aa,bb)))))
    for m in PLANES:
        mm=tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in m))
        q.append(10+PLANES.index(mm))
    return q

# This also independently checks the full S6 action on the geometric incidence matrix.
for p in permutations(E):
    q=action(p)
    assert sorted(q)==list(range(25))
    for i in range(10):
        for j in range(15):assert I[i,j]==I[q[i],q[10+j]-10]

def cycle_perm(part):
    p=list(E); k=0
    for length in part:
        for i in range(length):p[k+i]=k+(i+1)%length
        k+=length
    return p

def smith_coinv(part,root):
    q=action(cycle_perm(part))
    other=[i for i in range(25) if i!=root]
    # Degree-zero divisor group has basis e_v-e_root for v != root.
    R=L.extract(other, list(range(25)))
    C=Matrix(24,24,lambda r,c:int(q[other[c]]==other[r])-int(q[root]==other[r])-int(r==c))
    diag=smith_normal_form(R.row_join(C),domain=ZZ)
    vals=[abs(int(diag[i,i])) for i in range(24)]
    assert 0 not in vals
    assert vals==sorted(vals) and all(vals[i+1]%vals[i]==0 for i in range(23))
    return {k:v for k,v in sorted(Counter(vals).items()) if k>1}

# Independent distinguished roots give equivalent integral presentations.
for part,expected in EXPECTED.items():
    for root in (0,7,24):
        found=smith_coinv(part,root)
        assert found==expected,(part,root,found)
    print('cycle_type',part,'nonunit_Smith',expected)

D=smith_normal_form(L[:24,:24],domain=ZZ)
svals=[abs(int(D[i,i])) for i in range(24)]
assert {k:v for k,v in Counter(svals).items() if k>1}==EXPECTED[(1,1,1,1,1,1)]
assert abs(int(L[:24,:24].det()))==2**29*5**8
assert prod(svals)==2**29*5**8
print('SEGRE_GRAPH_FROBENIUS_INTEGRAL_VERIFIED_OK')
