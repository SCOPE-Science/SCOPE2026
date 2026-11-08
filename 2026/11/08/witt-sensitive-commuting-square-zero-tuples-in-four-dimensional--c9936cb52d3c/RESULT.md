# Witt-sensitive commuting square-zero tuples in four-dimensional orthogonal Lie algebras

## Finding
Let \(k=\mathbb F_q\) be a finite field of odd order and let \((V,B)\) be a nondegenerate symmetric bilinear space of dimension four. For every integer \(r\ge2\), let
\[
\mathcal X_r(V)=\{(X_1,\ldots,X_r)\in\mathfrak{so}(V)^r:\ X_i^2=0,\ [X_i,X_j]=0\text{ for all }i,j\}.
\]
In the split case (Witt index two), the exact ordered-tuple count is
\[
\boxed{\#\mathcal X_r(V)(\mathbb F_q)=1+2(q+1)(q^r-1)+(q+1)^2\bigl((2q-1)^r-2q^r+1\bigr).}
\]
The number of tuples for which **every** pairwise product \(X_iX_j\) is zero is \(1+2(q+1)(q^r-1)\); the remaining \((q+1)^2((2q-1)^r-2q^r+1)\) tuples have at least one nonzero product. Each nonzero product has rank one. In the nonsplit case (Witt index one), the zero tuple is the **only** \(\mathbb F_q\)-rational point.

Over an algebraic closure \(\bar k\), independently of the finite-field Witt type, the underlying reduced variety \(\mathcal X_r(V)_{\bar k}^{\mathrm{red}}\) has exactly \(2^r\) geometrically irreducible components. Exactly two have dimension \(r+1\), and the other \(2^r-2\) have dimension \(r+2\). Thus the square-zero commuting tuple variety is non-equidimensional for every \(r\ge2\). In the nonsplit case Frobenius exchanges complementary-index components in pairs, yielding \(2^{r-1}\) irreducible components over \(\mathbb F_q\), each geometrically reducible, despite having only one rational point in the entire variety.

The formula has a finer support interpretation. In the split case, the nonzero operators form two families, each indexed by a projective conic of \(q+1\) directions with \(q-1\) nonzero scalar representatives per direction. For any disjoint, nonempty index sets \(S,T\subseteq\{1,\ldots,r\}\), there are exactly \((q+1)^2(q-1)^{|S|+|T|}\) tuples supported on the first and second families at indices \(S\) and \(T\), respectively, and zero elsewhere. Two nonzero tuple entries have nonzero product exactly when their indices belong to opposite families.

## Assumptions and scope
The algebraic geometric statements hold over any field of characteristic different from two after base change to an algebraic closure; the split/nonsplit arithmetic enumeration concerns finite fields of odd cardinality. The variety is defined by the literal matrix-square and ordinary Lie-commutator equations in the natural four-dimensional orthogonal representation, not by the restricted Lie \(p\)-power alone. Component assertions concern the underlying reduced variety; no scheme-theoretic multiplicity claim is made. For split finite quadratic spaces, Witt index is two; nonsplit spaces have Witt index one. The same statements hold for every odd prime power, not just prime fields.

## Proof
**1. The split tensor model.** Let \(W_1=W_2=k^2\) with their standard nondegenerate alternating forms \(\omega_1,\omega_2\). The tensor product form \(B=\omega_1\otimes\omega_2\) on \(V=W_1\otimes W_2\) is nondegenerate, symmetric, and split. In characteristic different from two, the map
\[
\mathfrak{sl}(W_1)\oplus\mathfrak{sl}(W_2)\longrightarrow\mathfrak{so}(V),\qquad
(A,D)\longmapsto A\otimes I+I\otimes D
\]
is injective: a tensor equality \(A\otimes I=-I\otimes D\) forces both endomorphisms to be scalar, hence zero because they are traceless. Both sides have dimension six, so it is an isomorphism of Lie algebras. The two summands are commuting ideals. Every traceless \(2\times2\) matrix has scalar square by Cayley--Hamilton. Accordingly, for \(X=A\otimes I+I\otimes D\),
\[
X^2=(\alpha+\beta)I\otimes I+2A\otimes D,
\qquad A^2=\alpha I,\ D^2=\beta I.
\]
Partial trace over either factor gives \(\alpha+\beta=0\) if \(X^2=0\), since the trace of \(A\) and \(D\) is zero and two is invertible. It follows that \(A\otimes D=0\), so \(A=0\) or \(D=0\), and the remaining factor is square-zero. Hence the nonzero square-zero elements of \(\mathfrak{so}(V)\) lie in precisely one of the two ideals.

**2. Commutation in a factor.** For any nonzero square-zero \(A\in\mathfrak{sl}_2(k)\), the centralizer \(C_{\mathfrak{sl}_2}(A)\) is exactly \(kA\), as is checked in a basis with \(A=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\). Thus all nonzero square-zero entries of a commuting tuple lying in the same ideal are scalar multiples of a single nilpotent direction. Entries from opposite ideals commute automatically. Their ordinary matrix product is \(A\otimes D\), which is nonzero of rank one whenever both factors are nonzero. A product within the same ideal is zero because its two factors are scalar multiples of a square-zero matrix. This proves the complete support/product description.

**3. Finite-field count.** A traceless \(2\times2\) matrix \(\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)\) is square-zero exactly when \(a^2+bc=0\). The projectivization of the nonzero solutions is a nonsingular conic with \(q+1\) rational points; every direction contains \(q-1\) nonzero matrices. The tuple with all entries zero contributes one. Tuples supported on exactly one ideal contribute \(2(q+1)(q^r-1)\). When both ideals occur, choose one nilpotent line in each, obtaining \((q+1)^2\) choices. At each index there are \(2q-1\) possibilities (zero or a nonzero scalar from exactly one line). Requiring each line to occur gives by inclusion-exclusion \((2q-1)^r-2q^r+1\) scalar patterns. This proves the claimed total and its two-product refinement, including the exact count for prescribed labeled index supports.

