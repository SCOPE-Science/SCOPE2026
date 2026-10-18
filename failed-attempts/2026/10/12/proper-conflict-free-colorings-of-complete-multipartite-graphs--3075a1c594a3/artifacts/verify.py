from itertools import product
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def S2(n,k):
    if n == 0 and k == 0:
        return 1
    if n < 0 or k < 0 or k > n or k == 0:
        return 0
    return k*S2(n-1,k) + S2(n-1,k-1)

def falling(n,j):
    out = 1
    for a in range(j):
        out *= n-a
    return out

def A(n,c):
    return factorial(c)*S2(n,c) if 1 <= c <= n else 0

def H(n,c):
    if not 1 <= c <= n:
        return 0
    return sum(
        (-1)**(j+1) * comb(c,j) * falling(n,j) * factorial(c-j) * S2(n-j,c-j)
        for j in range(1,c+1)
    )

def U(n,c):
    return A(n,c)-H(n,c)

def comps(q,caps):
    ans=[]
    def rec(i,left,cur):
        if i == len(caps):
            if left == 0:
                ans.append(tuple(cur))
            return
        high=min(caps[i], left-(len(caps)-i-1))
        for c in range(1,high+1):
            cur.append(c)
            rec(i+1,left-c,cur)
            cur.pop()
    rec(0,q,[])
    return ans

def formula_count(profile,q):
    total=0
    for cs in comps(q,profile):
        all_count=1
        zero_witness=1
        for n,c in zip(profile,cs):
            all_count *= A(n,c)
            zero_witness *= U(n,c)
        one_witness=0
        for j,(n,c) in enumerate(zip(profile,cs)):
            term=H(n,c)
            for i,(nn,cc) in enumerate(zip(profile,cs)):
                if i != j:
                    term *= U(nn,cc)
            one_witness += term
        good = all_count-zero_witness-one_witness
        alloc=factorial(q)
        for c in cs:
            alloc //= factorial(c)
        total += alloc*good
    return total

def graph(profile):
    parts=[]
    part_of={}
    start=0
    for i,n in enumerate(profile):
        p=list(range(start,start+n))
        parts.append(p)
        for v in p:
            part_of[v]=i
        start += n
    N=start
    adj=[[False]*N for _ in range(N)]
    for u in range(N):
        for v in range(N):
            adj[u][v] = part_of[u] != part_of[v]
    return parts,part_of,adj

def direct(profile,coloring):
    parts,part_of,adj=graph(profile)
    N=len(coloring)
    for u in range(N):
        for v in range(u+1,N):
            if adj[u][v] and coloring[u] == coloring[v]:
                return False
    for v in range(N):
        counts={}
        for u in range(N):
            if adj[v][u]:
                counts[coloring[u]] = counts.get(coloring[u],0)+1
        if counts and not any(x == 1 for x in counts.values()):
            return False
    return True

def structural(profile,coloring):
    parts,part_of,adj=graph(profile)
    N=len(coloring)
    for u in range(N):
        for v in range(u+1,N):
            if adj[u][v] and coloring[u] == coloring[v]:
                return False
    witnesses=0
    for p in parts:
        counts={}
        for v in p:
            counts[coloring[v]] = counts.get(coloring[v],0)+1
        if any(x == 1 for x in counts.values()):
            witnesses += 1
    return witnesses >= 2

def profiles_of(total):
    out=[]
    def rec(rem,last,cur):
        if rem == 0:
            if len(cur) >= 2:
                out.append(tuple(cur))
            return
        for x in range(last,rem+1):
            cur.append(x)
            rec(rem-x,x,cur)
            cur.pop()
    rec(total,1,[])
    return out

profiles=0
pairs=0
labeled=0
surjective=0

for N in range(2,7):
    for profile in profiles_of(N):
        profiles += 1
        r=len(profile)
        t=sum(1 for n in profile if n == 1)
        chi=r+max(0,2-t)
        spectrum=[]
        for q in range(1,N+1):
            pairs += 1
            labeled += q**N
            brute=0
            for coloring in product(range(q), repeat=N):
                if len(set(coloring)) != q:
                    continue
                surjective += 1
                d=direct(profile,coloring)
                s=structural(profile,coloring)
                if d != s:
                    raise AssertionError(("structural mismatch",profile,q,coloring,d,s))
                if d:
                    brute += 1
            exact=formula_count(profile,q)
            if brute != exact:
                raise AssertionError(("count mismatch",profile,q,brute,exact))
            if exact > 0:
                spectrum.append(q)
        if spectrum != list(range(chi,N+1)):
            raise AssertionError(("spectrum mismatch",profile,spectrum,chi,N))

print(
    "ALL CHECKS PASSED; "
    f"profiles={profiles}; "
    f"profile_color_pairs={pairs}; "
    f"labeled_colorings={labeled}; "
    f"surjective_colorings={surjective}; "
    "orders=2..6"
)
