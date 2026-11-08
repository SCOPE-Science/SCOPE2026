# The triple Hermite spectral crossing for disk localization with a first-excited window

## Finding

Let \(h_0(t)=2^{1/4}e^{-\pi t^2}\), \(h_1(t)=2\sqrt\pi\,t h_0(t)\), and \(D_A=\{(x,\xi)\in\mathbb R^2:\pi(x^2+\xi^2)<A\}\) for \(A>0\). The positive, trace-class concentration operator \(L_A=V_{h_1}^*\mathbf1_{D_A}V_{h_1}\) has the complete following nearest-neighbour spectral ordering.

For each integer \(n\ge1\), its Hermite eigenvalues satisfy
\[
\lambda_n(A)-\lambda_{n-1}(A)=-\frac{e^{-A}A^{n-1}}{n!}(A-n+1)(A-n).
\]
At a noninteger area \(m<A<m+1\), \(m\in\mathbb N_0\), exactly one adjacent step, from \(m\) to \(m+1\), increases; every other adjacent step decreases. At every integer \(A=m\ge1\), exactly the two adjacent gaps indexed \(m\) and \(m+1\) vanish; the three consecutive Hermite levels \(m-1,m,m+1\) coincide.

The **global** maximum undergoes one transition: for \(0<A<1\) the sole maximizing Hermite direction is \(h_1\); for \(A=1\) the top eigenspace is precisely \(\operatorname{span}\{h_0,h_1,h_2\}\); for \(A>1\) the sole maximizing Hermite direction is \(h_0\). The sharp norm is therefore
\[
\|L_A\|=\begin{cases}1-(A^2+1)e^{-A},&0<A<1,\\1-2/e,&A=1,\\1-(A+1)e^{-A},&A>1.\end{cases}
\]

## Assumptions and scope

Use the unitary short-time Fourier transform \(V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt\), with normalized window \(\|g\|_2=1\). The normalized Hermite functions \(h_n\), indexed by \(n\ge0\), form an orthonormal basis of \(L^2(\mathbb R)\). The domain is the centered open disk of Euclidean area \(A\); boundary conventions have no effect. All claims hold for every real \(A>0\), and no finite-dimensional truncation is assumed.

## Proof

**Hermite diagonalization.** The rotation invariance of the disk and the covariance of Hermite functions under the fractional Fourier rotation make \(L_A\) diagonal in the simple Hermite basis. The standard displaced-Hermite/Laguerre overlap identity, for \(r=\pi(x^2+\xi^2)\), gives
\[
|V_{h_1}h_0|^2=e^{-r}r,\qquad
|V_{h_1}h_n|^2=\frac{e^{-r}r^{n-1}}{n!}(n-r)^2\quad(n\ge1).
\]
The area element in the radial coordinate \(r\) is \(dr\). Consequently
\[
\lambda_0(A)=\int_0^A re^{-r}\,dr,
\qquad \lambda_n(A)=\frac1{n!}\int_0^A r^{n-1}(n-r)^2e^{-r}\,dr\quad(n\ge1).
\]
Each integrand is nonnegative and integrates to one over the half-line, so \(0<\lambda_n(A)<1\). Also \(\sum_n\lambda_n(A)=A\) by the STFT isometry/reproducing-kernel diagonal identity, so the operator is trace class.

**Exact adjacent gaps.** Integration of integer-shape gamma densities yields
\[
\lambda_0=1-e^{-A}(1+A),\quad
\lambda_n=1-e^{-A}Q_n(A),\quad
Q_n(A)=\sum_{j=0}^{n-1}\frac{A^j}{j!}+\frac{A^n(A-n+1)}{n!}\quad(n\ge1).
\]
Direct subtraction, including \(n=1\) when \(Q_0(A)=1+A\), gives the claimed factorization
\[
Q_n(A)-Q_{n-1}(A)=\frac{A^{n-1}}{n!}(A-n+1)(A-n).
\]
For \(m<A<m+1\), its factors have opposite signs exactly when \(n=m+1\). All other factors have the same sign; this proves the full nearest-neighbour ordering. At \(A=m\in\mathbb N\), the two factors vanish exactly for \(n=m\) and \(n=m+1\), proving the exact three-consecutive-level collision.

**Global optimization.** If \(0<A<1\), the sole upward step is \(\lambda_1>\lambda_0\), followed by strict decreases; hence \(h_1\) is the unique top Hermite direction. For \(A\ge1\), the only possible competitors to \(\lambda_0\) are \(\lambda_{m+1}\) when \(m<A<m+1\), or the plateau \(\lambda_{m-1}=\lambda_m=\lambda_{m+1}\) when \(A=m\) is integral. Their comparison is explicit: for every integer \(m\ge1\) and \(A\ge m\),
\[
Q_{m+1}(A)-Q_0(A)=\sum_{j=2}^{m}\frac{A^j}{j!}+\frac{A^{m+1}(A-m)}{(m+1)!}\ge0.
\]
Equality is possible only for \(m=A=1\). Thus \(\lambda_0\) strictly dominates the potential secondary peak whenever \(A>1\), whereas at \(A=1\), precisely \(\lambda_0=\lambda_1=\lambda_2=1-2/e\). Since \(\lambda_n\to0\) as \(n\to\infty\), no omitted high index can maximize. A positive diagonal operator has norm its largest eigenvalue, and the corresponding Hermite eigenspaces give all maximizers.

## Verification

The accompanying `CHECK.py` reconstructs the first fifteen radial integrals independently, confirms the factorization for the first 39 adjacent gaps symbolically, and checks ten disk areas by direct numerical quadrature against the exact formulas and the top-eigenspace transition. The proof above is infinite-dimensional and does not rely on finite testing. Reproduce with `python CHECK.py` using SymPy and SciPy.

## Relationship to prior work

Keller and Luef (2019 preprint, 2021 journal version) develop polyanalytic Fock quantization, the displaced-Hermite/Laguerre representation, and Hermite-window localization in a general operator-theoretic setting. Their results provide foundational identities, not the complete fixed-disk ordered Hermite spectrum or its triple-mode norm transition. Knutsen (2019 preprint, 2020 journal version) studies the Gaussian-window operator on annuli and infinite-measure periodic radial regions, not the first-excited-window centered disk. The precise comparison is of spectral conclusions rather than similar terminology.

## Limitations

This is a one-dimensional, first-excited-window, centered-disk result. It does not classify coincidences of nonadjacent lower eigenvalues, windows of higher Hermite order, noncircular masks, or inverse localization problems. Standard Laguerre overlap formulas and radial Hermite diagonalization are used as established background; the exact ordering, all integer triple adjacent collisions, and global transition follow from the displayed calculations. Earlier specialized computations of this exact case, if found, could affect historical priority.

## References

1. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (first public 19 May 2019), subsequently *Journal of Fourier Analysis and Applications* 27 (2021), article 47; DOI 10.1007/s00041-021-09843-0.
2. H. Knutsen, *Daubechies’ time–frequency localization operator on Cantor type sets I*, arXiv:1907.00848 (first public 1 July 2019), subsequently *Journal of Fourier Analysis and Applications* 26 (2020), article 47; DOI 10.1007/s00041-020-09751-9.
