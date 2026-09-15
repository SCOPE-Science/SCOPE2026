import numpy as np
print("alpha=(4-2b)/(d-2) for d>=6, 0<b<2:")
for d in [6,7,8,10,12]:
    for b in [0.01,0.5,1.0,1.5,1.99]:
        a=(4-2*b)/(d-2)
        print(f"d={d} b={b:.2f} alpha={a:.4f} C1a_only={a<1} C2={a>=1}")
print()
print("Conclusion: for all d>=6, b>0, alpha<1 strictly; as b->0+,d=6, alpha->1- .")
print("Hence F(z)=|z|^alpha z is C^{1,alpha} but NOT C^2; F''(z)~|z|^{alpha-1} blows up at 0.")
# Holder gap quantification: contraction needs Lipschitz difference of gradient
# |F'(z1)-F'(z2)| <= C(|z1|^{alpha-1}+|z2|^{alpha-1})|z1-z2| blows up near 0.
print()
print("Gradient-difference blowup: |F'(z1)-F'(z2)|/|z1-z2| ~ |z|^{alpha-1} -> inf as z->0 since alpha-1<0.")
for a in [0.9,0.5,0.25]:
    for z in [1e-1,1e-2,1e-3,1e-4]:
        print(f"alpha={a} |z|^{{alpha-1}} at z={z:g}: {z**(a-1):.2e}")
