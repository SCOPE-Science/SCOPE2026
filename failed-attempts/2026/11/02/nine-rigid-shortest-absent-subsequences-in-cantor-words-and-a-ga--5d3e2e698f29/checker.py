"""Exact shortest-absent-subsequence checks for Cantor substitution iterates.

Uses independent earliest-embedding and suffix dynamic programs, not proof lemmas.
"""
from itertools import product
from random import Random

A = ('00','01','11')
B = ('00','10','11')

def predicted(m):
    return {a+'1'*(m-3)+b for a in A for b in B}

def subsequence(query, word):
    i = 0
    for ch in word:
        if i < len(query) and ch == query[i]:
            i += 1
    return i == len(query)

def sas_by_suffix_dp(word):
    n = len(word)
    nexts = [[-1,-1] for _ in range(n+1)]
    nxt = [-1,-1]
    for i in range(n-1,-1,-1):
        nxt[int(word[i])] = i + 1
        nexts[i] = nxt.copy()
    depth = [0]*(n+1)
    missing = [None]*(n+1)
    for i in range(n,-1,-1):
        choices=[]
        for bit in ('0','1'):
            j=nexts[i][int(bit)]
            if j==-1:
                choices.append((1, {bit}))
            else:
                choices.append((1+depth[j], {bit+s for s in missing[j]}))
        depth[i]=min(d for d,_ in choices)
        missing[i]=set().union(*(words for d,words in choices if d==depth[i]))
    return depth[0],missing[0]

def verify_family(word):
    m=word.count('1')
    expected=predicted(m)
    gotlen,got=sas_by_suffix_dp(word)
    assert gotlen==m+1, (m,gotlen)
    assert got==expected,(m,len(got),sorted(got^expected)[:10])
    assert len(got)==9
    assert all(not subsequence(s,word) for s in expected)


def main():
    cantor='1'
    for k in range(8):
        if k>=2:
            verify_family(cantor)
            m=2**k
            if k<=4:
                missing={''.join(s) for s in product('01',repeat=m+1)
                         if not subsequence(''.join(s),cantor)}
                assert missing==predicted(m)
            print('Cantor level',k,'length',len(cantor),'ones',m,'shortest absent',9,'PASS')
        cantor=''.join('101' if c=='1' else '000' for c in cantor)

    rng=Random(20261025)
    for r in range(2,10):
        gaps=[1 if j in (1,2*r-1) else
              (rng.randint(1,7) if j%2 else rng.randint(3,10))
              for j in range(1,2*r)]
        word='1'+''.join('0'*g+'1' for g in gaps)
        verify_family(word)
        print('Gap-inflated family',r,'ones',2*r,'length',len(word),'PASS')
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
