# Scientific review

## Correctness: PASS

The exact finite lemma exhausts \(90\cdot 2^5=2880\) core-word/cut configurations and reconstructs all segment-count and oriented-pair observation classes, with fiber sizes \(1\), \(2\), or \(6\) and exact source-mass checks. Marker pair counts recover the marker order, and marker/core pair counts recover every gap's Parikh content. Each observed class is therefore one of the finite lemma classes at a specified choice of nonempty gaps. The formula \(r!\sum_{k=1}^6 d_{k,s}\binom{r+1}{k}\) is a proof for every \(r\), not an empirical fit; polynomial simplifications are checked symbolically. A second full-deck implementation enumerates all words in a fixed marker order for \(r=0\) through \(5\). The precise limitation is that the theorem does not extend beyond the stated composition without new reasoning.

## Originality: PASS, qualified

Full-text sections of Rigo–Salimov (2013), Lejeune–Rigo–Rosenfeld (2020), and Lejeune's 2021 dissertation were compared for equivalent deck statistics, fixed-content class counts, and stronger claims. They establish the relation, general algorithms and asymptotic bounds, but the inspected sections do not state the three-doubled-letter all-marker exact fiber distribution. Public mathematical research records include the adjacent **two-repeated-symbol** formula, but the extra independent core-pair coordinate and distinct fiber-size-six phenomenon are absent and not implied by that statement. Exact-value, alias and parameter searches found no explicit equivalent formula. This establishes best-knowledge novelty, not a proof of historical uniqueness; unindexed results or unpublished computations remain possible.

## Value: PASS

Reconstruction from unordered scattered-pair counts is a natural zero-error observation problem. The smallest balanced three-symbol core with genuinely interacting oriented-pair counts has a finite nontrivial ambiguity spectrum, yet adjoining distinctly labeled markers causes a sharp \(12/r^2\) ambiguous-source decay. Classifying every possible fiber size as well as its count gives an exact general marker-augmentation benchmark, rather than a single isolated finite datum.

## Scope and residual risks

The theorem covers a fixed ternary multiplicity-two core plus arbitrary singleton markers; it is not a statement about contiguous bigram spectra or all Parikh vectors. Prior algorithms can enumerate particular finite cases but do not provide the all-parameter formulas. Completeness of historical indexing cannot be guaranteed; no independent expert verification was performed.

Self-review: passed. Independent audit: not yet performed.
