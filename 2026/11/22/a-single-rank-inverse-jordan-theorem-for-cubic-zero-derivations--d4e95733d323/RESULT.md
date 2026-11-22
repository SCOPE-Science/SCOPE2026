# A single-rank inverse Jordan theorem for cubic-zero derivations of height-one symmetric algebras

## Finding
Let \(k\) be any field of characteristic three and let \(V\) be an \(n\)-dimensional \(k\)-vector space, where \(n\geq1\). Put
\[
A(V)=\operatorname{Sym}_k(V)/(v^3:v\in V).
\]
For every \(T\in\operatorname{End}_k(V)\) satisfying \(T^3=0\), let \(D_T\) be the degree-preserving algebra derivation of \(A(V)\) determined by \(D_T(v)=T(v)\). Write the nilpotent Jordan partition of \(T\) as \((1^a,2^b,3^c)\), so \(a+2b+3c=n\). If \(b+c=0\), then \(D_T=0\). Otherwise set
\[
h=3^a 2^{2(b+c)-1}.
\]
Then the complete Jordan form of \(D_T\) is
\[
J_1^{\oplus h}\oplus J_2^{\oplus h}\oplus J_3^{\oplus(3^{n-1}-h)},
\]
and hence
\[
\operatorname{rank}(D_T)=2\cdot3^{n-1}-h,\qquad
\operatorname{rank}(D_T^2)=3^{n-1}-h.
\]
In particular, **the single integer \(\operatorname{rank}(D_T)\), together with the known dimension \(n\), uniquely determines the complete Jordan partition of the original operator \(T\)**. For positive rank, compute \(h=2\cdot3^{n-1}-\operatorname{rank}(D_T)\), then
\[
a=v_3(h),\quad t=\frac{v_2(h)+1}{2},\quad c=n-a-2t,\quad b=t-c.
\]
For zero rank, \(T=0\) and \((a,b,c)=(n,0,0)\).

For every \(q=3^f\), the exact finite-field polynomial counting all such \(T\) by the rank of the induced derivation is
\[
1+\sum_{\substack{a,b,c\ge0\\a+2b+3c=n\\b+c>0}}
\frac{|\operatorname{GL}_n(\mathbb F_q)|}{q^{(a+b+c)^2+(b+c)^2+c^2}
\prod_{j=1}^{a}(1-q^{-j})\prod_{j=1}^{b}(1-q^{-j})\prod_{j=1}^{c}(1-q^{-j})}
\,z^{\,2\cdot3^{n-1}-3^a2^{2(b+c)-1}}.
\]
Empty products are one. Each displayed coefficient is an integer, because it is a nilpotent conjugacy-class cardinality. At \(n=3\), \(q=3\), the polynomial is \(1+104z^{12}+624z^{16}\).

## Assumptions and scope
The algebra is the **height-one truncated symmetric algebra**: after choosing a basis of \(V\), it is \(k[x_1,\ldots,x_n]/(x_1^3,\ldots,x_n^3)\), of dimension \(3^n\). This is **not** the total-degree-three truncation \(\operatorname{Sym}(V)/(V)^{3}\), and it is not the exterior algebra. The operator \(D_T\) is a derivation induced by a linear map on the generators, not multiplication by an element of the algebra. We classify exactly the subfamily with \(T^3=0\), not every derivation of \(A(V)\).

In characteristic three, the ideal \((v^3:v\in V)\) is preserved by any derivation induced from \(T\), since \(D_T(v^3)=3v^2T(v)=0\). Moreover \(D_T^3\) is itself a derivation, because all the intervening binomial coefficients in its Leibniz expansion vanish modulo three. It vanishes on generators when \(T^3=0\), so \(D_T^3=0\) on the entire algebra. Thus only Jordan block lengths one, two, and three occur.

