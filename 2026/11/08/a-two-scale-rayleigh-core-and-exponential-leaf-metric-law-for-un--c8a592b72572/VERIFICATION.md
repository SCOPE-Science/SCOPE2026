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
The exact finite metric-reduction identity and deterministic peripheral inequalities were checked in independent, positive-integer edge-weight graph instances using all-pairs Floyd–Warshall on the full bipartite graph and separately on the reduced complete core. The reproducible `verify.py` uses a fixed seed and checks \(a=2,3,4,5\), \(b=1,\ldots,9\), and 17 instances for every pair of sizes. It also evaluates the exact two-hub survival formula \(\Pr(\sqrt b M>t)=[e^{-t/\sqrt b}(1+t/\sqrt b)]^b\) against the Rayleigh limit at multiple integer sample sizes, and checks the gamma-two small-tail inequality.

These finite checks are not an exhaustive proof of the stochastic limit. The proof in `RESULT.md` establishes the required pair-event estimates, joint upper-orthant limit, continuous-mapping closure, tightness and asymptotic independence for all fixed \(a\ge2\) and finite \(s\). There is no theorem in the package for variable core size or all peripheral distances jointly. Historical priority and independent mathematical review remain unverified.
