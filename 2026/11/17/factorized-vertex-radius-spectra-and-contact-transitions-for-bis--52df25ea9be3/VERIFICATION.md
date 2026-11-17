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
# Verification

The complete proof is in `RESULT.md`; the executable `verify.py` is a finite, exact-arithmetic corroboration of its combinatorial and metric steps. The all-parameter vertex–orientation bijection, sign counts, factorization and extremal-degree analysis are deductive arguments; numerical extrapolation is not invoked.

Run `python3 verify.py` using ordinary Python 3. It evaluates the nine cases \((p,q)\in\{1,2,3\}^2\). For each, it independently constructs all signed indegree vectors and all signed diamond endpoint sums; calculates complete integer squared-radius multiplicities; checks the exact first-face formula, radius and *entire* outer-contact set; and constructs an explicit exposing integer potential for each oriented tree. It terminates with `OK: 3535 exact assertions over 9 bistar instances` on success and raises `AssertionError` on any discrepancy. The enumeration does not purport to be exhaustive for larger parameters, and an independent mathematical audit has not been performed.

The accompanying review assessed proof completeness, scope and research overlap, including the specific remaining historical-priority risks. These checks establish neither external certification nor priority over any inaccessible equivalent result.
