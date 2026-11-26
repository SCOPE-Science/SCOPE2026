from itertools import product
from collections import Counter
from functools import lru_cache
from math import factorial, comb

@lru_cache(None)
def stirling(n,k):
    if n==k==0:return 1
    if n==0 or k==0 or k>n:return 0
    return stirling(n-1,k-1)+k*stirling(n-1,k)

def polysum(a,b):
    z=Counter(a)
    for k,v in b.items():z[k]+=v
    return +z

def pmul(a,b):
    z=Counter()
    for i,x in a.items():
        for j,y in b.items():z[i+j]+=x*y
    return +z

def predicted(ns,q):
    n=sum(ns); r=len(ns)
    out=Counter()
    # all proper TOTAL colourings, using 1..q colours total
    for ss in product(*(range(1,min(ni,q)+1) for ni in ns)):
        u=sum(ss)
        if u>q: continue
        ways=factorial(q)//factorial(q-u)
        for ni,si in zip(ns,ss): ways*=stirling(ni,si)
        out[n]+=ways
        if u!=q:continue
        I=[i for i,si in enumerate(ss) if si==1]
        if not I:continue
        poly={0:1}
        for i in I:
            poly=pmul(poly,{j:comb(ns[i],j) for j in range(1,ns[i]+1)})
        for h in I:
            term={0:1}
            for i in I:
                if i!=h:term=pmul(term,{j:comb(ns[i],j) for j in range(1,ns[i]+1)})
            poly=polysum(poly,term)
        shift=n-sum(ns[i] for i in I)
        for k,v in poly.items():out[shift+k]+=v*ways
        out[n]-=ways
    return +out

def brute(ns,q):
    parts=[]
    for i,size in enumerate(ns):parts.extend([i]*size)
    neigh=[tuple(j for j in range(len(parts)) if parts[j]!=parts[i]) for i in range(len(parts))]
    counts=Counter()
    for assignment in product(range(q+1),repeat=len(parts)):
        if any(assignment[i]>0 and assignment[i]==assignment[j] for i in range(len(parts)) for j in neigh[i]):continue
        arr=list(assignment)
        while True:
            anyforce=False
            for i,x in enumerate(arr):
                if x:continue
                used={arr[j] for j in neigh[i]}-{0}
                if len(used)==q-1:
                    arr[i]=(set(range(1,q+1))-used).pop()
                    anyforce=True
                    break
            if not anyforce: break
        if all(arr):counts[sum(x>0 for x in assignment)]+=1
    return +counts
def check_balanced(r,t,q):
    from math import ceil,prod
    N=r*t
    enumerated=predicted((t,)*r,q)
    excess=q-r
    k=(excess+t-2)//(t-1)
    if k>r-1:
        assert min(enumerated)==N
        return (N,enumerated[N])
    smallest=r-1+k*(t-1)
    ways=(comb(r,k)*(r-k)*t**(r-k-1)*factorial(q)*
          sum(prod(stirling(t,d+1) for d in ds)
              for ds in product(range(1,t),repeat=k)
              if sum(ds)==excess))
    assert min(enumerated)==smallest and enumerated[smallest]==ways
    return (smallest,ways)

if __name__=='__main__':
    tests=[((2,2,2),q) for q in range(3,7)]+\
          [((1,2,3),q) for q in range(3,7)]+\
          [((2,2,1,1),q) for q in range(4,7)]+\
          [((3,2,1),q) for q in range(3,7)]+\
          [((2,2),q) for q in range(2,5)]
    tested=0
    for ns,q in tests:
        observed=brute(ns,q)
        computed=predicted(ns,q)
        assert observed==computed,(ns,q,observed,computed)
        tested+=1
    print('DIRECT_FORCING_VS_STIRLING_FORMULA_OK',tested,'cases')
    print('K_2_2_2:',{q:dict(predicted((2,2,2),q)) for q in (4,5,6)})
    balanced=0
    for r,t in ((3,2),(3,3),(4,2)):
        for q in range(r+1,r*t+2):
            check_balanced(r,t,q)
            balanced+=1
    print('BALANCED_MINIMUM_AND_MULTIPLICITY_OK',balanced,'cases')
    print('VERIFICATION_OK')
