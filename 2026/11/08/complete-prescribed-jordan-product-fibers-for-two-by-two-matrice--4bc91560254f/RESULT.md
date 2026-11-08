# Complete prescribed Jordan-product fibers for two-by-two matrices over odd finite fields

## Finding
Let \(k=\mathbb F_q\) be any finite field of odd order, \(M=M_2(k)\), and define the ordinary anticommutator-fiber count
\[
N_q(C)=\#\{(A,B)\in M^2:AB+BA=C\}.
\]
For \(C\in M\), let \(e(C)\) be the number of one-dimensional \(k\)-subspaces invariant under \(C\), and let \(z(C)\) be the number of such subspaces contained in \(\ker C\). They count \(k\)-rational eigenlines, including the zero-eigenvalue lines. The complete fiber law is
\[
N_q(C)=\begin{cases}
q^5+3q^4-2q^3-2q^2+q,& C=0,\\
q^5+q^4-2q^3-q^2+q,& C=\lambda I,\ \lambda\ne0,\\
q^2(q^2-1)+q(q-1)(qz(C)-e(C)),& C\text{ nonscalar}.
\end{cases}
\]
The nonzero nonscalar cases form exactly five similarity-invariant strata. The table lists each stratum, its \((e,z)\), its number of output matrices, and its fiber count \(N_q\):

| Target type | \((e,z)\) | Number of targets | Fiber count |
| --- | --- | --- | --- |
| Irreducible quadratic characteristic polynomial | \((0,0)\) | \(q^2(q-1)^2/2\) | \(q^2(q^2-1)\) |
| Nondiagonalizable, repeated nonzero eigenvalue | \((1,0)\) | \((q-1)(q^2-1)\) | \(q^2(q^2-1)-q(q-1)\) |
| Nonzero nilpotent Jordan block | \((1,1)\) | \(q^2-1\) | \(q^2(q^2-1)+q(q-1)^2\) |
| Two distinct nonzero eigenvalues | \((2,0)\) | \(q(q+1)(q-1)(q-2)/2\) | \(q^2(q^2-1)-2q(q-1)\) |
| Two distinct eigenvalues, one zero | \((2,1)\) | \(q(q+1)(q-1)\) | \(q^2(q^2-1)+q(q-1)(q-2)\) |

The remaining targets are the zero matrix (one target) and the nonzero scalar matrices (\(q-1\) targets). These seven target classes partition all \(q^4\) matrices, and the weighted fiber mass is exactly \(q^8\). The novelty-bearing component is the full **prescribed nonzero target** distribution; the zero-target anticommuting-pair count is a previously studied specialization.

## Assumptions and scope
The field is an arbitrary finite prime-power field of odd characteristic, including nonprime fields. The ordered factors are unrestricted labeled matrices in \(M_2(k)\). The product is \(AB+BA\), not the Lie commutator \(AB-BA\). If one instead uses the normalized Jordan product \((AB+BA)/2\), its fiber at \(C\) is the displayed count evaluated at \(2C\); because \(2\) is invertible and rescales eigenvalues, the same seven-stratum distribution results.

## Proof
Write \(\tau(A)=\operatorname{tr}(A)\) and let \(T_A:M\to M\) be \(T_A(B)=AB+BA\). For each fixed \(A\), every nonempty fiber of \(T_A\) has exactly \(q^{4-\operatorname{rank}T_A}\) elements. Partition the \(q^4\) first factors into four disjoint classes.

**(i) \(A=0\).** The map \(T_A\) is zero. It contributes \(q^4\) solutions if and only if \(C=0\).

