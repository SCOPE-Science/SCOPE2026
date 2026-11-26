---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a unit direction the length is min(2a/√(1−U_z²),2b/√(1−U_x²)). Let R=√(a²+b²). The absolute coordinate marginals are uniform; the signed pair projects to the unit disk with density 1/(2π√(1−z²−x²)). Hence the central-band overlap is (2/π)∫₀ˢ arcsin(t/√(1−z²)) dz when s²+t²<1. Integration by parts followed by z=√(1−t²)sin φ gives the stated elementary expression. Below 2b only the a-constraint has positive probability of limiting the chord at the threshold; at 2R the strict absolute-coordinate survival inequalities cannot both hold, and equality is attained at |U_x|=a/R, |U_z|=b/R. Every interior length is attained by continuity. There are no atoms. On the interior two-constraint branch, conditioning on |U_z|=s or on |U_x|=t and differentiating its marginal threshold gives the two joint length/contact densities, since ties have spherical measure zero. The factors in brackets can be written as (2/π)arctan(√Δ/t) and (2/π)arctan(√Δ/s), respectively, with Δ=4R²/l²−1. Thus as l=2R−ε, the densities are asymptotic to a√Δ/(πRb) and b√Δ/(πRa), giving the limiting proportions and, on integrating their sum, 2√R ε^(3/2)/(3πab). At 2b the first marginal changes by O(ε); the second opens with t∼√(ε/b), multiplied by 1−(2/π)arcsin(√(1−a²/b²))=(2/π)arcsin(a/b). The lower endpoint follows directly from s∼√(ε/a). This independently fills in the abbreviated upper-tail calculation. The supplied numerical checker was inspected, not executed; no Monte Carlo evidence is needed for these identities.

## originality

FAIL

The unequal-cylinder interpretation is not stated in the strongest read sources, but the exact law is covered by their spherical two-cap overlap. Mazonka Eq. (45) at axis angle π/2 directly gives the upper survival probability, and the earlier Resultary box record explicitly gives the same two-coordinate exceedance function at arbitrary thresholds. The cylinder labels select the two ordinary partial derivatives of this known function; the threshold and endpoint constants are the immediate small-argument expansions of those derivatives and the single-coordinate marginal. Thus the exact mathematics, not merely a method or analogous exponent, is covered as a specialization.

## value

FAIL

The central sampling model is natural, and the contact notation is useful. Nevertheless, the known exact joint cap survival already evaluates the nontrivial branch, and the marks and singular coefficients are obtained by taking its two partial derivatives, applying the threshold derivatives and expanding the elementary factors. Those interpretations do not leave a distinct exact invariant or nonroutine mathematical gap in the delivered claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
