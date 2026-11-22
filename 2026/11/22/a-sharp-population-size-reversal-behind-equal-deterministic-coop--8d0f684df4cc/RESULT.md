# A sharp population-size reversal behind equal deterministic cooperation basins

## Finding

For a two-strategy population with an instantaneous strategy-dependent environment that reverses the two payoff rows, take the baseline payoffs \(R=3\), \(S=1\), \(P=0\) and \(1<T<2\). Every associated deterministic replicator equation has exactly equal basins of attraction for full defection and full cooperation, separated by \(x=1/2\). Nevertheless, in the finite-population, no-self-interaction Fermi pairwise-comparison process defined below, the single-mutant fixation probabilities \(\rho_C\) and \(\rho_D\) obey, **for every integer \(N\ge 2\) and every \(\beta>0\)**,

\[
\frac{\rho_C}{\rho_D}=\exp\left\{\frac{\beta}{6}\left[(2-T)(N-5)-6T\right]\right\}.
\]

Thus the odds reverse at the exact real population threshold \(N_*(T)=(10+T)/(2-T)\): \(\rho_C<\rho_D\) for \(N<N_*(T)\), equality at the threshold, and \(\rho_C>\rho_D\) for \(N>N_*(T)\). Independently, the cooperator is **strictly below neutral single-mutant fixation at every size and intensity**: \(\rho_C<1/N\). With \(T=3/2\), the odds ratio is \(\exp[\beta(N-23)/12]\), and \(N=23\) is the exact integer reversal point. Consequently the mutant cooperator can beat the mutant defector in the two-direction comparison while both are less successful than a neutral mutant. These are distinct selection criteria.

## Assumptions and scope

Let \(N\ge2\) individuals occupy a well-mixed population with \(i\) cooperators and \(x=i/N\). At each transient population composition, payoffs follow the deterministic instantaneous feedback matrix

\[
U(x)=(1-x)\begin{pmatrix}T&P\\R&S\end{pmatrix}+x\begin{pmatrix}R&S\\T&P\end{pmatrix},
\qquad (R,S,P,T)=(3,1,0,T),\quad 1<T<2.
\]

The first row and column correspond to cooperation. Payoffs are averages against independently chosen uniformly random *other* individuals, with self-interactions excluded. If \(U_{ab}(x)\) denotes the entries, define

\[
\pi_C(i)=\frac{(i-1)U_{CC}(x)+(N-i)U_{CD}(x)}{N-1},\quad
\pi_D(i)=\frac{iU_{DC}(x)+(N-i-1)U_{DD}(x)}{N-1},\quad
\Delta_i=\pi_C(i)-\pi_D(i).
\]

For \(\beta>0\), one update changes \(i\) by one with probabilities

\[
T_i^\pm=\frac{i(N-i)}{N^2}\frac{1}{1+\exp(\mp\beta\Delta_i)}.
\]

Zero and \(N\) are absorbing. \(\rho_C\) is the probability of reaching \(N\) from \(i=1\), whereas \(\rho_D\) is the probability of reaching zero from \(i=N-1\). This is a specified finite-population extension of the feedback payoff law; it is not a claim that the continuous model itself entails a unique stochastic update mechanism. In the infinite-population replicator limit the same feedback law yields the indicated equal-basin comparison.

## Proof

**1. Deterministic symmetry.** For the above feedback matrix, the infinite-population payoff difference is

\[
\pi_C(x)-\pi_D(x)=(2x-1)[1+(2-T)x].
\]

The bracket is strictly positive on \([0,1]\). Thus the replicator vector field \(x(1-x)(\pi_C-\pi_D)\) points left on \((0,1/2)\) and right on \((1/2,1)\); the two basins are intervals of equal length, independently of \(T\).

**2. Finite-state payoff sums.** Direct substitution of the four feedback-matrix entries into the no-self-interaction definitions gives

\[
\Delta_i=-\frac{N^2-NiT+NT-N+2i^2T-4i^2-iT+4i}{N(N-1)}.
\]

Summing the quadratic polynomial over \(i=1,\ldots,N-1\) gives two exact identities:

\[
\sum_{i=1}^{N-1}\Delta_i=\frac{(2-T)(N-5)-6T}{6},\qquad
W:=\sum_{i=1}^{N-1}(N-i)\Delta_i=-\frac{N^2+(2T-1)N-T+4}{6}.
\]

