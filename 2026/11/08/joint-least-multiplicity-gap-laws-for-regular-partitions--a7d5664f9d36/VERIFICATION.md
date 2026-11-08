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
The mathematical claim is the exact joint survivor count together with its fixed-parameter joint weak limit. The proof is in `RESULT.md`; it uses the classical Euler-product and Ingham partition coefficient asymptotics, and a finite bijection whose shifts are exact.

`python verify_joint.py` independently enumerates all allowed-part partitions through size 24, checks 9,600 joint survivor cases for \(\ell=2,\ldots,7\), and also compares nonmonotone-threshold layer-cake shifts and numerical large-size examples. Its produced text is `verification_output.txt`. Finite checks do not certify an infinite-domain asymptotic or substitute for independent audit.
