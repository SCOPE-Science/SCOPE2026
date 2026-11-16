# Thin equatorial Slepian belts: a central-binomial observability law and Gauss–Legendre nodal limit

## Finding
Let \(L\geq0\) be a fixed integer. Let \(V_L=\bigoplus_{\ell=0}^{L}\mathcal H_\ell(S^2)\) be the complex spherical-harmonic space of all degrees at most \(L\). For \(0<a<1\), define the equatorial belt \(B_a=\{(x,y,z)\in S^2:|z|<a\}\) and its minimum concentration ratio
\[
\lambda_L(a)=\min_{0\neq f\in V_L}\frac{\int_{B_a}|f|^2\,d\Omega}{\int_{S^2}|f|^2\,d\Omega}.
\]
Then, with \(\kappa_L=2^{-L}\binom{2L}{L}\),
\[
\boxed{\lim_{a\downarrow0}\frac{\lambda_L(a)}{a^{2L+1}}=\kappa_L^{-2}=\left(\frac{2^L}{\binom{2L}{L}}\right)^2.}
\]
For each fixed \(L\geq1\), the minimizing eigenspace is one-dimensional and zonal for all sufficiently small \(a>0\). Choose its real polynomial representative \(p_{L,a}(z)\) with positive leading coefficient, and write \(q_{L,a}(t)=p_{L,a}(at)/(a^Lc_{L,a})\), where \(c_{L,a}\) is the coefficient of \(z^L\) in \(p_{L,a}\). Then \(q_{L,a}\) is monic and converges coefficientwise to the monic Legendre polynomial \(P_L(t)/\kappa_L\). In particular, the \(L\) simple zeros of the minimizing zonal function lie in the belt and, after division of their \(z\)-coordinates by \(a\), converge to the Gauss–Legendre nodes. For \(L=0\), \(\lambda_0(a)=a\) exactly.

For example, \(\lambda_2(a)\sim(4/9)a^5\), and the two limiting scaled zero coordinates are \(\pm1/\sqrt3\). The result concerns the least eigenvalue of the finite-band *continuum* concentration operator, not discrete sampling or the large-bandwidth limit.

## Assumptions and scope
The sphere carries its standard surface-area measure \(d\Omega\); scaling the whole measure does not affect Rayleigh quotients. The band contains all longitudes and is centered on the equator. The degree cutoff \(L\) is fixed before \(a\to0\). Complex as well as real spherical-harmonic combinations are allowed. All spherical-harmonic degrees \(0,\ldots,L\) are present; the same formula does not automatically apply to an isolated homogeneous degree or a degree mask missing lower levels.

## Proof
**1. Azimuthal decomposition.** Axisymmetry makes different spherical azimuthal orders orthogonal both on \(B_a\) and on \(S^2\). For order \(m\) with \(|m|\le L\), write \(n=L-|m|\). The order-\(m\) subspace, after removing \(e^{im\phi}\), consists exactly of
\[
(1-z^2)^{|m|/2}p(z),\qquad \deg p\le n.
\]
Thus its least concentration eigenvalue is
\[
\mu_{n,|m|}(a)=\inf_{0\neq p\in\mathbb C[z]_{\le n}}
\frac{\int_{-a}^a|p(z)|^2(1-z^2)^{|m|}\,dz}
{\int_{-1}^1|p(z)|^2(1-z^2)^{|m|}\,dz}.
\]
The full least eigenvalue is the minimum of these finitely many blockwise minima. No comparison between the two azimuthal signs is required, since their eigenvalues coincide.

**2. Shrinking-interval polynomial lemma.** For each fixed pair of nonnegative integers \(n,m\), let \(w(z)=(1-z^2)^m\) and \(J_{n,m}=\int_{-1}^1z^{2n}w(z)\,dz>0\). The exact asymptotic is
\[
\mu_{n,m}(a)\sim C_{n,m}a^{2n+1},\qquad
C_{n,m}=\frac{2}{(2n+1)\kappa_n^2J_{n,m}},
\quad \kappa_n=2^{-n}\binom{2n}{n}.
\]
To prove the upper bound, take the monic Legendre polynomial \(Q_n=P_n/\kappa_n\) and the trial polynomial \(p_a(z)=a^nQ_n(z/a)\). Its denominator tends to \(J_{n,m}\) and its numerator divided by \(a^{2n+1}\) tends to
\(\int_{-1}^1|Q_n(t)|^2\,dt=2/((2n+1)\kappa_n^2)\).

