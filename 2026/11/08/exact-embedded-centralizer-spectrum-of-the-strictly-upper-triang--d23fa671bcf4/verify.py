"""Independent finite-field enumeration of element centralizer row spaces for N_4."""
from collections import Counter,defaultdict
from itertools import product

PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5,7)
        self.q=q
    def add(self,x,y):
        return (x^y) if self.q==4 else (x+y)%self.q
    def neg(self,x):
        return x if self.q==4 else (-x)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        w=0
        while b:
            if b&1:w^=a
            b>>=1;a<<=1
            if a&4:a^=7  # x^2+x+1=0
        return w
    def inv(self,a):
        assert a
        for v in range(1,self.q):
            if self.mul(v,a)==1:return v
        raise ArithmeticError(a)
    def sub(self,a,b):return self.add(a,self.neg(b))

def commutator(f,x,y):
    A={(i,j):c for (i,j),c in zip(PAIRS,x)}
    B={(i,j):c for (i,j),c in zip(PAIRS,y)}
    out=[]
    for i,j in PAIRS:
        xy=0;yx=0
        for k in range(i+1,j):
            xy=f.add(xy,f.mul(A.get((i,k),0),B.get((k,j),0)))
            yx=f.add(yx,f.mul(B.get((i,k),0),A.get((k,j),0)))
        out.append(f.sub(xy,yx))
    return out

def rref(f, mat):
    rows=[row[:] for row in mat]
    r=0
    for col in range(len(rows[0])):
        pivot=next((i for i in range(r,len(rows)) if rows[i][col]),None)
        if pivot is None:continue
        rows[pivot],rows[r]=rows[r],rows[pivot]
        inv=f.inv(rows[r][col]);rows[r]=[f.mul(inv,v) for v in rows[r]]
        for j in range(len(rows)):
            if j==r or not rows[j][col]:continue
            factor=rows[j][col]
            rows[j]=[f.sub(v,f.mul(factor,w)) for v,w in zip(rows[j],rows[r])]
        r+=1
        if r==len(rows):break
    return tuple(tuple(row) for row in rows[:r])

def enumerate_q(q):
    f=Field(q)
    bucket=defaultdict(Counter)
    for a,b,d,e,g in product(range(q),repeat=5):
        x=(a,b,0,d,e,g)
        columns=[]
        for i in range(6):
            y=[0]*6;y[i]=1
            columns.append(commutator(f,x,y))
        full=[[columns[j][i] for j in range(6)] for i in range(6)]
        key=rref(f,full)
        bucket[len(key)][key]+=1
    fibers={r:Counter(d.values()) for r,d in bucket.items()}
    expected={
      0:Counter({1:1}),
      1:Counter({q-1:q+1}),
      2:Counter({q-1:q**3+q**2,q*q*(q-1):1}),
      3:Counter({q*(q-1):q**3-q}),
    }
    # In q=2 some distinct fiber sizes coincide? Here q-1 != q^2(q-1); okay.
    for r in range(4):
        assert fibers[r]==expected[r],(q,r,fibers[r],expected[r])
    count_by_rank={r:len(bucket[r]) for r in range(4)}
    assert sum(count_by_rank.values())==2*q**3+q*q+3
    assert sum(sum(d.values()) for d in bucket.values())==q**5
    # All centralizers contain E14; adjoining it to x changes nothing.
    for i in range(6):
        x=[0]*6;x[i]=1
        z=[0]*6;z[2]=1
        for j in range(6):
            y=[0]*6;y[j]=1
            assert commutator(f,x,y)==commutator(f,tuple(f.add(a,b) for a,b in zip(x,z)),y)
    print('q=',q,'distinct_by_codimension=',count_by_rank,'fibers=',{r:dict(d) for r,d in sorted(fibers.items())},'total=',sum(count_by_rank.values()))

for q in (2,3,4,5,7):enumerate_q(q)
print('VERIFY_OK_N4_CENTRALIZERS')
