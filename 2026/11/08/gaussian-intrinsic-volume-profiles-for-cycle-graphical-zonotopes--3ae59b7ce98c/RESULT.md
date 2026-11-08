# Gaussian intrinsic-volume profiles for cycle graphical zonotopes

## Finding

Let \(n\ge3\), use cyclic indices \(e_{n+1}=e_1\), and equip the zero-sum hyperplane of \(\mathbb R^n\) with its inherited Euclidean metric. Define the standard cycle graphical zonotope
\[
Z_n=\sum_{i=1}^{n}[0,e_i-e_{i+1}],\qquad \dim Z_n=n-1.
\]
Its intrinsic volumes \(V_k(Z_n)\), normalized by the Steiner polynomial
\[
\operatorname{vol}_{n-1}(Z_n+sB)=\sum_{k=0}^{n-1}\kappa_{n-1-k}V_k(Z_n)s^{n-1-k},
\]
have the *exact* finite expansion
\[
V_k(Z_n)=\frac{n}{n-k}[z^n]\Big(\sum_{j\ge1}\sqrt j\,z^j\Big)^{n-k},\quad 0\le k<n.\tag{1}
\]
Here \([z^n]\) denotes coefficient extraction and \(\kappa_m\) is the volume of the \(m\)-dimensional unit ball.

For every fixed real \(t>0\), put
\[
W_n(t)=\sum_{k=0}^{n-1}V_k(Z_n)t^k,\quad
F(z)=\sum_{j\ge1}\sqrt j\,z^j=\operatorname{Li}_{-1/2}(z).
\]
There is a unique \(\rho=\rho(t)\in(0,1)\) with \(F(\rho)=t\). Define the probability distribution
\[
p_j=\frac{\sqrt j\,\rho^j}{t}\quad(j\ge1),\qquad
\mu=\sum_{j\ge1}jp_j,\quad \sigma^2=\sum_{j\ge1}(j-\mu)^2p_j,
\]
and constants \(\alpha(t)=1-1/\mu\) and \(\beta(t)=\sigma^2/\mu^3\). Then \(0<\alpha(t)<1\), \(\beta(t)>0\), and for some \(c_t\in(0,1)\),
\[
\boxed{W_n(t)=\big(t/\rho(t)\big)^n\big(1+O_t(c_t^n)\big).}\tag{2}
\]
If \(K_{n,t}\) is the intrinsic-volume index with
\[
\Pr(K_{n,t}=k)=\frac{V_k(Z_n)t^k}{W_n(t)},\qquad0\le k<n,
\]
then
\[
\boxed{\mathbb E K_{n,t}=n\alpha(t)+O_t(c_t^n),\quad
\operatorname{Var}(K_{n,t})=n\beta(t)+O_t(c_t^n),}\tag{3}
\]
and
\[
\boxed{\frac{K_{n,t}-n\alpha(t)}{\sqrt{n\beta(t)}}\ \Longrightarrow\ N(0,1)}\quad(n\to\infty).\tag{4}
\]
The error base \(c_t\) may be adjusted between displays. In particular, at \(t=1\),
\[
\rho=0.4385979757975646\ldots,\quad \alpha=0.5294005566860604\ldots,\quad
\beta=0.2113306362060691\ldots.
\]
Thus the unweighted sum of intrinsic volumes grows as \((2.279992282640062\ldots)^n\), while its index has asymptotically Gaussian fluctuations of order \(\sqrt n\) around \(0.52940056\ldots n\).

## Assumptions and scope

The theorem concerns the canonical *unscaled* edge-vector realization of the cycle graphical zonotope, in its intrinsic \((n-1)\)-dimensional Euclidean space. The weighting parameter \(t\) is fixed and strictly positive as \(n\to\infty\). Since intrinsic volumes have different physical degrees, specifying this realization and the weight \(t\) is necessary: arbitrary rescalings change the index law. No statement is made for a varying parameter \(t=t_n\), or for general graphical zonotopes.

## Proof

**1. Exact Gram determinants.** The established zonotope intrinsic-volume identity expresses \(V_k\) as the sum of norms of wedges of all independent \(k\)-tuples of generating vectors (Joós--Lángi, Corollary 1, also Brazitikos--McIntyre). Every proper subset of edges of \(C_n\) is a forest. For a forest consisting of path components of vertex sizes \(l_1,\ldots,l_m\), with isolated vertices included, its edge-incidence Gram determinant is
\[
\det(B_E^{\mathsf T}B_E)=\prod_{a=1}^{m}l_a.\tag{5}
\]
Indeed, the Gram matrix is block diagonal across components; the \((l-1)\)-edge oriented path block has determinant \(l\), by the tridiagonal determinant recurrence \(D_q=2D_{q-1}-D_{q-2}\), \(D_0=1\), \(D_1=2\). Hence the wedge norm is \(\sqrt{l_1\cdots l_m}\).

**2. Cyclic compositions.** Choosing \(k\) cycle edges leaves \(m=n-k\) deleted edges. The resulting components have \(m\) positive vertex sizes summing to \(n\). Counting each choice of a distinguished deleted edge gives \(m\) roots per forest; conversely, the first deleted edge can be chosen at any of \(n\) cyclic locations for each ordered positive composition. Therefore
\[
V_k=\frac n m\sum_{l_1+\cdots+l_m=n}\sqrt{l_1\cdots l_m},
\]
which is (1). This applies to all \(0\le k<n\); in particular \(V_0=1\) and \(V_{n-1}=n\sqrt n\).

