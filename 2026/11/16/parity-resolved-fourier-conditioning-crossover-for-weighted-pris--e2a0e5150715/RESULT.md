# Parity-resolved Fourier conditioning crossover for weighted prism dimers

## Finding

Let \(G_n=C_n\square K_2\) be the simple circular ladder, with \(n\ge3\) labelled columns, and sample a perfect matching with probability proportional to \(\lambda^{R}\), where \(\lambda>0\) and \(R\) is the number of selected rungs. Write \(X_i\in\{0,1\}\) for rung occupancy at column \(i\) and \(K_{ij}=\operatorname{Cov}(X_i,X_j)\). With orthonormal spatial Fourier vectors \(n^{-1/2}(e^{2\pi i j k/n})_{k=0}^{n-1}\), let \(\Lambda_j\) be the corresponding covariance eigenvalue. Put \(a=\operatorname{arsinh}(\lambda/2)\) and

\[
p_n(\lambda)=\mathbb E X_0=
\begin{cases}
\tanh a\,\coth(na),&n\text{ odd},\\
\tanh a\,\tanh(na/2),&n\text{ even}.
\end{cases}
\]

For **every** \(j=1,\ldots,n-1\), the complete nonconstant Fourier spectrum is

\[
\boxed{\displaystyle\Lambda_j=p_n(\lambda)\frac{4\cos^2(\pi j/n)}{\lambda^2+4\cos^2(\pi j/n)}.}
\]

The remaining eigenvalue is \(\Lambda_0=\lambda\,dp_n/d\lambda>0\). Therefore \(\operatorname{rank}K=n\) for odd \(n\), and \(\operatorname{rank}K=n-1\) for even \(n\), with the sole even-length null vector \(((-1)^i)_{i=0}^{n-1}\). Restrict to the mean-zero subspace, also removing that forced alternating null direction when \(n\) is even. Its sharp squared-energy condition ratio is

\[
\boxed{\displaystyle
\kappa_n(\lambda)=\frac{M_n}{m_n}\frac{\lambda^2+4m_n}{\lambda^2+4M_n},\quad
M_n=\cos^2(\pi/n),\quad
m_n=\begin{cases}\sin^2(\pi/(2n)),&n\text{ odd},\\
\sin^2(\pi/n),&n\text{ even}.
\end{cases}}
\]

At every positive activity, the largest retained Fourier modes are \(j=1,n-1\); the smallest are those nearest the alternating frequency (excluding the exact null when present). For each fixed \(\lambda>0\), the sharp parity-separated growth is

\[
\lim_{\substack{n\to\infty\\ n\text{ even}}}\frac{\kappa_n(\lambda)}{n^2}
=\frac{\lambda^2}{\pi^2(\lambda^2+4)},\qquad
\lim_{\substack{n\to\infty\\ n\text{ odd}}}\frac{\kappa_n(\lambda)}{n^2}
=\frac{4\lambda^2}{\pi^2(\lambda^2+4)}.
\]

At the **critical rung activity** \(\lambda=c/n\), for every fixed \(c>0\), the two parity classes instead have finite and distinct limits:

\[
\boxed{\displaystyle
\lim_{\substack{n\to\infty\\n\text{ even}}}\kappa_n(c/n)=1+\frac{c^2}{4\pi^2},\qquad
\lim_{\substack{n\to\infty\\n\text{ odd}}}\kappa_n(c/n)=1+\frac{c^2}{\pi^2}.}
\]

More precisely, write \(f_e(c)=\tfrac c2\tanh(c/4)\) and \(f_o(c)=\tfrac c2\coth(c/2)\). Then \(np_n(c/n)\to f_e(c)\) along even lengths and \(np_n(c/n)\to f_o(c)\) along odd lengths. For any fixed integer \(r\ge1\), the near-alternating eigenvalues along even lengths satisfy

\[
n\Lambda_{n/2-r}\longrightarrow f_e(c)\frac{4\pi^2r^2}{c^2+4\pi^2r^2},
\]

and for any fixed \(r\ge0\), along odd lengths,

