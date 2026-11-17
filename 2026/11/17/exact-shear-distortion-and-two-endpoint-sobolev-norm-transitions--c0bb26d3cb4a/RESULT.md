# Exact shear distortion and two endpoint-Sobolev norm transitions

## Finding

For an integer \(k\geq 1\) equip the real Sobolev space \(W^{k,1}(\mathbb R^2)\) with the **unweighted, complete derivative-sum norm**
\[
N_k(f)=\sum_{j=0}^{k}\sum_{s=0}^{j}
\bigl\|\partial_x^{j-s}\partial_y^{s}f\bigr\|_{L^1(\mathbb R^2)}.
\]
For every real \(t\), let \((U_tf)(x,y)=f(x+ty,y)\). Then \(U_t\) is bounded and invertible, and its **exact operator norm at every order** is
\[
\boxed{\|U_t\|_{W^{k,1}\to W^{k,1}}=
\max_{0\leq s\leq k}\sum_{i=s}^{k}{i\choose s}|t|^{i-s}.}
\]
The inverse is \(U_{-t}\), with the same norm. For \(t\ne0\) this supremum is not attained by any nonzero Sobolev function; for \(t=0\) the operator is the identity.

Writing \(q=|t|\), the first nontrivial orders admit the complete phase diagrams
\[
\|U_t\|_{W^{2,1}}=
\begin{cases}
1+2q,&0\leq q\leq1,\\
1+q+q^2,&q\geq1,
\end{cases}
\]
and
\[
\|U_t\|_{W^{3,1}}=
\begin{cases}
1+3q,&0\leq q\leq\frac13,\\
1+2q+3q^2,&\frac13\leq q\leq1+\sqrt2,\\
1+q+q^2+q^3,&q\geq1+\sqrt2.
\end{cases}
\]
For positive shear magnitude the order-three norm has exactly two differentiability cusps, at \(q=1/3\) and \(q=1+\sqrt2\). The order-two norm has a cusp at \(q=1\). In the small-shear regimes the dominant top derivative is mixed; for sufficiently large shear it is the pure horizontal derivative.

## Assumptions and scope

The domain is all of \(\mathbb R^2\) with Lebesgue measure; derivatives are weak partial derivatives and are each counted once, without multinomial weights. Functions are real-valued. The integer \(k\) is at least one, and \(t\) is arbitrary real. The formula is specific to this coordinate-dependent Sobolev norm and to the volume-preserving triangular shear; no assertion is made for Euclidean-tensor derivative norms, arbitrary domains, or nonlinear maps.

## Proof

**1. Chain-rule upper bound.** Set \(u=x+ty\), \(v=y\), so \(\partial_x=\partial_u\), \(\partial_y=t\partial_u+\partial_v\), and the Jacobian equals one. At any order \(0\leq j\leq k\), and for \(0\leq i\leq j\), the repeated chain rule yields
\[
\partial_x^{j-i}\partial_y^i(U_tf)
=\sum_{s=0}^{i}{i\choose s}t^{i-s}
\bigl(\partial_u^{j-s}\partial_v^sf\bigr)\circ(x+ty,y).
\]
Consequently, if \(N_j^{\mathrm{hom}}(f)=\sum_{s=0}^j\|\partial_x^{j-s}\partial_y^sf\|_1\) and
\[
P_{j,s}(q)=\sum_{i=s}^{j}{i\choose s}q^{i-s},\qquad
M_j(q)=\max_{0\leq s\leq j}P_{j,s}(q),
\]
then the triangle inequality and volume preservation give
\[
N_j^{\mathrm{hom}}(U_tf)
\leq\sum_{s=0}^jP_{j,s}(q)\|\partial_x^{j-s}\partial_y^sf\|_1
\leq M_j(q)N_j^{\mathrm{hom}}(f).
\]
For \(q>0\), \(P_{j+1,s}(q)>P_{j,s}(q)\) whenever \(0\leq s\leq j\), so \(M_{j+1}(q)>M_j(q)\). Summing over orders gives \(N_k(U_tf)\leq M_k(q)N_k(f)\). For \(q=0\), the map is the identity and all \(M_j(0)=1\).

