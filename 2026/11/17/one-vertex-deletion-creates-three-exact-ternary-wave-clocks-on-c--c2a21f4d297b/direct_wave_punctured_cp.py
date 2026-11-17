"""Independent graph-local orbit enumeration for the punctured cocktail-party wave.
Execute: python direct_wave_punctured_cp.py
"""

def local_census(r):
    n=2*r+1; base=3**n; size=base*base
    vertices=tuple(range(n))
    neighbors=[tuple(j for j in vertices if j!=i and not(i<2*r and j==(i^1))) for i in vertices]
    digits=[tuple((index//(3**i))%3 for i in vertices) for index in range(base)]
    weights=[3**i for i in vertices]
    next_state=[0]*size
    for u in range(base):
        au=[sum(digits[u][j] for j in neighbors[i])%3 for i in vertices]
        for v in range(base):
            newu=sum(((au[i]-digits[v][i])%3)*weights[i] for i in vertices)
            next_state[u+base*v]=newu+base*u
    assert len(set(next_state))==size
    seen=bytearray(size); counts={}
    for index in range(size):
        if seen[index]:continue
        cur=index; orbit_len=0
        while not seen[cur]:
            seen[cur]=1;orbit_len+=1;cur=next_state[cur]
        assert cur==index
        counts[orbit_len]=counts.get(orbit_len,0)+orbit_len
    return counts
if __name__=='__main__':
    for r in (1,2):print(f'r={r} direct local populations:',dict(sorted(local_census(r).items())))