**4. The nonsplit arithmetic obstruction.** For any skew-adjoint endomorphism \(X\), the matrix \(BX\) is alternating, so \(\operatorname{rank}X\) is even. If \(X^2=0\), then \(B(Xv,Xw)=-B(v,X^2w)=0\); hence \(\operatorname{im}X\) is totally isotropic. A nonsplit four-dimensional quadratic space over \(\mathbb F_q\) has Witt index one. It can therefore contain no nonzero even-dimensional totally isotropic image, so \(X=0\). This establishes the nonsplit count without relying on any computational search.

**5. Geometric components and descent.** Work over an algebraic closure, where every nondegenerate symmetric four-space is split. For \(m\ge1\), define
\[
\mathcal C_m=\{(A_1,\ldots,A_m)\in\mathfrak{sl}_2^m:\ A_i^2=0,\ [A_i,A_j]=0\}.
\]
Every nonzero tuple has the form \((c_1N,\ldots,c_mN)\) for one nonzero nilpotent \(N\). Its projectivization is the image of \(\mathbb P^1\times\mathbb P^{m-1}\) under the line bundle \(\mathcal O(2,1)\): the first factor parametrizes the nilpotent conic, the second the scalar direction. Thus \(\mathcal C_m\) is an irreducible affine cone of dimension \(m+1\). Put \(\mathcal C_0=\{0\}\). For each subset \(S\subseteq\{1,\ldots,r\}\), form the closed subvariety \(Z_S\) of commuting square-zero tuples whose entries lie in the first ideal at positions \(S\), and the second ideal at positions outside \(S\). Then
\[
Z_S\cong\mathcal C_{|S|}\times\mathcal C_{r-|S|}.
\]
By Step 1, their union exhausts the reduced solution variety. Every \(Z_S\) is irreducible, and each contains a tuple all of whose entries are nonzero; no such generic tuple lies in any \(Z_T\) with \(T\ne S\). Hence the \(Z_S\) are exactly the \(2^r\) irreducible components. For \(S\) empty or full, the dimension is \(r+1\); otherwise it is \((|S|+1)+(r-|S|+1)=r+2\). In a nonsplit four-space over a finite field, the two rulings of the associated quadric become defined over \(\mathbb F_{q^2}\) and are exchanged by Frobenius. They give the two ideals after algebraic closure, so Frobenius maps \(Z_S\) to \(Z_{S^c}\). All orbits on the component set have size two; therefore there are exactly \(2^{r-1}\) irreducible components over \(\mathbb F_q\), none geometrically irreducible. These statements concern reduced varieties and do not require smoothness of their cone vertices.

