import math

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x): yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts): out += [i]*a
    return out

def dominates(mask,lab):
    n=len(lab)
    if mask==0: return False
    for v in range(n):
        if mask>>v & 1: continue
        if not any((mask>>u & 1) and lab[u]!=lab[v] for u in range(n)):
            return False
    return True

def perfect(mask,lab):
    vs=[v for v in range(len(lab)) if mask>>v & 1]
    if len(vs)%2: return False
    if not vs: return True
    u=vs[0]
    rem=mask & ~(1<<u)
    return any(lab[v]!=lab[u] and perfect(rem & ~(1<<v),lab) for v in vs[1:])

def pd(mask,lab):
    return mask!=0 and dominates(mask,lab) and perfect(mask,lab)

def formula(parts):
    N=sum(parts); c=[0]*(N+1)
    for t in range(1,N//2+1):
        bad=0
        for ni in parts:
            for j in range(t+1,min(ni,2*t)+1):
                q=2*t-j
                if 0<=q<=N-ni:
                    bad += math.comb(ni,j)*math.comb(N-ni,q)
        c[2*t]=math.comb(N,2*t)-bad
    return c

types=subsets=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=labels(parts); actual=[0]*(N+1); valid=[]
            for mask in range(1<<N):
                subsets+=1
                if pd(mask,lab):
                    actual[mask.bit_count()]+=1
                    valid.append(mask)
            assert actual==formula(parts)
            mins=[]
            for mask in valid:
                minimal=True
                sub=(mask-1)&mask
                while sub:
                    if pd(sub,lab):
                        minimal=False; break
                    sub=(sub-1)&mask
                if minimal: mins.append(mask)
            e=sum(parts[i]*parts[j] for i in range(r) for j in range(i+1,r))
            assert len(mins)==e
            assert all(m.bit_count()==2 for m in mins)
            types+=1
print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("orders = 2..9")
print("all polynomial coefficients matched")
print("all minimal paired-dominating sets were exactly cross-part pairs")