For the matching lower bound, take minimizers normalized by \(\int_{-1}^1|p_a|^2w=1\), and write \(p_a(z)=\sum_{j=0}^nc_j(a)z^j\). The upper bound makes the numerator \(O(a^{2n+1})\). Because \(w\) is bounded below on small centered intervals, equivalence of the Euclidean coefficient norm and \(L^2([-1,1])\) polynomial norm applied to \(p_a(at)\) gives
\[
|c_j(a)|=O(a^{n-j})\quad(0\le j\le n).
\]
Normalization therefore forces \(|c_n(a)|\to J_{n,m}^{-1/2}\), while all lower coefficients tend to zero. Divide by \(c_n(a)a^n\): the rescaled polynomials \(p_a(at)/(c_n(a)a^n)\) are monic and have bounded coefficients. Each limit point \(Q\) is monic. Along any convergent subsequence, the Rayleigh quotient divided by \(a^{2n+1}\) tends to \(\int_{-1}^1|Q|^2/J_{n,m}\). The unique monic minimizer of this integral, even among complex polynomials, is \(Q_n\), by Legendre orthogonality. This identifies both the liminf and every coefficient limit, proving the lemma and the scaled-shape convergence.

**3. Competition between azimuthal sectors.** For order \(m\ne0\), the lemma gives a positive multiple of \(a^{2(L-|m|)+1}\); this dominates the zonal order-\(0\) value of order \(a^{2L+1}\) as \(a\downarrow0\). In the zonal sector, \(J_{L,0}=2/(2L+1)\), so \(C_{L,0}=\kappa_L^{-2}\), establishing the boxed limit.

**4. Eventual simplicity and nodes.** For \(L\ge1\), the second-smallest eigenvalue in the zonal polynomial sector is at least the minimum Rayleigh quotient restricted to its codimension-one subspace of polynomials of degree at most \(L-1\), by Courant–Fischer. That minimum is a positive multiple of \(a^{2L-1}\), hence eventually strictly larger than the zonal least eigenvalue. The nonzonal sectors are also separated by the previous power comparison. Thus the global least eigenvalue is eventually simple, with a real zonal minimizer. The polynomial lemma applied to this minimizer gives \(q_{L,a}\to Q_L\). Because the \(L\) zeros of \(P_L\) are real, distinct and in \((-1,1)\), real-root continuity gives exactly \(L\) simple roots of \(p_{L,a}\) inside \((-a,a)\) for sufficiently small \(a\), with the asserted scaled limits.

## Verification
Run `python checker.py` using Python 3 and `mpmath`. The checker uses the exact finite polynomial moment formula
\[
\int_{-a}^a z^{2j}(1-z^2)^m\,dz=
2\sum_{r=0}^{m}(-1)^r\binom mr\frac{a^{2j+2r+1}}{2j+2r+1}
\]
and high-precision generalized Hermitian eigenvalue calculations. It tests \(L=1,\ldots,5\) at three belt widths, confirms that the zonal block minimizes, and checks convergence to the claimed constant. These finite numerical tests do not establish the all-degree limit; the preceding polynomial lemma does.

## Relationship to prior work
Spherical Slepian theory and the symmetric polar-gap/equatorial-belt eigenproblem were developed by Simons and Dahlen (2006), and the approach was used for latitude-restricted Jovian gravity estimation by Parisi and collaborators (2020). The geometric concentration operator, its azimuthal decomposition and numerical computation are **not** claimed to be new. The present result is the fixed-band, vanishing-belt sharp least-eigenvalue asymptotic, including its central-binomial constant, eventual unique azimuthal order, and Gauss–Legendre nodal scaling. The standard Legendre leading-coefficient formula and polynomial norm minimization are used openly. The older works consulted present the belt eigenproblem and numerical solutions rather than this explicit asymptotic. Historical priority remains subject to equivalent specialized small-interval polynomial concentration results.

## Limitations
The constant depends on retaining the entire harmonic cutoff \(0\le\ell\le L\) and on the centered equatorial belt. It is not uniform when \(L\) grows with inverse belt width, and gives no explicit error rate or finite-width threshold for simplicity. It is a continuum stability law and does not by itself control finite sampling or noisy inversion in a geophysical model. No independent mathematical audit has been performed.

## References
- F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International 166 (2006), 1039–1061. First arXiv version: https://arxiv.org/abs/math/0603271 ; DOI: https://doi.org/10.1111/j.1365-246X.2006.03065.x .
- M. Parisi, E. Galanti, W. M. Folkner, Y. Kaspi, D. R. Buccino, *Resolving the Latitudinal Short-Scale Gravity Field of Jupiter Using Slepian Functions*, Journal of Geophysical Research: Planets 125 (2020), e2020JE006416. https://doi.org/10.1029/2020JE006416 ; first public article 2020-09-30.
- NIST Digital Library of Mathematical Functions, Section 14.30, spherical harmonics, https://dlmf.nist.gov/14.30 .
