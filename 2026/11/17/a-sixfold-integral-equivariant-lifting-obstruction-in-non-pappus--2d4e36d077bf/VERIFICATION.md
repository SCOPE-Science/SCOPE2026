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
# Reproducibility and scope of checks

Execute `python3 verify_nonpappus.py` in the directory containing the verifier. It needs Python 3 with standard-library `itertools`, `collections` and `fractions` only. The expected output is stored in `verification_output.txt`.

The executable independently reconstructs the eight forbidden triples, both independence complexes, all 12 automorphisms by an exhaustive 4,320-case incidence-compatible search, the central involution and complementary symmetric group. A separate complete 9-factorial permutation check also found exactly 12 automorphisms during the scientific review.

It evaluates signed Lefschetz traces for all group elements, checks rational character multiplicities, constructs every valid sign-twisted triangle orbit sum, computes all 36 edge-boundary rows, and verifies the displayed four critical rows and the complete boundary of the integer vector `(1,-2,0,0,-2,0,1,6)`. The elementary identity from the critical four rows forces every equivariant projection coefficient to be divisible by six. The explicit vector proves sharpness.

A tetrahedral boundary argument on each absent triangle establishes integral first-homology vanishing and the free integral degree-two ranks. The computation does not depend on a finite-field rank as evidence for an integral statement.

Limitations: verification is for precisely the documented rank-three matroid and its automorphism group. The calculation is not an independently performed mathematical audit, and publication priority has not been independently certified.
