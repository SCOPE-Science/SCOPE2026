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

The compact block perturbation and the exact block eigenvalues give the asserted full, point and approximate-point sets. The scalar limit over blocks is approximate spectrum but not an eigenvalue, for both the generator and each t>0; the real exponential moduli keep the block eigenvalues distinct from that limit. A fixed nonzero block diverges forward and its inverse block tends to zero, so every nonzero orbit diverges and equal-clock closeness is impossible for distinct states. At fixed time the blocks approach a rotation, ruling out uniform exponential expansion. The shear minimum singular value gives the exact sampled infimum. For γ<β, the rescaled objective has profile (a^q/c)e^x x^(−q), with minimum at x=q. The lower bound e^x/(t^(−(1−q))+ca^(−q)x^q) diverges along t→∞ and x→0 or x→∞; this joint-limit statement is the localization needed, not divergence at zero for a fixed time. The sampled infimum is attained for large t since the block tail tends to one and the trial value tends to zero. At γ=β differentiation gives the stated minimum and dense asymptotic sampling; at γ>β all but finitely many blocks are accretive and the exceptional block minima tend to infinity. For γ≥β the checked sufficient theorem applies. Independently, after pulling back by T(−t), uniform positive minimum modulus bounds the shift discrepancy; the bounded-below generator gives a short-time linear displacement lower bound and continuity pins s(t)−t in a small interval. Along a convergent sequence of shifts at times tending to infinity, each fixed-block inverse tends to zero, giving equality of the two orbits at the limiting short shift. For γ<β the phase period makes the lag initially invisible to O(n^(−β)+n^(−γ)); during the switch both trajectories are small by the explicit shear cancellation, and after the switch they coincide. The non-unit moduli at nonzero time in the selected block exclude every smaller orbit lag. This proves failure for increasing homeomorphisms as claimed.

## originality

PASS

The established distinct claim is the exact opposing Bowen–Walters regimes with identical spectral sets in this nonnormal Jordan family, the lag-switch counterexample, and the sharp lower-modulus asymptotics. The positive half is an application of a credited sufficient criterion; generic spectrum-versus-expansivity separation and diagonal/operator analogues are not claimed as new.

## value

PASS

A common elementary compact-perturbation model now separates the exact time-change dynamical property while retaining generator and all fixed-time full, point and approximate spectral data, and even retaining kinematic expansiveness on both sides. The transition is measured by a quantitative lower-modulus trichotomy and proved on its difficult side by an explicit time-change mechanism. This is a useful test case against attempting to decide the dynamical property from spectral sets alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
