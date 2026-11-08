#!/usr/bin/env python3
"""Exact integer checks for weighted four-part partitions and ring period certificates.
No external libraries; no floating-point arithmetic.
"""

# Polynomials in ascending degree (integer coefficients).
def mul_poly(u, v):
    w=[0]*(len(u)+len(v)-1)
    for i,a in enumerate(u):
        for j,b in enumerate(v): w[i+j]+=a*b
    return w

def pow_poly(v,k):
    r=[1]
    for _ in range(k): r=mul_poly(r,v)
    return r

D=[1]
for p,k in [([-1,1],6),([1,1],4),([1,0,1],3),([1,1,1],3)]:
    D=mul_poly(D,pow_poly(p,k))
N=[0]*4+[6,15,34,57,95,121,146,126,106,72,50,25,11]
assert len(D)==23 and D[0]==D[-1]==1 and len(N)==17
K=22

def ring_mul(u,v,mod):
    w=[0]*(2*K-1)
    for i,a in enumerate(u):
        if a:
            for j,b in enumerate(v):
                if b:w[i+j]=(w[i+j]+a*b)%mod
    for t in range(2*K-2,K-1,-1):
        c=w[t]
        if c:
            for j in range(K):w[t-K+j]=(w[t-K+j]-c*D[j])%mod
    return w[:K]

def ring_pow(T,mod):
    x=[0]*K;x[1]=1
    y=[0]*K;y[0]=1
    while T:
        if T&1:y=ring_mul(x,y,mod)
        x=ring_mul(x,x,mod)
        T//=2
    return y

def period_divisibility(T,mod):
    r=ring_pow(T,mod)
    r[0]=(r[0]-1)%mod
    nr=ring_mul(N+[0]*(K-len(N)),r,mod)
    return not any(nr)

