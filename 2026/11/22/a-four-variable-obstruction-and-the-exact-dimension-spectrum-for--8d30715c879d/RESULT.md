# A four-variable obstruction and the exact dimension spectrum for ordered-separating cubic Boolean functions

## Finding
Let \(V=\mathbb F_2^n\), \(n\geq1\), and let \(\alpha:V\to\mathbb F_2\) satisfy \(\alpha(0)=0\). Write
\[
D_2\alpha(x,z)=\alpha(x+z)+\alpha(x)+\alpha(z),\qquad S_x=\{z\in V:D_2\alpha(x,z)=1\}.
\]
Call \(\alpha\) *ordered separating* if, for all distinct nonzero \(x,y\in V\), the set difference \(S_x\setminus S_y\) is nonempty.

**Theorem.** An ordered-separating Boolean polynomial of algebraic degree **exactly three** on \(\mathbb F_2^n\) exists if and only if
\[
\boxed{n=3\quad\text{or}\quad n\ge5.}
\]
More strongly, in dimension four every degree-three Boolean polynomial has two distinct nonzero commutation rows with strict support inclusion. After a linear change of coordinates, the obstruction can always be witnessed by an empty row or by rows of respective cardinalities \((4,8)\) or \((8,12)\), with the smaller support strictly contained in the larger one. Linear summands do not affect this conclusion.

## Assumptions and scope
Polynomials are square-free algebraic normal forms over \(\mathbb F_2\). The degree-three requirement is essential: the four-variable quadratic polynomial \(x_1x_2+x_3x_4\) **does** satisfy ordered separation, because its second polar is a nondegenerate alternating bilinear form. No arbitrary functions of algebraic degree four or higher are covered. A linear term may be added to impose \(\alpha(e_i)=1\) for every coordinate basis vector without changing \(D_2\alpha\) or the theorem.

## Proof
**1. Cubic normal form in four variables.** Let \(\deg\alpha=3\) on \(V=\mathbb F_2^4\). The third combinatorial polar \(D_3\alpha\) is a nonzero alternating trilinear form. The natural isomorphism \(\Lambda^3V^*\cong V\otimes\Lambda^4V^*\) shows that \(\mathrm{GL}(V)\) is transitive on nonzero such forms: the determinant character is trivial over \(\mathbb F_2\). Equivalently, each nonzero three-form has a one-dimensional radical and a volume form on the three-dimensional quotient. Since the third polar uniquely determines the cubic homogeneous component, a linear change of coordinates reduces \(\alpha\), up to a linear summand, to
\[
\alpha(u_1,u_2,u_3,s)=u_1u_2u_3
+a u_1u_2+b u_1u_3+c u_2u_3
+s(\lambda_1u_1+\lambda_2u_2+\lambda_3u_3),
\]
where all coefficients are in \(\mathbb F_2\). The linear summand is omitted because its second polar vanishes.

**2. A forced nested pair.** If \(\lambda_1=\lambda_2=\lambda_3=0\), the nonzero vector \(r=(0,0,0,1)\) has \(S_r=\varnothing\). The cubic part is nonzero, so some other nonzero row is nonempty; hence there is strict inclusion.

Otherwise a further invertible transformation of the first three variables puts \(\lambda(u)=u_1\), keeping the cubic coefficient one and allowing the displayed arbitrary quadratic coefficients to change. Let
\[
r=(0,0,0,1),\quad x=(0,1,0,s),\quad z=(w_1,w_2,w_3,t).
\]
A direct expansion of the second polar gives
\[
D_2\alpha(r,z)=w_1,\qquad
D_2\alpha(x,z)=w_1(w_3+s+a)+cw_3.
\]
Set \(s=a+c\). When \(c=0\), the latter is \(w_1w_3\), so \(S_x\subsetneq S_r\), with respective cardinalities \(4\) and \(8\). When \(c=1\), the latter is \(w_1(w_3+1)+w_3\), so \(S_r\subsetneq S_x\), with respective cardinalities \(8\) and \(12\). The two nonzero vectors \(r,x\) are distinct. Thus no degree-three polynomial in four variables is ordered separating. This proves the negative part without relying on enumeration.

**3. Sharpness and all remaining dimensions.** No polynomial in fewer than three Boolean variables has degree three. In dimension three, \(t(x)=x_1x_2x_3\) has ordered separation; the direct second-polar row calculation is given in Pineda Montoya, Lemma 4.1 (2026). In odd dimensions \(n=3+2m\) with \(m\ge1\), use
\[
 t(x_1,x_2,x_3)+\sum_{j=1}^{m} x_{2j+2}x_{2j+3}.
\]
This is ordered separating by the three-variable seed, nondegenerate quadratic-block separation, and the direct-sum lemma, as proved in Pineda Montoya's Theorem A. In even dimensions \(n=6+2m\), \(m\ge0\), use the direct sum of two disjoint ternary monomials followed by \(m\) nondegenerate quadratic blocks; two ternary blocks separate by the direct-sum lemma (Pineda Montoya, Corollary 8.1). Every example still has a cubic monomial, so its algebraic degree is exactly three. All positive dimensions are therefore attained.

## Verification
The standalone \(\texttt{verify.py}\) checks ordered separation directly from second-polar row truth tables. It exhausts all \((2^4-1)2^6=960\) choices of nonzero cubic and arbitrary quadratic coefficients on four variables; the other \(2^4\) possible linear parts have no effect. Every choice has a failing ordered pair. It independently checks each of the eight canonical nested-support witnesses and additionally verifies explicit positive examples in dimensions \(3,5,6,7,8\) and a degree-two positive example in dimension four. The execution output was \(\texttt{VERIFY_OK 960 [3, 5, 6, 7, 8] WITNESS_OK}\). These checks corroborate the four-dimensional obstruction and small constructions; the proof above, not finite testing, establishes the general dimension spectrum.

## Relationship to prior work
Morier-Genoud and Ovsienko (2010/2011), Appendix 10, introduced the exact ordered separation condition and conjectured that its cubic solutions are equivalent to symmetric normal forms. Pineda Montoya (2026) disproved that classification and proved the ternary seed, odd-dimensional symplectic extensions, and direct-sum constructions, including dimension six. Those existence results are credited here. The new result is the four-variable nonexistence proof, its explicit nested-row obstruction, and the resulting sharp *existence dimension spectrum*; none is asserted to follow merely from a title search or from the known constructions alone.

## Limitations
The theorem classifies dimensions of existence, not all cubic polynomials, their linear equivalence or all twisted quasialgebras. The normalization and exact-degree conventions matter: a nondegenerate quadratic form is a counterexample to any version of the negative statement that allows degree at most three. Historical priority has not been independently established beyond the checked sources; an unlocated equivalent treatment remains possible. No independent audit has been performed.

## References
1. S. Pineda Montoya, *Counterexamples to a Cubic Nondegeneracy Conjecture*, arXiv:2611.02544v1, publicly submitted 2026-11-02. Full text: https://arxiv.org/html/2611.02544v1. Especially Sections 2, 3, 4, 5, and 8.
2. S. Morier-Genoud and V. Ovsienko, *A Series of Algebras Generalizing the Octonions and Hurwitz–Radon Identity*, arXiv:1003.0429v4 (first posted 2010-03-01), especially Appendix 10, “Cubic polynomials.” Full text: https://arxiv.org/html/1003.0429v4.
