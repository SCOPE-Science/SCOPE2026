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

# Reproducibility

Run `python3 checker.py` in a directory containing the bundled checker. Python standard library only. The checker independently constructs actual error outputs by permuting each four-bit input block; it does not reuse the proof's counting algorithm for these sets. It then cross-checks the closed formula and the asserted maximum and six maximizers over all 8,176 binary words of lengths four through twelve. Recorded run: `PASS direct-channel-vs-formula; total words 8176` and `PASS sharp maxima and six equality words {4: (6, 6), 5: (9, 6), 6: (12, 6), 7: (15, 6), 8: (18, 6), 9: (21, 6), 10: (24, 6), 11: (27, 6), 12: (30, 6)}`. Finite enumeration is not proof of the statements for unbounded lengths; consult the symbolic induction in `RESULT.md`.

No independent mathematical audit has been performed. Historical priority may remain incomplete.
