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

# Reproducible checks

From the directory containing these complete files, execute `python3 VERIFY.py` with Python 3.8 or later; no third-party modules are needed. The script performs a symmetry-reduced independent search that processes source positions one by one, creates all possible partial copies, retains only compatible common-prefix states, and checks full equality after the final position. It checks 286 positive four-run instances with 2–4 copies against the proposed arithmetic criterion. Separately it calculates 1,372 exact enumeration cells for 2–8 copies and source-copy counts up to 14, comparing the count formula with full enumeration of all allowed positive run compositions. Six large-parameter density comparisons confirm the predicted limiting constants numerically. All checks returned `ALL CHECKS PASSED` upon actual execution.

The infinite proofs do not rely on these bounded checks. Especially, asymptotic numerical comparisons are illustrative, not a proof of a limit. The proof of the formula, of the limiting law and of uniqueness of the density minimum appears in RESULT.md. Literature search cannot establish mathematical uniqueness or priority definitively. No independent audit or external formal certification is asserted.
