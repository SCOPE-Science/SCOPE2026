# Self-review

## Correctness — PASS

A fresh derivation uses the killed Brownian resolvent with Dirichlet boundaries at \(\pm L\), integrates the safe-reset probability over \((-L/2,L/2)\), and establishes the physical-time renewal including independent nonnegative waits. The exact formula is checked against 40 separately discretized backward-generator instances. Necessity at equality and for every positive reset rate follows from an analytic power-series with the first two coefficients vanishing and every coefficient from index three strictly positive, not a finite test. The proof states the existence but not the uniqueness of the optimal positive rate.

## Originality — PASS, qualified

Grange (arXiv:2111.15241) provides the exact ring winding mechanism and no-delay mean, whereas Evans–Majumdar (arXiv:1809.01551) provides general refractory reset renewal, Pal–Prasad (arXiv:1812.03009) studies standard absorbing endpoints under resetting, and Sunil et al. (arXiv:2304.09348) study restart costs on the line. Comparison of their stated objects and relevant mathematical sections does not identify the **sharp universal one-ninth threshold with strict global no-benefit at equality** in the terminal-reset winding geometry. Derivability by synthesizing general renewal formulas remains a real priority risk; the finding does not claim an independent new renewal method or known total literature coverage.

## Mathematical value — PASS

The mean delay for a physical reset is a natural control parameter missing from the instantaneous topological speedup model. The proved criterion is an exact if-and-only-if feasibility boundary rather than a small-rate heuristic, remains unchanged for every independent nonnegative waiting-time law of the same finite mean, and separates the strict equality case. It answers which physical protocols can realize the known speedup in this natural model.

## Closest literature and limitations

Primary full-text comparisons: Grange 2021, Evans–Majumdar 2018, Pal–Prasad 2018, Sunil et al. 2023. The proof assumes a zero-duration return jump, active-time-only Poisson events, independent finite-mean waits, and a specific shortest-arc topological completion rule. Optimal positive reset-rate uniqueness and finite-speed returns are unproved. Independent priority checking is still warranted.

Self-review: passed. Independent audit: not yet performed.
