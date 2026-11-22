# Arithmetic cube-zero strata and the full cotangent-rank census of a cubic box algebra

## Finding

Let \(q=p^f\) be any prime power and consider the commutative, unital, 27-dimensional finite-field algebra
\[
 A_q=\mathbb F_q[x,y,z]/(x^3,y^3,z^3),\qquad \mathfrak m=(x,y,z)A_q.
\]
The **cotangent rank** of a unital \(\mathbb F_q\)-algebra endomorphism \(\varphi\) is the rank \(r\in\{0,1,2,3\}\) of its induced map on \(\mathfrak m/\mathfrak m^2\). The following formulas give the exact number \(c_r(q)\) of endomorphisms of each rank.

If \(p\ne3\), define
\[
 Z_q=\begin{cases}
 q^5+q^3-q^2,&p=2,\\
 q^5+q^3-q^2+q(q-1)^3\chi_q(6),&p\ge5,
 \end{cases}
 \qquad U=q^{17}Z_q,\quad V=q^{17}(q-1),
\]
where \(\chi_q(6)\in\{-1,1\}\) is the quadratic character in \(\mathbb F_q\) when \(p\ge5\). Then
\[
\begin{aligned}
 c_0(q)&=U^3,\\
 c_1(q)&=3\big((U+V)^3-U^3\big),\\
 c_2(q)&=3\big((U+2V)^3-2(U+V)^3+U^3\big),\\
 c_3(q)&=6V^3.
\end{aligned}
\]
In particular the full endomorphism monoid has order
\[
 \boxed{|\operatorname{End}_{\mathbb F_q\mathrm{-alg}}(A_q)|=q^{51}\big(Z_q+3(q-1)\big)^3.}
\]
If \(p=3\), all elements of \(\mathfrak m\) are cube-zero. Consequently, for \(0\le r\le3\),
\[
 \boxed{c_r(q)=q^{69}{3\brack r}_q\prod_{j=0}^{r-1}(q^3-q^j),}\qquad
 |\operatorname{End}_{\mathbb F_q\mathrm{-alg}}(A_q)|=q^{78},
\]
where \({3\brack r}_q\) denotes the Gaussian binomial coefficient and an empty product is one.

For \(p\ne3\), the only nonzero cotangent columns of a cube-zero generator image are scalar multiples of coordinate vectors; thus the rank-at-most-one obstruction is not merely a determinant condition. The arithmetic term \(\chi_q(6)\) makes the singular-endomorphism census nonpolynomial as a function of the field size in odd characteristics at least five.

## Assumptions and scope

All homomorphisms are unital and fix \(\mathbb F_q\) pointwise. The ideal \(\mathfrak m\) is the unique maximal ideal, and its quotient by its square is three-dimensional. Images of the three generators are required to be cube-zero. The claim counts *all* endomorphisms, including noninjective ones; it is not an automorphism-only enumeration and is not a statement about the endomorphism group scheme on nonreduced base rings. The formula uses the quadratic character in the actual field \(\mathbb F_q\), including proper extensions of prime fields.

## Proof

**1. Endomorphisms reduce to three independent cube-zero images.** Every nilpotent element of \(A_q\) lies in \(\mathfrak m\), since reduction modulo the maximal ideal is a field. A unital algebra endomorphism is therefore uniquely determined by three elements \(a,b,c\in\mathfrak m\) satisfying \(a^3=b^3=c^3=0\), with no other constraints. Their degree-one coefficient vectors are precisely the columns of the induced cotangent matrix. If \(p=3\), Frobenius gives \(a^3=0\) for every \(a\in\mathfrak m\): every monomial in \(a\) has at least one positive exponent, so its cube contains \(x^3\), \(y^3\), or \(z^3\). There are \(q^{23}\) choices of higher-degree coefficients for each fixed linear coefficient vector, hence \(q^{69}\) choices for each \(3\times3\) linear matrix. Counting such matrices of rank \(r\) by choosing their image \(r\)-space and a surjection to it gives \({3\brack r}_q\prod_{j=0}^{r-1}(q^3-q^j)\). Summing over all matrices yields \(q^{69}q^9=q^{78}\).

