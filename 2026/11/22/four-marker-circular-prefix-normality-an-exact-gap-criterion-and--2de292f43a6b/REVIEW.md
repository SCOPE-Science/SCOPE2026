# Scientific review: four-marker circular prefix normality

## Correctness — PASS

The claim uses oriented binary necklaces of weight four and compares all length-matched circular factors against the chosen prefix, including wrapping factors. The proof first restricts extremal windows to ones as starting positions and characterizes all simultaneous maximizing roots by their three successive-one thresholds. Requiring the immediately following gap to be minimum and the immediately preceding gap to be maximum automatically minimizes every two-gap sum when there are exactly four gaps. The forbidden necklace generating series follows from a complete enumeration of the four possible weak-order multiplicity types, with exact rotation-orbit size four for every forbidden tuple. Burnside's formula and the leading poles yield the stated asymptotic proportion. The direct circular-window checker matched root sets on 14,950 gap tuples and the first 23 exact generating-series coefficients, without using the proof's thresholds. The five-marker example is checked directly. Finite tests alone do not establish the all-length claim; the symbolic arguments do.

## Originality — PASS, qualified

The 2016 prefix-normal form study and the 2018/2021 infinite-word study define the underlying property but do not state this four-marker cyclic rotation criterion and forbidden-necklace series. The closest indexed three-one result gives the same extreme-gap condition for three gaps, but its proof has no additional consecutive-two-gap comparison and its generating function is different. The four-run cyclic result applies to only two one-runs, whereas this theorem includes four isolated ones. The sharp linear-cut obstruction is a different, weaker nonwrapping condition. The run-rearrangement extremality theorem permits reordering, not merely rotating, the original circle. Search coverage cannot rule out unindexed equivalent work. Primary full-text and related result comparisons are summarized in the structured audit.

## Value — PASS

This gives a complete all-length root-existence test for circular streams with four markers, including all ties and zero gaps, and an exact rational enumeration of nonreconstructible phase representatives. The limiting failure probability is \(2/3\), compared with the established three-marker value \(1/2\). The explicit family of counterexamples at every marker weight at least five identifies the sharp limit of adjacent extreme-gap control, a structural boundary relevant to circular jumbled indexing and canonical rotation selection. These are exact natural invariants, not a numerical parameter increment or an arbitrary finite slice.

## Limitations and references

The theorem does not characterize all five-marker words or unrestricted-weight circles. The asymptotic is conditional on weight four. An independent historical-priority review and independent mathematical audit have not been performed. Background: Burcsi et al., *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017v1; Cicalese, Lipták and Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273. Comparators: *First circular prefix-normal obstructions and the complete three-one classification*; *Prefix-normal rotations of four-run binary cycles*; and *The sharp cyclic prefix-normal representative obstruction*.

Self-review: passed. Independent audit: not yet performed.
