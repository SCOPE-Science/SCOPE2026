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

The polynomial-module argument in RESULT.md proves all infinite-horizon statements. The standalone `verify.py` tests finite polynomial degrees and finite block ranks with exact \(\mathbb F_2\) arithmetic; it does not certify infinitely many cases or publication priority. In the reported run, all 961 ordered pairs of nonzero polynomials with degrees at most four passed the determinant/entropy consistency tests at \(N=3,6,12\). Both examples passed pairwise-independence and exact block-rank checks for \(N=1,\ldots,19\).

Run using `python3 verify.py` from a directory containing the package. No dependencies beyond the Python standard library are required. Floating-point simulation is not used.
