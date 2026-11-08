# Self-review: the finite-innovation return window

## Correctness: PASS

The statement specifies the full triangular-array regime, including the even/odd parity distinction and the endpoint \(\lambda=0\). The forest representation converts a Fourier bias to the exact all-even-component probability; it is independently established in Peres--Qin's equation (37). The critical step is the joint convergence of fringe sizes at a *fixed* number of independently sampled cut labels. The proof controls ancestry events at order \(O((\log N)/N)\), localizes label birth times above a cutoff \(\delta\), and uses explicit multitype birth generators with bounded first moments on the localized interval. Poissonization and the telescoping odd-size series then yield the precise constant. The large-innovation regime uses a published nonasymptotic inequality, valid uniformly across the triangular array. The standalone script provides 135 finite checks; it is not an infinite proof.

## Originality: PASS, subject to independent historical-priority assessment

The main directly relevant source, Peres--Qin (2026), proves the exact parity/forest identity and upper/lower bounds for all finite parameters, but does not derive the critical \(N(1-\alpha_N)\) scaling constant. Their companion paper covers fixed-parameter mixing, and does not imply a limit in this triangular array. Meir--Moon's single-cut fringe-size law, given in Baur--Bertoin (2014), is explicitly acknowledged. Baur (2014) treats convergent percolation cluster trees under a condition requiring \((1-p(n))n^{p(n)}\to\infty\) for first-generation limits; this excludes the \(1-p(n)\asymp 1/n\) finite-cut window. The comparison is by hypotheses and conclusions, not title similarity. The remaining material historical risk is an equivalent finite-cut Poisson marking result in random-tree fragmentation or mutation literature not identified in the primary inspections.

## Mathematical value: PASS

The exact constant \(2^{-\lambda}\) resolves the quantitatively natural critical window for memory approaching perfect reinforcement. Existing two-sided finite-horizon bounds permit different limiting exponential rates, while the new result identifies the rate using a genuine Poisson marking mechanism. The joint cluster-size limit is independently meaningful as a finite-innovation boundary of recursive-tree percolation. This is not merely a reformulation of the single-edge marginal law, which alone does not imply independence of several marked components.

## Closest literature and limitations

Peres and Qin, *Transition probabilities of step-reinforced random walks*, arXiv:2604.07227 (2026), Corollary 1.6 and equation (37); Peres and Qin, *Mixing times of step-reinforced random walks*, arXiv:2604.07207 (2026); Baur and Bertoin, *Cutting edges at random in large recursive trees*, arXiv:1406.2238 (2014), Proposition 1 and §5; Baur, *Percolation on random recursive trees*, arXiv:1407.2508 (2014), Theorem 1 assumptions. The statement is confined to the fair two-point increment law and gives no error rate or extension to other finite groups. Priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
