# Review of the three-generator gap-run spectrum

## Correctness

PASS. The explicit fixed-summand offset identity is proved by induction; the rowwise membership equivalence excludes all but two summand counts. Exact row patterns are obtained by complementary integer intervals and yield every frequency, including the two small-base cases. `CHECK.py` passed its documented independent finite comparisons. The infinite claim relies on the mathematical row argument, not an experiment.

## Originality

PASS on examined sources. Shor (arXiv:2101.01760, sections 3 and 5) studies residues of *individual gaps* and special Apéry progressions, not maximal gap-run histograms for this family. Liu–Xin–Ye–Yin (arXiv:2306.03459, sections 1–2 and specialized applications) compute genus and Frobenius invariants, not this histogram. The closest database records treat a two-generator spectrum and isolated gaps of a different triple, and neither mathematically implies a three-generator gap-run spectrum at shifts three and five. Search coverage does not prove worldwide uniqueness; older unindexed semigroup results remain a bibliographic risk.

## Value

PASS. Gap-run lengths refine the two standard invariants genus and Frobenius number; the result gives the *entire* natural gap-size distribution over an infinite, minimally three-generated family. The sharp five-class dependence of short gaps and unique multiplicity of each permitted long gap are structural arithmetic features that cannot be inferred from the genus or the terminal gap alone.

## Limitations

The result concerns only the stated family and includes no independent audit or claim of external certification. The computational checker is finite.

Self-review: passed. Independent audit: not yet performed.
