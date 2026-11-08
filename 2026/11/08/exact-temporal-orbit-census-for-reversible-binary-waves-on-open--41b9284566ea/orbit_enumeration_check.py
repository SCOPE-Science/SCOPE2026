"""Independent exhaustive functional-cycle enumeration on small open chains."""
from math import gcd


def update(state,n):
    mask=(1<<n)-1
    new=((state & mask)<<1 ^ (state&mask)>>1 ^ (state>>n)) & mask
    return new | ((state & mask)<<n)


def v2(k):
    a=0
    while k%2==0: k//=2; a+=1
    return a,k


def predicted_fixed(n,t):
    a,u=v2(n+1)
    b,v=v2(t)
    h=gcd(u,v)
    return 1<<((h-1)*min(1<<(a+1),1<<b)+min((1<<(a+1))-2,1<<b))


def mobius(k):
    p=0
    d=2
    while d*d<=k:
        if k%d==0:
            k//=d
            if k%d==0:return 0
            p+=1
        d+=1
    if k>1:p+=1
    return (-1)**p


def main():
    count=0
    for n in range(2,9):
        size=1<<(2*n)
        seen=bytearray(size)
        observed={}
        for x in range(size):
            if seen[x]: continue
            cycle=[]
            y=x
            while not seen[y]:
                seen[y]=1
                cycle.append(y)
                y=update(y,n)
            assert y==x,('nonperiodic',n,x)
            observed[len(cycle)]=observed.get(len(cycle),0)+1
        order=2*(n+1)
        for t in range(1,order+1):
            if order%t:continue
            sum_fixed=sum(k*o for k,o in observed.items() if t%k==0)
            assert sum_fixed==predicted_fixed(n,t),(n,t,sum_fixed,predicted_fixed(n,t))
            predicted_points=sum(mobius(t//d)*predicted_fixed(n,d) for d in range(1,t+1) if t%d==0)
            assert t*observed.get(t,0)==predicted_points,(n,t,observed.get(t,0),predicted_points)
            count+=1
        assert sum(k*o for k,o in observed.items())==size
        assert max(observed)==order
        print(f'n={n} states={size} orbit_periods={sorted(observed.items())}')
    print(f'PASS: {count} independent fixed-count and primitive-orbit comparisons')

if __name__=='__main__':main()