## Verification
The standalone `check.py` explicitly enumerates the six free coefficients of every skew-adjoint four-by-four matrix for both Witt types over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). It computes literal squares, commutators, products and ranks, and exhaustively enumerates commuting tuples up to length four, three, and two respectively. All cases agree with the total and zero-product predictions. In particular, for \(r=2\) the split counts are \(193,1441,5377\), and the nonsplit count is one, at field orders three, five, seven respectively. At \(q=3\), the total numbers for lengths three and four are \(1361\) and \(8065\). The program also checks that every nonzero square-zero skew-adjoint matrix has rank two and that every commuting product has rank zero or one.

Run `python3 check.py` from the package directory to reproduce the checks. `check_output.txt` contains its complete recorded output. These exhaustive computations are finite tests, not proofs for all prime powers or of the component assertions; the preceding algebraic argument establishes the full theorem.

## Relationship to prior work
Premet's 2003 work proves equidimensionality of the **unrestricted nilpotent commuting-pair variety** of a reductive Lie algebra in good characteristic. Imposing the stronger literal square-zero equations in the natural orthogonal representation produces the distinct, non-equidimensional geometry classified here. Schröer's 2004 classification concerns unrestricted matrix pairs satisfying mutual annihilation and nilpotence, not orthogonal skew-adjoint commuting tuples with their possible nonzero products. Fulman and Guralnick's 2016 preprint enumerates commuting pairs in several classical Lie algebras and states that orthogonal cases are not treated there. Boos, Cerulli Irelli and Esposito study parabolic and Borel orbits of individual square-zero elements in classical Lie algebras; their classification is not an enumeration or component decomposition of arbitrary-length commuting tuples. Guralnick and Ngo study unrestricted nilpotent commuting tuples of full general linear matrices; their statements do not determine the orthogonal square-zero refinement. These works supply background and potentially relevant general constructions; the classification here does not assert priority over all related literature.

## Limitations
The arithmetic formulas require odd-characteristic finite fields and dimension four. Characteristic two, higher-dimensional orthogonal spaces, unit-group conjugacy class counts, and nonreduced scheme multiplicities are not covered. The geometric decomposition is for reduced varieties. No independent mathematical or historical-priority assessment has been performed. The tensor-model technique uses classical structure theory of type \(D_2\); an unidentified more general finite-field orbit or commuting-scheme theorem could imply the formulas.

## References
1. A. Premet, *Nilpotent commuting varieties of reductive Lie algebras*, arXiv:math/0302204, first public preprint 2003-02-18; Invent. Math. 154 (2003), 653–683.
2. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, Comment. Math. Helv. 79 (2004), 396–426, DOI:10.1007/S00014-003-0788-3.
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499, first public preprint 2016-11-16.
4. M. Boos, G. Cerulli Irelli and F. Esposito, *Parabolic orbits of 2-nilpotent elements for classical groups*, arXiv:1802.06425, first public preprint 2018-02-18, especially §§2 and 6.2.
5. R. Guralnick and N. V. Ngo, *Reducibility of nilpotent commuting varieties*, arXiv:1308.2420, first public preprint 2013-08-11.
