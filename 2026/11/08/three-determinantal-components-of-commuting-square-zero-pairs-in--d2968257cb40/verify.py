#!/usr/bin/env python3
"""Direct enumerator for commuting square-zero 4x4 strict upper-triangular matrices.

Uses encoded six-entry matrices (a,b,c,d,e,f) and verifies the two
rank-one determinantal models over prime fields and GF(4).
"""
from itertools import product

def field(q):
    if q == 4:
        # F2[z]/(z^2+z+1), encoded in the basis (1,z).
        def mul(x,y):
            z = 0
            for i in range(2):
                for j in range(2):
                    if ((x>>i)&1) and ((y>>j)&1): z ^= 1 << (i+j)
            if z&4: z ^= 7
            return z
        return (lambda x,y:x^y),mul, (lambda x: x)
    return (lambda x,y:(x+y)%q), (lambda x,y:(x*y)%q), (lambda x: (-x)%q)

def run(q):
    add,mul,neg=field(q)
    sub=lambda x,y: add(x,neg(y))
    sq=lambda a,b,c,d,e,f: mul(a,d)==0 and mul(d,f)==0 and add(mul(a,e),mul(b,f))==0
    elts=[z for z in product(range(q),repeat=6) if sq(*z)]
    raw={"all":0,"main":0,"row":0,"column":0,"intersection":0}
    for x in elts:
        a,b,c,d,e,f=x
        for y in elts:
            A,B,C,D,E,F=y
            if sub(mul(a,D),mul(A,d)) !=0 or sub(mul(d,F),mul(D,f))!=0 or sub(add(mul(a,E),mul(b,F)),add(mul(A,e),mul(B,f)))!=0:
                continue
            raw['all']+=1
            main=(a==f==A==F==0)
            # determinants of vertical concatenation of M and N: all 4 rows proportional.
            rows=[(a,b),(neg(f),e),(A,B),(neg(F),E)]
            row= all(sub(mul(r[0],s[1]),mul(r[1],s[0]))==0 for r in rows for s in rows)
            # horizontal concatenation [M|S N]: both 4-entry rows proportional.
            cols1=(a,b,A,B)
            cols2=(neg(f),e,F,neg(E))
            column=all(sub(mul(z,w),mul(v,u))==0 for i,z in enumerate(cols1) for j,u in enumerate(cols1) if i<j for v,w in [(cols2[i],cols2[j])])
            assert main or row or column, ('uncovered',x,y)
            assert d==D==0 or main
            raw['main']+=bool(main)
            raw['row']+=bool(row and d==D==0)
            raw['column']+=bool(column and d==D==0)
            raw['intersection']+=bool(row and column and d==D==0)
    formula=q**8+2*q**7-2*q**5
    assert raw['all']==formula,(q,raw,formula)
    assert raw['main']==q**8
    assert raw['row']==q**2*(q**5+q**4-q)
    assert raw['column']==raw['row']
    assert raw['intersection']==q**2*(q**4+2*q**3-2*q)
    print('field_size=',q,'square_zero_single=',len(elts),'commuting_pairs=',raw['all'], 'components=',(raw['main'],raw['row'],raw['column']),'subcomponent_intersection=',raw['intersection'])

if __name__=='__main__':
    for q in (2,3,4,5):run(q)
    print('ALL_STRICT_UPPER4_COMMUTING_SQUARE_ZERO_CHECKS_PASS')
