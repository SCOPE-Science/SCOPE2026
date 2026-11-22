"""Direct finite checks for free class-three and class-four rank-two Lie retractions."""
from itertools import product
from collections import Counter
from math import prod

# Basis x,y,[x,y],[x,[x,y]],[y,[x,y]]; in class four add
# [x,[x,[x,y]]],[x,[y,[x,y]]],[y,[y,[x,y]]].
def bracket(a,b,p,c):
    s=lambda i,j:(a[i]*b[j]-a[j]*b[i])%p
    out=[0,0,s(0,1),s(0,2),s(1,2)]
    if c==4: out.extend([(s(0,3))%p,(s(0,4)+s(1,3))%p,s(1,4)])
    return tuple(out)

def rank2(a,b,p):
    return 2 if (a[0]*b[1]-a[1]*b[0])%p else 1 if (a[0] or a[1] or b[0] or b[1]) else 0

def check(c,p):
    d={3:5,4:8}[c]
    vectors=list(product(range(p),repeat=d))
    ct=Counter()
    for a in vectors:
        for b in vectors:
            z=bracket(a,b,p,c);u=bracket(a,z,p,c);v=bracket(b,z,p,c)
            images=[a,b,z,u,v]
            if c==4:
                images.extend((bracket(a,u,p,c),bracket(a,v,p,c),bracket(b,v,p,c)))
            def F(w):
                return tuple(sum(w[j]*images[j][i] for j in range(d))%p for i in range(d))
            if F(a)==a and F(b)==b:
                ct[rank2(a,b,p)]+=1
    expect={0:1,1:(p+1)*p**(d-1),2:1}
    assert ct==expect,(c,p,ct,expect)
    print(f'PASS c={c}, d=2, q={p}: '+str(dict(sorted(ct.items())))+f'; all {p**(2*d)} generator assignments checked')

if __name__=='__main__':
    for c,p in [(3,2),(3,3),(4,2)]:check(c,p)