def exact_order_tests():
    expected={2:48,3:54,4:96,5:300,6:432,7:84,8:192,9:324,
              10:1200,11:132,12:864,13:156,14:336,16:384,
              17:204,18:1296,19:228,21:756,22:528,23:276,
              25:1500,26:624,27:972,28:672,29:348,31:372,37:444,49:588}
    for m,T in expected.items():
        assert period_divisibility(T,m),(m,T,'not a period')
        # A candidate period is least exactly when division by each prime fails.
        n=T; primes=[];p=2
        while p*p<=n:
            if n%p==0:
                primes.append(p)
                while n%p==0:n//=p
            p+=1
        if n>1:primes.append(n)
        for p in primes:
            assert not period_divisibility(T//p,m),(m,T,p,'final')
    return expected

def add_poly(u,v):
    w=[0]*max(len(u),len(v))
    for i,a in enumerate(u):w[i]+=a
    for i,b in enumerate(v):w[i]+=b
    return w

def generating_identity():
    # Four positive partition parts are a+b+c+e+1,b+c+e+1,c+e+1,e+1.
    # Every monomial in e_2(parts) is listed below in gap variables a,b,c,e.
    monomials=[(1,(1,1,0,0)),(2,(1,0,1,0)),(3,(1,0,0,1)),
               (3,(1,0,0,0)),(1,(0,2,0,0)),(4,(0,1,1,0)),
               (6,(0,1,0,1)),(6,(0,1,0,0)),(3,(0,0,2,0)),
               (9,(0,0,1,1)),(9,(0,0,1,0)),(6,(0,0,0,2)),
               (12,(0,0,0,1)),(6,(0,0,0,0))]
    weights=(1,2,3,4)
    def term(w,k):
        x=[0]*w+[1]
        one_minus=[1]+[0]*(w-1)+[-1]
        if k==0:return mul_poly(one_minus,one_minus)
        if k==1:return mul_poly(x,one_minus)
        if k==2:return add_poly(x,mul_poly(x,x))
        raise ValueError(k)
    H=[0]
    for coefficient,exps in monomials:
        t=[coefficient]
        for w,k in zip(weights,exps):t=mul_poly(t,term(w,k))
        H=add_poly(H,t)
    C=[1]
    for w in weights:C=mul_poly(C,pow_poly([1]+[0]*(w-1)+[-1],3))
    left=mul_poly(([0]*4)+H,D)
    right=mul_poly(N,C)
    assert left==right or all((left[i] if i<len(left) else 0)==(right[i] if i<len(right) else 0)
                              for i in range(max(len(left),len(right))))


def poly_mod(u, v, p=None):
    a=u[:]
    if p is not None:a=[x%p for x in a];v=[x%p for x in v]
    while len(a)>1 and a[-1]==0:a.pop()
    while len(a)>=len(v):
        if p is None:
            assert v[-1]==1
            mult=a[-1]
        else:mult=a[-1]*pow(v[-1],-1,p)%p
        off=len(a)-len(v)
        for i,c in enumerate(v):
            a[off+i]-=mult*c
            if p is not None:a[off+i]%=p
        while len(a)>1 and a[-1]==0:a.pop()
        if len(a)==1 and a[0]==0:break
    return a

def polynomial_source_checks():
    assert sum(N)==864
    assert sum(v*(-1)**i for i,v in enumerate(N))==32
    assert poly_mod(N,[1,0,1])==[-12]
    assert poly_mod(N,[1,1,1])==[0,6]
    for p,expected in [
        (2,mul_poly(pow_poly([1,1],4),[1,1,1])),
        (3,mul_poly(pow_poly([-1,1],2),pow_poly([1,0,1],3)))
    ]:
        u=[x%p for x in N];v=[x%p for x in D]
        while any(v):
            u,v=v,poly_mod(u,v,p)
        u=[x*pow(u[-1],-1,p)%p for x in u]
        target=[x%p for x in expected]
        while len(target)>1 and target[-1]==0:target.pop()
        assert u==target,(p,u,target)

def direct(n):
    ans=0
    for l4 in range(1,n//4+1):
        for l3 in range(l4,(n-l4)//3+1):
            for l2 in range(l3,(n-l4-l3)//2+1):
                l1=n-l4-l3-l2
                if l1>=l2:
                    x=[l1,l2,l3,l4]
                    ans+=sum(x[i]*x[j] for i in range(4) for j in range(i+1,4))
    return ans

def recurrence(nmax=110):
    a=[]
    for n in range(nmax+1):
        rhs=(N[n] if n<len(N) else 0)
        for j in range(1,min(len(D),n+1)):
            rhs-=D[j]*a[n-j]
        a.append(rhs)
    b=[direct(n) for n in range(nmax+1)]
    assert a==b,(next((i for i in range(len(b)) if a[i]!=b[i]),None))
    return a

def wrong_table_witnesses():
    a=[]
    for n in range(1247):
        value=(N[n] if n<len(N) else 0)
        value-=sum(D[j]*a[n-j] for j in range(1,min(n+1,len(D))))
        a.append(value)
    assert a[0]==0
    assert a[1150]%10==2
    assert a[1246]%18==6
    return a[1150]%10, a[1246]%18

def certify_lifts():
    assert period_divisibility(48,2)
    assert period_divisibility(54,3)
    assert period_divisibility(96,4)
    assert period_divisibility(108,3)
    assert not period_divisibility(54,9)
    for p,t,coordinate,k in [(2,48,1,1),(2,96,1,2),(3,108,0,1)]:
        mod=p**(k+1)
        r=ring_pow(t,mod);r[0]=(r[0]-1)%mod
        z=ring_mul(N+[0]*(K-len(N)),r,mod)
        assert all(v%(p**k)==0 for v in z)
        assert z[coordinate]//(p**k)%p==1,(p,t,coordinate,z[coordinate])
    assert period_divisibility(108,3) # q^108 itself equals 1 modulo 3
    r=ring_pow(108,3);r[0]=(r[0]-1)%3
    assert not any(r)
    r=ring_pow(96,4);r[0]=(r[0]-1)%4
    assert not any(r)

if __name__=='__main__':
    generating_identity()
    polynomial_source_checks()
    a=recurrence()
    certify_lifts()
    periods=exact_order_tests()
    print('EXACT_GENERATING_IDENTITY_OK via 14 gap-variable monomials')
    print('RESULTANTS_AND_MODULAR_GCDS_OK: 864,32,144,36 and primes 2,3')
    print('WEIGHTED_FOUR_PART_GENERATING_FUNCTION_CHECK OK n=0..110; a(4)=%s; a(20)=%s; a(100)=%s'%(a[4],a[20],a[100]))
    print('MODULAR_RING_CERTIFICATES OK; D degree %d, N degree %d'%(len(D)-1,len(N)-1))
    print('MINIMAL_PERIODS_FINITE_CHECK OK',sorted(periods.items()))
    c1,c2=wrong_table_witnesses()
    print('TABLE_DISCREPANCY_WITNESSES a(0)=0; a(1150) mod 10=%s; a(1246) mod 18=%s'%(c1,c2))
