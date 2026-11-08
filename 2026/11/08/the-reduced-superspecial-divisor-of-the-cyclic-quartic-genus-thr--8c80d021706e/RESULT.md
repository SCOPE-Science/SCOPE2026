# The reduced superspecial divisor of the cyclic-quartic genus-three pencil at inert primes

## Finding

Let \(p\) be any prime with \(p\equiv3\pmod4\), \(k=\overline{\mathbb F}_p\), \(m=(p-1)/2\), and \(t\in k\setminus\{0,1\}\). Consider the smooth plane quartic
\[
 C_t:\quad Y^4=XZ(X-Z)(X-tZ).
\]
Define the Deuring polynomial
\[
 H_m(T)=\sum_{i=0}^{m}\binom mi^2T^i\in\mathbb F_p[T].
\]
In the standard monomial basis of \(H^1(C_t,\mathcal O_{C_t})\), its semilinear Hasse–Witt matrix is
\[
\operatorname{diag}(0,-H_m(t),0).
\]
Consequently the Jacobian's Cartier \(a\)-number is \(2\) when \(H_m(t)\ne0\) and \(3\) when \(H_m(t)=0\), while its \(p\)-rank is, respectively, \(1\) or \(0\). Its Prym abelian surface for the quotient by \(Y\mapsto-Y\) is superspecial for **every** smooth parameter. The full genus-three Jacobian is superspecial precisely at the roots of \(H_m\). Those roots give exactly \(m=(p-1)/2\) pairwise distinct, reduced, smooth **marked coefficient parameters** in \(k\); no claim is made about the number of curve isomorphism classes. In particular the pencil supplies an explicit superspecial smooth nonhyperelliptic plane quartic in every prime characteristic congruent to three modulo four.

## Assumptions and scope

The base field is algebraically closed of prime characteristic \(p\equiv3\pmod4\), including \(p=3\). The parameter excludes the colliding branch values \(0\) and \(1\). The equation is a homogeneous plane quartic, and its quotient \(E_t\) by the involution \(Y\mapsto-Y\) is the elliptic curve \(v^2=x(x-1)(x-t)\). Cartier \(a\)-number means \(\dim_k\operatorname{Hom}(\alpha_p,\operatorname{Jac}(C_t)[p])\). The \(p\)-rank is the dimension of the stable semilinear Frobenius image on \(H^1(C_t,\mathcal O)\). Superspecial means that the \(a\)-number equals the dimension of the abelian variety, equivalently it is geometrically isomorphic to a product of supersingular elliptic curves. This is a statement about a marked one-dimensional family, not the full genus-three moduli space.

## Proof

**1. Smoothness and the cohomology basis.** Write \(F=Y^4-P\), where \(P=XZ(X-Z)(X-tZ)\). Since \(p\ne2\), any singular point would have \(Y=0\), and then would be a repeated zero of one of the four distinct linear factors of \(P\) on the line \(\mathbb P^1\), which is impossible for \(t\ne0,1\). Thus \(C_t\) is smooth of genus \((4-1)(4-2)/2=3\). The exact sequence \(0\to\mathcal O_{\mathbb P^2}(-4)\xrightarrow{F}\mathcal O_{\mathbb P^2}\to\mathcal O_{C_t}\to0\) identifies \(H^1(C_t,\mathcal O_{C_t})\) with \(H^2(\mathbb P^2,\mathcal O(-4))\). A Cech basis is represented by the three Laurent monomials whose negative exponent triples are
\[
 (2,1,1),\qquad(1,2,1),\qquad(1,1,2).
\]
Frobenius is represented by the coefficients of \(X^{pa_1-b_1}Y^{pa_2-b_2}Z^{pa_3-b_3}\) in \(F^{p-1}\), for these exponent triples \(a,b\). This follows directly by lifting absolute Frobenius through the above hypersurface sequence: on Cech representatives it applies \(p\)-th powers and multiplies by \(F^{p-1}\), followed by projection onto the three basis monomials.

**2. The exact Hasse–Witt entry.** The \(Y\)-exponents in \(F^{p-1}\) are multiples of four. Since \(p\equiv3\pmod4\), among the nine indicated coefficient targets the only one with \(Y\)-exponent divisible by four has both exponent triples equal to \((1,2,1)\). Put \(m=(p-1)/2\). This coefficient is that of \(X^{2m}Y^{4m}Z^{2m}\). Taking \(m\) factors \(Y^4\) and \(m\) factors \(-P\) in \(F^{2m}\) yields
\[
\binom{2m}{m}(-1)^m\,[X^m Z^m]\bigl((X-Z)^m(X-tZ)^m\bigr)
=\binom{2m}{m}\sum_{j=0}^{m}\binom mj^2t^j.
\]
Because \(\binom{p-1}{m}\equiv(-1)^m=-1\pmod p\), the matrix is exactly \(\operatorname{diag}(0,-H_m(t),0)\). Its rank is one or zero according as \(H_m(t)\) is nonzero or zero. Its stable Frobenius rank is likewise one or zero: a nonzero one-by-one semilinear block remains nonzero under every iterate. Hence the asserted \(p\)-ranks and \(a\)-numbers follow.

