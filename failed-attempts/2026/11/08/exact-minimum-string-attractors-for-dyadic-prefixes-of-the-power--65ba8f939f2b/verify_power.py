"""Standalone independent finite tests of the exact sparse-power string-attractor theorem."""
from itertools import combinations

def word(k):
    return ''.join('1' if (i+1)&i==0 else '0' for i in range(1<<k))

def positions(k):
    S={2**j-1 for j in range(1,k,2)}
    S.add((1<<(k-1))-1)
    S.add((1<<k)-2)
    return S

def obstructions(k):
    P=['1'+'0'*((1<<j)-1)+'1' for j in range(0,k-1,2)]
    if k%2:
        P.append('0'*(1<<(k-3))+'10')
    P.append('0'*(1<<(k-2))+'1')
    return P

def occurrences(s,t):
    return [(i,i+len(t)) for i in range(len(s)-len(t)+1) if s.startswith(t,i)]

def check(k):
    s=word(k); S=positions(k); obs=obstructions(k)
    assert len(S)==len(obs)==(k+1)//2+1
    cover=[]
    for t in obs:
        occ=occurrences(s,t)
        assert occ, (k,t)
        z=set()
        for a,b in occ:z.update(range(a,b))
        cover.append(z)
    assert all(a.isdisjoint(b) for a,b in combinations(cover,2)),(k,obs)
    factors={s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)}
    for f in factors:
        assert any(any(a<=p<a+len(f) for p in S) for a,b in occurrences(s,f)),(k,f)
    return k,len(s),len(factors),len(S)

if __name__=='__main__':
    for k in range(2,9): print('PASS',check(k),flush=True)
