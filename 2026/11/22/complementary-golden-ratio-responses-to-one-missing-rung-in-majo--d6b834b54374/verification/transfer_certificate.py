#!/usr/bin/env python3
"""Integer-only transfer, rational-function and spectral-residue certificate.
The graphs and all polynomial coefficients are rebuilt from the local majority map.
"""
from collections import defaultdict
from fractions import Fraction


def majority(left,centre,right,missing):
    # Each two-bit argument stores the upper and lower rail, respectively.
    if missing:
        u=(left&1) if (left&1)==(right&1) else (centre&1)
        v=((left>>1)&1) if ((left>>1)&1)==((right>>1)&1) else ((centre>>1)&1)
    else:
        u=int((left&1)+(right&1)+((centre>>1)&1)>=2)
        v=int(((left>>1)&1)+((right>>1)&1)+(centre&1)>=2)
    return u+(v<<1)


def transfer(temporal,missing):
    q=1<<(2*temporal)
    g={}
    for a in range(q):
        for b in range(q):
            edges=[]
            for c in range(q):
                for t in range(temporal):
                    left=(a>>(2*t))&3
                    mid=(b>>(2*t))&3
                    right=(c>>(2*t))&3
                    next_mid=(b>>(2*((t+1)%temporal)))&3
                    if majority(left,mid,right,missing)!=next_mid: break
                else: edges.append(b*q+c)
            if edges:g[a*q+b]=edges
    return g,q*q


def recurrent_components(g):
    verts=set(g)
    for vs in g.values():verts.update(vs)
    inv=defaultdict(list)
    for v,vs in g.items():
        for w in vs:inv[w].append(v)
    used=set();order=[]
    for v in verts:
        if v in used:continue
        used.add(v);st=[(v,0)]
        while st:
            node,k=st[-1]
            if k==len(g.get(node,())):
                order.append(node);st.pop();continue
            st[-1]=(node,k+1);w=g[node][k]
            if w not in used:used.add(w);st.append((w,0))
    used=set();out=[]
    for v in reversed(order):
        if v in used:continue
        used.add(v);st=[v];comp=[]
        while st:
            x=st.pop();comp.append(x)
            for w in inv[x]:
                if w not in used:used.add(w);st.append(w)
        if len(comp)>1 or v in g.get(v,()):out.append(sorted(comp))
    return out


def add(a,b):return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):c[i+j]+=x*y
    return c


