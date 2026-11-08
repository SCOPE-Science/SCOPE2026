# Scientific review: parity-optimal two-walker cover starts

## Correctness (PASS)
The two-side coupon-collector reduction is exact because each walk's next destination is independent uniform on the opposite side. Even deadlines reduce to the \(2\times2\) log-concavity minor of the surjection counts \(j!S(N,j)\), and the recurrence \(a_{N+1,j}=j(a_{N,j}+a_{N,j-1})\) gives a self-contained induction for nonnegative and sharp strict minors. The odd formula follows from a first-draw identity and conditioning; duplicate starts admit an exact pathwise dominance coupling. The claim's quantifiers, time-zero convention, boundary cases and all optimal starting geometries are explicit. Independently enumerating labeled two-walk trajectories gave 81 exact CDF equalities; further checker assertions covered 672 parity comparisons and 378 surjection inequalities.

## Originality (PASS, qualified)
Published multiwalk cover-time bounds in Rivera–Sauerwald–Sylvester do not supply this exact deadline-by-deadline optimal initial placement for non-lazy \(K_{n,n}\). Dey–Kim–Terlov examine collaborative ranges and pose questions about initial seeds, rather than proving the full-coverage probability parity reversal. Relevant other finite-graph hitting and graph-indexed range results do not imply the statement under the same objects and quantifiers. Cross-formulation and stronger-coverage searches found no known implication, but literature discovery is not exhaustive. An overlooked exact joint cover-time formula could imply this result; this is the main residual historical-priority risk.

## Value (PASS)
Selecting initial sites to maximize the chance that multiple explorers completely cover a network by a prescribed deadline is a natural stochastic optimization problem. This theorem completely classifies two-walker starting placements over an infinite graph family, gives sharp strictness thresholds, and proves a genuine odd–even reversal that rules out a universally stochastically optimal start. It is not an isolated tabulated example or a mere adjustment of a known constant.

## Closest literature and limitations
See Rivera–Sauerwald–Sylvester, arXiv:2011.07893 (2020); and Dey–Kim–Terlov, arXiv:2302.14241 (2023). The stochastic comparisons are confined to independent synchronous non-lazy walks and balanced complete bipartite graphs. None of the finite verification runs is used to infer the general theorem.

Self-review: passed. Independent audit: not yet performed.
