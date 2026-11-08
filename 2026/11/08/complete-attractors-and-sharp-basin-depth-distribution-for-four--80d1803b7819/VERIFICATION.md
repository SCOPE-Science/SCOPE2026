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

# Verification of the finite classification

The exact table is `gap_table.csv` and the self-contained verification script is `verify.py` (Python standard library only). To rerun, place these files next to each other and execute `python3 verify.py`. Expected standard output is stored in `verification_output.txt`.

The checker starts from the mathematical definition of the four-digit base-\(12\) map, separately reconstructs all 77 gap states and their weights, and then processes all 20736 padded integer starting strings. It confirms every gap-table byte and matches all stated cycles, basin sizes, entry-depth histograms and the exceptional twelve repdigits. A finite complete certificate is appropriate because the theorem quantifies over a precisely bounded \(12^4\)-element domain; it does not imply any assertion for other bases or digit lengths.

Self-review passed; independent mathematical audit has not been performed.
