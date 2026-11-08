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

# Reproduction and limits

Execute the embedded `verification/ctmc_cycle_checker.py` using standard Python 3.10 or later. It requires no third-party packages and works entirely in exact rational arithmetic. The script enumerates all immune subsets and possible susceptible second index infections, computing expected final recoveries from CTMC first-step equations with infection propensity \(\beta\) times infectious-neighbor count and recovery propensity \(\gamma\) per infectious person. It directly compares those results to the theorem's polynomial, rather than using the polynomial within the recursion.

The saved checker passed all \(30\) comparisons on \(4\le n\le8\), every admissible \(k\), and \((\beta,\gamma)=(1,1),(2,3)\), as well as \(30\) saturated-limit combinatorial identities. These are independently implemented finite spot checks, **not** an exhaustive proof for arbitrary population sizes or symbolic parameter values. The proof of the general identities and limiting formulas appears in RESULT.md.

The 2026 motivating preprint was examined in its openly readable HTML version for its network CTMC dynamics, immunity protocol and spatial-network results; Ferrari et al. and Hiraoka et al. were also compared. Prior qualitative results are acknowledged. This item has not undergone an independent audit or external validation.
