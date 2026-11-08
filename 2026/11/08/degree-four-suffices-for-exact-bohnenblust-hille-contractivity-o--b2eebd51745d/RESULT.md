# Degree four suffices for exact Bohnenblust–Hille contractivity on progression-free three-monomial supports

## Finding
Let \(n\ge2\) and \(m\ge4\) be integers, and let \(\Lambda\subseteq\{\alpha\in\mathbb N_0^n:|\alpha|=m\}\) consist of three distinct exponent vectors. Set \(p_m=2m/(m+1)\) and
\[
D_m(\Lambda)=\sup_{0\ne P(z)=\sum_{\alpha\in\Lambda}c_\alpha z^\alpha}
\frac{(\sum_{\alpha\in\Lambda}|c_\alpha|^{p_m})^{1/p_m}}{\sup_{|z_1|,\ldots,|z_n|\le1}|P(z)|}.
\]
Then \(D_m(\Lambda)=1\) if and only if \(\Lambda\) contains no nontrivial three-term arithmetic progression. In the progression-free case, equality in the coefficient inequality for a nonzero polynomial holds if and only if it has just one nonzero coefficient. If the support contains a progression, \(D_m(\Lambda)>1\). The contractive half also holds for prescribed supports of cardinality one or two.

This gives a dimension-independent degree-four cutoff for three prescribed monomials. It does **not** assert that degree four is the least possible uniform cutoff.

## Assumptions and scope
All scalars are complex, the polynomial is homogeneous of degree \(m\), and the norm is the supremum norm on the complex unit polydisk (equivalently, by the maximum modulus principle, on \(\mathbb T^n\)). An arithmetic progression means distinct vectors \(\alpha-\beta,\alpha,\alpha+\beta\) with \(\beta\in\mathbb Z^n\setminus\{0\}\). The three designated monomials need not all have nonzero coefficients in a particular polynomial. No restriction is imposed on the number of variables apart from finiteness.

## Proof
**Step 1: distinct differences give a sharp pair-product control.** Assume \(\Lambda=\{\alpha_1,\alpha_2,\alpha_3\}\) contains no nontrivial three-term arithmetic progression. Every ordered difference \(\alpha_i-\alpha_j\) with \(i\ne j\) is distinct: if two such differences coincide, cancellation either makes the ordered pairs identical or produces \(2\alpha_k=\alpha_i+\alpha_j\), a forbidden progression. For \(P=\sum_{j=1}^3c_jz^{\alpha_j}\), put \(M=\|P\|_\infty\) and \(q=\sum_{j=1}^3|c_j|^2\). The function \(F(z)=M^2-|P(z)|^2\) is nonnegative on \(\mathbb T^n\), with mean \(M^2-q\). At the unique difference \(\alpha_i-\alpha_j\), the Fourier coefficient of \(F\) is \(-c_i\overline{c_j}\), so the elementary bound that each Fourier coefficient of a nonnegative function is at most its mean in modulus yields
\[
M^2\ge q+|c_i c_j|\qquad(i\ne j).
\]
Ordering magnitudes \(x\ge y\ge z\ge0\) gives \(M^2\ge x^2+y^2+z^2+xy\).

**Step 2: exact scalar inequality at exponent \(8/5\).** For every \(x\ge y\ge z\ge0\),
\[
(x^{8/5}+y^{8/5}+z^{8/5})^{5/4}\le x^2+y^2+z^2+xy,
\]
with equality only when \(y=z=0\) (or all three vanish). For \(x>0\), divide by \(x^2\), set \(t=y/x\), \(s=z/x\), and observe that \(0\le s\le t\le1\). The function
\[
H_t(s)=(1+t^{8/5}+s^{8/5})^{5/4}-s^2
\]
is strictly increasing for \(s>0\), since
\[
H_t'(s)=2s^{3/5}\bigl((1+t^{8/5}+s^{8/5})^{1/4}-s^{2/5}\bigr)>0.
\]
It is therefore enough to show \((1+2t^{8/5})^{5/4}\le1+t+2t^2\). Convexity on \([0,1]\) gives
\[
(1+2u)^{5/4}\le1+(3^{5/4}-1)u\quad(0\le u\le1).
\]
For every \(t>0\), elementary differentiation gives
\[
\frac{t+2t^2}{t^{8/5}}=t^{-3/5}+2t^{2/5}\ge\frac52(4/3)^{3/5}>3^{5/4}-1.
\]
The last strict inequality follows from two exact rational certificates: \(3^5\,20^4=38{,}880{,}000<38{,}950{,}081=79^4\) and \(59^5\,27=19{,}302{,}956{,}073<20{,}000{,}000{,}000=50^5\,64\), which imply \(3^{5/4}-1<59/20<(5/2)(4/3)^{3/5}\). The limiting case \(t=0\) is equality, establishing the scalar claim including rigidity.

