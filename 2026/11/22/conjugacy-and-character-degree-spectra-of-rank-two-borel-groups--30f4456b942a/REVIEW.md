# Self-review

## Correctness — PASS

For a finite commutative local ring \(R\) with \(\mathfrak m^2=0\), the decomposition \(B_2(R)\cong R^\times\times(R^+\rtimes R^\times)\) is verified directly from multiplication of triangular matrices. For fixed affine multiplier \(s\), the conjugacy action on translations is precisely multiplication by units on \(R/(1-s)R\), with every quotient orbit lifted across the ideal. The mutually exhaustive cases \(1-s\) unit, nonzero radical, and zero produce the six row-wise class sizes and multiplicities. The additive-character group has \(q\) lifts of each character of the radical. Its nonzero restriction orbits have stabilizer \(1+\ker\beta\), proving the three complete ordinary irreducible-degree rows by the standard little-group theorem. The class total, sum of class sizes, and sum of squared degrees satisfy the exact order identities for all integer parameters \(q>1,d\ge1\).

Full direct conjugacy and additive-character enumerations passed for split rings with \((q,d)=(2,1),(3,1),(2,2)\), residue rings \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/9\mathbb Z\), and a nonchain mixed-characteristic local ring of order eight. Those finite checks do not establish the universal result by themselves, which is supplied by the mathematical argument.

## Originality — PASS (best of knowledge)

The field parabolic orbit method in S. H. Murray, *Conjugacy classes in maximal parabolic subgroups of general linear groups* (2000), is classical background, not a claim of novelty. The complete published affine-group character census for **chain rings** covers radical dimension one only; its cyclic/socle-character method does not automatically extend to nonprincipal square-zero rings with radical dimension at least two. The full-affine-**monoid** centralizer census concerns a larger semigroup and lacks ordinary character degrees of the unit subgroup. Results on radical-square-zero **quiver algebra unit groups** have different multiplication: the upper-triangular ring matrix algebra has radical cross-products even when the coefficient ring's radical squares to zero. Hence these results do not imply the complete nonprincipal Borel spectra. A specialized older character census under alternate terminology remains a historical-priority risk; published literature coverage is best-of-knowledge, not a proof of novelty.

## Mathematical value — PASS

The problem concerns two standard complete invariants of a natural finite group family: conjugacy-class size distribution and irreducible-degree spectrum. The formulas hold uniformly over all nonprincipal square-zero local rings and their mixed-characteristic realizations, a setting in which ordinary generating additive characters for the ring do not exist. The character restriction/stabilizer method explains the dimension dependence, distinguishes the nonchain situation from a direct application of chain-ring classifications, and obtains an exact commuting probability and a nonzero large-embedding-dimension limit. This is a natural complete family classification, not merely a single small numeric example.

## Closest literature and boundaries

- Murray (2000), arXiv:math/0001031v1, establishes the parabolic/abelian-normal orbit reduction over fields, not the nonprincipal finite-local-ring spectra.
- *Conjugacy and ordinary character spectra of affine groups over finite chain rings* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-conjugacy-and-ordinary-character-spectra-of-affine-groups-over-f--0a4181d7ad6d, completely covers the \(d=1\) chain-ring subcase. The new claim's distinctive range is \(d\ge2\).
- *Centralizer spectra of finite affine monoids distinguish local-ring geometry* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-centralizer-spectra-of-finite-affine-monoids-distinguish-local-r--5531b23a5b4d, concerns monoid centralizers, not group conjugacy or representation degrees.
- Lins de Araujo (2025), https://doi.org/10.1002/mana.202300448, discusses projective Borel/affine identification and twisted conjugacy, not this finite census.

Conjugacy spectra do not determine full character values or group isomorphism. Published-priority uncertainty remains. The tests are finite; the theorem proof covers arbitrary finite residue fields and radical dimensions.

Self-review: passed. Independent audit: not yet performed.
