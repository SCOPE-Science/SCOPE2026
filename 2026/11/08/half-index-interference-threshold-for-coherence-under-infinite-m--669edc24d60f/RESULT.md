# Half-index interference threshold for coherence under infinite-mean renewal resetting of a quantum gate

## Finding

For a fixed finite-dimensional quantum gate, an infinite-mean renewal clock can drive the averaged state to complete dephasing between *distinct gate eigenphases*. The decay has two competing algebraic channels, one produced by trajectories that have not reset recently and the other by recent resets. For the exact power-law clock below, their dominant order changes at \(\alpha=1/2\).

Let the exact scalar coherence \(C_t(z)\) and analytic functions \(S_\alpha,H_\alpha\) be as defined below. For every \(|z|=1\), \(z\ne1\), the following asymptotics hold as the integer \(t\to\infty\):

\[
C_t(z)=\begin{cases}
z^tH_\alpha(z^{-1})t^{-\alpha}+o(t^{-\alpha}),&0<\alpha<1/2,\\
t^{-1/2}\left(S_{1/2}(z)/\pi+z^tH_{1/2}(z^{-1})\right)+o(t^{-1/2}),&\alpha=1/2,\\
\bigl(\sin(\pi\alpha)/\pi\bigr)S_\alpha(z)t^{\alpha-1}+o(t^{\alpha-1}),&1/2<\alpha<1.
\end{cases}
\]

For the physical two-level gate \(U=\operatorname{diag}(1,-1)\) reset to \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\), define the standard Dirichlet eta function \(\eta(\alpha)=\sum_{j\ge0}(-1)^j(j+1)^{-\alpha}\). Its measured \(\sigma_x\) expectation is real and has the sharp expression

\[
C_t(-1)=\begin{cases}
(-1)^t\,[2\eta(\alpha)]^{-1}t^{-\alpha}+o(t^{-\alpha}),&0<\alpha<1/2,\\
t^{-1/2}\bigl(\eta(1/2)/\pi+(-1)^t/[2\eta(1/2)]\bigr)+o(t^{-1/2}),&\alpha=1/2,\\
(\sin(\pi\alpha)/\pi)\eta(\alpha)t^{\alpha-1}+o(t^{\alpha-1}),&1/2<\alpha<1.
\end{cases}
\]

Hence the qubit coherence is eventually positive on even times and negative on odd times precisely for \(0<\alpha\le1/2\); for \(1/2<\alpha<1\) it is eventually positive at every time. Moreover, \(\|\rho_t-I/2\|_1=|C_t(-1)|\), and the decay exponent is sharp on both parities. The parity contrast is not merely an upper bound: all displayed limiting coefficients are nonzero.

## Assumptions and scope

Let \(\mathcal H\) have finite dimension, \(U\) be a unitary on \(\mathcal H\), and \(\rho_0\) be an arbitrary density matrix. A reset event replaces the state by the same \(\rho_0\), independently of its preceding evolution. Between events, exactly one application of \(U\) occurs per integer time step. At time zero the system is freshly reset. The reset intervals \(L_1,L_2,\ldots\) are independent and identically distributed positive integers with

\[
\Pr(L>n)=(n+1)^{-\alpha}\quad(n=0,1,2,\ldots),\qquad 0<\alpha<1.
\]

Thus \(\Pr(L=k)=k^{-\alpha}-(k+1)^{-\alpha}>0\), and \(\mathbb E L=\infty\). Write \(A_t\in\{0,\ldots,t\}\) for the age in unitary steps since the most recent reset. If \(P_\lambda\) denotes the spectral projection of \(U\) onto its (possibly degenerate) eigenvalue \(\lambda\), the resonance-preserving dephasing map is \(\mathcal D_U(\rho_0)=\sum_\lambda P_\lambda\rho_0P_\lambda\).

For \(|w|<1\), define \(S_\alpha(w)=\sum_{j\ge0}(j+1)^{-\alpha}w^j=\operatorname{Li}_\alpha(w)/w\), with its removable value \(S_\alpha(0)=1\). Define \(H_\alpha(w)=[(1-w)S_\alpha(w)]^{-1}\) and extend the expressions by analytic continuation to points on the unit circle other than \(1\). For any spectral eigenphase ratio \(z=\lambda/\mu\), set \(C_t(z)=\mathbb E[z^{A_t}]\). The conclusions distinguish \(z=1\), for which \(C_t(1)=1\), from \(z\ne1\).