For \(N\ge2\) and \(1<T<2\), \(W<0\). For instance \(N^2+(2T-1)N-T+4>0\) follows from \(N^2\ge4\), \(2T-1>1\), \(N\ge2\), and \(-T+4>2\).

**3. Fixation-odds reversal.** The one-step ratio is \(T_i^-/T_i^+=\exp(-\beta\Delta_i)\). Write \(A_k=\sum_{i=1}^k\Delta_i\) and \(A_0=0\). The absorbing birth–death recurrence, or an elementary first-step calculation, yields

\[
\rho_C=\left[\sum_{k=0}^{N-1}\exp(-\beta A_k)\right]^{-1},\qquad
\rho_D=\frac{\exp(-\beta A_{N-1})}{\sum_{k=0}^{N-1}\exp(-\beta A_k)}.
\]

Dividing gives \(\rho_C/\rho_D=\exp(\beta A_{N-1})\). Apply step 2, observe \(2-T>0\), and solve the unique linear root of \(A_{N-1}\). For \(T=3/2\), the root is exactly \(23\).

**4. Neutrality distinction, uniformly for all intensities.** From step 2, \(\sum_{k=0}^{N-1}A_k=W<0\). Jensen's strict inequality for the convex exponential yields, whenever \(\beta>0\),

\[
\frac1N\sum_{k=0}^{N-1}\exp(-\beta A_k)
\;\ge\;\exp\left(-\frac{\beta}{N}\sum_{k=0}^{N-1}A_k\right)
=\exp(-\beta W/N)>1.
\]

Therefore \(\sum_k\exp(-\beta A_k)>N\), so \(\rho_C<1/N\) for every admissible parameter. At or above the odds-reversal threshold, the same strict neutral upper bound also holds for \(\rho_D\). This completes all claims.

## Verification

Run `python3 verify.py`. It independently evaluates the finite payoff matrix and pairwise-transition probabilities, checks the two polynomial-sum identities using exact rational arithmetic for sampled population sizes and several rational payoff parameters, solves the tridiagonal absorption recurrences numerically without inserting the closed fixation formula, and compares its probabilities with the analytically predicted odds. The infinite family is proved algebraically above; numerical finite tests are corroboration only. The script requires only the Python standard library.

## Relationship to prior work

Chen, Zhang and Li (arXiv:2610.21575, initially public 2026-10-15) define the row-reversing environmental-feedback matrix and analyze its deterministic game transitions and basins; the finite, no-self-encounter all-selection fixation-odds and neutrality contrast above are additional conclusions about an explicitly defined stochastic extension. Traulsen, Nowak and Pacheco (2006) provide the Fermi pairwise-comparison and classical birth–death fixation formula for fixed-payoff evolutionary games. The birth–death identity itself is **not** new. This result inserts a composition-dependent reversed payoff law and isolates the nontrivial exact size threshold together with the strictly subneutral cooperator probability across all selection intensities. Lv, Li and Zhao (2024) examine a related environmentally responsive **Moran** process and population size effects, so that study is a high-priority historical comparison; only its accessible abstract could be assessed, not its complete derivations. No exhaustive priority claim is made.

## Limitations

The conclusion depends on the specified instantaneous environment, no-self-payoff convention, fixed feedback parameters, and Fermi pairwise comparison rather than Moran reproduction or stochastically evolving environmental states. The example \(T=3/2\) is a transparent calibration of a larger continuous one-parameter family, not the entire scope. The ratio comparison \(\rho_C/\rho_D\) is different from \(\rho_C>1/N\); in this family the latter never occurs. The all-size statements are analytical, but independent historical-priority and mathematical auditing remain unperformed. A potentially relevant publisher article could not be inspected in full, so its precise overlap remains uncertain.

## References

1. Y. Chen, J.-Q. Zhang, B.-Q. Li, *Cooperation Dynamics with Environmental Feedback: Steady States and Transitions*, arXiv:2610.21575, first version 2026-10-15. https://arxiv.org/abs/2610.21575
2. A. Traulsen, M. A. Nowak, J. M. Pacheco, *Stochastic dynamics of invasion and fixation*, Physical Review E 74 (2006), 011909. https://doi.org/10.1103/PhysRevE.74.011909
3. S. Lv, J. Li, C. Zhao, *Fixation of cooperation in evolutionary games with environmental feedbacks*, Applied Mathematics and Computation 482 (2024), 128957. https://doi.org/10.1016/j.amc.2024.128957
4. The related finite and environmentally coupled evolutionary-game literature is described in the comparison section and associated scientific-review record; published full texts were compared where accessible.
