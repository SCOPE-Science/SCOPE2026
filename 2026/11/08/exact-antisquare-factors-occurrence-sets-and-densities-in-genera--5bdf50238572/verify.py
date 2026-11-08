from collections import Counter
from math import floor

def val(b,n):
    z=0
    while n%b==0:
        n//=b; z+=1
    return z

def H(b,n):
    ans=0; p=b
    while p<=n:
        ans+=n//p-n//(p*b)
        p*=b*b
    return ans

def E(n):
    ans=0; p=4
    while p<=n:
        ans+=n//p-n//(2*p)
        p*=4
    return ans

def predicted(b,n):
    C={'01':H(b,n+1),'10':H(b,n)}
    if b==2:
        C['010101']=E((n-1)//2+2)
        C['101010']=E((n-2)//2+2)
    if b==3:
        Q=(n-3)//3
        C['1001']=Q+1-H(3,Q+1)-H(3,Q+2) if Q>=0 else 0
    return C

for b in range(2,15):
    L=16000
    a=[val(b,i+1)&1 for i in range(L+240)]
    cnt=Counter()
    for i in range(L):
        for k in range(1,33):
            if all(a[i+j]!=a[i+k+j] for j in range(k)):
                cnt[''.join(str(x) for x in a[i:i+2*k])]+=1
    P=predicted(b,L)
    assert dict(cnt)=={x:y for x,y in P.items() if y>0},(b,dict(cnt),P)
    for n in (0,1,2,3,4,5,6,7,10,20,50,100,511,512,1023,2024,5000,15000):
        D=Counter()
        for i in range(n):
            for k in range(1,16):
                if all(a[i+j]!=a[i+k+j] for j in range(k)):
                    D[''.join(map(str,a[i:i+2*k]))]+=1
        assert dict(D)=={x:y for x,y in predicted(b,n).items() if y>0},(b,n,dict(D),predicted(b,n))
print('VERIFY_OK bases=2..14 starts=16000 order_max=32 prefix_checks=18')
