# A three-state census of ordered annihilating ideal pairs in radical-square-zero quiver algebras

## Finding
For any finite directed quiver \(Q\), any finite field \(k=\mathbb F_q\), and its arrow ideal \(J\), set \(A=kQ/J^2\). Here loops and parallel and opposite-direction arrows are allowed. Define the bivariate **ordered zero-product ideal census**
\[
\mathcal Z_Q(X,Y)=\sum_{\substack{I,K\triangleleft A\\IK=0}}X^{\dim_k I}Y^{\dim_k K}.
\]
For each ordered pair of vertices \((a,b)\) with \(m=m_{ab}>0\) arrows from \(a\) to \(b\), define the Gaussian subspace enumerator
\[
F_m(T)=\sum_{d=0}^{m}{m\brack d}_q T^d,
\qquad
{m\brack d}_q=\prod_{i=0}^{d-1}\frac{q^{m-i}-1}{q^{d-i}-1}.
\]
Use the states \(0,L,R\) for a vertex selected in neither ideal, in the left ideal, or in the right ideal. Define the following matrix of bivariate polynomials, with rows and columns indexed in that order:
\[
W_m(X,Y)=\begin{pmatrix}
F_m(X)F_m(Y)&X^mF_m(Y)&Y^m\\
X^m&X^m&0\\
F_m(X)Y^m&X^mY^m&Y^m
\end{pmatrix}.
\]
Then **for every finite quiver**, with \(Q_0\) its vertices and with only occupied ordered arrow blocks included in the product,
\[
\boxed{\mathcal Z_Q(X,Y)=
\sum_{c:Q_0\to\{0,L,R\}}
X^{\#c^{-1}(L)}Y^{\#c^{-1}(R)}
\prod_{(a,b):m_{ab}>0}
W_{m_{ab}}(X,Y)_{c(a),c(b)}.}
\]
This is a finite three-state partition function. Its coefficients count individual pairs of two-sided ideals; it is not a count up to isomorphism. Setting \(Y=1\) does **not** give the single-ideal enumerator: one must instead sum over all right ideals, while \(\mathcal Z_Q(X,0)\) **does** give the single-ideal dimension polynomial, because the only dimension-zero ideal is zero.

Two consequences illustrate information beyond a single ideal count. For the three-vertex source fork \(0\to1,\,0\to2\), the ideal-dimension polynomial agrees with that of the reversed sink fork, but
\[
[X^4Y^3]\mathcal Z_Q=1,\qquad [X^3Y^4]\mathcal Z_Q=0,
\]
so the ordered-product census detects orientation. Its total value \(\mathcal Z_Q(1,1)\) is \(69\), independent of the finite field. For two vertices with two parallel arrows in one direction, the total is
\[
\mathcal Z_Q(1,1)=q^2+8q+20.
\]
When every occupied ordered arrow block has multiplicity one, the entire polynomial is independent of field size.

## Assumptions and scope
The quiver is finite, but loops, oriented cycles, and multiple arrows are allowed. The algebra is the ordinary unital quotient of its path algebra by all paths of length at least two (the square of its arrow ideal); it is finite-dimensional with \(\dim_k A=|Q_0|+|Q_1|\). The field \(k\) has any prime-power order \(q\), with no characteristic restriction. The pair \((I,K)\) consists of ordered two-sided \(k\)-subspace ideals and the zero-product condition is \(IK=0\) (not necessarily \(KI=0\)). The sum includes \((0,0)\), \((0,A)\), \((A,0)\), and all intermediate ideals. Only the *reduced* finite set of ideals over the chosen finite field is counted; no assertion is made about ideal schemes.

## Proof
Write \(E_{ab}\) for the vector space spanned by the arrows from vertex \(a\) to vertex \(b\), and \(e_v\) for the vertex idempotents, so that
\[
A=\bigoplus_{v\in Q_0}ke_v\oplus\bigoplus_{a,b\in Q_0}E_{ab},\qquad
J=\bigoplus_{a,b}E_{ab},\qquad J^2=0.
\]
The multiplication rules are \(e_aE_{ab}e_b=E_{ab}\) and all products of two arrows vanish. Every two-sided ideal is uniquely of the form
\[
I(S,U)=\bigoplus_{v\in S}ke_v\oplus\bigoplus_{a,b}U_{ab},\qquad
U_{ab}\le E_{ab},
\]
where \(S\subseteq Q_0\), and \(U_{ab}=E_{ab}\) whenever \(a\in S\) or \(b\in S\). To verify the normal form, project an ideal to the semisimple algebra \(A/J=\bigoplus_v ke_v\) and let \(S\) be the support. If its image contains the coordinate \(e_v\), multiply a representative on the left and right by \(e_v\): this yields \(e_v\) plus possibly loops at \(v\). Multiplication by all incident arrows first forces those loops into the ideal, so subtraction yields \(e_v\) itself. Consequently all incident arrow blocks lie in the ideal. Once all selected \(e_v\) have been removed, multiplication by the vertex idempotents splits the remaining radical subspace into the corner subspaces \(U_{ab}\). Conversely, any such choice is closed under left and right multiplication. The subspaces and the support are recovered uniquely from the ideal.

For two such ideals, \(I=I(S,U)\) and \(K=I(T,V)\), multiplication gives the **exact** decomposition
\[
IK=\bigoplus_{v\in S\cap T}ke_v\ \oplus\
\bigoplus_{a,b}\left(\mathbf1_{a\in S}V_{ab}+\mathbf1_{b\in T}U_{ab}\right).
\]
Therefore \(IK=0\) if and only if \(S\cap T=\varnothing\) and for every occupied block \((a,b)\) both constraints hold: \(a\in S\Rightarrow V_{ab}=0\) and \(b\in T\Rightarrow U_{ab}=0\). At the same time, the ideal normal form forces \(U_{ab}=E_{ab}\) if an endpoint is in \(S\), and likewise \(V_{ab}=E_{ab}\) if an endpoint is in \(T\). Encode \(S,T\) as disjoint three-state vertex colors \(0,L,R\). For a fixed occupied arrow block of dimension \(m\), its nine endpoint-color combinations give, row by row, the products of subspace-count generating polynomials
\[
\left(F_m(X)F_m(Y),\ X^mF_m(Y),\ Y^m\right),\quad
\left(X^m,\ X^m,\ 0\right),\quad
\left(F_m(X)Y^m,\ X^mY^m,\ Y^m\right).
\]
For example the row-\(L\), column-\(R\) case is forbidden because an arrow from a left-selected source to a right-selected target would simultaneously have to generate the entire arrow block and vanish in the product. Distinct ordered arrow blocks impose independent choices. Multiplying their polynomials and the one-dimensional vertex weights and then summing all three-state configurations proves the displayed identity, including loops (where a block uses the same state at both endpoints).

If \(m_{ab}=1\) for every occupied block, \(F_1(T)=1+T\), so the entire sum has integer coefficients independent of \(q\). The fork and two-parallel-arrow specializations follow by evaluating the finitely many (respectively \(3^3\) and \(3^2\)) state assignments; the attached checker independently verifies the fork coefficients and special total counts by exhaustive multiplication in the original algebras over the stated small fields.

## Verification
The supplied file `check_ideal_census.py` constructs the path multiplication table directly for each displayed small quiver over prime fields. It enumerates subspaces by reduced-row-echelon forms, tests closure under left and right multiplication by every basis element, then checks the defining product \(IK=0\) by multiplying all basis-row pairs for each ordered ideal pair. It compares the resulting bivariate count with separately computed vertex-color and corner-subspace counts. The independent three-state matrix evaluation is also compared against the direct enumeration. The full execution output is in `verification_output.txt`.

Exhaustive direct zero-product checks cover a two-loop one-vertex quiver, parallel arrows over \(\mathbb F_2\) and \(\mathbb F_3\), opposite arrows, a single arrow, a three-vertex directed path and a source fork, and a mixed-parallel quiver. Five three-state cases are separately checked. The markers `RADICAL_SQUARE_ZERO_ORDERED_IDEAL_ANNIHILATION_DIRECT_CHECK_PASS` and `THREE_STATE_QUVER_EDGE_MODEL_CHECK_PASS` occur after successful assertions. These finite checks do not prove the all-quiver formula; the preceding decomposition does.

## Relationship to prior work
General ideal-lattice and ideal-product frameworks for finite-dimensional algebras were developed by Catoiu, Chin, and Krop (2003 manuscript). The two-sided ideal normal form and radical-product reduction here are specializations of standard idempotent/corner methods and are not claimed as conceptually new. Aliniaeifard, Behboodi, and Li (arXiv:1411.4159, publicly submitted 2014-11-15) develop directed annihilating-ideal graph constructions and qualitative graph results, but the inspected text does not state the all-quiver finite-field bivariate labeled-ideal-pair polynomial or this explicit three-state weighting. Bekkert and Drozd (arXiv:0812.4818, submitted 2008-12-28) study derived representation types of radical-square-zero algebras rather than this counting invariant. The present claim is restricted to the explicit uniform bivariate census and its orientation-sensitive specialization, not novelty of the underlying ideal-lattice theory.

## Limitations
The formula counts ordered ideal pairs over finite fields, not geometric ideal varieties, isomorphism classes, higher products of ideals, or higher radical powers. It does not determine all features of the zero-product graph beyond its dimension-refined edge counts. An unidentified general enumeration or ideal-semigroup theorem could imply this transfer formula; literature priority has not been independently certified. The verification exercises only small prime fields and quivers. No independent audit has been performed.

## References
1. Stefan Catoiu, William Chin, Leonid Krop, *Two-Sided Ideals of Some Finite-Dimensional Algebras*, manuscript dated 2003-10-04, `https://condor.depaul.edu/wchin/CCK.pdf`. Main text and examples inspected, including general ideal lattice/semigroup results.
2. F. Aliniaeifard, M. Behboodi, Y. Li, *The Annihilating-Ideal Graph of a Ring*, arXiv:1411.4159, initial public submission 2014-11-15, `https://arxiv.org/abs/1411.4159`. Abstract, introduction, graph definitions and principal results inspected.
3. V. Bekkert, Yu. Drozd, *Derived categories for algebras with radical square zero*, arXiv:0812.4818, initial public submission 2008-12-28, `https://arxiv.org/abs/0812.4818`. Abstract and paper's representation-theoretic scope inspected.
