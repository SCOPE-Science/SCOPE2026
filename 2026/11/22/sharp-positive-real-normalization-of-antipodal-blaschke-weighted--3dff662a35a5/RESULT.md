# Sharp positive-real normalization of antipodal Blaschke-weighted Bergman kernels

## Finding
For a two-point antipodal finite Blaschke weight in the analytic Bergman disk, the ordinary Bergman denominator provides a *sharp half-plane normalization*:
\[
\operatorname{Re}\bigl[(1-z\overline w)^2 K_a(z,w)\bigr]>1
\qquad(z,w\in\mathbb D).
\]
Its constant is optimal, as equality holds in the continuous boundary extension when \(z=w\) lies on the unit circle. A companion exact bivariate polynomial-margin theorem is proved below.

## Assumptions and scope
Write \(\mathbb D=\{z:|z|<1\}\), choose any real \(0<a<1\), put \(t=a^2\), and define
\[
 B_a(z)=\frac{z^2-t}{1-tz^2},\qquad
 \|f\|_{a}^{2}=\frac1\pi\int_{\mathbb D}|f(z)|^{2}|B_a(z)|^{2}\,dA(z).
\]
Let \(K_a(z,w)\) be the analytic weighted Bergman reproducing kernel, with its second argument anti-holomorphic. A boundary statement always refers to the unique continuous rational extension for fixed \(t\in(0,1)\). Introduce the *independent* complex variable \(\eta=\overline w\); its closed-bidisk range is \(|z|,|\eta|\le1\).

The precise rational identity is
\[
S_t(z,\eta):=(1-z\eta)^2K_a(z,\overline\eta)
=1+\frac{2(1-t^2)}{1+t^2}
\frac{(1-z\eta)(1+t^2z\eta)}{(1-tz^2)(1-t\eta^2)}.
\tag{1}
\]
Define the polynomial \(P_t(z,\eta)=(1+t^2)(1-tz^2)(1-t\eta^2)S_t(z,\eta)\), equivalently
\[
P_t=3-t^2-t(1+t^2)(z^2+\eta^2)-2(1-t^2)^2z\eta
+t^2(3t^2-1)z^2\eta^2.
\tag{2}
\]
The second, sharp assertion is
\[
\min_{|z|,|\eta|\le1}|P_t(z,\eta)|=(1-t)^2(1+t^2),
\]
with equality exactly at \((z,\eta)=(1,1)\) and \((-1,-1)\). Its scale as \(t\uparrow1\) is \(2(1-t)^2(1+o(1))\).

## Proof
**Reproducing-kernel reduction.** Multiplication by \(B_a\) is an isometry from the weighted space onto the ordinary Bergman closed subspace of functions vanishing at both \(a\) and \(-a\). The latter is the orthogonal complement of the two evaluation vectors. Their even and odd combinations are
\[
E_a(z)=\frac{1+t z^2}{(1-t z^2)^2},\qquad
O_a(z)=\frac{2az}{(1-t z^2)^2},
\]
with squared norms \(E_a(a)=(1+t^2)/(1-t^2)^2\) and \(O_a(a)=2t/(1-t^2)^2\); they are orthogonal by parity. Consequently the vanishing-subspace kernel equals
\[
\frac1{(1-z\eta)^2}
-\frac{E_a(z)E_a(\eta)}{E_a(a)}
-\frac{O_a(z)O_a(\eta)}{O_a(a)}.
\]
Divide by \(B_a(z)B_a(\eta)\), initially away from its zeros, and cancel the removable factors. Direct polynomial expansion (also checked in `CHECK.py`) gives (1) and (2) everywhere on the bidisk.

