"""Independent brute-force projective enumeration over F49=F7[i]/(i^2+1)."""
P=7
def mul(a,b):
    x,y=divmod(a,P);z,w=divmod(b,P)
    return ((x*z-y*w)%P)*P+((x*w+y*z)%P)
def pw(a,e):
    r=7 # representation a=7*x+y, so 1=7
    while e:
        if e&1:r=mul(r,a)
        a=mul(a,a);e//=2
    return r
powers=[pw(a,6) for a in range(49)]
def linear(a,b,c,x,y,z):
    # a,b,c are base field coefficients, values encoded a=7*u+v
    return ((a*(x//7)+b*(y//7)+c*(z//7))%7==0 and
            (a*(x%7)+b*(y%7)+c*(z%7))%7==0)
for co,expected in [((1,1,5),42),((1,2,4),36)]:
    a,b,c=co
    # All points [x:y:1], [x:1:0], and [1:0:0], once each.
    affine=sum(linear(a,b,c,powers[x],powers[y],7) for x in range(49) for y in range(49))
    inf=sum(linear(a,b,c,powers[x],7,0) for x in range(49))
    last=1 if linear(a,b,c,7,0,0) else 0
    count=affine+inf+last
    assert affine==36 and inf==(6 if a==1 and b==1 else 0) and last==0
    assert count==expected, (co,count)
    print('VERIFY_POINT_COUNT',co,'affine=',affine,'infinity=',inf,'total=',count)
print('VERIFY_PROJECTIVE_OK')
