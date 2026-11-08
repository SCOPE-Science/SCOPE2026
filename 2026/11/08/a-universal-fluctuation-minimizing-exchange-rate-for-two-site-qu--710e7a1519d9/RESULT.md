# A universal fluctuation-minimizing exchange rate for two-site quantum failure

## Finding

For the resonant two-site amplitude-damping spin chain initialized with both spins excited, let the local loss rates be \(x=\gamma_1>0\) and \(y=\gamma_2>0\), and the exchange coupling be \(J\geq0\). Denote by \(T\) the first time at which the absorbing zero-excitation state is reached; let \(C(J)^2=\operatorname{Var}(T)/(\mathbb ET)^2\) be its squared coefficient of variation. Define \(s=x+y\), \(p=xy\) and \(q=x^2+xy+y^2\). Then

\[
\mathbb ET=\frac{q+12J^2}{s(p+4J^2)},\qquad
C(J)^2=\frac{80J^4+8J^2(9p-s^2)+q^2-4p^2}{(q+12J^2)^2}.
\]

If \(x\ne y\), the squared coefficient of variation is strictly decreasing for \(0<J<s/(2\sqrt2)\), has its **unique global minimum** at

\[
\boxed{J_*=\frac{x+y}{2\sqrt2}},\qquad
\boxed{C(J_*)^2=\frac{x^2+8xy+y^2}{5x^2+8xy+5y^2}},
\]

and is strictly increasing for \(J>J_*\). Simultaneously, the mean lifetime is strictly decreasing for all positive \(J\); hence every coupling \(J>J_*\) is strictly dominated by \(J_*\) in the two-objective comparison of larger mean lifetime and smaller time-to-failure coefficient of variation, and the undominated set of nonnegative couplings is exactly \([0,J_*]\). The optimum always lies in the underdamped sector, beyond the exceptional point \(J_{\mathrm{EP}}=|x-y|/4\). If \(x=y\), the full failure-time distribution, and therefore \(C(J)^2=5/9\), are independent of \(J\); uniqueness and strict tradeoffs do not apply.

## Assumptions and scope

The Hamiltonian is resonant (equal on-site energy), with exchange \(J(\sigma_+^{(1)}\sigma_-^{(2)}+\sigma_-^{(1)}\sigma_+^{(2)})\). Evolution obeys the time-homogeneous Lindblad equation with jump operators \(L_i=\sqrt{\gamma_i}\sigma_-^{(i)}\), positive fixed rates and no common-bath or cross-dissipative channels. The initial density matrix is \(|11\rangle\langle11|\). The ground state \(|00\rangle\) is absorbing, so \(\Pr(T>t)=1-\langle00|\rho(t)|00\rangle\). These conclusions concern the ideal continuous-time failure variable, not a finite-bin hazard estimator. No detuning, pumping, feedback, dephasing, or more than two spins is included.

## Proof

