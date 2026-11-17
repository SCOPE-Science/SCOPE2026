---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For bounded degrees D in {1,3,5}, mean 3 implies p1=p5=t, p3=1-2t, 0<=t<=1/2. Standard thinned configuration model giant fraction Xi=1-G0(u), u=min fixed point of u=1-T+T G1(u). On u<1, cancellation gives 1/T=Psi(u,t)=(1+u)(1+t(5u^2-1)/3), strictly increasing in u, Psi_u>=5/6. Explicit differentiation gives Xi_t=(1+u)P(u,t)/(3Psi_u), P polynomial as in RESULT.md. Independently verified this identity by exact SymPy expansion, and factorized P_t=(u^2-1)(10u^4+5u^3+u^2-u+1). Descartes sign variation gives exactly one positive P root z(t) in (1/2,1), increasing t; monotone frontier Tcal(t)=1/Psi(z(t),t) decreases from .642387380782 to .503512762467. Therefore all t tie T<=.3, t=.5 is unique max for .3<T<=Tlow, unique interior for Tlow<T<Thigh, and t=0 unique for T>=Thigh. Sample frontier at t=0,.1,.25,.5 checked. Infinite random graph limit relies on established configuration-model branching theorem, not numerical simulation.

## originality

PASS

Britton–Trapman (2010) Theorem4.1 covers the *unrestricted* fixed-mean distributional optimizer with support {0,k,k+1}; the constrained family {1,3,5} is disjoint from this optimizer class and its paper explicitly does not give closed formulas for k or masses. Leibenzon–Assaf (2023) shows heterogeneity-dependent outbreak-size reversals, mainly in correlated populations and large-degree asymptotics; their full HTML does not give the two algebraic thresholds for the odd-degree, mean-3 independent-bond family. Resultary search returns the submitted claim and other unlike epidemic problems; no identical constrained optimization found. Priority remains bounded.

## value

PASS

The degree family {1,3,5} with mean3 is the smallest nontrivial positive odd-degree support allowing mean-preserving variance control; the sharp three-phase optimum, two algebraic thresholds, uniqueness and endpoint ties provide a useful exactly solvable benchmark for heterogeneity effects not mechanically implied by unrestricted optimizer theory. It is not presented as a global degree-law optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
