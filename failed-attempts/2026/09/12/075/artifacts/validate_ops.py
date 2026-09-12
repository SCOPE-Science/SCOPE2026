"""Validate graph-surgery ops for the domino shuffle by brute-force Z comparison."""
import itertools, math, cmath
from fractions import Fraction

class WGraph:
    def __init__(self):
        self.V = {}   # vid -> color 0/1
        self.E = {}   # (u,v) sorted tuple -> weight (number or sympy)
    def add_edge(self, u, v, w):
        assert self.V[u] != self.V[v], (u, v)
        self.E[tuple(sorted((u,v)))] = w
    def nbrs(self, v):
        out=[]
        for (a,b),w in self.E.items():
            if a==v: out.append((b,w))
            elif b==v: out.append((a,w))
        return out
    def deg(self,v): return len(self.nbrs(v))

def brute_Z(G):
    verts=list(G.V)
    adj={v:[] for v in verts}
    for (a,b),w in G.E.items():
        adj[a].append((b,w)); adj[b].append((a,w))
    used=set(); total=0.0
    def rec(cur):
        nonlocal total
        rem=[v for v in verts if v not in used]
        if not rem: total+=cur; return
        v=rem[0]; used.add(v)
        for (u,w) in adj[v]:
            if u not in used:
                used.add(u); rec(cur*w); used.discard(u)
        used.discard(v)
    rec(1.0)
    return total

def build_aztec_cj(n, a, b):
    """CJ coords. Edge weight = face-uniform value; verify each edge in exactly one face."""
    G=WGraph()
    W=[(i,j) for i in range(1,2*n,2) for j in range(0,2*n+1,2)]
    B=[(i,j) for i in range(0,2*n+1,2) for j in range(1,2*n,2)]
    for w in W: G.V[('W',w)]=0
    for bb in B: G.V[('B',bb)]=1
    edge_face={}
    for i in range(n):
        for j in range(n):
            w = a if (i+j)%2==0 else b
            vB1=('B',(2*i,2*j+1)); vB2=('B',(2*i+2,2*j+1))
            vW1=('W',(2*i+1,2*j)); vW2=('W',(2*i+1,2*j+2))
            for e in [(vB1,vW1),(vB1,vW2),(vB2,vW1),(vB2,vW2)]:
                key=tuple(sorted(e))
                assert key not in edge_face, f"edge in two faces: {key}"
                edge_face[key]=(i,j)
            G.add_edge(vB1,vW1,w); G.add_edge(vB1,vW2,w)
            G.add_edge(vB2,vW1,w); G.add_edge(vB2,vW2,w)
    return G

for n in [1,2,3]:
    G=build_aztec_cj(n,0.7,1.0)
    print(f"n={n} V={len(G.V)} E={len(G.E)} 4n^2={4*n*n} Z={brute_Z(G):.10f}")

def spider(G, corners, inner_shift=2):
    """corners=(v0,v1,v2,v3) cyclic B,W,B,W with edges e_i=(v_i,v_{i+1}).
    Replace by legs (v_i,u_i,wt1) + inner square (u_i,u_{i+1}) wt W_i.
    Convention: W_i = w_{i+2}/Delta (opposite edge)."""
    v0,v1,v2,v3=corners
    ws=[]
    for (x,y) in [(v0,v1),(v1,v2),(v2,v3),(v3,v0)]:
        ws.append(G.E.pop(tuple(sorted((x,y)))))
    Delta=ws[0]*ws[2]+ws[1]*ws[3]
    Pts=[(f"P{k}", len(G.V)+k, id(G) % 997) for k in range(4)]
    for k,vk in enumerate(corners):
        G.V[Pts[k]]=1-G.V[vk]
    for k,vk in enumerate(corners):
        G.add_edge(vk,Pts[k],1.0)
    W=[ws[(k+inner_shift)%4]/Delta for k in range(4)]
    for k in range(4):
        G.add_edge(Pts[k],Pts[(k+1)%4],W[k])
    return Delta

# Test spider Z-preservation on Aztec_2 with external edges present (spider at one face only)
import copy
G=build_aztec_cj(2,0.7,1.3)
z0=brute_Z(G)
corners=[('B',(0,1)),('W',(1,0)),('B',(2,1)),('W',(1,2))]
D=spider(G,corners)
z1=brute_Z(G)
print(f"spider test: Z_before={z0:.10f} Delta*Z_after={D*z1:.10f} match={abs(z0-D*z1)<1e-9}")
