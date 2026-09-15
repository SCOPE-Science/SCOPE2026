"""Slice-coupling check for lane-20326 target (vectorized)."""
import numpy as np

def Qmat(W):
    return W[:,0]**2 + W[:,1]**2 - W[:,2]**2 - W[:,3]**2

h = 0.05
centers = np.array([
    [0.0, 0.0, -0.5, -0.5],
    [0.0, 0.0,  0.5,  0.5],
    [0.0, 0.0, -0.5,  0.5],
])
lin = np.linspace(-h, h, 5)
G = np.array(np.meshgrid(lin, lin, lin, lin)).reshape(4, -1).T  # 625 pts
print("grid pts per cap:", len(G))

def min_abs_Q(ci, cj):
    A = ci + G          # (625,4)
    B = cj + G          # (625,4)
    D = A[:,None,:] - B[None,:,:]          # (625,625,4)
    M = D[...,0]**2 + D[...,1]**2 - D[...,2]**2 - D[...,3]**2
    return float(np.abs(M).min())

print("pairwise min |Q(xi-eta)| over sampled caps:")
for i in range(3):
    for j in range(i+1, 3):
        print(f"  tau{i+1}-tau{j+1}: {min_abs_Q(centers[i], centers[j]):.4f}")

print("u-projection centers (all (0,0), half-side 0.05): identical -> overlap volume 100%")
print("v-projection centers: (-.5,-.5),(.5,.5),(-.5,.5): pairwise disjoint but share u-fiber")

for R in [10, 100, 1000]:
    nslabs = int(2*R)
    print(f"R={R}: O(1) x5-slabs ~ {nslabs}, triangle loss ~ {nslabs}x vs allowed R^eps ~ {R**0.05:.2f}")
    print(f"  phase variation of exp(i x5 |u|^2) across B_R at |u|=1: {2*R:.0f} rad >> 1 -> amplitude not frozen")
