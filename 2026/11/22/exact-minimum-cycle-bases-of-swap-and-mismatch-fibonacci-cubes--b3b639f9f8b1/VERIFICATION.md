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

Run `python3 verify.py` in the directory containing the accompanying standalone checker. It enumerates admissible words and both edge types for each \(1\le n\le11\), checks that triangles uniquely match swap edges, and computes binary ranks of replacement-square and joint triangle-square incidence vectors. Its reported ranks equal \(H_n-F_{n+2}+1\) and \(H_n+T_n-F_{n+2}+1\), respectively. Exact Fibonacci edge counts and the minimum-basis length identity are checked at every enumerated size. The cases \(n\ge12\) are covered by the mathematical proof, not by the finite enumeration. The enumeration checks ranks and formulas, not an independent optimized cycle-basis solver. Independent audit has not been performed.
