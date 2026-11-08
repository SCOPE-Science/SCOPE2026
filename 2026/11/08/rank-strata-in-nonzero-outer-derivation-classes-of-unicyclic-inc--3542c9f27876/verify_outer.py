#!/usr/bin/env python3
"""Reproduce the full derivation and non-inner rank distributions on small height-two incidence algebras."""
import itertools
from collections import Counter

def mul(a,b,q):
    if q!=4:return a*b%q
    y=0
    for j in range(2):
        if (b>>j)&1:y^=a<<j
    if y&8:y^=0b1100
    if y&4:y^=0b111
    return y

def add(a,b,q):return a^b if q==4 else (a+b)%q

def neg(a,q):return a if q==4 else (-a)%q

def inv(a,q):
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def matrix_rank(mat,q):
    rows=[r[:] for r in mat];r=0
    for j in range(len(rows[0])):
        k=next((k for k in range(r,len(rows)) if rows[k][j]),None)
        if k is None:continue
        rows[r],rows[k]=rows[k],rows[r]
        d=inv(rows[r][j],q)
        for h in range(j,len(rows[0])):rows[r][h]=mul(rows[r][h],d,q)
        for k in range(len(rows)):
            if k==r:continue
            d=rows[k][j]
            if d:
                for h in range(j,len(rows[0])):
                    rows[k][h]=add(rows[k][h],neg(mul(d,rows[r][h],q),q),q)
        r+=1
    return r

def derivation_matrix(n,edges,beta,z,q):
    mat=[[0]*(n+len(edges)) for _ in edges]
    for j,(u,v) in enumerate(edges):
        mat[j][u]=z[j]
        mat[j][v]=neg(z[j],q)
        mat[j][n+j]=beta[j]
    return mat

def inner_condition(n,edges,beta,q):
    # Derivation is inner iff beta is a vertex gradient; use tree propagation independently
    potentials=[None]*n
    for root in range(n):
        if potentials[root] is not None:continue
        potentials[root]=0
        todo=[root]
        for u in todo:
            for j,(a,b) in enumerate(edges):
                if u==a:
                    other=b; proposed=add(potentials[u],neg(beta[j],q),q)
                elif u==b:
                    other=a; proposed=add(potentials[u],beta[j],q)
                else:continue
                if potentials[other] is None:
                    potentials[other]=proposed;todo.append(other)
                elif potentials[other]!=proposed:return False
    return True

def polynomial(q,e,L):
    a=q*q-1
    def times(f,g):
        h=[0]*(len(f)+len(g)-1)
        for i,x in enumerate(f):
            for j,y in enumerate(g):h[i+j]+=x*y
        return h
    def pw(f,k):
        t=[1]
        for _ in range(k):t=times(t,f)
        return t
    tree=pw([1,a],e-L)
    c=pw([1,a],L)
    other=pw([1,-1],L)
    # All derivations, their non-inner subset, and inner subset.
    full=c[:]; full[L-1]+=(q-1)**L; full[L]-=(q-1)**L
    outer=[(q-1)*(c[j]-other[j])//q for j in range(L+1)]
    assert all((q-1)*(c[j]-other[j])%q==0 for j in range(L+1))
    full=times(tree,full); outer=times(tree,outer)
    per_class=[z//(q-1) for z in outer]
    assert all(z%(q-1)==0 for z in outer)
    return full,outer,per_class

def check(q,n,edges,L):
    e=len(edges);full,outer,perclass=polynomial(q,e,L)
    tally=Counter();outs=Counter();byclass={c:Counter() for c in range(1,q)}
    for x in itertools.product(range(q),repeat=2*e):
        b,z=x[:e],x[e:]
        r=matrix_rank(derivation_matrix(n,edges,b,z,q),q)
        tally[r]+=1
        if not inner_condition(n,edges,b,q):
            outs[r]+=1
            c=0
            for j in range(L):c=add(c,b[j] if j%2==0 else neg(b[j],q),q)
            assert c!=0
            byclass[c][r]+=1
    assert [tally[i] for i in range(e+1)]==full,(q,n,tally,full)
    assert [outs[i] for i in range(e+1)]==outer,(q,n,outs,outer)
    assert sum(outer)==q**(2*e)-q**(2*e-1)
    for c in range(1,q):
        assert [byclass[c][i] for i in range(e+1)]==perclass,(q,c,byclass[c],perclass)
    assert outer[0]==0 and outer[1]==q*(q-1)*L
    print('CHECK',q,n,L,'full',full,'outer',outer,'perclass',perclass)

def leibniz_sample(q,n,edges):
    e=len(edges);dim=n+e
    mult={}
    for i in range(n):mult[i,i]={i:1}
    for j,(u,v) in enumerate(edges):
        mult[u,n+j]={n+j:1}; mult[n+j,v]={n+j:1}
    def prod(a,b):return mult.get((a,b),{})
    for beta,z in [(tuple(range(e)),tuple(range(e))),((1,)*e,(1,)*e),((0,)*e,(0,)*e)]:
        beta=tuple(x%q for x in beta);z=tuple(x%q for x in z)
        D=derivation_matrix(n,edges,beta,z,q)
        for a in range(dim):
            for b in range(dim):
                lhs=[0]*e;rhs=[0]*e
                for j,v in prod(a,b).items():
                    for k in range(e):lhs[k]=add(lhs[k],mul(v,D[k][j],q),q)
                for k in range(e):
                    # D(a) b and a D(b) with output in radical
                    rhs[k]=add(rhs[k],mul(D[k][a],prod(n+k,b).get(n+k,0),q),q)
                    rhs[k]=add(rhs[k],mul(D[k][b],prod(a,n+k).get(n+k,0),q),q)
                assert lhs==rhs,(a,b,beta,z,lhs,rhs)
    print('LEIBNIZ',q,n,'PASS')

if __name__=='__main__':
    C4=[(0,1),(2,1),(2,3),(0,3)]
    C6=[(0,1),(2,1),(2,3),(4,3),(4,5),(0,5)]
    C4leaf=C4+[(0,4)]
    for q,n,edges,L in [(2,4,C4,4),(3,4,C4,4),(4,4,C4,4),(2,6,C6,6),(2,5,C4leaf,4),(3,5,C4leaf,4)]:
        leibniz_sample(q,n,edges)
        check(q,n,edges,L)
    print('VERIFY_OK')
