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

# Verification details

The included `VERIFY.py` runs in Python 3 without third-party packages. Execute `python3 VERIFY.py` in the same directory as the scientific files. It returned:

`PASS: 1659 deterministic assertions; four exact factorizations; sharp stage-four transition`

The program uses exact rational arithmetic to check the four symmetric-winding polynomial factorizations at seven rational winding parameters and 36 rational site positions, the stage-four strict separated-site fraction witness, the threshold algebra, independently summed winding series, unequal-site-strength Perron ordering, and interior/global stage-four phase behaviors. These finite checks are supplemental. The all-parameter proof consists of the generating series identities, the positivity of the Perron sensitivity, and the exact sign analysis of the cubic polynomial derivative in RESULT.md. Reproducing the displayed algebra requires no symbolic-computation package. The source comparison and access limits are documented in AUDIT.json. No human or independent audit is represented by this verification record.
