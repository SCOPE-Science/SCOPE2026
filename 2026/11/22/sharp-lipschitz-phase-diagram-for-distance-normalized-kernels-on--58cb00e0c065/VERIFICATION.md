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

The self-contained `verify.py` runs in Python 3 with no third-party packages. It compares exact-rational Markov row matrices with the closed formula by exhaustive sign potential enumeration on each finite test star. It also checks the explicit optimizing signs, each obstruction polynomial, the all-parameter diameter-two ceiling in the tested domain, a uniform branch cutoff, and an unbalanced three-vertex example.

Command: `python verify.py`.

Result: PASS, 870 exact-rational parameter cases and supplementary threshold/envelope checks.

The finite tests do not exhaust all positive real masses, all finite star degrees, or all real bandwidths. The direct proof in `RESULT.md` covers those cases through exact algebra, the tree Lipschitz duality, a strictly decreasing polynomial, and a limit family. No independent audit has been performed.
