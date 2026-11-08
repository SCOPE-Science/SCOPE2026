# Review of exact hub persistence on clique bouquets

## Correctness

**PASS.** The claim is an exact event probability for a specified finite, connected graph family under the usual voter-model copying dynamics, followed by an asymptotic statement for bounded private clique sizes. Before its first flip, the hub is equivalent to a frozen external source, and its possible opposing copying events form independent Poisson thinnings of the hub clock. Conditional survival equals the exponential of the integrated opposing-neighbor exposure. The private blade processes are independent in this frozen construction. The one-blade birth-death transition rates include the hub in the denominator and give the stated tridiagonal resolvent and determinant ratio. The drift of the zero count is exactly its negative divided by the private clique size; integration gives an exposure expectation equal to the square of that size. Uniform bounded blade sizes then justify the Laplace logarithm and the stated error bound. Full-labelled-state and symbolic test programs passed on their declared finite domains. Limitation: those programs cannot substitute for the proof of the all-size assertion.

## Originality

**PASS, with priority risk.** The 1995 Ben-Naim–Frachebourg–Krapivsky source studies voter-model persistence as a temporal statistic on lattices and in mean-field regimes, not hub persistence up to a finite graph's consensus time on arbitrary clique bouquets. The 2007 Sood–Antal–Redner preprint establishes degree-weighted eventual-fixation probabilities, which are explicitly reused as a baseline, but these do not imply paths that contain no hub reversal. The 2014 Iwamasa–Masuda primary study addresses expected consensus times on distinct extremal graph classes. Primary paper sections and full-text search targets were inspected, as were indexed statements and accessible earlier claims. No directly covering same-graph, same-event, same-parameter theorem was found. This is not proof against unindexed prior calculations. Standard probabilistic tools themselves are not presented as novel.

## Mathematical value

**PASS.** Single-site persistence is an established, intrinsically dynamical question, distinct from consensus selection. The new exact graph-family factorization produces a quantitative structural law: the size-biased mean private clique size determines the limiting chance that a high-degree hub never changes opinion. In particular, private edges between leaves alter the limit from \(e^{-1}\) for a star to \(e^{-2}\) for a triangle friendship graph with the same hub degree. More generally the limit is \(e^{-r}\) for equal \(r\)-sized blades, whereas eventual fixation has the classical probability \(1/(r+1)\). This distinction between no-reversal persistence and eventual winner selection is mathematically motivated and not an arbitrary finite numerical slice.

## Closest literature and limitations

The closest published persistence study is Ben-Naim, Frachebourg and Krapivsky, arXiv:cond-mat/9511040v1 (1995). The fixation comparator is Sood, Antal and Redner, arXiv:0712.4288 (2007). Network-specific voter consensus-time analysis appears in Iwamasa and Masuda, arXiv:1404.6360 (2014). The result assumes one initially distinct hub and ordinary neighbor-copy voter dynamics. The bounded-blade-size requirement is essential to the stated uniform asymptotic; no result for arbitrarily growing blade sizes is asserted. Independent mathematical audit and worldwide historical-priority adjudication remain outstanding.

Self-review: passed. Independent audit: not yet performed.
