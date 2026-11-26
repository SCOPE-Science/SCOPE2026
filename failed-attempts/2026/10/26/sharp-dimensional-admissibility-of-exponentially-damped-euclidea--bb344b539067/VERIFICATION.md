---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

I independently obtain the transform by writing k(r)=Im(e^(−cr)/r)/ω for c=a−iω. For real c>0 the Gaussian integral e^(−cr)/r=π^(−1/2)∫₀^∞ t^(−1/2)exp(−tr²−c²/(4t))dt gives Fourier transform (4π)^p Γ(p)(s²+c²)^(−p) in dimension 2p+1. The identity extends to Re c>0 by domination on compact subsets and the identity theorem; the denominator does not vanish there. This recovers the frozen normalization and confirms its Bessel recurrence calculation. The negative argument of s²+c² runs strictly upward from −2 arctan(ω/a) to zero; hence the displayed sine gives exactly the interior zeros and sign changes, with an endpoint zero at s=0 when the phase is a multiple of π. The density is everywhere nonnegative precisely when the upper positive phase is at most π and has a negative open band otherwise. At the admissible boundary it is positive for all s>0. Bochner and Fourier uniqueness give the finite Gram-matrix criterion, and strictness follows because a nonzero combination of characters at distinct locations cannot vanish on an open frequency set (restrict to a line with distinct projections and use the Vandermonde equations).

## originality

FAIL

The sharp criterion and complete spectral phase are covered by an explicit specialization of the earlier Resultary phase–frequency cone, despite the different spatial formula. Let m=d−2=2p−1, z=a−iω and use the prior damped cosine-plus-sine kernel in dimension m with coefficient β=a/ω (its upper coefficient face). Its spectral formula is c_m Re[(1−iβ)z(s²+z²)^(−p)], with c_m=2^m π^((m−1)/2)Γ((m+1)/2). Since (1−iβ)z=−i(a²+ω²)/ω and (4π)^p Γ(p)=2πc_m, the frozen density in dimension d is exactly 2π/(a²+ω²) times the prior density in dimension m, for every radial frequency and parameter pair. Thus all signs, zeros and boundary cases agree. The prior criterion on this face is (m+1) arctan(ω/a)≤π, exactly the frozen criterion. Its phase proof on this face is the identical sine-sign calculation. The earlier finding need not mention sinc to imply this result. This is a coverage finding based on exact passages, not an adverse inference from unavailable papers or empty searches.

## value

FAIL

The damped wave kernel is a natural object and the threshold is mathematically correct. But as a standalone new result, its whole admissibility diagram and finer spectral signs are a direct dimension-index and coefficient specialization of a known exact phase theorem. The separate proof and spatial formula do not supply a new structural gap, sharper boundary, or independently useful unknown invariant beyond that mechanically implied corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
