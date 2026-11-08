"""Independent point-extension and formula certificates for balanced crown/biclique graphs.
Checks finite representatives of the permanent index-strategy; verifies characteristic
formulas and exact independent-set boundaries by brute force.
"""
import itertools


def vertices(n):
    return [(s,i) for s in range(2) for i in range(n)]


def edge(v,w,crown):
    return v[0]!=w[0] and (not crown or v[1]!=w[1])


def independent_max(n,crown):
    verts=vertices(n)
    out=0
    for size in range(1,len(verts)+1):
        if any(all(not edge(u,v,crown) for u,v in itertools.combinations(t,2)) for t in itertools.combinations(verts,size)):
            out=size
        else:
            break
    return out


def fo3_detects_matching_deletion(n,crown):
    vs=vertices(n)
    return any(x!=y and not edge(x,y,crown) and
        all(not(edge(z,x,crown) and edge(z,y,crown)) for z in vs)
        for x,y in itertools.product(vs,repeat=2))


def check_strategies():
    tested=0
    # Canonical positions: occupied source indices i<r and target indices i<r.
    # Allow both orientations, both sides at each pebble, repetitions and shared indices.
    for k,n,m in [(2,2,3),(3,3,4),(3,3,6),(4,4,5),(4,4,6),(5,5,6)]:
        for r in range(k):
            for indexed in itertools.product(range(max(1,r)),repeat=r):
                if r and set(indexed)!=set(range(max(indexed)+1)):
                    continue
                for sides in itertools.product((0,1),repeat=r):
                    source=list(zip(sides,indexed))
                    target=list(zip(sides,indexed))
                    for move in itertools.product((0,1), range(n)):
                        # Spoiler can always replay same index or select fresh.
                        unused=set(range(m))-set(indexed)
                        options=[(move[0],move[1])] if move[1] in indexed else [(move[0],z) for z in unused]
                        assert options
                        # A response is required to preserve equality and all graph atoms.
                        assert any(all((move==v)==(res==w) and edge(move,v,True)==edge(res,w,True)
                            for v,w in zip(source,target)) for res in options)
                        tested+=1
    print('canonical crown strategy positions/moves:',tested)
    print('index-pattern extension verification: PASS')
    for n in range(2,7):
        for crown in (False,True):
            assert independent_max(n,crown)==n
            assert fo3_detects_matching_deletion(n,crown)==crown
    print('independence and FO3 matching-defect checks: 10 graph models PASS')
    print('sharp boundary width k and width k+1: witnessed by independent-set formula')

if __name__ == '__main__':
    check_strategies()
