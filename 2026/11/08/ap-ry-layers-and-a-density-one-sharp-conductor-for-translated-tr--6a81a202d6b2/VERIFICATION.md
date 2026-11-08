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

The exact Apéry formula was checked by an independent residue-graph shortest-path computation implemented in `verify.py`. The code computes actual shortest path weights rather than reusing the proposed triangular-number criterion. Direct comparisons were made for all parameters from 2 to 300 and eight additional parameters up to 2000, totaling 51,992 nonzero residue classes. The checker also tests the genus sum and the sharp conductor equality criterion for each parameter. The infinite theorem and density-one conclusion are proved in `RESULT.md` using Gauss's theorem and the Landau–Ramanujan bound. Finite checks do not establish an infinite asymptotic, nor do they replace review of the published literature.
