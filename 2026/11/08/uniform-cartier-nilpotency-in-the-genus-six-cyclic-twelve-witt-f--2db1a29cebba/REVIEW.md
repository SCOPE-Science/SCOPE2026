# Independent mathematical audit

## correctness

PASS

The proof of the all-parameter ranks survived. In length-two Witt coordinates the second component of (F−1)(y,w) is w²+w+y²+y³. With t=1/x and c²=λ+1 the invertible change v=w+cy yields y²+y=t³, v²+v=y³+(λ+c)y. The unique odd local poles of orders 3 and 9 (in the two successive base fields) force connected, totally ramified covers and different exponents 4 and 10. Transitivity gives div(dt)=(10+2·4−8)P∞=10P∞ and genus 6. Pole orders 4,6,9 give a numerical semigroup with just six gaps (all 12–15 occur, and adding 4 gives all higher integers); equality follows from genus. The six listed differentials are regular and have distinct valuations. The decomposition y³=(y+t³)²+t(ty)² follows by substituting y+t³=y². With c0²=λ+c it yields C(v dt)=(ty+c0 t)dt, and C(ty dt)=y dt, C(y dt)=t dt, C(t dt)=dt, C(dt)=C(t²dt)=0. Thus the successive images have dimensions 4,3,2,1,0 over the perfect ground field, including λ=0. The archived script was inspected, not run. Its gf_root(x) squares twice on F4, hence applies the identity instead of inverse Frobenius (squaring); those rank dimensions happen to be unchanged, but the claimed semilinear replay was defective. The audited repairs/4/verify_cartier_c12.py explicitly distinguishes the actions on a coefficient α∉F2 and checks all successive image cardinalities, four c0 and each corresponding λ specialization. The corrected script passed its polynomial, semilinear, and gap checks. It corroborates, not replaces, the all-parameter proof.

## originality

PASS

PASS for the precise uniform Cartier image filtration (and its associated Jacobian invariants), not for the published Witt-family classification or the routine marked semigroup consequence now identified as supporting geometry. The strongest inspected same-family theorem gives the exact model and jumps, not the action on the canonical space. The strongest inspected broader Cartier result gives bounds for the supersingular-intermediate case, rather than the exact ordinary-base formula. No covering implication for the full rank profile was established in the compared material.

## value

PASS

On a natural classified wild family, the entire power-rank sequence supplies a precise local Jacobian invariant not obtained just from its published genus, group, jumps or generic bounds. The explicit basis and length-five chain explain constancy even when the parameter-dependent coefficient vanishes. This is not a claim to determine the full 2-torsion group scheme or to add a separate novelty for the pole semigroup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
