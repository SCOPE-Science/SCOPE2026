# Bivariate rank spectrum of commuting idempotent derivations of full matrix algebras

## Finding
For every prime power \(q\), integer \(n\ge2\), and two *ordered* \(\mathbb F_q\)-linear derivations \(D,E\) of \(M_n(\mathbb F_q)\) with \(D^2=D\), \(E^2=E\), and \(DE=ED\), let
\[
\mathcal C_{n,q}(X,Y)=\sum_{(D,E)}X^{\operatorname{rank}D}Y^{\operatorname{rank}E}.
\]
If \(q\) is odd, \(\mathcal C_{n,q}=1\). If \(q\) is even, define
\[
a_{u,j}(Q)={u\brack j}_Q Q^{j(u-j)}\quad (0\le j\le u),
\qquad g_u(q)=\frac{|\mathrm{GL}_{u}(q)|}{|\mathrm{GL}_{u/2}(q^2)|}
\]
for positive even \(u\), and take \(g_u(q)=0\) for odd \(u\); here \({u\brack j}_Q\) is the Gaussian binomial coefficient. Put \(\rho_n(j)=2j(n-j)\), and
\[
L_n(Y)=1+\sum_{1\le j<n/2}a_{n,j}(q)Y^{\rho_n(j)}
+\mathbf 1_{2\mid n}\frac{a_{n,n/2}(q)+g_n(q)}2Y^{n^2/2},
\]
\[
H_{r,s}(Y)=\frac12\biggl[
\sum_{j=0}^{r}\sum_{k=0}^{s}a_{r,j}(q)a_{s,k}(q)Y^{2(j+k)(r+s-j-k)}
+\mathbf1_{2\mid r,\,2\mid s}g_r(q)g_s(q)Y^{(r+s)^2/2}\biggr]
\]
for positive \(r,s\) with \(r+s=n\), and
\[
K_m(Y)=\frac12\sum_{j=0}^m a_{m,j}(q^2)
\bigl(Y^{8j(m-j)}+Y^{2m^2}\bigr).
\]
Then the **complete bivariate rank polynomial** is
\[
\boxed{\mathcal C_{n,q}(X,Y)=L_n(Y)
+\sum_{1\le r<n/2}a_{n,r}(q)X^{\rho_n(r)}H_{r,n-r}(Y)
+\mathbf1_{2\mid n}X^{n^2/2}
\left[\frac{a_{n,n/2}(q)}2 H_{n/2,n/2}(Y)
+\frac{g_n(q)}2K_{n/2}(Y)\right].}
\]
In terms involving \(n/2\), that value is used only when \(n\) is even. All displayed coefficients are nonnegative integers. The polynomial also obeys \(\mathcal C_{n,q}(X,Y)=\mathcal C_{n,q}(Y,X)\), as is independently clear by interchanging the ordered derivations.

## Assumptions and scope
Derivations are linear over the stated ground field; their ranks are ranks as endomorphisms of the \(n^2\)-dimensional \(\mathbb F_q\)-vector space \(M_n(\mathbb F_q)\). A pair is labeled/ordered, and no quotient by algebra automorphisms is taken. Both zero derivations are allowed. The algebra is the **full associative matrix algebra**, not the abstract Lie algebra \(\mathfrak{gl}_n\); all derivations considered satisfy the ordinary associative Leibniz identity. A Gaussian coefficient with a zero endpoint is one. \(|\mathrm{GL}_{u}(Q)|=\prod_{i=0}^{u-1}(Q^u-Q^i)\), and the order of the zero-dimensional group is one.

## Proof
**1. All derivations are inner, and only characteristic two contributes.** The elementary matrix-unit argument gives every \(\mathbb F_q\)-linear associative derivation as \(D=\operatorname{ad}_A\), with \(D(Z)=AZ-ZA\). Indeed, for the standard matrix units \(E_{ij}\), set \(A=\sum_{i=1}^{n}D(E_{i1})E_{1i}\); the Leibniz rule for \(E_{ij}=E_{i1}E_{1j}\) and \(E_{11}^2=E_{11}\) gives \(D(E_{ij})=[A,E_{ij}]\). Implementing matrices are unique modulo scalar matrices, because the center of the full matrix algebra consists of scalars. For any derivation \(D\) satisfying \(D^2=D\), its eigenspaces \(K=\ker D\) and \(I=\operatorname{im}D\) decompose the algebra. The Leibniz identity gives \(KI+IK\subseteq I\) and \(D(xy)=2xy\) for \(x,y\in I\). In odd characteristic, the possible eigenvalues of \(D\) are zero and one, hence \(I^2=0\). Consequently \(I\) is a two-sided ideal in the simple algebra \(M_n\), so \(I=0\) and \(D=0\).

From now on the field has characteristic two. Direct expansion yields \(\operatorname{ad}_A^2=\operatorname{ad}_{A^2}\). Thus \(\operatorname{ad}_A^2=\operatorname{ad}_A\) exactly when \(A^2+A=cI\) for some \(c\in\mathbb F_q\). The polynomial \(t^2+t+c\) is separable. It splits over \(\mathbb F_q\) exactly when \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(c)=0\), and otherwise is irreducible quadratic.

