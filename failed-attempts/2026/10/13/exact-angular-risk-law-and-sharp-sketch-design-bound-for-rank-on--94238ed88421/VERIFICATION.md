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

Direct expansion with u=g/||g|| and v=(-u2,u1) gives the PSD rank-one residual ab vv^T/(a u1²+b u2²), whose Frobenius norm is its sole nonzero eigenvalue. The optimum Frobenius tail is b, so R=κ/[1+(κ−1)T] with T=u1². The Gaussian direction is uniform on the circle, T has the arcsine density, and inversion gives the claimed CDF (at κ=1 the law is a point mass). The first two angular integrals follow from tan θ substitution and differentiation in the two denominator coefficients. For q<1/2, t^(−q) is an integrable majorant against the arcsine law; for q>1/2, scaling t=s/κ on t≤1/2 gives the stated beta constant and the upper half contributes O(1). For q=1/2, the integral is (2/π)K(1−1/κ) in parameter convention, with endpoint log(4√κ)+o(1) for K, giving coefficient 1/π and bounded remainder. For any unit isotropic probe E[T]=1/2; strict Jensen gives equality precisely at constant squared coordinate energies, and the normalized independent signs attain it with zero cross moment. The statement is about a fixed known eigenbasis, not uniform benefit over unknown rotations. Replay: RESULT.md lines 4–64; the frozen VERIFICATION.md and verify.py were inspected without execution, and the finite checks described there are only corroborative.

## originality

FAIL

The decisive same-day FunNyström proof already gives the full unpowered two-eigenvalue residual as a function of the exact squared-normal ratio, not merely the first moment. Its one-pass, matrix-exponent-one specialization is the same random variable, and its deterministic formula applies to each nonzero probe. The additional frozen law and moment statements are evaluations or endpoint expansions of that explicit distribution; the isotropic-energy optimum is a direct Jensen corollary of the same pointwise formula. A materially distinct exact result is not established. This is statement-level overlap and implication, not a finding about which same-day record was first.

## value

FAIL

Contrast sensitivity and the square-loss comparison are useful benchmarks, but the frozen scope is exactly the previously exhibited two-eigenvalue directional formula. The displayed constants quantify its classical one-variable endpoint behavior, and the optimality statement is a scalar constant-energy Jensen equality in the known basis. This does not establish a nonmechanical additional risk or design result. In particular the sign sketch is not shown to be optimal without the known basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
