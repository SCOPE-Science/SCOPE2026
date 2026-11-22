"""Independent finite-diagram tests for semigeneric multipartite extension-type formulas.

Only finite cases are tested. The general theorem requires a separate symbolic proof.
"""
from itertools import combinations, product
from math import comb

def stirling(n,k):
    if n==k==0: return 1
    if k==0 or k>n: return 0
    a=[0]*(k+1); a[0]=1
    for i in range(1,n+1):
        b=[0]*(k+1)
        for j in range(1,min(i,k)+1): b[j]=j*a[j]+a[j-1]
        a=b
    return a[k]

def formula(n,k,r):
    return sum(comb(r,j)*k**(r-j)*stirling(j,l)*2**(l*n+(k+l-1)*r-k*l-l*(l-1)//2)
               for l in range(r+1) for j in range(l,r+1))

def assignments(k,r):
    def rec(a,h):
        if len(a)==r:
            yield tuple(a); return
        for c in range(k+h+1):
            yield from rec(a+[c],h+(c==k+h))
    yield from rec([],0)

def brute(n,k,r,phase=0):
    # Canonical nonempty old classes; their sizes may differ.
    classes=tuple(list(range(k))+[(i%k) for i in range(n-k)])
    total=0
    for tail in assignments(k,r):
        full=classes+tail
        edges=[(i,j) for i in range(n+r) for j in range(i+1,n+r) if full[i]!=full[j]]
        base=[(i,j) for i,j in edges if i<n and j<n]
        free=[(i,j) for i,j in edges if not (i<n and j<n)]
        base_values={e:((i%2) if phase and k==2 else 0) for i,e in enumerate(base)}
        # With two singleton/one extra vertices, any base orientation is parity-legal.
        # Check validity of chosen old-base phase first.
        rectangles=[]
        for ca,cb in combinations(sorted(set(full)),2):
            av=[i for i,v in enumerate(full) if v==ca]
            bv=[i for i,v in enumerate(full) if v==cb]
            for p,q in combinations(av,2):
                for s,t in combinations(bv,2):
                    rectangles.append(tuple((min(a,b),max(a,b)) for a,b in ((p,s),(p,t),(q,s),(q,t))))
        if any(all(e in base_values for e in rect) and sum(base_values[e] for e in rect)%2 for rect in rectangles):
            raise ValueError('Old-base orientation invalid')
        for bits in product((0,1),repeat=len(free)):
            vals=dict(base_values);vals.update(zip(free,bits))
            if all(sum(vals[e] for e in rect)%2==0 for rect in rectangles):total+=1
    return total

def checks():
    count=0
    for n in range(1,5):
        for k in range(1,n+1):
            for r in range(3):
                actual=brute(n,k,r)
                expect=formula(n,k,r)
                assert actual==expect,(n,k,r,actual,expect)
                count+=1
    for n,k,r in [(2,2,3),(3,1,3),(3,2,3),(3,3,3),(3,2,2)]:
        assert brute(n,k,r)==formula(n,k,r)
        count+=1
    # Independently change the orientation of a nontrivial three-vertex base.
    assert brute(3,2,2,phase=1)==formula(3,2,2)
    count+=1
    for n in range(1,15):
        for k in range(1,n+1):
            u=2**n+k*2**(k-1)
            v=2**(2*n+1)+(2*k+1)*2**(n+k)+k*k*2**(2*k-2)
            assert formula(n,k,1)==u and formula(n,k,2)==v
            count+=1
    seen={}
    collisions=0
    for n in range(1,90):
        for k in range(1,n+1):
            u=formula(n,k,1)
            v=formula(n,k,2)
            for n0,k0,v0 in seen.get(u,[]):
                assert k!=k0
                assert (k>k0 and v<v0) or (k<k0 and v>v0)
                collisions+=1
            seen.setdefault(u,[]).append((n,k,v))
            count+=1
    for g in range(5):
        for e in range(1,5):
            k=2**(g+2)*(2**e-1)-1
            n=k+g
            assert formula(n,k,1)==formula(n+e,k-1,1)
            assert formula(n,k,2)<formula(n+e,k-1,2)
            count+=1
    print('EXACT_DIAGRAM_CHECKS_PASS',count,'one_type_collisions_compared',collisions)
    print('BASE_COLLISION_EXAMPLE', (3,3,formula(3,3,1),formula(3,3,2)),(4,2,formula(4,2,1),formula(4,2,2)))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':checks()
