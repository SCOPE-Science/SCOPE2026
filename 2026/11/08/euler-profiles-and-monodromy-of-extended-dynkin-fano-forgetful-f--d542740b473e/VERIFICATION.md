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

The standalone `CHECK.py` is standard-library Python. Reproduction: `python3 CHECK.py` from this directory. It verifies the finite torus-fixed cutoff counts for multiplicities 1 through 15, the fourfold fibre Euler values 4/3/6/9/5, and integral subset-permutation traces and anti-eigenspace ranks for dimensions 3 through 11. Its successful final line is `FINITE_CERTIFICATE_OK`.

The unbounded fibre formula is proved by classifying every monomial cutoff and using torus-fixed Euler localization. The exact discriminant uses the nilpotent Jordan quadric-cone chart and the two-cycle node chart plus closedness of critical values. The local-system theorem uses the ordered-root cover and complex orientation of projective-line factors. Finite computations alone do not establish those geometric inputs.

No independent mathematical audit has been performed. Scheme-theoretic discriminant multiplicities, arbitrary framings and derived direct images are outside the claim.
