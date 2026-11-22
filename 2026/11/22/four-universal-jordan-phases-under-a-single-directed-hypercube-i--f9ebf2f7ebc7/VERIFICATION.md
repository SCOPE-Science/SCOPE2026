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

The claim has an all-dimension finite-field proof in `RESULT.md`. The files here give finite computational checks, not independent certification of that proof. The entire proof's claims about higher dimensions rest on algebraic arguments, not on extrapolating from these checks.

Run using the standard Python library:

```sh
python check_rank.py
python check_dynamics.py
```

`check_rank.py` computes actual matrices and products over characteristic two without using a precomputed Jordan form. It checks all 27 parameter pairs with dimension \(2\le d\le7\) and endpoint Hamming distance \(1\le\rho\le d\), confirming power ranks and stabilization or extinction identities. Its captured exact output is `check_rank.stdout`.

`check_dynamics.py` directly enumerates all \(q^{2^d}\) states for every endpoint-distance class in dimensions two through four over \(\mathbb F_2\) and dimensions two through three over \(\mathbb F_4\). Each trajectory is iterated to its first repeat, at which point entry time and primitive period are known. It compares cumulative entry and primitive-period populations against the stated formulas, including 65,536 states per \(\mathbb F_4\) dimension-three case. Its captured exact output is `check_dynamics.stdout`.

The checks do not address arbitrary multiple-edge changes, non-characteristic-two fields, asynchronous updates, or possible historical equivalents. Independent auditing has not been performed.
