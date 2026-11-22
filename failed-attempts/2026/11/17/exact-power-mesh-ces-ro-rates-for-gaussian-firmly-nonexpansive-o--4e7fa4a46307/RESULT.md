# Exact power-mesh Cesàro rates for Gaussian firmly nonexpansive orbits

## Finding
For each \(1/2<\alpha<1\) and \(0<\delta\leq \frac18\sqrt{\alpha 2^{\alpha-1}}\), there exist a real Hilbert space \(H=L^2(\mathbb R;\mathbb R)\), a firmly nonexpansive map \(T:H\to H\) with \(\operatorname{Fix}T=\{0\}\), and \(x_1\in H\) such that \(x_n=T^{n-1}x_1\rightharpoonup0\), while \(\|x_n\|\to\exp[-\delta^2\zeta(2\alpha)]>0\). Their Cesàro means \(Y_N=N^{-1}\sum_{n=1}^Nx_n\) have the **exact** asymptotic
\[
\lim_{N\to\infty}N^{1-\alpha}\|Y_N\|^2
=\frac{\sqrt\pi}{\delta(1+\alpha)}\exp[-2\delta^2\zeta(2\alpha)].
\]
Equivalently, \(\|Y_N\|\sim \frac{\pi^{1/4}}{\sqrt{\delta(1+\alpha)}}\exp[-\delta^2\zeta(2\alpha)]N^{-(1-\alpha)/2}\). The exponent and constant are sharp for this family because the displayed limit is strictly positive. The Gaussian Gram asymptotic itself holds for every fixed \(\delta>0\); the stated restriction ensures the firmly nonexpansive realization.

## Assumptions and scope
Fix the displayed \(\alpha,\delta\), and put \(d_n=\delta n^{-\alpha}\), \(t_1=0\), \(t_n=\sum_{k=1}^{n-1}d_k\), and \(\rho_n=\exp(-\sum_{k=1}^{n-1}d_k^2)\). Define the unit Gaussian curve in real \(L^2(\mathbb R)\) by
\[
u(t)(r)=\pi^{-1/4}\exp[-(r-2t)^2/2],\quad
x_n=\rho_n u(t_n).
\]
Its inner products are exactly \(\langle u(s),u(t)\rangle=\exp[-(s-t)^2]\). We use ordinary (unweighted) Cesàro averages, with \(N\) a positive integer and the usual Hilbert norm. \(\zeta\) denotes the convergent Riemann zeta series at arguments greater than one. All constants depend on fixed \(\alpha,\delta\); no uniformity as \(\alpha\to1\) or \(\delta\to0\) is asserted.

## Proof
**1. Realization as iterates.** The two power series \(\sum d_n^2\) and \(\sum d_n\) respectively converge and diverge because \(1/2<\alpha<1\). The mean value theorem and \(n\ge1\) give
\[
n^\alpha\big((n+1)^\alpha-n^\alpha\big)
\ge\alpha 2^{\alpha-1} n^{2\alpha-1}
\ge\alpha 2^{\alpha-1}\ge64\delta^2.
\]
Consequently \(d_1=\delta\le1/8\), and
\[
\frac1{d_{n+1}}-\frac1{d_n}
=\frac{(n+1)^\alpha-n^\alpha}{\delta}\ge64d_n.
\]
These are precisely the mesh assumptions (36) and (38)–(39) of Bauschke–Tung [1]. Their Theorem 7.1, applied to this Gaussian curve, supplies a firmly nonexpansive \(T\) on \(H\) with \(\operatorname{Fix}T=\{0\}\) and \(Tx_n=x_{n+1}\). Moreover \(t_n\to\infty\), so \(u(t_n)\rightharpoonup0\), while \(\rho_n\to\rho_\infty=\exp[-\delta^2\zeta(2\alpha)]>0\). The construction of \(T\), and these qualitative properties, are taken from [1], not claimed as new.

**2. A uniform Gaussian row bound.** For each \(1\le i\le N\), define
\[
J_{i,N}=\sum_{j=1}^N \exp[-(t_i-t_j)^2].
\]
Every increment among \(t_1,\ldots,t_N\) is at least \(\delta N^{-\alpha}\). Hence \(|t_i-t_j|\ge\delta |i-j|N^{-\alpha}\), and Gaussian integral comparison gives
\[
0<J_{i,N}\le1+2\sum_{h=1}^\infty e^{-\delta^2h^2N^{-2\alpha}}
\le1+\frac{\sqrt\pi}{\delta}N^\alpha.
\]
The same bound applies to the weighted rows \(A_{i,N}=\rho_i\sum_{j=1}^N\rho_j e^{-(t_i-t_j)^2}\), since \(0<\rho_j\le1\).

