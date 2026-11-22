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

The proof establishes the result for every integer \(N\ge1\) by exact Farey interval lengths, finite Möbius inversion, and absolutely convergent Dirichlet-series differentiation at \(2\). The classical Farey-neighbor characterization is an acknowledged input, not a novelty claim.

Run `python3 verify.py`. This performs exact rational checks of all carry profiles in Farey cells for \(2\le d\le55\), compares interval lengths to inverse-residue sums, and verifies 55 exact finite-\(N\) Möbius--harmonic identities. The executable tests cover only the stated finite ranges. The harmonic estimates and analytic remainder bound are arguments in RESULT.md rather than consequences of those tests.

The mathematical priority claim remains conditional on literature coverage beyond the sources actually inspected; no independent validation has been performed.
