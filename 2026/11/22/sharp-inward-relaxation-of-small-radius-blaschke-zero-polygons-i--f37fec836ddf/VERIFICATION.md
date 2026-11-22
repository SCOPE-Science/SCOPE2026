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

# Verification and limits

The exact Fourier representation is \(\mathcal V(B)=2\sum_{m\ge1}|\sum_j a_j^m|^2\), by summing Poisson kernels on the unit circle. The proof constructs normalized zeros \(u_j=a_j/r\), with one root exactly one, and uses Newton coordinates \(q=(p_1,\ldots,p_{d-1})\). The Jacobian from coordinates to the monic root polynomial is invertible at the regular \(d\)-gon; the higher-mode Hessian is uniformly \(O_d(r^{2d})\), dominated by the positive core lower bound \(2r^{2d-2}\). Stationary equations give \(q_{d-1}=d^2r^2/(d-1)+O_d(r^4)\), and every other \(q_m=O_d(r^4)\). The derived root displacements are strictly inward for every non-distinguished index, completing global feasibility.

Run `python CHECK.py` from the extracted artifact directory. It carries out exact rational Newton checks for degrees 3–13 and finite Fourier-energy diagnostics for degrees 3–9. These are repeatable supplementary diagnostics, not exhaustive verification of the continuous-parameter theorem. The proof is analytic; no independent external audit or expert validation has been performed.
