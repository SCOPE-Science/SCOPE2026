# A sharp unit-area transition and integer triple resonances for first-Hermite disk localization

## Finding

Let \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and \(h_1(t)=2\sqrt\pi\,t h_0(t)\), and let \(\{h_j\}_{j\ge0}\) be the normalized Hermite basis in \(L^2(\mathbb R)\). For \(s>0\), set \(\mathcal D_s=\{(x,\omega)\in\mathbb R^2:\pi(x^2+\omega^2)\le s\}\), which has ordinary Euclidean area \(s\). Define the positive time-frequency localization operator \(L_s=V_{h_1}^{*}\mathbf1_{\mathcal D_s}V_{h_1}\), using the short-time Fourier transform with the first excited Hermite window.

The eigenvalue \(\lambda_j(s)\) of \(L_s\) at \(h_j\) has the following closed forms:
\[
\lambda_0(s)=1-(1+s)e^{-s},\qquad
\lambda_j(s)=\frac1{j!}\int_0^s e^{-t}t^{j-1}(j-t)^2\,dt\quad (j\ge1).
\]
For every integer \(j\ge0\) and every \(s>0\), its successive spectral difference is
\[
\boxed{\lambda_{j+1}(s)-\lambda_j(s)
=-\frac{e^{-s}s^j}{(j+1)!}(s-j)(s-j-1).}
\]
Consequently, at each *positive integer* disk area \(m\), the eigenvalue corresponding to Hermite levels \(m-1,m,m+1\) is exactly triple, with no other levels at that eigenvalue; at noninteger areas no consecutive eigenvalues coincide.

The sharp concentration bound over **all** unit-norm signals in \(L^2(\mathbb R)\) is
\[
\boxed{\sup_{\|f\|_2=1}\int_{\mathcal D_s}|V_{h_1}f|^2
=\|L_s\|=\begin{cases}
1-(1+s^2)e^{-s},&0<s<1,\\
1-2e^{-1},&s=1,\\
1-(1+s)e^{-s},&s>1.
\end{cases}}
\]
For \(0<s<1\) precisely the unimodular multiples of \(h_1\) maximize the integral; for \(s>1\), precisely unimodular multiples of \(h_0\) do so. At \(s=1\), the maximizing unit vectors are **all** unit vectors of \(\operatorname{span}\{h_0,h_1,h_2\}\). In particular the top eigenspace changes from dimension one to three and back to one at exactly the unit-area threshold.

## Assumptions and scope

The short-time Fourier transform is \(V_gf(x,\omega)=\int_{\mathbb R}f(u)\overline{g(u-x)}e^{-2\pi i\omega u}\,du\). The Hermite basis is normalized in \(L^2(\mathbb R)\), with \(h_1=2\sqrt\pi\,t h_0\). There are no finite-band restrictions on the input signal. The disk is centered at the origin, its parameter is ordinary phase-plane area rather than radius, and the analysis window is the fixed first excited Hermite function, not the Gaussian. The theorem makes no claim about other windows or noncircular observation regions.

## Proof

**1. Exact spectral representation and normalization.** By the standard radial Hermite-window localization diagonalization (Abreu--Gröchenig--Romero, Section 4.2, Lemma 4.2), \(L_sh_j=\lambda_j(s)h_j\). With \(t=\pi(x^2+\omega^2)\), the normalized Hermite cross-spectrograms satisfy
\[
|V_{h_1}h_0(x,\omega)|^2=e^{-t}t,
\qquad |V_{h_1}h_j(x,\omega)|^2
=e^{-t}\frac{t^{j-1}(j-t)^2}{j!}\quad(j\ge1).
\]
These follow from the first Laguerre polynomial \(L_1^{j-1}(t)=j-t\) and the normalization of the complex Hermite functions. In polar variables the angular integration leaves exactly \(dt\), proving the integral formulas. Since the integrands are nonnegative and integrate to one on the entire half-line, \(0<\lambda_j(s)<1\). The localization operator is positive trace-class, \(\sum_{j\ge0}\lambda_j(s)=s\), and the Hermite modes are a complete eigenbasis.

**2. An identity for every adjacent pair.** Integrating the polynomial-exponential integrands gives, for \(j\ge1\),
\[
\lambda_j(s)=1-e^{-s}\sum_{\ell=0}^{j-1}\frac{s^\ell}{\ell!}
+(j-1-s)e^{-s}\frac{s^j}{j!}.
\]
Together with the formula for \(\lambda_0(s)\), direct subtraction and cancellation of the finite exponential sums yields
\[
\lambda_{j+1}(s)-\lambda_j(s)
=-\frac{e^{-s}s^j}{(j+1)!}(s-j)(s-j-1)
\quad(j=0,1,\ldots).
\]
For every positive integer \(m\), precisely the two adjacent differences at indices \(m-1\) and \(m\) vanish at \(s=m\). The difference is otherwise strictly negative: for indices below \(m-1\) both factors are positive, and for indices above \(m\) both factors are negative. Thus the three corresponding equal eigenvalues lie strictly between the preceding and following levels, giving **exactly** multiplicity three; for \(m=1\), these are the first three levels. For noninteger \(s>0\), no factor in any adjacent difference vanishes.

