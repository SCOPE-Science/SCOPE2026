# Independent Audit — 2026/09/13/056

Audit date: 2026-09-28 (UTC)
Audited tree: `20dc399819c1cd37677215c07e566b818b5ed78a`

## Disposition

**FAILED** — Rejected: genus-4 kernel computation is correct, but [a,b]c^2 is a classical quadratic surface word and the finite surface cover is standard orbifold topology rather than new surface-subgroup theory.

## Correctness

**PASS**. The Reidemeister–Schreier calculation is sound. For the kernel of c↦1 mod 4, the four rewritten relators are R0=A0A2z, R1=A1A3z, R2=A2zA0, R3=A3zA1. Eliminating z=(A0A2)^{-1} makes R2 redundant and reduces R1/R3 to one relator A0A2A3^{-1}A1^{-1}, which becomes a product of four commutators after swapping entries in the inverse commutators. Hence the index-4 kernel is a closed orientable genus-4 surface group. The defining word is not a proper power, so standard one-relator-with-torsion hyperbolicity applies, and finite index implies quasiconvexity.

## Originality

**FAIL**. The word [a,b]c² is already a standard nonorientable quadratic surface word (a product of one commutator and one square). Classical quadratic-word theory identifies such words with surface relators, and adjoining the square relation is naturally the corresponding compact 2-orbifold group. The existence of torsion-free finite-sheeted surface covers is therefore structural; the explicit mod-4 cover and its genus are a short Reidemeister–Schreier/Euler-characteristic computation, not a genuinely new small-exponent surface-subgroup phenomenon.

## Scientific value

**FAIL**. Although the explicit generators are correct and useful as an exercise, the record reframes an elementary finite orbifold-cover calculation as progress on the general Gromov surface-subgroup problem. That framing overstates the research value because this particular relator is itself a surface word and the finite-index surface cover is expected from standard orbifold topology.

## Evidence and limitations

Repository files were read from the exact assigned/current tree and GitHub was used only as evidence. The following literature comparisons were inspected from lawful open-access sources:
- https://web.stevens.edu/algebraic/alexeim/Teaching/Math627_Fall_2005/Sections/Notes_new/Section8.pdf — Classical quadratic-word normal form: orientable products of commutators and nonorientable products of squares; places [a,b]c^2 in standard surface-word theory.
- https://arxiv.org/abs/2510.01876 — Ng: genuinely nontrivial large-exponent quasiconvex surface subgroup results; not needed to obtain the present finite orbifold cover.

The failure is not a claim that the subgroup is absent; the explicit subgroup exists, but the research framing and originality/value claims do not survive audit.
