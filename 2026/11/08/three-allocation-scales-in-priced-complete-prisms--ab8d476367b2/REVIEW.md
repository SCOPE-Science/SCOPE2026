# Scientific review: priced complete-prism resistance allocation

## Correctness — PASS

The theorem has a full analytic proof over all individual nonnegative conductance allocations for every integer \(n\ge4\), positive price \(c\), and positive budget \(B\). Strict convexity of the Kirchhoff index on the connected feasible region and a compactness argument give a unique full-budget optimizer. Graph automorphisms then force its two conductance classes. The exact Cartesian-product Laplacian spectrum proves the scalar objective, and its unique positive critical point gives the global minimum. Fixed-price rational derivative expansions establish the distinct linear, two-thirds-power, and square-root ratios and the budget fractions. The standalone Python verifier checks \(54\) exact rational Laplacian inversions against the spectral formula, \(144\) root-sign/budget tests, and \(4\) asymptotic samples, totaling `VERIFY_OK 202`. These are cross-checks, not substitutes for the infinite-domain proof.

## Originality — PASS, with priority uncertainty

The nearest general antecedent is A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph* (2008, 2006 conference version). Its full accessible paper develops convex resistance optimization and symmetry, and calculates a wheel and a two-clique barbell with only **one** joining edge. The present two-clique graph instead has a **perfect matching** of links, a different spectrum and optimizer, and a critical matching-price law with three exponents. The August 29, 2006 Boyd lecture likewise states the general inverse-eigenvalue criterion but not this classification. Bollobás and Brightwell (1997) study resistance properties of Cartesian graph products; the accessible abstract does not state any expenditure-constrained optimum. Other related studies concern fixed-weight prism indices or Laplacian spectral-gap rather than this resistance objective. Previous related specific results on cyclic prisms and matching-priced complete bipartite graphs do not imply this complete-prism claim for \(n\ge4\). The relevant full general framework was read; the remaining possibility of an unindexed equivalent analysis is explicitly acknowledged.

## Value — PASS

A complete matching between dense communities is a natural network-design object, not an arbitrary graph slice. The exact critical price \(c=1\) and its new \(n^{2/3}\) ratio separate two distinct spending regimes. Below the critical price the interlayer budget share remains positive as network size grows, while at and above the critical price it vanishes according to different power laws. These precise asymptotics quantify when to concentrate or dilute intercommunity investment, beyond merely restating the standard convex optimization framework.

## Sources and limitations

- S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, ICM Madrid lecture, August 29, 2006: https://web.stanford.edu/~boyd/papers/pdf/icm06_talk.pdf, especially slide 5.
- A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf, especially Sections 2 and 5.2 and pp. 60–61.
- B. Bollobás and G. Brightwell, *Random Walks and Electrical Resistances in Products of Graphs*, Discrete Applied Mathematics 73 (1997), 69–79, DOI 10.1016/S0166-218X(96)00002-9: https://digitalcommons.memphis.edu/facpubs/5572/ (abstract available).
- The general resistance framework has a July 2006 conference version but its exact first-public-release day is unresolved. The full text of Bollobás and Brightwell's product-graph article was not accessible. The graph and price class are restricted as stated, and independent mathematical review is still needed.

Self-review: passed. Independent audit: not yet performed.
