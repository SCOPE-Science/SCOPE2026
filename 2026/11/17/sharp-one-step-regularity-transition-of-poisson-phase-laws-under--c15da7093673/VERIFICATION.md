---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For T(theta)=theta+omega-s sin(theta+gamma), derivative 1-s cos gives analytic diffeomorphism for |s|<1, one order-three degeneracy at |s|=1 with third derivative equal to 1, and two nondegenerate folds for |s|>1 with absolute second derivative sqrt(s²-1). Poisson-law-to-Poisson-law orientation-preserving homeomorphisms must be Möbius because conjugation by boundary automorphisms preserves Haar and hence is rotation. A nonrotation Möbius derivative has a second harmonic absent from 1-s cos; only s=0 closes. Change of variables yields the critical cusp coefficient 2P_a(c)/6^(2/3), fold coefficient P_a(c)sqrt(2/absolute second derivative) and strict L^p cutoffs 3/2,2. Independent numerical local cubic ratios at source displacements 0.06,0.03,0.01 are 1.03390,1.01737,1.00588 and converge correctly. These checks corroborate the analytic asymptotics, not the all-s proof.

## originality

PASS

The complete 2026-11-08 published weak-kick circular-cumulant result proves only fixed-order O(s²) moment defects for small kicks and cannot imply regularity at |s|>=1. The motivating 2026 Kuramoto abstract already notes qualitative nonclosure and provides transfer equation; generic fold and cusp exponents and invertibility threshold are old, but the joint exact Poisson density one-step all-s classification, coefficient and integrability statement is not shown in inspected sources. Best-of-knowledge pass with original primary full text unavailable.

## value

PASS

A single sharp one-step regularity phase diagram for the noninvertible sine kick of Poisson ensembles, including model-specific density coefficients, L^p thresholds and all-amplitude nonclosure, provides a motivated diagnostic for discrete phase dynamics beyond qualitative Ott-Antonsen failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
