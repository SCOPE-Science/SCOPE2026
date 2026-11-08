# Cut-support rigidity and exact counts for square-zero derivations of triangular matrix algebras

## Finding

For any field \(k\) with \(\operatorname{char}k\ne2\) and integer \(n\ge2\), square-zero derivations of the associative algebra \(T_n(k)\) of upper-triangular matrices correspond bijectively to matrices supported in a single strictly upper-right rectangular block. Precisely, every such derivation has a unique strictly upper-triangular implementer \(N\), and for some cut \(c\) with \(1\le c<n\), its only possibly nonzero entries satisfy \(i\le c<j\). Conversely, each matrix with that support defines a square-zero derivation \(D(X)=NX-XN\).

The reduced geometric locus has exactly \(n-1\) irreducible components, the linear spaces
\[
U_c=\{N:N_{ij}=0\text{ unless }i\le c<j\}\cong\mathbb A_k^{c(n-c)}.
\]
The intersection of \(U_c\) and \(U_d\), for \(c<d\), is a linear space of dimension \(c(n-d)\). Its largest component dimension is \(\lfloor n^2/4\rfloor\); hence the reduced locus is non-equidimensional for every \(n\ge4\), and is equidimensional for \(n=2,3\).

Over the finite field \(\mathbb F_q\) of odd cardinality \(q\), the exact number of square-zero derivations is
\[
\begin{aligned}
S_n(q)=1+\sum_{1\le a<b\le n}\big(&q^{a(n-b+1)}-q^{(a-1)(n-b+1)}\\
&-q^{a(n-b)}+q^{(a-1)(n-b)}\big).
\end{aligned}
\]
For example, \(S_2(q)=q\), \(S_3(q)=2q^2-q\), \(S_4(q)=q^4+2q^3-2q^2\), and \(S_5(q)=2q^6+q^4-2q^3\). For fixed \(n\), the leading coefficient is \(1\) when \(n\) is even and \(2\) when \(n\ge3\) is odd.

## Assumptions and scope

A derivation here is a \(k\)-linear map \(D:T_n(k)\to T_n(k)\) satisfying \(D(XY)=D(X)Y+XD(Y)\). Square-zero means the composition \(D\circ D\) vanishes on all of \(T_n(k)\). This is *not* the condition \(N^2=0\) on the implementing matrix. Matrix units are \(E_{ij}\), where \(1\le i\le j\le n\). The zero derivation occurs once, despite lying in every component. Statements on reduced geometric components mean the reduced variety over an algebraic closure, not a claim about the nonreduced scheme structure of the defining equations.

## Proof

**Every derivation is inner.** Put \(e_i=E_{ii}\). Given a derivation \(D\), set \(X=\sum_i D(e_i)e_i\). The derivation identity and \(e_ie_j=\delta_{ij}e_i\) give \([X,e_i]=D(e_i)\). Thus \(D-\operatorname{ad}_X\) vanishes on every \(e_i\) and consequently sends each \(E_{ij}=e_iE_{ij}e_j\) to a scalar multiple \(a_{ij}E_{ij}\). The identity \(E_{ij}E_{j\ell}=E_{i\ell}\) gives \(a_{i\ell}=a_{ij}+a_{j\ell}\). Hence there are scalars \(h_i\) with \(a_{ij}=h_i-h_j\), so the remaining derivation equals \(\operatorname{ad}_{\operatorname{diag}(h_1,\ldots,h_n)}\). The center of \(T_n(k)\) is exactly \(kI\), so the implementer is unique modulo scalars.

**Scalar diagonal is forced.** If \(D=\operatorname{ad}_Y\) has \(D^2=0\), its action on the \((i,i+1)\) entry of \(E_{i,i+1}\) has square \((Y_{ii}-Y_{i+1,i+1})^2\). It follows that all diagonal entries of \(Y\) coincide. Subtracting a scalar matrix yields a *unique* strictly upper-triangular implementer \(N\).

**Reduction to a two-sided sandwich.** In every characteristic,
\[
(\operatorname{ad}_N)^2(X)=N^2X-2NXN+XN^2.
\]
Taking its \((a,b)\)-entry on \(X=E_{aa}\), where \(a<b\), shows that \((N^2)_{ab}=0\). Since \(N^2\) is strictly upper triangular, \(N^2=0\). In characteristic different from two, therefore, \(D^2=0\) is equivalent to \(NXN=0\) for every \(X\in T_n(k)\). For matrix units \(E_{ij}\), \(i\le j\), the \((a,b)\)-entry of \(NE_{ij}N\) is exactly \(N_{ai}N_{jb}\). No sum or cancellation occurs here.

Let \(\alpha\) be the greatest row index of a nonzero entry of \(N\), and let \(\beta\) be the least column index of a nonzero entry. If \(N\ne0\), the preceding product test says that every nonzero-entry column is strictly greater than every nonzero-entry row; this is precisely \(\alpha<\beta\). Choosing any integer \(c\) with \(\alpha\le c<\beta\) gives the required cut. Conversely, for a cut-supported \(N\), all possible entries of \(N X N\) vanish for every upper-triangular \(X\), because a nonzero product would require a column of \(N\) not exceeding a row of \(N\). This proves the classification.

