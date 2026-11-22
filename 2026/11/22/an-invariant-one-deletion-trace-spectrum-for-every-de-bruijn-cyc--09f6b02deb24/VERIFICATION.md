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

# Reproducibility and limits

Run `python3 verify.py` with Python 3. No third-party packages or network access are needed. The program includes a literal cyclic-window uniqueness test, direct enumeration of every deletion position, output canonicalization by all rotations, source cyclic-run counting, and exact integer comparison of output multiplicities.

It checks 16 FKM-constructed de Bruijn cycles for \(q=2,3,4,5\) at the orders recorded in `verification.log`. A second generation procedure varies every outgoing arc order in the directed binary overlap graph and obtains all de Bruijn necklaces at orders 2, 3, 4 and 5: precisely 1, 2, 16 and 2048 instances. These are verified without using the run-anchor proof in the counting code. The expected final line is `VERIFY_OK FKM_parameter_pairs 16 binary_all_orders_2_to_5`.

The verifier's finite domain cannot prove the theorem for arbitrary \(q,n\). The complete mathematical argument is in `RESULT.md`: uniqueness of each constant factor, linear equality after distinct deletions rooted at that factor, and an exact count of short and maximal runs. No claim is made about independent external evaluation or formal proof-assistant certification.
