import numpy as np

def rank_spectral(q,alpha=None):
    # GF2 and GF4 with irreducible polynomial x^2+x+1, otherwise odd prime
    if q in (2,4):
        add=lambda a,b:a^b
        def mul(a,b):
            if q==2:return a*b
            r=0
            while b:
                if b&1:r^=a
                b>>=1;a<<=1
                if a&4:a^=7
            return r
        sq=lambda a:mul(a,a)
        trace=lambda a: a if q==2 else add(a,sq(a))
        chi=lambda a:1 if trace(a)==0 else -1
        alpha=1 if q==2 else 2
        def Q(x):
            a,b,u,v=x
            return add(add(mul(a,b),sq(u)),add(mul(u,v),mul(alpha,sq(v))))
        def B(x,y):
            a,b,u,v=x;aa,bb,uu,vv=y
            return add(add(mul(a,bb),mul(aa,b)),add(mul(u,vv),mul(uu,v)))
    else:
        chi=lambda a:np.exp(2j*np.pi*a/q)
        def Q(x):
            a,b,u,v=x
            return (a*b-u*u+alpha*v*v)%q
        def B(x,y):
            a,b,u,v=x;aa,bb,uu,vv=y
            return (a*bb+aa*b-2*u*uu+2*alpha*v*vv)%q
    import itertools
    C=[];S=[]
    for x in itertools.product(range(q),repeat=4):
        (C if Q(x)==0 else S).append(x)
    H=np.array([[chi(B(x,y)) for y in S] for x in S],dtype=complex)
    vals=np.linalg.svd(H,compute_uv=False)
    r=q*q+1; c=1+r*(q-1);s=q**4-c
    predicted=np.array(sorted([q**2]*(s-c+1)+[q**1.5]*(r*(q-2))+[q]*r,reverse=True))
    assert len(S)==s and len(C)==c
    assert len(vals)==len(predicted)
    err=max(abs(vals-predicted))
    assert err<1e-7
    print('HERMITIAN_FOURIER_SPECTRUM_PASS', 'q=',q,'size=',s,'maxerr=',err)
for q,d in [(2,None),(3,2),(4,None),(5,2)]:rank_spectral(q,d)
