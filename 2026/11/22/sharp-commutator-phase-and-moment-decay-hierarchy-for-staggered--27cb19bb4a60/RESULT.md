# Sharp commutator phase and moment-decay hierarchy for staggered block projections

## Finding

For integers \(p\ge 2\) and \(1\le r<p\), let \(P\) and \(Q\) be the orthogonal block-averaging projections on \(\ell^2(\mathbb Z)\) associated with the partitions
\[
B_j=\{jp,\ldots,jp+p-1\},\qquad
C_j=\{jp+r,\ldots,jp+r+p-1\},\quad j\in\mathbb Z.
\]
Write \(\tau=r(p-r)/p^2\in(0,1/4]\), and set \(A=PQP\) on \(\operatorname{Ran}P\). The following statements together give one spectral-and-convergence classification of this staggered pair.

1. After identifying each unit block-constant vector with one coordinate of \(\ell^2(\mathbb Z)\), the alternating projection step is **exactly** the lazy discrete heat step
   \[
   A=I-\tau\Delta,\qquad (\Delta c)_j=2c_j-c_{j-1}-c_{j+1}.
   \]
   Its spectrum on \(\operatorname{Ran}P\) is \([1-4\tau,1]\). The powers converge strongly to zero on \(\operatorname{Ran}P\), but \(\|A^N\|=1\) for every integer \(N\ge1\).

2. The full and Fredholm essential spectra of the skew-adjoint commutator coincide:
   \[
   \sigma([P,Q])=\sigma_{\mathrm{ess}}([P,Q])
   =\{iy:-\kappa\le y\le\kappa\},
   \quad
   \kappa=\begin{cases}
   2\sqrt{\tau(1-4\tau)},&0<\tau<1/8,\\
   1/2,&1/8\le\tau\le1/4.
   \end{cases}
   \]
   Thus \(\|[P,Q]\|=\|[P,Q]\|_{\mathrm{ess}}=\kappa\). There are no nonzero eigenvalues. The zero eigenspace is trivial when \(p=2\) and infinite-dimensional when \(p\ge3\). In particular, the commutator is always noncompact. For a shift of one coordinate (\(r=1\)), the universal maximum \(1/2\) occurs for \(2\le p\le6\), and the norm is strictly smaller for every \(p\ge7\).

3. For a nonzero finitely supported block-constant vector \(x=\sum_{j\in\mathbb Z}c_jp^{-1/2}\mathbf1_{B_j}\), let \(k\ge0\) be the smallest integer with \(m_k=\sum_j j^k c_j\ne0\). Then the **sharp individual decay law** is
   \[
   \lim_{N\to\infty}N^{(2k+1)/4}\|A^Nx\|_2
   =\frac{|m_k|}{k!}
   \left[\frac{\Gamma(k+1/2)}{2\pi(2\tau)^{k+1/2}}\right]^{1/2}.
   \]
   In particular, for a single normalized block impulse \(u_0=p^{-1/2}\mathbf1_{B_0}\),
   \[
   \|A^Nu_0\|_2\sim (8\pi\tau N)^{-1/4}.
   \]
   Each additional vanishing block moment speeds the decay by one factor of \(N^{-1/2}\).

## Assumptions and scope

All spaces and spectra are complex-Hilbert-space objects; the same numerical bounds hold for real input vectors. The lattice is bilateral, not a half-line or a finite grid. Both partitions have the **same** width \(p\) and a nonzero relative integer stagger \(r\). The averaging projections preserve the normalized constant direction on each of their own blocks. The essential spectrum is the Fredholm essential spectrum. The asymptotic formula in item 3 is asserted for nonzero finitely supported input in \(\operatorname{Ran}P\) and not uniformly over all unit inputs.

## Proof

### Exact compressed heat operator

Set \(u_j=p^{-1/2}\mathbf1_{B_j}\), \(v_j=p^{-1/2}\mathbf1_{C_j}\). Each family is orthonormal and spans the corresponding projection range. Let \(U,V:\ell^2(\mathbb Z)\to\ell^2(\mathbb Z)\) be the isometries with \(Ue_j=u_j\), \(Ve_j=v_j\). The only nonzero overlaps for a fixed \(u_j\) are
\[
\langle u_j,v_j\rangle=1-r/p=:a,
\qquad\langle u_j,v_{j-1}\rangle=r/p=:b.
\]
Hence \(U^*V=aI+bS\), with \(S\) one of the two conventional orientations of the bilateral shift. Since \(P=UU^*\) and \(Q=VV^*\),
\[
U^*PQP U=(U^*V)(V^*U)
=(a^2+b^2)I+ab(S+S^*)
=I-ab(2I-S-S^*).
\]
Here \(a+b=1\), and \(ab=\tau\), establishing the heat-step identity. Fourier transform of the coarse lattice converts \(A\) into multiplication by
\[
\lambda(\theta)=a^2+b^2+2ab\cos\theta
=1-4\tau\sin^2(\theta/2),\qquad-\pi\le\theta\le\pi.
\]
Its range is \([1-4\tau,1]\). Since \(0\le\lambda(\theta)<1\) for almost every \(\theta\), dominated convergence gives strong convergence of powers to zero. Because \(\operatorname*{ess\,sup}\lambda=1\), \(\|A^N\|=1\) for every \(N\ge1\).

### Commutator spectrum and norm

