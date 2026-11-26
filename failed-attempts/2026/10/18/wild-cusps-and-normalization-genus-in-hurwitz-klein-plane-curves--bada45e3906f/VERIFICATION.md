---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On the torus, t=u^n/v and u=−(1+t)/v^{n−1} identify the equation with v^m=R(t), where R=(−1)^n(1+t)^n/t. The reciprocal polynomial is Eisenstein at t=0 even in inseparable characteristic. No component lies on the axes and each coordinate vertex is smooth. If p does not divide m, the v-derivative in these torus coordinates is nonzero. If p divides m, p is odd and n,n−1 are units. Then R'/R=((n−1)t−1)/(t(1+t)) has a simple zero at t0=1/(n−1)=1/n² in k; v^m=R(t0) has exactly r distinct roots, and returning to u yields the stated formulas. At each such point w=v^r−v0^r is a formal parameter in the v-coordinate, and w^q=R(t)−R(t0)=(t−t0)² times a unit. Taking a formal square root gives the claimed germ directly; the parameterization by powers q and 2 establishes unibranchedness, semigroup and delta. Setting tau=t^(1/q) yields the displayed function field by Frobenius; the pole of order one forces the inseparable degree q. The residual Kummer divisor orders −1,n,1−n are all coprime to r, yielding the stated ramification and Riemann–Hurwitz genus, with r=1 rational. This also checks the examples and the boundary p dividing the plane degree. The supplied files were inspected, not executed; their 150 prime-field checks would not prove the local or normalization statements.

## originality

FAIL

The distinct indexed record 027b54346512 states the all-parameter cusp, delta and normalization-genus classification, and gives the same torus function-field model in cyclically shifted coordinates. In its Proof steps 1–2 take the chart with original y=1 by a cyclic relabelling: its coordinate u is the frozen v and its s is v^(n−1) times the frozen u, so s=−1−t. Substitution into u^N=−s^n/(1+s) gives exactly the frozen equation v^m=R(t). In exceptional characteristic, adjoining s^(1/q) and separating the prime-to-p exponent immediately gives the frozen tame Kummer presentation (s^(1/q)=−1−tau); its divisor orders give the asserted total ramification as a direct Kummer criterion. The indexed local equation differs only by a sign in the odd power, and its singular support equations translate to the same support. Thus the alternate Riemann–Hurwitz proof is not an independent uncovered scientific claim. The indexed path is later-dated than the frozen path; this is a coverage determination, not a historical priority claim.

## value

FAIL

A uniform description of wild plane cusps is a meaningful objective, but the cusp and genus classification is already covered, and the remaining presentation of the tame cover is a direct extraction of the prime-power factor from the same indexed torus equation. No independent exact invariant beyond this coverage is established by the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
