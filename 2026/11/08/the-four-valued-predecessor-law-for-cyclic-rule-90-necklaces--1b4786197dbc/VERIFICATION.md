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

# Verification record

The proof consists of four checked steps: (i) exact kernels and images of the binary linear rule, including the two exceptional tiny rings; (ii) identification of input-necklace fibers with orbits of the output's rotation stabilizer; (iii) Burnside's fixed-point formula in terms of divisors of the primitive multiplicity; and (iv) evaluation of the even/odd divisor sums by the totient identity. These deductions apply to every positive integer ring size and are not inferred from numerical experiments.

Run `python3 verify.py` in the extracted folder. The code implements the cellular update cell by cell, separately canonicalizes cyclic rotations, exhaustively enumerates all input words through length sixteen and checks predicted inverse degrees for every output necklace. Replayed locally, it reported `VERIFY_OK lengths=1..16 necklaces=8923 witnesses=5`. This experiment checks finite cases and does not substitute for the universal proof.

The source comparison examines algebraic labeled-state results, the all-elementary-rule necklace network study, and the adjacent-XOR necklace map. No completeness claim is made for unpublished or unindexed historical work. No external independent review or validation is asserted.
