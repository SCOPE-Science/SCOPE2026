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

# Verification of the 315-tetrad Frobenius classification

Run `python3 VERIFY.py` from the extracted directory. No external data or dependencies are used. The verifier enumerates the 210 simple four-cycles on 8 labels and the 105 perfect matchings, independently recovers the exact same 315 four-edge sets by checking parity masks 0 and 255 among all 20,475 four-edge choices, and confirms the two constructions agree.

It constructs a representative for each of the 22 integer partitions of eight and checks the cycle decompositions on the 210-, 105- and 315-element sets. For every power up to the maximum cycle length, it independently counts fixed tetrads and checks the divisor-sum fixed-point formula. It also verifies weighted conjugacy-class totals 40,320, a Burnside average of one in each of the two geometric orbits, the exact rational-tetrad existence obstruction, the three bitangent-free rational-tetrad types, and equality of tetrad and octad splitting degrees.

Expected terminal marker: `CAYLEY_OCTAD_TETRAD_FROBENIUS_VERIFIED_OK`.

The calculation is exhaustive over the finite Cayley model and all symmetric-group conjugacy classes, not a sampling of curves. Its geometric applicability uses the classical characteristic-not-two Cayley/odd-theta correspondence for a smooth quartic with a Frobenius-stable regular octad. No independent audit has been performed, and realizability of every class over a fixed finite field is not asserted.
