---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The averaged gradient is the Gaussian convolution of the centered arcsine law of radius A, with A=0 giving a single Gaussian. It is analytic and even, with negative first derivative for x>A. For A>0 the bounded approximants have derivative measures with signs +,−,+,− in order (the outer signs are endpoint atoms). The Gaussian variation-diminishing result applies to these finite measures, with the uniform derivative limit following from L¹ convergence. The bound can also be checked directly: after factoring the Gaussian, four distinct zeros of a convolved approximant derivative would give four exponentials orthogonal to the derivative measure weighted by e^{−y²/(2σ²)}. A nonzero combination vanishing at −A,0,A has only these three zeros and all are simple, by the Rolle induction for distinct real exponentials. It has opposite signs on the two interior intervals and kills both atoms, so its integral against the weighted measure cannot vanish. Thus the limiting derivative has at most three sign changes. Symmetry and its eventual negativity give exactly the claimed maxima once the near-center derivative sign is fixed; zeros without sign changes cannot add extrema. The circular-mean identity reduces the central curvature to e^{−u}[(2u−1)I₀−2u I₁]/(sqrt(2π)σ³). For u>1/2 each zero of d=1−1/(2u)−I₁/I₀ has d′=1/(4u²)>0, and d is negative at 1/2 and positive at 1, so there is only one zero. At that root the Bessel bracket B has B′=I₀/(2u) and B″=−I₀/(2u²); applying σ⁻²(u∂²_u+∂_u) again gives p_A⁽⁴⁾(0)=−p_A(0)/σ⁴, settling strict unimodality at equality. Separate rational positive-series bounds with geometric remainders verify opposite bracket signs at 7899784/10⁷ and 7899785/10⁷, and numerical bisection gives u≈0.78997842134357 and A/σ≈1.77761460541206. The frozen CHECK.py was inspected, not executed. The strictly positive mean gradient and Gaussian symmetry prove the single midpoint crossing regardless of mode count.

## originality

PASS

Both the arcsine averaging reduction and the Gaussian variation bound are covered by prior mathematics. The distinct result assessed here is the sharp one-to-two modal classification for this particular arcsine–Gaussian convolution, with its unique Bessel-ratio root and strict quartic equality regime. The inspected close catalogue analogue uses a different smoothing law, and the inspected general theorems do not determine the central sign or the unique threshold. A plausible signal-processing lead remains unresolved rather than treated as negative evidence.

## value

PASS

This is a quantitatively sharp diagnostic for interpreting a plausible averaging artifact: a single translating interface can give two averaged gradient peaks without adding any median salinity crossing or instantaneous interface. The critical amplitude relative to the intrinsic width and the strict equality case decide whether this can happen for the specified model, rather than merely giving a numerical counterexample. The all-parameter mode bound also excludes more complex false profiles in this specific setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
