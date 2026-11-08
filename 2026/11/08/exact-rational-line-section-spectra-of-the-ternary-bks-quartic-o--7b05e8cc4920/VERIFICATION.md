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

# Exact finite-field verification

Run `python3 verify_bks.py` in the package directory. No external Python packages or online resources are required. The program constructs complete tables over two irreducible polynomial quotient representations of each of \(\mathbb F_{27}\) and \(\mathbb F_{81}\), certifies the moduli by elementary finite trial division, enumerates all projective points and dual lines, evaluates the ternary BKS quartic on every point, and counts every rational line section. Four-secants are regenerated from point-pair spans and their incidences counted at every point. The normalization image and two incidence double counts are cross-checked.

Expected successful last line: `BKS_SHORT_EXTENSION_COMPLETE_EXACT_CENSUS_PASS`. Full output includes complete line intersection histograms and all point multiplicity histograms. The computations are exhaustive **only** for these two field sizes; they make no claim for larger extensions or different base fields.

The self-review recorded PASS on correctness, originality and value for the stated exact finite claim. It does not constitute independent auditing, formal verification, or external novelty certification.
