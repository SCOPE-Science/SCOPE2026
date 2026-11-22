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
# Reproducibility and boundaries

Run `python3 check_projective_rook.py` with Python 3 and no external packages. The script constructs six groups \(C_2,C_3,C_4,C_2^2,S_3,Q_8\) through explicit multiplication tables, checks associativity, computes group centers and inverses, enumerates all labelled partial injections for \(n=1,2,3\), and partitions them into central-label gauge classes. It counts rank strata and self-inverse classes by direct inversion and separately evaluates the closed formula using central square roots.

The script additionally obtains actual partial-conjugation signatures on every supported labelled matrix unit for \(n\le2\), and for \(n=3\) with \(C_2\) and \(S_3\). It checks that equal signatures are exactly equal gauge classes, establishing an independent finite test of the key equivalence, not merely of the combinatorial formula. See `verification_output.txt` for the exact replay output, concluding with `VERIFY_OK`.

These finite checks cannot establish the all-groups statement. The general correctness rests on the fully written conjugation-on-matrix-units proof and the disjoint-cycle enumeration. Independent external mathematical verification has not been performed. No reliance on inaccessible computation traces or unspecified external libraries is required.
