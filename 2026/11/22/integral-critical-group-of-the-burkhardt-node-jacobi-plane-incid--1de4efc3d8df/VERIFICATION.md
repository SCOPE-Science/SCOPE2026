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

The public standalone script `burkhardt_critical_verify.py` uses Python 3 standard-library integer arithmetic only. Running `python3 burkhardt_critical_verify.py` from the extracted package verifies all 45 nodes, 40 planes, 360 incidences, a second geometric coordinate construction of the incidence matrix, the 45-by-45 Gram identity, graph connectivity, and the exact three prime-local Smith valuation distributions for reduced Laplacians with two different deleted vertices. It also checks their invariant factors against the spectral spanning-tree order.

Expected final line: `BURKHARDT_85_CRITICAL_GROUP_VERIFIED_OK`.

The exact computation exhausts this one finite incidence configuration; it does not establish any unproved infinite-family claim. The prime valuations come from invertible operations over rings \(\mathbb Z/p^{12}\mathbb Z\), with every pivot valuation less than \(12\). The separate order calculation establishes that no other primes occur. No external independent validation has been performed.
