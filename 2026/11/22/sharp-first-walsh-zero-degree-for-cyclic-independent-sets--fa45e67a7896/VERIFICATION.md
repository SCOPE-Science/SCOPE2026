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

# Verification and scope

The mathematical claim is an all-integer theorem with a self-contained matrix/free-product proof in `RESULT.md`. The exact matrix identity \(A_+A_-^2A_+=-A_-\), the order-three projective relation, the interval ping-pong inequalities, and the syllable-length induction are the critical nonstandard steps. The lower bound does not rely on a finite census.

Run `python3 verify_fwht.py`: it enumerates independent-set incidence words and computes full exact integer Walsh transforms for all cycle sizes three through eighteen, independently of the transfer-matrix derivation. Run `python3 verify_transfer.py`: it checks exact signed matrix products against reduced free-product words for all frequencies through fifteen vertices, verifies the zero-degree threshold, and tests both local matrix identities. Both programs ran to completion without assertion failures.

Observed zero-frequency counts at multiples of three through length eighteen were 3, 18, 111, 696, 4413, and 28206, with first Hamming zero degrees 2, 3, 4, 5, 6, and 7 respectively. No formula for those total counts is claimed. At lengths not divisible by three, these runs found no zeros, consistent with the known parity boundary.

All computations use the Python 3 standard library and exact integers. The finite ranges are reproducibility checks only; they cannot prove the unrestricted statement or exclude an equivalent prior publication. Independent validation has not been performed.
