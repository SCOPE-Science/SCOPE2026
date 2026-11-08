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

The included `check.py` is executable using the Python standard library. Running `python check.py` reports 341 passed checks: complete mapping enumeration through six vertices, exact conditional probabilities, permutation factorial moments, the finite KL chain rule, and a 30-term high-precision constant with an analytical tail bound below \(1.5\cdot10^{-24}\).

The all-size identity and limit do **not** follow from finite tests: the proof in `RESULT.md` derives the conditional law by counting, obtains the KL chain identity exactly, controls the rencontres divergences by an explicit superfactorial majorant, and bounds the binomial–Poisson KL divergence by \(O(n^{-2})\). The 30-term numerical bound is rigorous given standard exact integer arithmetic and the displayed elementary inequalities; the printed decimal expansion is a reproducibility aid, not a substitute for the proof.

The scientific priority assessment is based on the inspected and cited sources; it is not exhaustive historical certification. Independent validation has not been performed.
