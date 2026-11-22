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
# Reproducibility record

Run `python3 verify.py` from this extracted package. The program enumerates all matrices with square zero over the rings \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/9\mathbb Z\), \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\), and \(\mathbb F_3[\varepsilon]/(\varepsilon^2)\), then traverses their actual orbits using elementary conjugations. The tested dimensions are three for residue field size two and two for residue field size three. The generators include elementary transvections and all diagonal unit scalings, so their closure is the full general linear group for these local principal rings. The result is checked separately in each reduction-rank stratum against the finite-field rational-canonical class counts. `verification_output.txt` is the checked output of the packaged verifier.

The proof of the universal statement is the block calculation in RESULT.md; finite exhaustion alone cannot certify untested dimensions, arbitrary residue fields or mixed-characteristic rings beyond those examples. The prior sources were checked for claimed implication, but an unlocated earlier equivalence may exist.
