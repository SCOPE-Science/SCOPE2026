# An exact positive cubic-gap defect for multiwindow hat-spline Gabor frames

## Finding
Fix an integer \(r\ge1\) and arbitrary real shifts \(s_1,\ldots,s_r\), with repetitions allowed. Put \(g(t)=(1-|t|)_+\), and use the union, with multiplicity, of \(\{M_nT_mT_{s_j}g:m,n\in\mathbb Z\}\) for \(j=1,\ldots,r\). Let \(A\) and \(B\) be its optimal frame bounds (with \(A=0\) if it is not a frame). Write \(y_1<\cdots<y_k<y_1+1\) for the \(k\) distinct residues of the shifts modulo one, in cyclic order, and define \(h_i=y_{i+1}-y_i>0\), where \(y_{k+1}=y_1+1\). Define the continuous circle potential
\[
F(x)=4\sum_{j=1}^{r}d_{\mathbb T}(x,s_j+\tfrac12)^2,
\qquad z_i=\tfrac12(y_i+y_{i+1}),
\]
where \(d_{\mathbb T}(u,v)=\min_{m\in\mathbb Z}|u-v-m|\). Then \(B=r\), \(A=\min_{x\in\mathbb R/\mathbb Z}F(x)\), and the system is a frame exactly when \(k\ge2\).

The following *exact two-term nonnegative defect identity* holds for every configuration, including repeated shifts:
\[
\boxed{\frac r3\Bigl(1-\frac1{k^2}\Bigr)-A
=\frac r3\sum_{i=1}^k\Bigl(h_i-\frac1k\Bigr)^2
                 \Bigl(h_i+\frac2k\Bigr)
+\sum_{i=1}^kh_i\bigl(F(z_i)-A\bigr).}
\]
Both summands are nonnegative. Equality holds **if and only if** the \(k\) residues are equally spaced and each has identical multiplicity \(r/k\), which requires \(k\mid r\). In particular, for \(k=r\),
\[
A\le\frac{r^2-1}{3r},\qquad
\frac{r^2-1}{3r}-A\ge
\frac r3\sum_{i=1}^{r}\bigl(h_i-\tfrac1r\bigr)^2
                             \bigl(h_i+\tfrac2r\bigr),
\]
with equality in the first bound exactly for a rotation of the equally spaced distinct shifts.

## Assumptions and scope
The window is the fixed unit-height centered triangular spline \(g\), not a general spline or a Gaussian. Both time and modulation lattices are exactly \(\mathbb Z\). All \(r\) channels use all integer shifts and all integer modulations; duplicated channels count separately. The optimal bounds are for the full coefficient analysis norm \(\sum_{j,m,n}|\langle f,M_nT_mT_{s_j}g\rangle|^2\) versus \(\|f\|_2^2\), for all \(f\in L^2(\mathbb R)\). No restriction to rational shifts is assumed. Circle distances and \(z_i\) are interpreted modulo one. The lower bound is allowed to be zero in the defective one-residue case.

## Proof
Use the unitary Zak transform \(Zf(x,\nu)=\sum_{m\in\mathbb Z}f(x+m)e^{-2\pi im\nu}\) on a unit fundamental square. Up to a unimodular factor from quasi-periodicity, the shifted triangular spline has
\[
Zg(u,\nu)=1-u+u e^{2\pi i\nu},\qquad 0\le u<1,
\]
so that
\[
|Zg(u,\nu)|^2=1-4u(1-u)\sin^2(\pi\nu).
\]
By the orthonormal Fourier-series fiber decomposition at the critical integer lattice, the frame operator of all \(r\) channels is multiplication by \(H(x,\nu)=\sum_{j=1}^{r}|Zg(x-s_j,\nu)|^2\). For each \(x\), its maximum over \(\nu\) is \(r\), attained at \(\nu=0\), and its minimum is at \(\nu=1/2\). Since \(1-4u(1-u)=(2u-1)^2=4d_{\mathbb T}(x,s_j+1/2)^2\), these are precisely \(B=r\) and \(A=\min_xF(x)\). The continuous nonnegative summands in \(F\) vanish simultaneously exactly when every shift has the same residue, giving the frame criterion.

