# Self-review

## Correctness — PASS
The conventional rational-base digit recurrence is stated with the numerator \(b\) as divisor and the denominator \(a\) as multiplier. At each block of \(b\) output edges, the floor increments \(\lfloor a(r+1)/b\rfloor-\lfloor ar/b\rfloor\) are exactly \(a\) jumps of size one and the remaining zero, and their source edges concatenate without omissions or repetition. Parity of \(a-b\delta\) gives the two distinct cases, and exactly implies the identity for every \(N\). The discrepancy recursion contracts by \(a/b\), so the logarithmic error is proved rather than inferred from examples. The all-odd case follows by strict descent. Direct digit computations and the independent recurrence agree in the attached checker. No symbolic-frequency assumptions or unsupported numerical extrapolation enter the proof.

## Originality — PASS on checked evidence
The closest primary sources concern rational-base automata and the special base-\(3/2\) parity word. In that special case its numerically reported two-letter frequencies anticipate \(C(N)/N\to2/5\); this covered instance is credited and does not form the claimed original contribution. The new general quantified statement applies simultaneously to every reduced \(b/a>1\), including different parity regimes and exact \(b\)-versus-\(a\) finite-length equations, which do not follow from the single-base results or the cited automaton characterization alone. Targeted semantic database and literature searches did not locate a universal law. That is evidence of noncoverage in checked materials, not proof of global uniqueness; an uncatalogued equivalent identity is a residual risk.

## Value — PASS
Adjacent digit-sum parity changes are a canonical two-point arithmetic statistic. An exact law for all rational radices answers the natural extension from the unusually difficult base-\(3/2\) word and yields the surprising dependence on only the even numerator/denominator and their sum; opposite parity parameter regimes behave differently and both-odd parameters degenerate to alternation. The finite two-scale identity controls every prefix up to logarithmic error without assuming existence of symbol frequencies. The result is structural across an infinite family and not a one-off numerical curiosity.

## Closest work and limitations
Rigo–Stipulanti (arXiv:2102.10828), Dekking (arXiv:2301.13563), and Cassaigne et al. (arXiv:2602.21895) were compared at the level of the objects and claimed implications. The last source is newer and covers the base-\(3/2\) special case; it explicitly frames other rational bases as further questions. This result does not determine separate \(00\)/\(11\) frequencies, and indexing of obscure existing results may be incomplete.

Self-review: passed. Independent audit: not yet performed.
