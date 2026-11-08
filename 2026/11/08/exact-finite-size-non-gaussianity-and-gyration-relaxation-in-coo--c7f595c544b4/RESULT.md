# Exact finite-size non-Gaussianity and gyration relaxation in cooperative Brownian resetting

## Finding

For every integer \(N\ge2\), diffusion constant \(D>0\) and constant *unordered-pair* averaging rate \(\nu>0\), the centered, pair-averaging Brownian process below has a unique stationary law. Write \(Q=\sum_{i=1}^{N}Y_i^2\) for its centered squared radius and \(P_4=\sum_{i=1}^{N}Y_i^4\). The stationary moments are exactly

\[
\mathbb E Q=\frac{4D(N-1)}{\nu N},\qquad
\mathbb E Q^2=\frac{16D^2(N-1)(7N^2+13N-6)}{\nu^2N^2(7N-6)},
\]
\[
\mathbb E P_4=\frac{48D^2(N-1)(9N^2-13N+6)}{\nu^2N^3(7N-6)}.
\]

The stationary centered single-coordinate excess kurtosis and the pair-separation excess kurtosis are respectively

\[
\frac{\mathbb E[Y_1^4]}{\mathbb E[Y_1^2]^2}-3
=\frac{6N^2}{(N-1)(7N-6)},\qquad
\frac{\mathbb E[(Y_1-Y_2)^4]}{\mathbb E[(Y_1-Y_2)^2]^2}-3
=\frac{3(N+6)}{7N-6}.
\]

Both strictly decrease for integers \(N\ge2\), starting at \(3\) for \(N=2\), and tend respectively to \(6/7\) and \(3/7\) as \(N\to\infty\). By contrast, the centered gyration obeys the sharp self-averaging and dynamical identities

\[
\frac{\operatorname{Var}(Q)}{(\mathbb E Q)^2}
=\frac{2(13N-6)}{(N-1)(7N-6)}\sim\frac{26}{7N},
\qquad
\operatorname{Cov}_{\mathrm{stat}}(Q(0),Q(t))
=\operatorname{Var}_{\mathrm{stat}}(Q)e^{-\nu Nt/2},\ t\ge0.
\]

These statements give a single finite-size result: non-Gaussian local fluctuations persist even as the collective squared radius self-averages, while its centered autocovariance relaxes at one exact rate.

## Assumptions and scope

The state is \(X(t)=(X_1(t),\ldots,X_N(t))\in\mathbb R^N\). Between interactions, coordinates follow independent stochastic differential equations \(dX_i=\sqrt{2D}\,dB_i\). For each unordered distinct pair \(\{i,j\}\), an independent Poisson clock of rate \(\nu\) simultaneously maps \(X_i\) and \(X_j\) to \((X_i+X_j)/2\). Thus a given particle participates at total rate \((N-1)\nu\); there is no hidden normalization by the number of pairs. All Brownian drivers and clocks are mutually independent.

Define \(M=N^{-1}\sum_iX_i\) and \(Y_i=X_i-M\). Pair updates leave \(M\) unchanged; the full system has a diffusing center of mass and **no stationary probability law for its absolute positions**. The theorem concerns solely \(Y\) on the hyperplane \(\sum_iY_i=0\). The centered diffusion covariance is \(2D(I-\mathbf 1\mathbf 1^\top/N)\). The constant-rate model is the distance-independent case of cooperative self-organized resetting; the rate \(\nu\) is precisely the unordered-pair intensity, regardless of alternative normalizations used elsewhere.

## Proof

**1. Stationarity and integrability.** Couple two centered solutions using exactly the same Brownian motions and pair clocks. Their difference \(Z\) changes only under pair averaging. Since \(\sum_i Z_i=0\), the sum of pairwise squared-distance losses is

\[
\sum_{i<j}\bigl(\|Z^{ij}\|^2-\|Z\|^2\bigr)
=-\frac12\sum_{i<j}(Z_i-Z_j)^2
=-\frac N2\|Z\|^2.
\]

Thus \(\mathbb E\|Z(t)\|^2=e^{-\nu Nt/2}\|Z(0)\|^2\). The transition semigroup contracts quadratically integrable laws in \(W_2\) by \(e^{-\nu Nt/4}\). By fixed-time contraction on complete \(\mathcal P_2\), it has a unique invariant law. A quadratic-square drift bound gives its fourth moments: for \(Q\ge0\), \(0\le P_4\le Q^2\), and the generator identity derived below implies

\[
\mathcal LQ^2=4D(N+1)Q+\nu\bigl[-(N-3/4)Q^2+(N/4)P_4\bigr]
\le4D(N+1)Q-\frac{3\nu}{4}(N-1)Q^2.
\]

The standard truncated Lyapunov argument bounds stationary fourth moments. Consequently the moment balances used next are justified, rather than merely formal. Permutation symmetry of the unique invariant law gives exchangeable marginals.

**2. Closed exact generator equations.** At a given centered vector, write \(Q=\sum_iY_i^2\), \(P_4=\sum_iY_i^4\), and superscript \(ij\) for the state after averaging pair \(i,j\). Direct binomial expansion and \(\sum_iY_i=0\) give

\[
\sum_{i<j}(Q^{ij}-Q)=-\frac N2Q,\quad
\sum_{i<j}(P_4^{ij}-P_4)=\frac{3Q^2-7NP_4}{8},
\]
\[
\sum_{i<j}((Q^{ij})^2-Q^2)
=-\left(N-\frac34\right)Q^2+\frac N4P_4.
\]

The projected Brownian generator contributes respectively \(2D(N-1)\), \(12D(N-1)Q/N\), and \(4D(N+1)Q\) to \(Q\), \(P_4\), and \(Q^2\). Therefore

