"""Exact, dependency-free checks for characteristic-three Ciani quartic strata."""
from itertools import product

# Sparse symbolic monomials in (x,y,z,a,b,c), over F_3.
terms = [((4,0,0,0,0,0),1),((0,4,0,0,0,0),1),
         ((0,0,4,0,0,0),1),((2,2,0,1,0,0),1),
         ((0,2,2,0,1,0),1),((2,0,2,0,0,1),1)]
F2 = {}
for m,u in terms:
    for n,v in terms:
        e=tuple(m[i]+n[i] for i in range(6))
        F2[e]=(F2.get(e,0)+u*v)%3
F2={e:v for e,v in F2.items() if v}
V=[(1,0,0),(0,1,0),(0,0,1)]
expected=[{(0,1,0):2,(1,0,1):2},
          {(0,0,1):2,(1,1,0):2},
          {(1,0,0):2,(0,1,1):2}]
for i,u in enumerate(V):
    for j,v in enumerate(V):
        xyz=tuple(3*u[k]-v[k]+2 for k in range(3))
        output={ex[3:]:coeff for ex,coeff in F2.items() if ex[:3]==xyz}
        assert output==(expected[i] if i==j else {}),(i,j,output)

# Check polynomial identities by an independent sparse polynomial representation.
def monomial(coef,exp):return {exp:coef%3}
def plus(P,Q):
    R=P.copy()
    for e,c in Q.items():R[e]=(R.get(e,0)+c)%3
    return {e:c for e,c in R.items() if c}
def mul(P,Q):
    R={}
    for e,c in P.items():
        for f,d in Q.items():
            g=tuple(e[i]+f[i] for i in range(3))
            R[g]=(R.get(g,0)+c*d)%3
    return {e:c for e,c in R.items() if c}
def scale(P,n):return {e:(c*n)%3 for e,c in P.items() if c*n%3}
one=monomial(1,(0,0,0));a=monomial(1,(1,0,0));b=monomial(1,(0,1,0));c=monomial(1,(0,0,1))
A2=mul(a,a);B2=mul(b,b);C2=mul(c,c)
delta=plus(plus(A2,B2),plus(C2,plus(scale(mul(mul(a,b),c),-1),scale(one,-1))))
hx=plus(b,mul(a,c)); hy=plus(c,mul(a,b)); hz=plus(a,mul(b,c))
def subst(P,sub):
    out={}
    for (i,j,k),co in P.items():
        term=scale(mul(mul(powpoly(sub[0],i),powpoly(sub[1],j)),powpoly(sub[2],k)),co)
        out=plus(out,term)
    return out
def powpoly(P,n):
    r=one
    for _ in range(n):r=mul(r,P)
    return r
assert subst(delta,[a,scale(mul(a,c),-1),c]) == scale(mul(plus(A2,scale(one,-1)),plus(C2,scale(one,-1))),-1)
for s in (1,-1):
    # delta on c = s equals (a + s*b)^2 in F3
    lhs=subst(delta,[a,b,scale(one,s)])
    rhs=mul(plus(a,scale(b,s)),plus(a,scale(b,s)))
    assert lhs==rhs

# Finite field F_{3^d}, represented in powers of t. For d=2: t^2+1; d=3: t^3-t+1.
def finite_field(d):
    q=3**d
    poly={1:None,2:(1,0,1),3:(1,2,0,1)}[d]
    def digs(x):
        out=[]
        for _ in range(d):out.append(x%3);x//=3
        return out
    digits=[digs(x) for x in range(q)]
    def encode(v):return sum(x*3**i for i,x in enumerate(v))
    add=[[encode([(digits[a][i]+digits[b][i])%3 for i in range(d)]) for b in range(q)] for a in range(q)]
    muls=[]
    for a0 in range(q):
        row=[]
        for b0 in range(q):
            res=[0]*(2*d-1)
            for i,x in enumerate(digits[a0]):
                for j,y in enumerate(digits[b0]):res[i+j]=(res[i+j]+x*y)%3
            if d>1:
                for k in range(2*d-2,d-1,-1):
                    v=res[k]
                    for j in range(d):res[k-d+j]=(res[k-d+j]-v*poly[j])%3
            row.append(encode(res[:d]))
        muls.append(row)
    return q,add,muls

for degree in (1,2,3):
    q,add,mul_table=finite_field(degree)
    def sm(x,y):return add[x][y]
    def mm(x,y):return mul_table[x][y]
    def sq(x):return mm(x,x)
    minus1=2
    # no zero divisors (verifies both quotient polynomials are irreducible).
    assert all(mm(x,y)!=0 for x in range(1,q) for y in range(1,q))
    count=[0,0,0,0]
    for aa,bb,cc in product(range(q),repeat=3):
        if 1 in (sq(aa),sq(bb),sq(cc)):
            continue
        # negative abc is 2*abc, using addition only
        abc=mm(mm(aa,bb),cc)
        negabc=sm(abc,abc)
        dd=sm(sm(sq(aa),sq(bb)),sm(sq(cc),sm(negabc,minus1)))
        if dd==0:continue
        h=(sm(bb,mm(aa,cc)),sm(cc,mm(aa,bb)),sm(aa,mm(bb,cc)))
        f=sum(v!=0 for v in h)
        count[f]+=1
    predicted=[1,3*(q-3),3*(q-3)*(q-5),(q-3)*(q*q-7*q+18)]
    assert count==predicted,(q,count,predicted)
    assert sum(count)==(q-2)**3-(q-3)**2
    print('GF({}): rank-stratum counts {} (verified)'.format(q,count))
print('ALL_CHECKS_PASSED')
