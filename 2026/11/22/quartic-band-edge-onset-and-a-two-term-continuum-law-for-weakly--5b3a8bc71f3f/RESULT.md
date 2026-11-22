# Quartic band-edge onset and a two-term continuum law for weakly enhanced weighted shifts

## Finding

Let \(m\ge1\), \(\alpha>0\), and let \(S_{m,\alpha}\) be the unilateral shift on \(\ell^2(\mathbb N_0)\) with weights \(t_m=1+\alpha/m^2\) on the first \(m\) links and weight \(1\) thereafter. Write \(J_{m,\alpha}=S_{m,\alpha}+S_{m,\alpha}^*\). Its essential spectrum is \([-2,2]\). Set
\[
 a_j=\frac{(2j-1)^2\pi^2}{8},\qquad j=1,2,\ldots.
\]
For \(\alpha\ne a_j\) for every \(j\), the number of positive eigenvalues of \(J_{m,\alpha}\) larger than \(2\), for every sufficiently large \(m\), is exactly \(\#\{j:a_j<\alpha\}\). For each such index \(j\), there is a unique pair \(\sigma_j,\kappa_j>0\) satisfying
\[
 \sigma_j^2+\kappa_j^2=2\alpha,\qquad
 (j-\tfrac12)\pi<\sigma_j<\min\{j\pi,\sqrt{2\alpha}\},
 \qquad \sigma_j\cot\sigma_j=-\kappa_j.
\]
Numbering the eigenvalues in decreasing order, \(\lambda_{m,j}>2\), we have the **two-term sharp asymptotic**
\[
 \lambda_{m,j}=2+\frac{\kappa_j^2}{m^2}
 +\frac{2\kappa_j\sigma_j^2}{(1+\kappa_j)m^3}+O_{\alpha,j}(m^{-4}).
\]
At each *critical* coupling \(\alpha=a_j\), the \(j\)-th bound state still exists for all sufficiently large \(m\), but is a scale smaller:
\[
 \lambda_{m,j}-2=\frac{4a_j^2}{m^4}+O_j(m^{-5}).
\]
The same formulas yield the numerical-radius transition \(w(S_{m,\alpha})=\max\sigma(J_{m,\alpha})/2\). In particular \(w(S_{m,\alpha})=1\) for large \(m\) if \(\alpha<a_1\), while at \(\alpha=a_1\), \(m^4(w(S_{m,\alpha})-1)\to2a_1^2\).

The finite-size mechanism is explicit: with arbitrary fixed \(t>1\) on the first \(m\) links, the positive eigenvalues outside \([-2,2]\) are born, one at a time, at the distinct exact thresholds
\[
 t_{m,j}=\sec\!\left(\frac{(2j-1)\pi}{2(m+1)}\right),\qquad
 1\le j\le\left\lfloor\frac{m+1}{2}\right\rfloor.
\]
The finite-size thresholds alone are not asserted as new: the contribution is their joint weak-enhancement continuum limit, the exact \(m^{-3}\) correction, and the unexpectedly \(m^{-4}\) critical edge law.

## Assumptions and scope

All shifts act on complex \(\ell^2(\mathbb N_0)\), with the standard orthonormal basis. Eigenvalues are ordered among the positive isolated eigenvalues above the fixed essential edge \(2\), with multiplicity. The coupling \(\alpha>0\) is fixed as \(m\to\infty\). The remainder bounds hold for each fixed noncritical \(\alpha,j\), respectively each fixed critical index \(j\), and are not asserted uniform when the coupling itself approaches a threshold at an unspecified rate. At a critical coupling \(a_j\), any already-existing lower-index bound states retain their noncritical asymptotics; the quartic law concerns the newly born \(j\)-th state.

## Proof

**1. Exact discrete spectral reduction.** Since \(J_{m,\alpha}\) differs from the free half-line Jacobi matrix by finitely many off-diagonal entries, Weyl's theorem gives \(\sigma_{\mathrm{ess}}=[-2,2]\). Put \(t=t_m\). A bound eigenvalue \(\lambda>2\) obeys \(\lambda=2\cosh\eta\), \(\eta>0\), and \(\lambda<2t\): the latter follows from \(\|J\|\le2t\), with strictness because \(J\) is not the constant-\(t\) matrix. Therefore write \(\cos\theta=\cosh\eta/t\) with \(0<\theta<\pi/2\). For sites \(0\le n\le m\) the unique solution of the Jacobi recurrence normalized by \(x_0=1\) is \(x_n=U_n(\cos\theta)=\sin((n+1)\theta)/\sin\theta\). For \(n\ge m\), square summability forces \(x_{m+k}=x_me^{-k\eta}\). Matching at \(n=m\) yields precisely
\[
 t\sin(m\theta)=e^\eta\sin((m+1)\theta). \tag{1}
\]
Conversely every \(\eta>0\) satisfying (1) with \(\cos\theta=\cosh\eta/t\) gives an eigenvector, so the reduction is equivalent, not merely necessary. Irreducibility of the Jacobi matrix makes all eigenvalues outside the band simple; the bipartite sign change supplies a negative partner for each positive one.

**2. Exact threshold count.** At \(\eta=0\), write \(t=\sec\theta\). Multiplying (1) by \(\cos\theta\) gives \(\sin(m\theta)-\cos\theta\sin((m+1)\theta)=-\sin\theta\cos((m+1)\theta)=0\). Thus the positive critical values are the displayed \(t_{m,j}\). They are all distinct. For an exact count, use the Schur complement of \(2I-J\) against the free infinite tail: its threshold form on the first \(m+1\) coordinates has tridiagonal matrix \(H_m(t)\), with diagonal \(2\) on coordinates \(0,\ldots,m-1\), diagonal \(1\) at \(m\), and off-diagonal entries \(-t\). At spectral parameters decreasing to \(2\) from above, the negative inertia of the Schur complement equals the number of positive eigenvalues above the parameter; continuity yields the count above \(2\). The matrix \(H_m(t)/t\) has fixed off-diagonals \(-1\) and a strictly decreasing positive diagonal \((2/t,\ldots,2/t,1/t)\); its eigenvalues decrease strictly in \(t\). At \(t=1\) the form is positive, and it can change inertia only at the simple roots \(t_{m,j}\). Hence
\[
 \#\{\lambda(J)>2\}=\#\{j:t>t_{m,j}\}.
\]
At equality there is a non-square-summable constant tail (an edge resonance), rather than an eigenvector. Finally \(m^2(t_{m,j}-1)=a_j-2a_j/m+O_j(m^{-2})\), proving the claimed count, including the existence of the \(j\)-th state at \(\alpha=a_j\).

**3. Continuum equation and unique modes.** Introduce \(\eta=\kappa/m\), \(\sigma=\sqrt{2\alpha-\kappa^2}\) and \(\theta_m=\arccos(\cosh(\kappa/m)/(1+\alpha/m^2))\). On compact subsets of \(0\le\kappa<\sqrt{2\alpha}\),
\[
 m\theta_m=\sigma+O(m^{-2}),
\quad m\big[t_m\sin(m\theta_m)-e^{\kappa/m}\sin((m+1)\theta_m)\big]
 =-G(\kappa)+\frac{H(\kappa)}m+O(m^{-2}),
\]
where \(G(\kappa)=\kappa\sin\sigma+\sigma\cos\sigma\) and \(H(\kappa)=\sigma^2\sin\sigma-\kappa\sigma\cos\sigma\). For fixed \(\alpha\), each interval \(((j-1/2)\pi,\min(j\pi,\sqrt{2\alpha}))\) with \(\alpha>a_j\) contains exactly one solution: the function \(-\sigma\cot\sigma\) rises from zero to infinity (or exceeds \(\sqrt{2\alpha-\sigma^2}\) at the endpoint), whereas \(\sqrt{2\alpha-\sigma^2}\) decreases. There are no other bound-state branches by the exact count in step 2. These are precisely the asserted \(\sigma_j,\kappa_j\), with decreasing \(\kappa_j\) as \(j\) increases.

**4. First lattice correction.** At any positive root \(\kappa\), \(\cos\sigma=-\kappa\sin\sigma/\sigma\), so
\[
 H(\kappa)=2\alpha\sin\sigma,\qquad
 G'(\kappa)=\frac{2\alpha(1+\kappa)}{\sigma^2}\sin\sigma\ne0.
\]
The implicit-function argument applied to the uniform analytic expansion gives
\[
 \kappa_{m,j}=\kappa_j+\frac{\sigma_j^2}{(1+\kappa_j)m}+O(m^{-2}).
\]
Using \(2\cosh(\kappa_{m,j}/m)=2+\kappa_{m,j}^2/m^2+O(m^{-4})\) proves the \(m^{-3}\) term and \(O(m^{-4})\) remainder.

**5. Critical quartic edge.** For \(\alpha=a_j\), the limiting root is \(\kappa=0\), \(\sigma=(j-1/2)\pi\), and \(G'(0)=\sin\sigma\ne0\). The same expansion extends analytically through \(\kappa=0\) and yields \(\kappa_{m,j}=\sigma^2/m+O(m^{-2})=2a_j/m+O(m^{-2})\). In view of the strict finite threshold ordering in step 2 this root is positive and is the \(j\)-th bound state. Consequently \(\lambda_{m,j}-2=4a_j^2/m^4+O(m^{-5})\). This is a genuine eigenvalue, not merely an approximate resonance.

## Verification

The bundled `check.py` reproduces finite-dimensional spectral comparisons against the exact secular equation, the threshold counts, the noncritical \(m^{-3}\) coefficient, and the critical \(m^{-4}\) coefficient with explicit, stated tolerances. These finite tests only diagnose the proof; infinite-limit claims are justified by the analytic steps above.

## Relationship to prior work

Undrakh, Nakazato, Vandanjav and Chien (2015) provide an exact polynomial characterization of **all fixed finite-prefix** weighted-shift point spectra. The exact finite-prefix recurrence, hence also the existence of the finite threshold numbers in step 2, is pre-existing machinery, not independently novel. Vandanjav and Undrakh (2014) analyze individual and adjacent weighted bonds, and the known two-enhanced-bond threshold is recovered by the special case \(m=2\). Ghosh, Birbonshi and Ojha (2026) analyze another weighted-shift family with exponentially decaying periodic modulation. The new assertion is the combined growing-prefix/vanishing-contrast scaling, the sharp next-order drift for **every** positive edge state, and the \(m^{-4}\) birth at the exact continuum critical couplings. The continuum equation resembles the classical half-line finite-square-well problem; its leading zero-order form is not claimed novel. No complete published matching lattice second-order/critical law was identified in the inspected sources.

## Limitations

This is a concrete half-line, piecewise constant off-diagonal model. It does not establish an analogous law for arbitrary compactly supported or slowly varying bond profiles, nor uniformity for couplings approaching a threshold jointly with \(m\). General discrete-to-continuum approximation theory may offer alternative derivations, and a less-indexed matching lattice expansion remains a bibliographic risk. The self-review is not independent validation.

## References

1. A. Ghosh, R. Birbonshi and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486 (first public 2026-08-18). https://arxiv.org/abs/2608.17486
2. B. Undrakh, H. Nakazato, A. Vandanjav and M.-T. Chien, *The numerical radius of a weighted shift operator*, Electronic Journal of Linear Algebra **30** (2015), 944–963. https://journals.uwyo.edu/index.php/ela/article/download/1617/1617/
3. A. Vandanjav and B. Undrakh, *On the numerical range of some weighted shift matrices and operators*, Linear Algebra and its Applications **449** (2014), 76–88. https://doi.org/10.1016/j.laa.2014.02.018