\[
n\Lambda_{(n-1)/2-r}\longrightarrow
f_o(c)\frac{4\pi^2(r+\tfrac12)^2}{c^2+4\pi^2(r+\tfrac12)^2}.
\]

At every fixed nonzero Fourier index \(j\), \(n\Lambda_j\to f_e(c)\) or \(f_o(c)\) along the respective parity subsequence. These formulas give the complete critical soft-frequency profiles.

## Assumptions and scope

The prism is the **simple** graph, so \(n\ge3\); horizontal rail edges have weight one and each selected rung contributes a factor \(\lambda>0\). All Fourier eigenvalues refer to the covariance of the \(n\) labelled rung indicators, not to the full \(3n\)-edge incidence covariance. The condition ratio is specifically the ratio of extremal positive covariance eigenvalues on the *mean-zero* Fourier space after removing the forced even-length null mode. No assertion that this is the condition ratio on all positive covariance eigenspaces is made.

## Proof

**1. Exact weighted counting.** A perfect matching with at least one rung breaks each rail into the same disjoint paths; every gap between consecutive selected rungs must have even length, and the horizontal edges in each gap are forced. Consequently, these matchings correspond bijectively to monomer–dimer coverings of a single \(n\)-cycle, with each monomer weighted \(\lambda\). If \(n\) is even and no rung is present, the prism has four all-horizontal matchings while the single cycle has only two dimer coverings. This yields exactly two additional configurations. Let

\[
T=\begin{pmatrix}\lambda&1\\1&0\end{pmatrix},\qquad
\alpha=\frac{\lambda+\sqrt{\lambda^2+4}}2,\quad
\beta=\frac{\lambda-\sqrt{\lambda^2+4}}2.
\]

The partition function is therefore

\[
Z_n(\lambda)=\operatorname{tr}(T^n)+2\mathbf1_{2\mid n}
=\alpha^n+\beta^n+2\mathbf1_{2\mid n}.
\]

Set \(D=\sqrt{\lambda^2+4}\) and \(F_k=(\alpha^{k+1}-\beta^{k+1})/D\), for integers \(k\ge0\). Thus \(F_0=1\), \(F_1=\lambda\), and \(F_k=\lambda F_{k-1}+F_{k-2}\). For two distinct columns at cyclic distance \(1\le d<n\), fixing the corresponding rungs leaves two independent paths of lengths \(d-1\) and \(n-d-1\). Hence

\[
\mathbb P(X_0=1)=\frac{\lambda F_{n-1}}{Z_n}=p_n(\lambda),\qquad
\mathbb P(X_0=X_d=1)=\frac{\lambda^2F_{d-1}F_{n-d-1}}{Z_n}.
\]

Writing \(\alpha=e^a\) and \(\beta=-e^{-a}\) proves the stated odd/even formulas for \(p_n\): for odd \(n\), \(Z_n=2\sinh(na)\); for even \(n\), \(Z_n=4\cosh^2(na/2)\).

**2. Fourier diagonalization.** The covariance is circulant. Fix \(j\in\{1,\ldots,n-1\}\), put \(\omega=e^{-2\pi ij/n}\), \(\theta=2\pi j/n\), and \(r_0=\beta/\alpha\in(-1,0)\). Because \(\sum_{d=0}^{n-1}\omega^d=0\), centering drops out of the nonconstant Fourier transform except for the diagonal, giving

\[
\Lambda_j=p_n+\frac{\lambda^2}{Z_n}\sum_{d=1}^{n-1}F_{d-1}F_{n-d-1}\omega^d.
\]

Using \(\omega^n=1\) in two geometric sums yields the *exact* identity

\[
\sum_{d=1}^{n-1}F_{d-1}F_{n-d-1}\omega^d
=-\frac{\alpha^n(1-r_0^n)(1-r_0^2)}{D^2(1-2r_0\cos\theta+r_0^2)}.
\]

Substitute \(p_n=\lambda\alpha^n(1-r_0^n)/(DZ_n)\) and use \(\lambda/D=(1+r_0)/(1-r_0)\). It follows that

