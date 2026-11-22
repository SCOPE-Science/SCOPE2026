# Scientific review

## Correctness — PASS

The thirteen cyclic lines are the translates of \(\{0,1,3,9\}\), a planar Singer difference set, independently identified by the field \(\mathbb F_{27}\) with \(\operatorname{PG}(2,3)\). Because the order-thirteen rotation fixes no nonempty face of the rank-three independence complex, the geometric quotient has ordinary CW cells \((1,6,18)\). The eighteen cellular attaching words are explicitly enumerated and reproduced by `verify_singer13.py`. Five admissible one/two-cell CW cancellations reduce the six edge generators to one; the thirteen remaining maps consist of eight null words and five maps of degree thirteen. The first such map forms \(M(\mathbb Z/13,1)\); the other twelve cells attach nullhomotopically, giving exactly twelve \(S^2\) wedge summands. The cover is universal, so the lifted Moore boundary \(1+r+\cdots+r^{12}\) and twelve lifted sphere orbits give the integral deck-module \(I\oplus R^{12}\). A separate exact integer Smith calculation gives factors \(1,1,1,1,1,13\). The checker is supporting finite evidence; it is not substituted for the cell-homotopy argument.

## Originality — PASS relative to checked evidence

The pre-existing full Singer-quotient homology theorem for rank-three projective matroids already determines the order-thirteen fundamental group and rank-twelve second homology in the ternary case. **Those numerical conclusions are not independently new.** It does not determine the attaching-map homotopy type or the integral deck-group module. The published cyclic Fano cap quotient gives a Moore space for an order-seven action on a different complex; the published Fano matroid Singer result determines a different integral module at field order two. Published ternary arc and line-avoidance computations concern larger complexes or different forbidden faces. The primary matroid-shellability and equivariant-character literature determines unquotiented topology or rational representations, not these cellular quotient attachments. Thus the complete homotopy and deck-module classification is not implied by the inspected results, subject to the stated priority risk.

## Value — PASS

The first nonbinary projective plane supports a canonical free Singer action on its rank-three independence complex. Its homology-only quotient description does not distinguish a Moore-plus-spheres two-complex from other homotopy types with the same integral homology and finite fundamental group. The exact classification supplies this missing natural homotopy invariant, explicitly exhibits thirteen-primary fundamental-group torsion and an integral augmentation-ideal deck summand, and provides finite reproducible attaching-map data for further comparisons.

## Closest literature, scope and limitations

The closest antecedents are Ardila–Castillo–Samper (arXiv:1410.3870, matroid shellability), Cook–Migliore–Nagel–Zanello (arXiv:1503.04335, collinearity incidence complex), Moci–Pezzoli (arXiv:2001.03760, complex homology representations), the recorded general Singer quotient fundamental-group/homology theorem, and the published Fano Singer examples. The new homotopy result concerns only \(\operatorname{PG}(2,3)\), with no claims for other field orders or subgroups. Full independent mathematical validation has not been conducted, and an equivalent unindexed earlier classification remains a risk.

Self-review: passed. Independent audit: not yet performed.
