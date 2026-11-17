# Pyramidal reduction and sharp reflection mixed-volume profiles of homothetic frusta

## Finding
Let \(d\ge2\), let \(B\subset\mathbb R^{d-1}\) be an arbitrary convex body with \((d-1)\)-dimensional volume \(A>0\), and let \(0\le r\le1\). Form the homothetic frustum
\[
F_r=\operatorname{conv}\bigl(B\times\{0\},\;rB\times\{1\}\bigr).
\]
For indices \(0\le j\le d-1\), define the lower-dimensional reflection mixed volumes
\[
M_j=V_{d-1}\bigl(B[d-1-j],(-B)[j]\bigr),\qquad M_0=M_{d-1}=A.
\]
For every \(1\le k\le d-1\), the **exact dimension-reduction identity** is
\[
\boxed{\frac{V_d(F_r[d-k],(-F_r)[k])}{\operatorname{vol}_d(F_r)}=
\frac{(1-r^{d-k})M_k+(1-r^k)M_{k-1}}{(1-r^d)A}}\quad (0\le r<1).
\tag{1}
\]
At the prism endpoint, the continuous limit is
\[
\boxed{\frac{V_d(F_1[d-k],(-F_1)[k])}{\operatorname{vol}_d(F_1)}=
\frac{(d-k)M_k+kM_{k-1}}{dA}.}
\tag{2}
\]
In particular, at the pyramid endpoint, equation (1) reduces to \((M_k+M_{k-1})/A\). For **every** such base and index, the normalized coefficient decreases strictly as \(r\) moves from zero to one.

The established Godbersen bound in dimension \(d-1\), together with (1), yields a **sharp extremal profile for all bases**:
\[
\boxed{\frac{V_d(F_r[d-k],(-F_r)[k])}{\operatorname{vol}_d(F_r)}\le
U_{d,k}(r):=
\frac{(1-r^{d-k})\binom{d-1}{k}+(1-r^k)\binom{d-1}{k-1}}{1-r^d}}
\tag{3}
\]
with endpoint interpreted by continuity. When \(d\ge3\), equality in (3) holds **if and only if** the base is a \((d-1)\)-simplex. For \(d=2\), every base is a line segment and hence a simplex. More precisely, the extremal deficit is the following *exact* weighted sum of the neighboring lower-dimensional deficits:
\[
U_{d,k}(r)-\frac{V_d(F_r[d-k],(-F_r)[k])}{\operatorname{vol}_d(F_r)}
=\frac{(1-r^{d-k})(\binom{d-1}{k}-M_k/A)+(1-r^k)(\binom{d-1}{k-1}-M_{k-1}/A)}{1-r^d}.
\tag{4}
\]
The sharp function \(U_{d,k}(r)\) for simplex bases coincides with a published truncated-simplex computation; the contribution here is the **arbitrary-base reduction, its global extremal characterization, and the strict shape-evolution law**.

## Assumptions and scope
A convex body is compact, convex, and full dimensional in its affine span. No symmetry, differentiability, or polytopality of \(B\) is assumed. Mixed volumes use the standard normalization
\[
\operatorname{vol}_m(X+sY)=\sum_{j=0}^{m}\binom mj V_m(X[m-j],Y[j])s^j,\qquad s\ge0.
\]
The scaling parameter is \(r\in[0,1]\); the endpoint \(r=0\) is a pyramid and \(r=1\) a prism. Height has been set to one by an invertible affine transformation; all normalized mixed-volume conclusions are affine invariant. The case \(d=2\) is included, with the stated equality characterization interpreted accordingly. Every index is an integer \(1\le k\le d-1\).

## Proof
**1. Translate the base and determine exact slices.** Choose any point \(c\in\operatorname{int}B\). The affine shear \((x,u)\mapsto (x-[1-(1-r)u]c,u)\) transforms \(F_r(B)\) into \(F_r(B-c)\). Accordingly we may assume \(0\in B\), so that \(\alpha B\subseteq\beta B\) for \(0\le\alpha\le\beta\). Put \(a=1-r\), and introduce an independent scalar \(s\ge0\). The horizontal sections of \(F_r\) at height \(v\in[0,1]\) equal \((1-av)B\), and the horizontal sections of \(s(-F_r)\) at height \(-sw\), \(w\in[0,1]\), equal \(s(1-aw)(-B)\).

A point at height \(u=v-sw\) in \(F_r+s(-F_r)\) can be written as the sum of points from these sections. If \(u\ge0\), then \(v=u+sw\), and both horizontal dilation factors decrease with \(w\). The largest such section is therefore obtained when \(w=0\), giving exactly \((1-au)B+s(-B)\). If \(u\le0\), then \(w=(v-u)/s\); both factors decrease with \(v\), and the largest section is achieved at \(v=0\), giving \(B+(s+au)(-B)\). Thus, including the evident limiting interpretation at \(s=0\),
\[
\operatorname{vol}_d(F_r+s(-F_r))
=\int_0^1\operatorname{vol}_{d-1}((1-au)B+s(-B))\,du
+\int_{-s}^0\operatorname{vol}_{d-1}(B+(s+au)(-B))\,du.
\tag{5}
\]
This is an exact slice decomposition, not a numerical approximation. It remains valid for every convex base, since it only uses nesting of homothetic copies.

