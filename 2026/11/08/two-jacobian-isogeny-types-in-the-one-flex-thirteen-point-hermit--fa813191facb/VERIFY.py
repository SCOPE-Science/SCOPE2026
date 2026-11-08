"""Exact finite-field certificate for three Hermitian-relative plane quartics.
Only standard-library Python; exhaustive field and point enumeration.
"""

def a9(x,y):
    return ((x%3+y%3)%3)+3*((x//3+y//3)%3)

def n9(x):
    return (-(x%3))%3+3*((-(x//3))%3)

def m9(x,y):
    a,b=x%3,x//3
    c,d=y%3,y//3
    return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)

def a81(x,y):
    return a9(x%9,y%9)+9*a9(x//9,y//9)

def n81(x):
    return n9(x%9)+9*n9(x//9)

def m81(x,y):
    a,b=x%9,x//9
    c,d=y%9,y//9
    return a9(m9(a,c),m9(4,m9(b,d)))+9*a9(m9(a,d),m9(b,c))

def coeff729(x):
    return (x%9,(x//9)%9,x//81)

def a729(x,y):
    xx,yy=coeff729(x),coeff729(y)
    return sum((9**i)*a9(xx[i],yy[i]) for i in range(3))

def n729(x):
    xx=coeff729(x)
    return sum((9**i)*n9(xx[i]) for i in range(3))

def m729(x,y):
    xx,yy=coeff729(x),coeff729(y)
    p=[0]*5
    for i in range(3):
        for j in range(3):
            p[i+j]=a9(p[i+j],m9(xx[i],yy[j]))
    # If u^3=u+1, then u^4=u^2+u.
    return a9(p[0],p[3])+9*a9(a9(p[1],p[3]),p[4])+81*a9(p[2],p[4])

def power(x,k,mul):
    acc=1
    while k:
        if k&1: acc=mul(acc,x)
        x=mul(x,x)
        k>>=1
    return acc

# Check polynomial moduli define fields; 4=1+i is nonsquare in F9;
# s^3-s-1 has no F9 root, hence irreducible.
assert {m9(v,v) for v in range(9)} == {0,1,2,3,6}
assert 4 not in {m9(v,v) for v in range(9)}
assert all(a9(a9(power(v,3,m9),n9(v)),n9(1))!=0 for v in range(9))
for q,mul in ((9,m9),(81,m81),(729,m729)):
    assert all(power(v,q-1,mul)==1 for v in range(1,q))

FIELDS=((9,a9,n9,m9),(81,a81,n81,m81),(729,a729,n729,m729))
results={}
for q,add,neg,mul in FIELDS:
    cubes=[power(x,3,mul) for x in range(q)]
    bycube={}
    for x,val in enumerate(cubes): bycube.setdefault(val,[]).append(x)
    for c in (range(1,9) if q==9 else (2,4,7)):
        # x^3-c(y^3-1)x-y=0. All points at z=0 are
        # [1:0:0] and [0:1:0], independent of c.
        hist={0:0,1:0,3:0}
        affine=[]
        for y in range(q):
            beta=mul(c,add(cubes[y],neg(1)))
            roots=[]
            for x in range(q):
                if add(add(cubes[x],neg(mul(beta,x))),neg(y))==0:
                    roots.append(x)
            assert len(roots) in hist
            hist[len(roots)]+=1
            if q==9: affine.extend((x,y) for x in roots)
        N=2+sum(k*v for k,v in hist.items())
        results[(q,c)]=(N,hist)
        print('POINTS',q,c,N,'fibre_hist',hist)
        if q==9:
            flex=[]
            for x,y in affine:
                aa=mul(c,add(1,neg(cubes[y])))
                # Tangency substitution has t^3 coefficient 1-c*x*aa^3.
                if add(1,neg(mul(mul(c,x),power(aa,3,mul))))==0:
                    flex.append((x,y))
            # Both points at infinity have contact order exactly three.
            print('FLEX',c,len(flex),flex)
            if c in (2,4,7): assert len(flex)==1
            assert (N==13 and len(flex)==1)==(c in (2,4,7))

assert [results[(9,c)][0] for c in (2,4,7)] == [13]*3
assert [results[(81,c)][0] for c in (2,4,7)] == [109,73,73]
assert [results[(729,c)][0] for c in (2,4,7)] == [676]*3

def weil_poly(N1,N2,N3):
    # Trace of Frobenius powers on H^1, base field cardinality 9.
    s1=10-N1
    s2=82-N2
    s3=730-N3
    a1=-s1
    assert (s1*s1-s2)%2==0
    a2=(s1*s1-s2)//2
    assert (s3+a1*s2+a2*s1)%3==0
    a3=-(s3+a1*s2+a2*s1)//3
    # Genus-three functional equation a_(6-i)=9^(3-i) a_i.
    return (1,a1,a2,a3,9*a2,81*a1,729)

p2=weil_poly(13,109,676)
p4=weil_poly(13,73,676)
assert p2==(1,3,18,27,162,243,729)
assert p4==(1,3,0,-27,0,243,729)

def multpoly(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return tuple(r)
assert p2==multpoly(multpoly((1,-3,9),(1,3,9)),(1,3,9))
assert p4==multpoly((1,3,9),(1,0,-9,0,81))
assert sum(p2)==1183
assert sum(p4)==949
# T^4-9T^2+81 irreducible over Q. If it factors into two
# quadratics (T^2+aT+b)(T^2-aT+d), then a(d-b)=0,
# bd=81 and b+d-a^2=-9; neither a=0 nor b=d admits a rational a,b,d.
# For a=0, b,d solve U^2+9U+81=0 (discriminant -243).
# For b=d=9 or -9, a^2=27 or -9, neither rational square.
print('WEIL',p2,p4)
print('JACOBIAN_ORDERS',sum(p2),sum(p4))
print('VERIFY_OK')
