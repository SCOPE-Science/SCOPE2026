"""Construct explicit global-spin-complement loops at the maximal cut energy."""

def make_spin(n,positions):
    z=sum(1<<j for j in positions)
    assert z.bit_count()%2==n%2
    x=0
    # z_i = 1 iff x_i=x_(i+1); hence x_(i+1)=x_i XOR(1-z_i)
    for i in range(n-1):
        nextbit=((x>>i)&1) ^ (1-((z>>i)&1))
        x |= nextbit<<(i+1)
    assert ((((x>>(n-1))^(x>>0))&1)==(1-((z>>(n-1))&1)))
    return x

def cut(n,x):
    return sum(((x>>i)^(x>>((i+d)%n)))&1 for i in range(n) for d in (1,2))

def sequence(n):
    assert n%4 !=0
    k = n//2 if n%4==3 else (n-3)//2 if n%4==1 else (n-2)//2
    initial=make_spin(n,range(0,2*k,2))
    sites=[]
    if k%2==1:
        for r in range(n):
            for j in range(k-1,-1,-1):
                sites.append((r+2*j+1)%n)
    else:
        assert n==2*k+2
        sites += [2*k-1,2*k]
        for j in range(k-2,-1,-1): sites += [2*j+1,2*j+2]
        sites += [2*k+1,0]
    x=initial; m=cut(n,x)
    for i in sites:
        y=x^(1<<i)
        assert cut(n,y)==m,(n,i,x,cut(n,y),m)
        x=y
    assert x == initial ^ ((1<<n)-1), (n,x,initial,sites)
    return len(sites),len(set(sites))

if __name__=='__main__':
    for n in range(5,26):
        if n%4==0:continue
        length,distinct=sequence(n)
        assert length % n == 0
        print(n,length,distinct)
    print('PASS: explicit all-spin-complement neutral loops in every non-four-divisible tested length')
