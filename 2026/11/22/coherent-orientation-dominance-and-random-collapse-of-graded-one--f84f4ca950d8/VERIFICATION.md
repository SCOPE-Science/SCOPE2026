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

# Reproducibility and limitations

Run `python3 verify.py` from the package directory. The expected deterministic result is embedded as `verification_output.txt`. The verifier compares direct legal three-state extension enumeration against an independent supportwise binary-spin count, checks every orientation in the stated finite sizes, checks all coefficient inequalities and exact cubic deficits, and performs exact rational random expectation calculations through matrix size three. The infinite coefficient inequality and almost-sure random limit are established by the written Hölder and first-moment arguments in `RESULT.md`; the finite program does not certify these conclusions independently. The historical-priority comparison is provisional. Independent audit has not been performed.