The convergence and rates refer to the ensemble-averaged state, not to convergence of each individual unitary trajectory, and make no assertion about complete-positivity divisibility.

## Proof

**1. The renewal convolution is exact.** Write \(s_j=\Pr(L>j)=(j+1)^{-\alpha}\), \(f_k=\Pr(L=k)=s_{k-1}-s_k\), and let \(u_0=1\), \(u_n=\sum_{k=1}^{n}f_ku_{n-k}\) for \(n\ge1\). The event that the last reset before or at time \(t\) occurred at time \(t-j\) has probability \(u_{t-j}s_j\). Therefore

\[
\Pr(A_t=j)=u_{t-j}s_j,\qquad
C_t(z)=\sum_{j=0}^{t}u_{t-j}s_jz^j.
\]

If \(F(w)=\sum_{k\ge1}f_kw^k\), direct summation of \(f_k=s_{k-1}-s_k\) gives \(1-F(w)=(1-w)S_\alpha(w)\). Hence the renewal series \(H_\alpha(w)=\sum_{n\ge0}u_nw^n=1/(1-F(w))\). Multiplication of generating functions yields the exact, finite-time identity

\[
\sum_{t\ge0}C_t(z)w^t
=\frac{S_\alpha(zw)}{(1-w)S_\alpha(w)}
=H_\alpha(w)S_\alpha(zw).
\]

Since \(f_k>0\) for every positive integer \(k\), one has \(|F(w)|<1\) for \(|w|<1\) and \(|F(w)|<1\) also for \(|w|=1\), \(w\ne1\). The latter strict inequality follows from equality in the triangle inequality: all nonzero powers of \(w\) would have to agree, which forces \(w=1\). Thus \(H_\alpha\) has no spurious unit-circle poles. The polylogarithm has analytic continuation to slit neighborhoods of the circle away from its singularity at \(1\).

**2. The two singularities.** For \(0<\alpha<1\), the standard polylogarithm expansion, valid in a slit neighborhood of \(w=1\), gives

\[
S_\alpha(w)=\Gamma(1-\alpha)(1-w)^{\alpha-1}(1+o(1)),\qquad
H_\alpha(w)=\frac{(1-w)^{-\alpha}}{\Gamma(1-\alpha)}(1+o(1)).
\]

Fix \(|z|=1\), \(z\ne1\). The product \(H_\alpha(w)S_\alpha(zw)\) has precisely two potentially dominant singularities on the unit circle, at \(w=1\) and \(w=z^{-1}\). At the first, \(S_\alpha(zw)\) is analytic, with value \(S_\alpha(z)\), and the singular part is

\[
\frac{S_\alpha(z)}{\Gamma(1-\alpha)}(1-w)^{-\alpha}.
\]

At the second, \(H_\alpha(w)\) is analytic, with nonzero value \(H_\alpha(z^{-1})\), and the singular part is

\[
\Gamma(1-\alpha)H_\alpha(z^{-1})(1-zw)^{\alpha-1}.
\]

Apply the standard multiple-dominant-singularity coefficient-transfer theorem to these analytic slit expansions. The first contributes

\[
\frac{S_\alpha(z)}{\Gamma(1-\alpha)\Gamma(\alpha)}t^{\alpha-1}
=\frac{\sin(\pi\alpha)}{\pi}S_\alpha(z)t^{\alpha-1},
\]

and the second contributes \(z^tH_\alpha(z^{-1})t^{-\alpha}\). Local remainder terms are strictly smaller than the leading term or terms in each of the three stated regimes. In particular, the assertion does **not** claim that these are the first two terms of a uniform expansion for all \(\alpha\); a correction near \(w=1\) may outrank the subdominant endpoint for some parameters. Comparison of \(\alpha-1\) with \(-\alpha\) proves the three cases, with a tie at exactly \(\alpha=1/2\). Positivity of \(f_k\) ensures the coefficients are finite and nonzero when \(z\ne1\).

