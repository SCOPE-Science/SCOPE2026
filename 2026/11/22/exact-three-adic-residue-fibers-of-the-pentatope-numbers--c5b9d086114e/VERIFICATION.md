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

# Reproducibility and limits

Run `python3 artifacts/verify.py` with Python 3 and no external libraries. The script computes the actual binomial coefficient residues for every index in the candidate period at exponents one through seven, computes predicted fibers independently from modular square roots, compares the complete residue dictionaries and predicted fiber-size histograms, and checks periodic shifts in each range. The extracted script reported `PASS: 12926 exact finite index/period checks, all target fiber spectra reproduced`.

The infinite proof is given in `RESULT.md`, using two isometric branches and one explicitly normalized square branch. Computation does not prove infinitely many moduli or originality, and no independent mathematical audit is claimed.
