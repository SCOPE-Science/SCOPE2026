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

The theorem is true with the stated local smooth successor convention. Subtracting and adding the two cyclic equations gives x²+xy+y²=1-2/h and either x+y=0 or x²-xy+y²=1. The first case gives the antipodal pair exactly for h>2. In the second non-antipodal case xy=-1/h, (x+y)²=1-3/h and (x-y)²=1+1/h, with precisely two choices up to interchange for h>3. These identities also give sufficiency and the h=3 coalescence. At regular points the inverse return derivative is the reciprocal of the product H'_h(x)H'_h(y), yielding the two displayed multipliers. The antipodal singularity is at 5/2; the asymmetric singularity is at 1+3/sqrt(2). The fixed-point inverse multipliers are 1/(1+2h) at ±1 and 1/(1-h) at zero wherever regular. The frozen proof does not justify exclusion of attraction at the unit-multiplier cases merely by reporting those multipliers. To fill that gap, the polynomial returns at h=3 about the antipodal points and at h=2 about zero have leading expansions z-48z³+O(z⁴) and z-4z³+O(z⁴), respectively; the respective inverse returns repel. At the asymmetric flip h=1+sqrt(5), the polynomial two-step return F=H_h² has F'=-1 and negative Schwarzian. Indeed SH_h(t)=6h[(1-h)-6ht²]/(H'_h(t))² is strictly negative at each regular cycle point and the Schwarzian composition law preserves that sign. With F=-z+bz²+cz³+O(z⁴) in cycle-centered coordinates, SF(0)=-6(c+b²)<0, and F²=z-2(c+b²)z³+O(z⁴); the inverse of F² therefore repels on both sides. Thus none of the equality endpoints adds an attractor. For h>1+sqrt(5) all six indicated regular returns are attracting, and for smaller h fewer are so. A smooth autonomous scalar ODE cannot have a nonconstant periodic trajectory, by uniqueness at an extremum.

## originality

FAIL

Rogers and Whitley, Chaos in the Cubic Mapping (1983), analyze exactly the same cubic with a=h; they explicitly factor the degree-nine period-at-most-two equation, give the asymmetric quartic and the pairing of its roots, compute the return eigenvalues, and locate the exact symmetry breaking and flip values including 1+sqrt(5). Their displayed factors are an algebraic identity for all h, even though the paper primarily studies the invariant interval for 0<a≤4. The inverse-branch relation has exactly the same cycles and reciprocates the nonzero return multipliers. Consequently the advertised numerical threshold and census are either explicit there or mechanical consequences, not an uncovered scalar classification. This is affirmative prior coverage, not an access failure.

## value

FAIL

The example is useful pedagogically as an illustration of spurious local backward-Euler attractors, but the scientifically advertised exact census and sharp threshold come from a known classification of the identical cubic, by local inversion, with only standard neutral-return calculus at equality. The open-interval result above a=4 is a direct algebraic extension of the published formulas. No distinct branch-selection theorem, basin classification, or nonroutine surviving invariant was established. A new certificate or a restatement in integrator language would not supply that missing contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
