import itertools, math

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x):
            yield (x,)+q

def labels(parts):
    L=[]
    for i,a in enumerate(parts): L += [i]*a
    return L

def total_dom(mask,L):
    if mask==0: return False
    n=len(L)
    for v in range(n):
        if not any((mask>>u)&1 and L[u]!=L[v] for u in range(n)):
            return False
    return True

def secure_total(mask,L):
    if not total_dom(mask,L): return False
    n=len(L)
    for v in range(n):
        if (mask>>v)&1: continue
        defended=False
        for u in range(n):
            if (mask>>u)&1 and L[u]!=L[v]:
                if total_dom((mask & ~(1<<u)) | (1<<v),L):
                    defended=True
                    break
        if not defended: return False
    return True

def profile(mask,parts):
    L=labels(parts); a=[0]*len(parts)
    for v,i in enumerate(L):
        if (mask>>v)&1: a[i]+=1
    return a

def criterion(a,parts):
    sup=[i for i,x in enumerate(a) if x]
    if len(sup)>=3: return True
    if len(sup)!=2: return False
    i,j=sup
    return (a[i]==parts[i] or a[j]>=2) and (a[j]==parts[j] or a[i]>=2)

def formula(parts):
    N=sum(parts); c=[0]*(N+1)
    for counts in itertools.product(*[range(n+1) for n in parts]):
        if criterion(counts,parts):
            ways=1
            for n,a in zip(parts,counts): ways*=math.comb(n,a)
            c[sum(counts)] += ways
    return c

def min_formula(parts):
    r=len(parts); N=sum(parts)
    s=sum(n==1 for n in parts)
    t=sum(n==2 for n in parts)
    if r>=3:
        if s>=2:
            return 2, math.comb(s,2)
        e3=sum(parts[i]*parts[j]*parts[k]
               for i in range(r) for j in range(i+1,r) for k in range(j+1,r))
        return 3, e3+t*(N-2)
    a,b=parts
    if a==b==1: return 2,1
    if a==1 or b==1: return N,1
    if a==2 or b==2: return 3,t*(N-2)
    cnt=math.comb(a,2)*math.comb(b,2)+(b if a==3 else 0)+(a if b==3 else 0)
    return 4,cnt

types=subsets=0
for N in range(2,11):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            L=labels(parts); actual=[0]*(N+1)
            for mask in range(1<<N):
                subsets+=1
                got=secure_total(mask,L)
                assert got==criterion(profile(mask,parts),parts)
                if got: actual[mask.bit_count()]+=1
            assert actual==formula(parts)
            g=min(i for i,x in enumerate(actual) if x)
            assert (g,actual[g])==min_formula(parts)
            types+=1
print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("orders = 2..10")
print("all-set criterion matched")
print("all polynomial coefficients matched")
print("minimum sizes and minimum-set counts matched")