## Proof
**1. Reduction to three fixed modules.** The Jordan normal form of \(T\) is defined over \(k\), since its annihilating polynomial divides \(X^3\). For a length-\(s\) Jordan block, choose \(x_1,\ldots,x_s\) with \(D(x_1)=0\) and \(D(x_j)=x_{j-1}\) for \(j>1\). Denote by \(M_s\) the resulting \(k[D]/(D^3)\)-module on \(k[x_1,\ldots,x_s]/(x_1^3,\ldots,x_s^3)\). The original algebra is the tensor product of the block algebras, and on tensor products the derivation acts by \(D\otimes1+1\otimes D\).

**2. Exact local Jordan matrices.** In the monomial basis indexed by \(\alpha\in\{0,1,2\}^s\), the matrix is completely specified by
\[
D(x^\alpha)=\sum_{j=2}^s \alpha_j x^{\alpha-e_j+e_{j-1}},
\]
where terms containing a third power of a variable are zero and all coefficients are reduced modulo three. Elementary row reduction of the matrices and their squares, separated by total degree, gives the following exact checks (the three entries in each row are respectively total dimension, rank of \(D\), rank of \(D^2\)):

| Block | Degrees in order | Degreewise triples |
|---|---|---|
| \(s=1\) | \(0,1,2\) | \((1,0,0),(1,0,0),(1,0,0)\) |
| \(s=2\) | \(0,1,2,3,4\) | \((1,0,0),(2,1,0),(3,2,1),(2,1,0),(1,0,0)\) |
| \(s=3\) | \(0,1,2,3,4,5,6\) | \((1,0,0),(3,2,1),(6,4,2),(7,4,1),(6,4,2),(3,2,1),(1,0,0)\) |

The matrices have coefficients in \(\mathbb F_3\); their ranks therefore do not change upon extension to arbitrary characteristic-three fields. Using \(m_3=\operatorname{rank}(D^2)\), \(m_2=\operatorname{rank}(D)-2m_3\), and \(m_1=\dim-2\operatorname{rank}(D)+m_3\), these triples give
\[
[M_1]=3[J_1],\qquad [M_2]=2[J_1]+2[J_2]+[J_3],\qquad
[M_3]=2[J_1]+2[J_2]+7[J_3].
\]
These finite matrix reductions can be reproduced from the complete standalone source `VERIFY.py`; no claim about arbitrarily large matrices is inferred from an experiment.

**3. Exact primitive tensor rules.** Let \(J_s\) denote the indecomposable \(s\)-dimensional nilpotent \(k[D]/(D^3)\)-module. With the primitive tensor action, direct rank reduction on tensor products of matrices of sizes at most nine gives
\[
J_2\otimes J_2\cong J_1\oplus J_3,\quad
J_2\otimes J_3\cong J_3^{\oplus2},\quad
J_3\otimes J_3\cong J_3^{\oplus3}.
\]
The module \(J_1\) is the tensor unit. These rules are valid in every characteristic-three field, and prove that the additive subgroup generated by \([J_3]\) is a tensor ideal in the Green ring of \(k[D]/(D^3)\)-modules. In the quotient ring, \([J_2]^2=[J_1]\).

**4. Tensor multiplication and ranks.** Each \(M_2\) or \(M_3\) reduces modulo the projective ideal to \(2([J_1]+[J_2])\), while each \(M_1\) reduces to \(3[J_1]\). Put \(t=b+c>0\). Modulo the projective ideal the tensor product has class
\[
3^a2^t([J_1]+[J_2])^t
=3^a2^{2t-1}([J_1]+[J_2]).
\]
The equality follows immediately from \(([J_1]+[J_2])^2=2([J_1]+[J_2])\). Thus the actual multiplicities of \(J_1\) and \(J_2\) are both \(h\). Since \(\dim A(V)=3^n\), the remaining multiplicity is \((3^n-3h)/3=3^{n-1}-h\). The displayed rank formulas follow. All multiplicities are nonnegative, and the full nilpotent Jordan form is thereby determined for every \(n\).

