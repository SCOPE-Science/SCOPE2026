# Scientific review

## Correctness

PASS. The proof first establishes uniform recurrence and that both ordered unequal endpoint pairs occur at every positive separation. It then decomposes any long sliding window into two image-boundary pieces and complete Parikh-constant image blocks. Prefix dominance makes the two ordered endpoint pairs sharp, and the sliding-window one-count changes by at most one, establishing every intermediate Parikh vector. The displayed residue formula follows with the correct offset correction and all quantifiers. The infinite parameter family is separately proved aperiodic by analyzing the three possible column maps and excluding each least period. The bundled standard-library verifier checks both extrema and interval filling in finite samples; these samples do not constitute the infinite proof.

## Originality

PASS, with residual bibliographic uncertainty. The closest source, Rigo–Stipulanti–Whiteland (2024), proves automaticity for Parikh-collinear fixed points, but explicitly leaves ultimate periodicity for Parikh-constant fixed points as a question. Its Theorem 3 and concluding question do not state this exact subclass theorem. Their 2023 precursor provides automaticity and a non-Parikh-constant example with aperiodic complexity, not a periodic formula for the present family. Guo–Lü–Wen (2022) treat automatic boundary sequences and related automatic abelian complexities; its accessible abstract does not imply the residue-extremum result. The direct image-boundary method is compared against these scientific statements; an unindexed equivalent might exist.

## Mathematical value

PASS. This gives a nontrivial positive subclass of an explicitly published periodicity question, with exact computable Parikh spectra at every sufficiently long length rather than a mere automaticity assertion. The sharp attained endpoints, a general sufficient condition, and a two-parameter family with rigorously verified aperiodicity are natural structural information; their full residue profiles vary with the image prefix geometry.

## Closest literature and limitations

Rigo, Stipulanti and Whiteland, arXiv:2405.18032 (2024) and their 2023 conference work, are the primary comparators. Guo, Lü and Wen (Discrete Mathematics 2022) is a secondary plausible comparator whose accessible abstract does not assert the present result; its complete original text was not materially inspected. A global bibliographic uniqueness claim is not made. The result requires binary alphabet, aperiodic fixed point, equal-length equal-Parikh image blocks, and pointwise prefix dominance. A standalone verifier was run, but independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
