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

# Reproducibility and limits

Run `python3 verify_path_tail.py` in a Python 3 environment. The file depends only on the standard library; `verification_output.txt` contains the observed output from an actual execution. The verifier constructs all bond configurations for each finite check using exact rational arithmetic and separately evaluates the formulas and optimization policy against exhaustive expectations.

Checks completed: 16,376 deterministic run-count identities; 252 exact-rational expected long-component counts; 36 exact-rational expected connected pair counts; 1,089 path-size, threshold and probability optimizer comparisons; exact excess threshold risk \(1/24\) on the seven-vertex path at \(h=3\) and \(p=1/2\).

These tests cannot establish a universal parameter theorem by enumeration. The argument in `RESULT.md` proves the all-order statement by the deterministic run-count identity and a strictly convex discrete pair-connectivity functional. No independent scientific or historical-priority audit has been performed.
