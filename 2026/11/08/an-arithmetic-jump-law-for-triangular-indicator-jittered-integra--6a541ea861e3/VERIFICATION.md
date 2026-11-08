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

The accompanying `verify.py` is self-contained Python 3 and replays `verification_output.txt`. All arithmetic operations in the main finite tests use `fractions.Fraction`, not floating point. The independent geometric test clips a half-plane to each cell and computes exact shoelace areas. The rational period constants and finite-grid variances are checked for every reduced positive slope up to denominator 35, with multi-period grids; small-grid computations use independent polygon clipping, not the phase formula.

The proof in `RESULT.md` is necessary for statements quantified over all \(n\) and all real \(\alpha\). Finite checks alone do not prove those infinite claims. In particular, continuity at irrational slopes follows by a Weyl-equidistribution argument and reduced-denominator decay. The checked package contains all required code; no network, unpublished database or inaccessible auxiliary file is needed to replay it. Scientific novelty and specialist precedence remain subject to independent assessment.
