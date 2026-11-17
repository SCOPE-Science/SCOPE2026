"""Independent direct, non-matrix enumeration of complete states for d=0,1,2.
Local arithmetic is over F_3; the analytical theorem covers all F_{3^f}.
"""
from collections import Counter

def step(u,v,d):
    n=1<<d; z=[]
    for x in range(n):
        neigh=sum(u[x^(1<<j)] for j in range(d))
        z.append((neigh-v[x])%3)
    return tuple(z),u

def powers(num):
    a=(2**num-(-1)**num)//3
    b=(2**num+2*(-1)**num)//3
    q=3
    return {1:q**a,2:q**(2*a),3:q**(2*a),4:q**(2*b+2*a),6:q**(4*a),12:q**(2*b+4*a)}

def encode(x,n):
    r=[0]*n
    for i in range(n):r[i],x=x%3,x//3
    return tuple(r)

for d in (0,1,2):
    n=1<<d
    counter=Counter()
    for k in range(3**(2*n)):
        u=encode(k%(3**n),n); v=encode(k//(3**n),n)
        initial=(u,v); state=initial
        for t in range(1,13):
            state=step(*state,d)
            if state==initial:
                counter[t]+=1;break
        else:raise AssertionError((d,k,'no return within 12'))
    assert sum(counter.values())==3**(2*n)
    expect=powers(d)
    cumulative={t:sum(c for p,c in counter.items() if t%p==0) for t in (1,2,3,4,6,12)}
    assert cumulative==expect,(d,cumulative,expect)
    assert all(t in (1,2,3,4,6,12) for t in counter)
    print(f'd={d} total={3**(2*n)} period_populations={dict(sorted(counter.items()))} fixed_counts={cumulative}')
print('PASS complete direct enumeration, d=0,1,2')