**(ii) \(\tau(A)=0\), \(A\ne0\).** Polarizing the two-by-two Cayley--Hamilton identity gives, for arbitrary \(A,B\),
\[
AB+BA=\tau(A)B+\tau(B)A+
\bigl(\operatorname{tr}(AB)-\tau(A)\tau(B)\bigr)I.
\]
Thus \(T_A(B)=\tau(B)A+\operatorname{tr}(AB)I\) when \(\tau(A)=0\). Because the field has odd characteristic, \(A\ne0\) with trace zero is nonscalar; the trace pairing is nondegenerate and the two linear functionals \(\tau(B)\) and \(\operatorname{tr}(AB)\) are independent. Hence \(\operatorname{im}T_A=kI+kA\) and \(\operatorname{rank}T_A=2\). There are \(q^3-1\) such first factors. For scalar \(C\), every one yields \(q^2\) second factors. For nonscalar \(C\), put \(D=C-\tau(C)I/2\). The condition \(C\in kI+kA\) is equivalent to \(A\in k^\times D\); therefore exactly \(q-1\) first factors yield \(q^2\) solutions each.

**(iii) \(\tau(A)\ne0\), \(\det A=0\).** In this case \(A=t(I-P)\) for a unique nonzero \(t=\tau(A)\in k^\times\) and a unique rank-one idempotent \(P\) projecting onto \(\ker A\). In a basis adapted to \(P\), the map \(T_A\) sends a matrix \(B\) to one with its first diagonal entry zero and its remaining three entries arbitrary. Thus \(\operatorname{rank}T_A=3\), with
\[
C\in\operatorname{im}T_A\quad\Longleftrightarrow\quad\operatorname{tr}(PC)=0.
\]
Every such first factor contributes \(q\) solutions. To count suitable rank-one idempotents \(P\), fix a projective line \(U=ku\). Every projection with image \(U\) is \(P=u\varphi\), where \(\varphi(u)=1\), and there are \(q\) of these. The additional condition is \(\varphi(Cu)=0\). When \(Cu\notin U\) there is exactly one such functional, when \(Cu=0\) all \(q\) work, and when \(Cu\in U\setminus\{0\}\) none works. Since there are \(q+1\) lines, the number of suitable projections is
\[
M(C)=q+1-e(C)+qz(C).
\]
For each projection, \(t\) has \(q-1\) choices; the full contribution is \(q(q-1)M(C)\).

**(iv) \(\tau(A)\ne0\), \(\det A\ne0\).** Over an algebraic closure, the eigenvalues of \(T_A\) are \(2\lambda_1\), \(\lambda_1+\lambda_2\) twice, and \(2\lambda_2\), where \(\lambda_1,\lambda_2\) are the eigenvalues of \(A\), counted with multiplicity. Since both determinant and trace of \(A\) are nonzero, these four eigenvalues are nonzero. This remains true when \(A\) is nondiagonalizable: invertibility of \(T_A\) follows by the same determinant calculation. Each such \(A\) contributes exactly one \(B\), for any \(C\). There are \(q^3\) matrices of each prescribed trace. For a nonzero trace, the singular ones are exactly the \(q(q+1)\) rank-one matrices \(t(I-P)\), giving the constant contribution
\[
U=(q-1)\bigl(q^3-q(q+1)\bigr)=(q-1)q(q^2-q-1).
\]

Adding (i)--(iv), for nonscalar \(C\), gives
\[
U+q(q-1)(q+1-e(C)+qz(C))+q^2(q-1)
=q^2(q^2-1)+q(q-1)(qz(C)-e(C)).
\]
For \(C=\lambda I\), \(\lambda\ne0\), every projective line is a nonzero-eigenvalue line, hence \(e=q+1,z=0\) and the rank-three contribution vanishes; add \(U+q^2(q^3-1)\). At zero, all \(q+1\) lines are zero-eigenvalue lines, so \(M(0)=q(q+1)\), and there is the extra contribution \(q^4\) from (i). This gives the two scalar formulas.