**5. Injectivity and exact counting.** If \(T\ne0\), unique factorization \(h=3^a2^{2t-1}\) recovers \(a\) and \(t\); the known equation \(n=a+2b+3c=a+2t+c\) then recovers \(c\) and \(b\). A zero induced derivation forces \(T=D_T|_V=0\), so this case is separate. Finally, the centralizer algebra of Jordan type \((1^a,2^b,3^c)\) has vector-space dimension \((a+b+c)^2+(b+c)^2+c^2\). Its group of invertible elements has order equal to the displayed power of \(q\) times the three factors \(\prod_{j=1}^m(1-q^{-j})\) for \(m=a,b,c\), respectively. Orbit-stabilizer under \(\operatorname{GL}_n(\mathbb F_q)\) gives the exact coefficient in the finding.

## Verification
The accompanying self-contained Python program `VERIFY.py` implements exact linear algebra over \(\mathbb F_3\). It checks each local block and all three primitive tensor rules, then exhaustively examines all \(3^9\) three-by-three matrices, retaining the 729 matrices with cube zero and computing the induced 27-dimensional Jordan profile for each. It also checks canonical block combinations in dimensions four and five. The expected three-dimensional counts are one zero matrix, 104 matrices of Jordan type \((2,1)\), and 624 matrices of type \((3)\). The program exits successfully with `TRUNCATED_SYMMETRIC_JORDAN_RIGIDITY_VERIFIED` when every assertion passes. This finite verification supports the fixed-size lemmas; the unrestricted-dimensional conclusion follows from the tensor proof.

## Relationship to prior work
Chang and Yao (first public version 15 August 2021, arXiv:2108.06657) study tensor products of defining Witt-algebra modules on truncated polynomial rings in characteristic greater than three. Their focus is the two-fold tensor module's invariant subspaces and composition series, not this characteristic-three nilpotent linear derivation and its rank-inversion theorem. Korhonen (arXiv:2101.01365) studies nilpotent actions on degree-two exterior and symmetric powers in characteristic two. Benson and Symonds (arXiv:1902.02895) study general tensor-module projectivity and core asymptotics, not this specific exact multiplicity and rank classification. Doty and Walker's work on truncated symmetric powers and \(\operatorname{GL}_n\)-representations addresses a broader modular setting; its author-uploaded text describes composition factors and Schur-module characters, not the rank-one-parameter inverse for the induced restricted derivations studied here. A complete line-by-line priority comparison remains incomplete.

Nearby indexed exact results classify **multiplication** Jordan spectra on the height-one algebra in two variables, and composition-idempotent derivations on a different *total-degree truncated* algebra. Multiplication operators and composition-idempotent derivations do not encompass the degree-preserving cubic-zero induced derivations classified here. A previously reported exterior-algebra result uses a different \(2^n\)-dimensional algebra and two ranks to identify nilpotent generator type; it neither implies this formula for the \(3^n\)-dimensional truncated symmetric algebra nor determines this single-rank inverse.

## Limitations
Only derivations induced by linear \(T\) with \(T^3=0\) are classified, not arbitrary vector fields on the truncated algebra. The theorem is specific to characteristic three. The finite-field count enumerates such \(T\), equivalently the corresponding distinct \(D_T\); no claim is made about all derivations of \(A(V)\). Computations alone do not establish an all-dimensional result: the tensor argument does. No absolute literature-priority certification is asserted. The general modular-representation literature may contain an equivalent statement not identified in the inspected material; particularly the OCR-imperfect author-uploaded Doty–Walker full text could not be comprehensively compared at every line.

## References
- H. Chang and Y.-F. Yao, *Tensor products of the defining representations over the Witt algebra in positive characteristic*, arXiv:2108.06657, first posted 2021-08-15, https://arxiv.org/abs/2108.06657.
- M. Korhonen, *Decomposition of exterior and symmetric squares in characteristic two*, arXiv:2101.01365, first posted 2021-01-05, https://arxiv.org/abs/2101.01365.
- D. J. Benson and P. Symonds, *The non-projective part of the tensor powers of a module*, arXiv:1902.02895, first posted 2019-02-08, https://arxiv.org/abs/1902.02895.
- S. Doty and G. Walker, *Truncated symmetric powers and modular representations of \(\operatorname{GL}_n\)*, Math. Proc. Cambridge Philos. Soc. 119 (1996), 231–242, https://doi.org/10.1017/S0305004100074120.
