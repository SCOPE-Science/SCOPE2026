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

# Reproducibility
Run `python3 verify.py` using Python 3 with its standard library. The verifier performs exact arithmetic checks of the Fibonacci divisibility formula for \(1\le i,d\le160\) and checks finite Beatty samples using `math.isqrt` (not floating point). The independent inputs are the elementary power recurrence and the explicit theorem predicate. An empty finite intersection is not used to infer global disjointness. The global proof invokes the stated Skolem–Bang theorem and the Fibonacci strong-divisibility identity, both externally established results. No external or independent validation has been performed.
