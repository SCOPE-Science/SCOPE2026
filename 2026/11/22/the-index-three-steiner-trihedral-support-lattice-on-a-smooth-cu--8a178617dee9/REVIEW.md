# Review of the Steiner-trihedral support lattice theorem

## Correctness

PASS. The claim concerns the universal \(27\)-line configuration, and the proof reduces all smooth characteristic-zero cubic surfaces to that configuration via the six-point plane blowup. Line classes are enumerated explicitly; the quotient-class map has rank-six image because the line classes generate the rank-seven Picard lattice and the anticanonical class is primitive. The tritangent lattice is pinned down by an exact \(21\)-by-\(21\) determinant \(-1\), and the Steiner sublattice has a selected full-rank minor \(+3\) on the same rows. Each Steiner column has divisor class three times the anticanonical class. A surjective mod-three anticanonical-degree homomorphism gives the matching lower bound on the index. The complete standard-library checker reconstructs the \(45\) and \(120\) sets from Picard classes and verifies the determinants with exact integer arithmetic. An independent full-matrix Smith-form computation confirmed the result. No finite sample of surfaces is used to infer universality.

## Originality

PASS, with historical-priority qualification. Elsenhans--Jahnel's explicit \(120\) classical Steiner supports (2010) and the tritangent monomial exchanges are prior data. The published integral tritangent-presentation theorem already makes the three-line lattice primitive, but does not determine the sublattice of nine-line Steiner supports. The published double-six incidence theorem uses twelve-line supports, and the toric-ideal theorem concerns relations among tritangent monomials rather than the nine-line support span. These differences were checked at the level of their mathematical maps, not just their titles. The new claim identifies the exact Picard preimage \(\pi^{-1}(3\mathbb Z[-K_X])\), an index-three quotient, and the absence of two-primary torsion. The \(2010\) list of supports makes the computation possible but does not itself provide this integral generation theorem. Older unindexed incidence-design computations remain a residual originality risk.

## Mathematical value

PASS. A Steiner pair is a canonical nine-line geometric marking, and its formal support determines a natural integral reconstruction question. The result characterizes precisely which integral line-label combinations the marking supports generate, giving a direct criterion in the Picard lattice and a sharp universal order-three obstruction. Especially meaningful is the disappearance of two-primary obstructions when passing to once-counted line supports, despite the more complicated integer behavior of other tritangent/Steiner incidence maps. This is a complete natural invariant rather than an arbitrary small-field census or cosmetic reformulation.

## Limits and closest literature

The theorem does not classify rational cubic surfaces, Galois descent of Steiner pairs, or actual Picard-group torsion. The antecedent geometric configuration is classical, and an equivalent historical Smith table cannot be excluded by bounded literature searching. Relevant detailed comparisons are in `AUDIT.json` and the references in `RESULT.md`. The reproduction script is included and was run; it is an exact finite certificate for a uniform geometric configuration, not an independent human audit.

Self-review: passed. Independent audit: not yet performed.