**2. The single-derivation classification and weights.** In the split case \(A=bI+P\) for a projection \(P^2=P\). Choosing a rank-\(r\) image and a complementary kernel gives \(a_{n,r}(q)={n\brack r}_q q^{r(n-r)}\) labeled projections. On block matrices \(\operatorname{ad}_P\) vanishes on the two diagonal blocks and is identity on the two off-diagonal blocks, so its rank is \(2r(n-r)\). The projections \(P\) and \(I+P\) produce the same derivation; if \(r<n/2\), precisely one has the smaller rank, whereas for \(r=n/2\) every pair is counted twice. The zero case is represented by \(P=0\) or \(P=I\). If \(t^2+t+c\) is irreducible then \(n=2m\) is even. Its conjugacy class has \(g_{2m}(q)\) elements because the centralizer is \(\mathrm{GL}_m(q^2)\), and it has derivation rank \(n^2/2\). There are \(q/2\) such \(c\)'s, while each derivation has exactly \(q\) scalar-related implementers; hence \(g_n(q)/2\) nonsplit derivations. Summing produces \(L_n\), including its first term \(1\).

**3. Commutation is literal commutation of implementers.** For \(D=\operatorname{ad}_A\), \(E=\operatorname{ad}_B\), the commutator \([D,E]=\operatorname{ad}_{[A,B]}\). If \(D\) and \(E\) commute, \([A,B]\) is scalar. But \([A,B]=D(B)\) lies in \(\operatorname{im}D\), while scalar matrices lie in \(\ker D\); since \(D\) is idempotent, these spaces intersect trivially. Hence \([A,B]=0\). The converse is immediate. Thus for fixed \(D\), its commuting idempotent derivations are counted by solutions \(B\) of \(B^2+B=cI\) in the matrix centralizer of \(A\), divided by \(q\) for scalar shifts. This argument also covers \(D=0\), for which the conditional polynomial is \(L_n(Y)\).

**4. Conditional distribution over a split implementer.** Fix \(A=P\) of rank \(r\), with \(s=n-r\). Its centralizer consists of pairs of blocks \(B_r\in M_r(\mathbb F_q)\), \(B_s\in M_s(\mathbb F_q)\). When \(c\) has absolute trace zero, a fixed root \(b\in\mathbb F_q\) identifies solutions of \(B^2+B=cI\) with pairs of projections of ranks \(j,k\). Their multiplicity is \(a_{r,j}(q)a_{s,k}(q)\), and the resulting derivation has rank \(2(j+k)(n-j-k)\) on \(M_n\). When the trace of \(c\) is one, both blocks must have even sizes, and the numbers of irreducible-quadratic matrices on the respective blocks are \(g_r(q)\) and \(g_s(q)\). The resulting derivation has rank \(n^2/2\). Exactly \(q/2\) scalars \(c\) of each trace class occur. Dividing the number of implementing matrices by \(q\), the number of scalar shifts per derivation, gives the displayed \(H_{r,s}(Y)\). Changing \(P\) into \(I+P\) interchanges \(r,s\) but not the conditional polynomial.

**5. Conditional distribution over an irreducible implementer.** Suppose \(n=2m\) and \(A\) induces an \(\mathbb F_{q^2}\)-vector-space structure on the \(n\)-space. Its centralizer is \(M_m(\mathbb F_{q^2})\). For absolute-trace-zero \(c\), choose \(b\in\mathbb F_q\) with \(b^2+b=c\). Every commuting implementing matrix is \(B=bI+Q\), where \(Q\) is an \(\mathbb F_{q^2}\)-linear projection of rank \(j\). There are \(a_{m,j}(q^2)\) choices. Its two eigenspaces on the original \(\mathbb F_q\)-space have dimensions \(2j\) and \(2(m-j)\); therefore \(\operatorname{rank}\operatorname{ad}_B=8j(m-j)\). For absolute-trace-one \(c\), fix \(b\in\mathbb F_{q^2}\setminus\mathbb F_q\) with \(b^2+b=c\). Again \(B=bI+Q\) for some projection \(Q\) over \(\mathbb F_{q^2}\), in exactly \(a_{m,j}(q^2)\) ways at rank \(j\). Under the two embeddings of \(\mathbb F_{q^2}\) into an algebraic closure, the multiplicities of the two roots of \(t^2+t+c\) add to \(m\) each, so \(\operatorname{rank}\operatorname{ad}_B=n^2/2=2m^2\), independently of \(j\). Once more \(q/2\) choices for each trace class and division by \(q\) give \(K_m(Y)\).

**6. Finish.** Partition the first derivation into its zero, split (unbalanced or balanced), and irreducible cases as in Step 2; multiply their cardinalities by the conditional polynomials from Steps 3–5. This gives precisely the boxed formula, with no overlaps and no uncounted cases. Every normalization and its boundaries are explicit in the six steps.

