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

The standalone source `verify_universal_fixed_nsc.py` is part of the same package; run with Python 3 standard library only. Its recorded output is `verify_universal_fixed_nsc_output.txt`.

Five explicit finite input complexes were evaluated. Each arithmetic graph construction was regenerated from the input facets. For all tractable step subsets, explicit directed reachability was compared with the gcd-based connectivity criterion. The simplicial fixed-set face collection was compared exactly against the union of its full prime-divisibility simplices and the nerve against the input face collection. Independent bitset boundary ranks over \(\mathbb F_2\) reproduced their known reduced Betti numbers: zero for a simplex, rank one in reduced degree zero for a disconnected edge and point, rank one in degree one for a triangular circle and four-cycle, and rank one in degree two for a tetrahedral sphere.

The general result depends on proved arithmetic and simplicial lemmas plus Hultman's published Theorem 4.3. Computations are finite examples, not an infinite proof. No independent mathematical audit, publisher-level priority determination or certification is represented here.
