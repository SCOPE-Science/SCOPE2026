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

The standalone `VERIFY.py` replays exact-rational and symbolic checks. It confirms the negative-binomial coefficient identities through degree five, the finite exact boundary comparisons for eight refinement factors, and the five-vertex path's completed step computed by exact matrix inverses at two rational step sizes. It checks row sums and symmetry for the exhibited matrix. Execute `python VERIFY.py` using Python 3 and SymPy.

The analytic argument in `RESULT.md` separately proves the geodesic leading-term identity, existence and uniqueness of the negative leading-coefficient crossing, eventual positivity for every finite connected undirected graph, and the full \(d_r\sim\log r/\log\log r\) asymptotic. No finite simulation is treated as an infinite mathematical proof. A general claim about positivity at arbitrary intermediate steps, necessity of the diameter condition, and numerical floating-point robustness is not made.
