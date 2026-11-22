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

The finite computations can be reproduced by invoking `python3 VERIFY.py` in the directory containing the supplied script. The script checks standard necklace orbit counts independently, enumerates local transition matchings and short-cycle inclusion–exclusion sums, enumerates all binary depth-two long-cycle necklace multisets of total length eight, and exhaustively checks colored permutations up to six vertices for the binary depth-one lower bound.

Observed output ends with `VERIFY_OK 25`. The output includes counts \(1,3,40,7749\) at binary depths one through four and \(64\) at ternary depth one. The short-cycle reduction is proved symbolically: revisiting a length-\(d\) state within a cycle of length at most \(d\) forces a shorter cyclic color period and a repeated arc label, impossible in a permutation. The checks have finite bounds. The proof of the theorem for all integers \(q\ge2\), \(d\ge1\) is the structural argument in `RESULT.md`, not an inference from computations.

Scientific limitations: the language is one bijective unary function with exactly one of \(q\) named colors per point, and the claimed profiles are quantifier-free and bounded in function-term depth. The enumerator uses a finite inclusion–exclusion over all short directed simple cycles; polynomial running time in variable \(q,d\) is not asserted.
