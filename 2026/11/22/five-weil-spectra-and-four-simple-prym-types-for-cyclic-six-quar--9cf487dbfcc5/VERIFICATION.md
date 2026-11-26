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

The affine singularity test reduces to repeated roots of y⁴+ry²+1, hence r=±2; the only point at infinity [1:0:0] has nonzero Z derivative. A smooth plane quartic has genus three. On every odd extension, cubing is bijective: one point per y and one at infinity. Thus odd Frobenius power sums vanish and the reciprocal degree-six polynomial is even. A fresh exhaustive affine-pair enumeration over F₂₈₉, independent of the uploaded checker, gives counts 284,380,344,392,356,344,356,356,344,356,392,344,380,284 in parameter order 1,3,4,5,6,7,8,9,10,11,12,13,14,16. Newton's identity gives c=(N₂−290)/2 and d=c−17. The order-two quotient completes the square to V²=U³+(r²−4)/4, yielding an elliptic curve with 18 points and trace zero. The norm decomposition gives the complementary Prym factor. For F(X)=X⁴+dX²+289, a rational root yields its opposite root as well, so a reducible case must split into two monic rational quadratics. Vanishing cubic and linear coefficients say their linear terms are opposite and either zero or their constants coincide. The zero case needs the negative discriminant d²−1156 to be a square, the coincident case needs ±34−d to be a square; none is possible for the four listed d. At d=34 the factor is the elliptic square; via finite-field isogeny this gives exactly the stated nonsimple Pryms. Exactly r=±5 attains the upper bound 392. The primary r² criterion gives the seven geometric classes and the two distinct-curve collisions. The unrooted Hasse–Witt matrix has only possible entries (1,3) and (3,1) by X-degree mod 3 and Y-degree mod 2. With u=r² they are 7u+12 and 5u⁴+2u³+6u²+4u+10. Evaluation on D gives both zero exactly at ±5 and both units otherwise, so the claimed stable ranks and a-numbers follow. Independent reproduction files: /workspace/branches/5eba91cc-f0f1-48ad-92c7-cfbdd7ed8c31/. The frozen verify.py was inspected, not executed.

## originality

PASS

Pass the distinct exact five-spectrum and four-simple-Prym classification on these marked F₁₇ forms. The family, geometric isomorphism classes and geometric Cartier strata, including the exceptional geometric class, are known and are not counted as original.

## value

PASS

All the marked curves have the same ground-field point count, so a full Weil census resolves an ambiguity left by that natural coarse invariant. It identifies geometrically different curves with isogenous Jacobians, determines the complete set of simple Prym types, and separates the marked maximizers. Those are meaningful exact invariants of this symmetry family beyond the known Cartier strata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
