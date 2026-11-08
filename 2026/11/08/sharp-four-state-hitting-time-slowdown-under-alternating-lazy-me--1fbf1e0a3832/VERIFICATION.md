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

The executable `verify.py` is a standalone Python 3 script requiring no third-party packages. It enumerates all \(2^{\binom n2}\) labeled simple graphs for \(n=2,3,4\), checks connectivity by finite reachability, builds the lazy symmetric Metropolis kernel using exact rational edge weights, and checks row sums, symmetry and laziness. It solves the two-phase absorbing linear system for every graph pair, start, target and initial phase, verifies rational residuals and compares against both static chains. Unordered graph pairs plus both phases exhaust all ordered pairs.

Actual completed replay: `VERIFY_OK` with counts \((1,4,38)\) connected graphs; respectively \((4,120,17784)\) comparisons; \((0,0,168)\) strict slowdown cases; maximum ratios \((1,1,646/607)\). The maximum on four vertices is attained in 24 labeled phase cases. A separate direct six-state augmented-system solve reproduces the explicit cycle/paw witness and both static hitting vectors.

The certificate is a finite exact census only. It does not extrapolate to higher graph orders; no Monte Carlo approximation or timeout is used as evidence. Published prior-work comparison does not establish independent historical priority. Independent external validation has not been performed.
