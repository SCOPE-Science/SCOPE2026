---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Using the exact finite window g(j)=rho^j on Z_(qm), Fourier transform in the m modulation columns decomposes the Gabor synthesis into m q-by-q fibres. Writing t=ma+b gives fibre entries rho^((j-b) mod m) C_R[:,a+1_{b>j} mod q], R=rho^m, where C_R is invertible since its circular Fourier eigenvalues are (1-R^q)/(1-R exp(-2pi ik/q)). Thus rank equals the sum of distinct selected indices per fibre; full rank forces all remainders b_a equal, precisely the m coset masks. For each full-rank mask, diagonalization gives the full claimed lambda_(s,k), exact extrema, determinant and condition number. The derivative equation for optimal R is monotone and diverges at R->1, giving a unique global minimizing taper. Direct independent NumPy synthesis/SVD over all 20 q=3,m=2 masks at rho=.6 checked rank and exact squared spectrum; source checker covers more finite instances. Exact proof is all q,m>=2, not finite extrapolation. Verified Git tree and RESULT.md/check_geometric_masks.py blob identities.

## originality

PASS

General subgroup block-equivalence of Gabor systems is prior art and supplies the fibre reduction. The specified positive geometric cyclic window forces an additional rigid complete mask classification, explicit all-eigenvalue formula, determinant and unique optimal taper. Relevant Resultary Gabor phase-retrieval and nonnegative-window records examine different operators or fixed sampling geometries, not the q-subset translation-mask classification; no stronger published implication found. Residual risk from other specialized circulant/finite Gabor literature remains.

## value

PASS

Selecting q translation locations from qm coordinates is a mathematically natural finite-Gabor sampling-design problem. The unexpected rigidity that only subgroup cosets yield bases despite a nowhere-zero window, together with the exact rank for every mask, sharp frame spectrum and optimal taper, is a complete structural classification and reproducible exact design criterion. Its value is not contingent on a downstream general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
