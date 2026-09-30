"""E8 exceptional topology: Cartan, unimodularity, rho-ample coefficients, negativity."""
import json
import numpy as np

# E8 Dynkin: chain 0-1-2-3-4-5-6 plus leaf 7 attached to node 2
# (branch node 2 has arms {0,1},{3,4,5,6},{7} of lengths 2,4,1 -> E8)
n = 8
edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(2,7)]
C = 2*np.eye(n)
for i,j in edges:
    C[i,j] = C[j,i] = -1

detC = round(float(np.linalg.det(C)))
Cinv = np.linalg.inv(C)
ones = np.ones(n)
a = Cinv @ ones            # rho-ample coefficients: C a = 1 > 0
Ca = C @ a
eigC = np.linalg.eigvalsh(C)
eigN = np.linalg.eigvalsh(-C)   # D_i . D_j = -C_ij, must be negative definite

out = {
  "cartan": [[int(x) for x in row] for row in C],
  "det": detC,
  "inverse": [[round(float(x),6) for x in row] for row in Cinv],
  "inverse_all_positive": bool((Cinv > 1e-9).all()),
  "inverse_min_entry": float(Cinv.min()),
  "ample_coeffs_a": [round(float(x),6) for x in a],
  "ample_all_positive": bool((a > 1e-9).all()),
  "C_times_a": [round(float(x),6) for x in Ca],
  "cartan_eigenvalues": [round(float(x),6) for x in sorted(eigC)],
  "cartan_positive_definite": bool((eigC > 1e-9).all()),
  "neg_intersection_eigenvalues": [round(float(x),6) for x in sorted(eigN)],
  "exceptional_Q_divisor_pairing": [round(float(x),6) for x in (-Ca)],
  "notes": ("D_i.D_j=-C_ij negative definite; sum a_j D_j is rho-ample since "
            "(sum a_j D_j).D_k = -(C a)_k = -1 < 0 for all k, with all a_j > 0. "
            "det C = 1: resolution is crepant, K_{tilde S} = rho^*K_{S0}. "
            "Nonzero ASD integral classes e on K3 have e^2 <= -2 (even lattice), "
            "certifying the pulled-back Euler classes e_i = rho^*omega_i are nonzero.")
}
with open("e8_topology.json","w") as f:
    json.dump(out,f,indent=1)
print("det =",detC,"| a =",np.round(a,4).tolist(),"| min(Cinv) =",round(float(Cinv.min()),4))
print("eig(-C) =",np.round(sorted(eigN),4).tolist())
