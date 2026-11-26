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

The centered increasing test vector has jumps 1 except 2r at the center, so its Rayleigh quotient bounds every feasible allocation, not merely symmetric ones. The prefix identity w_i(x_{i+1}-x_i)=-lambda sum_{j<=i}x_j gives the positive candidate, and with these weights all the vertex equations follow by differencing. Since the resulting tridiagonal Laplacian is irreducible with negative off-diagonal entries, its no-zero-component eigenvector with exactly one sign change is the second mode. Equality in the Rayleigh principle forces the same test vector and hence the same weights for any other optimizer. Summation gives B/u=1+2(m-1)r(r+(2m-1)/3)/(r+(m-1)/2), increasing from B/u0 at r=1/2 to infinity. The candidate saturates the budget on both branches; when r=1/2 the parabolic weights give u0. The affine cap bound [B+(4r^2-1)u]/V_m(r), at fixed r, supports the value function from above at contact. On 0<u<u0 the implicit solution is differentiable, so the derivative equals (4r^2-1)/V_m(r)>0 and goes to zero at u0, joining the constant regime. Solving the budget equation at small u gives r=B/[2(m-1)u]+O(1), yielding the stated second-order expansion. Independent finite tridiagonal eigensolves and finite differences in /tmp/opencode/frozen_1_2_3_checks.py included m=3,B=19,u=3 with gap 1 and cap derivative 3/28. Inspected the uploaded exact verifier without executing it.

## originality

FAIL

Sun, Boyd, Xiao and Diaconis (SIAM Review 48 (2006), 681–699) give the unique exact fastest continuous-time allocation on paths with arbitrary positive edge prices, not just uniform prices or an unevaluated optimization framework. Their §5.2 Result 5 specializes to the frozen optimizer via one price and a positive rescaling. The cap-to-price implication below establishes coverage of both phases, the optimizer and uniqueness; the threshold and local behavior are direct algebraic consequences. This failure is based on primary full-text theorem and hypothesis passages, not access uncertainty.

## value

FAIL

The hard-cap question is natural and its concrete formula can be useful. But the entire classification is the explicit one-edge-price restriction of the established arbitrary-price path solution, with an elementary scaling to meet the cap, a one-variable budget equation, and immediate equality and limiting consequences. The frozen result offers no independent new classification or invariant beyond that implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
