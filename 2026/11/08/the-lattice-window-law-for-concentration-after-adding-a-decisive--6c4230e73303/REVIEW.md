# Review of the lattice-window law for concentration after adding a decisive pair

## Correctness

PASS. The exact graph identity \(\mu=\sum_i d_i^2/(4m^2)=(m+W)/(2m^2)\) gives the precise edge-addition inequality without asymptotic approximation. The local degree sum conditional on the proposed pair being absent is exactly binomial, while the edge and wedge counts obey joint first-order laws. The centered statistic \(W-cm\) admits a linear-plus-quadratic centered-Bernoulli expansion with an exact variance and a strictly positive limiting variance \(c^2(1+c)/2\) after division by \(n\). The connected-overlap cumulant argument proves its normal limit; deleting the proposed pair's incident edges proves asymptotic independence from the local degree. The only arithmetic boundary is the integer value \(D=2c+1\), where the normal sign yields the stated Gaussian crossover. Exact finite graph and rational moment enumerations test the nonstandard algebra independently, and simulation is used only as a spot check. The proof does not claim finite computation proves asymptotic normality.

## Originality

PASS within accessible comparison evidence, with nonzero residual risk. Abe (arXiv:2606.05655, Proposition 4.1 and Sections 5–6) supplies the quadratic concentration definition, its minimal-winning-coalition overlap form, and a nonmonotonic two-group threshold example. The present result is **not** the assertion that this quadratic index exists or that some threshold changes have nonmonotone effects. It describes the probability of a **single random missing pair** increasing the index in sparse graphic games, with a countably infinite lattice of jumps and a quantitative root-size window. Hof–Kern–Kurz–Paulusma (arXiv:1805.02192, Sections 1–2) define graphic simple games but study the different critical-threshold parameter for weightedness, not Deegan–Packel concentration. Relevant indexed research records on Deegan–Packel ranking conflicts concern different indices/events and do not imply this probability distribution. Standard random-graph normal approximation does cover one technical ingredient (two-star fluctuations), but a separate exact insertion reduction, a local Poisson variable, a joint independence argument, and treatment of threshold atoms are required for the claimed result. The original paper's PDF was materially inspected; unindexed or differently named equivalents in other literature remain possible. This is not an assertion of unique priority or independent validation.

## Mathematical value

PASS. Coalition additions are a natural comparative-statics operation for a minimal-winning-coalition-based power measure; existing axiomatic formulas alone do not quantify its consequences in sparse organizations. The result supplies a precise probability of an unexpected **increase** in power concentration from adding an opportunity to cooperate. Its sharp threshold is not a single ordinary law-of-large-numbers limit: local integer degrees create infinitely many discontinuities, and global Gaussian fluctuations quantitatively resolve each narrow transition. The result is an all-parameter structural and distributional law, not an arbitrary small finite census or a routine numerical substitution.

## Closest literature and limitations

- T. Abe, *Measuring Concentration of Power in Approval Voting Games*, arXiv:2606.05655, public 2026-06-04, PDF v2 2026-06-26. General quadratic index and threshold-parameter nonmonotonicity; not the random single-pair law.
- F. Hof, W. Kern, S. Kurz, D. Paulusma, *Simple Games versus Weighted Voting Games*, arXiv:1805.02192, 2018. Graphic simple games and their distance to weighted voting, not random changes of squared Deegan–Packel concentration.
- Deegan and Packel, *A New Index of Power for Simple \(n\)-Person Games*, Int. J. Game Theory 7 (1978), 113–123, DOI 10.1007/BF01753239. Original power-index construction, not concentration-change asymptotics.

The theorem is restricted to sparse independent-edge graphic voting games and a proposed absent pair; correlated coalition models, other indices, and different edge-density scales are outside the proven scope. The related literature was searched but cannot be exhaustively ruled out. There was no independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
