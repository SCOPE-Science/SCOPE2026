---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Binary quadratic polar alternating rank yields minimum Hamming weight n/4 on codimension-two affine flats and next possible Hamming weight >=3n/8. The first essential bit j of an affine-flat indicator forces at least n/2^(j+3) cyclic one-runs; with weight n/4 this yields T_j threshold. Adjacent eight top-bit block-pair indicators give 7-dimensional RM(2,3); explicit (x_j+x_{j+1})(x_i+b) and three-equal-bit indicator add independent quotient monomials at each lower-bit threshold. Cayley components are cosets of H_alpha. Independent full direct enumeration at m=3,4,5 (127+2047+65535=67709 nonzero words) reproduces successive ranks, and actual check.py examined; this is corroboration of induction, not infinite proof. Need exact LSB order and cyclic wrap.

## originality

PASS

Earlier published Resultary findings give the complete RM(1,m) symbol-pair spectrum/profile in the SAME numerical ordering, but neither includes quadratic monomials or the n/4-based RM(2,m) subcode filtration. Classical Reed–Muller Hamming distributions supply the Hamming gap but cannot infer order-sensitive runs. Singh–Singh establish general pair-generation/coset framework but available abstract gives no all-layer RM(2,m) classification; best-of-knowledge risk retained.

## value

PASS

This is a complete natural higher-order code-filtration theorem, giving every connected component and all sharp layer jumps under a concrete symbol-pair read channel; it is nontrivial beyond ordinary distance or RM1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
