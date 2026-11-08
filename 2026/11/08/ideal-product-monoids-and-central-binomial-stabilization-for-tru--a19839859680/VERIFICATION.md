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

# Reproducible checks and scope

Run `python verify_cyclic_nakayama.py` from the directory containing this document. The checker uses Python's standard library, builds the original path-product multiplication table and enumerates every row-reduced subspace over \(\mathbb F_2\) in four small ambient spaces. Closure under primitive idempotents and arrows is independently tested for each subspace; results are compared against the profile-classification formula. All ordered products of the enumerated ideal pairs are then independently evaluated as spans of original path products and compared with the profile formula.

Cases: \((n,\ell)=(1,3),(2,2),(2,3),(3,2)\). These have \(16,67,2825,2825\) subspaces; exactly \(4,7,10,18\) are two-sided ideals. All \(489\) ideal products pass. Further direct combinatorial checks compare the transfer-polynomial coefficients with dimension reciprocity at small \(n,\ell\) and verify the central-binomial increment at \(1\le n\le7\) in the cutoffs emitted by the checker. The printed record is retained in `verification_output.txt` and terminates with `CYCLIC_NAKAYAMA_IDEAL_MONOID_DIRECT_CHECK_PASS`.

The proofs for all fields and arbitrary cycle length and cutoff are the mathematical arguments in RESULT.md. The finite tests do not prove infinite parameter ranges, scheme-theoretic claims, novelty, or priority. No independent audit has been performed.
