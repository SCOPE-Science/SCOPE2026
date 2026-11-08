#!/usr/bin/env python3
"""Independent finite checks of constrained binary subsequence universality."""
from itertools import product
from collections import defaultdict

def index_greedy(w):
    seen = None
    ans = 0
    for c in w:
        if seen is None:
            seen = c
        elif seen != c:
            seen = None
            ans += 1
    return ans

def is_subsequence(pattern, word):
    j = 0
    for c in word:
        if j < len(pattern) and c == pattern[j]:
            j += 1
    return j == len(pattern)

def index_direct(word):
    for k in range(len(word)//2, -1, -1):
        if all(is_subsequence(p, word) for p in product('01',repeat=k)):
            return k
    raise AssertionError('index undefined')

def coefficients(r, N):
    # Coefficients from the proposed numerator-denominator identity.
    a = defaultdict(int)
    for n in range(N+1):
        for k in range(n//2+1):
            a[n,k] = (a[n-1,k]+2*a[n-2,k-1]
                      -a[n-r-2,k-1]-a[n-r-3,k-2]
                      +(n==0 and k==0)+(n==1 and k==0)
                      -(n==r+1 and k==0)-(n==r+2 and k==1))
    return a

def valid(word,r):
    return '1'*(r+1) not in word

def transition_dp(r,N):
    # State (unfinished first-letter or None, current 1-run length, index)
    d = {(None,0,0):1}
    rows=[{0:1}]
    for n in range(1,N+1):
        nd=defaultdict(int)
        for (seen,j,k),count in d.items():
            for c in '01':
                jj = j+1 if c=='1' else 0
                if jj>r:continue
                if seen is None: sn=c; kk=k
                elif seen==c: sn=c; kk=k
                else: sn=None;kk=k+1
                nd[sn,jj,kk]+=count
        d=nd
        row=defaultdict(int)
        for (seen,j,k),count in d.items():row[k]+=count
        rows.append(dict(row))
    return rows

def main():
    checks=0
    direct_checks=0
    for r in range(1,9):
        a=coefficients(r,44)
        rows=transition_dp(r,44)
        for n in range(45):
            for k in range(n//2+1):
                assert a[n,k]==rows[n].get(k,0),(r,n,k,a[n,k],rows[n])
                checks+=1
            assert sum(rows[n].values()) == allowed_count(n,r)
        for n in range(0,13):
            brute=defaultdict(int)
            for w in product('01',repeat=n):
                if not valid(''.join(w),r):continue
                x=index_greedy(w)
                y=index_direct(w)
                assert x==y,(r,n,w,x,y)
                brute[x]+=1
                direct_checks+=1
            assert dict(brute)==rows[n],(r,n,brute,rows[n])
        for k in range(1,20):
            want=(k+1) if r==1 else (2**k)
            assert a[2*k,k]==want,(r,k,a[2*k,k],want)
    print(f'VERIFY_OK r=1..8 n=0..44 cells={checks} direct_words={direct_checks} full_alphabet=true minimal_profiles=true')

def allowed_count(n,r):
    if n==0:return 1
    # All allowed binary words by final positive run (independent from arches)
    f=[1]
    for i in range(1,n+1):
        f.append(sum(f[max(0,i-j-1)] if i-j-1>=0 else 1 for j in range(0,min(r,i)+1)))
    # This recurrence is just by initial all-ones run followed by zero
    return f[n]

if __name__=='__main__':main()
