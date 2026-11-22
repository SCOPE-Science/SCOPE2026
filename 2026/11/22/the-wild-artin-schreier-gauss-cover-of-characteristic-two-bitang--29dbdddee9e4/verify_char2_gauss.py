"""Independent small-field checks of the Gauss-contact splitting formula.

Pure Python polynomial-basis arithmetic; exhaustive for fields of orders 2, 4,
8, and a deterministic sample for order 16. The proof is algebraic and is
independent of these finite checks.
"""
import itertools

MOD = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}

def mul(x,y,m):
    mask=(1<<m)-1
    red=MOD[m]&mask
    z=0
    while y:
        if y&1: z^=x
        y>>=1
        carry=x&(1<<(m-1))
        x=(x<<1)&mask
        if carry: x^=red
    return z

def pw(x,n,m):
    y=1
    while n:
        if n&1:y=mul(y,x,m)
        x=mul(x,x,m);n>>=1
    return y

def trace(x,m):
    y=0
    for _ in range(m):
        y^=x;x=mul(x,x,m)
    assert y in (0,1)
    return y

def check(m, sample=1):
    q=1<<m; checked=0
    roots4={pw(v,4,m):v for v in range(q)}
    for a,b,c,d in itertools.product(range(q),repeat=4):
        if b==0 or (a*17+b*19+c*23+d*29)%sample:continue
        b2=mul(b,b,m)
        delta=mul(a,b2,m)^mul(c,c,m)^1
        if not delta:continue
        invb=pw(b,q-2,m)
        lam=roots4[mul(delta,pw(invb,4,m),m)]
        assert pw(lam,4,m)==mul(delta,pw(pw(b,q-2,m),4,m),m)
        D=mul(d,pw(pw(b,q-2,m),2,m),m)
        split=0;nonsplit=0
        for t in list(range(1,q))+[None]:
            if t is None:
                predicted=(trace(D,m)==0)
                actual=sum((pw(y,4,m)^mul(b,pw(y,2,m),m)^d)==0 for y in range(q))
            else:
                invt=pw(t,q-2,m)
                predicted=(trace(D^mul(lam,invt,m),m)==0)
                e= a^mul(c,pw(t,2,m),m)^mul(b,pw(t,3,m),m)^mul(d,pw(t,4,m),m)
                actual=sum((pw(y,4,m)^mul(b,mul(pw(t,2,m),pw(y,2,m),m),m)^e)==0 for y in range(q))
            assert actual==(2 if predicted else 0),(q,a,b,c,d,t,actual,predicted)
            if predicted:split+=1
            else:nonsplit+=1
        assert (split,nonsplit)==(q//2,q//2),(q,a,b,c,d,split,nonsplit)
        checked+=1
    print('GF',q,'INTEGRAL_PARAMETERS_TESTED',checked,'SPLIT_LINES',q//2,'NONSPLIT_LINES',q//2)

for m in (1,2,3):check(m)
check(4,sample=103)
print('GAUSS_CONTACT_SPLITTING_VERIFIED')
