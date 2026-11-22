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

# Reproduction and limits

Run `python CHECK.py` from the extracted package directory. The supplied checker uses only Python standard libraries and enumerates all four-subsets of each cyclic order 4 through 26. In the current verification it checked 80,730 subsets and matched the closed formula and all predicted equality configurations. These tests are finite and floating-point, not an infinite proof. The proof is the trigonometric two-pair identity, concavity, parity and antipodal-pair argument in `RESULT.md`. No independent mathematical audit has been performed.
