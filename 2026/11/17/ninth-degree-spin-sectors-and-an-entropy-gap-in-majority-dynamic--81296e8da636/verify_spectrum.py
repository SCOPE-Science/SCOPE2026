"""Exact transfer, spin-complement, and Perron checks for GP(n,2).
Usage: python verify_spectrum.py. Requires sympy (not a solver service).
"""
import sympy as S


def transfer(step):
    states = 4**(2*step)
    edges = [[] for _ in range(states)]
    for u in range(states):
        word = [(u >> (2*j)) & 3 for j in range(2*step)]
        for new in range(4):
            window = word+[new]
            center = step
            outer = lambda z: z >> 1
            inner = lambda z: z & 1
            m = window[center]
            outer_same = (int(outer(window[center-1])==outer(m))+
                          int(outer(window[center+1])==outer(m))+
                          int(inner(m)==outer(m)))
            inner_same = (int(inner(window[center-step])==inner(m))+
                          int(inner(window[center+step])==inner(m))+
                          int(outer(m)==inner(m)))
            if outer_same >= 2 and inner_same >= 2:
                v = sum(z << (2*j) for j,z in enumerate(word[1:]+[new]))
                edges[u].append(v)
    return edges


def components(edges):
    index = 0; stack = []; on = set(); ind = {}; low = {}; result = []
    def visit(v):
        nonlocal index
        ind[v] = low[v] = index; index += 1
        stack.append(v); on.add(v)
        for w in edges[v]:
            if w not in ind:
                visit(w); low[v] = min(low[v],low[w])
            elif w in on:low[v] = min(low[v],ind[w])
        if low[v] == ind[v]:
            c=[]
            while True:
                w=stack.pop();on.remove(w);c.append(w)
                if w==v:break
            result.append(sorted(c))
    for v in range(len(edges)):
        if v not in ind:visit(v)
    return sorted(result,key=lambda x:-len(x))


def matrix(edges,verts):
    pos={u:i for i,u in enumerate(verts)}
    B = S.zeros(len(verts))
    for i,u in enumerate(verts):
        for v in edges[u]:
            if v in pos:B[i,pos[v]]+=1
    return B


def traces(edges,nmax):
    values=[]
    for n in range(1,nmax+1):
        trace=0
        for first in range(len(edges)):
            dist={first:1}
            for _ in range(n):
                nxt={}
                for u,c in dist.items():
                    for v in edges[u]:nxt[v]=nxt.get(v,0)+c
                dist=nxt
            trace+=dist.get(first,0)
        values.append(trace)
    return values

E=transfer(2)
assert len(E)==256 and sum(map(len,E))==320
SCC=components(E)
assert len(SCC[0])==24
loops=[c[0] for c in SCC if len(c)==1 and c[0] in E[c[0]]]
assert len(loops)==2 and len(SCC)==233
V=SCC[0];B=matrix(E,V)
flip=lambda x: sum((3-((x>>(2*j))&3))<<(2*j) for j in range(4))
assert all(flip(x) in V and x!=flip(x) for x in V)
R=[x for x in V if x<flip(x)]
assert len(R)==12
Mplus=S.Matrix([[int(y in E[x])+int(flip(y) in E[x]) for y in R] for x in R])
Mminus=S.Matrix([[int(y in E[x])-int(flip(y) in E[x]) for y in R] for x in R])
x=S.Symbol('x')
Pplus=x**9-x**8-x**7-x**4+2*x**3+1
Pminus=x**9-x**8-x**7+2*x**6-x**4-1
assert S.expand(Mplus.charpoly(x).as_expr()-x**3*Pplus)==0
assert S.expand(Mminus.charpoly(x).as_expr()-x**3*Pminus)==0
assert S.expand(B.charpoly(x).as_expr()-x**6*Pplus*Pminus)==0

# Exact Collatz-Wielandt inequalities; no floating-point arithmetic.
v=[1]*len(V);p={y:j for j,y in enumerate(V)}
rows=[[p[y] for y in E[x] if y in p] for x in V]
for _ in range(60):v=[sum(v[j] for j in row) for row in rows]
w=[sum(v[j] for j in row) for row in rows]
assert min(100000*w[i]-156485*v[i] for i in range(24))>0
assert min(156486*v[i]-100000*w[i] for i in range(24))>0

E1=transfer(1)
assert len(E1)==16
P1=x**10*(x-1)**2*(x*x-x-1)*(x*x-x+1)
assert S.expand(matrix(E1,list(range(16))).charpoly(x).as_expr()-P1)==0
for n,g in enumerate(traces(E,15),start=1):
    if n>=5:print('GP2 n',n,'fixed',g)
for n,g in enumerate(traces(E1,15),start=1):
    if n>=5:print('PRISM n',n,'fixed',g)
print('spin polynomials:',str(Pplus),';',str(Pminus))
print('component vertices',len(V),'nonzero loops',len(loops),'edge count',sum(map(len,E)))
print('CERTIFICATE PASS: 156485/100000 < Perron root < 156486/100000')
print('EXACT SYMBOLIC AND TRANSFER CHECKS PASS')