\[
\Lambda_j=p_n\left(1-\frac{(1+r_0)^2}{1-2r_0\cos\theta+r_0^2}\right)
=p_n\frac{4\cos^2(\theta/2)}{\lambda^2+4\cos^2(\theta/2)}.
\]

For the constant mode, \(\Lambda_0=n^{-1}\operatorname{Var}(\sum_iX_i)\). Logarithmic differentiation of \(Z_n(\lambda)\) gives \(\mathbb E\sum_iX_i=n p_n\) and \(\operatorname{Var}(\sum_iX_i)=\lambda\,d(n p_n)/d\lambda\), proving \(\Lambda_0=\lambda p_n'(\lambda)\).

**3. Nullity and exact extrema.** For \(\lambda>0\), the occupancy count has at least two attainable values with positive weight for every \(n\ge3\), so \(\Lambda_0>0\). The formula for \(j\ne0\) is positive except when \(\cos(\pi j/n)=0\), which occurs only at \(j=n/2\) for even \(n\). This is the deterministic alternating balance of the selected rungs. Since \(t\mapsto 4t/(\lambda^2+4t)\) is strictly increasing on \(t\ge0\), the largest and smallest retained squared cosines are exactly \(M_n\) and \(m_n\), giving the claimed extremizers and \(\kappa_n\).

**4. Critical and fixed-activity limits.** At fixed positive \(\lambda\), use \(\sin(\pi/n)\sim\pi/n\), \(\sin(\pi/(2n))\sim\pi/(2n)\) and \(\cos(\pi/n)\to1\) in the *exact* ratio. If \(\lambda=c/n\), \(a=\operatorname{arsinh}(c/(2n))\sim c/(2n)\). The explicit formulas for \(p_n\) give the stated limits \(f_e,f_o\), while the same trigonometric expansions give both finite condition-ratio limits. Taking \(j=n/2-r\) or \(j=(n-1)/2-r\) in the exact Fourier formula proves the asserted near-alternating profiles. Every limit holds along the indicated parity subsequence, with the stated fixed positive parameters.

## Verification

The accompanying standalone standard-library script, `rung_spectrum_checker.py`, independently enumerates all prism perfect matchings for \(3\le n\le14\) and compares the weighted partition functions, exact rational one- and two-rung moments, and the full numerical Fourier spectrum at three positive rational fugacities. It completed **666 assertions** successfully. Finite enumeration supports the closed formulas; the proof above, rather than these experiments, covers all \(n\) and all \(\lambda>0\).

## Relationship to prior work

The general dimer transfer-matrix framework, topological sectors and correlations are established in Wilkins–Powell (2021), which studies the even-by-even periodic square lattice and its thermodynamic-limit observables. Quitmann (2023) proves exponential decay of monomer/dimer correlations for fixed positive monomer activity in the lattice monomer–dimer model, without this finite-prism Fourier spectrum or shrinking-activity limit. The classical Heilmann–Lieb monomer–dimer theory supplies general partition-function and analyticity context. The uniform-activity specialization \(\lambda=1\) can be obtained from the known full-edge covariance analysis of uniform prism matchings; no new priority is claimed for that isolated case. The present claim is the **activity-dependent exact rung spectrum together with its parity-sensitive, sharp \(n^{-1}\)-activity conditioning crossover and near-alternating profiles**.

## Limitations

Only rung occupation observables are analysed. The prism is simple, so the two-column multigraph is excluded. The condition ratio deliberately omits the constant spatial mode and any deterministic alternating null mode; the constant-mode eigenvalue is nevertheless given exactly. Historical priority is provisional: a specialized one-dimensional dimer structure-factor calculation could imply the result despite not appearing in the checked literature. No independent mathematical audit has been performed.

## References

1. N. Wilkins and S. Powell, *Topological sectors, dimer correlations and monomers from the transfer-matrix solution of the dimer model*, arXiv:2103.03260, first version 2021-03-04, https://arxiv.org/abs/2103.03260.
2. A. Quitmann, *Decay of correlations in the monomer-dimer model*, arXiv:2309.13632, first version 2023-09-24, https://arxiv.org/abs/2309.13632.
3. O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics **25** (1972), 190–232, https://doi.org/10.1007/BF01877590.
