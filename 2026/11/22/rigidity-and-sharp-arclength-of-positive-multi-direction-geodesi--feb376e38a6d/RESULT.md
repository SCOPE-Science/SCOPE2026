# Rigidity and sharp arclength of positive multi-direction geodesic Fourier designs on the flat torus

## Finding
Fix an integer \(N\ge1\) and the square frequency band \(\mathcal F_N\) on the flat torus \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\). For every finite positive-weighted family of complete primitive closed geodesics, possibly containing several different directions, exact preservation of the \(L^2\) energy is **equivalent to exactness in every direction separately**. In particular, no mixture of directions can improve the minimum acquisition length: if there are \(J\) distinct unoriented primitive directions, its total trajectory arclength satisfies
\[
\mathcal L\ge 2\pi J(2N+1).
\]
The bound is attained for \(J=1\) and \(J=2\), using respectively one or both coordinate directions, and is strict for \(J\ge3\). The absolute minimum at \(J=1\) is attained precisely by \(2N+1\) parallel coordinate circles with equal weights and equally spaced offsets. The new assertion is the multi-direction factorization, universal arclength bound and global equality classification; the previously known one-direction equal-weight calculation is not reasserted as new.

## Assumptions and scope
Let \(\mathcal F_N=\operatorname{span}_{\mathbb C}\{e_k(x)=e^{i k\cdot x}: k\in\{-N,\ldots,N\}^2\}\), equipped with normalized Haar measure. Every measurement loop is \(\gamma_{v,a}(s)=a+sv\pmod{2\pi}\) for \(0\le s\le2\pi\), with \(v=(p,q)\in\mathbb Z^2\) primitive, i.e. \(\gcd(|p|,|q|)=1\), and \(a\in\mathbb T^2\). Its length is \(2\pi\sqrt{p^2+q^2}\). Opposite signs of \(v\) represent the same direction. Let \(w_j>0\) be independent component weights with \(\sum_jw_j=1\). The observation quadratic form is
\[
Q(f)=\sum_j w_j\frac{1}{2\pi}\int_0^{2\pi}|f(a_j+s v_j)|^2\,ds.
\]
For each unoriented slope class \(v=(p,q)\), put \(m_v=\max(|p|,|q|)\), \(T_v=\lfloor 2N/m_v\rfloor\), \(\eta_{v,j}=q a_{j,1}-p a_{j,2}\pmod{2\pi}\), \(W_v=\sum_{j:v_j\sim v} w_j\), and \(L_v\) equal to the number of its loops. Repeated identical offset circles may be combined for phase tests, but their physical lengths still count separately.

The exact criterion is
\[
Q(f)=\|f\|_{L^2(\mathbb T^2)}^2\ \ \forall f\in\mathcal F_N
\quad\Longleftrightarrow\quad
\sum_{j:v_j\sim v}w_j e^{it\eta_{v,j}}=0\quad\forall v,\ 1\le t\le T_v.
\]
There is no condition when \(T_v=0\). If \(L_v=T_v+1\), all phases are an equally spaced translate of the \(L_v\)-th roots of unity and the weights inside the direction are \(W_v/L_v\).

