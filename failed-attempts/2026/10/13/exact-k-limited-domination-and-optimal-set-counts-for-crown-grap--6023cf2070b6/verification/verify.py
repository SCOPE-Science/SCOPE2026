from itertools import combinations
from math import comb


def predicted(n,k):
    if k >= n-1:
        return 2, n
    q=n-k; r=q-1
    if r>=2 and 2*r<=n:
        return 2*r, comb(n,r)*comb(n-r,r)
    return 2*q, comb(n,q)**2


def legal_profile(n,k,s,t,x):
    # For n>=3 any dominating set meeting both shores must have at least two
    # selected vertices on each shore; a one-vertex shore leaves its matched mate undominated.
    if s<2 or t<2: return False
    # x = |S cap T|.  A selected vertex whose mate is selected sees n-t outside
    # on the opposite shore; otherwise it sees n-t-1.  Symmetrically for B.
    if s:
        if x>0 and n-t>k: return False
        if s-x>0 and n-t-1>k: return False
    if t:
        if x>0 and n-s>k: return False
        if t-x>0 and n-s-1>k: return False
    return True


def exact_by_profiles(n,k):
    if k>=n-1:
        # ordinary domination: precisely the n deleted matching pairs are minimum
        return 2,n
    best=10**9; count=0
    for s in range(n+1):
        for t in range(n+1):
            for x in range(max(0,s+t-n),min(s,t)+1):
                if not legal_profile(n,k,s,t,x): continue
                z=s+t
                ways=comb(n,x)*comb(n-x,s-x)*comb(n-s,t-x)
                if z<best: best=z; count=ways
                elif z==best: count+=ways
    return best,count


def legal_sets(n,k,S,T):
    for i in range(n):
        if i not in S and not any(j!=i for j in T): return False
        if i not in T and not any(j!=i for j in S): return False
    for i in S:
        if sum(j not in T and j!=i for j in range(n))>k: return False
    for i in T:
        if sum(j not in S and j!=i for j in range(n))>k: return False
    return True


def brute(n,k):
    best=2*n+1; count=0
    for sm in range(1<<n):
        S={i for i in range(n) if sm>>i&1}
        for tm in range(1<<n):
            T={i for i in range(n) if tm>>i&1}
            z=len(S)+len(T)
            if z>best: continue
            if legal_sets(n,k,S,T):
                if z<best: best=z; count=1
                elif z==best: count+=1
    return best,count


def main():
    profile_cases=0
    for n in range(3,51):
        for k in range(1,n):
            got=exact_by_profiles(n,k); want=predicted(n,k)
            assert got==want,(n,k,got,want)
            profile_cases+=1
    brute_cases=0; subset_pairs=0; table=[]
    for n in range(3,7):
        for k in range(1,n):
            got=brute(n,k); want=predicted(n,k)
            assert got==want,(n,k,got,want)
            brute_cases+=1; subset_pairs+=4**n; table.append((n,k,*got))
    print('ALL CHECKS PASSED')
    print(f'profile_parameter_cases={profile_cases}; profile_range=3<=n<=50')
    print(f'brute_parameter_cases={brute_cases}; brute_subset_pairs={subset_pairs}; brute_range=3<=n<=6')
    print('table='+repr(table))
if __name__=='__main__': main()
