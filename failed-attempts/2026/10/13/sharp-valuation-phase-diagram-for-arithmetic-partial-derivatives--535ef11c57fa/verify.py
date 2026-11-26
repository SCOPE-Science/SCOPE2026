from math import factorial

def vp(n,p):
    if n==0: return 10**9
    n=abs(n); e=0
    while n%p==0:
        n//=p; e+=1
    return e

def Dp(n,p):
    if n==0: return 0
    return n*vp(n,p)//p

def primes_upto(N):
    out=[]
    for x in range(2,N+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out

checks=0
for p in primes_upto(97):
    for a in [-11,-7,-1,1,5,13]:
        if a%p==0: continue
        # extinction and landing regimes, all e through 2p-1
        for e in range(0,2*p):
            n=a*(p**e)
            x=n
            if e<p:
                for j in range(e+1):
                    expect=a*(factorial(e)//factorial(e-j))*(p**(e-j))
                    assert x==expect,(p,a,e,j,x,expect)
                    x=Dp(x,p)
                    checks+=1
                assert x==0
                checks+=1
            else:
                r=e-p
                for j in range(r+1):
                    expect=a*(factorial(e)//factorial(e-j))*(p**(e-j))
                    assert x==expect,(p,a,e,j,x,expect)
                    x=Dp(x,p)
                    checks+=1
                fixed=a*(factorial(e)//factorial(p))*(p**p)
                assert x==fixed and Dp(fixed,p)==fixed
                checks+=2
        # divergent regime: sample e from 2p through 2p+30 and 40 iterates
        for e in range(2*p,2*p+31):
            x=a*(p**e)
            base=abs(x)
            for i in range(40):
                ee=vp(x,p)
                assert ee>=2*p,(p,a,e,i,ee)
                y=Dp(x,p)
                assert abs(y)>=2*abs(x),(p,a,e,i,ee,x,y)
                x=y
                checks+=2
            assert abs(x)>= (2**40)*base
            checks+=1
print('VERIFY_OK')
print('primes_tested',len(primes_upto(97)))
print('checks',checks)
print('boundary_examples')
for p in [2,3,5,7,11]:
    vals=[]
    for e in [p-1,p,2*p-1,2*p]:
        n=p**e
        vals.append((e,Dp(n,p),vp(Dp(n,p),p) if Dp(n,p) else None))
    print(p,vals)
