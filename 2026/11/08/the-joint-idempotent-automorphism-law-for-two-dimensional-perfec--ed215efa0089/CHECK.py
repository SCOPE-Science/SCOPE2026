"""Exact finite-field checks for a joint invariant of dimension-two evolution algebras."""
from collections import Counter
from math import gcd


def field(p, modpoly=None):
    degree = (len(modpoly) - 1) if modpoly is not None else 1
    q = p ** degree
    def digs(a):
        return [(a // p ** i) % p for i in range(degree)]
    def code(v):
        return sum((x % p) * p ** i for i, x in enumerate(v[:degree]))
    add = [[code([x+y for x,y in zip(digs(a),digs(b))]) for b in range(q)] for a in range(q)]
    mul = []
    for a in range(q):
        row = []
        for b in range(q):
            va,vb = digs(a),digs(b)
            prod=[0]*(2*degree-1)
            for i,x in enumerate(va):
                for j,y in enumerate(vb):
                    prod[i+j]=(prod[i+j]+x*y)%p
            if modpoly:
                for z in range(2*degree-2,degree-1,-1):
                    t=prod[z]
                    for j in range(degree):
                        prod[z-degree+j]=(prod[z-degree+j]-t*modpoly[j])%p
            row.append(code(prod))
        mul.append(row)
    assert all(len(set(mul[a]))==q for a in range(1,q))
    return q,add,mul


def expected(q,p,deg):
    s=(q-1)**2
    L=q*(q-1)**2*(q+1)
    h=s*(q-1) if p!=2 else 0
    g=gcd(3,q-1)
    r=1 if p==2 else 2
    if p==2:
        R=q//2-int(deg%2==0)
    else:
        R=(q-1)//2-int(q%4==1)-int(g==3)
    assert 0<=R<=q-r
    out=Counter()
    out[(2,3)]=s*R
    out[(2,1)]=s*(q-r-R)
    if g==1:
        out[(2,1)]+=s
    else:
        out[(3,0)]=2*s//3
        out[(6,3)]=s//3
    marg=[L//3,(L-h)//2,h,(L-3*h)//6]
    for k,count in enumerate(marg):
        out[(1,k)]=count-sum(n for (order,j),n in out.items() if j==k and order!=1)
        assert out[(1,k)]>=0
    assert sum(out.values())==L
    return {x:y for x,y in out.items() if y}


def actual(q,add,mul):
    nz=range(1,q)
    sq=[mul[x][x] for x in range(q)]
    out=Counter()
    for a in range(q):
      for b in range(q):
       for c in range(q):
        for d in range(q):
         # A is invertible exactly when ad and bc are different (all fields).
         if mul[a][d]==mul[b][c]:
          continue
         # Idempotent multiplication uses squares of coordinates.
         K=0
         for x in range(q):
          for y in range(q):
           if x==y==0:
            continue
           if add[mul[a][sq[x]]][mul[c][sq[y]]]==x and add[mul[b][sq[x]]][mul[d][sq[y]]]==y:
            K+=1
         # Enumerate *every* monomial automorphism independently.
         autom=0
         for x in nz:
          x2=sq[x]
          for y in nz:
           y2=sq[y]
           if mul[a][x2]==mul[a][x] and mul[b][x2]==mul[b][y] and mul[c][y2]==mul[c][x] and mul[d][y2]==mul[d][y]:
            autom+=1
           if mul[c][x2]==mul[b][y] and mul[d][x2]==mul[a][x] and mul[a][y2]==mul[d][y] and mul[b][y2]==mul[c][x]:
            autom+=1
         assert autom in (1,2,3,6)
         out[(autom,K)]+=1
    return dict(out)


def main():
    configs=[(2,None),(3,None),(2,[1,1,1]),(5,None),(7,None),
             (2,[1,1,0,1]),(3,[1,0,1]),(11,None),(13,None)]
    for p,poly in configs:
        deg=len(poly)-1 if poly else 1
        q,add,mul=field(p,poly)
        predicted=expected(q,p,deg)
        observed=actual(q,add,mul)
        assert observed==predicted,(q,observed,predicted)
        print(f'q={q}: exact joint histogram {sorted(observed.items())}; matches')
    for p,degree in [(2,4),(2,6),(2,8),(3,2),(3,3),(5,1),(7,1),(13,1),(19,1)]:
        q=p**degree
        result=expected(q,p,degree)
        assert all(v>=0 for v in result.values())
        assert sum(v for (_,k),v in result.items() if k==0)==q*(q-1)**2*(q+1)//3
    print('VERIFY_OK')

if __name__=='__main__':
    main()
