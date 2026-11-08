"""Independent simulation and exact run-formula checks for synchronous binary majority on fans."""
from math import comb

def exact_orbits(n):
    ans=0
    for k in range(n//2+1,n):
        for r in range(1,min(k//2,n-k)+1):
            if 2*(k-r)>=n: continue
            num=n*comb(k-r-1,r-1)*comb(n-k-1,r-1)
            assert num%r==0
            ans+=num//r
    return ans

def update(n,z):
    # vertex 0 hub, vertices 1..n along the path
    y=0
    nb=[list(range(1,n+1))]
    nb.extend(([0]+([i-1] if i>1 else [])+([i+1] if i<n else [])) for i in range(1,n+1))
    for i,nei in enumerate(nb):
        t=sum((z>>j)&1 for j in nei)
        if 2*t>len(nei) or (2*t==len(nei) and (z>>i)&1):
            y|=1<<i
    return y

def alternate_hub0(n,z):
    x=[(z>>i)&1 for i in range(1,n+1)]
    edges=[(0,1)]+[(i-1,i+1) for i in range(1,n-1)]+[(n-2,n-1)]
    k=sum(x)
    e=sum(x[a]&x[b] for a,b in edges)
    open_fixed=all(not x[i] or any(x[a]&x[b] for a,b in edges if i in (a,b)) for i in range(n))
    return 2*k>n and 2*e<n and open_fixed

if __name__=='__main__':
    for n in range(3,14):
        fixed=period2=hub0states=0
        for z in range(1<<(n+1)):
            y=update(n,z)
            if update(n,y)!=z: continue
            if y==z:
                fixed+=1
                assert z in (0,(1<<(n+1))-1)
            else:
                period2+=1
                assert ((z^y)&1)==1
                if not(z&1):
                    hub0states+=1
                    assert alternate_hub0(n,z)
        expected=exact_orbits(n)
        assert (fixed,period2,hub0states)==(2,2*expected,expected),(n,fixed,period2,expected)
        print(f'n={n} fixed={fixed} primitive_two_states={period2} two_orbits={expected}')
    print('DIRECT_AND_BINOMIAL_OK')
