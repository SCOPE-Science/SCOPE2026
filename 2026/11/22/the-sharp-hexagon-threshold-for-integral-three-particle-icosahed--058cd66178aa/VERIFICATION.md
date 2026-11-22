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

## Reproduction

With Python 3 and the two co-located files `verify_icosa.py` and `BASIS_CERTIFICATE.json`, run `python3 verify_icosa.py`. It requires only the standard library and processes an explicitly encoded 30-edge graph. Its success marker is `EXACT_ICO_3PARTICLE_TORUS_THRESHOLD_OK`.

## Checks performed

The actual check reconstructed a 14,080-column, 31,680-row reduced degree-three differential and found rank 13,970 over the two-element field, using a complete deterministic bitset elimination. It enumerated exactly 700 triple-cycle tori, checked the integral boundary of every one, found 110 integral unit pivots (100 triangle triples and 10 triangle–triangle–hexagon triples), and verified all shorter tori lie integrally in the first 100 span. The resulting unit triangular coordinate minor proves primitivity of the full lattice, not merely rational independence.

## Scope of the certificate

The rank bound uses exact arithmetic in one finite field together with a matching collection of integral unit-pivot cycles. This combination proves the integer top-degree theorem; finite-field rank alone would not. No computation concerning lower-degree homology or a geometric homotopy equivalence is asserted. Independent audit has not been performed.