**3. Exact local row limit.** Choose any \(0<u<1\), and any integer sequence \(i_N\) with \(i_N/N\to u\). For bounded real \(z\) and \(h_N=\lfloor zN^\alpha\rfloor\), the mean value theorem applied to the defining sums gives
\[
t_{i_N+h_N}-t_{i_N}
=\delta h_N i_N^{-\alpha}+o(1)
\longrightarrow\frac{\delta z}{u^\alpha}.
\]
The error is uniform for \(z\) in compact sets because \(N^\alpha=o(N)\). The global row bound above also yields a Gaussian dominating tail \(\exp(-\delta^2 z^2)\) for the scaled displacement \(z=h/N^\alpha\); its integral outside \([-L,L]\) vanishes as \(L\to\infty\). Thus a Riemann-sum limit gives
\[
\frac{J_{i_N,N}}{N^\alpha}\longrightarrow
\int_{\mathbb R} e^{-\delta^2z^2/u^{2\alpha}}\,dz
=\frac{\sqrt\pi}{\delta}u^\alpha.
\]
For \(|h|\le LN^\alpha\), both indices \(i_N\) and \(i_N+h\) tend to infinity, whence \(\rho_{i_N}\rho_{i_N+h}\to\rho_\infty^2\) uniformly. The same dominating tail therefore gives
\[
\frac{A_{i_N,N}}{N^\alpha}\longrightarrow
\rho_\infty^2\frac{\sqrt\pi}{\delta}u^\alpha.
\]

**4. Global limit.** The Gram identity gives
\[
\|Y_N\|^2
=\frac1{N^2}\sum_{i,j=1}^N\rho_i\rho_j e^{-(t_i-t_j)^2}
=\frac1{N^2}\sum_{i=1}^NA_{i,N}.
\]
By Step 2, the quantities \(A_{i,N}/N^\alpha\) are bounded uniformly in \(i,N\). Viewing them as step functions on \((0,1)\), Step 3 supplies convergence at every fixed \(u\in(0,1)\). Dominated convergence therefore yields
\[
N^{1-\alpha}\|Y_N\|^2
=\frac1N\sum_{i=1}^N\frac{A_{i,N}}{N^\alpha}
\longrightarrow\rho_\infty^2\frac{\sqrt\pi}{\delta}\int_0^1u^\alpha\,du
=\rho_\infty^2\frac{\sqrt\pi}{\delta(1+\alpha)}.
\]
This proves the result and its strictly positive leading coefficient.

## Verification
The exact Gaussian Gram identity, row domination, and normalized local limit make the proof independent of computational extrapolation. The companion standalone program `check_gaussian.py` directly evaluates finite Gram sums for several power meshes, prints the finite-to-predicted ratios, and tests 40,000 instances of the mesh inequality. These are diagnostic checks, not a proof of an infinite-dimensional statement. Execute `python check_gaussian.py` with Python 3, NumPy, and SciPy.

## Relationship to prior work
Bauschke and Tung [1] construct the Gaussian firmly nonexpansive orbit family, give a positive lower bound for harmonic increments \(\delta/n\) (Example 7.4), and show ordinary Cesàro convergence for every admissible mesh with \(nd_n\to\infty\) (Theorem 7.6), including the particular \(n^{-3/4}/16\) increment sequence (Example 7.7). Their Lemma 4.3 and Theorem 7.6 already provide a useful global Gaussian row upper bound. The finding above adds the full interval \(1/2<\alpha<1\), an exact decay exponent for each \(\alpha\), and the leading constant including the orbit-norm factor. A separate published record [2] obtains an exact norm limit for the **harmonic** \(\alpha=1\) endpoint; that positive-limit formula does not cover the present shrinking-limit regime, where the neighborhood width is \(N^\alpha=o(N)\).

## Limitations
The firmly nonexpansive realization is invoked from [1], while the new assertion is the sharp asymptotic. The proof does not classify all firmly nonexpansive maps, give a uniform parameter-dependent error bound, or cover the critical \(\alpha=1\) endpoint. Equivalence to an older general theorem on irregular Gaussian Gram sums remains a possible priority risk. No independent audit has been performed.

## References
[1] H. H. Bauschke and T. T. Tung, *Cesàro means of firmly nonexpansive iterates need not converge strongly*, arXiv:2605.25491, first submitted 2026-05-25; Sections 5–7, especially (36), (39), (51), Theorem 7.1, Examples 7.4 and 7.7. https://arxiv.org/abs/2605.25491

[2] *Exact Cesàro norm limit for the harmonic firmly nonexpansive counterexample*, published research record, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ces-ro-norm-limit-for-the-harmonic-firmly-nonexpansive-cou--4fec08167fba
