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

# Verification notes

The mathematical proof is contained in `RESULT.md`. For each \(n\geq1\), the essential-norm identity is deduced analytically from the diagonal operator \(S^n(S^n)^*\) and the finite-window gap structure; no finite matrix truncation is used as a proof of compactness or its absence. Rota universality is proved from a norm-one bounded right inverse and an explicitly infinite-dimensional kernel. The lower resolvent estimate uses a unit vector supported on infinitely long teeth, and the upper estimate uses a norm-convergent power series.

Run `python3 check_comb.py` with a standard Python 3 interpreter. This self-contained checker passed `FINITE_COMB_CHECKS_PASS 2946`. It checks sparse-window counts, descendant numbers for finite truncations, and finite resolvent witnesses against analytical upper estimates at several parameters. These tests are diagnostic only: they do not establish the all-parameter, infinite-dimensional, or limiting results.

The proof assumes complex \(\ell^2\), positive \(0<\alpha<1\), the explicit rooted comb, and a real resolvent parameter approaching one from above. It does not assert an exact resolvent leading constant or generality for arbitrary tree weights. Independent mathematical validation has not been performed.