**2. Nonzero cotangent vectors when \(p\ne3\).** Let \(a\in\mathfrak m\) satisfy \(a^3=0\), and let its linear part be \(\ell=a_1x+a_2y+a_3z\). The degree-three part of \(a^3\) is \(\ell^3\). Its coefficient of \(x_i^2x_j\) for distinct \(i,j\) is \(3a_i^2a_j\). These monomials survive the box truncation. As \(3\ne0\), at most one of \(a_1,a_2,a_3\) can be nonzero. If the unique nonzero coefficient is that of \(x\), write
\[
 a=v+x u+x^2w
\]
uniquely with \(u,v,w\in\mathbb F_q[y,z]/(y^3,z^3)\), where \(u\) is a unit. The coefficients of \(x\) and \(x^2\) in \(a^3\) are respectively \(3v^2u\) and \(3v^2w+3vu^2\). Vanishing first implies \(v^2=0\), then \(v=0\); thus \(a\in xA_q\). Conversely, every \(a\in xA_q\) is cube-zero. There are \(\dim_{\mathbb F_q}(xA_q)=18\) basis monomials divisible by \(x\); fixing a nonzero coefficient of \(x\) yields \(V=(q-1)q^{17}\) possibilities, independent of which one of the three coordinates is used.

**3. Zero cotangent vectors.** If \(a\) has zero linear part, write \(a=Q+h\), with \(Q\) homogeneous of degree two and \(h\in\mathfrak m^3\). The largest surviving total degree in the ring is six, so \(a^3=Q^3\). Write
\[
 Q=A x^2+B y^2+C z^2+Dxy+Exz+Fyz.
\]
All degree-six monomials except \(x^2y^2z^2\) vanish. The coefficient of that monomial in \(Q^3\) is
\[
 3\big(2ABC+2DEF+AF^2+BE^2+CD^2\big).
\]
The ideal \(\mathfrak m^3\) has dimension \(17\) (there are \(1+3+6\) monomials of degrees zero through two, out of \(27\)). Thus each solution of the displayed degree-six scalar equation gives \(q^{17}\) cube-zero elements with zero cotangent vector.

**4. Evaluate the six-variable scalar equation.** When \(p=2\), its zero-locus equation becomes \(AF^2+BE^2+CD^2=0\). For \((D,E,F)=(0,0,0)\) there are \(q^3\) choices of \((A,B,C)\); for each of the other \(q^3-1\) triples there are \(q^2\) solutions. Hence the quadratic-part count is \(Z_q=q^3+(q^3-1)q^2=q^5+q^3-q^2\).

For \(p\ge5\), divide by three and solve for \(C\):
\[
 (2AB+D^2)C+AF^2+BE^2+2DEF=0.
\]
There are precisely \(q^2\) triples \((A,B,D)\) satisfying \(2AB+D^2=0\). For the other \(q^3-q^2\) triples and each pair \((E,F)\), there is one choice of \(C\), contributing \((q^3-q^2)q^2\). For the exceptional triples, let \(T\) count the choices of \((A,B,D,E,F)\) satisfying both constraints. The case \((A,B,D)=(0,0,0)\) contributes \(q^2\). Exactly \(2(q-1)\) other triples have \(AB=0\), each contributing \(q\). The remaining \((q-1)^2\) triples have \(AB\ne0\), and the binary quadratic \(AF^2+BE^2+2DEF\) is nondegenerate. Its determinant is \(AB-D^2=3AB\); since \(D^2=-2AB\), the square class of its negative determinant is that of \(3/2\), namely \(6\). A nondegenerate binary quadratic over \(\mathbb F_q\) has \(q+(q-1)\chi_q(-\det)\) zeroes. Consequently
\[
 T=q^2+2q(q-1)+(q-1)^2\big(q+(q-1)\chi_q(6)\big)
  =q^3+q^2-q+(q-1)^3\chi_q(6).
\]
Finally \(Z_q=(q^3-q^2)q^2+qT=q^5+q^3-q^2+q(q-1)^3\chi_q(6)\).