**3. Spectral maximum for small area.** If \(0<s<1\), the difference at \(j=0\) is strictly positive, while all differences at \(j\ge1\) are strictly negative. Therefore the unique largest eigenvalue is \(\lambda_1(s)\). Substituting \(j=1\) in the explicit formula gives \(\lambda_1(s)=1-(1+s^2)e^{-s}\). At \(s=1\), the first three eigenvalues tie and all others are strictly smaller.

**4. A strict half-energy bound at each integral mode crossing.** For every integer \(m\ge1\), the formula above gives
\[
\lambda_m(m)=\int_0^m\frac{t^me^{-t}}{m!}\,dt <\frac12.
\]
For the strict inequality, put \(f_m(t)=t^me^{-t}/m!\). For \(0<u<m\),
\[
\log\frac{f_m(m+u)}{f_m(m-u)}
=m\log\frac{m+u}{m-u}-2u>0,
\]
by \(\log\frac{1+v}{1-v}>2v\) for \(0<v<1\). Hence the mass of \(f_m\) between \(m\) and \(2m\) exceeds that between \(0\) and \(m\); there is also positive mass beyond \(2m\). As \(\int_0^\infty f_m(t)dt=1\), the claimed strict inequality follows. Furthermore, \(\lambda_0(s)\) is strictly increasing, and \(\lambda_0(2)=1-3e^{-2}>1/2\), using \(e^2>6\).

**5. Spectral maximum for larger area.** The first difference obeys \(\lambda_1(s)-\lambda_0(s)=e^{-s}s(1-s)<0\) for \(s>1\). Summing the first two differences gives
\[
\lambda_2(s)-\lambda_0(s)=\frac{e^{-s}s^2}{2}(1-s)<0\qquad(s>1).
\]
For \(1<s<2\), every difference with index \(j\ge2\) is strictly negative, so \(\lambda_0(s)\) dominates the remaining spectrum. For \(s\ge2\), put \(m=\lfloor s\rfloor\). All eigenvalues at indices \(1,\ldots,m\) are smaller than \(\lambda_0(s)\), because their successive differences from index zero are nonpositive and the first is strictly negative. If \(s\) is an integer, the remaining tail is no larger than \(\lambda_{m+1}(m)=\lambda_m(m)<1/2<\lambda_0(s)\). If \(m<s<m+1\), then monotonicity in disk area gives
\[
\lambda_{m+1}(s)<\lambda_{m+1}(m+1)<1/2<\lambda_0(s).
\]
For higher indices all successive differences are negative, so they too are strictly below \(\lambda_0(s)\). Thus \(\lambda_0(s)\) is the unique largest eigenvalue for every \(s>1\), with the asserted sharp norm and maximizing input signals.

## Verification

The standalone script `check.py` checks the finite-sum difference identity symbolically for 35 consecutive indices, verifies the exact rational polynomial coefficients at all 35 integer triple points, compares independently evaluated integral and closed-form eigenvalues at 238 test cases over 14 disk areas, and numerically checks the sharp norm and maximizing-index transition. It prints `FIRST_HERMITE_DISK_PASS` if all assertions succeed. These tests corroborate the calculation; the preceding proof establishes the statements for all areas and all Hermite indices.

## Relationship to prior work

The 2017 preprint of Abreu, Gröchenig and Romero establishes disk diagonalization and the integral eigenvalues for general Hermite windows (Lemma 4.2), and Remark 4.3 points out the collision of the first two eigenvalues in its first-excited-window figure. **The diagonalization, Laguerre formula and existence of that initial crossing are not new claims here.** What is established here beyond those statements is the uniform factorized difference for every adjacent pair, exact triple multiplicity at every positive integer area, a rigorous global comparison with all other infinitely many eigenvalues, and the complete piecewise sharp top-eigenvalue and equality-space formula. Knutsen's radial localization operator estimates use the Gaussian analysis window and fractal/Cantor radial regions, not this first-Hermite disk maximizer. Galbis's norm estimates concern radial Toeplitz symbols on the analytic Fock space, with Gaussian-window applications, rather than the stated first-excited-window all-mode maximizer.

## Limitations

The norm formula and crossings are specific to the first excited Hermite analysis window and origin-centered round disks. Other Hermite orders and geometries are not treated. The adjacent difference identity characterizes neighboring-level coincidences; it does not claim to classify all possible nonadjacent coincidences at noninteger areas. Finite calculations are corroborative, not proofs of the universal statements. Historical priority remains provisional, since equivalent spectral-ordering results might exist in specialist polyanalytic Fock or Landau-level literature despite the direct source comparisons.

## References

1. L. D. Abreu, K. Gröchenig, J. L. Romero, *Harmonic analysis in phase space and finite Weyl-Heisenberg ensembles*, arXiv:1704.03042, first public version 2017-04-10. Especially Section 4.2, Lemma 4.2 and Remark 4.3. https://arxiv.org/abs/1704.03042
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, arXiv:1907.00848, first public version 2019-07-01. https://arxiv.org/abs/1907.00848
3. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031, first public version 2021-02-03. https://arxiv.org/abs/2102.02031
