"""Directly iterate all binary configurations, with no matrix rank operations."""

def next_state(m,s):
    n=1<<m;mask=n-1;out=0
    for w in range(n):
        new=((s>>((2*w)&mask))^(s>>(((2*w)&mask)|1)))&1
        if w==0:new^=(s&1)
        out|=new<<w
    return out

def test(m):
    n=1<<m;T=max(0,m-1);d=m+2;layer=[0]*(T+1)
    for s in range(1<<n):
        u=s
        for t in range(T):u=next_state(m,u)
        v=u
        for _ in range(d):v=next_state(m,v)
        assert u==v,(m,s,u,v)
        # smallest entry t with F^(t+d)(s)=F^t(s)
        a=s
        first=None
        for t in range(T+1):
            b=a
            for _ in range(d):b=next_state(m,b)
            if a==b:
                first=t;break
            a=next_state(m,a)
        assert first is not None
        layer[first]+=1
    for t in range(T+1):
        cnt=sum(layer[:t+1]);rr=(1<<(m-t))+t if t<=m else m+1
        assert cnt==2**(n-rr+(m+1)),(m,t,cnt,rr)
    print('m',m,'states',1<<n,'entry shells',layer)
if __name__=='__main__':
    for m in range(1,5):test(m)
    print('PASS independent exhaustive state enumeration')
