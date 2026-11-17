"""Exact rational consistency tests for the cactus mean-zero Sobolev formula.

Requires Python 3, networkx and sympy. Does not constitute a proof for
arbitrary graphs: the proof is given in RESULT.md.
"""
from fractions import Fraction as F
from collections import deque
import networkx as nx
import sympy as sy


def edge_key(u, v):
    return tuple(sorted((u, v)))


def build(edges):
    G = nx.Graph()
    for u, v, l in edges:
        assert u != v and l > 0 and not G.has_edge(u, v)
        G.add_edge(u, v, length=F(l))
    assert nx.is_connected(G)
    return G


def glen(G, e):
    return G.edges[e]['length']


def exterior_mass(G, removed, root):
    H = G.copy()
    H.remove_edges_from(removed)
    comp = nx.node_connected_component(H, root)
    return sum((H.edges[e]['length'] for e in H.edges if e[0] in comp and e[1] in comp), F(0))


def blocks(G):
    out=[]
    for cyc in nx.cycle_basis(G):
        n=len(cyc)
        ces=[edge_key(cyc[j],cyc[(j+1)%n]) for j in range(n)]
        assert len(ces)==len(set(ces))
        pos={cyc[0]:F(0)}
        for j in range(1,n):pos[cyc[j]]=pos[cyc[j-1]]+glen(G,ces[j-1])
        length=sum((glen(G,e) for e in ces),F(0))
        masses={v:exterior_mass(G,ces,v) for v in cyc}
        out.append(dict(kind='cycle',verts=cyc,edges=ces,L=length,pos=pos,m=masses))
    cycle_edges={e for B in out for e in B['edges']}
    for u,v,attr in G.edges(data=True):
        e=edge_key(u,v)
        if e not in cycle_edges:
            m0=exterior_mass(G,[e],u)
            m1=exterior_mass(G,[e],v)
            out.append(dict(kind='bridge',verts=[u,v],edges=[e],L=attr['length'],pos={u:F(0),v:attr['length']},m={u:m0,v:m1}))
    assert len({e for B in out for e in B['edges']})==G.number_of_edges()
    assert sum((B['L'] for B in out),F(0))==sum((a['length'] for _,_,a in G.edges(data=True)),F(0))
    return out


def rho(s,L):
    s=s%L
    return s*(L-s)/L


def local_phi(B,s):
    l=B['L']
    if B['kind']=='cycle':
        return l*l/6+sum((m*rho(s-p,l) for v,m in B['m'].items() for p in [B['pos'][v]]),F(0))
    u,v=B['verts']; return (s*s+(l-s)*(l-s))/2+B['m'][u]*s+B['m'][v]*(l-s)


def local_J(B):
    l=B['L']; m=B['m']
    if B['kind']=='bridge':
        u,v=B['verts']; return l**3/3+l*l*(m[u]+m[v])+2*m[u]*m[v]*l
    z=l**3/6+l*l*sum(m.values())/3
    vv=B['verts']
    return z+2*sum((m[vv[i]]*m[vv[j]]*rho(B['pos'][vv[i]]-B['pos'][vv[j]],l)
                     for i in range(len(vv)) for j in range(i+1,len(vv))),F(0))


def gate(G,B,v):
    if v in B['pos']:return v
    # By the cactus block tree, every path to the block has the same first entry vertex.
    candidates=[]
    for w in B['verts']:
        candidates.append((nx.shortest_path_length(G,v,w),w))
    return min(candidates)[1]


def Fvertex(G, bs,v):
    return sum((local_phi(B,B['pos'][gate(G,B,v)]) for B in bs),F(0))


def candidates(G,bs):
    out=[]
    for v in G.nodes:
        if G.degree(v)==1:out.append(('leaf',v,None,Fvertex(G,bs,v)))
    for B in bs:
        if B['kind']!='cycle':continue
        msum=sum(B['m'].values())
        if not msum:
            out.append(('pure_cycle',B['verts'][0],F(0),Fvertex(G,bs,B['verts'][0])))
            continue
        anchors=sorted((B['pos'][v] for v,m in B['m'].items() if m))
        L=B['L']; ref=B['verts'][0]; base=Fvertex(G,bs,ref)-local_phi(B,B['pos'][ref])
        for i,a in enumerate(anchors):
            b=anchors[(i+1)%len(anchors)] + (L if i+1==len(anchors) else 0)
            mid=(a+b)/2
            der=sum((w*(1-2*((mid-p)%L)/L) for v,w in B['m'].items() for p in [B['pos'][v]]),F(0))
            x=mid+der*L/(2*msum)
            if a<x<b:out.append(('cycle',ref,x%L,base+local_phi(B,x%L)))
    return out


def Fpoint(G,bs,edge,offset):
    u,v=edge
    B=next(B for B in bs if edge_key(u,v) in B['edges'])
    if offset==0:return Fvertex(G,bs,u)
    if offset==glen(G,edge):return Fvertex(G,bs,v)
    if B['kind']=='bridge':
        a=B['pos'][u];b=B['pos'][v];s=a+(b-a)*offset/glen(G,edge)
    else:
        a=B['pos'][u];L=B['L'];vv=B['verts']
        i=vv.index(u)
        if vv[(i+1)%len(vv)]==v:s=(a+offset)%L
        else:
            assert vv[(i-1)%len(vv)]==v
            s=(a-offset)%L
    return Fvertex(G,bs,u)+local_phi(B,s)-local_phi(B,B['pos'][u])