**3. A renewal logarithm.** Summing (1) over \(k\) and replacing \(m=n-k\) gives the exact formal coefficient identity
\[
W_n(t)=-nt^n[z^n]\log\big(1-F(z)/t\big).\tag{6}
\]
For any fixed positive \(t\), the function \(F\) is analytic on \(|z|<1\), strictly increasing from zero to infinity along \((0,1)\), and its positive solution \(\rho(t)\) to \(F(\rho)=t\) is simple. By strict positivity of every coefficient, the triangle inequality shows that no other zero of \(1-F(z)/t\) has modulus at most \(\rho\): equality at \(|z|=\rho\) would require the first two consecutive nonzero powers of \(z\) to have the same phase, forcing \(z=\rho\). Thus for some \(R_t\in(\rho,1)\) there is no other zero in \(|z|\le R_t\).

For complex \(u\) in a small neighborhood of zero, the implicit-function theorem provides a unique analytic root \(\rho(te^u)\) near \(\rho(t)\). The difference
\[
-\log\big(1-F(z)/(te^u)\big)+\log\big(1-z/\rho(te^u)\big)
\]
is analytic and uniformly bounded on a disk of radius strictly greater than \(|\rho(te^u)|\), because the two logarithmic singularities cancel and the remaining factor is nonzero there. Cauchy's estimate for its \(n\)-th Taylor coefficient yields, uniformly for such \(u\),
\[
W_n(te^u)=\big(te^u/\rho(te^u)\big)^n(1+O(c^n))\tag{7}
\]
for a fixed \(c<1\). At \(u=0\) this proves (2).

**4. Limit law.** The moment-generating function of \(K_{n,t}\) is \(W_n(te^u)/W_n(t)\). Equation (7) gives an analytic uniform expansion
\[
\log\mathbb E(e^{uK_{n,t}})=n\Lambda_t(u)+O(c^n),\qquad
\Lambda_t(u)=u-\log\rho(te^u)+\log\rho(t).\tag{8}
\]
Differentiating \(F(\rho(te^u))=te^u\), and writing \(\mu=\rho F'(\rho)/F(\rho)\), gives
\[
\frac{d\log\rho(te^u)}{du}=\frac1{\mu(te^u)}.
\]
The distribution \(p_j\) is an exponential family in \(\log\rho\), so \(d\mu/d\log\rho=\sigma^2\). Consequently \(\Lambda'_t(0)=1-1/\mu=\alpha(t)\) and \(\Lambda''_t(0)=\sigma^2/\mu^3=\beta(t)\). Since \(p_1,p_2>0\), its mean is greater than one and its variance is strictly positive. Analytic differentiation of (8) proves the two moment assertions (3). Inserting \(u=is/\sqrt{n\beta(t)}\) in (8), subtracting the linear phase and expanding the analytic \(\Lambda_t\) to second order gives the characteristic function \(e^{-s^2/2}+o(1)\); the continuity theorem proves (4). No numerical experiment is used to prove the limit.

## Verification

The standalone `verify_intrinsic.py` independently constructs incidence Gram matrices and checks their integer determinants against path-component products for all proper edge subsets of cycles of orders \(3\) through \(11\); it also compares the independent forest sum against (1). In addition, it evaluates full coefficient arrays through order \(150\) and checks their normalized growth, means, variances, and normal-CDF approximations against (2)--(4). There are \(4160\) finite determinant/component and comparison assertions, with all checks passing. The printed numerical root and fluctuation constants agree with independently evaluated polylogarithms. This is corroboration, not a proof of the arbitrary-order or asymptotic claims.

## Relationship to prior work

Ross Glew's 2026 in-in-zonotope construction identifies graphical zonotopes as natural Minkowski summands and boundary factors. It does not derive an intrinsic-volume index limit law for graph cycles. Joós and Lángi's 2022/2023 zonotope theorem, independently related to the Brazitikos--McIntyre formula, supplies the known wedge-volume identity used in Step 1; neither this identity nor the ordinary volume \(V_{n-1}=n\sqrt n\) is claimed new. Padrol, Pilaud, and Poullot study deformations, normal fans, and facets of graphical zonotopes, not an all-dimensional Gaussian intrinsic-volume profile. The claimed addition is the cyclic-composition reduction, exact renewal generating identity, uniform singularity analysis, and the resulting explicit one-parameter Gaussian concentration law.

## Limitations

Originality is assessed relative to the accessible literature and mathematical-record searches, not certified independently. An unindexed graph-zonotope or renewal-theory specialization could cover the Gaussian conclusion. Constants depend on the canonical Euclidean realization and fixed positive \(t\); the theorem does not establish uniformity as \(t\) tends to zero or infinity. It makes no assertion about the intrinsic volumes of the larger in-in zonotope itself.

## References

1. R. Glew, *Geometry of in-in correlators*, arXiv:2601.18903, first public January 26, 2026; especially Sections III and VI.
2. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204 (2022), Mathematika 69 (2023), 508–534; Corollary 1 and Theorem 3.
3. S. Brazitikos and F. McIntyre, intrinsic-volume wedge formulas for zonotopes, as cited in Joós--Lángi, Sections 1–2.
4. A. Padrol, V. Pilaud, and G. Poullot, *Deformed Graphical Zonotopes*, Discrete & Computational Geometry 73 (2025), 447–465; first online 2023, DOI:10.1007/s00454-023-00586-x.
5. M. Lotz, M. McCoy, I. Nourdin, G. Peccati, and J. Tropp, *Concentration of the intrinsic volumes of a convex body*, arXiv:1810.12412 (2018); general motivation for intrinsic-volume index statistics, not a cycle-specific limit theorem.
