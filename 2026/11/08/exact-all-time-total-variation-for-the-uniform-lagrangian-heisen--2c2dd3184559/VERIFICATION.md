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

# Verification and reproducibility

Running `python CHECK.py` from the directory containing this file and `CHECK.py` requires only Python's standard library. The program uses exact fractions to construct the true convolution powers from the group law, compares every state probability for times 1–4 against the proposed all-time formula, and checks total variation and chi-square identities at fields of orders 3, 5, 7 and 9 and dimensions 1 and 2. The order-nine field is implemented directly using its irreducible polynomial \(\theta^2+1\) over \(\mathbb F_3\). Prime-field Schrödinger operator sums are additionally checked against the parity projector with absolute tolerance \(10^{-11}\). Expected final line:

`LAGRANGIAN_HEISENBERG_EXACT_CHECKS_PASS`

All exact arithmetic comparisons passed on the embedded checker before packaging. The check is finite and cannot prove the theorem for untested dimensions, field orders, or arbitrarily large convolution times. The analytical proof for every odd prime power and all positive integer times is in `RESULT.md`. The full source is embedded in this package. Independent mathematical validation has not been performed.
