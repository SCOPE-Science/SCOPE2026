# Morse-rigid Jordan spectra of ternary quadratic layers in modular group algebras

## Finding

Let \(p\ge3\) be prime, \(q=p^e\), \(e\ge1\), and
\[
A=\mathbb F_q[x,y,z]/(x^p,y^p,z^p)\cong\mathbb F_q[(C_p)^3].
\]
Write \(\mathfrak m=(x,y,z)\). For a homogeneous quadratic \(Q\in A_2\), let \(r(Q)\in\{0,1,2,3\}\) be the rank of its symmetric coefficient matrix, with mixed monomials represented by half their coefficients. For \(f\in A\), let \(J(f)\) be the nilpotent Jordan multiset of left multiplication \(M_f:a\mapsto fa\), whenever \(f\in\mathfrak m\). Denote a size-\(j\) nilpotent Jordan block by \(J_j\), and write \(J_j^{\oplus a}\) for its multiplicity.

**Theorem (complete quadratic census and nonsingular-lift rigidity).** The Jordan multiset \(J(Q)\) depends only on \(r=r(Q)\), and the *entire* rank-stratified census is

| \(r\) | \(J(Q)\) | Number of quadratic forms over \(\mathbb F_q\) |
|---|---|---|
| \(0\) | \(J_1^{\oplus p^3}\) | \(1\) |
| \(1\) | \(J_{(p+1)/2}^{\oplus p^2}\oplus J_{(p-1)/2}^{\oplus p^2}\) | \(q^3-1\) |
| \(2\) | \(J_p^{\oplus p}\oplus\bigoplus_{j=1}^{p-1}J_j^{\oplus 2p}\) | \(q^2(q^3-1)\) |
| \(3\) | \(J_p^{\oplus(p^2+1)/2}\oplus\bigoplus_{j=1}^{p-1}J_j^{\oplus4\min(j,p-j)}\) | \(q^2(q-1)(q^3-1)\) |

For every \(f\in\mathfrak m^2\) with nonsingular quadratic initial form \(Q=f\bmod\mathfrak m^3\), there is an \(\mathbb F_q\)-algebra automorphism \(\phi\) of \(A\) satisfying \(\phi(Q)=f\). Consequently \(J(f)=J(Q)\), including its \((p^2+1)/2\) blocks of maximum possible size \(p\). This full-rank initial-form stratum contains exactly
\[
q^{p^3-10}\,q^2(q-1)(q^3-1)
\]
elements of \(\mathfrak m^2\). The four Jordan multisets for homogeneous quadratics are pairwise distinct, so \(J(Q)\) recovers the quadratic rank.

## Assumptions and scope

The characteristic is an odd prime; the coefficient field is any finite extension of its prime field. The count is of distinct coefficients of homogeneous degree-two elements, not of projective quadrics or of algebraic-group orbits. The lift assertion covers *only* elements of \(\mathfrak m^2\) whose quadratic initial form is nonsingular; it does not assert stability for degenerate initial forms. The operator acts on the full \(p^3\)-dimensional regular module, not on a quotient or a graded component. All Jordan blocks have eigenvalue zero, since \(f^p=0\) for \(f\in\mathfrak m\).

## Proof

**1. Coordinate normal forms and nilpotence.** Every invertible linear coordinate substitution preserves the ideal \((x^p,y^p,z^p)\) in characteristic \(p\): the \(p\)-th power of each new coordinate is a linear combination of the original \(p\)-th powers. Thus \(\mathrm{GL}_3\) acts by automorphisms of \(A\). After extending scalars to an algebraic closure, every homogeneous quadratic of rank \(r\) is equivalent, up to a nonzero scalar, to a form on exactly \(r\) independent coordinates. Scalar extension does not change nilpotent Jordan multiplicities, and multiplying the operator by a nonzero scalar does not change its blocks. We may take rank-one normal form \(z^2\), rank-two form \(xy\), and rank-three form \(xy+z^2\). This also proves independence from the discriminant square class over \(\mathbb F_q\).

