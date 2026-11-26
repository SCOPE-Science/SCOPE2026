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

Using the stated commutator convention, the translation in [X,Y] is u⁻¹v⁻¹((1−v)x+(u−1)y), and a further bracket with Y multiplies any translation by v⁻¹−1. For fixed v,u the two coefficients therefore generate the ideal of exponent min(m,ki,(k−1)i+j), with the zeroth power interpreted as 1 at k=1. Uniformity on this ideal and the additive kernel count give the displayed fibers; they sum to |G|². For fixed Y, the right-hand side of (66) is in the left coefficient's ideal exactly when the unit satisfies the given threshold r. This remains true when s=m (no condition) and at i=m,k=1 (v=1, so only the right expression matters). Each solvable multiplier contributes q^d translations. The crossed identity follows from uu'−1=(u−1)+u(u'−1), which proves subgroup closure. When q=2 and k<m, i=j=1 realizes the largest ideal m^k; at depth m−1 only i=1 contributes for m≥3, giving 1/4, while for m=2 three of the four unit pairs give the socle, giving 3/8. When q>2, the i=0 term is always full uniformity and for k≥m+1 all other terms are point masses. At every earlier step the positive i=1,j=0 term (i=m=1,j=0 for fields) shrinks strictly, increasing the identity mass, while no term decreases it. At the last step m≥2 the excess nonidentity mass is Pr(i=1)Pr(j=0)(1−1/q)=(q−2)/q²; at m=1 replace Pr(i=1) by 1/(q−1), giving the stated field gap. The two q=2,m=3 examples both have commutator subgroup the maximal-ideal translations, while their unit groups are respectively C2×C2 and C4, giving the stated abelianizations. Read the frozen code and sixteen-case log (largest |G|=500); these are limited examples, not the basis of the universal check, and the uploaded code was not executed.

## originality

PASS

Credit verified coverage at depth one for centralizer orders and commuting probability, and coverage of the field and order-two-complement laws by prior special cases. The supported distinct claim is the joint all-depth valuation law, prescribed target fibers, and fixed-right size spectrum for arbitrary chain length, including the noncoprime sharp stabilization and exact last-step gaps. The same-ring Lie fiber formula is a substantive analogue, not the same word or unit-constrained input law.

## value

PASS

Right Engel words provide natural distributional invariants of these affine groups, including when the translation and unit orders are not coprime. Counting individual targets and the sizes at each fixed right argument is materially stronger than one identity probability. The sharp depth transition and the same-law nonisomorphic examples give concrete information about what the word statistics detect and what they cannot distinguish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
