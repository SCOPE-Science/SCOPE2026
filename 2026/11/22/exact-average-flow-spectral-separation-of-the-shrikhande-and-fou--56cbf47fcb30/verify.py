"""Exact subset-dynamic-programming certificate for two 16-vertex graphs."""
from fractions import Fraction

N = 16
V = [(a,b) for a in range(4) for b in range(4)]
GENERATORS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
EXPECTED = {
 'rook': (6,30,138,612,2556,9792,34452,110016,313344,779904,1648656,2828880,3672000,3191616,1399680),
 'shrikhande': (6,30,138,612,2556,9792,34320,109680,314064,785424,1661712,2844336,3682176,3195072,1389408),
}
TOTAL = {'rook':13991682, 'shrikhande':14029326}
WEIGHTED = {'rook':177310488, 'shrikhande':177724236}

def build(name):
    adj = [0] * N
    for i,(a,b) in enumerate(V):
        for j,(c,d) in enumerate(V):
            if i==j:continue
            has = ((a==c or b==d) if name=='rook' else ((c-a)%4,(d-b)%4) in GENERATORS)
            if has: adj[i]|=1<<j
    return adj

def check_parameters(adj, name):
    assert all(mask.bit_count()==6 for mask in adj)
    for i in range(N):
        for j in range(i+1,N):
            assert (adj[i]&adj[j]).bit_count()==2
            assert bool(adj[i]>>j&1)==bool(adj[j]>>i&1)
    near=[j for j in range(N) if (adj[0]>>j)&1]
    local_degrees=[(adj[j] & sum(1<<h for h in near)).bit_count() for j in near]
    assert sorted(local_degrees)==[2]*6
    # two triangles / one 6-cycle distinguished by triangle counts
    triangles = sum(1 for j in near for k in near for h in near if j<k<h and (adj[j]>>k)&1 and (adj[j]>>h)&1 and (adj[k]>>h)&1)
    assert triangles == (2 if name=='rook' else 0)

def paths_from_zero(adj):
    # State (visited subset, last vertex), exact integer recurrence.
    states={(1,0): 1}
    res=[]
    for length in range(1,N):
        nxt={}
        for (mask,u),ways in states.items():
            available=adj[u] & ~mask
            while available:
                bit=available & -available;available-=bit
                v=bit.bit_length()-1
                key=(mask|bit,v)
                nxt[key]=nxt.get(key,0)+ways
        res.append(sum(nxt.values()))
        states=nxt
    return tuple(res)

results={}
for name in EXPECTED:
    a=build(name)
    check_parameters(a,name)
    paths=paths_from_zero(a)
    assert paths==EXPECTED[name], (name,paths)
    P=sum(paths)
    W=sum(k*t for k,t in enumerate(paths,start=1))
    assert (P,W)==(TOTAL[name], WEIGHTED[name])
    results[name]=Fraction(W,P)
    print(name, 'P=',P, 'W=',W,'flow=',results[name], 'path_histogram=',','.join(map(str,paths)))
assert EXPECTED['rook'][:6]==EXPECTED['shrikhande'][:6]
assert EXPECTED['rook'][6]!=EXPECTED['shrikhande'][6]
assert results['rook']-results['shrikhande']==Fraction(24601265726,5452607446287)
print('SHRIKHANDE_ROOK_EXACT_AVERAGE_FLOW_SEPARATION_PASS')