## Verification
The bundled pure-Python script `verify.py` enumerates scalar-normalized implementing matrices over \(\mathbb F_2,\mathbb F_3\), and the genuine extension field \(\mathbb F_4\). It tests the defining quadratic equations, the original Leibniz identity and idempotence for matrix-unit bases, and directly evaluates the commutation equations for small configurations. For \(n=4\) it uses the proved equivalence with commuting implementers after testing the original derivation/idempotence identities on representative matrices. It independently computes the predicted bivariate formula via Gaussian coefficients and general-linear-group orders, and compares every coefficient, not just the total. Its saved output contains:

- \(n=2,q=2\): \(13\) commuting ordered pairs.
- \(n=2,q=4\): \(49\) pairs (using the actual field of four elements).
- \(n=3,q=2\): \(253\) pairs.
- \(n=4,q=2\): \(18169\) pairs.
- Both checked odd-characteristic configurations give only the zero pair.

Running `python3 verify.py` should end with `COMMUTING_IDEMPOTENT_DERIVATION_BIVARIATE_RANK_OK`. Exhaustive finite computations are checks of small cases; the all-dimensional theorem rests on the proof above.

## Relationship to prior work
Caenepeel, Dăscălescu and Năstăsescu provide an earlier general Galois-descent account of finite-abelian-group matrix gradings, including Theorem 3.4 on forms of good gradings up to isomorphism. Their result explains the split-versus-nonsplit picture but does not state an all-dimensional labeled bivariate rank-count formula. Diniz and Pellegrino subsequently count **isomorphism classes** of finite-group gradings (their Theorem 4.3 is over algebraically closed fields), again not the labeled finite-field ordered-pair rank distribution. Khazal, Boboc and Dăscălescu classify gradings of \(M_2(k)\), including characteristic-two \(C_2\)- and Klein-four gradings; in particular, their Theorem 3.1 says every Klein-four grading of \(M_2(k)\) in characteristic two is induced by a cyclic order-two grading. Their isomorphism-level classification covers the low-dimensional grading picture and is fully credited. The present formula counts **all labeled ordered commuting derivation pairs, stratified simultaneously by both ranks, for all \(n\ge2\) and finite fields**, rather than grading-isomorphism types. Commuting idempotent derivations naturally give \((C_2)^2\)-gradings in characteristic two through their joint eigenspaces.

Ayupov and Arzikulov's general matrix-ring derivation results provide related structural background; they do not give these conditional finite-field multiplicities. Bahturin–Zaicev's group-grading work is stated in characteristic zero and does not directly cover the modular count. The recent graded-matrix-algebra identity manuscript by Diniz and collaborators assumes every finite subgroup of the grading group is cyclic, which excludes \((C_2)^2\) as a direct specialization. A publicly indexed prior result involving quadratic polynomials of complex inner derivations concerns a different spectral resonance equation over \(\mathbb C\), not modular commuting idempotents. The combinatorics of centralizers, Grassmannians and finite-field quadratic extensions are classical building blocks, not claimed as discoveries in isolation.

## Limitations
No classification of simultaneous similarity classes of the ordered implementing pairs is claimed; the formula enumerates distinct field-linear derivation pairs as operations on the fixed matrix algebra. The result does not cover arbitrary commuting derivations, higher nilpotence orders, non-field coefficient rings or nonreduced moduli schemes. Generic grading-classification theorems may yield some of the conditional counts after additional work; historical-priority verification is therefore provisional, and no independent mathematical audit has occurred.

## References
1. S. Caenepeel, S. Dăscălescu and C. Năstăsescu, *On gradings of matrix algebras and descent theory*, arXiv:math/0107148v1 (publicly submitted 2001-07-20). Theorem 3.4 classifies forms by Galois descent up to isomorphism.
2. D. Diniz and D. Pellegrino, *On the number of gradings on matrix algebras*, arXiv:2004.02285v1 (2020-04-05). Theorem 4.3 counts isomorphism classes over an algebraically closed field.
3. R. Khazal, C. Boboc and S. Dăscălescu, *Group gradings of \(M_2(k)\)*, Bulletin of the Australian Mathematical Society **68** (2003), 285–293. DOI: 10.1017/S0004972700037667 (publisher online date 2009-04-17).
4. S. Ayupov and F. Arzikulov, *2-Local derivations on matrix rings over associative rings*, arXiv:1303.6033v1 (first submitted 2013-03-25).
5. Y. Bahturin and M. Zaicev, *Group gradings on matrix algebras*, Canadian Mathematical Bulletin **45** (2002). DOI: 10.4153/CMB-2002-031-4.
6. Diniz et al., *Identities and isomorphisms of finite graded matrix algebras*, arXiv:2610.20113 (2026-10-14); abstract inspected, not its full manuscript.
7. *Cyclic-monomial rigidity and necklace count at the quadratic commutator resonance threshold*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cyclic-monomial-rigidity-and-necklace-count-at-the-quadratic-com--4510ac7aff16; complete RESULT inspected for mathematical comparison.
