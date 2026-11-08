# Real-rooted Ehrhart numerators of height-one tetrahedral Cayley frusta

## Finding
For every pair of positive integers \(a,b\), let \(\Delta_3=\operatorname{conv}(0,e_1,e_2,e_3)\) be the standard lattice tetrahedron, and set
\[
P_{a,b}=\operatorname{conv}\big((a\Delta_3)\times\{0\},(b\Delta_3)\times\{1\}\big)\subset\mathbb R^4.
\]
Every zero of its Ehrhart numerator \(h^*_{P_{a,b}}(z)\) is **real, strictly negative, and simple**. This holds uniformly for unequal tetrahedral bases, including all unit-lattice-width, non-Cartesian cases. Its degree is one for \((a,b)=(1,1)\), two when \(\{a,b\}=\{1,2\}\), and three otherwise.

The exact numerator is \(1+h_1z+h_2z^2+h_3z^3\), with
\[
\begin{aligned}
6h_1={}&a^3+b^3+6(a^2+b^2)+11(a+b)-18,\\
6h_2={}&4(a^3+b^3)+3ab(a+b)+12ab-22(a+b)+18,\\
6h_3={}&(a+b-3)(a+b-2)(a+b-1).
\end{aligned}
\]
In particular, this real-rootedness statement implies log-concavity and unimodality of the numerator coefficients. It addresses a different invariant from Ehrhart-polynomial coefficient positivity, which by itself does not establish where the numerator zeros lie.

## Assumptions and scope
Here \(a,b\in\mathbb Z_{\ge1}\), \(z\) is an indeterminate, and \(\mathbb Z^4\) is the ambient lattice. Ehrhart's numerator is defined by
\[
\sum_{k\ge0}|kP_{a,b}\cap\mathbb Z^4|z^k=\frac{h^*_{P_{a,b}}(z)}{(1-z)^5}.
\]
The four-dimensional polytope has exactly six facets, namely \(t\ge0\), \(t\le1\), \(x_i\ge0\) for \(1\le i\le3\), and \(x_1+x_2+x_3\le a+(b-a)t\). It is smooth: at each vertex the three primitive edges in its tetrahedral layer form a lattice basis in the first three coordinates, and the fourth primitive edge between layers has final coordinate \(\pm1\). Hence all four primitive edge directions form a basis of \(\mathbb Z^4\). Each vertical coordinate lies between zero and one; the lattice width therefore equals one.

## Proof
**Exact lattice count.** For every integer \(k\ge0\), the section of \(kP_{a,b}\) at final coordinate \(j\), where \(0\le j\le k\), is \((a(k-j)+bj)\Delta_3\). Consequently,
\[
E_{a,b}(k)=\sum_{j=0}^{k}\binom{a(k-j)+bj+3}{3}.
\]
For \(0\le r\le4\), coefficient extraction in the defining series gives
\[
h_r=\sum_{j=0}^{r}(-1)^{r-j}\binom{5}{r-j}E_{a,b}(j).
\]
Expansion yields the three displayed coefficient formulas and \(h_4=0\). The latter also follows from Ehrhart reciprocity: no lattice point can be interior to \(P_{a,b}\), because its fourth coordinate would have to lie strictly between zero and one.

**Nonnegative coordinates.** Put \(X=a-1\ge0\), \(Y=b-1\ge0\). Algebraically the coefficients become
\[
\begin{aligned}
6h_1={}&X^3+Y^3+9(X^2+Y^2)+26(X+Y)+18,\\
6h_2={}&4(X^3+Y^3)+3XY(X+Y)+15(X^2+Y^2)+24XY+11(X+Y),\\
6h_3={}&(X+Y-1)(X+Y)(X+Y+1).
\end{aligned}
\]
Thus \(h_1>0\) always, \(h_2>0\) when \(X+Y>0\), and \(h_3>0\) exactly when \(X+Y\ge2\) for integral nonnegative \(X,Y\).

**Real and simple roots.** When \(X+Y=0\), the numerator equals \(1+3z\), with one simple negative root. When \(X+Y=1\), it equals \(1+9z+5z^2\); the quadratic discriminant is \(61>0\), so both roots are simple and negative.

