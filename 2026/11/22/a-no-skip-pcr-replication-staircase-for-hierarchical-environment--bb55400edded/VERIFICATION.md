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

# Verification record

The stand-alone Python checker uses the standard library only and is included as `check.py`. Run `python3 check.py` from the extracted scientific package. It confirms the conditional miss-probability identity for many selected parameters, compares the integer optimizer against a broad finite candidate grid, brackets selected continuous maximizers, locates several adjacent-switch probabilities by bisection, and numerically checks the proposed asymptotic scale. Actual package replay passed 504 assertions.

The mathematical proof in `RESULT.md` is the evidence for all-parameter and all-integer statements. Neither a finite parameter grid nor floating-point bisection constitutes a proof of an infinite or exact claim. The first three reported threshold decimals are rounded approximations, not exact algebraic constants. The theorem's sharp asymptotic is a limit with fixed positive per-sample and per-PCR costs and fixed conditional PCR sensitivity, as capture probability approaches one or switching index diverges.

Independent validation was not conducted. The related-literature comparison is limited to the explicitly cited source material and does not certify historical precedence.
