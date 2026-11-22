# Self-review: elapsed-time stabilization on sparse conflict graphs

## Correctness

**PASS.** The exact model specifies the fixed initial colors, conflict-only guard, palette availability, independent rate-one clock processes, atomic updates, and physical stabilization time. The original same-color edge persists exactly until either endpoint's first clock; no recoloring can create a new conflict. This proves the max–min edge-clock identity for every clock realization without ties and gives the independent-set CDF directly. For surviving-edge indicators, all pairs with disjoint endpoint sets are independent. Counting ordered overlapping pairs gives precisely \(b_1=(m+D_2)q^4\), \(b_2=D_2q^3\), \(b_3=0\); the 1989 Stein–Chen inequality yields the displayed conservative total-variation error. With \(q=e^{-x/2}/\sqrt m\), the error tends to zero under the declared overlap condition and gives standard Gumbel after normalization \(2T-\log m\). The star and clique boundary formulas follow from independent first-clock times. The standalone deterministic checker passed 632,891 assertions but does not substitute for the infinite-graph proof.

## Originality

**PASS against inspected accessible statements, with risk.** The closest paper, arXiv:2611.17989v1, explicitly identifies the conflict graph, local-maximum/recoloring-count reduction, and the last-first-tick description under Poisson clocks. These established components are not asserted to be new. The same paper's main results and appendix focus on the *number of successful recolorings* and not a sparse-graph universal law for elapsed physical time. Arratia–Goldstein–Gordon (1989) gives a general Poisson-approximation theorem, not a stabilization-time conclusion or the graph overlap criterion in this setting. The novel statement compared here is the graph-uniform physical-time half-Gumbel theorem, its explicit structural \(D_2\) condition, quantitative error, and structurally contrasting non-Gumbel limits. Indexed search did not reveal an equivalent theorem, but this is not a proof of historical novelty. A broad prior vertex-percolation result could imply it through a nontrivial combination with the known clock representation; this residual risk remains.

## Value

**PASS.** The motivating work measures *recoloring moves*, whereas continuous-time deployment requires the *last clock event that removes a conflict*. This distinction changes scaling dramatically: on every bounded-degree sequence with a growing number of initial conflicts the physical completion time has a universal half-logarithmic Gumbel window, yet on stars it stays of constant order and on dense cliques its centered law is a second-extreme-value distribution. The precise overlapping-pair condition identifies what geometry supports rare unresolved edges acting independently, and the finite-sample error can be used to quantify this approximation. The theorem is a concise structural limit result, not a claim of a broad scheduling optimality result.

## Closest literature and limitations

De Panafieu–Mathieu–Potop-Butucaru–Tixeuil (2026), arXiv:2611.17989v1, Sections 2–3, 5, Appendix A; Arratia–Goldstein–Gordon (1989), Theorem 1. See `RESULT.md` for the precise scope and counterexamples. The hypothesis is sufficient, not claimed necessary. No independent mathematical assessment has been performed; unindexed or inaccessible priority remains possible.

Self-review: passed. Independent audit: not yet performed.
