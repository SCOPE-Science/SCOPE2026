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

In characteristic at least seven the binary branch quartic is separable and the plane cover is smooth of genus three. In the finite unramified chart with y^4=g(x), y''=(4gg''-3(g')^2)/(16y^7)=-Q/(16y^7). The Hessian gives the same condition globally, and Q has no root at infinity. The three pair-product expressions are the resolvent roots by the elementary symmetric coefficients; their pairwise differences are, up to signs, 4*lambda*(2-lambda)/3, 4*(2*lambda-1)/3 and 4*(lambda^2-1)/3. Their squared product gives the monic discriminant; multiplying by 3^6 recovers the stated quartic discriminant. Evaluating Q at 0, 1 and lambda gives the nonzero resultant with g. Thus the four roots are simple, their four lifts each have contact exactly three, and each of the four branch points has tangent contact four. The canonical weights are contact order minus two. For the arithmetic, the three pair-sum differences have squares 16*D_i/9 and D1*D2=(lambda-2)^2*D3. Square values of D1,D2 therefore make all three differences rational, and their signed sums together with the total root sum recover the individual roots. The Klein-four transforms preserve Q and act freely on its roots: for A, reduction modulo x^2=lambda gives 4*lambda*(lambda+1)*(lambda+1-2*x), so the asserted resultant excludes fixed roots; the B and C fixed-point tests follow by x->1-x and x->x/lambda, respectively, with the associated parameter change. Thus one rational root implies four, and the g-transform ratios are nonzero squares, yielding either zero or eight rational ordinary supports. For D1,D2,D3 the full-line character sums are -c,-1,-c, while the excluded contributions are c,2c-1,c, with c=chi(-2); the split count is (q-5-6c)/4. The fixed-point-free partner lambda->1-lambda changes g to -g and hence swaps squares and nonsquares. This halves the split count and gives M_q as stated; the odd extension degree yields c=1 for q=3 mod 8 and c=-1 for q=7 mod 8. No flex multiplicities are included in the rational support counts.

## originality

PASS

Credit the existing pencil and the geometric generic flex inventory. The supported distinct contribution is the arithmetic all-or-none rational ordinary flex splitting and the exact count of marked parameters realizing it at q=3 mod 4. The strongest available statements for the identical pencil compute other invariants; the closest indexed flex-splitting comparison treats another family.

## value

PASS

Rationality of the canonical flex supports is a natural arithmetic refinement of the known geometric stratum of this standard quartic pencil. Rather than a few examples, the result rules out all intermediate numbers, exhibits the fourth-power obstruction even when the x-coordinates split, and gives an all-field marked frequency. The parameter involution explains why splitting and liftability contribute different fractions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
