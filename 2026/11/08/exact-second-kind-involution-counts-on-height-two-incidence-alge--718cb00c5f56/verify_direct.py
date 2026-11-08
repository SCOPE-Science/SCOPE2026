"""Independent exhaustive two-vertex-chain check of all semilinear anti-automorphisms.
Only the primitive-idempotent image constraint and a nonzero arrow image are used.
"""
for p in (2,3):
    Q=p*p
    def add(a,b):return (a%p+b%p)%p+p*((a//p+b//p)%p)
    def neg(a):return (-a%p)+p*(-(a//p)%p)
    def mul(a,b):
        a0,a1=a%p,a//p; b0,b1=b%p,b//p
        if p==2:return (a0*b0+a1*b1)%p+p*((a0*b1+a1*b0+a1*b1)%p)
        return (a0*b0-a1*b1)%p+p*((a0*b1+a1*b0)%p)
    def exp(x,k):
        out=1
        for _ in range(k):out=mul(out,x)
        return out
    star=lambda a:exp(a,p)
    # e_0=(1,0,0), e_1=(0,1,0), E=(0,0,1).
    def prod(x,y):return (mul(x[0],y[0]),mul(x[1],y[1]),add(mul(x[0],y[2]),mul(x[2],y[1])))
    def plu(x,y):return tuple(add(a,b) for a,b in zip(x,y))
    zero=(0,0,0); basis=((1,0,0),(0,1,0),(0,0,1))
    passed=0
    for a in range(Q):
      for c in range(1,Q):
        images=((0,1,a),(1,0,neg(a)),(0,0,c))
        def apply(x):
            y=zero
            for k in range(3):
                z=tuple(mul(star(x[k]),t) for t in images[k]);y=plu(y,z)
            return y
        valid=all(apply(apply(x))==x for x in basis)
        valid=valid and all(apply(prod(x,y))==prod(apply(y),apply(x)) for x in basis for y in basis)
        if valid:passed+=1
    assert passed==p*(p+1),(p,passed)
    print(f'F_{Q}: independently tested {Q*(Q-1)} semilinear anti-automorphisms; exactly {passed} square to identity')
print('VERIFY_OK')
