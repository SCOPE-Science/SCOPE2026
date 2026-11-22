# Scientific review

## Correctness — PASS

For each five-bin histogram, the sum-two class is precisely a disjunction of a loop at the middle vertex and an edge between the two outer vertices. Splitting it by an integer parameter reduces realizability to the standard connected-support Euler trail/circuit criterion. Linear outputs exclude exactly three mutually disjoint disconnected-support classes; cyclic outputs are partitioned into four explicitly proven parity and connectivity cases. Their rational series and coefficients are calculated without extrapolating from finite tests. Exact exhaustive and constructive checks in `verify.py` corroborate the formulas over explicitly bounded parameter ranges.

## Originality — PASS, with historical-priority risk

The closest primary studies concern linear substring-composition reconstruction, substring multispectra, oriented sequence-profile graphs, and indexed local histograms. Three published exact ternary cyclic profile enumerators retain six unordered or nine oriented pair bins, or restrict the allowed words; none of the inspected results states the image cardinality after the sum-two collision merges the unordered pairs \(\{0,2\}\) and \(\{1,1\}\). The current result counts that non-injective projected image exactly for both linear and cyclic words. Earlier work's general graph model is a useful premise, not an already-stated projected capacity formula. No claim of exhaustive priority proof is made; specialized additive-histogram sources not located by available searches are a residual risk.

## Value — PASS

An aggregate, length-two numeric read is a natural low-resolution statistic in sequence reconstruction. Its five-bin output capacity cannot be calculated by simply using six-bin profile counts because different edge-type profiles coalesce. The theorem gives a complete output feasibility classification, exact finite codebook sizes, and a sharp factor-two asymptotic penalty caused by cyclic parity. These are all-length, structurally motivated invariants, not arbitrary finite tabulations. The result does not establish robustness against errors, laboratory feasibility, or larger-alphabet generalizations.

Self-review: passed. Independent audit: not yet performed.
