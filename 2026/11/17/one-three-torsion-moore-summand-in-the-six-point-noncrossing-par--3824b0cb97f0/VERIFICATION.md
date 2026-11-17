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

# Exact verification and limits

Run `python3 verify_nc6.py` with Python 3 (standard library only). The accompanying `verification_output.txt` is the complete recorded stdout, and begins `NC6_CYCLIC_QUOTIENT_EXACT_PASS`.

The program constructs all 130 proper noncrossing partitions on six cyclically ordered elements, all order-complex chains and all rotation orbits; constructs signed cellular matrices, checks the two compositions vanish; cancels 25, 152 and 207 integral unit pivots and confirms that the sole remaining nonzero differential is coefficient 3. It separately checks that rotations by two and by three labels fix vertices. The computation is exhaustive for exactly this finite object, uses integer arithmetic, and includes no probabilistic or floating-point steps.

The output `homology_H2=Z/3 homology_H3=Z^8 pi1=trivial` includes a fundamental-group conclusion that uses the independent *mathematical argument* in RESULT.md (EL-shellability plus Armstrong's fixed-point subgroup theorem); the program by itself only confirms the relevant fixed-point premises and integral homology. The homotopy wedge decomposition likewise uses the simply connected three-dimensional CW theorem and not the computational log alone. No result for other vertex counts is claimed.

Self-review: passed. Independent audit: not yet performed.
