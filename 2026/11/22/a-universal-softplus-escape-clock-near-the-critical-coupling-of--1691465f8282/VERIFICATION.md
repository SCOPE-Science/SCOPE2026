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

The invariant antidiagonal gives u_{n+1}=u_n(1+h_ε(u_n))², h_ε(u)=2ε+a(u−1)e^(−u), with u_0>2. The increments are at least 4εu_n, so all defined targets are eventually crossed. The zero-detuning contribution is strictly decreasing in h for u>2, giving a unique balance root U>2 and U−log(U−1)=log(a/(2ε)); this gives the stated two-term root asymptotic. Writing λ=4εU, the root relation makes q_ε(U+w)/λ→1+e^(−w) uniformly on compact w. For each fixed layer boundary, increments below it are eventually less than 1 past a sufficiently large fixed cutoff, and below the cutoff the images are bounded; thus the crossing originates within a bounded w-window and has overshoot O(λ). The reciprocal-increment Riemann sum therefore gives the compact layer integral. Before the layer, the fixed-cutoff crossing takes bounded time, and the decreasing lower bound q_0(v)=2av(v−1)e^(−v) supplies 1≤∫_v^{v+q_ε(v)}ds/q_0(s); multiplication of the resulting integral bound by λ gives limsup at most e^(1−L) at U−L. Sending L to infinity yields the clock. Bracket a fixed τ between the limiting clocks of two offsets on either side of log(e^τ−1) to justify the floor-time inverse. No off-antidiagonal or τ=0 assertion follows. Read VERIFICATION.md and verify.py without executing; the finite floating-point checks are supplementary, including the bisection root check, not exact computations or a limit proof.

## originality

PASS

The supported distinct claim is the positive-detuning joint limit with its entire finite-offset profile. The fixed-critical escape law, the balance-root scale on the opposite side and the underlying coupled map are already known; none of the compared statements determines this clock.

## value

PASS

This determines the actual time dependence across the competition between exponentially small Gaussian drift and positive detuning, rather than merely locating their balance or proving escape. The scale and exact clock allow predictions at fixed offsets or times with no fitted dependence on the gain or fixed starting radius. The result fills a concrete neighboring regime of the known critical law, though only on the invariant antidiagonal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
