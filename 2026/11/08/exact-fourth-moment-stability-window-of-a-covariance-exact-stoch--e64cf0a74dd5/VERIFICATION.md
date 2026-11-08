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

Run `python3 verify.py` from the extracted folder with standard Python 3. The recorded `verification_output.txt` reports 3,028 exact-rational assertions and the explicitly evaluated \(r=t=s=1\) benchmark. The verifier checks Gaussian moment expansions, recursions, the strict fourth-moment condition and algebraic boundary cases on a finite rational parameter grid.

The general result, including the sharp radical threshold and the divergence of the continuous and numerical fourth moments at their respective boundaries, is proved analytically in `RESULT.md`. The finite program does not certify every real parameter, and no independent scientific audit has been performed.