Finally, a nonscalar \(2\times2\) matrix is classified by its irreducible, repeated-root, or split separable characteristic polynomial, refined by which roots are zero. Using elementary conjugacy-centralizer sizes, the multiplicities are: \(q(q-1)\) per irreducible quadratic, \(q^2-1\) per nontrivial Jordan block, and \(q(q+1)\) per unordered distinct pair of eigenvalues. There are \(q(q-1)/2\) monic irreducible quadratics, \(q-1\) nonzero repeated roots, \((q-1)(q-2)/2\) unordered pairs of nonzero distinct roots, and \(q-1\) unordered pairs with exactly one zero. This proves every table row. Summing their target populations with scalars gives \(q^4\), and summing output counts weighted by the formulas gives \(q^8\), as required by the definition of \(N_q\).

## Verification
The included `verify_prime_fields.py` independently constructs every ordered pair of literal two-by-two matrices over \(\mathbb F_3\) and \(\mathbb F_5\) (respectively \(3^8=6561\) and \(5^8=390625\) pairs), computes the four entries of \(AB+BA\), and compares the resulting fiber counts at every target to the theorem. Both complete enumerations passed. The zero-fiber sizes were \(417\) and \(4705\), respectively; the seven ordered fiber sizes were \(60,66,72,78,84,264,417\) for \(q=3\), and \(560,580,600,660,680,3480,4705\) for \(q=5\). The weighted mass equals \(q^8\) in each case.

The included `verify_extension.py` uses a separately implemented field \(\mathbb F_9=\mathbb F_3[\alpha]/(\alpha^2+1)\), constructs the \(4\times4\) coordinate matrix for \(B\mapsto AB+BA\) directly, and applies independent Gaussian elimination to count solutions to twenty-two sampled target equations. For every target it visits all \(9^4=6561\) possible first matrices and matches the theorem. These finite computations are corroboration, not a proof for all fields or sizes. Run with `python verify_prime_fields.py` and `python verify_extension.py` in a standard Python 3 environment; no third-party packages are required.

## Relationship to prior work
Bourgeois, *About the matrix function \(X\mapsto AX+XA\)* (arXiv:1210.0766v1, 2012), studies the range of determinant and invertibility properties of the same linear Sylvester map, including a two-by-two real-field determinant-sign classification; its published arguments and scope do not supply targetwise finite-field fiber counts. Kaylor and Offner, *Counting matrices over a finite field with all eigenvalues in the field* (Involve 7, 2014), provide classical similarity and finite-field matrix counts, including the required rational conjugacy ingredients, but not counts of solutions to \(AB+BA=C\). On a 2021 MathOverflow discussion about finite-field anticommuting pairs, contributors derive the **zero-target** anticommuting-pair census in general matrix sizes; that previously known zero case is explicitly not claimed as new. The present contribution is the complete prescribed **nonzero-target** law and its five nonscalar arithmetic strata, not the original Sylvester rank criterion or the classical zero-fiber result. An unlocated general fiber theorem might imply this calculation.

## Limitations
The formulas cover unrestricted ordered matrix pairs only for the full two-by-two matrix algebra in odd characteristic. They do not count conjugacy orbits of factor pairs, constrain factor ranks, extend to higher matrix sizes, or apply in characteristic two. The computational checks are exhaustive only in the stated small prime fields and sample finitely many extension-field targets. Historical priority remains subject to independent literature verification.

## References
- G. Bourgeois, *About the matrix function \(X\mapsto AX+XA\)*, arXiv:1210.0766v1 (first posted 2012-10-02), https://arxiv.org/abs/1210.0766.
- L. Kaylor and D. Offner, *Counting matrices over a finite field with all eigenvalues in the field*, Involve 7 (2014), 627--645, doi:10.2140/involve.2014.7.627, https://msp.org/involve/2014/7-5/involve-v7-n5-p05-p.pdf.
- A. Mellit and other contributors, *Number of anticommuting matrices over finite fields* discussion, MathOverflow question 404817 (2021), https://mathoverflow.net/questions/404817/number-of-3-times-3-anticommuting-matrices-over-finite-fields-mathbbf-p-i.