## Proof
**1. Exact Fourier coefficient of one loop.** For every integer vector \(h\in\mathbb Z^2\),
\[
\frac1{2\pi}\int_0^{2\pi}e^{ih\cdot(a+sv)}\,ds=\mathbf1_{h\cdot v=0}\,e^{ih\cdot a}.
\]
By polarization, \(Q\) is the Haar norm on \(\mathcal F_N\) precisely when all off-diagonal Fourier Gram entries vanish. Every nonzero difference \(h=k-k'\) belongs to \([-2N,2N]^2\cap\mathbb Z^2\), and conversely every vector in this difference box is such a difference.

**2. Different directions never cancel.** Any nonzero integer \(h\) is perpendicular to at most one unoriented primitive integer direction. If \(h\cdot(p,q)=0\), primitiveness forces \(h=t(q,-p)\) for a nonzero integer \(t\). Such a difference lies in the box exactly when \(|t|m_v\le 2N\). Hence its only possibly nonzero directional contribution to the global Gram entry is \(\sum_{j:v_j\sim v}w_j e^{it\eta_{v,j}}\). This proves the full necessary-and-sufficient separate Fourier-moment criterion, including both signs via complex conjugation.

**3. Positive moment rank and equality.** Normalize the weights inside one direction by \(W_v\). Under the criterion, the \((T_v+1)\times(T_v+1)\) Toeplitz matrix
\[
C_{rs}=\sum_{j:v_j\sim v}\frac{w_j}{W_v}e^{i(r-s)\eta_{v,j}},\qquad 0\le r,s\le T_v,
\]
is the identity. It is a sum of \(L_v\) rank-one matrices, so \(L_v\ge T_v+1\). If equality holds, the square matrix whose \(j\)-th column is \(\sqrt{w_j/W_v}(1,e^{i\eta_{v,j}},\ldots,e^{iT_v\eta_{v,j}})^\top\) is unitary. Equal column lengths give \(w_j/W_v=1/(T_v+1)\); orthogonality of distinct columns gives \(\sum_{r=0}^{T_v}e^{ir(\eta_i-\eta_j)}=0\), forcing all phase differences to be nontrivial \((T_v+1)\)-st roots of unity. The minimal phase set is therefore a regular root polygon. Conversely such a polygon gives zero moments through order \(T_v\). This argument includes \(T_v=0\), in which case one loop is sufficient and phases are unrestricted.

**4. Physical length and sharpness.** For each direction,
\[
\frac{\mathcal L_v}{2\pi}=L_v\sqrt{p^2+q^2}
\ge (T_v+1)m_v\ge 2N+1.
\]
The last step holds because \((\lfloor2N/m_v\rfloor+1)m_v\) is an integer strictly greater than \(2N\). Equality requires \(\sqrt{p^2+q^2}=m_v\), hence one coordinate is zero and primitiveness gives \(m_v=1\); it also forces \(L_v=2N+1\). Then step 3 forces equal weights and equally spaced transverse offsets. Summing over the \(J\) direction classes yields \(\mathcal L\ge2\pi J(2N+1)\); for \(J=1\) the regular coordinate-loop design attains equality. For \(J=2\), the direction-wise lower bounds are jointly attained by employing both coordinate directions, each in its own equally spaced \(2N+1\)-loop family with equal weights within that family and arbitrary positive total weight. For \(J\ge3\), the summed bound is strict because only two distinct coordinate directions can achieve directional equality. Since every additional direction costs positive arclength, the absolute global minimum is attained only for one coordinate direction. For arbitrary choices of directions, the independent regular root polygons provide sharp component-count examples, showing sufficiency of the criteria and impossibility of cross-direction savings.

## Verification
The proof is infinite and does not depend on the finite checks. The standalone `CHECKER.py` evaluates the exact loop Fourier integrals and tests complete Fourier Gram matrices for \(N=1,2,3\), eight primitive directions, and their positive mixtures. Its 51 Gram examples have maximum floating deviation below \(4\times10^{-16}\). It separately checks the integer-geometric arclength inequality and every equality case for \(1\le N\le49\) across primitive directions in a finite search box. Run `python CHECKER.py` from a directory containing the extracted script. These tests corroborate, but are not substitutes for, steps 1–4.

## Relationship to prior work
Rashkovskii–Ulanovskii–Zlotnikov (2020) study mobile sampling along families of *Euclidean planar* curves for Bernstein and Paley–Wiener spaces; their parallel-line criteria do not give the compact torus *exact Parseval* criterion or the independent-direction no-cancellation theorem. Ehler–Gröchenig (2023) establish general spherical t-design curves and mobile sampling on spheres, including configurations formed from circles, but not this flat-torus direction factorization. Kunis (2026) and Ehler (2026) study positive quadrature and lengths of *closed design curves on tori*, including Korobov-type paths; their publicly accessible abstracts do not claim this classification for arbitrary finite, independently positively weighted mixtures of geodesic components. Their complete text was not available for a decisive appendix-level comparison. A pre-existing analysis of **parallel equal-weight primitive loops** provides the one-direction threshold and its restricted minimum. That result alone does not imply the cross-direction factorization or unrestricted geodesic-mixture optimum.

## Limitations
The class is **finite** mixtures of **complete** primitive closed geodesics. The positivity of weights is assumed; relative weights between direction classes need not track physical arclength. The measurement functional concerns normalized \(L^2\) energy on a finite square Fourier band, not sampling at finitely many points, nor stable but non-tight frames. This result does not give the minimum for arbitrary curved or connected acquisition paths; it excludes travel between distinct loops and does not address conditioning away from exact Parseval. Historical priority remains uncertain because some highly relevant 2026 full texts were unavailable; an implicit earlier formulation is possible.

## References
1. A. Rashkovskii, A. Ulanovskii, I. Zlotnikov, *On 2-dimensional mobile sampling*, arXiv:2005.11193 (first public 2020-05-22), https://arxiv.org/html/2005.11193v1.
2. M. Ehler, K. Gröchenig, *t-design curves and mobile sampling on the sphere*, arXiv:2306.13152 (first public 2023-06-19), https://doi.org/10.1017/fms.2023.106.
3. S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915 (first public 2026-08-12), https://arxiv.org/abs/2608.11915.
4. M. Ehler, *Optimal bounds for design curves on the torus*, arXiv:2611.03362 (first public 2026-11-02), https://arxiv.org/abs/2611.03362.
