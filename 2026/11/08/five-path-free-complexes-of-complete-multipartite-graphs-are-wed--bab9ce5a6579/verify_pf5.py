from itertools import combinations, permutations, product
from math import comb
from collections import defaultdict

def groups(parts):
    return tuple(j for i,n in enumerate(parts) for j in [i]*n)

def enumerated_faces(parts):
    typ=groups(parts); N=len(typ)
    faces=defaultdict(list)
    for k in range(N+1):
        for x in combinations(range(N),k):
            ok=True
            if k>=5:
                for ys in combinations(x,5):
                    for pi in permutations(ys):
                        if all(typ[pi[j]]!=typ[pi[j+1]] for j in range(4)):
                            ok=False;break
                    if not ok:break
            if ok: faces[k-1].append(x)
    return faces

def reduced_rank(faces,p):
    out={}
    ks=sorted(k for k in faces if k>=0)
    for d in ks:
        if d==0:
            out[d]=1 if faces[d] else 0;continue
        col=faces[d-1]; row={x:i for i,x in enumerate(col)}
        pivots={}
        for f in faces[d]:
            v={row[f[:i]+f[i+1:]]:(-1 if i%2 else 1)%p for i in range(len(f))}
            while v:
                i=min(v)
                if not v[i]%p:del v[i];continue
                if i not in pivots:
                    a=v[i]%p; inv=pow(a,-1,p)
                    pivots[i]={j:(x*inv)%p for j,x in v.items() if x%p}
                    break
                pp=pivots[i]; fact=v[i]%p
                for j,x in pp.items():
                    val=(v.get(j,0)-fact*x)%p
                    if val:v[j]=val
                    elif j in v:del v[j]
        out[d]=len(pivots)
    ans={}
    for d in ks:
        ans[d]=len(faces[d])-out[d]-(out.get(d+1,0))
    return {k:v for k,v in ans.items() if v}

def beta(parts):
    N=sum(parts)
    def C(a,b):return comb(a,b) if 0<=b<=a else 0
    return C(N-1,4)-sum(C(a-1,4)+(N-a)*C(a-1,3) for a in parts)

count=0
for n in range(5,9):
    for m in range(2,min(n,5)+1):
        for p in combinations(range(1,n),m-1):
            z=(0,)+p+(n,)
            parts=tuple(z[i+1]-z[i] for i in range(m))
            f=enumerated_faces(parts)
            for field in [2,3]:
                h=reduced_rank(f,field)
                if h !=({3:beta(parts)} if beta(parts)>0 else {}):
                    raise AssertionError((parts,field,h,beta(parts)))
            count+=1
print('PF5_OK',count,'cases', 'mod2/mod3', 'n<=8')
for p in [(1,1,1,1,1),(2,2,2),(3,3,3),(4,3,2),(3,2,2,2),(5,2,2)]:
 print(p,'beta3',beta(p))
