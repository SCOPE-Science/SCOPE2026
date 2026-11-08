"""Independent finite enumeration of automorphisms of abelian core quandles."""
from itertools import product,permutations
from math import factorial

def group(mod):
    return list(product(*(range(x) for x in mod)))

def op(a,b,mod):
    return tuple((2*y-x)%m for x,y,m in zip(a,b,mod))

def direct_count(mod):
    G=group(mod); n=len(G)
    assert n<=8
    ids={x:i for i,x in enumerate(G)}
    mul=[[ids[op(x,y,mod)] for y in G] for x in G]
    count=0
    for f in permutations(range(n)):
        if all(f[mul[x][y]] == mul[f[x]][f[y]] for x in range(n) for y in range(n)):
            count+=1
    return count

def automorphism_count(M):
    # Aut(2G) computed as permutations of actual group elements preserving addition, not from formula.
    G=group(M)
    H=sorted(set(tuple((2*z)%m for z,m in zip(x,M)) for x in G))
    zero=tuple(0 for _ in M); ids={x:i for i,x in enumerate(H)}
    add=lambda a,b:tuple((x+y)%m for x,y,m in zip(a,b,M))
    good=0
    for f in permutations(range(len(H))):
        if f[ids[zero]]!=ids[zero]: continue
        if all(f[ids[add(a,b)]]==ids[add(H[f[i]],H[f[j]])] for i,a in enumerate(H) for j,b in enumerate(H)):
            good+=1
    s=sum(m==2 for m in M)
    t=sum(m%2==0 and m>=4 for m in M)
    count=len(G)*good*2**(t*(2**(s+t)-1))*factorial(2**s-1)*factorial(2**s)**(2**t-1)
    return count,good,s,t


def construction_checks(M):
    G=group(M); zero=tuple(0 for _ in M)
    H=sorted(set(tuple((2*z)%m for z,m in zip(x,M)) for x in G))
    keys=sorted(set(tuple(x_i%2 if m%2==0 else 0 for x_i,m in zip(x,M)) for x in G))
    reps={c:tuple(c_i for c_i in c) for c in keys}
    elem_by_key={c:[x for x in G if tuple(x_i%2 if m%2==0 else 0 for x_i,m in zip(x,M))==c] for c in keys}
    ids={x:i for i,x in enumerate(H)}
    add=lambda a,b:tuple((x+y)%m for x,y,m in zip(a,b,M))
    sub=lambda a,b:tuple((x-y)%m for x,y,m in zip(a,b,M))
    dbl=lambda a:tuple(2*x%m for x,m in zip(a,M))
    n=0
    for gp in permutations(H):
        g=dict(zip(H,gp))
        if g[zero]!=zero or any(g[add(a,b)]!=add(g[a],g[b]) for a in H for b in H): continue
        choices={}
        for c in keys:
            choices[c]={d:[a for a in elem_by_key[d] if dbl(a)==g[dbl(reps[c])]] for d in keys}
        # Simultaneously choose all allowed distinct target cosets, fixing zero.
        for ds in permutations(keys[1:]):
            sigma=dict(zip(keys,[keys[0]]+list(ds)))
            if any(not choices[c][sigma[c]] for c in keys):continue
            candidates=[([zero] if c==keys[0] else choices[c][sigma[c]]) for c in keys]
            for arr in product(*candidates):
                a=dict(zip(keys,arr))
                # f for f(0)=0, composed with any translation of G.
                f={x:add(a[next(k for k in keys if x in elem_by_key[k])],g[sub(x,reps[next(k for k in keys if x in elem_by_key[k])])]) for x in G}
                assert len(set(f.values()))==len(G)
                assert all(f[op(x,y,M)]==op(f[x],f[y],M) for x in G for y in G)
                n+=1
    expected,_,_,_=automorphism_count(M)
    assert n*len(G)==expected,(M,n,expected)
    print(f'{M}: normalized_constructed={n} verified_all_pairs=yes total={n*len(G)}')

if __name__ == '__main__':
    cases=[(2,),(4,),(8,),(3,),(2,2),(2,4),(2,8),(4,4),(2,3),(2,2,2),(4,3),(2,4,3)]
    for M in cases:
        formula,ag,s,t=automorphism_count(M)
        if __import__('math').prod(M)<=8:
            direct=direct_count(M)
            assert direct==formula,(M,direct,formula)
            label=f'exhaustive={direct}'
        else:
            label='formula_only'
        print(f'{M}: Aut(2G)={ag} s={s} t={t} total={formula} {label}')
    assert automorphism_count((4,4))[0]==6144
    assert automorphism_count((2,4))[0]==128
    assert automorphism_count((2,8))[0]==512
    assert automorphism_count((2,4,3))[0]==768
    for M in [(2,4),(2,8),(4,4),(2,4,3)]: construction_checks(M)
    print('VERIFY_OK distinct_groups=12 exhaustive_small_cases=8 constructive_cases=4')
