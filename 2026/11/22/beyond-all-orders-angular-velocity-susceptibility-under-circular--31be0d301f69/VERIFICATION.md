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

For the explicitly defined forward radius-normalized angular momentum, weak coupling first gives the bounded observable of independent Gaussian noises added to a circle of radius a=R exp(−s), with variances v_i=T_i(1−exp(−2s)). Continuity of the nondegenerate age-conditioned Gaussian law and bounded convergence justify the susceptibility. The circular complex angular average has a residue only for |z|>a; at |z|=a the pole is removable. The anisotropic Gaussian polar integral then has the stated I₁ factor, strictly positive except when the temperatures coincide, with the stated sign. A direct endpoint check sets x=(ρ²−a²)/(2v₊). After factoring exp(−a²/(2v₊)), scaling the remaining amplitude using I₁(z)exp(−z)~(2πz)^(−1/2) gives an integrand dominated by a constant times x exp(−x), with limiting integral 1. The amplitude is 2√(2/π) v₊²/[a³√(v₊−v₋)]. With c=R²/(4T₊), the exponent is −c/s+c+O(s), so the positive magnitude of A(s) is asymptotic to 8T₊² exp(c)s^(3/2) exp(−c/s)/(R³√(π(T₊−T₋))). The K_{5/2} integral gives √π c r^(−1/2) exp(−2√(cr)) after multiplication by r; the large-age error is exponentially negligible and the relative small-age error is bounded by the corresponding positive integral. These factors give the frozen prefactor. The second-moment integral gives the momentum susceptibility separately. This verifies the observable defined in RESULT.md, not a different definition based on the generator acting on a polar-angle branch or on reset chords. The supplied notes and checks/verify.py were inspected but not executed.

## originality

PASS

Pass for exact circular interior cancellation, definite finite-rate weak-coupling sign, and the sharp beyond-all-orders velocity susceptibility with prefactor, not for the renewal law, the angular-velocity definition, circular angular momentum, or a coarse zero high-reset limit. The strongest distinct indexed result shares the observable and gives zero limiting velocity for a single radius, but does not resolve the rate or ordered susceptibility.

## value

PASS

The exact erasure is a mechanism, not just a vanishing leading Taylor coefficient: it explains why many small, ordinary excursions contribute nothing and why the response selects exponentially rare boundary crossings. The sharp time-scale exponent and prefactor distinguish the specific angular velocity from the ordinary angular momentum in the same reset model, which has an algebraic susceptibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
