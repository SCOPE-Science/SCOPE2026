from collections import defaultdict
from itertools import product
from math import comb

def direct(n):
    ws=[]
    for x in product('UD',repeat=n):
        h=0
        for c in x:
            h+=1 if c=='U' else -1
            if h<0:break
        else:ws.append(''.join(x))
    ds=[{w[:i]+w[i+1:] for i in range(n)} for w in ws]
    even=odd=0
    for i in range(len(ws)):
        for j in range(i+1,len(ws)):
            if len(ds[i]&ds[j])==2:
                if ws[i].count('U')==ws[j].count('U'):even+=1
                else:odd+=1
    return even,odd

def dp(N):
    # state (altitude, final symbol); tuple (number of paths, sum of D-start alternating suffix counts, sum of marked factors by parity)
    D={(0,'?'):(1,0,0,0)}
    out=[(0,0)]
    for n in range(1,N+1):
        nxt=defaultdict(lambda:(0,0,0,0))
        for (h,last),(cnt,a,e,o) in D.items():
            for c in 'UD':
                nh=h+(1 if c=='U' else -1)
                if nh<0:continue
                added=a if (last=='D' and c=='U') or (last=='U' and c=='D') else 0
                na=(a if last=='D' else 0) if c=='U' else (cnt+(a if last=='U' else 0))
                x,y,z,t=nxt[(nh,c)]
                nxt[(nh,c)]=(x+cnt,y+na,z+e+(added if c=='U' else 0),t+o+(added if c=='D' else 0))
        D=nxt
        out.append((sum(v[2] for v in D.values()),sum(v[3] for v in D.values())))
    return out

def cat(n):return comb(2*n,n)//(n+1)

def convolution(a,b,N):return [sum(a[k]*b[n-k] for k in range(n+1)) for n in range(N+1)]

def series(N):
    C=[0]*(N+1)
    for m in range(N//2+1):C[2*m]=cat(m)
    t=[0]+C[:-1]
    def add(a,b):return [x+y for x,y in zip(a,b)]
    def sub(a,b):return [x-y for x,y in zip(a,b)]
    def inv(a):
        assert a[0]==1
        r=[0]*(N+1);r[0]=1
        for n in range(1,N+1):r[n]=-sum(a[k]*r[n-k] for k in range(1,n+1))
        return r
    def mul(*aa):
        r=[1]+[0]*N
        for a in aa:r=convolution(r,a,N)
        return r
    one=[1]+[0]*N
    # E_even=z²/(1-z²) C/(1-2z) * (t/(1-t)-t³/(1-t²)); E_odd=z³/(1-z²) C/(1-2z)*(t/(1-t)-t²/(1-t²))
    z=[0,1]+[0]*(N-1);z2=mul(z,z);z3=mul(z,z,z)
    twoz=[0,2]+[0]*(N-1)
    common=mul(C,inv(sub(one,twoz)),inv(sub(one,z2)))
    even=mul(common,z2,sub(mul(t,inv(sub(one,t))),mul(t,t,t,inv(sub(one,mul(t,t))))))
    odd=mul(common,z3,sub(mul(t,inv(sub(one,t))),mul(t,t,inv(sub(one,mul(t,t))))))
    return list(zip(even,odd))

if __name__=='__main__':
    a=dp(60);b=series(60)
    assert a==b,(next((i,a[i],b[i]) for i in range(len(a)) if a[i]!=b[i]),)
    for n in range(2,11):
        x=direct(n);assert a[n]==x,(n,x,a[n]);print(n,x,sum(x))
    print('DP and formal series agree for 0 <= n <= 60; deletion-set census agrees for 2 <= n <= 10.')
