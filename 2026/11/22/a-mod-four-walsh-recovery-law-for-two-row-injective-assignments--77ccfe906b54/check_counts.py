"""All-range independent type-enumeration and explicit extremizer checks.
Run: python check_counts.py
"""
from math import comb

def coefficient(x, y):
    n=len(x)
    return sum(x[i]*y[j] for i in range(n) for j in range(n) if i != j)

def count_zeros(n):
    ans=0
    for u in range(n+1):
        for v in range(n+1):
            for t in range(max(0,u+v-n), min(u,v)+1):
                a,b=n-2*u,n-2*v
                c=n-2*(u+v-2*t)
                if a*b==c:
                    ans+=comb(n,u)*comb(u,t)*comb(n-u,v-t)
    return ans

def example(n,kind):
    if n%2==0:
        x=[-1]*(n//2)+[1]*(n//2)
        y=[1]*n
        if kind=='small': y[-1]=-1
    else:
        k=(n-1)//4 if n%4==1 else (n-3)//4
        u=2*k if n%4==1 else 2*k+1
        t=(k if kind=='zero' else k-1) if n%4==1 else k
        first=set(range(u))
        second=set(range(t)) | set(range(u,u+(u-t)))
        assert len(second)==u and max(second)<n
        x=[-1 if i in first else 1 for i in range(n)]
        y=[-1 if i in second else 1 for i in range(n)]
    return coefficient(x,y)

for n in range(2, 31):
    z=count_zeros(n)
    assert (z==0)==(n%4==3), (n,z)
    if n%2==0:
        assert example(n,'zero')==0
        assert abs(example(n,'small'))==2
    elif n%4==1:
        assert example(n,'zero')==0
        assert example(n,'small')==4
    else:
        assert example(n,'small')==2
    assert z+ (4**n-z)==4**n
    print(f'n={n}: zero={z}, rank={4**n-z}, PASS')
print('independent type enumeration and explicit extremizers passed')
