---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytic certificate consists of: (i) the unique stationary-point formula, (ii) a strictly positive second derivative of the geometric-return mixture for every integer group size at least three, (iii) the explicit Dulac multiplier and its positive divergence, (iv) the Poincaré–Bendixson consequence for all non-equilibrium forward orbits, and (v) an explicit pairwise conserved coercive energy whose regular levels are closed trajectories.

Run `python check.py` to verify derivative identities and exact rational matrices. It requires SymPy. The checker is not an exhaustive simulation and cannot replace the topological arguments. For parameters \(N=3\), \(r=3\), \(\delta_s=\delta_d=1/2\), \(\varepsilon=\theta=1\), the rational Jacobian is \(\bigl(\begin{smallmatrix}1/32&-1/4\\63/128&0\end{smallmatrix}\bigr)\), with spectrum \((1\pm i\sqrt{503})/64\). At \(N=2\), the analogous Jacobian has spectrum \(\pm i/4\), with a global energy integral.

No independent scientific assessment was performed. The first public motivating source date is October 11, 2025, as recorded on the original arXiv abstract; the February 2026 date is a later revision, not the first-public date.
