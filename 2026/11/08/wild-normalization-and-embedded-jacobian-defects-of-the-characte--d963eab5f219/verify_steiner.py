"""Exact checks for a characteristic-two quartic Steiner surface."""
from itertools import product

IRREDUCIBLE={1:0b11,2:0b111,3:0b1011,4:0b10011}

def mul(a,b,n):
    p=IRREDUCIBLE[n]; m=(1<<n)-1; o=0
    while b:
        if b&1:o^=a
        b>>=1; a<<=1
        if a&(1<<n): a^=p
    return o&m

def square(a,n): return mul(a,a,n)

def norm(v,n):
    # first nonzero entry to 1
    q=1<<n
    for a in v:
        if a:
            inv=next(z for z in range(1,q) if mul(a,z,n)==1)
            return tuple(mul(x,inv,n) for x in v)
    raise ValueError('zero vector')

def f(point,n):
    w,x,y,z=point
    prod=mul(mul(x,y,n),z,n)
    Q=mul(x,y,n)^mul(x,z,n)^mul(y,z,n)
    return mul(w,prod,n)^square(Q,n)

def gen_projective(n,count):
    q=1<<n
    for i in range(count):
        for rest in product(range(q),repeat=count-i-1):
            yield (0,)*i+(1,)+rest

def check(n):
    q=1<<n
    points=set(gen_projective(n,4))
    surface={p for p in points if f(p,n)==0}
    expected=q*q+q+2
    assert len(surface)==expected,(q,len(surface),expected)
    singular={p for p in surface if (mul(mul(p[1],p[2],n),p[3],n)==0 and
       mul(mul(p[0],p[2],n),p[3],n)==0 and
       mul(mul(p[0],p[1],n),p[3],n)==0 and
       mul(mul(p[0],p[1],n),p[2],n)==0)}
    target_sing={p for p in points if sum(int(t!=0) for t in p[1:])<=1}
    assert singular==target_sing
    im=[]
    for a,b,c in gen_projective(n,3):
        w=square(a,n)^square(b,n)^square(c,n)
        x=mul(b,c,n);y=mul(a,c,n);z=mul(a,b,n)
        p=norm((w,x,y,z),n)
        assert p in surface
        im.append(p)
    assert len(im)==q*q+q+1
    # The parameterized geometric normalization need not surject on F_q-points.
    assert len(set(im).difference(singular))==len(surface.difference(singular))
    # A point is missed precisely when it is on an axis and t^2+wt+1 irreducible.
    missing=surface-set(im)
    line_sizes=[]
    for var in (1,2,3):
        this={p for p in missing if p[var]!=0}
        line_sizes.append(len(this))
    assert len(missing)==3*(q//2), (q,len(missing))
    print(f'q={q}: X_points={len(surface)}, normalization_points={len(im)}, geometric_singular_Fq={len(singular)}, image_Fq={len(set(im))}, missing_axis_points={len(missing)}')

for n in range(1,5): check(n)
print('STEINER_CHAR2_EXACT_CHECKS_PASSED')
