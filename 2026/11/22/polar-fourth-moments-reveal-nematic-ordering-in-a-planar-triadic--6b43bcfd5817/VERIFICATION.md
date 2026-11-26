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

The planar cosine-product identity gives one doubled-angle cosine per pair per third vertex. Thus the doubled-spin density has coupling c_N=c(1−2/N) and weight exp(c_N|S_N|²/(2N)); the undoubled signs conditional on all doubled angles are independent and fair. The exact Rademacher fourth moment counts three pairings and corrects the all-equal indices, yielding 2−2/N+|m_N|² conditionally. The second complex moment conditionally equals m_N, whose angular average is zero, so the planar covariance is exactly I/2. An editorial distinction: the formula's baseline 2−2/N is the pairing subtraction, not the actual independent-uniform-spin fourth moment 2−1/N. Relative to the latter the exact excess is E|m_N|²−1/N; the displayed finite-N and critical equations are correct as written. For the radial auxiliary field the likelihood-ratio argument gives strict decrease of I_1(r)/(r I_0(r)) from 1/2 to zero, yielding the stated maximizers; the tail is controlled by log I_0(r)≤r. Conditional log cos gives the planar Fourier exponent −|t|²/4−Re((t_1−it_2)²m_N)/4+O_K(N^−1), uniformly on each compact K. Averaging over the uniform direction and taking the radial concentration limit gives the Bessel mixture, whose fourth-coordinate-moment excess is 3ρ²/2 after standardization. At c=2, with h=N^−1/4 u, the finite-size quadratic shift is O(N^−1/2 |u|²); the log I_0 Taylor remainder is O(N^−1/2 |u|^6). On |h|≤δ both exponents are bounded above by −κ|u|^4 for fixed small δ and κ>0; the difference of their exponentials is controlled by this integrable bound times N^−1/2(|u|²+|u|^6). The complement has exponentially small contribution to the needed moments by the strict free-energy gap and Gaussian tail. The quartic law has E|u|²=8/√π. The exact conditional second moment of the doubled-spin sample mean is 1/N+(1−1/N)(I_1(|h|)/I_0(|h|))², giving E|m_N|²=2/√(πN)+O(N^−1). The conditional independent bounded summands give O(N^−2) fourth moment for the centered sample mean, and the field fourth moment is O(N^−1), hence E|m_N|⁴=O(N^−1). Expanding the angular I_0 factor at |t|²|m_N|/4 now gives |t|⁴/(32√(πN)) with the stated compact-uniform remainder. The supplied quadrature/sign-check code and recorded scope were read, not executed; the amplitudes and remainder were checked analytically.

## originality

PASS

The exact doubled-angle reduction, local gauge degeneracy, nematic transition and critical nematic moment coefficient are prior. The supported distinct claim is the distributional and moment theory for the undoubled polar sum in this canonical law: the finite-size fourth-moment identity, the full fixed-temperature Gaussian-mixture characteristic function, and its compact-uniform critical correction. The numerical critical coefficients use the known nematic amplitude and are not independent novelty claims.

## value

PASS

Because the first harmonic is commonly measured yet its covariance cannot diagnose the transition in this model, knowing exactly which higher-order statistic detects the director is useful. The result also determines when Gaussian modeling of that observable fails, identifies the mixing mechanism, and separates a Gaussian critical limit from its leading non-Gaussian finite-size correction. This is specific to the zero-field canonical law; it makes no claim about noisy measurements, dynamics or ensembles in a field.

The dated certificate retains the supplied scientific assessment, sources and limitations.
