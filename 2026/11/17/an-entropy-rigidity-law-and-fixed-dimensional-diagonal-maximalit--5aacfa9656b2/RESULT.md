# An entropy rigidity law and fixed-dimensional diagonal maximality for \(\ell_p\) hyperplane sections

## Finding
For each fixed integer \(n\ge2\), put \(m=n-1\), let \(B_p^n=\{x\in\mathbb R^n:\sum_{i=1}^n|x_i|^p\le1\}\), and write
\[
V_{n,p}(a)=\operatorname{vol}_m(B_p^n\cap a^\perp),\qquad a\in S^{n-1},\qquad \kappa_m=\frac{\pi^{m/2}}{\Gamma(1+m/2)}.
\]
Let \(d=(1,\ldots,1)/\sqrt n\), \(q_i(a)=1-a_i^2\), \(q_0=m/n\), and \(D(a)=\sum_{i=1}^n(a_i^2-1/n)^2\). Interpret \(0\log0=0\).

**Theorem (one coherent stability statement).** The normalized first-order deficit obeys, uniformly over all unit normals,
\[
\lim_{p\downarrow2}\sup_{a\in S^{n-1}}
\left|\frac{V_{n,p}(d)-V_{n,p}(a)}{\kappa_m(p-2)}
-\frac14\sum_{i=1}^nq_i(a)\log\frac{q_i(a)}{q_0}\right|=0.
\tag{1}
\]
The entropy term is at least \(D(a)/8\), with equality at zero only for \(|a_i|=1/\sqrt n\) for every coordinate. Moreover, for each fixed \(n\ge2\) there exists \(\delta_n>0\) such that for every \(2<p<2+\delta_n\) and every unit \(a\),
\[
\boxed{V_{n,p}(d)-V_{n,p}(a)\ge\frac{\kappa_m}{16}(p-2)D(a).}
\tag{2}
\]
Thus the diagonal-normal sections, up to coordinate signs, are the **only** volume-maximizing central hyperplane sections for all sufficiently small superquadratic exponents in any fixed dimension. No dimension-independent choice of \(\delta_n\) is asserted.

## Assumptions and scope
All bodies are real, finite-dimensional and centered; volumes use the intrinsic Euclidean measure in \(a^\perp\). Unit normals are identified up to sign. The interval \((2,2+\delta_n)\) depends on the fixed ambient dimension. The result concerns *central hyperplanes* and the unnormalized section volumes; comparisons in the same dimension and exponent also apply to any common normalization.

## Proof
**1. Exact polar formula and uniform first variation.** For \(u\in S^{m-1}(a^\perp)\) define \(g_p(u)=\sum_i|u_i|^p\). Polar coordinates within the section give
\[
V_{n,p}(a)=\frac1m\int_{S^{m-1}(a^\perp)}g_p(u)^{-m/p}\,d\sigma(u).
\tag{3}
\]
For \(p\) in a compact interval beginning at 2, \(g_p(u)\ge n^{1-p/2}>0\) uniformly in \(a,u\), and the functions \(|t|^p\log|t|\) are uniformly bounded for \(|t|\le1\). Consequently differentiation under the sphere integral is uniform over unit normals. As \(g_2(u)=1\),
\[
\left.\partial_p\frac{V_{n,p}(a)}{\kappa_m}\right|_{p=2}
=-\frac m2\,\mathbb E\sum_{i=1}^nU_i^2\log|U_i|,
\tag{4}
\]
where \(U\) is uniform on the Euclidean unit sphere of \(a^\perp\). This argument also applies when \(m=1\), with the uniform distribution on the two-point sphere.

**2. Computing the coordinate marginals.** Let \(q_i=\|\operatorname{Proj}_{a^\perp}e_i\|_2^2=1-a_i^2\). By rotation invariance within \(a^\perp\), \(U_i\) has the same distribution as \(\sqrt{q_i}\,Y\), where \(Y\) is the first coordinate of a uniform point of \(S^{m-1}\). Since \(\mathbb E Y^2=1/m\),
\[
\mathbb E(U_i^2\log|U_i|)=\frac{q_i}{m}\left(\frac12\log q_i+c_m\right),\qquad
c_m=\frac12\left[\psi(3/2)-\psi((m+2)/2)\right],
\tag{5}
\]
with continuity at \(q_i=0\); \(\psi\) denotes the digamma function. For \(m=1\), \(c_1=0\). Substitution into (4), using \(\sum q_i=m\), yields
\[
G(a):=\left.\partial_p\frac{V_{n,p}(a)}{\kappa_m}\right|_{2}
=-\frac14\sum_{i=1}^n q_i\log q_i-\frac m2c_m.
\tag{6}
\]
The uniform differentiability in Step 1 proves (1) by subtracting (6) at \(d\) and at \(a\).

**3. Strict entropy gap.** For \(h(x)=x\log x\), \(h''(x)=1/x\ge1\) on \((0,1]\). Its strong-convexity inequality, extended continuously to zero, gives
\[
\sum_{i=1}^n\big[h(q_i)-h(q_0)\big]
\ge h'(q_0)\sum_i(q_i-q_0)+\frac12\sum_i(q_i-q_0)^2
=\frac12D(a).
\tag{7}
\]
Thus \(G(d)-G(a)\ge D(a)/8\), with the vanishing set exactly the finite signed-diagonal orbit \(\mathcal D=\{a\in S^{n-1}:a_i^2=1/n\}\).

