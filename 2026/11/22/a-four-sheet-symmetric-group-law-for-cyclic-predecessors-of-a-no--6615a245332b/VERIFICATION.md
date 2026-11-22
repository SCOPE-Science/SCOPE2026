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

The exact standalone checker is `check.py`; run `python3 check.py` from the package directory. It requires Python 3 with no third-party dependencies. The checker computes the complete transformation closure of two explicit maps on 16 states, the full two-letter transition graph, its kernel/image structure and primitive strongly connected components. It also independently exhausts original cyclic configurations of sizes 1 through 12 and compares every target's fiber size with the corresponding fixed-point transfer formula.

The infinite-length conclusion follows mathematically from the fixed-point correspondence, the finite monoid certificate, and the finite irreducible aperiodic Markov-chain convergence theorem. Small-ring enumeration alone does not prove the asymptotics. The checker does not establish the theorem for different local rules, optimal spectral rates, or independent mathematical validation.
