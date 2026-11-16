# Sharp polar-cap Slepian spectral floors and Gauss–Jacobi nodal collapse

## Finding
Fix a spherical-harmonic bandwidth \(L\in\mathbb Z_{\geq0}\). On the unit sphere with normalized area measure \(d\sigma=d\Omega/(4\pi)\), let \(V_L=\bigoplus_{\ell=0}^{L}\mathcal H_\ell(S^2;\mathbb C)\). For the northern polar cap \(C_h=\{(\theta,\phi):1-\cos\theta<h\}\) with \(0<h<2\), let \(T_{L,h}\) be the positive concentration operator defined by \(\langle T_{L,h}f,g\rangle=\int_{C_h}f\overline g\,d\sigma\). Its eigenvalues are strictly positive.

For each azimuthal order \(m\in\{0,1,\ldots,L\}\), let \(\lambda^{\mathrm{floor}}_{L,m}(h)\) denote the *smallest* concentration eigenvalue in the order-\(m\) sector (the \(-m\) sector has the same eigenvalues). Then, as \(h\downarrow0\) with \(L,m\) fixed,
\[
\boxed{\lambda^{\mathrm{floor}}_{L,m}(h)\sim C_{L,m}\,h^{2L-m+1}},\qquad
C_{L,m}=\frac{2^{m-2L-1}}{B(2L-m+1,m+1)(2L-m+1)\binom{2L-m}{L-m}^{2}}.
\]
Here \(B\) is Euler's beta function. In particular, the globally smallest eigenvalue is eventually simple and zonal, and
\[
\boxed{\lambda_{\min}(T_{L,h})\sim\frac{h^{2L+1}}{2^{2L+1}\binom{2L}{L}^{2}}.}
\]
The top concentration eigenvalue and the sharp spectral condition number satisfy
\[
\lambda_{\max}(T_{L,h})\sim\frac{(L+1)^2h}{2},\qquad
\boxed{\frac{\lambda_{\max}(T_{L,h})}{\lambda_{\min}(T_{L,h})}\sim (L+1)^2 2^{2L}\binom{2L}{L}^{2}h^{-2L}.}
\]

The least-concentrated order-\(m\) eigenmode has a radial polynomial of degree \(n=L-m\). For an eigenmode with radial polynomial \(p_h(t)\), write \(a_{n,h}=[t^n]p_h(t)\) and set \(\widetilde p_h(u)=p_h(hu)/(a_{n,h}h^n)\). This monic rescaled polynomial converges coefficientwise to the monic shifted Jacobi polynomial
\[
q_{n,m}(u)=\frac{P_n^{(0,m)}(2u-1)}{\binom{2n+m}{n}}.
\]
For all sufficiently small \(h\), its \(n\) zeros are simple and lie *inside* the cap; their scaled \(u\)-coordinates tend to the \(n\) zeros of \(q_{n,m}\) in \((0,1)\). For \(m=0\), these are shifted Gauss–Legendre nodes, yielding \(L\) interior nodal latitude circles of the unique global least-observable mode. When \(L=0\), the eigenvalue is exactly \(h/2\) and the nodal assertion is empty.

## Assumptions and scope
All limits are **fixed bandwidth** \(L\) and fixed azimuthal order \(m\), while cap area shrinks through \(h=1-\cos\Theta\downarrow0\). This is not a high-bandwidth or fixed-Shannon-number limit. The sphere is the unit two-sphere; angular harmonics are complex and the normalized energy ratio does not depend on choosing probability versus ordinary area measure. The nodal statement concerns the radial polynomial factor, or the latitude zeros away from the poles; the \(m>0\) angular factor already vanishes at the pole. No assertion of uniformity in growing \(L\) is made.

## Proof
**1. Exact Fourier-sector reduction.** Rotation invariance decomposes \(V_L\) into orders \(-L\le m\le L\). Put \(t=1-\cos\theta\). In a sector of absolute order \(m\), every element has the form \(e^{im\phi}[t(2-t)]^{m/2}p(t)\), where \(p\) ranges over all polynomials of degree at most \(n=L-m\). (The associated Legendre basis \(P_\ell^m\), \(m\le\ell\le L\), has precisely these polynomial factors.) Its full and cap squared norms, after angular integration, are
\[
Q_m(p)=\tfrac12\int_0^2 t^m(2-t)^m|p(t)|^2\,dt,
\qquad Q_{m,h}(p)=\tfrac12\int_0^h t^m(2-t)^m|p(t)|^2\,dt.
\]
Thus the sectoral minimum is the smallest generalized Rayleigh quotient \(Q_{m,h}/Q_m\). Every quotient is positive for \(h>0\) because a nonzero polynomial cannot vanish on an interval.

**2. Endpoint polynomial lemma (including the sharp constant).** Let \(n\ge0\), \(m\ge0\) be fixed and \(I_{n,m}=Q_m(t^n)\). Elementary beta integration gives
\[
I_{n,m}=2^{2(n+m)}B(2n+m+1,m+1).
\]
Use the competitor \(p_h(t)=h^n q(t/h)\) for an arbitrary monic degree-\(n\) polynomial \(q\). As \(h\downarrow0\), its full norm tends to \(I_{n,m}\) and its cap norm is
\[
Q_{m,h}(p_h)=2^{m-1}h^{2n+m+1}\Big(\int_0^1u^m|q(u)|^2\,du+O(h)\Big).
\]
The monic minimizer of the weighted integral is the shifted Jacobi polynomial \(q_{n,m}(u)=P_n^{(0,m)}(2u-1)/\binom{2n+m}{n}\), with the exact norm
\[
\int_0^1u^m|q_{n,m}(u)|^2\,du
=\frac{1}{(2n+m+1)\binom{2n+m}{n}^{2}}.
\]
This establishes the required upper asymptotic.

