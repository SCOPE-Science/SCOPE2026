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
# Verification scope

Execute `python3 check.py` in the directory containing the source files. The script constructs binary quadratic norm-one conics for field orders 2, 4, 8, and 16 from explicit irreducible polynomials, checks every unordered pair sum for uniqueness, and directly computes the nonzero Weyl ambiguity coefficients for multiple phase alphabets. It compares each exact rank to the partition formula; its final success marker is `BINARY_SIDON_PHASE_RANK_SPECTRUM_PASS`.

A separate 4-dimensional operator singular-value calculation checked the entire positive/zero singular multiset and normalization for both a resonant and a nonresonant phase mask. All computations are finite checks and do not establish the all-dimension theorem; the proof in RESULT.md supplies the quantifiers and boundaries. Independent mathematical audit remains unperformed.
