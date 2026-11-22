#!/usr/bin/env python3
"""Independent finite checks for colored double-star independence complexes."""
from itertools import combinations, product
from math import prod

def faces(p,q,k):
    # vertex order: all p leaves of u, all q leaves of v, hub u, hub v
    m=p+q+2
    order=[(j,c) for j in range(m) for c in range(k)]
    base_edges={(i,p+q) for i in range(p)}|{(p+j,p+q+1) for j in range(q)}|{(p+q,p+q+1)}
    bydim={-1:{()}}
    for r in range(1,m+1):
        for idxs in combinations(range(m),r):
            if any(u in idxs and v in idxs for u,v in base_edges):continue
            for cols in product(range(k),repeat=r):
                z=tuple(sorted(k*j+c for j,c in zip(idxs,cols)))
                bydim.setdefault(r-1,set()).add(z)
    return [sorted(bydim.get(j,set())) for j in range(-1,m)]

def rankmod(cols,nrows,mod):
    pivots={}; r=0
    for col in cols:
        v={i:(a%mod) for i,a in col.items() if a%mod}
        while v:
            i=min(v)
            if i not in pivots:
                inv=pow(v[i],-1,mod)
                pivots[i]={j:(x*inv)%mod for j,x in v.items() if (x*inv)%mod}
                r+=1;break
            f=v[i]
            for j,x in pivots[i].items():
                nv=(v.get(j,0)-f*x)%mod
                if nv:v[j]=nv
                else:v.pop(j,None)
    return r

def betti(faces,mod):
    # augmented boundaries C_0 -> C_-1. Complex connected => Htilde0=0.
    m=len(faces)-2
    boundaries=[]
    ranks=[]
    for d in range(m+1):
        fs=faces[d+1]; low=faces[d]
        pos={z:i for i,z in enumerate(low)}
        cols=[{pos[z[:i]+z[i+1:]]:(-1)**i for i in range(len(z))} for z in fs]
        ranks.append(rankmod(cols,len(low),mod))
    return {d:len(faces[d+1])-ranks[d]-ranks[d+1] for d in range(m) if len(faces[d+1])-ranks[d]-ranks[d+1]}

def expected(p,q,k):
    out={p+q-1:(k-1)**(p+q)}
    out[p]=out.get(p,0)+k*(k-1)**p
    out[q]=out.get(q,0)+k*(k-1)**q
    return out

def main():
    trials=[(2,2,2),(2,2,3),(2,3,2),(3,2,2),(3,3,2),(2,4,2),(2,3,3)]
    for p,q,k in trials:
        f=faces(p,q,k)
        expected_b=expected(p,q,k)
        print(f'case p={p}, q={q}, fiber={k}; cells={sum(map(len,f))} expected={expected_b}',flush=True)
        for prime in (2,101):
            got=betti(f,prime)
            assert got==expected_b,(p,q,k,prime,got,expected_b)
        print('  integral-formula Betti ranks agree over F_2 and F_101')
    print('PASS all finite homology tests')
if __name__=='__main__':main()

# permutation action check: reduced Lefschetz numbers (on augmented chains)
def simplicial_sign(image):
    return -1 if sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))%2 else 1

def lefschetz(faces,vertex_perm):
    total=-1  # degree -1 augmented chain, acted on by identity
    for d,dimfaces in enumerate(faces[1:]):
        chain_trace=0
        for face in dimfaces:
            img=[vertex_perm[v] for v in face]
            if sorted(img)==list(face):chain_trace+=simplicial_sign(img)
        total+=(-1)**d*chain_trace
    return total

def check_lefschetz():
    for p,q,k in [(2,2,2),(2,2,3),(2,3,3),(3,3,2),(2,4,2)]:
        f=faces(p,q,k)
        num=p+q+2
        def vperm(index_map,color_map=None):
            if color_map is None: color_map={}
            return [k*index_map[i]+color_map.get(i,lambda c:c)(c) for i in range(num) for c in range(k)]
        ident=list(range(num))
        top=(k-1)**(p+q)
        lower_u=k*(k-1)**q
        lower_v=k*(k-1)**p
        def expected_lef(ltop,lu,lv):
            return (-1)**(p+q-1)*ltop+(-1)**q*lu+(-1)**p*lv
        perm=vperm(ident,{p+q:lambda c:(1-c if c<=1 else c)})
        observed=lefschetz(f,perm)
        predicted=expected_lef(top,(k-2)*(k-1)**q,lower_v)
        assert observed==predicted,('center-color',p,q,k,observed,predicted)
        perm=vperm(ident,{0:lambda c:(1-c if c<=1 else c)})
        observed=lefschetz(f,perm)
        predicted=expected_lef((k-3)*(k-1)**(p+q-1),lower_u,k*(k-3)*(k-1)**(p-1))
        assert observed==predicted,('leaf-color',p,q,k,observed,predicted)
        index=ident.copy();index[0],index[1]=index[1],index[0]
        observed=lefschetz(f,vperm(index))
        predicted=expected_lef(-(k-1)**(p+q-1),lower_u,-k*(k-1)**(p-1))
        assert observed==predicted,('leaf-swap',p,q,k,observed,predicted)
        if p==q:
            index=[i+p if i<p else i-p if i<p+q else (p+q+1 if i==p+q else p+q) for i in range(num)]
            observed=lefschetz(f,vperm(index))
            predicted=expected_lef(((-1)**p)*(k-1)**p,0,0)
            assert observed==predicted,('hub-swap',p,q,k,observed,predicted)
        print(f'case p={p}, q={q}, fiber={k}; four/some Lefschetz tests agree',flush=True)
    print('PASS all signed naturality tests')
if __name__=='__main__':check_lefschetz()
