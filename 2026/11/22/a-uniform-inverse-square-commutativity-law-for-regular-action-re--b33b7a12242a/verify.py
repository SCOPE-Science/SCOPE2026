"""Self-contained finite checks of commutation in restriction monoids.
Uses explicit partial-map composition and an independent subset-constraint test.
"""
from itertools import permutations

def cyclic_table(n):
    return [[(i+j)%n for j in range(n)] for i in range(n)]

def symmetric_three_table():
    elems=list(permutations(range(3)))
    index={p:i for i,p in enumerate(elems)}
    return [[index[tuple(a[b[x]] for x in range(3))] for b in elems] for a in elems]

def d4_table():
    # (rotation, reflection); (a,b)*(c,d)=(a+(-1)^b*c, b+d)
    return [[(a+(-1)**b*c)%4+4*((b+d)%2) for c,d in [(j%4,j//4) for j in range(8)]] for a,b in [(i%4,i//4) for i in range(8)]]

def maps_of_group(T):
    n=len(T)
    result=[(-1,)*n] # zero, represented by all undefined (-1)
    for g in range(n):
        for mask in range(1,1<<n):
            result.append(tuple(T[g][i] if (mask>>i)&1 else -1 for i in range(n)))
    assert len(result)==n*((1<<n)-1)+1
    assert len(set(result))==len(result)
    return result

def compose(f,g):
    return tuple(-1 if g[x]<0 else f[g[x]] for x in range(len(f)))

def brute_commuting(T):
    arr=maps_of_group(T)
    return sum(compose(a,b)==compose(b,a) for a in arr for b in arr)

def subsets_commuting(T):
    n=len(T)
    identity=next(i for i in range(n) if all(T[i][j]==j and T[j][i]==j for j in range(n)))
    fixed=0; others=[]
    for g in range(n):
        for h in range(n):
            count=0
            for A in range(1<<n):
                for B in range(1<<n):
                    d1={x for x in range(n) if (B>>x)&1 and (A>>T[h][x])&1}
                    d2={x for x in range(n) if (A>>x)&1 and (B>>T[g][x])&1}
                    if d1==d2 and all(T[g][T[h][x]]==T[h][T[g][x]] for x in d1):
                        count+=1
            if g==identity and h==identity:
                assert count==4**n
                fixed=count
            else:
                others.append(count)
    total=fixed+sum(others)-2*n*(n-1)*(2**n)+(n-1)**2
    return total, max(others,default=0), others

def bound(n):
    # For every nonidentity label pair, the shift with nontrivial action has
    # disjoint matching edges of total cardinality at least n//3.
    return (4**n)*(7/8)**(n/3)

def run():
    cases=[('C1',cyclic_table(1)),('C2',cyclic_table(2)),('C3',cyclic_table(3)),('C4',cyclic_table(4)),('S3',symmetric_three_table()),('D4',d4_table())]
    for label,T in cases:
        n=len(T)
        brute=brute_commuting(T)
        raw,max_other,others=subsets_commuting(T)
        assert brute==raw,(label,brute,raw)
        assert all(x<=bound(n)+1e-7 for x in others),(label,max_other,bound(n))
        ident_fraction=4**n/brute
        print(label,'order',n,'monoid_order',len(maps_of_group(T)),'commuting_pairs',brute,'identity_pair_share',round(ident_fraction,6),'largest_raw_other',max_other)
    # Independently check disjoint-edge (matching) bound on cycles.
    for L in range(2,64):
        assert (L//2)>=L/3
    print('VERIFY_OK')
if __name__=='__main__':run()