For the matching lower bound, normalize a true minimizing polynomial \(p_h\) by \(Q_m(p_h)=1\). The upper bound makes the rescaled polynomial \(r_h(u)=h^{-n}p_h(hu)\) bounded in \(L^2([0,1],u^mdu)\); finite-dimensional norm equivalence makes *every coefficient* of \(r_h\) bounded. Consequently, every coefficient of \(p_h\) below degree \(n\) tends to zero. Every convergent subsequence of \(r_h\) therefore has leading coefficient of modulus \(I_{n,m}^{-1/2}\), since the full norm equals one and \(p_h\) converges to its leading monomial. The weighted integral of any such limit is at least the Jacobi minimum above, forcing the lower bound. Uniqueness of the weighted monic minimizer implies, upon fixing the phase of the leading coefficient, coefficientwise convergence of \(r_h\) to \(I_{n,m}^{-1/2}q_{n,m}\). Inserting \(n=L-m\) gives exactly the displayed \(C_{L,m}\).

**3. Identification of the global minimum and nodal geometry.** The floors from step 2 have exponents \(2L-m+1\), which strictly decrease with \(m\). Because all coefficients are strictly positive and there are finitely many sectors for fixed \(L\), the global minimum eventually comes from \(m=0\). The zonal smallest eigenvalue is eventually simple: otherwise along a sequence \(h_j\downarrow0\) two orthogonal normalized minimizers would both converge, after phases, to the same normalized polynomial \(t^L\), contradicting orthogonality. The exact beta value at \(m=0\), \(B(2L+1,1)=(2L+1)^{-1}\), yields the stated central-binomial constant. Jacobi polynomial roots are simple and interior to \((0,1)\); coefficient convergence and continuity of simple roots give all \(n\) scaled zero limits and eventual interiority.

**4. Top eigenvalue and condition number.** In the finite-dimensional space \(V_L\), evaluation at the north pole has squared norm equal to the diagonal reproducing kernel \(K_L(N,N)=\sum_{\ell=0}^{L}(2\ell+1)=(L+1)^2\) when the underlying area measure is normalized. The positive operator \(T_{L,h}/(h/2)\) converges in operator norm to the rank-one evaluation projector \(K_N\otimes K_N\) as the cap shrinks. Thus its largest eigenvalue tends to \((L+1)^2\). Dividing by the floor from step 3 yields the condition-number constant. The case \(L=0\) is exact.

## Verification
The accompanying `cap_checker.py` computes exact moment formulas followed by high-precision generalized Hermitian eigenvalues. It checks all orders for \(0\le L\le5\), confirms the sharp sector constants and the maximum/condition-number limits at \(h=10^{-3}\), and checks the coefficientwise limit of the zonal eigenpolynomial on four interior points. After installing `requirements.txt`, executing `python cap_checker.py` produces `POLAR_CAP_FIXED_BAND_PASS`. These are finite corroborations; the proof above supplies the all-\(L\) assertion.

## Relationship to prior work
Simons, Dahlen and Wieczorek (arXiv:math/0408424, Sections 5 and 7) establish the spherical concentration problem, its azimuthal block structure, and a distinct joint limit where the cap shrinks **while bandwidth grows** with a fixed Shannon number. Michel, Plattner and Seibert (arXiv:2103.14650, Sections 3.2–3.3) treat scalar and spin-weighted spherical Slepian kernels and commuting operators. The present result is a fixed-bandwidth, small-cap statement about the *least* eigenvalue in every angular order, exact leading coefficients, and nodal collapse. Neither cited result states this limit. Gilbert and Slepian (1977) address concentrated polynomial eigenproblems and emphasize large-degree asymptotics; their full text was not inspected, so a more general equivalent treatment remains a priority risk. A published narrow-equatorial-belt hierarchy concerns a different shrinking region and does not itself imply the endpoint-weight Jacobi constants here.

## Limitations
The theorem is asymptotic for each fixed \(L\), with no effective uniform error estimate and no claim about the large-\(L\), fixed-area regime. The linear-algebra checker is finite, not an infinite proof. Literature priority is provisional where older full text was inaccessible, especially general polynomial concentration theory. The limit of the least eigenvector is specified up to a constant phase and normalization. The ill-conditioning concerns continuous cap energy observation, not discrete sensor placement or noisy inversion algorithms.

## References
1. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (public 2004-08-31), Sections 5 and 7; SIAM Review 48 (2006), 504–536.
2. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (public 2021-03-26), Sections 3.2–3.3.
3. E. N. Gilbert, D. Slepian, *Doubly Orthogonal Concentrated Polynomials*, SIAM Journal on Mathematical Analysis 8 (1977), 290–319, DOI:10.1137/0508022 (abstract inspected; full text not accessible).
4. L. Miranian, *Slepian functions on the sphere, generalized Gaussian quadrature rule*, Inverse Problems 20 (2004), 877–892, DOI:10.1088/0266-5611/20/3/014 (abstract inspected).
