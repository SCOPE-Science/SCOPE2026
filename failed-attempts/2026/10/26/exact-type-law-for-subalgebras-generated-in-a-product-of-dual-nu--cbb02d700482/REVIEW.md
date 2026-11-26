# Independent mathematical audit

## correctness

PASS

Let P be the polynomial algebra on the sampled generators. Evaluation at a+εb on each residue class factors through P/m_a², by expansion to first order, with no division or characteristic restriction. The ideals m_a² are pairwise comaximal, so the Chinese remainder theorem allows the independent choice of a constant and first jet in every occupied residue class. In the block with residue a the first-jet map has the row span of its tangent matrix as image; products in the image radical vanish. The block is thus a local factor A_s, and the primitive idempotents distinguish the factors with dimensions s+1. For a labeled block of size m, choosing an s-dimensional column image and a surjection to it gives the stated count N. Each of the q^ℓ labels can be empty or contribute one nonempty rank-marked block. Multiplying exponential series allocates the r coordinate labels, with multiplier r! and normalization q^(2ℓr); subtraction of 1 excludes the empty input. At z_s=1 the block sum by rank gives e^(q^ℓ t)−1, so the full series is e^(q^(2ℓ)t)−1 as required. At q=2, ℓ=1, r=2 direct small enumeration and coefficient extraction give counts (2,0):2, (1,1):4, (0,2):2, (1,0):2, (0,1):6. This small check corroborates the proof only. The supplied script compares rank-derived counts in small prime fields rather than independently constructing arbitrary embedded subalgebras and was inspected, not executed.

## originality

FAIL

The exact joint statistic is not stated verbatim in the compared records. Nevertheless the complete result is obtained by a mechanical rank marking of the exact labeled occupancy construction in Resultary 531dcf3be3b2 with the exact local rank law in Resultary 697b7c781727. The only algebraic assembly is the standard splitting across distinct residue maximal ideals, after which the marks are independent conditional on the residue labels. This is a demonstrated implication of the compared content, not a claim about the priority order of same-day records or proof that one source prints the entire formula.

## value

FAIL

The abstract type is a natural statistic and the assembled formula may be useful. But the claimed exact invariant is a size-by-size marking of an available labeled block EGF by an available rank law, plus standard splitting and normalization. It is not an independent resolution of a new enumeration obstacle under the review standard. No additional asymptotic, interaction law, or case outside that assembly is established in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
