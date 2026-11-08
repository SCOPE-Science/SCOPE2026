#!/usr/bin/env python3
"""Finite exact regression for the two-, three-, and four-cycle classification.
The unrestricted theorem is proved symbolically in RESULT.md, not by this scan."""

def largest_prime_factors(N):
    out = [0]*(N+1)
    for p in range(2, N+1):
        if out[p] == 0:
            for j in range(p, N+1, p):
                out[j] = p
    return out

def canonical(seq):
    j=seq.index(min(seq))
    return tuple(seq[j:]+seq[:j])

def true_cycles_from_starts(k, lp, max_prime):
    done=set(); cycles=set()
    for p in range(2,max_prime+1):
        if lp[p] != p: continue
        x=p; pos={}; seq=[]
        while x not in pos and x not in done:
            assert 2 <= x < len(lp), (k,p,x)
            pos[x]=len(seq);seq.append(x)
            x = x+k if lp[x]==x else lp[x]
        if x in pos:
            cycles.add(canonical(seq[pos[x]:]))
        done.update(seq)
    return cycles

def predicted_short(k, lp):
    ans=set()
    for p in range(2,k+1):
        if lp[p] == p and k%p==0 and lp[1+k//p] <= p:
            ans.add(canonical([p,p+k]))
    a=1
    while (1<<a)-1 <= k:
        if k == (1<<a)-1 and lp[(1<<a)+1] == (1<<a)+1:
            ans.add(canonical([2,(1<<a)+1,1<<(a+1)]))
        a+=1
    b=1
    while 3**b-1 <= k:
        if 3**b-1 == k and lp[3**b+2]==3**b+2 and lp[2*3**b+1]==2*3**b+1:
            ans.add(canonical([3,3**b+2,2*3**b+1,3**(b+1)]))
        b+=1
    ps=[p for p in range(2,k+3) if lp[p]==p]
    for p in ps:
        for q in ps:
            if p==q: continue
            t=1
            while True:
                kk=t*p*q-p-q
                if kk>k:break
                if kk==k and t*p-1>1 and t*q-1>1:
                    if lp[t*p-1] <= q and lp[t*q-1] <= p:
                        ans.add(canonical([p,p+k,q,q+k]))
                t+=1
    return ans

LIMIT=160
lp=largest_prime_factors(80000)
short_counts={2:0,3:0,4:0}
for k in range(1,LIMIT+1):
    # Finite regression over a large explicit set of prime starts, not a global bound.
    observed=true_cycles_from_starts(k,lp,max(200,k*k//2+2))
    actual={c for c in observed if len(c)<=4}
    predicted=predicted_short(k,lp)
    assert all(len(c)>1 for c in observed), ('fixed',k)
    assert actual==predicted, (k, 'missing',sorted(actual-predicted), 'unexpected',sorted(predicted-actual))
    for c in actual:short_counts[len(c)]+=1
assert short_counts[3]==3
assert canonical([2,3,4]) in predicted_short(1,lp)
assert canonical([3,5,7,9]) in predicted_short(2,lp)
assert canonical([3,11,19,27]) in predicted_short(8,lp)
assert canonical([3,83,163,243]) in predicted_short(80,lp)
print('VERIFY_OK k=1..160 prime_starts>=200 (even k: >= k*k/2+2)')
print('observed primitive short cycles:',short_counts)
print('period-3 parameters <= 160: [1, 3, 15]')
print('exceptional three-prime period-4 parameters <= 160: [2, 8, 80]')
for k in [7,22,23,53,80]:
    print('k=',k,'short cycles=',sorted(predicted_short(k,lp)))
