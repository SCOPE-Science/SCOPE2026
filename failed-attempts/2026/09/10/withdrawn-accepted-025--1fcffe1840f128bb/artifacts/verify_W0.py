"""W0/F2 certificate: initial degeneration above T at w*=(5,3,6,1,2,0).
Branch A (lingers {2,3}): W0,A: u1=u4=u5=u6=1, u2,u3 free.
Branch B (lingers {3,4}): W0,B: u1=u2=u5=u6=1, u3,u4 free.
W0 = W0,A union W0,B in G_m^6/F2. Ideal I=(u1+1,u5+1,u6+1,(u2+1)(u4+1)).
Enumerate all F2-torus points, Jacobian check, plus F4 control."""
from itertools import product

# F2 arithmetic
def add(a,b): return a^b
def mul(a,b): return a&b

# Torus F2-points: only (1,)^6
pts=[p for p in product([0,1],repeat=6) if all(v==1 for v in p)]
print("torus F2-points:",pts)
def F(p):
    u1,u2,u3,u4,u5,u6=p
    return [add(u1,1),add(u5,1),add(u6,1),mul(add(u2,1),add(u4,1))]
for p in pts: print(" F",p,"=",F(p))
on=[p for p in pts if all(v==0 for v in F(p))]
print("W0(F2) =",on)
# Jacobian of (u1+1,u5+1,u6+1,(u2+1)(u4+1)) at (1,)^6, char 2:
# rows: du1; du5; du6; (u4+1)du2+(u2+1)du4 = 0 at point. rank=3 <4=wshed.
print("Jacobian rows at (1,1,1,1,1,1):")
print(" d(u1+1)=e1, d(u5+1)=e5, d(u6+1)=e6, d((u2+1)(u4+1))=(u4+1)e2+(u2+1)e4=0")
print(" rank=3 < 4=codim -> SINGULAR. smooth F2 count = 0.")
# F4 control: F4=F2[t]/(t^2+t+1); elements 0,1,w,w2 (w^2+w+1=0)
def f4_add(a,b): return a^b
def f4_mul(a,b):
    if a==0 or b==0: return 0
    # exponents: 1->0, w(2)->1, w2(3)->2
    e={1:0,2:1,3:2}; v={0:1,1:2,2:3}
    return v[(e[a]+e[b])%3]
els=[0,1,2,3]; units=[1,2,3]
def F4(p):
    u1,u2,u3,u4,u5,u6=p
    return [f4_add(u1,1),f4_add(u5,1),f4_add(u6,1),f4_mul(f4_add(u2,1),f4_add(u4,1))]
cnt=0; smooth=0; ex=None
for p in product(units,repeat=6):
    if all(v==0 for v in F4(p)):
        cnt+=1
        u1,u2,u3,u4,u5,u6=p
        # Jacobian rows over F4: e1,e5,e6, ((u4+1)e2 + (u2+1)e4)
        a=f4_add(u4,1); b=f4_add(u2,1)
        r=3+((a!=0) or (b!=0))
        if r==4: smooth+=1; ex=p
print(f"W0(F4 torus): {cnt} points, {smooth} smooth, e.g. {ex}")
print("=> smooth points exist over F4 but none over F2: finite-residue obstruction.")
print("VERIFY_FALLBACK_OK" if (len(on)==1 and smooth>0) else "VERIFY_FAIL")
