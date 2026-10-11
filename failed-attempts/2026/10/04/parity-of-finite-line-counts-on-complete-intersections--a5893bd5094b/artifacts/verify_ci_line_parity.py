from itertools import combinations_with_replacement

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def factor_poly(d):
    p=[1]
    for j in range(d+1):
        p=mul(p,[d-j,j])
    return p

def line_count(ds,n):
    q=[1]
    for d in ds: q=mul(q,factor_poly(d))
    # coeff of x^(n-1) in (1-x)q
    return q[n-1] - (q[n-2] if n>=2 else 0)

def parts(total,k,lo=2):
    def rec(rem,kk,minv,pref):
        if kk==0:
            if rem==0: yield tuple(pref)
            return
        for v in range(minv, rem//kk+1):
            yield from rec(rem-v,kk-1,v,pref+[v])
    yield from rec(total,k,lo,[])

known={((5,),4):2875,((4,2),5):1280,((3,3),5):1053,((3,2,2),6):720,((2,2,2,2),7):512}
for (ds,n),want in known.items():
    got=line_count(ds,n)
    assert got==want,(ds,n,got,want)

cases=0
odd_cases=0
for n in range(3,13):
    for s in range(1,n):
        # zero expected dimension: sum(d_i+1)=2n-2
        total=2*n-2-s
        if total<2*s: continue
        for ds in parts(total,s,2):
            c=line_count(ds,n)
            pred=all(d%2 for d in ds)
            assert (c%2==1)==pred,(n,ds,c,pred)
            cases+=1
            odd_cases+=pred
print('VERIFY_OK', 'cases',cases,'odd_cases',odd_cases)