**4. Local second variation at the diagonal.** For any \(d'\in\mathcal D\) and tangent vector \(v\in T_{d'}S^{n-1}\), the coordinate variations along a sphere geodesic through \(d'\) satisfy \(q_i'(0)=-2d_i'v_i\) and \(\sum_iq_i(t)=m\). Differentiating (6) twice therefore gives
\[
\operatorname{Hess}_{S^{n-1}}G(d')[v,v]
=-\frac14\sum_i\frac{4(d_i')^2v_i^2}{q_0}
=-\frac{\|v\|^2}{m}.
\tag{8}
\]
For \(a=\cos t\,d'+\sin t\,v\) with unit tangent \(v\) and small \(t\), one also has
\[
D(a)=\frac4n t^2+O_n(t^3),\qquad
G(d')-G(a)=\frac{t^2}{2m}+O_n(t^3),
\tag{9}
\]
uniformly in the unit tangent direction.

We justify the requisite uniformity in \(p\) and \(a\) rather than assuming a pointwise asymptotic suffices. On a small neighborhood of \(d'\), choose a smooth orthonormal frame \(R(a):\mathbb R^m\to a^\perp\) and parameterize (3) over one fixed sphere. Each coordinate form \(z\mapsto[R(a)z]_i\) has coefficient norm \(\sqrt{q_i(a)}\ge c_n>0\). The derivatives in the frame coordinates through order two of \(|[R(a)z]_i|^p\), and their first \(p\)-derivatives, are dominated after integration by finite combinations of \(1+|\log|[R(a)z]_i||\) for \(p\in[2,2+\eta]\). These logarithms have uniformly bounded integrals because the coefficient norms stay bounded below; for \(m=1\) the coordinate forms are nonzero in this neighborhood. The positive lower bound for \(g_p\) controls its negative powers. Dominated convergence therefore shows
\[
H_p(a):=\frac{V_{n,p}(a)/\kappa_m-1}{p-2}\longrightarrow G(a)
\quad\text{in }C^2\text{ near every }d'\in\mathcal D.
\tag{10}
\]
Coordinate-sign and permutation symmetries make each \(d'\) stationary for \(H_p\) for all \(p\). By (8)–(10) and Taylor's theorem, the quotient
\[
\frac{H_p(d')-H_p(a)}{D(a)}
\tag{11}
\]
is bounded below by \(1/16\) for sufficiently small \(p-2>0\) and all \(a\ne d'\) in a sufficiently small fixed neighborhood of \(d'\); its joint limiting value at \((p,a)=(2,d')\) is \(n/[8(n-1)]>1/8\). There are finitely many such neighborhoods.

**5. Compactness away from diagonal normals.** On the compact complement of those neighborhoods, \(D(a)\) has a positive minimum. The uniform convergence in (1) together with (7) then gives \([H_p(d)-H_p(a)]/D(a)\ge1/16\) for sufficiently small \(p-2>0\). Combining this with Step 4 produces a common \(\delta_n>0\) and proves (2). Equality can hold only at \(D(a)=0\), and every signed diagonal gives equal volume by coordinate reflections.

## Verification
The standalone `VERIFY.py` executes deterministic direct-quadrature checks for planar central sections of three-dimensional \(\ell_p\) balls, compares their first exponent derivative against the closed digamma expression, checks the sharp entropy-convexity inequality on random normals in dimensions 2 through 20, and checks the local diagonal Hessian ratio. It passed **2,066** assertions. The infinite-dimensional-parameter quantifiers and the existence of \(\delta_n\) follow from Steps 1–5, **not** from finite numerical experiments. Reproduce with `python VERIFY.py` in an environment with NumPy and SciPy.

## Relationship to prior work
Koldobsky's classical result identifies the diagonal as minimizing section volume for \(1<p<2\), which implies a non-strict ordering of first derivatives at \(p=2\) but does not furnish the strict global superquadratic conclusion. König's 2024 open-access discussion explicitly raises strictness of that first-derivative ordering as a route to fixed-dimensional near-\(2\) maximality. Brazitikos and Eskenazis (2026) obtain an all-dimensional optimal threshold for \(p\ge p_0\) and an asymptotic-in-dimension comparison below it; neither statement implies the fixed-dimensional interval obtained here. The present result supplies the explicit strict entropy derivative and promotes it to a uniform directional quadratic gap in each fixed dimension. The finite threshold \(\delta_n\) is not quantified.

## Limitations
The interval size is existential and may shrink with dimension. Nothing is asserted about all exponents up to the conjectural global transition or about a dimension-independent neighborhood of 2. The statement is for real central hyperplane sections; analogous complex or higher-codimension sections require separate proof. The literature comparison is based on the named inspected sources and indexed searches, not exhaustive historical priority certification. Independent mathematical validation has not been performed.

## References
1. S. Brazitikos and A. Eskenazis, *The dimension-free threshold for maximal sections of \(\ell_p\)*, arXiv:2611.07619v1 (first public 2026-11-05), https://arxiv.org/html/2611.07619v1.
2. H. König, *On hyperplane sections and projections in \(\ell_p^n\)*, Banach Journal of Mathematical Analysis **18**, article 64 (2024), DOI:10.1007/s43037-024-00375-5, https://link.springer.com/article/10.1007/s43037-024-00375-5.
3. H. König, *On maximal hyperplane sections of the unit ball of \(\ell_p^n\) for \(p>2\)*, Advances in Operator Theory **10**, article 15 (2025; online 2024-11-21), DOI:10.1007/s43036-024-00404-y, https://link.springer.com/article/10.1007/s43036-024-00404-y.
4. A. Koldobsky, *An application of the Fourier transform to sections of star bodies*, Israel Journal of Mathematics **106** (1998), 157–164, as cited in König (2024).
