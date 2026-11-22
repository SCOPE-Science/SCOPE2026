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

The derivation of the classification is in `RESULT.md`. The auxiliary `verify.py` is a standard-Python-3 implementation of exact calculations over the prime field with three elements; it is intentionally independent of the symbolic proof's counting derivation.

Run `python3 verify.py`. The script enumerates every unital linear map on the four-dimensional algebra with quotient form \(\operatorname{diag}(1,1)\), first applying its mandatory square equations (a completeness-preserving filter of all \(3^{12}\) maps), and then checking every original pairwise multiplication equation. Its rank counts are \(72\) and \(144\). It exhausts all possible scalar characters for nontrivial idempotent images, obtaining zero. Separately, it enumerates all idempotent radical matrices for \((m,r)=(2,1)\) and \((2,2)\), verifying retraction counts \((9,1)\) and \((81,108,1)\), respectively. Successful completion prints `DEGENERATE_SPIN_RETRACTIONS_VERIFIED`.

These are exact finite calculations for the specified cases, not a substitute for the proof for arbitrary fields and dimensions. The geometric irreducibility and full Witt-independent formulas are justified mathematically in `RESULT.md` rather than inferred from experiments. No external independent mathematical audit has been performed.
