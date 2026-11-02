"""Signed integral cubical computation for ordered two-point configurations of K5.
Run: python3 check_k5.py (standard library)."""
from itertools import permutations, combinations
from collections import defaultdict
V=tuple(range(5)); E=tuple(combinations(V,2))
C0=tuple((a,b) for a in V for b in V if a!=b)
C1=tuple((e,v) for e in E for v in V if v not in e)+tuple((v,e) for e in E for v in V if v not in e)
C2=tuple((e,f) for e in E for f in E if not set(e)&set(f))
I0={c:i for i,c in enumerate(C0)};I1={c:i for i,c in enumerate(C1)};I2={c:i for i,c in enumerate(C2)}
assert (len(C0),len(C1),len(C2))==(20,60,30), (len(C0),len(C1),len(C2))
D1=[{} for _ in C1];D2=[{} for _ in C2]
for k,(x,y) in enumerate(C1):
    if isinstance(x,tuple): a,b=x;D1[k]={I0[(b,y)]:1,I0[(a,y)]:-1}
    else:a,b=y;D1[k]={I0[(x,b)]:1,I0[(x,a)]:-1}
for k,(e,f) in enumerate(C2):
    a,b=e;c,d=f
    D2[k]={I1[(b,f)]:1,I1[(a,f)]:-1,I1[(e,d)]:-1,I1[(e,c)]:1}
for t in D2:
    accum=defaultdict(int)
    for u,v in t.items():
        for w,s in D1[u].items():accum[w]+=v*s
    assert all(i==0 for i in accum.values())
incidence=defaultdict(list)
for j,bdry in enumerate(D2):
    for e,sign in bdry.items():incidence[e].append((j,sign))
assert all(len(incidence[e])==2 for e in range(len(C1)))
# Orient the connected closed surface by propagation over squares.
z={0:1};stack=[0]
while stack:
    a=stack.pop()
    for e,ea in D2[a].items():
        jx=incidence[e]
        (j,ej)=jx[0] if jx[1][0]==a else jx[1]
        needed=-z[a]*ea*ej
        if j in z:assert z[j]==needed
        else:z[j]=needed;stack.append(j)
assert len(z)==len(C2)
# Check each vertex link is a circular path.
for k,cell in enumerate(C0):
    edges=[i for i,d in enumerate(D1) if k in d]
    link=defaultdict(list)
    for square in D2:
        en=[i for i in edges if i in square]
        if en:
            assert len(en)==2
            a,b=en;link[a].append(b);link[b].append(a)
    assert len(link)==len(edges) and all(len(v)==2 for v in link.values())
    seen={edges[0]}; st=[edges[0]]
    while st:
        for u in link[st.pop()]:
            if u not in seen:seen.add(u);st.append(u)
    assert len(seen)==len(edges)
# 1-skeleton connected
adj=defaultdict(set)
for edge in D1:
    u,v=edge;adj[u].add(v);adj[v].add(u)
seen={0};st=[0]
while st:
    for u in adj[st.pop()]:
        if u not in seen:seen.add(u);st.append(u)
assert len(seen)==len(C0)
assert len(C0)-len(C1)+len(C2)==-10 # genus 6

def mapped_edge(e,g):
    a,b=g[e[0]],g[e[1]]
    return tuple(sorted((a,b))), 1 if a<b else -1

def mapped_cell(c,g,swap):
    mapped=[];sign=1
    for x in c:
        if isinstance(x,tuple):e,s=mapped_edge(x,g);mapped.append(e);sign*=s
        else:mapped.append(g[x])
    if swap:
        if all(isinstance(x,tuple) for x in mapped):sign=-sign
        mapped.reverse()
    return tuple(mapped),sign

def sign_perm(p):return (-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))

def graph_trace(g):
    return sum(sign for e in E for f,sign in [mapped_edge(e,g)] if f==e)-sum(g[v]==v for v in V)+1
checks=0;orient_set=set();bad=[]
for g in permutations(V):
  for swap in (False,True):
    transported=[0]*len(C2)
    for c,k in I2.items():
        mapped,s=mapped_cell(c,g,swap)
        transported[I2[mapped]]+=s*z[k]
    assert transported==[z[i]*transported[0]//z[0] for i in range(len(C2))]
    character=transported[0]//z[0]
    assert character in (-1,1)
    orient_set.add((sign_perm(g),swap,character))
    lef=sum((1,-1,1)[j]*sum(s for c in C for c2,s in [mapped_cell(c,g,swap)] if c==c2) for j,C in enumerate((C0,C1,C2)))
    h1=0 if swap else 2*graph_trace(g)
    assert lef==1-h1+character
    checks+=1
print('cells',len(C0),len(C1),len(C2),'chi',len(C0)-len(C1)+len(C2),'genus',6)
print('orientation character (permutation parity, particle swap, H2 scalar):',sorted(orient_set))
print('PASS surface links, cycle sign, Lefschetz over',checks,'symmetries')
# Quotient of the genus-six orientable surface by the even subgroup A5.
# The nonidentity even conjugacy classes: 15 involutions of type (ab)(cd),
# 20 elements of order 3, and 24 elements of order 5.
for g,needed in [( (1,0,3,2,4),6 ),((1,2,0,3,4),2),((1,2,3,4,0),0)]:
    assert sign_perm(g)==1
    # Isolated fixed points of an orientation-preserving periodic surface map
    # each have local Lefschetz index +1.
    Lef=2-2*graph_trace(g)
    assert Lef==needed,(g,Lef)
# Each branch-point stabilizer is cyclic and hence has order 2 or 3.
# The involution fixed-point incidences: 15*6 =90 -> 90/30 =3 orbits.
# The order-three incidences: 20*2 =40, each fixed point counted twice:
# 20 points -> 20/20 =1 orbit. Hurwitz gives quotient genus zero.
branch2=(15*6)//(60//2)
branch3=(20*2//2)//(60//3)
assert (branch2,branch3)==(3,1)
from fractions import Fraction
assert Fraction(-10)==60*(2-(branch2*Fraction(1,2)+branch3*Fraction(2,3)))
print('PASS A5 quotient signature: genus zero, cone orders (2,2,2,3)')