**3. The Prym.** The quotient by the involution \(Y\mapsto-Y\) is the smooth elliptic Legendre curve \(E_t:v^2=x(x-1)(x-t)\). The degree-two pullback and norm maps yield a \(2\)-power-degree isogeny \(E_t\times P_t\to\operatorname{Jac}(C_t)\), where \(P_t\) is the connected Prym surface. Since \(p\) is odd, the isogeny induces an isomorphism on \(p\)-divisible groups and Cartier modules. The one-dimensional central Frobenius block is the elliptic quotient block (the quotient differential is \(dx/y^2\)); the other two blocks are zero on the Prym component. Thus \(a(P_t)=2\), and this abelian surface is superspecial for every admissible \(t\). Also \(\operatorname{Jac}(C_t)\) is superspecial if and only if \(E_t\) is supersingular, which is equivalent to \(H_m(t)=0\).

**4. Exactly \(m\) simple roots.** The polynomial \(H_m\) has degree \(m\) with leading coefficient one, and \(H_m(0)=1\) while \(H_m(1)=\binom{2m}{m}\equiv-1\ne0\). Its coefficients satisfy the exact hypergeometric differential equation in characteristic \(p\):
\[
 T(1-T)H_m''+(1-2T)H_m'-m^2H_m=0.
\]
Suppose \(\alpha\notin\{0,1\}\) were a multiple root. Then both \(H_m(\alpha)\) and \(H_m'(\alpha)\) would vanish. Because \(\alpha(1-\alpha)\ne0\), the differential equation recursively forces every Taylor coefficient up to degree \(m\) to vanish: at each stage the coefficient of the next derivative is a nonzero multiple of \(\alpha(1-\alpha)\), with factorials nonzero since \(m<p\). This contradicts \(H_m\ne0\). Thus all \(m\) roots are simple and avoid the two excluded parameters; the superspecial parameter divisor is reduced of degree \(m\).

## Verification

Run `python3 verify.py` using only the standard library. The verifier independently computes all nine potential plane-quartic Hasse–Witt coefficients using binomial expansion rather than assuming the claimed matrix, checks the Deuring polynomial identity and its differential equation, computes polynomial gcds to test squarefreeness, and enumerates prime-field roots for primes \(3,7,11,19,23,31,43,47,59,67,71,79\), all congruent to three modulo four. It prints `VERIFY_M7_CARTIER_OK 12`. This finite replay supports the algebraic derivation but is not an exhaustive test of every prime; the proof establishes the universal statement. The derivation of the Prym splitting uses standard norm/pullback properties of degree-two covers, not a numerical experiment.

## Relationship to prior work

Goodson [1] studies **this same quartic pencil**, its hypergeometric periods and point-count formulas, but does not determine the present \(p\equiv3\pmod4\) Cartier-rank stratification or count its superspecial parameters. Li–Mantovan–Pries–Tang [2, Table in Section 6.1] already list the **two possible Newton polygons** in the characteristic-three-mod-four case, namely an ordinary elliptic factor with a supersingular surface and the supersingular threefold; those possibilities and the generic Newton polygon are prior work, not new claims. Their table does not identify exactly which smooth marked parameters realize the basic case, count them, or determine the full Cartier \(a\)-numbers. Cavalieri–Pries [3, Section 6.1, Corollary 6.4] identify the Moonen family \(M[7]\) with inertia \((1,1,1,1)\) and compute mass and \(a\)-number data **under** \(p\equiv1\pmod4\); their hypotheses exclude the present residue class. Moonen [4] establishes the ambient special-family classification. The classical Deuring polynomial controls the supersingular Legendre elliptic quotient; the contribution here is its precise scheme-theoretic pullback to the **nonhyperelliptic genus-three** superspecial and Cartier strata at inert primes. This classification is not an assertion of priority for the Deuring polynomial, the general Hasse–Witt coefficient method, Newton polygon possibilities, or the Prym decomposition principle.

## Limitations

The count \(m\) is for geometric marked coefficient parameters \(t\) on the punctured affine line, not for geometric isomorphism classes of unmarked plane quartics, and not for rational parameters over a specified finite subfield. No zeta functions, Frobenius signs over \(\mathbb F_{p^2}\), or rational-point maxima are asserted. The result applies only to primes congruent to three modulo four; the complementary split-prime behavior is treated differently in the cited literature. An older published parameter-level theorem under equivalent hypergeometric notation remains a residual historical-priority risk. The earliest directly relevant public account of the exact genus-three pencil among the inspected sources is [1], dated May 5, 2017; [2]–[4] provide subsequent or broader mathematical context.

## References

[1] Heidi Goodson, *Hypergeometric Properties of Genus 3 Generalized Legendre Curves*, arXiv:1705.02404 (public May 5, 2017), Section 5. https://arxiv.org/abs/1705.02404

[2] Wanlin Li, Elena Mantovan, Rachel Pries, Yunqing Tang, *Newton Polygons Arising from Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914 (public May 17, 2018), Sections 5–6, especially the table for the family M[7]. https://arxiv.org/abs/1805.06914

[3] Renzo Cavalieri, Rachel Pries, *Mass Formula for Non-Ordinary Curves in One Dimensional Families*, arXiv:2308.14891 (first public August 28, 2023), Sections 2 and 6. https://arxiv.org/abs/2308.14891

[4] Ben Moonen, *Special Subvarieties Arising from Families of Cyclic Covers of the Projective Line*, Documenta Mathematica 15 (2010), 793–819, Table 1. https://doi.org/10.4171/DM/314
