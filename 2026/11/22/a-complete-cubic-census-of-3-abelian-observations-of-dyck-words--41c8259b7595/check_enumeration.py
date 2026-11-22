#!/usr/bin/env python3
"""Exhaustive independent enumeration of Dyck 3-Abelian profiles."""
from collections import Counter, defaultdict

TRIPLES = tuple(f"{i:03b}" for i in range(8))

def dyck_words(m):
    def walk(word, ups, downs):
        if ups == m and downs == m:
            yield word
            return
        if ups < m:
            yield from walk(word + '1', ups + 1, downs)
        if downs < ups:
            yield from walk(word + '0', ups, downs + 1)
    yield from walk('', 0, 0)

def signature(word):
    # Include EVERY contiguous factor length 1, 2 and 3, with overlaps.
    return tuple(sum(word[i:i+k] == target
                     for i in range(len(word)-k+1))
                 for k in (1, 2, 3)
                 for target in (f'{i:0{k}b}' for i in range(2**k)))

def formula(m):
    return m * (m*m - 3*m + 5) // 3

def profile_parameters(word):
    lengths=[]
    run=1
    for i in range(1,len(word)):
        if word[i]==word[i-1]:run+=1
        else:
            lengths.append(run)
            run=1
    lengths.append(run)
    a,b=lengths[::2],lengths[1::2]
    return len(a),sum(x==1 for x in a),sum(x==1 for x in b),int(a[0]==1),int(b[-1]==1)

def admissible(m,p,u,v,alpha,beta):
    if p==m:
        return u==v==p and alpha==beta==1
    if not (1<=p<m):return False
    lo=max(0,2*p-m)
    if not (lo<=u<=p-1 and lo<=v<=p-1):return False
    k=alpha+beta
    return u>=k and v>=k

def main():
    for m in range(1,12):
        profiles=defaultdict(list)
        parameters={}
        for word in dyck_words(m):
            sig=signature(word)
            par=profile_parameters(word)
            profiles[sig].append(word)
            if sig in parameters:
                assert parameters[sig]==par
            else: parameters[sig]=par
        observed=set(parameters.values())
        predicted={(p,u,v,a,b) for p in range(1,m+1)
                    for u in range(p+1) for v in range(p+1)
                    for a in range(2) for b in range(2)
                    if admissible(m,p,u,v,a,b)}
        assert observed==predicted, (m, observed^predicted)
        assert len(profiles)==formula(m), (m,len(profiles),formula(m))
        # Every signature is a full-length 1/2/3-gram spectrum.
        print(f'm={m:2d}: Dyck={sum(map(len,profiles.values())):6d}; profiles={len(profiles):4d}; singleton={sum(len(x)==1 for x in profiles.values()):3d}')
    print('PASS: exhaustive spectra and complete parameter support through semilength 11')

if __name__=='__main__':main()
