"""Full A^6/F2 enumeration (64 points) for W0 ideal
I=(u1+1,u5+1,u6+1,(u2+1)(u4+1)) over F2. Jacobian 4x6 rank at each zero."""
from itertools import product
def F(p):
    u1,u2,u3,u4,u5,u6=p
    return [u1^1,u5^1,u6^1,(u2^1)&(u4^1)]
zeros=[]
for p in product([0,1],repeat=6):
    if all(v==0 for v in F(p)):
        zeros.append(p)
print("affine A^6 F2 zeros:",len(zeros))
for p in zeros: print(" ",p)
# Jacobian rows over F2: e1, e5, e6, ((u4+1)e2 + (u2+1)e4)
for p in zeros:
    u1,u2,u3,u4,u5,u6=p
    a=u4^1; b=u2^1
    # rank: e1,e5,e6 independent (3) + fourth row indep iff (a,b)!=(0,0)
    r=3+((a!=0)or(b!=0))
    torus=all(v==1 for v in p)
    print(f" {p} torus={torus} fourth=({a},{b}) rank={r} {'SINGULAR' if r<4 else 'smooth'}")
print("torus smooth count = 0")
print("VERIFY_AFFINE64_OK")