**2. Sharpness by the \(L^1\) non-inequality.** Fix a top-order index \(s_0\) maximizing \(P_{k,s}(q)\). The degree-\(k\) differential monomials
\(\partial_x^{k-s}\partial_y^s\), \(0\leq s\leq k\), are linearly independent. Ornstein's non-inequality, in the standard same-order form recalled and proved within the work cited in References [2], implies that for every \(\varepsilon>0\) there exists \(f_\varepsilon\in C_c^\infty(\mathbb R^2;\mathbb R)\) such that
\[
\sum_{\substack{0\leq s\leq k\\s\neq s_0}}
\|\partial_x^{k-s}\partial_y^s f_\varepsilon\|_1
\leq\varepsilon\|\partial_x^{k-s_0}\partial_y^{s_0}f_\varepsilon\|_1.
\]
Here the distinguished derivative cannot be identically zero; the non-inequality means exactly that no uniform coefficient controls it by the others. Applying the reverse triangle inequality row by row in the chain-rule expansion gives, for a constant \(B_{k,q}<\infty\) depending only on the fixed order and shear,
\[
N_k^{\mathrm{hom}}(U_tf_\varepsilon)
\geq\bigl(P_{k,s_0}(q)-B_{k,q}\varepsilon\bigr)
\|\partial_x^{k-s_0}\partial_y^{s_0}f_\varepsilon\|_1.
\]
Under dilation \(f_{\varepsilon,\lambda}(x,y)=f_\varepsilon(\lambda x,\lambda y)\), any derivative of order \(j\) scales in \(L^1\) as \(\lambda^{j-2}\). Hence, as \(\lambda\to\infty\), the ratio \(N_k(U_tf_{\varepsilon,\lambda})/N_k(f_{\varepsilon,\lambda})\) tends to the homogeneous top-order ratio. Since the top-order input denominator is at most \((1+\varepsilon)\) times its distinguished term,
\[
\|U_t\|\geq
\frac{P_{k,s_0}(q)-B_{k,q}\varepsilon}{1+\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) proves the exact formula. This argument does **not** assume that the independent derivative slots can be prescribed pointwise, and it does not replace Ornstein's theorem by finite numerical tests.

**3. Nonattainment.** For \(q>0\), strict growth of \(M_j(q)\) yields
\[
N_k(U_tf)\leq\sum_{j=0}^k M_j(q)N_j^{\mathrm{hom}}(f)
<M_k(q)\sum_{j=0}^kN_j^{\mathrm{hom}}(f)
\]
for every \(f\ne0\), because \(N_0^{\mathrm{hom}}(f)=\|f\|_1>0\). At \(t=0\) equality holds for every \(f\).

**4. Phase diagrams.** At order two the three column sums are \(1+q+q^2\), \(1+2q\), and \(1\), so the envelope switches at \(q=1\). At order three they are \(1+q+q^2+q^3\), \(1+2q+3q^2\), \(1+3q\), and \(1\). Comparing them pairwise yields the two positive upper-envelope crossings \(q=1/3\) and \(q=1+\sqrt2\). Their one-sided slopes are unequal: at the first crossing \(3<4\), and at the second the slope difference is \(2+2q>0\). Thus both transitions are genuine cusps.

**5. Why rank-one oscillations miss the endpoint constant.** For order two and \(0<q<1\), the leading derivative magnitudes of a conventional one-direction high-frequency test are proportional to \(a^2,|ab|,b^2\) with \((a,b)\ne(0,0)\). Since the unique winning column sum is \(1+2q\) and its gap over the pure horizontal column is \(q-q^2\), the triangle inequality bounds this test's limiting quotient by
\[
(1+2q)-(q-q^2)\frac{a^2+b^2}{a^2+|ab|+b^2}
\leq (1+2q)-\frac23q(1-q).
\]
Thus no single plane-wave direction obtains the sharp norm in the mixed regime. This strict gap explains why the published multiscale \(L^1\) non-inequality, rather than only a rank-one Fourier-symbol maximization, is essential to the equality proof.

## Verification

A separate standard-library script, `check_shear.py`, verifies the triangular chain-rule coefficient matrices, exact column sums, strict top-order domination, and the low-order upper-envelope inequalities on rational test grids. Its output is supplementary finite checking. The infinite-dimensional sharpness invokes the published Ornstein non-inequality stated above, whose hypotheses are independently checked for the linearly independent monomial differential operators; it is not established by the checker. The proof covers every integer \(k\geq1\) and every real \(t\).

## Relationship to prior work

Hamad [1] introduced precisely this complete unweighted derivative-sum norm in the 2026 classification of *surjective isometries*. Here the operator is a genuinely nonisometric coordinate shear and the claim is its exact quantitative norm, including optimal derivative mechanism, nonattainment, and phase transitions. Hamad's theorem provides the natural setting, not a proof of the present quantitative formula.

The crucial top-jet concentration is **not new**: it is a direct application of the classical Ornstein non-inequality [2,3]. The novel claimed specialization combines that non-inequality with a triangular all-order jet calculation and solves the resulting extremal polynomial envelope. Isometries between Sobolev spaces [4] and general composition estimates for quasiconformal maps [5] concern different isometry questions, gradient norms, or \(p>1\) regimes; they do not give the exact present \(L^1\) derivative-sum shear constant in the materials inspected. This is a literature-supported claim with residual priority risk, not proof of publication priority.

## Limitations

The result does not provide explicit compactly supported extremizing **sequences** beyond the existence furnished by Ornstein's theorem, does not study nonlinear diffeomorphisms or bounded domains, and does not classify all crossover points for arbitrary larger \(k\). The all-order norm formula and the explicit orders two and three are fully proved. No independent mathematical audit has been performed.

## References

[1] Samir Hamad, *Isometric Classification of Sobolev Spaces*, arXiv:2611.09577v1, first publicly submitted November 6, 2026, https://arxiv.org/html/2611.09577v1.

[2] Krystian Kazaniecki, Dmitriy M. Stolyarov, Michał Wojciechowski, *Anisotropic Ornstein Noninequalities*, Analysis & PDE 10(2) (2017), Theorem 2 and proof, DOI:10.2140/apde.2017.10.351, https://msp.org/apde/2017/10-2/apde-v10-n2-p04-p.pdf.

[3] Donald S. Ornstein, *A Non-Inequality for Differential Operators in the \(L^1\) Norm*, Archive for Rational Mechanics and Analysis (1962), DOI:10.1007/BF00253928.

[4] Markus Biegert and Robin Nittka, *Isometries between Sobolev spaces*, Math. Nachr. 285 (2012), 2059–2077, arXiv:0807.0360.

[5] Marcos Oliva and Martí Prats, *Sharp Bounds for Composition with Quasiconformal Mappings in Sobolev Spaces*, J. Math. Anal. Appl. 451 (2017), 1026–1044, DOI:10.1016/j.jmaa.2017.02.016 (abstract and opening available).
