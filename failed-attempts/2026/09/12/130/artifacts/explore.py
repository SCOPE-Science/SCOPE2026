import itertools, math, random

def conic_normals(p):
    pts=[]
    for a in range(p):
        for b in range(p):
            for c in range(p):
                if (a,b,c)==(0,0,0): continue
                if (a*a+b*b-c*c)%p==0:
                    pts.append((a,b,c))
    # projective: dedupe by scalar multiple
    seen=set(); reps=[]
    for (a,b,c) in pts:
        # canonical: first nonzero =1
        for lam in range(1,p):
            pass
        # find canonical representative
        v=(a,b,c)
        # normalize
        for i in range(3):
            if v[i]%p!=0:
                inv=pow(v[i],-1,p)
                v=tuple((x*inv)%p for x in v)
                break
        if v not in seen:
            seen.add(v); reps.append(v)
    return reps

for p in [5,7,11]:
    reps=conic_normals(p)
    print(p, len(reps), "expected", p+1 if (-1)**((p-1)//2)==1 else p+1)  # smooth conic has p+1 points always
    # count: smooth conic over F_p always p+1 points