**Strict positivity.** Denote the rational factor following the positive coefficient in (1) by
\[
T_t(z,\eta)=\frac{(1-z\eta)(1+t^2z\eta)}{(1-tz^2)(1-t\eta^2)}.
\]
On \(|z|=|\eta|=1\), write \(z=e^{i\alpha}\), \(\eta=e^{i\beta}\), and let \(u=\cos(\alpha+\beta)\), \(c=\cos(\alpha-\beta)\). Multiplying by the conjugate of its denominator and simplifying gives the *exact torus certificate*
\[
\operatorname{Re}T_t(e^{i\alpha},e^{i\beta})
=\frac{(1-t^2)(1-u)(1+t^2+2tc)}
{|(1-t e^{2i\alpha})(1-t e^{2i\beta})|^2}\ge0.
\tag{3}
\]
The denominator is positive and \(1+t^2+2tc\ge(1-t)^2>0\), so equality holds on the torus precisely when \(z\eta=1\). The real part of \(T_t\) is separately harmonic in each variable and continuous on the closed bidisk. Applying the harmonic minimum principle successively shows \(\operatorname{Re}T_t\ge0\) throughout. It is in fact strictly positive at every interior pair: otherwise the strong minimum principle in the first variable and then the second would force it to vanish identically, contradicting \(T_t(0,0)=1\). Equation (1) thus gives \(\operatorname{Re}S_t>1\) in the open bidisk, with exact boundary equality for \(z\eta=1\).

**Sharp polynomial margin.** On the closed bidisk, (1) and (3) imply \(|S_t|\ge\operatorname{Re}S_t\ge1\). Since \(|1-tz^2|\ge1-t\) and \(|1-t\eta^2|\ge1-t\), the definition of \(P_t\) gives
\[
|P_t(z,\eta)|\ge(1+t^2)(1-t)^2.
\]
Equality requires \(|1-tz^2|=|1-t\eta^2|=1-t\), hence \(z^2=\eta^2=1\), and also \(S_t=1\), which on this finite set forces \(z\eta=1\). The two stated pairs realize equality. The last asymptotic follows directly from the exact constant.

## Verification
The standalone Python 3/SymPy script `CHECK.py` checks (1)–(2), the rank-two deletion identity, the numerator in the torus certificate (3), both sharp boundary pairs, and the margin asymptotic by exact symbolic algebra. The proof of nonnegativity and strictness uses the sign factors and the minimum principle; no finite numerical test replaces that argument.

## Relationship to prior work
Hansbo, *Reproducing kernels and contractive divisors in Bergman spaces* (original 1996; English journal translation 1998), already gives an explicit two-point weighted Bergman kernel formula and a qualitative zero-free property of the normalized kernel. Miña-Díaz (first public preprint 15 December 2022), Theorem 1.1 and formula (1.11), provide a more general representation, explicitly crediting Hansbo for the two-point case. The present observation is **not a new kernel formula** or another proof of qualitative zero-freeness; it is the stronger sharp half-plane containment and quantitative globally sharp bivariate polynomial nonvanishing margin, using the antipodal geometry. Related published single-point positive-real statements concern a different one-variable extremal function and do not by themselves imply the simultaneous two-variable bound.

## Limitations
The theorem is confined to antipodal simple zeros, weight exponent two, and standard normalized disk area. No analogous positivity claim for arbitrary two-point zero configurations, higher multiplicities, or other exponents is asserted. Historical priority is best-knowledge, not established exhaustively: especially the older general two-point kernel literature may contain equivalent estimates not detected in the inspected statements. An independent mathematical audit has not been performed.

## References
1. Jonas Hansbo, *Reproducing kernels and contractive divisors in Bergman spaces*, Zap. Nauchn. Semin. POMI 232 (1996), 174–198; J. Math. Sci. (N.Y.) 92 (1998), 3657–3674. https://www.mathnet.ru/links/bc70d4ee2f64790e8861d64e243d85a6/znsl3685.pdf ; https://doi.org/10.1007/BF02440151
2. Erwin Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118, initial version 15 December 2022; Anal. Math. Phys. 13 (2023), article 58. https://arxiv.org/abs/2212.08118
3. T. H. MacGregor and M. I. Stessin, *Weighted reproducing kernels in Bergman spaces*, Michigan Math. J. 41 (1994). https://doi.org/10.1307/MMJ/1029005077
