---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The bounded budget simplex has a connected finite-valued design, and inverse trace diverges approaching disconnection (the eigenvalue lambda_2 of the full Laplacian tends to zero). For A=L+11^T/n and a nonzero Laplacian perturbation H, put D=A^{-1/2}HA^{-1/2}. The inverse-trace Hessian is 2n tr(D² A^{-1})>0; the edge-to-Laplacian map is injective. Uniqueness gives the three orbit variables and connectivity gives b>0. With k=n-2, the positive eigenvalues are x=2a+kb, nb, and z=2b+kc of multiplicity k-1. The trace problem exhausts the linear budget by homogeneity. Interior KKT for F=K/n gives lambda=2/z², z²=r x² and x²/b²=n[2(k+1)/r-k]. Thus a>0 iff r<n/k, and z²/b²>=nk>4 on the entire interior branch and at its endpoint, so c>0; enforcing the budget recovers T. At a=0 the b,c equations give z/b=sqrt(nk); the remaining KKT slack is 2(rk/n-1)/(k²b²), hence that branch is optimal at and above n/k, and remains unique at equality. Euler homogeneity gives K*=n lambda B including on the boundary. The D record has unique deletion beginning at r_D; the E support criterion has coexistence at r_E, not universal deletion there. Independently, at fixed spectral gap 1, averaging by the symmetries preserves feasibility and a. Given b>=1/n, minimize cost with a=(1-kb)^+/2 and c=(1-2b)^+/k. Cost on [1/n,1/k] has slope k+1-rk/2 and strictly increases beyond 1/k, so precisely the E tie allows both a=0 and a>0. Accordingly the A/E disagreement is compulsory on [r_A,r_E), with possible E retention also at the E tie; the width is 1 either way. D/A disagreement is [r_D,r_A), width 1/k. Replay: the exact spectrum and KKT/equality calculations above and RESULT.md §§1–5; VERIFICATION.md and verify.py were inspected as finite corroboration, not executed.

## originality

PASS

Support for the closed one-exceptional-price A-optimal solution and its comparison with the independently known D and E transitions. Neither general optimal-design theory nor a general KKT deletion test is new. The Tovar et al. weighted linear budget and support predicate are applicable as written, but to obtain this cutoff and both formulas one still has to solve for the deleted-network and interior optima in the one-priced-edge orbit; the inspected results do not solve those designs.

## value

PASS

A single expensive link is the minimal heterogeneous-price network design. Solving it exactly shows that choosing one standard optimality criterion over another can change both the weighted design and the decision to eliminate the anomalous link. The gap between A and E remains one unit of relative price even as the network grows; this structural distinction would not follow from general convexity, the homogeneous design, or an isolated numerical solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