**Step 3: contractivity and equality.** For \(m\ge4\), \(p_m\ge8/5\). Monotonicity of finite-dimensional \(\ell_p\) norms and Steps 1–2 give
\[
\left(\sum_{j=1}^{3}|c_j|^{p_m}\right)^{1/p_m}
\le (x^{8/5}+y^{8/5}+z^{8/5})^{5/8}
\le M.
\]
The scalar bound is strict if at least two coefficients are nonzero, whereas a monomial gives equality. Thus \(D_m(\Lambda)=1\), and equality is monomial-only.

**Step 4: the progression obstruction.** Suppose \(\Lambda\) contains \(\alpha-\beta,\alpha,\alpha+\beta\) with \(\beta\ne0\). Take
\[
P_\varepsilon(z)=z^\alpha+\varepsilon z^{\alpha+\beta}-\varepsilon z^{\alpha-\beta}.
\]
Because \(z^\beta\) traverses the circle as \(z\in\mathbb T^n\), one has \(\|P_\varepsilon\|_\infty^2=1+4\varepsilon^2\). On the other hand its coefficient \(\ell_{p_m}\) norm squared is \((1+2\varepsilon^{p_m})^{2/p_m}\). Since \(p_m<2\), the Bernoulli inequality yields \((1+2\varepsilon^{p_m})^{2/p_m}\ge1+(4/p_m)\varepsilon^{p_m}>1+4\varepsilon^2\) for all sufficiently small positive \(\varepsilon\). Therefore \(D_m(\Lambda)>1\) for every degree in which a progression exists. This completes both implications.

## Verification
The accompanying standalone Python checker performs 26,450 integer-exact assertions, including the two rational certificates, the scalar inequality on a fifth-power lattice (converted into an integer comparison), and unique-difference checks over numerous finite homogeneous triples. Run \(`python checker.py`\). The checker prints \(`THREE_MONOMIAL_BH_EXACT_OK 26450`\) when its assertions pass. These tests corroborate but do not replace the proof above; neither random nor finite exhaustive tests are used to justify the universally quantified theorem.

## Relationship to prior work
Pellegrino and Teixeira, *Rigidity of Exact Contractivity in the Complex Polynomial Bohnenblust–Hille Inequality* (arXiv:2610.36887v1, October 27, 2026), prove the analogous arithmetic-progression characterization for each fixed support size \(N\) once the degree exceeds a general explicit cutoff \(M_N\). Their (3.1)–(3.2) give \(M_3=\max\{3,1+\lceil \log3/\log(1+(1/19350)^4)\rceil\}\), far above four. The present result settles the three-monomial case already at every degree \(m\ge4\) through a coefficient-of-nonnegative-function estimate and a scalar inequality. Their Lemma 2.1 supplies the same progression obstruction; the proof above derives it directly.

Caro-Montoya, Núñez-Alarcón and Serrano-Rodríguez give asymptotic estimates for a distinct restriction, bounding the number of variables *within each monomial*; those estimates do not imply the exact contractivity cutoff for three chosen monomials. Related support-sensitive inequalities of Defant, Galicer, Mansilla, Mastyło and Muro likewise concern different parameter restrictions. No published equivalent degree-four three-monomial classification was identified in the checked sources; this is a best-knowledge priority assessment, not a uniqueness certificate.

## Limitations
This theorem is for complex polynomials with at most three prescribed monomials and \(m\ge4\). It does not determine the optimal cutoff, the complete degree-three classification, or the exact constant for noncontractive supports. It does not assert an analogous real-polynomial result. Publication priority requires further independent literature examination; no independent mathematical audit has been performed.

## References
1. D. M. Pellegrino and E. V. Teixeira, *Rigidity of Exact Contractivity in the Complex Polynomial Bohnenblust–Hille Inequality*, arXiv:2610.36887v1 (2026), Theorem A, Lemma 2.1 and equation (3.2), https://arxiv.org/abs/2610.36887.
2. N. Caro-Montoya, D. Núñez-Alarcón and D. Serrano-Rodríguez, *Asymptotic Contractivity of Bohnenblust–Hille Constants with Bounded Monomial Support*, Bull. Braz. Math. Soc. 57, 40 (2026), DOI: 10.1007/s00574-026-00527-1; arXiv:2607.20847.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Support-Sensitive Bohnenblust–Hille Inequalities and Local Invariants on Hamming Schemes*, arXiv:2607.05594 (2026).
