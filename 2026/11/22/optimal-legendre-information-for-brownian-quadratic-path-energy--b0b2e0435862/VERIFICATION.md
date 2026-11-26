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

The conditional path is a finite Gaussian mean plus an independent centered residual. Integrating its second moment gives the stated conditional estimator, and the Gaussian quadratic form variance is twice the squared Hilbert–Schmidt norm of the restricted Gram matrix. The total energy variance is 2∫∫min(s,t)² ds dt=1/3. Legendre orthogonality applied to the antiderivative formula, including f₀=t separately, gives the two parity chains and extra 0–1 edge. Compressing the sorted indices of each parity can only move each vertex to a larger diagonal weight and each existing chain edge to an earlier edge; consecutively selected vertices supporting any old edge remain consecutive. The 0–1 edge is never lost. The compressed score is a sum of strictly decreasing per-index rewards and a bonus attained by the prefix whenever m≥2. Strictness therefore proves uniqueness for every m, including m=1. The omitted diagonal and edge squares give precisely the two tails starting at m and m−2. The displayed partial fractions telescope to two boundary inverse squares plus a difference of reciprocals; restoring the two boundary edges gives the rational form and 1/(64m³). The Volterra Gram operator has cosine eigenfunctions with u′(0)=0 and u(1)=0; the Ritz values in any sensing subspace are bounded termwise by its eigenvalues. Equality is attained by the top eigenspace, whereas the polynomial span has a strictly smaller leading Ritz value because it does not contain the simple leading eigenfunction. The KL tail integral comparison and the risk ratio follow. Independently used exact polynomial recurrence, multiplication and integration for squared Gram entries through degree 8, enumerated all subsets of 0–8 for budgets 1–4, and checked prefix risks through m=6 (including 7/900 and 4/3675). The frozen verify.py was inspected, not run.

## originality

PASS

Pass for strict arbitrary-subset Legendre prefix optimality at all budgets and its exact risk and quantified ratio to the classical optimal-linear benchmark. Foster–Lyons–Oberhauser already give the exact two-coordinate conditional estimator and conditional-variance formula, so averaging the latter yields the same m=2 prefix risk, not a new isolated result. The KL machinery and generalized Fourier error calculus are also credited. The strongest distinct same-day records share the functional or nearby covariance but use point samples or a quantized observation, not the stated coordinate-bank design. No inspected stronger theorem yields the all-budget ordered-subset result.

## value

PASS

The Legendre bank is a standard structured source of exact Gaussian measurements. It is not automatic that its earliest coordinates optimize estimation of a nonlinear quadratic payoff, because capturing one of a pair without its partner loses the corresponding interaction. The theorem solves this allocation problem at every budget, gives exact risks, and measures the persistent factor of about 2.28 against optimal unrestricted linear information despite sharing the same decay exponent. This comparison is useful for choosing between a fixed polynomial bank and more flexible sensing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
