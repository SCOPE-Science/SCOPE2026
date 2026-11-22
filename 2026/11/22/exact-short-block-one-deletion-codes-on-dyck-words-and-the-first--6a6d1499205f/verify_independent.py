#!/usr/bin/env python3
"""Independent bit-mask and exact-fraction reconstruction of certificate tables."""
import itertools, json
from fractions import Fraction
from pathlib import Path

def all_paths(n):
    result=[]
    for pos in itertools.combinations(range(2*n),n):
        x=sum(1<<(2*n-1-i) for i in pos)
        h=0
        for j in range(2*n-1,-1,-1):
            h+=1 if x>>j&1 else -1
            if h<0:break
        else:result.append(x)
    return result

def dropbit(x,n,j):
    # j counts from the most significant source bit; return integer encoding
    # of the remaining 2*n-1 bits, with no special end markers.
    m=2*n
    hi=x>>(m-j)
    lo=x&((1<<(m-j-1))-1)
    return (hi<<(m-j-1))|lo

def readset(x,n):
    return {dropbit(x,n,j) for j in range(2*n)}

def decode(word):
    return int(word,2)

a=json.loads((Path(__file__).resolve().parent/'certificates.json').read_text(encoding='utf-8'))
expected={(1,1),(2,1),(3,2),(4,4),(5,9),(6,24)}
for n in range(1,7):
    words=all_paths(n); s=set(words)
    balls={x:readset(x,n) for x in words}
    outputs=set().union(*balls.values())
    data=a[str(n)]
    code=[decode(x) for x in data['code']]
    assert len(code)==len(set(code)) and set(code)<=s
    for i,x in enumerate(code):
        for y in code[i+1:]:assert balls[x].isdisjoint(balls[y])
    weights={decode(k):Fraction(v) for k,v in data['fractional_primal'].items()}
    covers={decode(k):Fraction(v) for k,v in data['fractional_dual'].items()}
    assert set(weights)<=s and set(covers)<=outputs
    left=[sum((weights.get(x,0) for x in words if y in balls[x]),Fraction(0)) for y in outputs]
    right=[sum((covers.get(y,0) for y in balls[x]),Fraction(0)) for x in words]
    assert all(v<=1 for v in left) and all(v>=1 for v in right)
    total=sum(weights.values(),Fraction(0))
    assert total==sum(covers.values(),Fraction(0))
    assert (n,len(code)) in expected and len(code)==total.numerator//total.denominator
    print(n,len(words),len(outputs),len(code),str(total))
assert Fraction(29,3)>9
print('INDEPENDENT_DYCK_OK')
