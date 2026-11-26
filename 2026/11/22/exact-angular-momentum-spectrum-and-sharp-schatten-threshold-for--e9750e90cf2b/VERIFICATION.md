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

Reconstructed RESULT.md lines 28–67, including the sign, domains and counting constant. For a degree-l solid harmonic, Fischer decomposition of x_j H gives a degree-l+1 harmonic and r^2 times (2l+d-2)^(-1) partial_j H. Radial projection replaces r^2 in the latter summand by its beta-moment ratio (l+d/2-1)/(l+d/2+beta). The two raising steps commute since their composite is the top-degree Fischer harmonic part of x_i x_j H; the two lowering steps commute by symmetry of partial derivatives. The antisymmetric cross terms are J_12/(2l+d+2beta) and -(1+2/(2l+d-2))J_12/(2l+d+2beta+2), giving -q_l J_12 for all l>=1. Constants are killed. The Fischer character cancels the radial factor (1-t^2); the coefficient of rotation weight m is t^|m|/(1-t)^(d-2), recovering the exact signed multiplicities, infinite kernel and norm O(l^-2) per block. For c=(beta+1)/2 and grid step h=sqrt(t/c), set y=h l, x=h m. Off the coordinate and threshold boundaries the rescaled counting condition tends to 0<x<=y, x>y^3 and the scaled weight tends to (y-x)^(d-3)/(d-3)!, with bounded support and uniform polynomial bounds. This is a Riemann sum with a measure-zero boundary; x=u y gives 0<u<1, 0<y<sqrt(u), and integration in y divides by d-1, yielding the displayed beta integral. For d=3 the binomial weight is exactly one. For the degree-critical trace, u^((d-1)/2)(1-u)^(d-3) is Lipschitz on [0,1]; its degreewise Riemann error, combined with the 1/l expansion of q_l and the binomial weight, gives summable O(l^-2) corrections to (d-1)K/l. Inverting the counting asymptotic and integrating the positive singular-value distribution give the asserted sequence law, strict endpoint, Hilbert–Schmidt cases and K in d=3. The uploaded check.py was inspected but not run; its selected polynomial and dimension comparisons are bounded diagnostics, not the proof.

## originality

PASS

The strongest direct catalogue analogue is the weighted harmonic disk monomial self-commutator at m=1. It gives exactly the real-coordinate pair in dimension two after multiplying by -i/2, but its one-dimensional signed Fourier sectors do not give the rotation-weight branching and all-degree coefficient in real dimensions d>=3. The inspected real-ball Toeplitz results supply boundedness, compactness and general setting or criteria, not the exact higher-dimensional compact spectrum and sharp counting coefficient. Priority remains best-of-knowledge, with limitations below.

## value

PASS

The two real coordinate compressions are canonical Toeplitz operators, and their commutator quantifies a concrete failure of commuting multiplication to survive harmonic projection. The exact angular formula resolves the nonzero levels, degeneracies and kernel, and the explicit Weyl constant and critical logarithmic trace distinguish Hilbert–Schmidt behavior across dimensions. These data could be needed to compare other harmonic compressions or spectral estimates; they are not supplied by compactness alone or an arbitrary finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