**5. Rank enumeration.** There are \(U=q^{17}Z_q\) choices for a generator image with zero cotangent column, and \(V=q^{17}(q-1)\) choices for each one of the three nonzero coordinate directions. The three generator images are chosen independently. Rank is simply the number of distinct coordinate directions used among the three columns. Inclusion-exclusion on the subsets of \(\{x,y,z\}\) gives
\[
 c_r(q)={3\choose r}\sum_{j=0}^r(-1)^{r-j}{r\choose j}(U+jV)^3.
\]
Expanding for \(r=0,1,2,3\) proves the four displayed formulas. Their sum is \((U+3V)^3\). For \(r=3\), the image has invertible cotangent matrix, and Nakayama's lemma shows the endomorphism is an automorphism; this boundary case agrees with known automorphism classification and is not asserted to be new on its own.

## Verification

The standalone `verify.py` independently implements coefficientwise multiplication in the 27-dimensional quotient, computes the degree-six coefficient of the cubic of every quadratic form, and exhaustively enumerates the six quadratic coefficients for \(q\in\{2,3,4,5,7,8\}\), using irreducible polynomial arithmetic for \(\mathbb F_4\) and \(\mathbb F_8\). It also independently cubed 950 seeded random elements and checked the general structural criterion, then checked rank-count sums in all six fields. The captured deterministic output is `verification_output.txt`, ending `VERIFY_OK direct_quadratics=6 sampled_powers=950 rank_profiles=6`.

Reproduce with `python3 verify.py`. Finite checks do not establish the infinite-field-family statement; that follows from the coefficient arguments and quadratic-form counts above. The checker evaluates \(\chi_q(6)\) only for prime odd test fields; the proof establishes the formula for all prime powers.

## Relationship to prior work

Angeltveit–Gerhardt–Hill–Lindenstrauss (2012) study precisely this class of multivariable truncated-polynomial rings but compute algebraic \(K\)-theory, not the finite-field endomorphism rank census. Díaz–Liendo–Manzano-Flores–Regeta (2024) study automorphism groups of zero-dimensional monomial algebras in characteristic zero. The published prime-power symmetry-jump result and the published smoothness-boundary result for automorphism schemes of box-truncated algebras describe automorphism groups, not all singular endomorphisms; their automorphism counts cover the rank-three boundary case above in certain characteristics. Related two-generator cubic-box Jordan enumerations concern multiplication by elements rather than endomorphism counts, and results on algebras truncated by \(\mathfrak m^3=0\) concern a different quotient. No statement inspected in these sources implies the four-rank census with its quadratic-character term.

## Limitations

The result applies to the fixed cubic-exponent, three-variable algebra, not arbitrary truncation exponents or embedding dimensions. It counts rational endomorphism points but neither describes the complete endomorphism-monoid multiplication table nor its scheme structure. The existence of potentially unindexed earlier work on finite algebra endomorphisms remains an originality risk; no independent historical or mathematical certification is claimed. The cubic characteristic is an exceptional regime, rather than a specialization of the odd-characteristic formula.

## References

1. V. Angeltveit, T. Gerhardt, M. A. Hill, A. Lindenstrauss, *On the algebraic K-theory of truncated polynomial algebras in several variables*, arXiv:1206.0247v1, first posted 2012-06-01, https://arxiv.org/abs/1206.0247 .
2. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197, first posted 2024-08-05, https://arxiv.org/abs/2408.02197 .
3. R. Díaz, G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group*, arXiv:2409.15081, first posted 2024-09-23, https://arxiv.org/abs/2409.15081 .
4. *An exact prime-power symmetry jump for modular monomial complete intersections*, publicly indexed scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-prime-power-symmetry-jump-for-modular-monomial-complete--bac767308614 .
5. *A sharp smoothness boundary for automorphism schemes of box-truncated polynomial algebras*, publicly indexed scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-smoothness-boundary-for-automorphism-schemes-of-box-trun--962bc42e198d .
