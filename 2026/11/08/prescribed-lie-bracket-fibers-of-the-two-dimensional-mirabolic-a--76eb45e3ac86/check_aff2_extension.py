"""Independent GF(4) verification using explicit polynomial arithmetic and image spaces."""
from itertools import product
from collections import Counter

q=4

def add(x,y): return x^y
def mul(a,b):
    c=0
    while b:
        if b&1: c^=a
        b>>=1; a<<=1
        if a&4: a^=7
    return c

def eqz(x): return x==0

def bracket(A,B):
    a,b,c,d=A; e,f,g,h=B
    return (add(mul(b,g),mul(f,c)),
            add(add(mul(a,f),mul(b,h)),add(mul(e,b),mul(f,d))),
            add(add(mul(c,e),mul(d,g)),add(mul(g,a),mul(h,c))),
            add(mul(c,f),mul(g,b)))

def image(A,B):
    a,b,c,d=A;e,f,g,h=B
    cols=((a,c),(b,d),(e,g),(f,h))
    v=next((v for v in cols if v!=(0,0)),None)
    if v is None: return [(0,0)]
    span={(mul(t,v[0]),mul(t,v[1])) for t in range(q)}
    w=next((w for w in cols if w not in span),None)
    if w is None:return sorted(span)
    return sorted({(add(mul(s,v[0]),mul(t,w[0])),add(mul(s,v[1]),mul(t,w[1]))) for s in range(q) for t in range(q)})

def predicted(Z,w):
    a,b,c,d=Z
    if add(a,d):return 0
    if Z==(0,0,0,0):
        if w==(0,0):return q**8+2*q**7+q**6-3*q**5-q**4+q**3
        return q**3*(q*q-1)*(q**3+q**2+q-1)
    det=add(mul(a,d),mul(b,c))
    if det:return q**5*(q*q-1)
    col=(a,c) if (a,c)!=(0,0) else (b,d)
    on_line=add(mul(col[0],w[1]),mul(col[1],w[0]))==0
    return q**3*(q*q-1)*(q*q+q-1 if on_line else q*q-1)

all4=list(product(range(q),repeat=4))
count=Counter()
for A in all4:
    for B in all4:
        Z=bracket(A,B)
        im=image(A,B)
        wt=q**(4-(0 if len(im)==1 else 1 if len(im)==q else 2))
        for v in im: count[(Z,v)]+=wt
for Z in all4:
    for w in product(range(q),repeat=2):
        a=count[Z,w]; e=predicted(Z,w)
        if a!=e:raise AssertionError((Z,w,a,e))
assert sum(count.values())==q**12
print(f'q=4 GF(4): checked all {q**8} ordered matrix pairs and {q**5} bracket targets; total {q**12} ordered affine Lie inputs')
print('AFF2_GF4_EXTENSION_FIELD_PASS')
