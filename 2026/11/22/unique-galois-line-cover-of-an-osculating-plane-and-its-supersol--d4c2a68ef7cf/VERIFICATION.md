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

# Verification of the finite-plane Galois-line arrangement

The theorem has four proof-dependent steps: exhaustive ambient Galois-line types from the cited classification; kernel sizes and forced rational witnesses for minimality; explicit pairwise intersection equations and modularity; addition–deletion plus inclusion–exclusion. Their logical order is given in `RESULT.md`.

Run `python verify_galois_cover.py` using Python 3 and the standard library. The code performs exact arithmetic in polynomial-basis representations of \(\mathbb F_{16}\), \(\mathbb F_{64}\), and \(\mathbb F_{256}\), using irreducible moduli 0x13, 0x43 and 0x11d. For the first two fields it exhausts every rational projective point and verifies the complete incidence profile and deletion necessity of every member. For all three fields it certifies that the pairwise intersections of distinct \(L_t\) give precisely \(\binom Q2\) triple points and verifies the image sizes of \(t^2+dt\). At \(Q=256\), no exhaustive projective-plane point census is claimed.

Expected checks: \(Q=16\) gives 31 cover lines, 120 triple points, one 15-fold point; \(Q=64\) gives 127 lines, 2016 triple points, one 63-fold point; \(Q=256\) gives 511 lines, 32640 triple points, one 255-fold point. The all-extension zeta formula is derived symbolically, not experimentally. The finite tests are not a substitute for the infinite-family proof. Independent mathematical audit has not been performed.
