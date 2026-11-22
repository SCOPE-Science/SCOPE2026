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

Run `python3 verify.py` using the Python standard library. The exhaustive finite test visits all edge-subsets for graph sizes \(3,4,5,6\), checks connectivity after deleting zero or one vertices, and checks all fixed faces under every nonidentity rotation. The expected final line is `PRIME_SEPARABLE_GRAPH_QUOTIENT_SANITY_OK`.

Verified face totals: \(6,53,785,21399\). Verified Euler characteristics: \(0,-1,-5,-23\). Rotation action is free for the checked primes \(3,5\) and not free for checked composites \(4,6\). For \(p=5,7,11\), the verifier checks the number and degrees of cyclic-homology and cohomological-power predictions. The all-prime result instead follows from the written graph-orbit proof and the original general sphere-wedge theorem in the references; finite verification must not be interpreted as proof of arbitrary primes. No full integral homology calculation in degrees at or above \(2p-5\) has been performed.