Suppose \(X+Y\ge2\). For the cubic \(h_3z^3+h_2z^2+h_1z+1\), its discriminant is
\[
\mathcal D=h_1^2h_2^2-4h_3h_1^3-4h_2^3-27h_3^2+18h_1h_2h_3.
\]
The exact polynomial identity certified in `certificate.json` and reconstructed by `verify.py` states that
\[
432\mathcal D=\sum_{\substack{i,j\ge0\\i+j\ge1}}c_{ij}X^iY^j,
\]
where precisely 90 coefficients \(c_{ij}\) are nonzero, all are **strictly positive integers**, and \(c_{1,0}=c_{0,1}=7776\). Every other coefficient is zero. In particular \(432\mathcal D\ge7776(X+Y)>0\). Hence the cubic has three **distinct real roots**. Since each of its coefficients is positive, the polynomial is strictly positive for \(z\ge0\); every real root must therefore be strictly negative. This completes the proof for all positive integers \(a,b\).

The certificate is an exact polynomial identity, not a finite-grid inference. It can be independently reconstructed from the displayed formulas without numerical root finding.

## Verification
Execute `python3 verify.py` in the directory containing `certificate.json`. Only Python's standard library is required. The script constructs exact bivariate integer polynomials for the numerators of the three \(h_i\), expands the cubic discriminant using integer polynomial arithmetic, divides its integer coefficients by three to obtain \(432\mathcal D\), and compares every monomial with the supplied 90-entry certificate. It checks integral positivity, symmetry, and the boundary cases. As a separate cross-check, it evaluates Ehrhart lattice counts directly for every integer pair \(1\le a,b\le13\) and each \(0\le k\le4\), comparing them to the coefficient-extraction formula (845 integer comparisons). Those finite comparisons are supplementary; the polynomial identity supplies the proof for all parameters.

## Relationship to prior work
Liu, Tang, Tao, and Zhang (2026), Theorem 2.1 and Proposition 3.1, classify smooth lattice polytopes with few facets and prove **positivity of Ehrhart polynomial coefficients** through four dimensions for at most six facets. Their one-simplex-bundle normal form includes these tetrahedral frusta, but their result does not classify roots of the distinct numerator polynomial. The present theorem settles the entire two-parameter height-one tetrahedral bundle subfamily, including the unequal-layer cases inapplicable to Cartesian-product root-preservation results.

Ferroni (2026) demonstrates that even smooth Cayley constructions can have nonunimodal Ehrhart numerators, so the strong positive root behavior here is not a formal consequence of being smooth or Cayley. Nill's 2026 theorem on sufficiently large lattice width does not cover this width-one family. Zonotope real-rootedness does not apply to the unequal-layer frusta, whose tetrahedral facets are not centrally symmetric. Large-dilation Veronese real-rootedness likewise does not apply to a polytope of lattice width one.

## Limitations
Only tetrahedra in two homothetic parallel layers at **unit lattice separation** are covered. This does **not** prove real-rootedness of all smooth four-dimensional six-facet polytopes, nor of higher-dimensional frusta or arbitrary Cayley sums. The 90-term discriminant expansion is an exact finite algebraic certificate; its correctness is independently reproducible from the source formulas. Historical-priority assessment is based on inspected relevant literature and research-record searches, not on a proof of uniqueness; earlier equivalent formulations remain possible. No independent external mathematical audit has been performed.

## References
1. F. Liu, J. Tang, S. Tao, and Z. Zhang, *Ehrhart positivity of smooth polytopes with few facets*, arXiv:2610.27819, first public 2026-10-20. https://arxiv.org/abs/2610.27819 (Theorem 2.1, Proposition 3.1).
2. L. Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513, first public 2026-09-09, v2 2026-10-29. https://arxiv.org/html/2609.10513v2 (Sections 1–4).
3. B. Nill, *Lattice polytopes of large width have real-rooted Ehrhart h*-polynomials*, arXiv:2608.03635, first public 2026-08-04. https://arxiv.org/abs/2608.03635.
4. M. Beck, K. Jochemko, and E. McCullough, *h*-Polynomials of zonotopes*, arXiv:1609.08596, 2016. https://arxiv.org/abs/1609.08596.
5. K. Jochemko, *On the real-rootedness of the Veronese construction for rational formal power series*, arXiv:1602.09139, 2016. https://arxiv.org/abs/1602.09139.
