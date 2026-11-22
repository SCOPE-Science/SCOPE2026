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

# Verification of the theorem

The operator identity, first subdiagonal and lower-triangular sign behavior were checked on four independent exact-rational finite matrix pairs with nine coordinates, giving 360 individual exact assertions. The standalone \(\texttt{check.py}\) also computes the Weyl circle integral using a fixed angular mesh and compares the resulting coefficient against singular values of three finite 300-by-300 commutators. It passed the asserted inequalities for ranks 25, 60 and 100. Running it requires Python 3 and NumPy; use \(\texttt{OPENBLAS_NUM_THREADS=1 python check.py}\) after extracting all files from the same finding.

These checks have a deliberate scope: finite numerical singular values do not verify a limit over infinitely many ranks. The infinite conclusion rests on the exact resolvent identity; the uniform geometric matrix-entry error estimate; the weighted Toeplitz counting lemma with explicit low-rank, cross-block, tail and polynomial-approximation controls; and singular-value perturbation inequalities. The code checks coefficients and finite algebra, not novelty, infinite compactness, or independent validation.

There are no inaccessible computational certificates or required files outside this package. No independent audit has been performed.
