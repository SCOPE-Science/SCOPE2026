"""Standard-library exact polynomial certificate for cycle connectivity-covariance formulas."""
from collections import defaultdict

checks=0

def poly(n, terms=None):
    return {tuple([0]*n): 0} if terms is None else {e:c for e,c in terms.items() if c}

def const(n,k): return {tuple([0]*n):k} if k else {}
def variable(n,j):
    e=[0]*n;e[j]=1
    return {tuple(e):1}
def add(*args):
    z=defaultdict(int)
    for a in args:
        for e,c in a.items():z[e]+=c
    return {e:c for e,c in z.items() if c}
def neg(a):return {e:-c for e,c in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    z=defaultdict(int)
    for e,c in a.items():
        for f,d in b.items():z[tuple(i+j for i,j in zip(e,f))]+=c*d
    return {e:c for e,c in z.items() if c}
def prod(args,n):
    out=const(n,1)
    for a in args:out=mul(out,a)
    return out

def connection(m,mask,x,y):
    parent=list(range(m))
    def rt(x):
        while parent[x]!=x:x=parent[x]
        return x
    for k in range(m):
        if not (mask>>k)&1: parent[rt(k)] = rt((k+1)%m)
    return rt(x)==rt(y)

for m,cases in [(2,[((0,1),(0,1))]),(3,[((0,1),(1,2))]),(4,[((0,1),(2,3)),((0,2),(1,3))])]:
    r=[variable(m,j) for j in range(m)]
    one=const(m,1)
    W=lambda mask:prod([r[j] for j in range(m) if mask>>j&1],m)
    Z=add(*(W(mask) for mask in range(1,1<<m)))
    for A,B in cases:
        a=add(*(W(mask) for mask in range(1,1<<m) if connection(m,mask,*A)))
        b=add(*(W(mask) for mask in range(1,1<<m) if connection(m,mask,*B)))
        ab=add(*(W(mask) for mask in range(1,1<<m) if connection(m,mask,*A) and connection(m,mask,*B)))
        R=sub(mul(Z,ab),mul(a,b))
        if m==2:
            expected=mul(mul(r[0],r[1]),add(r[0],r[1]))
        elif m==3:
            expected=mul(mul(r[0],r[1]),add(mul(add(r[0],r[1]),add(one,r[2])),r[2]))
        elif A==(0,1):
            expected=mul(mul(r[0],r[2]),sub(prod([add(one,r[0],r[2]),add(one,r[1]),add(one,r[3])],m),one))
        else:
            S=add(*r)
            expected=add(mul(add(mul(r[0],r[2]),mul(r[1],r[3])),add(S,mul(add(r[0],r[2]),add(r[1],r[3])))),mul(prod(r,m),add(const(m,4),S)))
        assert R==expected,(m,A,B,sub(R,expected));checks+=1
        assert all(c>=0 for c in R.values());checks+=1
        none=add(Z,ab,neg(a),neg(b))
        assert all(c>=0 for c in none.values());checks+=1
        # For any q>0 the covariance numerator equals R + q*(weight of neither event).
        # Check q=2 as a coefficientwise exact polynomial identity and q=5 for redundancy.
        for q in (2,5):
            left=sub(mul(add(Z,const(m,q)),add(ab,const(m,q))),mul(add(a,const(m,q)),add(b,const(m,q))))
            right=add(R,{e:q*c for e,c in none.items()})
            assert left==right,(m,A,B,q);checks+=1
print('PASS:',checks,'symbolic polynomial identities and coefficient-positivity checks')