def point_at_cycle(G,B,s):
    s=s%B['L'];verts=B['verts']
    for i,u in enumerate(verts):
        v=verts[(i+1)%len(verts)];a=B['pos'][u];l=glen(G,(u,v))
        if a<=s<=a+l:
            return (u,v),s-a
    raise ValueError((B,s))


def fem_Q(G, edge, offset):
    # Separately implemented finite-element calculation of the continuous Green diagonal.
    H=G.copy()
    e=edge_key(*edge); length=glen(H,e)
    if offset==0:x=edge[0]
    elif offset==length:x=edge[1]
    else:
        x=max(H.nodes)+1
        H.remove_edge(*edge)
        H.add_edge(edge[0],x,length=offset)
        H.add_edge(x,edge[1],length=length-offset)
    vs=sorted(H.nodes); idx={v:i for i,v in enumerate(vs)}; N=len(vs)
    L=sy.zeros(N,N); mass=[F(0) for _ in vs]
    T=sum((a['length'] for _,_,a in H.edges(data=True)),F(0))
    C=sum((a['length']**3 for _,_,a in H.edges(data=True)),F(0))/(12*T*T)
    for u,v,a in H.edges(data=True):
        l=a['length'];i=idx[u];j=idx[v];w=sy.Rational(l.denominator,l.numerator)
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
        mass[i]+=l/2;mass[j]+=l/2
    f=[sy.Rational(int(v==x)) - sy.Rational(m.numerator,m.denominator)/sy.Rational(T.numerator,T.denominator) for v,m in zip(vs,mass)]
    U=L[:-1,:-1].inv()*sy.Matrix(f[:-1]);q=sum((f[i]*U[i] for i in range(N-1)),sy.Rational(0))
    return F(q)+C


def check(G,name):
    bs=blocks(G);T=sum((B['L'] for B in bs),F(0));J=sum((local_J(B) for B in bs),F(0))
    cs=candidates(G,bs);assert cs
    Fmax=max(c[-1] for c in cs);K=Fmax/T-J/(2*T*T)
    assert K>0
    count=0
    samples=[]
    for u,v,a in G.edges(data=True):
        l=a['length'];samples.extend([((u,v),l*t) for t in [F(0),F(1,4),F(1,2),F(3,4),F(1)]])
    for kind,ref,s,Fc in cs:
        if kind=='cycle':
            B=next(B for B in bs if B['kind']=='cycle' and ref==B['verts'][0] and abs(Fvertex(G,bs,ref)+local_phi(B,s)-local_phi(B,0)-Fc)==0)
            samples.append(point_at_cycle(G,B,s))
    for edge,t in samples:
        qp=Fpoint(G,bs,edge,t)/T-J/(2*T*T)
        qf=fem_Q(G,edge,t)
        assert qp==qf,(name,edge,t,qp,qf)
        assert qp<=K,(name,edge,t,qp,K)
        count+=1
    for kind,ref,s,fm in cs:
        assert fm<=Fmax
    print(name,'T=',T,'K=',K,'max=',[(c[0],c[1],c[2]) for c in cs if c[-1]==Fmax], 'FE_checks=',count)
    return count


def examples():
    yield 'single_bridge',build([(0,1,F(7,2))])
    yield 'unequal_tree',build([(0,1,F(3,2)),(1,2,F(5,4)),(1,3,F(2,1)),(3,4,F(1,2))])
    yield 'single_cycle',build([(0,1,F(2,1)),(1,2,F(3,1)),(2,0,F(5,1))])
    yield 'two_petal_rose',build([(0,1,F(1,2)),(1,2,F(1,2)),(2,0,F(1,1)),(0,3,F(1,1)),(3,4,F(1,1)),(4,0,F(1,1))])
    yield 'two_loops_bridge',build([(0,1,F(2,1)),(1,2,F(1,1)),(2,0,F(3,1)),(0,3,F(5,2)),(3,4,F(1,1)),(4,5,F(1,2)),(5,3,F(2,1))])
    yield 'three_loops_nonantipodal',build([(0,1,F(1,1)),(1,2,F(4,1)),(2,0,F(5,1)),(0,3,F(1,2)),(3,4,F(1,2)),(4,0,F(1,1)),(1,5,F(1,1)),(5,6,F(1,1)),(6,1,F(1,1))])
    yield 'mixed_cactus',build([(0,1,F(2,1)),(1,2,F(1,1)),(2,0,F(3,1)),(1,3,F(4,3)),(3,4,F(1,2)),(4,5,F(2,1)),(5,3,F(5,2)),(5,6,F(1,3)),(6,7,F(7,4))])
    yield 'three_attachments_one_cycle',build([(0,1,F(1,1)),(1,2,F(2,1)),(2,3,F(3,1)),(3,0,F(4,1)),(0,4,F(2,1)),(1,5,F(2,3)),(5,6,F(3,1)),(6,1,F(1,1)),(3,7,F(1,4)),(7,8,F(3,4)),(8,3,F(1,2))])


if __name__=='__main__':
    tot=0
    for name,g in examples():tot+=check(g,name)
    print('EXACT_INDEPENDENT_KIRCHHOFF_GREEN_COMPARISONS_PASSED',tot)
    print('ALL_CACTUS_BLOCK_ENVELOPE_CHECKS_PASSED')
