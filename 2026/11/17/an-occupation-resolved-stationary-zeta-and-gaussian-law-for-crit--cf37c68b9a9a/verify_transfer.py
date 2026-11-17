"""Exact weighted 2-row Critters stationary transfer calculation.

Usage: python verify_transfer.py (requires sympy).
The even and odd block moves both use the original complementing rule.
"""
import sympy as sp

u,z=sp.symbols('u z')

def block(a):
    k=a.bit_count()
    if k==2:
        return a^15 if a in (6,9) else a
    b=a^15
    if k==3:
        b=((b&1)<<3)|((b&2)<<1)|((b&4)>>1)|((b&8)>>3)
    return b

assert sorted(block(a) for a in range(16))==list(range(16))
assert all(block(a).bit_count()==4-a.bit_count() for a in range(16))

T=sp.zeros(16)
for a in range(16):
    for b in range(16):
        fa,fb=block(a),block(b)
        # odd partition crosses from right column of a to left column of b,
        # in vertical order row 1 then row 0.
        before=((fa>>3)&1)|(((fb>>2)&1)<<1)|(((fa>>1)&1)<<2)|((fb&1)<<3)
        desired=((a>>3)&1)|(((b>>2)&1)<<1)|(((a>>1)&1)<<2)|((b&1)<<3)
        T[a,b]=int(block(before)==desired)

W=sp.diag(*[u**a.bit_count() for a in range(16)])*T
Q=1-(1+u**2+u**4)*z+(u**4-u**2-u**6)*z**2-u**6*z**3
expected=(1-u**2*z)**5*Q
actual=sp.factor((sp.eye(16)-z*W).det())
assert sp.expand(expected-actual)==0
print('block bijection and population complementation: PASS')
print('transfer edges:',sum(int(q) for q in T))
print('weighted determinant exact identity: PASS')
print('factored determinant:',sp.factor(actual))
# Closed walks are labelled configurations. Enumerate exact totals independently.
for m,expect in [(2,16),(3,44),(4,136),(5,448),(6,1504),(7,5076)]:
    total=sp.trace(T**m)
    assert total==expect
    print('m=%s total=%s'%(m,total))

# The Perron root solves lambda^3 -3lambda^2-lambda-1=0.
L=sp.Symbol('L')
poly=L**3-3*L**2-L-1
roots=sp.nroots(poly,maxsteps=300)
lambda1=max(float(sp.re(x)) for x in roots)
sigma2=8*(lambda1+1)/(3*lambda1**2-6*lambda1-1)
assert 3.3829<lambda1<3.3831 and 2.6897<sigma2<2.6900
print('lambda approx %.14f; sigma^2 approx %.14f'%(lambda1,sigma2))

# Check the nonzero cyclic graph components and the weighted small-size census.
adj={a:[b for b in range(16) if T[a,b]] for a in range(16)}
def reach(a):
    found={a};front=[a]
    while front:
        for b in adj[front.pop()]:
            if b not in found:
                found.add(b);front.append(b)
    return found
r={a:reach(a) for a in range(16)}
main={0,1,2,4,6,8,9,15}
assert all(main=={b for b in range(16) if b in r[a] and a in r[b]} for a in main)
assert all(a in r[0] and 0 in r[a] for a in main)
assert 0 in adj[0]
assert {a for a in range(16) if a in adj[a] and a not in main}=={3,5,10,12}
assert all(not (a in r[b] and b in r[a]) for a in {7,11,13,14} for b in range(16) if a!=b)
print('primitive dominant SCC and four isolated loops: PASS')
expected_hists={
 2:{0:1,2:4,4:6,6:4,8:1},
 3:{0:1,2:6,4:6,6:18,8:6,10:6,12:1},
 4:{0:1,2:8,4:16,6:24,8:38,10:24,12:16,14:8,16:1},
 5:{0:1,2:10,4:30,6:50,8:90,10:86,12:90,14:50,16:30,18:10,20:1},
}
for m,hist in expected_hists.items():
    actual_hist={int(k[0]):int(coeff) for k,coeff in sp.Poly(sp.trace(W**m),u).terms()}
    assert actual_hist==hist,(m,actual_hist,hist)
print('weighted small-size histograms compared with independent direct simulator: PASS')
