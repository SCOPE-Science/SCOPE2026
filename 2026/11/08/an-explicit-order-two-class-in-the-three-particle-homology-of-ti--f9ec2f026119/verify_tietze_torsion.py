#!/usr/bin/env python3
"""Exact integer/finite-field witness for order-two graph-braid H_2 torsion."""
from itertools import combinations, product
from collections import defaultdict
import json
import hashlib

EDGES = ((0,1),(0,10),(0,11),(1,2),(1,6),(2,3),(2,7),
         (3,4),(3,8),(4,9),(4,10),(5,7),(5,8),(5,11),
         (6,8),(6,9),(7,9),(10,11))
N=12

def make_complex():
    inc=[[] for _ in range(N)]
    for i,(a,b) in enumerate(EDGES):
        inc[a].append(i);inc[b].append(i)
    assert all(len(a)==3 for a in inc)
    # basis tuples: (ordered distinct degree-one vertices, half-edge difference
    # indexes at those vertices, ordered polynomial edge factors).
    def basis(d):
        return [(vs,ks,tuple(es))
                for vs in combinations(range(N),d)
                for ks in product(*(range(1,len(inc[v])) for v in vs))
                for es in combinations_with_repetition_of_edges(3-d)]
    def combinations_with_repetition_of_edges(d):
        from itertools import combinations_with_replacement
        return combinations_with_replacement(range(len(EDGES)),d)
    B={d:basis(d) for d in (1,2,3)}
    ix={d:{b:i for i,b in enumerate(B[d])} for d in (1,2)}
    def diff(d,source):
        vs,ks,ps=source;terms=defaultdict(int)
        for j,v in enumerate(vs):
            for e,c in ((inc[v][ks[j]],1),(inc[v][0],-1)):
                k=(vs[:j]+vs[j+1:],ks[:j]+ks[j+1:],tuple(sorted(ps+(e,))))
                terms[ix[d-1][k]] += (1 if j%2==0 else -1)*c
        return [(j,x) for j,x in sorted(terms.items()) if x]
    D3=[diff(3,b) for b in B[3]]
    D2=[diff(2,b) for b in B[2]]
    assert (len(B[3]),len(B[2]),len(B[1]))==(1760,4752,4104)
    return B,D3,D2

def mod2_relation(columns):
    piv={};deps=[]
    for i,col in enumerate(columns):
        x=0
        for r,c in col: x ^= 1<<r
        z=1<<i
        while x:
            b=x.bit_length()-1
            if b not in piv:
                piv[b]=(x,z)
                break
            xx,zz=piv[b];x^=xx;z^=zz
        if not x: deps.append([j for j in range(len(columns)) if (z>>j)&1])
    assert len(piv)==1759 and len(deps)==1
    return deps[0]

def rank_prime(columns,prime):
    # Sparse exact Gaussian elimination, processing descending pivot rows.
    piv={}
    for col in columns:
        x=defaultdict(int)
        for i,v in col:x[i]=(x[i]+v)%prime
        x={i:v for i,v in x.items() if v}
        while x:
            b=max(x)
            if b not in piv:
                inv=pow(x[b],-1,prime)
                piv[b]={i:v*inv%prime for i,v in x.items()}
                break
            c=x[b]
            for i,v in piv[b].items():
                z=(x.get(i,0)-c*v)%prime
                if z: x[i]=z
                else: x.pop(i,None)
    return len(piv)

def main():
    B,D3,D2=make_complex()
    support=mod2_relation(D3)
    assert len(support)==224
    d3c=defaultdict(int)
    for k in support:
        for i,v in D3[k]: d3c[i]+=v
    assert all(v%2==0 and abs(v)<=2 for v in d3c.values())
    w={i:v//2 for i,v in d3c.items() if v}
    assert len(w)==360 and set(w.values())=={-1,1}
    boundary=defaultdict(int)
    for j,c in w.items():
        for i,v in D2[j]:boundary[i]+=c*v
    assert not any(boundary.values())
    ranks={p:rank_prime(D3,p) for p in (3,5,101)}
    assert ranks=={3:1760,5:1760,101:1760}
    # Also validate d^2=0 on every top generator, not just witness.
    for col in D3:
        comp=defaultdict(int)
        for j,c in col:
            for i,v in D2[j]:comp[i]+=c*v
        assert not any(comp.values())
    digest=hashlib.sha256(','.join(map(str,support)).encode()).hexdigest()
    print('Tietze vertices=12 edges=18 cubic=yes Petersen vertex replaced by triangle')
    print('Reduced Swiatkowski weight=3 degree-3 basis=1760 degree-2 basis=4752 degree-1 basis=4104')
    print('top differential GF(2) rank=1759 kernel_dim=1')
    print('top differential full rank GF(3),GF(5),GF(101):',ranks)
    print('support of integral 3-chain c (0/1 coefficients)=',len(support))
    print('D3(c)=2*w, w support=',len(w),'coefficients=',sorted(set(w.values())))
    print('D2(w)=0; D2*D3=0 verified on all 1760 columns')
    print('c support sha256=',digest)
    print('Since D3 injective over Q and c is odd, w cannot be an integral boundary; 2[w]=0.')
    print('TIETZE_3PARTICLE_ORDER_TWO_TORSION_PASS')
    return {'edges':EDGES,'relation_columns':support,'w_rows':sorted(w.items()),'counts':{'C3':1760,'C2':4752,'C1':4104},'modular_ranks':{'2':1759,'3':1760,'5':1760,'101':1760}}

if __name__=='__main__':
    data=main()
    with open('tietze_certificate.json','w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,separators=(',',':'))
        f.write('\n')
