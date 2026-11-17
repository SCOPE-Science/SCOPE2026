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

# Reproducibility and evidence

Run `python verify.py` with Python 3 and packages `sympy` and `numpy` installed. The script is included in full in the same self-contained package. Its successful observed output was:

`VERIFY_OK log_jacobian_gap=1 exact_two_cycle=4 scalar_threshold=1 network_cases=3 initial_states=12 two_gene_attractor=1`

It checks an exact symbolic logarithmic-derivative identity, the exact two-cycle algebra and product multiplier, the symbolic scalar flip threshold, and twelve finite initial conditions across three heterogeneous networks. The universal convergence proof is mathematical, using an invariant positive box and a strict contraction in log coordinates. Numeric convergence tests and symbolic identity checking do not independently certify infinite quantifiers, historical priority, or the scientific interpretation. Independent audit has not been performed.
