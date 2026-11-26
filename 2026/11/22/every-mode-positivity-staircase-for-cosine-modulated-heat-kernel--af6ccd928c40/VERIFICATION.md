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

The kernel depends on the difference coordinate; multiplying by its first cosine shifts the Fourier coefficients by ±1. Thus λ_j=a_j(1+βF_j) with a_j>0 and F_j>0, so the largest F_j sets the only cutoff for real β. For the angular extension, the log derivative is positive up to π/2. Above π/2, dividing by sin θ gives u−v²y tanh(v√(1−y²))/(v√(1−y²)) with y=−cos θ. The subtracted product strictly increases in y, because tanh z/z strictly decreases in z>0. This proves strict unimodality and that any adjacent sampled equality is a global and exclusively two-representative tie. For consecutive upper angles the log-ratio divided by 2t is −AΔcos plus the integral of tanh(2tw) over [B sin((j+1)h),B sin(jh)]; it strictly increases from a negative limit to −2A cos(jh)>0. At the π/2 straddle the same limiting expression is nonpositive when N≡0,1 mod 4; for finite times the integral is strictly below its limit. When N≡2 mod 4 the sine factors tie and the cosine exponential favors the higher mode; when N≡3 both factors favor it. The straddle and all smaller modes are therefore excluded. At an upper adjacent tie, every comparison to its left still points upwards by strict unimodality, forcing every corresponding lower-index transition to occur later. Reversing adjacent signs in that order gives all active modes and no skipped or simultaneous transitions. The single-candidate case J=M needs none; t=0 is excluded. Reflection pairs j with N−j, except the even Nyquist singleton, proving the stated boundary nullities and strict inequalities away from the boundary. Read the frozen checker without running it. A separate stable spectral-exponential check (`python3 /workspace/independent_checks.py 3`) checked 4,851 adjacent roots in their within-cycle order for N=3–200 and direct positional DFT for N=3–25; for N=12 it gave 0.2881787753 and 0.4028304687. These bounded floating-point comparisons are not proofs of the strict all-time inequalities.

## originality

PASS

Best of current knowledge, the signed lag-mask Fourier cutoff follows from standard diagonalization, but the finite nearest-neighbor cycle's complete order of active modes and exact tie multiplicities are distinct. Even the closest earlier sharp first-harmonic theorem uses geodesic-exponential continuous-circle coefficients, and the other all-mode staircases use different masks or spectra. The same-day Bessel analogue has a locked mode, not the finite heat staircase; no order is inferred from the date.

## value

PASS

Positive heat spectra alone do not ensure positivity after a signed lag mask. The smallest nontrivial harmonic mask already leads to a full phase diagram in time, with sharp permissible negative coefficient and exact degeneracies. A uniform no-skips theorem gives a usable covariance-design criterion and predicts which modes lose positivity without an all-mode scan of every cycle and time; it is more than a Fourier rewrite of the cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
