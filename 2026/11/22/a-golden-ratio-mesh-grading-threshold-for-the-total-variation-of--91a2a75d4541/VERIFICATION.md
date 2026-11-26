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

The forced tridiagonal spline system has diagonal 2(h_{i-1}+h_i), off-diagonals h_{i-1},h_i and right-hand side −6 only at i=1. The homogeneous two-root solution with right boundary zero extends to fictitious value 6 at i=0, so replacing it with the actual left boundary value zero gives exactly the forcing −6. The roots are −a and −b with a/b=q∈(0,1); strict diagonal dominance gives uniqueness. On cell zero M_1<0 and |M_1|<6a<3, making its derivative strictly positive. On each later cell k_i=−M_{i+1}/M_i∈[0,a], the bracket is ≥1−2a>0, and the derivative of the excursion polynomial is positive at t=0 and negative at t=1. Its quadratic has exactly one root in (0,1), the displayed smaller root. Doubling the extremal excursion gives h_i²|M_i|F(k_i), with exactly the factor of 6 in the global sum. β is strictly increasing since D=1+R+√(R²+R+1) has D′<2 and D>R; at R*=(3+√5)/2, R*²=3R*−1 gives D=R*². At β<1 bound by a geometric series for fixed i; at β=1 the Lipschitz error of F and the endpoint weight are O(q^{N−i−1}) before dividing by 1−q^N, and Nq^N is bounded; at β>1 reverse the sum via j=N−i and dominate by β^{−j}. The limiting supercritical sum is strictly positive. This covers all R>0 at fixed R, including shrinking widths. Exact replay at N=2 gives M_1=−3/(1+R), F(0)=2/(9√3), and TV=1+2R²/[3√3(1+R)]. Independent numerical replay using tridiagonal elimination and cubic derivative roots also matched seven cases spanning R=.125 to 8; e.g. at R=R*, N=40, TV≈27.1887245197602, and at R=3 the rescaled TV approaches 3.75142608529279. For replication use the above system, integrate each cubic via differences at endpoints and derivative roots; finite results corroborate normalization but are not the proof. The frozen CHECK.py was read, not executed.

## originality

PASS

Standard natural-spline equations and the three-knot overshoot are not new. The surviving claim is the exact variation law for this step at arbitrary lengths of one geometric mesh and the sharp bounded/linear/exponential alternatives, with a critical slope and supercritical coefficient. No inspected result was found that subsumes this combination; the conclusion is provisional because relevant old spline literature is not exhaustively accessible.

## value

PASS

A natural C² interpolant of a monotone step exposes a sharp stability failure controlled by a single local width ratio. Critical linear variation arises despite bounded excursions, a distinction not captured by pointwise overshoot, and the prefactors permit quantitative comparison just within the specified family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
