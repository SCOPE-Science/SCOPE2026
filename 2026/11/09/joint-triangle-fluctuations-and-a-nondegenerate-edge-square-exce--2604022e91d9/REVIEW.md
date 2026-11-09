# Mathematical review of the finite-memory motif fluctuation theorem

## Correctness

**PASS.** The exact edge/triangle creation identities follow by checking the last two vertices of a triangle. Centering the creation bits gives the displayed linearized triangle statistic and the quadratic remainder identity. Exchangeability of a length-\(M\) Pólya word supplies the stationary Markov distribution, and an independent calculation of its innovation variance gives \(\rho(1-\rho)D_M\). The bounded martingale functional central limit theorem and the explicit quadratic-remainder bound yield the joint asymptotic, with the residual variance \(\frac{2}{15}\rho^3(1-\rho)D_M>0\). The accompanying exact-arithmetic checker independently verifies 8,615 identities and coefficient comparisons; the infinite argument remains analytic and no finite test is mistaken for a proof.

## Originality

**PASS, with priority risk.** Yu, Alajaji and Gharesifard (arXiv:2603.18452, Sections 3 and 4.2.2) present the finite-memory model and graph statistics but not this motif law. Konno, Masuda, Roy and Sarkar (arXiv:math/0505681, Section 4) already prove triangle central limit theorems for independent-weight threshold graphs, and Diaconis, Holmes and Janson (arXiv:0908.2448) explain equivalent threshold-graph representations; independence prevents these results from directly implying the displayed fixed-memory Markov coefficient. The separately established finite-memory edge fluctuation is credited and not treated as a novel component. The strictly positive joint residual is a new statement not implied by a scalar edge limit. Published research-record searches also compared percolation triangle covariance and threshold-graph random-greedy results; neither is the dependent-creation motif law. Possible broad Markov-dependent U-statistic theorems remain a residual priority risk.

## Mathematical value

**PASS.** Triangle density is a standard global motif statistic, not a chosen artificial slice. On the deterministic limit scale it equals the square of edge density, so identifying a *positive* second-order residual is a structural distinction. The exact \(2/15\) coefficient and fixed-memory factor quantify the residual and exhibit nontrivial joint edge–triangle behavior that an edge-only variance does not determine. The result completes a natural new statistic for the finite-memory extension rather than rephrasing a known edge law.

## Closest literature and limitations

The motivating paper's finite-memory regime is an explicit stochastic extension. Earlier static independent-weight threshold-network CLTs and independent graphon-sampling motif CLTs are relevant background but differ in the process dependence. The theorem assumes fixed positive reinforcement and fixed finite memory; no growing-memory or local-clustering theorem is asserted. The stated historical-priority comparison is best-knowledge and not definitive.

Self-review: passed. Independent audit: not yet performed.
