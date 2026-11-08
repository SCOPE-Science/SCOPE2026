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

The standalone `verify.py` uses only Python 3 standard-library code. Run `python3 verify.py` after extracting these same files. For all exponents \(j=2,\ldots,10\), it compares the direct binary transition coding with the fixed-point substitution, computes 2-binomial counts for each of the first \(3\cdot2^j\) windows, verifies the four-number fingerprint derived from the signatures, and checks all group separation invariants. The final marker is `VERIFY_OK`. The checked dyadic lengths are 4, 8, 16, 32, 64, 128, 256, 512, 1024 and class totals are 12, 24, 48, 96, 192, 384, 768, 1536, 3072.

Finite tests do not constitute a proof for all lengths; the all-\(j\) parity argument, modular moment bounds and known factor-complexity upper bound are stated in `RESULT.md`. The checker does not assess independence or establish novelty in any external literature beyond the references recorded there. No independent mathematical audit has been performed.
