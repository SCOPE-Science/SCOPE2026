#!/usr/bin/env python3
"""Reproduce a ternary commuting-idempotent count using two independent methods.
Only Python standard library is required.
"""
from itertools import permutations
from collections import Counter, defaultdict

PAIRS=((0,1),(0,2),(1,2))
Q=((2,3,3,0),(1,2,0,2),(1,2,2,0),(1,1,0,2))

def step(state, color):
    out=[]
    for k,(i,j) in enumerate(PAIRS):
        a=(color>>i)&1; b=(color>>j)&1
        if a and b: x=0
        elif a:
            if state[k]==2: return None
            x=1
        elif b:
            if state[k]==1: return None
            x=2
        else: x=state[k]
        out.append(x)
    return tuple(out)

def states_and_edges():
    states={(0,0,0)}; todo=[(0,0,0)]; edges={}
    while todo:
        s=todo.pop()
        edges[s]=tuple(t for color in range(8) if (t:=step(s,color)) is not None)
        for t in edges[s]:
            if t not in states: states.add(t);todo.append(t)
    return states,edges

def orbit(state,perm):
    out=[]
    for a,b in PAIRS:
        x,y=perm[a],perm[b]
        if x<y: out.append(state[PAIRS.index((x,y))])
        else: out.append((0,2,1)[state[PAIRS.index((y,x))]])
    return tuple(out)

def transfer_counts(max_n):
    states,edges=states_and_edges()
    assert len(states)==13
    orbits=[]; unseen=set(states)
    for s in sorted(states):
        if s not in unseen: continue
        group=set(orbit(s,p) for p in permutations(range(3)))
        assert group<=states
        unseen-=group;orbits.append(group)
    assert len(orbits)==4
    by_state={s:i for i,o in enumerate(orbits) for s in o}
    matrix=[[0]*4 for _ in range(4)]
    for i,o in enumerate(orbits):
        for t in edges[min(o)]: matrix[i][by_state[t]]+=1
        for s in o:
            row=[0]*4
            for t in edges[s]:row[by_state[t]]+=1
            assert row==matrix[i]
    assert tuple(map(tuple,matrix))==Q
    zero=by_state[(0,0,0)]
    counts=[];v=[0]*4;v[zero]=1
    for _ in range(max_n):
        counts.append(sum(v))
        v=[sum(v[i]*Q[i][j] for i in range(4)) for j in range(4)]
    return counts

def polysum(a,b):
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def polydiff(a,b):return polysum(a,[-c for c in b])
def polystep(a):return [0]+list(a)
def polyscale(a,k):return [k*x for x in a]

def check_rational_identity():
    # Certificate: (I-tQ)v=D 1, where v_0 is the claimed numerator.
    D=[1,-8,16,-12,2]
    v=[[1,0,-2,2],[1,-3,2],[1,-3,4,-2],[1,-4,5,-2]]
    for i in range(4):
        result=list(v[i])
        for j in range(4):
            result=polydiff(result,polyscale(polystep(v[j]),Q[i][j]))
        assert result+ [0]*(5-len(result))==D

def projections(n):
    maps=[]
    for bits in range(1<<(n-1)):
        fixed={0}|{i for i in range(1,n) if (bits>>(i-1))&1}
        maps.append(tuple(max(j for j in fixed if j<=i) for i in range(n)))
    return maps

def directly_count(n):
    maps=projections(n)
    def commutes(f,g):
        return all(f[g[i]]==g[f[i]] for i in range(n))
    size=len(maps)
    # For each ordered center f, count ordered pairs of neighbors (g,h) that commute.
    adj=[set(j for j in range(size) if commutes(f,maps[j])) for f in maps]
    return sum(len(adj[i] & adj[j]) for i in range(size) for j in adj[i])

def weighted_transfer(n):
    # Exponents of (x,y,z,u) record the three ranks minus one
    # and the product rank minus one; the starting fixed point 1 is omitted.
    by_state={(0,0,0):{(0,0,0,0):1}}
    for _ in range(n-1):
        next_state=defaultdict(lambda: defaultdict(int))
        for s,profiles in by_state.items():
            for color in range(8):
                target=step(s,color)
                if target is None: continue
                inc=tuple((color>>i)&1 for i in range(3))+(int(color==7),)
                for k,count in profiles.items():
                    next_state[target][tuple(k[i]+inc[i] for i in range(4))]+=count
        by_state=next_state
    out=Counter()
    for profiles in by_state.values():out.update(profiles)
    return out

def direct_rank_profile(n):
    maps=projections(n)
    def commutes(f,g):
        return all(f[g[i]]==g[f[i]] for i in range(n))
    adj=[set(j for j in range(len(maps)) if commutes(f,maps[j])) for f in maps]
    out=Counter()
    for i in range(len(maps)):
        for j in adj[i]:
            for k in adj[i] & adj[j]:
                out[(i.bit_count(),j.bit_count(),k.bit_count(),(i&j&k).bit_count())]+=1
    return out

def product_rank_polynomials(max_n):
    # Coefficients of (1-2t^2+2t^3) /
    # (1-(7+u)t+16t^2-(14-2u)t^3+(4-2u)t^4).
    def add(a,b,scale=1):
        out=Counter(a)
        for j,c in b.items():out[j]+=scale*c
        return +out  # negative coefficients could occur during intermediate stages
    def multlinear(a,constant,coefficient):
        out=defaultdict(int)
        for j,c in a.items():out[j]+=constant*c;out[j+1]+=coefficient*c
        return out
    nums=(1,0,-2,2)
    fs=[]
    for m in range(max_n):
        out=defaultdict(int);out[0]=nums[m] if m<4 else 0
        def plus(source,constant,coefficient):
            for j,c in source.items():
                out[j]+=constant*c;out[j+1]+=coefficient*c
        if m>=1:plus(fs[m-1],7,1)
        if m>=2:plus(fs[m-2],-16,0)
        if m>=3:plus(fs[m-3],14,-2)
        if m>=4:plus(fs[m-4],-4,2)
        assert all(c>=0 for c in out.values())
        fs.append({j:c for j,c in out.items() if c})
    return fs

def main():
    transfer=transfer_counts(12)
    assert transfer[:8]==[1,8,46,254,1390,7592,41452,226316]
    check_rational_identity()
    for n in range(1,9):
        actual=directly_count(n)
        assert actual==transfer[n-1], (n,actual,transfer[n-1])
    for n in range(1,7):
        poly=weighted_transfer(n)
        brute=direct_rank_profile(n)
        assert poly==brute, (n,poly-brute,brute-poly)
        assert sum(poly.values())==transfer[n-1]
    bivar=product_rank_polynomials(8)
    for n in range(1,9):
        by_product=Counter()
        for ex,c in weighted_transfer(n).items():by_product[ex[-1]]+=c
        assert dict(by_product)==bivar[n-1],(n,by_product,bivar[n-1])
    assert bivar[4]=={0:445,1:676,2:240,3:28,4:1}
    for k in range(4,len(transfer)):
        assert transfer[k]==8*transfer[k-1]-16*transfer[k-2]+12*transfer[k-3]-2*transfer[k-4]
    print('CATALAN_TRIPLE_COMMUTANTS_OK',transfer[:8])

if __name__=='__main__':main()