**2. Ranks zero, one and two.** Multiplication by zero has \(p^3\) blocks of size one. Put \(m=(p-1)/2\). On \(k[z]/z^p\), multiplication by \(z^2\) has two chains: exponents of even parity yield a block of length \(m+1\), and odd parity a block of length \(m\). The untouched two variables contribute a factor of \(p^2\). For \(xy\) on \(k[x,y]/(x^p,y^p)\), monomials split into chains indexed by exponent difference \(a-b\): there is one chain of length \(p\) and two of each length \(j=1,\ldots,p-1\). The untouched third variable contributes a factor \(p\).

**3. The modular tensor calculation for rank three.** Let \(J_a\boxplus J_b\) denote the Jordan multiset of \(X\otimes I+I\otimes Y\), where \(X,Y\) are single nilpotent Jordan blocks of lengths \(a,b\le p\). For \(a\le b\), the modular Clebsch--Gordan rule is
\[
J_a\boxplus J_b=\begin{cases}
\displaystyle\bigoplus_{i=1}^{a}J_{a+b-2i+1},&a+b\le p+1,\\
\displaystyle J_p^{\oplus(a+b-p)}\oplus\bigoplus_{i=1}^{p-b}J_{b-a+2i-1},&a+b>p+1.
\end{cases}
\]
Here the second summation is empty when \(b=p\). This rule also holds when \(a>b\) after swapping the two factors. For completeness, it follows by induction from \(J_2\boxplus J_b=J_{b-1}\oplus J_{b+1}\) for \(2\le b<p\), \(J_2\boxplus J_p=J_p^{\oplus2}\), and \(J_1\boxplus J_b=J_b\). The base rule follows directly by Jordan-reducing multiplication by \(X+Y\) on \(k[X,Y]/(X^2,Y^b)\); its top connecting coefficient is \(b\), nonzero for \(b<p\). Associativity and the recurrence then give the displayed two-case formula, including the boundary where top blocks fold into length \(p\). This is also the classical modular Jordan tensor rule.

We have, as a module for the relevant nilpotent operator,
\[
(k[x,y]/(x^p,y^p),M_{xy})\simeq J_p\oplus2\bigoplus_{a=1}^{p-1}J_a,
\qquad (k[z]/z^p,M_{z^2})\simeq J_m\oplus J_{m+1}.
\]
Their external tensor sum is exactly multiplication by \(xy+z^2\). For fixed \(b\in[1,p-1]\), the multiplicity of any nonprojective \(J_j\), \(1\le j<p\), in \(\bigoplus_{a=1}^{p-1}(J_a\boxplus J_b)\) is
\[
c_{b,j}=\min\{b,p-b,j,p-j\}.
\]
Indeed the two-case rule says \(J_j\) occurs precisely for integers \(a\) of parity \(b+j-1\) in the inclusive interval
\[
|b-j|+1\le a\le\min\{b+j-1,2p-b-j-1\}.
\]
Counting this arithmetic progression yields the stated minimum. At \(b=m,m+1\), both minima equal \(\min(j,p-j)\). The twofold coefficient in the \(xy\) decomposition and both \(z^2\) chains give exactly \(4\min(j,p-j)\) blocks of every size \(j<p\). The \(J_p\) summand from the \(xy\) chain contributes only length-\(p\) blocks. As the total dimension is \(p^3\), and
\[
\sum_{j=1}^{p-1}4j\min(j,p-j)=\frac{p(p^2-1)}2,
\]
the remaining length-\(p\) multiplicity is \((p^2+1)/2\). This completes the rank-three computation.

**4. Exact field counts.** The six quadratic coefficients correspond bijectively to symmetric \(3\)-by-\(3\) matrices because \(2\) is invertible. Rank zero gives one matrix. Rank one gives \((q-1)(q^2+q+1)=q^3-1\), by choosing its one-dimensional image and a nonzero symmetric form there. For rank two, choose the one-dimensional radical (\(q^2+q+1\) choices) and a nonsingular symmetric bilinear form on the two-dimensional quotient (\(q^2(q-1)\) choices). Subtracting from the \(q^6\) total yields the rank-three count \(q^2(q-1)(q^3-1)\). The different Jordan multisets are distinguished first by largest block size, then by the multiplicity of \(J_p\): \(p\) for rank two versus \((p^2+1)/2>p\) for rank three.

