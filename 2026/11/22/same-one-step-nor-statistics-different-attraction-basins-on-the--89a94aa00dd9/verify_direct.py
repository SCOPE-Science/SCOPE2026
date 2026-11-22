"""Independent complete-state enumeration of NOR dynamics on two 16-vertex graphs.
Run: python3 verify_direct.py
"""
from collections import Counter
from itertools import product

N = 16
DOMAIN = 1 << N
EXPECT = {
    'rook': {
        'fixed': 24, 'two': 315,
        'basin': {(1, 5):24,(2, 2):160,(2, 10):18,(2, 20):120,(2, 549):16,(2, 53732):1},
        'fixed_supports':{4:24}
    },
    'shrikhande': {
        'fixed': 48, 'two': 303,
        'basin': {(1, 1):32,(1, 5):16,(2, 2):144,(2, 10):22,(2, 20):120,(2, 549):16,(2, 53732):1},
        'fixed_supports':{3:32,4:16}
    }
}

def neighborhoods(name):
    out = []
    for x,y in product(range(4),repeat=2):
        row=0
        for u,v in product(range(4),repeat=2):
            if name == 'rook':
                adj = ((x == u) or (y == v)) and (x,y)!=(u,v)
            else:
                adj = ((u-x)%4,(v-y)%4) in ((1,0),(3,0),(0,1),(0,3),(1,1),(3,3))
            if adj: row |= 1 << (4*u+v)
        out.append(row)
    assert all(a.bit_count() == 6 for a in out)
    assert all((out[i]>>j&1)==(out[j]>>i&1) for i in range(N) for j in range(N))
    return out

def run(name):
    adj = neighborhoods(name)
    transition = []
    for s in range(DOMAIN):
        nxt=0
        for i in range(N):
            if not (adj[i]&s): nxt |= 1<<i
        transition.append(nxt)
    assert all(transition[transition[transition[s]]]==transition[s] for s in range(DOMAIN))
    predecessor_count = Counter(transition)
    image = set(transition)
    bivar = Counter((s.bit_count(),transition[s].bit_count()) for s in range(DOMAIN))
    fixed = [s for s in image if transition[s]==s]
    assert Counter(s.bit_count() for s in fixed) == EXPECT[name]['fixed_supports']
    used=set(); basin = Counter(); two = 0
    for state in sorted(image):
        if state in used: continue
        partner=transition[state]
        assert partner in image and transition[partner]==state
        pair = {state,partner}
        assert not (used & pair)
        used.update(pair)
        length=len(pair)
        basin[(length,sum(predecessor_count[v] for v in pair))]+=1
        two += length==2
    assert used==image
    assert len(fixed)==EXPECT[name]['fixed']
    assert two==EXPECT[name]['two']
    assert basin==EXPECT[name]['basin']
    assert sum(c*size for (length,size),c in basin.items())==DOMAIN
    assert len(image)==654
    assert len(predecessor_count)==654
    print(name, 'fixed',len(fixed),'two_orbits',two,'image',len(image))
    print(' basin',sorted((p,bs,c) for (p,bs),c in basin.items()))
    print(' fiber_hist',sorted(Counter(predecessor_count.values()).items()))
    return bivar, Counter(predecessor_count.values())

if __name__=='__main__':
    a,fa=run('rook')
    b,fb=run('shrikhande')
    assert a==b and fa==fb
    print('BIVARIATE_EQUALS',len(a),'nonzero coefficients')
    print('COEFFICIENTS',sorted(a.items()))
    print('ALL_CHECKS_PASSED')
