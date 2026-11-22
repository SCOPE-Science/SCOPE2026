import math

def F(x,n,s):
    y=0
    for i in range(n):
        if (x>>((i-1)%n))&1 or (x>>((i-s)%n))&1:
            y |= (1<<i)
    return y

def tm_count(m,t):
    # cyclic words without all-zero and without zero-run of length t+1
    good=1
    for x in range(1,1<<m):
        if all(any((x>>((i-j)%m))&1 for j in range(t+1)) for i in range(m)):
            good+=1
    return good

def test(maxn=12):
    for n in range(3,maxn+1):
        for s in range(2,n):
            g=math.gcd(n,s-1);m=n//g
            tcounts=[0]*m
            phase_fibers={}
            for x in range(1<<n):
                y=x;T=None
                for t in range(m):
                    z=F(y,n,s)
                    if all(((y>>i)&1)==((y>>((i+g)%n))&1) for i in range(n)):
                        T=t;break
                    y=z
                assert T is not None,(n,s,x)
                tcounts[T]+=1
                if n<=10:
                    yy=x
                    for _ in range(m-1):
                        yy=F(yy,n,s)
                    phase_fibers[yy]=phase_fibers.get(yy,0)+1
            expect=[tm_count(m,t)**g for t in range(m)]
            counts=[expect[0]] + [expect[t]-expect[t-1] for t in range(1,m)]
            assert counts==tcounts,(n,s,counts,tcounts)
            assert tcounts[-1]==2**n-(2**m-m)**g,(n,s)
            if n<=10:
                assert len(phase_fibers)==2**g
                for state,num in phase_fibers.items():
                    assert all(((state>>i)&1)==((state>>((i+g)%n))&1) for i in range(n))
                    w=sum((state>>j)&1 for j in range(g))
                    assert num==(2**m-1)**w,(n,s,state,num,w)
            print('OK',n,s,'g,m=',g,m,'E',tcounts)
    return 'ALL_OK'
if __name__=='__main__':print(test())
