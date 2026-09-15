import numpy as np
print("Tail-region remainder: W~0 (far field), f(z)=|z|^a z, R(W,v)=f(W+v)-f(W)-f'(W)v")
print("Standard DM contraction needs |R|<=C|v|^2 uniformly; test W=0 slice:")
for a in [0.75, 0.5, 0.25, 0.05]:
    row=[]
    for v in [1e-1,1e-2,1e-3,1e-4,1e-6]:
        R=abs(v)**a*v  # f(v) since W=0
        row.append(f"{abs(R)/v**2:.1e}")
    print(f"  alpha={a}: |R|/|v|^2 for v=1e-1..1e-6: {row}  (=|v|^(a-1)->inf)")
print()
print("Linearized potential decay: V=|x|^-b W^a, W~r^{-(d-2)} => V~r^{-4+b} (short-range, fine).")
print("So the spectral side is benign; the blocker is purely the Holder difference")
print("estimate for the Duhamel fixed point in H1-Strichartz spaces when a<1.")