The Fourier–Floquet decomposition for translation by \(p\) realizes the ambient Hilbert space as \(L^2(\mathbb T;\mathbb C^p)\). In each fiber \(P\) and \(Q\) have rank one, with unit range vectors \(u(\theta),v(\theta)\) satisfying
\[
|\langle u(\theta),v(\theta)\rangle|^2=\lambda(\theta).
\]
For two rank-one orthogonal projections onto unit vectors with squared inner-product modulus \(\lambda\), direct calculation in their span gives commutator eigenvalues \(\pm i\sqrt{\lambda(1-\lambda)}\), together with zero in the orthogonal complement. This remains valid by continuity at the degenerate endpoints. Thus the nonzero fiber eigenvalues here are
\[
\pm i\sqrt{\lambda(\theta)(1-\lambda(\theta))}.
\]
The scalar \(\lambda\) ranges continuously over \([1-4\tau,1]\); the continuous image of \(\sqrt{\lambda(1-\lambda)}\) is \([0,\kappa]\). Its maximum is \(1/2\) when the interval contains \(1/2\), equivalently \(\tau\ge1/8\). Otherwise the maximum is attained at \(\lambda=1-4\tau\) and equals \(2\sqrt{\tau(1-4\tau)}\).

The spectrum of a continuous matrix multiplier on the circle is the union of its fiber spectral ranges, and every point of that union belongs to the Fredholm essential spectrum: localized frequency packets provide mutually weakly null approximate eigenvectors. No nonzero scalar eigenvalue persists on a positive-measure frequency set, so there are no nonzero eigenvectors. If \(p=2\), the two fiber range vectors span \(\mathbb C^2\) almost everywhere, giving trivial kernel; if \(p\ge3\), their common orthogonal complement has fiber dimension \(p-2\) almost everywhere, giving an infinite-dimensional kernel. Norm equality follows from skew-adjoint normality. For \(r=1\), \(\tau=(p-1)/p^2\ge1/8\) holds for integers \(p=2,3,4,5,6\), and not for any integer \(p\ge7\).

### Sharp moment-decay asymptotics

Write \(F(\theta)=\sum_jc_je^{ij\theta}\), a trigonometric polynomial. By the minimality of \(k\),
\[
F(\theta)=\frac{i^km_k}{k!}\theta^k+O(\theta^{k+1}),\qquad
\lambda(\theta)=1-\tau\theta^2+O(\theta^4)
\quad(\theta\to0).
\]
Parseval yields
\[
\|A^Nx\|_2^2=\frac1{2\pi}\int_{-\pi}^{\pi}
\lambda(\theta)^{2N}|F(\theta)|^2\,d\theta.
\]
Off any small neighborhood of zero the integrand is exponentially small in \(N\); inside it, rescale \(\theta=y/\sqrt N\) and use a Gaussian dominating bound. The resulting integral is
\[
\lim_{N\to\infty}N^{k+1/2}\|A^Nx\|_2^2
=\frac{|m_k|^2}{2\pi(k!)^2}
\int_{\mathbb R} y^{2k}e^{-2\tau y^2}\,dy
=\frac{|m_k|^2\Gamma(k+1/2)}{2\pi(k!)^2(2\tau)^{k+1/2}}.
\]
Taking square roots gives the stated claim. A nonzero finite trigonometric polynomial has a zero of finite order at the origin, so a finite \(k\) always exists.

## Verification

The supplemental `verification/check_staggered.py` tests full commutator eigenvalue multisets and compressed spectra on 135 distinct finite cyclic Bloch models, the sharp norm transition for 276 width/stagger pairs, and twelve large-iteration heat-asymptotic ratios for the first three moment orders. Run it with a Python environment satisfying `verification/requirements.txt` by executing `python verification/check_staggered.py` from the package root. All tests passed in the tested environment. These finite tests support algebra and normalization only; the bilateral spectrum and asymptotic are proved by the analytic arguments above, not by numerical extrapolation.

## Relationship to prior work

The motivating 2019 paper of Borodin and Kopecká studies abstract alternating projection rates and proves an \(O(N^{-1/2})\) estimate for inputs in a particular sum of orthogonal complements. It does not identify this staggered-block heat multiplier or its localized impulse hierarchy. There is no contradiction: a single block impulse giving order \(N^{-1/4}\) lies outside that sum, as can also be inferred from the cited estimate. Badea and Seifert study a general convergence-rate dichotomy for products of projections without the concrete offset-grid coefficients. Loring's principal-angle decomposition and Dou–Du–Wang's anticommutator analysis explain the standard two-projection spectral technology, but do not compute this grid-dependent compression, its threshold, or its moment constants. A related unshifted integer-block calculation concerns unequal aligned grids and a finite collection of essential spectral points; it does not cover a staggered equal-width bilateral grid with a continuous essential interval.

## Limitations

The result is restricted to two uniform, equal-width shifted partitions of the entire bilateral lattice. Boundary effects on finite intervals or half-lines are not classified, nor are irregular partitions, unequal widths with stagger, or convergence rates for arbitrary infinite-support inputs. The general two-projection spectral mechanism is classical; the specific staggered-block symbol, sharp commutator transition, and moment-decay constants are the asserted contribution. Historical-priority searches cannot exclude every older multigrid, Markov averaging, or conditional-expectation formulation. No independent validation is asserted.

## References

- P. A. Borodin and E. Kopecká, *Alternating projections, remotest projections, and greedy approximation*, first publicly posted 14 November 2019, https://arxiv.org/abs/1911.06176.
- C. Badea and D. Seifert, *Ritt operators and convergence in the method of alternating projections*, first publicly posted 15 October 2015, https://arxiv.org/abs/1510.04560.
- T. A. Loring, *Principal angles and approximation for quaternionic projections*, first publicly posted 8 June 2013, https://arxiv.org/abs/1306.1923.
- Y.-N. Dou, H.-K. Du, and Y.-Q. Wang, *Spectra of anticommutator for two orthogonal projections*, first publicly posted 16 May 2017, https://arxiv.org/abs/1705.05866.
