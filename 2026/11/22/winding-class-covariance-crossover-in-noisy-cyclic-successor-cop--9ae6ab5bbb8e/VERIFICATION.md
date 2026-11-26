---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Positive rate a of independent uniform refresh makes the finite chain irreducible, so rotation and common colour-shift invariance follow by uniqueness and the Fourier mean vanishes. A copy at the first marked site contributes ω C_(d−1)−C_d, one at the second gives conjugate(ω) C_(d+1)−C_d, and the two refreshes contribute −2a C_d. This includes d=1 and n−1, where one predecessor coincides with the other marked site and its product becomes 1 before the phase. Demodulation gives the scalar recurrence R_(d+1)−2(1+a)R_d+R_(d−1)=0 with R_0=1 and R_n=ω^(−n), since C_n=C_0=1. The two real distinct roots exp(±κ) give the stated unique sine-hyperbolic interpolation. With fixed q, nκ→sqrt(2c) along the residue sequence, including limits at x=0,1; the subsequent c↓0 limit is the chord between 1 and ω^(−r). Its interior modulus is strictly less than 1 for r≠0, since these endpoints are distinct. 'Complex' describes the codomain, not a claim of a nonreal value in every sector: for even q and r=q/2 the profile is real. A separate 81-state generator at n=4, q=3, a=1/2 gave maximum absolute correlation discrepancy 2.49e−16 over d=0,…,4; the theorem rests on the analytic calculation, not that test.

## originality

PASS

The distinct assessed result is the complex holonomy-dependent two-point function and its residue-sensitive diffusive crossover on this directed ring, not generator moment closure or the solution of an ordinary untwisted noisy-voter recurrence. No inspected prior statement gives or dominates the winding-resolved result.

## value

PASS

The deterministic shift forces a natural global compatibility question: one circuit can accumulate a nontrivial colour phase despite identical local update rules. The formula resolves exactly how uniform refresh competes with this phase on the n^−2 scale, and separates unit-coherence and frustrated sectors in the weaker-noise limit. This is an explicit observable that distinguishes winding classes even though their local dynamics agree, not merely a reformulation of an ordinary periodic recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