Each point \(s_j\) is the unique nonsmooth location modulo one of its summand \(4d_{\mathbb T}(x,s_j+1/2)^2\). Thus on each *open gap* \((y_i,y_{i+1})\), the total potential is a quadratic with second derivative \(8r\). Its midpoint identity, obtained by integrating a quadratic, is
\[
\int_{y_i}^{y_{i+1}}F(x)\,dx=h_iF(z_i)+\frac r3h_i^3.
\]
Every individual squared circle distance integrates to \(1/12\), so \(\int_0^1F(x)dx=r/3\). Summing and subtracting the global minimum gives
\[
\frac r3-A=\sum_{i=1}^kh_i(F(z_i)-A)+\frac r3\sum_{i=1}^kh_i^3.
\]
The algebraic identity
\[
\sum_i h_i^3-\frac1{k^2}
=\sum_i\Bigl(h_i-\frac1k\Bigr)^2\Bigl(h_i+\frac2k\Bigr)
\]
follows from \(\sum_i h_i=1\) by expanding each term. This proves the exact claimed decomposition, including the strict positivity of its gap-irregularity term unless every gap equals \(1/k\).

For the full equality characterization, vanishing of the second term requires every gap midpoint to be a global minimizer. On each gap this forces \(F(x)=A+4r(x-z_i)^2\). Continuity at \(y_i\) forces \(h_{i-1}^2=h_i^2\) and hence all \(h_i=1/k\). If residue \(y_i\) has multiplicity \(m_i\), the left-to-right derivative jump there is \(-8m_i\), because each of those \(m_i\) terms is a squared circle distance. The gap expressions instead show that this jump is \(-4r(h_{i-1}+h_i)=-8r/k\). Therefore \(m_i=r/k\). Conversely equal gaps and equal multiplicities give a cyclically symmetric potential with global minima at all gap midpoints, so both nonnegative terms vanish. This also treats \(k=1\) (then \(F(z_1)=A=0\)).

## Verification
The standalone file `checker.py` uses exact rational arithmetic, exhaustive multisets on denominator grids \(4,6,8\) for each \(1\le r\le6\), and direct piecewise-quadratic minimization of \(F\). It verifies the frame criterion, upper bound, midpoint integration identity, cubic defect, and multiplicity-sensitive equality characterization. The run reports 4,134 checked designs, 143 equality designs and 324 distinct-site gap-deficit checks; this finite testing is a diagnostic, not the proof of claims for arbitrary real shifts. Replay by running `python3 checker.py` with the standard Python library.

## Relationship to prior work
The September 11, 2026 preprint by Hasannasab and Lemvig establishes Zak-zero and single-window Gabor-frame results for B-splines, including the triangular spline. The classical circle-polarization theorem of Hardin, Kendall and Saff establishes optimality of equally spaced sites for nonincreasing convex geodesic potentials; it **already implies** the equispaced-optimizer conclusion when all shifts are distinct. Thus **equispaced optimality is not presented as new**. The distinct contribution asserted here is the explicit *two-term exact nonnegative spectral-defect identity*, including arbitrary repeated shifts, a cubic quantified spacing penalty, midpoint slack and every equality stratum indexed by divisors of \(r\). Standard critical-lattice Zak diagonalization and previous multiwindow spline work explain the method but do not supply this specific joint identity in the sources inspected.

## Limitations
No other modulation lattice, unequal channel weights, general windows, or higher-dimensional grids are covered. The equal-spacing optimization is a known consequence of circle polarization; the new claim is specifically its exact quantitative decomposition and full multiplicity-sensitive equality law. An equivalent decomposition in older spline or circle-polarization literature may exist but was not located in the materials inspected. No independent mathematical review has been performed.

## References
1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, preprint first posted 2026-09-11, https://arxiv.org/abs/2609.13116.
2. D. P. Hardin, A. P. Kendall and E. B. Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, arXiv:1208.5261, https://arxiv.org/abs/1208.5261.
3. M. Faulhuber, *Gabor systems with Hermite functions of order N and oversampling greater than N+1 which are not frames*, 2025, https://doi.org/10.1007/s43670-025-00112-5 (for multiwindow Zak-frame methodology).
4. D. M. Onchis and S. Zappalà, *Approximate Duals of Gabor-like Frames Based on Realizable Multi-Window Spline-Type Constructions*, 2016, https://doi.org/10.1109/SYNASC.2016.027.
