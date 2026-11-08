# Scientific review

## Correctness — PASS
The objective is exactly the worst-case expected one-step energy reduction for exact serial coordinate minimization. A congruence transformation converts its optimization to strictly convex minimization of the sum of reciprocal diagonal obstacles. Slater's condition yields KKT necessity and sufficiency. The positive off-diagonal structure forces every optimum's residual PSD matrix to have rank one or two, and both cases are exhaustively classified by an explicit Gram-triangle certificate or three sign certificates. Reconstructing the proof confirms uniqueness and boundary cases. The packaged exact rational checker validates all formulas on 1000 triples with independently reconstructed primal and dual certificate matrices. Computations do not substitute for the infinite proof.

## Originality — PASS on inspected evidence, qualified
The 2013 optimal-probabilities paper optimizes ESO-based convergence bounds; the 2014 arbitrary-sampling paper provides a general framework; and the 2015 randomized-iterative-methods paper specifies a general semidefinite optimization in Section 5.1 without the evaluated three-coordinate four-candidate rule and rank transition. A published inverse-positive SPD formula covers some sign-gaugeable cases, but cannot handle the open region where all off-diagonal entries of the inverse three-cycle are negative. The two exact examples lie in this region and display distinct rank phases. Similarity searches over public research records and recoverable earlier claims found no statement with the same implication range. The 2000 Martinez--Wegman exact E-optimal-design article remains a material publication-priority risk because full text was inaccessible; no claim of exhaustive uniqueness in the literature is made.

## Mathematical value — PASS
Three positive pairwise correlations form the smallest complete odd cycle not reducible to an inverse-positive sign pattern. The classification replaces a semidefinite program by four finite algebraic tests and discovers a sharp geometric criterion for whether the limiting mode is simple or double. The exact full-parameter probability allocation is useful in assessing unbiased fixed serial sampling and supplies rational primal-dual certificates; it is not merely a scalar numerical improvement or an arbitrarily chosen instance.

## Limits
This is limited to three variables, strictly positive pairwise correlations, independent one-coordinate draws and exact line minimization. Adaptive and nonstationary samplers, higher dimensions, independent mathematical checking and final publication-priority certainty are outside the claim.

Self-review: passed. Independent audit: not yet performed.