**2. Extract every Minkowski coefficient.** Expand the first integrand using the lower-dimensional mixed-volume polynomial. The coefficient of \(s^k\) in the first integral is
\[
\binom{d-1}{k}M_k\int_0^1(1-au)^{d-1-k}\,du
=\binom{d-1}{k}M_k\frac{1-r^{d-k}}{a(d-k)}.
\tag{6}
\]
The second integral, with \(v=s+au\), equals \(a^{-1}\int_{rs}^{s}\operatorname{vol}_{d-1}(B+v(-B))\,dv\). Its coefficient of \(s^k\) is
\[
\binom{d-1}{k-1}M_{k-1}\frac{1-r^k}{ak}.
\tag{7}
\]
The binomial identities \(\binom{d-1}{k}/(d-k)=\binom dk/d\) and \(\binom{d-1}{k-1}/k=\binom dk/d\) therefore imply
\[
V_d(F_r[d-k],(-F_r)[k])
=\frac{(1-r^{d-k})M_k+(1-r^k)M_{k-1}}{d(1-r)}.
\tag{8}
\]
Also direct slicing gives \(\operatorname{vol}_d(F_r)=A(1-r^d)/[d(1-r)]\). Dividing (8) by this volume proves (1). The limits at \(r=1\) give (2). The endpoint \(r=0\) follows from (1) without a limiting argument. All coefficients are global since the Minkowski expansion is a polynomial in \(s\) for every \(s\ge0\).

**3. Prove strict monotonicity.** For each integer \(1\le p<d\), put
\[
f_p(r)=\frac{1-r^p}{1-r^d}.
\]
For \(0<r<1\) differentiation yields
\[
f_p'(r)=\frac{-r^{p-1}[p-dr^{d-p}+(d-p)r^d]}{(1-r^d)^2}<0.
\]
Indeed, \(H(r)=p-dr^{d-p}+(d-p)r^d\) satisfies \(H(1)=0\) and
\[
H'(r)=d(d-p)r^{d-p-1}(r^p-1)<0\qquad (0<r<1),
\]
so \(H(r)>0\) below one. Equation (1) expresses the normalized coefficient as \((M_k/A)f_{d-k}(r)+(M_{k-1}/A)f_k(r)\). The two mixed volumes are strictly positive for full-dimensional bodies, hence the coefficient is strictly decreasing on \((0,1)\) and, by endpoint continuity, on all of \([0,1]\).

**4. Sharpness, equality, and exact deficit.** The now-established Godbersen inequality in dimension \(d-1\) states
\[
M_j\le\binom{d-1}{j}A,\qquad 0\le j\le d-1.
\]
Substitution into the positive-weight combination (1) proves (3) and (4), including at \(r=1\) by continuity. A simplex satisfies equality simultaneously for every index. For \(d\ge3\), at least one of \(k-1\) and \(k\) is strictly between zero and \(d-1\), and both weights remain strictly positive at every \(r\in[0,1]\) (using their positive limits at one). The established equality theorem for Godbersen's inequality at an interior index then forces \(B\) to be a simplex. When \(d=2\), every one-dimensional convex body is itself a simplex. This completes the sharp equality classification.

## Verification
The standalone `verify.py` independently computes exact rational Minkowski coefficients from equation (5) by term-by-term integration, compares them to (8) for dimensions \(2\) through \(12\), all interior indices and rational frustum ratios, and checks the endpoint and monotonic expressions. It also compares the predicted full Minkowski polynomial with direct convex-hull volumes for triangular-base and square-base three-dimensional frusta, including both endpoint shapes. The analytic arguments above, rather than the finite tests, establish the theorem for every dimension and every convex base.

## Relationship to prior work
Fryš, Kotrbatý, Mouamine and Wang's 2026 work establishes the general Godbersen bound and higher-order extensions and characterizes its equality bodies; the present result uses that established theorem, rather than re-proving it. Friedland, Putterman and Szusterman independently clarify the equality case for every convex body. The previous exact *single-vertex truncated simplex* calculation determines precisely the sharp expression \(U_{d,k}(r)\) when \(B\) is a simplex; consequently, that expression **alone is not an originality claim**. It does not express the mixed volumes of a general frustum in terms of two mixed volumes of its arbitrary base, show that simplices uniquely maximize among all bases, or prove strict monotonicity for each fixed nonsimplex base.

A separate homothetic-frustum result computes the Santaló point and the volume product for every base; polar volume products are distinct from the reflection mixed-volume coefficients treated here. Search comparisons also considered pyramidal Godbersen inequalities, reflected cones, prismatoid Minkowski polynomials, and older anti-blocking-body mixed-volume results. An equivalent formula in unindexed classical mixed-volume literature remains a possible historical-priority risk.

## Limitations
The top and bottom sections must be homothetic about a common horizontal center, and the top scaling must satisfy \(0\le r\le1\). General prismatoids with unrelated bases, twisted sections, or reflection of a different convex body are outside the theorem. The sharp value for simplex bases and the global Godbersen inequality are earlier established results. This theorem gives neither a universal stability rate in Banach–Mazur distance nor an independently audited mathematical certificate. Originality is provisional pending historical review of older mixed-volume literature.

## References
1. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1 (5 October 2026), introduction and main equality theorems.
2. O. Friedland, E. Putterman and M. Szusterman, *The equality case in Godbersen's inequality and its generalizations*, arXiv:2610.04527v1 (3 October 2026).
3. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the L_p-Rogers–Shephard inequality*, arXiv:2607.20387 (2026).
4. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, published mathematical record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949.
5. *Universal Santaló and volume-product laws for homothetic frusta*, published mathematical record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359.
6. S. Artstein-Avidan, S. Sadovsky and R. Sanyal, *Geometric inequalities for anti-blocking bodies*, Communications in Contemporary Mathematics, DOI:10.1142/S0219199721501133 (2022).
