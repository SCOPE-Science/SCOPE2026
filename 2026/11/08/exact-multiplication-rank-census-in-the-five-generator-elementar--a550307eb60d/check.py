#!/usr/bin/env python3
"""Direct finite-field multiplication-rank checks in a five-variable square-zero algebra.
All assertions concern original multiplication matrices, not the classification routines.
"""
from collections import Counter
from itertools import combinations
from random import Random

N=5
DIM=1<<N
DEG=[i.bit_count() for i in range(DIM)]
MASKS={d:[i for i in range(DIM) if DEG[i]==d] for d in range(6)}
COMPLEMENT=[[(a,b,a|b) for a in range(DIM) if a & b == 0] for b in range(DIM)]


def rank2_from_bits(f):
    columns=[0]*DIM
    while f:
        bit=f & -f; b=bit.bit_length()-1; f-=bit
        for a,_,c in COMPLEMENT[b]:
            columns[a] ^= 1<<c
    piv={}
    for x in columns:
        while x:
            top=x.bit_length()-1
            if top in piv:x^=piv[top]
            else:
                piv[top]=x;break
    return len(piv)


def gf_mul(x,y,q):
    if q==2:return x & y
    # q=4 with alpha^2=alpha+1, binary representation.
    p=0
    for i in range(2):
        if (y>>i)&1:p^=x<<i
    if p&8:p^=0b1100
    if p&4:p^=0b111
    return p


def rankq(v,q):
    columns=[]
    for a in range(DIM):
        col=[0]*DIM
        for b in range(DIM):
            if a&b==0:col[a|b]^=v[b]
        columns.append(col)
    pivots={}
    for col in columns:
        while any(col):
            i=next(j for j,x in enumerate(col) if x)
            if i not in pivots:
                inverse=next(t for t in range(1,q) if gf_mul(col[i],t,q)==1)
                pivots[i]=[gf_mul(x,inverse,q) for x in col]
                break
            factor=col[i]
            col=[x^gf_mul(factor,y,q) for x,y in zip(col,pivots[i])]
    return len(pivots)


def polynomial_components(q):
    # Gaussian binomial [5 choose 2]_q = (q^2+1)(q^4+q^3+q^2+q+1).
    gauss52=(q*q+1)*(q**4+q**3+q*q+q+1)
    n2=(q-1)*gauss52
    n4=q**10-1-n2
    return {
      0:1,
      1:q-1,
      2:(q**5-1)*q,
      4:n2*q**6,
      6:n4*q**6,
      8:n2*q**15,
      10:n2*(q-1)*q**15,
      12:n4*q**16,
      16:(q**5-1)*q**26,
      32:(q-1)*q**31,
    }


def one(m):return 1<<m


def exhaustive_quadratic_representative(q2_mask,target):
    # All 2^16 higher-degree coefficients for a fixed quadratic 2-form.
    high=MASKS[3]+MASKS[4]+MASKS[5]
    observed=Counter()
    for k in range(1<<len(high)):
        f=q2_mask
        for i,b in enumerate(high):
            if (k>>i)&1:f^=1<<b
        observed[rank2_from_bits(f)]+=1
    assert observed==target, (q2_mask,observed,target)
    return observed


def q3_reps():
    # cde is decomposable, abc+ade has alternating dual rank four.
    return one(0b00111), one(0b00111)^one(0b11001)


def run():
    p2=one(0b00011)
    p4=p2^one(0b01100)
    c=exhaustive_quadratic_representative(p2,Counter({8:2**15,10:2**15}))
    print('F2_QUAD_RANK2_ALL_65536',sorted(c.items()))
    c=exhaustive_quadratic_representative(p4,Counter({12:2**16}))
    print('F2_QUAD_RANK4_ALL_65536',sorted(c.items()))
    q3a,q3b=q3_reps()
    high=MASKS[4]+MASKS[5]
    for f3,expected in [(q3a,4),(q3b,6)]:
        found=Counter()
        for k in range(1<<len(high)):
            f=f3
            for i,b in enumerate(high):
                if (k>>i)&1:f^=1<<b
            found[rank2_from_bits(f)]+=1
        assert found=={expected:64},(f3,found)
        print('F2_CUBIC_REP_ALL_64',hex(f3),expected)
    # Every quadratic and cubic form over F2 is independently classified
    # through alternating-matrix rank and tested with zero higher terms.
    def alternating_rank(v):
        matrix=[[0]*N for _ in range(N)]
        for a in MASKS[2]:
            if v[a]:
                i,j=[i for i in range(N) if a>>i&1]
                matrix[i][j]=matrix[j][i]=1
        # elimination over GF2
        rows=[sum(matrix[i][j]<<j for j in range(N)) for i in range(N)]
        piv={}
        for row in rows:
            while row:
                i=row.bit_length()-1
                if i in piv:row^=piv[i]
                else:piv[i]=row;break
        return len(piv)
    c=Counter()
    for k in range(1<<10):
        arr=[0]*DIM
        for i,a in enumerate(MASKS[2]):arr[a]=(k>>i)&1
        alt=alternating_rank(arr)
        f=sum(one(a) for a in MASKS[2] if arr[a])
        got=rank2_from_bits(f)
        assert got=={0:0,2:8,4:12}[alt],(k,alt,got)
        c[alt]+=1
    assert c=={0:1,2:155,4:868},c
    print('F2_ALL_1024_QUADRATIC_FORMS',sorted(c.items()))
    # Exterior duality identifies the rank of the cubic wedge map
    # with the rank of an alternating matrix defined by complementary pairs.
    cubics=Counter()
    full=(1<<N)-1
    for k in range(1<<len(MASKS[3])):
        f=sum(one(a) for i,a in enumerate(MASKS[3]) if (k>>i)&1)
        if f==0:continue
        dual=[0]*DIM
        for a in MASKS[3]:
            if (f>>a)&1:dual[full^a]=1
        alt=alternating_rank(dual)
        got=rank2_from_bits(f)
        assert got=={2:4,4:6}[alt],(k,alt,got)
        cubics[got]+=1
    assert cubics=={4:155,6:868},cubics
    print('F2_ALL_1023_NONZERO_CUBIC_FORMS',sorted(cubics.items()))
    for d,rank in [(4,2),(5,1)]:
        for k in range(1,1<<len(MASKS[d])):
            f=sum(one(a) for i,a in enumerate(MASKS[d]) if (k>>i)&1)
            assert rank2_from_bits(f)==rank
    print('F2_ALL_NONZERO_DEGREE4_AND_DEGREE5_FORMS_OK')
    # GF4 direct matrix samples including nonzero cubic obstruction.
    random=Random(71411)
    high=MASKS[3]+MASKS[4]+MASKS[5]
    for q2,which in [(p2,2),(p4,4)]:
        for index in range(80):
            v=[0]*DIM
            for a in MASKS[2]:v[a]=(q2>>a)&1
            for a in high:v[a]=random.randrange(4)
            if which==2:
                gamma=v[0b11100]
                expected=10 if gamma else 8
            else:expected=12
            got=rankq(v,4)
            assert got==expected,(which,index,gamma if which==2 else None,got,expected)
        print('F4_DIRECT_QUADRATIC_SAMPLES',which,80)
    for q in [2,4,8]:
        c=polynomial_components(q)
        assert sum(c.values())==q**32
        assert min(c)>=0
        print('FORMULA_TOTAL',q,q**32,'SUPPORT',sorted(c))
    print('ALL_DIRECT_MULTIPLICATION_RANK_CHECKS_OK')

if __name__=='__main__':run()
