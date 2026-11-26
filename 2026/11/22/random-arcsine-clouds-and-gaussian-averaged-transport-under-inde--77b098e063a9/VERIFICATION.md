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

With the stated order of the free step and kick, Fourier evolution multiplies by exp(2ih cos(k+q_j)) after shifting the previous state to k+q_j. Iterating from the constant transform gives the suffix phasor S_n. The inverse transform gives J_m(2h|S_n|)^2; symmetry gives conditional mean zero, and Fourier derivative Parseval gives variance 2h^2|S_n|^2. Summing the phasor correlations r^|j−k| yields exactly the finite-time variance including the negative transient. The forward phasor martingale differences have squared norm conditional mean 1−r² and pseudovariance (r^4−r²)U_(j−1)^2. The positive wrapped-Gaussian density makes the circle walk uniformly ergodic, so the average pseudovariance vanishes and the real covariance limit is isotropic. The telescope divides the limit by 1−r, giving variance alpha/2 in each coordinate. The reversal is only used in distribution; equivalently the radius equals that of the forward sum from U_0 to U_(n−1), pathwise. Rayleigh radius and exponential normalized variance follow. For any deterministic radii s_n→s, the characteristic functions J_0(4h sqrt(n) s_n sin(k/(2 sqrt(n)))) tend to J_0(2hsk), so the corresponding measures converge weakly (including s=0). Applying this to any Skorokhod coupling of the convergent random radii proves convergence in distribution of the conditional measures. A uniform angle independent of the Rayleigh radius yields the first coordinate of a circular Gaussian, proving the claimed annealed variance 2h² alpha. Bounded differences give uniform scaled higher moments, justifying the reported variance-fluctuation moment limit.

## originality

PASS

The same Gaussian-slope kick protocol, phasor and asymptotic averaged width are already in Wang; coherent Bessel propagation and generic annealed quantum-walk CLTs are also prior. The supported distinct result is the joint distributional description for the delta launch: a random weak arcsine profile with Rayleigh radius and non-self-averaging exponential width, together with the exact annealed Gaussian limit. The inspected results do not supply that description or its implications at this scope.

## value

PASS

A single diffusive width or an ensemble Gaussian could suggest an individual run has a similar cloud. The result gives instead an order-one distribution of widths and the exact shape of a conditional profile on the same spatial scale, and explains how their mixture produces a Gaussian. These are quantitatively useful for deciding whether averaging over histories is essential in this model, rather than an additional fit of the known variance slope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
