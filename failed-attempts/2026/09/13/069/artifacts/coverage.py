from itertools import product
def full(k):
    K=[0]+list(k)
    for i in range(1,6):
        for j in range(1,6):
            s=i+j
            if s<6:
                if K[s]>K[i]+K[j]: return None
            elif s>6:
                if K[s-6]>K[i]+K[j]+1: return None
    w=[0]+[6*K[i]+i for i in range(1,6)]
    def le(i,j):
        if i==j: return True
        if j>i: return (K[j]-K[i]>=K[j-i])
        else: return (K[j]-K[i]>=K[j-i+6]+1)
    mx=tuple(i for i in range(1,6) if all(not le(i,j) for j in range(1,6) if j!=i))
    mn=tuple(i for i in range(1,6) if all(not le(j,i) for j in range(1,6) if j!=i))
    e=1+len(mn); g=sum(k); c=max(w[1:])-5; n=c-g; W=e*n-c
    F=max(range(1,6),key=lambda i:w[i])
    return mx,mn,e,g,c,n,W,w,F,K
def le_lin(p,q):
    return ((q-p,0) if q>p else (q-p+6,1))
faces=[((1,2,3),(1,2,4,5)),((1,2,3),(1,2,5)),((1,2,3),(1,4,5)),((1,2,4),(1,3,4,5)),((1,2,4),(1,3,5)),((1,2,5),(2,3,4,5)),((1,2,5),(3,4,5)),((1,3,4),(2,3,4,5)),((1,3,4),(2,3,5)),((1,4,5),(1,2,3)),((1,4,5),(1,2,3,4)),((2,3,4),(1,3,5)),((2,3,5),(1,2,3,4)),((2,3,5),(1,3,4)),((2,4,5),(1,2,3,5)),((2,4,5),(1,3,5)),((3,4,5),(1,2,4,5)),((3,4,5),(1,2,5)),((3,4,5),(1,4,5))]
uncovered=0; tot=0; minW=None
for k in product(range(1,7),repeat=5):
    r=full(k)
    if r is None:
        continue
    mx,mn,e,g,c,n,W,w,F,K=r
    if len(mx)!=3:
        continue
    tot+=1
    if minW is None or W<minW:
        minW=W
    M,A=mx,mn
    assert (M,A) in faces,(k,M,A)
    nonmax=[q for q in range(1,6) if q not in M]
    nonmin=[j for j in range(1,6) if j not in A]
    found=False
    for wm in product(M,repeat=len(nonmax)):
        for wn in product(A,repeat=len(nonmin)):
            ok=True
            for q,p in zip(nonmax,wm):
                d,off=le_lin(q,p)
                if not (K[p]-K[q]-K[d]>=off):
                    ok=False; break
            for j,a in zip(nonmin,wn):
                if not ok:
                    break
                d,off=le_lin(a,j)
                if not (K[j]-K[a]-K[d]>=off):
                    ok=False; break
            if ok:
                found=True; break
        if found:
            break
    if not found:
        uncovered+=1
        print("UNCOVERED",k)
print("type-3 in box6:",tot,"uncovered:",uncovered,"minW:",minW)
