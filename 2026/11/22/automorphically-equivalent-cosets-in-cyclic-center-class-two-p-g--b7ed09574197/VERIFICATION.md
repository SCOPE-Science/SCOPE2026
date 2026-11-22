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

# Verification

The mathematical claim is proved in `RESULT.md` for every odd prime \(p\), center exponent \(p^k\) with \(k\ge2\), and every dimension \(2n\) of the central quotient. `checker.py` independently enumerates the complete subgroup and automorphism structures for the two order-81 examples, verifying the allowed normal-subgroup sets without relying on the general classification theorem. Execute `python3 checker.py` to reproduce the marker `CYCLIC_CENTER_AUTOMORPHIC_COSET_CHECKS_OK`.

The computations do not constitute a proof for untested group orders; the general statement rests on the group-theoretic argument. Historical-priority search is necessarily incomplete. No independent specialist audit has been performed.