**3. Quantum dephasing and sharp parity threshold.** In an eigenbasis of \(U\), each matrix element evolves according to \(\langle i|\rho(t)|j\rangle=\langle i|\rho_0|j\rangle C_t(\lambda_i/\lambda_j)\). The preceding asymptotics make every ratio other than \(1\) vanish; ratios equal to \(1\) remain unchanged. Finiteness of the dimension proves \(\rho(t)\to\mathcal D_U(\rho_0)\) in trace norm.

For \(U=\operatorname{diag}(1,-1)\), \(\rho_0=|+\rangle\langle+|\), and \(z=-1\), the alternating Dirichlet series gives \(S_\alpha(-1)=\eta(\alpha)\) and

\[
H_\alpha(-1)=\frac{1}{2\eta(\alpha)}.
\]

Since the alternating terms decrease strictly, \(0<\eta(\alpha)<1\). At \(\alpha=1/2\), \(1/[2\eta(1/2)]>\eta(1/2)/\pi\), since \(2\eta(1/2)^2<2<\pi\). Thus the oscillatory term determines the sign on both parities at and below the threshold. Above the threshold, the constant positive term dominates. Finally, the eigenvalues of \(\rho_t-I/2\) are \(\pm C_t(-1)/2\), giving the trace-norm equality. The limiting coefficients on both parity subsequences are strictly nonzero, establishing the asserted sharp rates.

## Verification

A standalone standard-library program `verify.py` implements the independent renewal recursion and a separate age-state hazard recursion for this exact waiting-time distribution. It compares their complex and parity coherence outputs at finite integer times, checks probability normalization, evaluates the Dirichlet eta coefficient by an alternating Euler series, and performs finite-horizon asymptotic diagnostics for \(\alpha\in\{1/4,1/2,3/4\}\). Execute `python verify.py` in the same directory. At construction the program passed 936 finite diagnostic assertions. These finite diagnostics test formulas and normalization but do not establish the infinite-time statements; the analytic argument above does.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo (arXiv:2410.11497v1, first posted 2024-10-15) study discrete-time quantum gates under Poissonian and age-dependent resetting. Their Section IV treats qualitative convergence for selected decaying reset hazards and Appendix C analyzes no-reset probabilities. They do not state the two competing nonzero-frequency coherence amplitudes, their half-index crossover, or the eventually signed parity classification proved here. The present exact survival clock gives a particular positive-hazard power-law renewal process with *infinite mean*, whereas their showcased decaying hazards are parameterized differently.

Akimoto (arXiv:2306.00359v1) develops age and occupation statistics for ordinary and alternating renewals, including infinite-mean aging. Carollo and Wald (arXiv:2601.13367v1) give a general last-reset quantum renewal formula and analyze non-Markovianity; that general convolution is consistent with the first proof step here, but does not by itself state the sharp Fourier-mode rates and parity transition. The singularity-transfer tool of Flajolet and Odlyzko is classical and is used, not claimed as an original lemma.

## Limitations

The waiting-time tail is the **exact** law \((n+1)^{-\alpha}\), not an arbitrary regularly varying law. The dimension is finite, reset is complete and instantaneous, and each reset interval is independent of the quantum gate dynamics. The statement establishes ensemble-state convergence and scalar coherence asymptotics, not a trajectory-wise convergence theorem, a finite-mean stationary-age theorem, a central limit theorem or a universal claim for every heavy-tail slowly varying factor. For general complex eigenphase ratios, the two terms at the critical index can partially cancel on subsequences, so a uniform nonoscillating norm equivalence is not claimed. Priority relative to unindexed general renewal-Fourier theorems remains an open literature risk; independent scientific review has not been performed.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1 (2024-10-15), https://arxiv.org/html/2410.11497v1.
2. T. Akimoto, *Statistics of the number of renewals, occupation times and correlation in ordinary, equilibrium and aging alternating renewal processes*, arXiv:2306.00359v1 (2023-06-01), https://arxiv.org/html/2306.00359v1.
3. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367 (2026), https://arxiv.org/abs/2601.13367.
4. P. Flajolet and A. Odlyzko, *Singularity Analysis of Generating Functions*, SIAM J. Discrete Math. 3 (1990), https://doi.org/10.1137/0403019.