\[
\begin{aligned}
\mathcal LQ&=2D(N-1)-\frac{\nu N}{2}Q,\\
\mathcal LP_4&=\frac{12D(N-1)}NQ+\frac\nu8(3Q^2-7NP_4),\\
\mathcal LQ^2&=4D(N+1)Q+\nu\left[-\left(N-\frac34\right)Q^2+\frac N4P_4\right].
\end{aligned}
\]

Setting these three expectations to zero yields a nonsingular linear system in \(\mathbb EQ\), \(\mathbb EQ^2\), \(\mathbb EP_4\) for every integer \(N\ge2\) and gives the claimed formulas by elementary elimination. Their denominators are strictly positive on the stated domain.

**3. Local versus pair fluctuations.** Exchangeability gives \(\mathbb EY_1^2=\mathbb EQ/N\), \(\mathbb EY_1^4=\mathbb EP_4/N\). The deterministic centered identities

\[
\sum_{i<j}(Y_i-Y_j)^2=NQ,\qquad
\sum_{i<j}(Y_i-Y_j)^4=NP_4+3Q^2
\]

then give \(\mathbb E(Y_1-Y_2)^2=8D/(\nu N)\) and \(\mathbb E(Y_1-Y_2)^4=1536D^2/[\nu^2N(7N-6)]\), hence both kurtosis formulas. For real \(z\ge2\), the derivatives are

\[
\frac d{dz}\frac{6z^2}{(z-1)(7z-6)}
=\frac{6z(12-13z)}{(z-1)^2(7z-6)^2}<0,
\quad
\frac d{dz}\frac{3(z+6)}{7z-6}
=-\frac{144}{(7z-6)^2}<0.
\]

This proves strict finite-size monotonicity and the stated elementary limits.

**4. Gyration fluctuations and time correlations.** Subtracting \((\mathbb EQ)^2\) from \(\mathbb EQ^2\) gives the exact coefficient of variation in the finding. Since \(\mathcal LQ\) is affine in \(Q\), the Markov property gives

\[
\mathbb E[Q(t)\mid Y(0)]
=\mathbb EQ+e^{-\nu Nt/2}\bigl(Q(0)-\mathbb EQ\bigr).
\]

Multiplying by \(Q(0)-\mathbb EQ\) and averaging in the unique stationary law proves the exact covariance formula without a Gaussian approximation.

## Verification

The standalone `verify_moments.py` uses SymPy and Python's standard library. Run `python verify_moments.py`. It verifies the three symbolic moment equations, the two kurtosis identities, variance scaling, and limits; then evaluates five independent pair-update polynomial identities on 117 rational, mean-zero sample configurations for \(2\le N\le10\), and three stationary identities at nine positive parameter choices. It prints `PASSED 612 exact independent pair updates and moment identities`. Symbolic identities and the analytic proof establish the all-\(N\) conclusions; the finite tests are corroboration, not an exhaustive infinite certificate.

## Relationship to prior work

Meigel and Rulands, *Controlling noise with self-organized resetting*, arXiv:2312.09307, introduce this midpoint-pair resetting mechanism and discuss its distance-independent case \(\alpha=0\), mean-field localization and distribution tails. Their accessible full text, including the mathematical appendices, gives the motivating dynamics but does not explicitly state the exact finite-particle centered fourth moments, the pair and local excess-kurtosis formulas, their distinct non-Gaussian thermodynamic limits, or the exact centered gyration correlation in the displayed analysis. The finding is **not** a new cooperative-resetting model, a new tail law, or a claim about the stationary absolute position density.

Olsen's *Steady-state moments under resetting to a distribution* (2023) treats externally prescribed resetting distributions, rather than simultaneous endogenous two-particle averaging. Vilk, Assaf and Meerson's *Fluctuations and first-passage properties of systems of Brownian particles with reset* (2022) examines reset-to-origin mechanisms. Classical randomized gossip and noisy-consensus papers analyze related averaging contractions but use different noise protocols or target consensus rather than exact stationary fourth-order relative-position laws. These distinctions concern the hypotheses and mathematical implications, not merely paper titles.

## Limitations

Only the constant, pair-independent reset rate on a complete graph is considered. Distance-dependent kernels, heterogeneous pair rates, non-Brownian driving, full stationary densities and convergence in distribution as \(N\to\infty\) are not established. The nonzero excess-kurtosis limits are limits of **exact ratios of finite-\(N\) moments**, not by themselves a distributional limit theorem. Generic moment-generator machinery could make the formulas implicitly derivable from earlier work; priority beyond the inspected materials is not independently certified. No independent scientific audit has been performed.

## References

1. F. J. Meigel and S. Rulands, *Controlling noise with self-organized resetting*, arXiv:2312.09307, first publicly submitted 2023-12-14; full text: https://arxiv.org/html/2312.09307v2 ; initial submission: https://arxiv.org/abs/2312.09307 .
2. K. Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E 108, 044120 (2023), https://doi.org/10.1103/PhysRevE.108.044120 .
3. O. Vilk, M. Assaf and B. Meerson, *Fluctuations and first-passage properties of systems of Brownian particles with reset*, Physical Review E 106, 024117 (2022), https://doi.org/10.1103/PhysRevE.106.024117 .
4. S. Boyd et al., *Randomized Gossip Algorithms* (2006), https://stanford.edu/~boyd/papers/gossip.html .
5. R. Rajagopal and M. J. Wainwright, *Network-based consensus averaging with general noisy channels*, report 751 (2008), https://statistics.berkeley.edu/tech-reports/751 .
