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

For −1≤m<0 the proper quadratic −mx²+y²+z² has derivative 2mx²−2nz². Its zero-dissipation set has no invariant orbit except the origin. For m=0, y²+z² controls y,z and the stable linear equation x'=y−x bounds x. A bounded complete omega-limit orbit in {z=0} obeys xy=0; any interval with y≠0 contradicts x'=y−x, and then x'=−x excludes any nonzero bounded complete orbit. The pair of nonzero equilibria for m>0 disproves universal attraction there. At criticality the stable plane is {y=0}. On the center manifold x=h(y), z=k(y), coefficient matching gives h(y)=y+y³/n+(5n+2)y⁵/n³+O(y⁷), k(y)=y²/n+(n+2)y⁴/n³+O(y⁶); the required finite differentiability is available for each fixed n>0. The reduced flow is y'=−a y³−b y⁵+O(y⁷), a=1/n, b=2(n+1)/n³. Thus w=y^(−2) obeys w'=2a+2b/w+O(w^(−2)); first w~2at, then w=2at+O(log t), after which the remainder in w'−2a−(b/a)/t is O(log t/t²) and integrable. The linear stable rates 1,n give exponential tracking in a sufficiently small neighborhood; alternatively, x−h(y), z−k(y) obey a linear stable system up to coefficients tending to zero and decay exponentially, and the small Lipschitz constant of the center flow gives an exponential shadow by solving the scalar error equation backwards from zero error at infinity in an exponential norm. The zero shadow gives the local strong-stable manifold, whose backwards-flow extensions form the global immersed set. For the other shadows the amplitude is of order t^(−1/2) with fixed sign; the exponentially small tracking error changes its reciprocal square by o(1) and does not change the leading limits of x,y,z. The original RESULT.md line 14 has coefficient b/a=2/n+2/n²; it does not have the extra factor shown in the abbreviated frozen-tool display.

## originality

PASS

The system, its spectral split, and subcritical local stability are prior. The new evidence-supported claim is global convergence through the critical boundary paired with the physical-coordinate clock with a finite renormalized offset on every orbit off the strong-stable manifold. The closest same-system stability attribution was checked in the 2011 primary paper: its origin calculation is local and its nonlinear stability analysis concerns periodic orbits after Hopf bifurcation, not this critical law.

## value

PASS

The natural boundary between one globally attracting state and multiple equilibria includes a nonhyperbolic endpoint. The theorem identifies the entire exceptional exponential-decay set and resolves the next-order relaxation in the original observable: the clock differs from every purely linear clock by an unbounded logarithm yet has a finite offset after renormalization. That quantitative statement is not a routine stability classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