def component_det(nodes,g):
    # Newton relation d_k=-sum(d_{k-j}tr(A^j))/k, all integer arithmetic.
    nodes=set(nodes);sz=len(nodes);sums=[0]*(sz+1)
    for start in nodes:
        cur={start:1}
        for k in range(1,sz+1):
            nxt=defaultdict(int)
            for v,val in cur.items():
                for w in g.get(v,()):
                    if w in nodes:nxt[w]+=val
            cur=nxt;sums[k]+=cur.get(start,0)
    D=[1]
    for k in range(1,sz+1):
        n=-sum(D[k-j]*sums[j] for j in range(1,k+1))
        assert n%k==0
        D.append(n//k)
    return D


def defect_sequence(g,h,N,limit):
    # f_n=tr(B A^(n-1)); one B-edge and n-1 ordinary A-edges.
    seq=[0]*(limit+1)
    for v,targets in h.items():
        cur={w:1 for w in targets}
        for n in range(1,limit+1):
            seq[n]+=cur.get(v,0)
            nxt=defaultdict(int)
            for w,c in cur.items():
                for x in g.get(w,()):nxt[x]+=c
            cur=nxt
    return seq


def polynomial_mod(poly,relation):
    p=[Fraction(v) for v in poly]
    q=[Fraction(v) for v in relation]
    assert q[-1]==1
    while len(p)>len(q)-1:
        fac=p[-1]
        if fac:
            offset=len(p)-len(q)
            for i,x in enumerate(q):p[offset+i]-=fac*x
        p.pop()
    return p


def assert_residue(numer,denom,minpoly,linear):
    # Exact rational identity -N(r)/(r D'(r))=linear(r)/5.
    dprime=[i*denom[i] for i in range(1,len(denom))]
    lhs=mul([-5],numer)
    rhs=mul([0,1],mul(dprime,linear))
    diff=add(lhs,[-v for v in rhs])
    assert not any(polynomial_mod(diff,minpoly)), polynomial_mod(diff,minpoly)


def main():
    # Reduced exact denominator polynomials have constant coefficient one.
    d1=[1]
    for fac in ([1,-1],[1,-1,1],[1,-1,-1]):d1=mul(d1,fac)
    n1=mul([0,2],[2,-4,2,2,-1,-2])
    d2=[1]
    for fac in ([1,-1],[1,1],[1,-3,1],[1,-1,-1],
                [1,-1,1],[1,1,-1],[1,1,1],
                [1,-1,2,1,1],[1,1,2,-1,1]):
        d2=mul(d2,fac)
    Q=[2,2,-11,-9,17,12,-154,-16,104,190,-158,0,374,-22,29,-101,45,-28,2,-12,6]
    n2=mul([0,2],Q)
    for temporal,den,num in [(1,d1,n1),(2,d2,n2)]:
        normal,N=transfer(temporal,False)
        fault,_=transfer(temporal,True)
        cyclic=recurrent_components(normal)
        deg=sum(len(c) for c in cyclic)
        full=[1]
        for component in cyclic:full=mul(full,component_det(component,normal))
        assert len(full)==deg+1 and len(den)<=len(full)
        # Independent factor-level characteristic-polynomial certificate.
        expected=[1]
        if temporal==1:
            characteristic_factors=[([1,-1],2),([1,-1,1],1),([1,-1,-1],1)]
        else:
            characteristic_factors=[
                ([1,-1],5),([1,1],3),([1,-3,1],1),
                ([1,-1,-1],2),([1,-1,1],2),
                ([1,1,-1],2),([1,1,1],3),
                ([1,-1,2,1,1],1),([1,1,2,-1,1],1)]
        for factor,power in characteristic_factors:
            for _ in range(power):expected=mul(expected,factor)
        assert full==expected
        # Exact factor division certifies that den divides det(I-z A).
        r=list(map(Fraction,full));denfrac=list(map(Fraction,den))
        quotient=[Fraction(0)]*(len(full)-len(den)+1)
        while len(r)>=len(den):
            i=len(r)-len(den)
            fac=r[-1]/denfrac[-1]
            quotient[i]=fac
            for j,v in enumerate(denfrac):r[i+j]-=fac*v
            while r and r[-1]==0:r.pop()
        assert not any(r)
        f=defect_sequence(normal,fault,N,N)
        # det(I-z A) has degree deg; Cayley-Hamilton for A on N dimensions
        # makes det(I-z A)*sum_{n>=1}tr(B A^(n-1))z^n polynomial of degree <=N.
        # Comparing <=N coefficients therefore proves the rational identity.
        assert f[0]==0
        conv=mul(den,f)
        assert conv[:N+1]==num+[0]*(N+1-len(num)), (temporal,[(i,conv[i]) for i in range(len(conv)) if i>len(num) and conv[i]][:3])
        print('time',temporal,'vertices',N,'normal arcs',sum(map(len,normal.values())),
              'fault arcs',sum(map(len,fault.values())),
              'cyclic sizes',sorted(map(len,cyclic),reverse=True),
              'unreduced degree',deg,'reduced degree',len(den)-1)
        print('first values',f[3:13])
        if temporal==1:
            assert_residue(num,den,[-1,1,1],[3,6])
            fibonacci=[0,1]
            for _ in range(2,257):fibonacci.append(fibonacci[-1]+fibonacci[-2])
            delta=[6,5,1,-2,-1,3]
            assert all(f[n]==3*fibonacci[n]+delta[n%6] for n in range(3,N+1))
        else:
            assert_residue(num,den,[1,-3,1],[1,6])
            assert [f[n] for n in range(3,10)]==[22,32,108,316,608,1552,3838]
    print('EXACT_TRANSFER_CERTIFICATE_OK')

if __name__=='__main__':main()