Write the reduced real state vector \(z=(\rho_{11},\rho_{22},\rho_{33},\rho_m)^\top\), where the first two components are the populations of the two single-excitation basis states, the third is the double-excitation population, and \(\rho_m=2\operatorname{Im}\rho_{12}\). It evolves as \(z'=Az\), with

\[
A=\begin{pmatrix}
-x&0&y&J\\
0&-y&x&-J\\
0&0&-s&0\\
-2J&2J&0&-s/2
\end{pmatrix},\qquad z(0)=e_3=(0,0,1,0)^\top.
\]

Let \(w=(1,1,1,0)^\top\). Then \(\Pr(T>t)=w^\top e^{At}e_3\). Since the mean excitation number \(N(t)\) obeys \(N'(t)=-x\langle n_1\rangle-y\langle n_2\rangle\leq-\min(x,y)N(t)\), while \(\Pr(T>t)\leq N(t)\), the bound \(\Pr(T>t)\leq2e^{-\min(x,y)t}\) gives all required moment integrals. Moreover, the transient generator \(A\) has only strictly stable modes for positive losses (e.g. by decay of the excitation-number Lyapunov observable), so \(B=-A\) is invertible. Survival integration now yields

\[
\mathbb ET=w^\top B^{-1}e_3,\qquad
\mathbb ET^2=2w^\top B^{-2}e_3.
\]

Two exact linear solves (or integration of the original closed-form survival function) give the first formula above and

\[
\mathbb ET^2=\frac{2\bigl(112J^4+8J^2(s^2+3p)+q^2-2p^2\bigr)}{s^2(p+4J^2)^2}.
\]

Subtracting \((\mathbb ET)^2\) and normalizing by that square gives the stated rational expression for \(C^2\). Its numerator is positive, because it also equals the positive physical variance divided by a positive square. Exact differentiation factorizes as

\[
\frac{dC(J)^2}{dJ}=-\frac{64J(x-y)^2\bigl(s^2-8J^2\bigr)}{(q+12J^2)^3},\qquad
\frac{d\,\mathbb ET}{dJ}=-\frac{8J(x-y)^2}{s(p+4J^2)^2}.
\]

For unequal rates, the first derivative switches sign exactly once on the positive coupling axis, at \(J_*=s/(2\sqrt2)\), and the second is always negative. Evaluating \(C^2\) there gives the minimum in the finding. The strong-coupling limit is \(5/9\), and its excess over the optimum is exactly

\[
\frac59-C(J_*)^2=\frac{16(x-y)^2}{9(5x^2+8xy+5y^2)}>0.
\]

Thus the minimum is genuine, and the asserted Pareto statement follows: for \(J>J_*\), both smaller mean lifetime and larger coefficient of variation make \(J_*\) strictly preferable; on \([0,J_*]\) the mean and coefficient of variation decrease together, so no two different points dominate each other under the stated conflicting objectives. Finally, since \(s>|x-y|\), \(s/(2\sqrt2)>|x-y|/4\). For equal rates, the exchange Hamiltonian commutes with the surviving symmetric single-excitation density matrix, so its dependence cancels; the two independent identical exponential losses give \(C^2=5/9\) and the rational formula confirms it.

## Verification

Run the self-contained Python standard-library program \(\texttt{python3 verify.py}\). It independently solves the transient-generator linear equations over exact rational numbers for a grid of positive loss rates and couplings, checks both moments and the claimed factorization against rational expressions, verifies the optimized value and strong-coupling bound, and compares separate spectral-mode evaluations at several real parameter points. The resulting output was `PASS: 2135 exact-rational identities / independent spectral assertions`. A finite test grid is not a proof for all positive rates; the full result follows from the symbolic identities and derivative signs above. For a concrete check, \((x,y)=(2,1)\) yields \(C(0)^2=33/49\), \(C(J_*)^2=21/41\), and \(\lim_{J\to\infty}C(J)^2=5/9\).

## Relationship to prior work

Sun and Zhou, *Reliability Dynamics in a Two-Site Dissipative Quantum Spin Chain* (2026), introduced this precise local-Lindblad failure model and derived the closed-form survival probability, hazard and overdamped-to-underdamped threshold, as well as a first-passage-data measurement proposal. Their Section VII.3 computes the sampling **variance of a binned hazard estimator**; this is distinct from the intrinsic variance of the random failure time considered here. The first and second time-to-failure moments and their coupling-optimal coefficient of variation are further consequences of the known survival solution, not independent new Lindblad dynamics. Menczel et al., *Full counting statistics and first-passage times in quantum Markovian processes* (2025), provide broad first-passage moment tools for Lindblad dynamics, which can also recover moments in an appropriate absorbing-model specialization; the claimed distinct conclusion here is the sharp universal physical tuning rule and its lifetime–fluctuation frontier, not general moment methodology.

## Limitations

The universal optimizer depends on the exact two-site resonant, no-reexcitation and independent-local-loss assumptions. It is an optimizer of **relative lifetime fluctuations**, not of survival at every time, absolute failure-time variance, or device lifespan. Experimental finite-bin estimators introduce sampling error not covered here. The result is elementary enough to be derivable from published survival and general moment formulas, so independent literature-priority validation is still needed. This analysis does not claim optimality for detuned, correlated-bath, driven, or multi-site chains.

## References

1. B. Sun and D. L. Zhou, *Reliability Dynamics in a Two-Site Dissipative Quantum Spin Chain*, arXiv:2603.11484 (first public March 12, 2026), https://arxiv.org/abs/2603.11484 . Sections III–VII and the analytical survival derivation.
2. P. Menczel, C. Flindt, F. Brange, F. Nori, and C. Gneiting, *Full counting statistics and first-passage times in quantum Markovian processes: Ensemble relations, metastability, and fluctuation theorems*, arXiv:2508.18614 (first public August 26, 2025), https://arxiv.org/abs/2508.18614 . First-passage moment and cumulant methods.
