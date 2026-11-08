# Self-review

**Claim reviewed:** For two periodic words built from the same cyclic sequence of pairwise distinct letters, the intersection of their contiguous factor languages is exactly the union of the factor languages of the mismatch-gap words \(F_i\); these are precisely the inclusion-maximal common factors. The number of maximal words is the number of unequal run lengths, and the maximum common length has an exact cyclic-sum expression. The identical-profile case has no maximal finite common factor.

## Correctness — PASS

The proof is a complete argument for every alphabet size at least two and all positive integral profiles, not an extrapolation from finite data. Unique letter transitions align run phases across the two input words. Interior full runs of a shared factor must have identical lengths. All mismatches therefore bound the possible common factors, giving an explicit union of factor languages. Each candidate's two endpoint extensions disagree in the two sources, establishing maximality; distinct starts establish uniqueness. An independent finite oracle checks all factors and all maximal factors across 2684 pairs, including single mismatches, adjacent mismatches and all runs mismatching. Scientific limit: this assumes a fixed distinct-letter cyclic order.

## Originality — PASS with stated bibliographic risk

The closest full-text primary literature includes Amir–Boneh (2018) on locally maximal *occurrences* for dynamic factor problems; Alzamel and coauthors (2019) on cyclically shifted finite common factors; Charalampopoulos and coauthors (2021) on fast general finite LCS; and Lee–Lin (2023) on finite RLE LCS algorithms. They do not explicitly state an antichain of exactly one inclusion-maximal common *word* per mismatched run type, nor the complete finite-language basis. General algorithms alone do not supply the symbolic theorem without a further argument. Equivalent-formulation, broader-coverage and exact-database searches were carried out; unindexed equivalents remain possible. No universal claim that the result has never appeared anywhere is made.

## Mathematical value — PASS

The theorem completely describes a natural two-input, infinite-periodic factor-language intersection in an arbitrary number of unequal-length runs. It gives a sharp cutoff and the full set of maximal common words using an O(q)-sized run representation, unlike a single numerical example or merely finite enumeration. It explains why mismatched runs block long common substrings and identifies each mismatch-free gap as one exact maximal generator.

## Limitations and nearest literature

The theorem is not about approximate matching, scattered subsequences, unrelated cyclic orders, or arbitrary run-length-compressed finite strings. This statement does not claim faster algorithms for unrestricted LCS. See DOI 10.4230/LIPIcs.CPM.2018.11 and arXiv:1901.11305, arXiv:2105.03106, arXiv:2310.00966 for the closest studied problems. A genuinely equivalent unindexed result would supersede the novelty assessment.

Self-review: passed. Independent audit: not yet performed.
