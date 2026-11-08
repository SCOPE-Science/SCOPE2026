#!/usr/bin/env python3
"""Integral chain certificate for unordered three-point configurations of GP(8,3).
Usage: python verify.py certificate.json
Only the standard library is required.
"""
import collections, itertools, json, math, sys, hashlib

N=16

def graph_edges():
    # Generalized Petersen GP(8,3), u_i=i, v_i=8+i.
    es = set()
    for i in range(8):
        for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
            es.add(tuple(sorted((a,b))))
    es=sorted(es)
    assert len(es)==24
    return es

def complex_bases(es):
    incidence=[[] for _ in range(N)]
    for e,(a,b) in enumerate(es):
        incidence[a].append(e);incidence[b].append(e)
    assert all(len(ls)==3 for ls in incidence)
    E=len(es)
    basis=[]
    for d in range(4):
        gens=[]
        for vs in itertools.combinations(range(N),d):
            for choices in itertools.product((0,1),repeat=d):
                halfedges=tuple(zip(vs,choices))
                for mon in itertools.combinations_with_replacement(range(E),3-d):
                    gens.append((halfedges,mon))
        basis.append(gens)
    assert list(map(len,basis))==[2600,9600,11520,4480]
    return basis,incidence

def boundary_matrix(source,target,inc):
    dest={a:i for i,a in enumerate(target)}
    cols=[]
    for halves,mon in source:
        out=collections.defaultdict(int)
        for pos,(v,choice) in enumerate(halves):
            remaining=halves[:pos]+halves[pos+1:]
            for edge,sign in ((inc[v][choice],(-1)**pos),(inc[v][2],-(-1)**pos)):
                key=(remaining,tuple(sorted(mon+(edge,))))
                out[dest[key]]+=sign
        cols.append({i:z for i,z in out.items() if z})
    return cols

def boundary(cols,chain):
    result=collections.defaultdict(int)
    for j,coef in chain.items():
        for i,v in cols[j].items():result[i]+=coef*v
    return {i:v for i,v in result.items() if v}

def elimination_rank(cols,prime,return_null=False):
    pivots={};null=[]
    for j,col in enumerate(cols):
        rem={i:v%prime for i,v in col.items() if v%prime}
        vector=(1<<j) if return_null else 0
        while rem:
            i=min(rem)
            if i not in pivots:
                pivots[i]=(rem,vector)
                break
            other,other_vector=pivots[i]
            fac=rem[i]*pow(other[i],-1,prime)%prime
            for k,z in other.items():
                val=(rem.get(k,0)-fac*z)%prime
                if val:rem[k]=val
                else:rem.pop(k,None)
            if return_null:
                assert prime==2
                vector ^= other_vector
        else:
            if return_null:null.append(vector)
    return len(pivots),null

def gf2_vector_rank(vectors):
    pivots={}
    for vec in vectors:
        while vec:
            bit=(vec&-vec).bit_length()-1
            if bit not in pivots:pivots[bit]=vec;break
            vec ^= pivots[bit]
    return len(pivots)

def verify(path):
    with open(path,encoding='utf-8') as f: certificate=json.load(f)
    assert certificate['construction']=='GP(8,3): integral reduced Swiatkowski, 3 particles'
    es=graph_edges();basis,inc=complex_bases(es)
    d3=boundary_matrix(basis[3],basis[2],inc)
    d2=boundary_matrix(basis[2],basis[1],inc)
    assert all(not boundary(d2,col) for col in d3)
    k={int(j):int(v) for j,v in certificate['kernel_chain']}
    assert all(0<=j<4480 and v for j,v in k.items())
    assert math.gcd(*(abs(v) for v in k.values()))==1
    assert boundary(d3,k)=={}
    r2,null=elimination_rank(d3,2,True)
    r3,_=elimination_rank(d3,3)
    r5,_=elimination_rank(d3,5)
    assert (r2,r3,r5)==(4475,4479,4479)
    assert len(null)==5 and gf2_vector_rank(null)==5
    k_mod2=sum(1<<j for j,v in k.items() if v%2)
    assert k_mod2 and gf2_vector_rank(null+[k_mod2])==5
    cs=[{int(j):1 for j in inds} for inds in certificate['mod2_kernel_chains']]
    assert len(cs)==4
    assert gf2_vector_rank([k_mod2]+[sum(1<<j for j in c) for c in cs])==5
    weights=[]
    for c in cs:
        assert all(0<=j<4480 for j in c)
        b=boundary(d3,c)
        assert b and all(v%2==0 for v in b.values())
        w={j:v//2 for j,v in b.items()}
        assert boundary(d2,w)=={}
        assert boundary(d3,c)=={j:2*v for j,v in w.items()}
        weights.append((len(c),len(w),max(abs(v) for v in w.values())))
    print('GRAPH: 16 vertices, 24 edges, GP(8,3)')
    print('REDUCED COMPLEX WEIGHT 3: ranks C0,C1,C2,C3 = 2600,9600,11520,4480')
    print('CHAIN TEST: D2*D3 = 0 for all 4480 degree-three generators')
    print('RANKS: D3 mod 2 = 4475, mod 3 = 4479, mod 5 = 4479')
    print('KERNEL: primitive integral k, D3*k=0, support',len(k))
    print('ORDER TWO WITNESSES: independent modulo integral kernel')
    for j,(size,ws,mx) in enumerate(weights):
        print(f'  c{j+1}: {size} terms; w{j+1}=D3*c{j+1}/2: {ws} terms; max coefficient {mx}; D2*w{j+1}=0')
    print('PROVED: H3 = Z; H2[2] = (Z/2)^4')
    print('MOBIUS_KANTOR_THREE_PARTICLE_TORSION_PASS')

if __name__=='__main__':
    assert len(sys.argv)==2, 'usage: python verify.py certificate.json'
    verify(sys.argv[1])
