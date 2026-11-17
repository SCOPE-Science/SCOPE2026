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

# Reproduction and scope

Run `python verify.py` from any directory with a standard Python 3.10+ interpreter. The program is self-contained, uses only `fractions`, `itertools`, `math`, and prints `VERIFICATION_OK 451620` upon success.

The verifier independently recomputes the exact squared coordinate and induced-subgraph supporting-plane distances for every integer \(4\le n\le500\), checks the phase change and uniqueness of the closest centered facet orbit, determines ranks of projected coordinate and singleton-cut normal systems through \(n=10\), and enumerates all labeled spanning trees by Prüfer sequences for \(n=4,5,6\). For the latter it evaluates all proper induced-subgraph inequalities. The verifier also constructs a nontrivial degree-preserving four-cycle perturbation of the uniform center and checks all shifted inequalities for \(n=4,5\).

**Analytic proof versus finite checks.** The exact all-\(n\) assertions are deduced in `RESULT.md` from orbit averaging, a sign calculation for a rational derivative, a quadratic threshold comparison, and the rank of the unsigned complete-graph vertex-edge incidence matrix. Finite enumeration and rank tests only guard against normalization and algebra mistakes. The claim does not rely on exhaustive checks beyond the tested dimensions.

No computer algebra server, notebook state, proprietary data, external package, or third-party full paper is required to reproduce the checks.