**5. Formal Morse stability for all nonsingular lifts.** Let \(f=Q+h\), where \(Q\) is nonsingular of degree two and \(h\in\mathfrak m^3\). Its partial derivatives are linearly independent linear forms generating \(\mathfrak m/\mathfrak m^2\). Suppose a coordinate change has removed all corrections of degree less than \(d\ge3\), leaving homogeneous degree-\(d\) part \(h_d\). Write \(h_d=\sum_i (\partial_i Q)u_i\) with homogeneous \(u_i\) of degree \(d-1\) (possible because the gradient generates the maximal ideal). Substituting \(x_i\mapsto x_i-u_i\) removes \(h_d\) and only creates terms of degree at least \(d+1\), since \(2(d-1)\ge d+1\). Such substitutions preserve the truncation ideal by Frobenius and are filtered automorphisms. Induction through the top nonzero total degree \(3(p-1)\) removes the entire tail. The resulting automorphism conjugates the multiplication operators. Since \(\dim\mathfrak m^2/\mathfrak m^3=6\), and \(\dim\mathfrak m^3=p^3-10\), each nonsingular quadratic form has precisely \(q^{p^3-10}\) distinct lifts, proving the count.

## Verification

The standalone Python program `checker.py` builds multiplication operators in the monomial basis and computes all ranks of their powers by sparse finite-field elimination; it does not invoke the modular Clebsch--Gordan formula in those rank calculations. It checks **all 729** homogeneous quadratics over \(\mathbb F_3\), including exact rank-stratum multiplicities; selected representatives and reproducibly seeded coefficients over \(\mathbb F_5\) and \(\mathbb F_7\); and higher-order nonsingular lifts in characteristics three and five. A separate modular-fusion arithmetic check verifies the symbolic block formula for primes through nineteen. The captured output is `checker_output.txt`. The proof is uniform in prime and extension degree; finite tests do not constitute the proof.

## Relationship to prior work

Carlson, Friedlander and Pevtsova (2011, arXiv:1106.4474) develop invariants of restrictions of modules over group algebras of elementary abelian groups to subalgebras generated by *linear* nilpotent elements, establishing the regular truncated-polynomial model. Norman (2010) and Barry (2015, arXiv:1508.01768) develop modular Jordan rules for tensor products and Kronecker sums of indecomposable blocks. Those rules supply a key ingredient here; they are **not** claimed as new. The result assessed here is the explicit rank-three quadratic multiplication classification, four finite-field quadratic-rank strata, and the nonsingular higher-order lifting rigidity in the regular algebra. Closely related existing two-generator quadratic-symbol classifications do not imply the ternary counts or the ternary modular-fusion multiplicities without the additional computation. A broad tensor-product rule can of course be used to derive part of the result, and the exact historical priority of the assembled formula remains subject to independent literature review.

## Limitations

This theorem addresses homogeneous quadratic elements in exactly three variables and arbitrary elements with **nonsingular quadratic initial form**. It does not classify all nonhomogeneous elements with degenerate quadratic initial form, all radical elements, characteristics two, or group-algebra modules other than the regular module. Formal Morse normalization relies on odd characteristic and an invertible quadratic Hessian. The bibliography search does not establish global historical uniqueness, and no independent validation is claimed.

## References

- J. F. Carlson, E. M. Friedlander and J. Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, initial public preprint 2011-06-22, https://arxiv.org/abs/1106.4474.
- M. J. J. Barry, *Generators for Decompositions of Tensor Products of Modules associated with standard Jordan partitions*, initial public preprint 2015-08-07, https://arxiv.org/abs/1508.01768.
- C. W. Norman, *On Jordan bases for the tensor product and Kronecker sum and their elementary divisors over fields of prime characteristic*, Linear and Multilinear Algebra, online 2010-09-22, https://doi.org/10.1080/03081080701395640.
