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

# Reproducibility and claim limits

Execute `python verify.py` in a Python 3 environment; no third-party packages are needed. In the checked run the program printed:

```
PASS: 39756 exact finite assertions. Infinite statements require the proof.
```

The script performs rational exact identities for crown eigenspaces at tested orders, evaluates nonconstant eigenmode factors, checks the exact optimal and comparison gain identities at rational spectral parameters in the claimed regime, tests the full symmetric spectral enclosure on rational meshes and compares endpoint lower bounds on a rational two-gain grid. The tests are finite, not exhaustive over all graphs, all spectral parameters or real gains. The proof in `RESULT.md` provides those unbounded quantifiers.

No independent mathematical audit was performed. The sampling constraint applies to the two affine-in-\(P\) Markov factors, not to arbitrarily chosen stochastic matrices or unrestricted Chebyshev filters. The sourced robust interval formula already covers the complementary large-\(s\) branch, so that range is excluded from the claim.
