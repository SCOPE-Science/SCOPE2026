"""Recovery test: local sqrt(eps) scaling for Vaaler stability near coordinate planes."""
import numpy as np
for eps in [0.001,0.01,0.1]:
    m = 1/(1+eps); d2 = 2*(1-m*m)
    print(f"k=1 eps={eps} dist={np.sqrt(d2):.6f} ratio={np.sqrt(d2)/np.sqrt(eps):.4f}")
rng = np.random.default_rng(0)
for t in range(3):
    n,k,m = 8,3,5
    L = 0.05*rng.standard_normal((m,k))
    M = np.vstack([np.eye(k), L]); Q,R = np.linalg.qr(M)
    P = Q@Q.T; P0 = np.zeros((n,n)); P0[:k,:k]=np.eye(k)
    d = np.linalg.norm(P-P0,'fro'); V = np.sqrt(np.linalg.det(np.eye(k)+L.T@L))
    print(f"trial{t} dist={d:.4f} V-1={V-1:.6f} ratio={d/np.sqrt(V-1):.4f}")