**Components and intersections.** The equations defining \(D^2=0\) have, over every extension field of odd characteristic, precisely the union \(\bigcup_{c=1}^{n-1} U_c\) as their solution set. Each \(U_c\) is linear and irreducible of dimension \(c(n-c)\); it cannot be contained in any other \(U_d\) since the unit \(E_{c,c+1}\) belongs to \(U_c\) and to no \(U_d\) with \(d\ne c\). For \(c<d\), common support requires \(i\le c\) and \(j>d\), yielding \(c(n-d)\) coordinates. The dimension and parity statements follow by maximizing \(c(n-c)\).

**Exact point count.** Every nonzero cut-supported matrix has unique extrema \(a=\alpha\) and \(b=\beta\), with \(1\le a<b\le n\). All its coordinates lie in the \(a\)-by-\((n-b+1)\) rectangle of rows \(1,\ldots,a\) and columns \(b,\ldots,n\). Inclusion-exclusion imposes at least one nonzero entry in row \(a\) and at least one in column \(b\), giving
\[
q^{a(n-b+1)}-q^{(a-1)(n-b+1)}-q^{a(n-b)}+q^{(a-1)(n-b)}.
\]
Summing over the mutually disjoint extrema and adding \(N=0\) proves the formula. Since \(N\mapsto\operatorname{ad}_N\) is injective on strictly upper-triangular matrices, these count distinct derivations, not merely matrices modulo a group action.

**Sharp characteristic-two boundary.** If \(\operatorname{char}k=2\), then \((\operatorname{ad}_N)^2=\operatorname{ad}_{N^2}\), and \(N^2\) is strictly upper-triangular. Since the center of \(T_n(k)\) is scalar, square-zero is then equivalent to \(N^2=0\). At \(n=4\), the matrix \(N=E_{12}+E_{34}\) satisfies \(N^2=0\), while \(\max\{1,3\}=3\not<2=\min\{2,4\}\), so no common cut exists. Dimensions \(2\) and \(3\) have no such exception because direct multiplication leaves only the two rectangular cut spaces. Thus \(n=4\) is the first failure dimension.

## Verification

Run `python3 checker.py` using standard Python 3, with no third-party dependencies. The script constructs the full commutator maps on the basis of upper-triangular matrix units, composes them, and compares *each* candidate against the cut-support criterion and counting formula. Exhaustive odd-field tests cover \((n,q)=(2,3),(3,3),(4,3),(4,5),(5,3)\), totaling \(75{,}433\) distinct candidate matrices; the characteristic-two counterexample is checked by direct commutator composition. See `verification_output.txt` for recorded results. This finite verification corroborates, but does not replace, the proof for arbitrary fields and dimensions.

## Relationship to prior work

Guo and Li's 2010 work on derivations of path algebras provides a broad canonical-basis and Lie-algebra framework for the algebra of a linearly oriented chain; the present result instead classifies the nonlinear condition \(D^2=0\), determines its reduced component arrangement, and counts its points over finite fields. Ekhad and Zeilberger's 1995 exact enumeration concerns square-zero upper-triangular **matrices** \(N^2=0\). That condition is weaker than \((\operatorname{ad}_N)^2=0\) in odd characteristic, so their numerical census does not directly give this one; it does count the corresponding characteristic-two case. Hu's 2022 theorem uses the distinct concept of *strong ad-nilpotence*, defined through nonzero eigenspaces of other adjoint maps, not square-zero adjoint operators. Mattarei's 2022 paper supplies the standard *sandwich element* terminology and studies thin Lie algebras rather than finite-dimensional upper-triangular algebras.

## Limitations

The result does not classify higher nilpotence indices, square-zero derivations of arbitrary incidence algebras, nonreduced scheme structures, or conjugacy classes. No independently validated historical-priority claim is made. A general unpublished or unlocated classification of sandwich elements in Borel Lie algebras could already imply some or all of the geometric statement; the exact finite-field census is also potentially an elementary consequence of such a theorem. The characteristic-two case is distinguished but not newly enumerated here.

## References

1. Li Guo and Fang Li, *Structure of Hochschild cohomology of path algebras and differential formulation of Euler's polyhedron formula*, arXiv:1010.1980v1 (first public version 2010-10-11); https://arxiv.org/abs/1010.1980.
2. Shalosh B. Ekhad and Doron Zeilberger, *The Number of Solutions of \(X^2=0\) in Triangular Matrices Over \(GF(q)\)*, Electronic Journal of Combinatorics 3 (1996), R2; published record 1995-12-01; https://doi.org/10.37236/1226.
3. Zhiguang Hu, *Strongly Ad-Nilpotent Elements of the Lie Algebra of Upper Triangular Matrices*, Journal of Mathematics 2022, 3484381; https://doi.org/10.1155/2022/3484381.
4. Sandro Mattarei, *A sandwich in thin Lie algebras*, Proceedings of the Edinburgh Mathematical Society 65 (2022), 136–145; https://doi.org/10.1017/S0013091521000845.
