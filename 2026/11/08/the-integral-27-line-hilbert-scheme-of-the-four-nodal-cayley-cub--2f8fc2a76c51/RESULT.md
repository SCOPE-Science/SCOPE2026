# The integral 27-line Hilbert scheme of the four-nodal Cayley cubic

## Finding

Let \(\mathcal X\subset\mathbb P^3_{\mathbb Z}\) be the projective cubic surface with integral defining equation
\[
X_0X_1X_2+X_0X_1X_3+X_0X_2X_3+X_1X_2X_3=0.
\]
Its complete relative Hilbert scheme \(\mathcal F=\operatorname{Hilb}^{t+1}(\mathcal X/\mathbb Z)\) of projective lines admits the following **integral isomorphism of finite schemes**:
\[
\boxed{\mathcal F\simeq
\coprod_{3}\operatorname{Spec}\mathbb Z\ \sqcup\
\coprod_{6}\operatorname{Spec}\mathbb Z[u,v]/(u^2,v^2).}
\]
The six length-four factors correspond to the coordinate-edge lines joining the four ordinary double points, while the three reduced factors correspond to the diagonal lines cut out by equations \(X_i+X_j=X_k+X_l=0\), for partitions of the four indices into two pairs. In particular, the scheme is finite flat of rank \(27\) over \(\mathbb Z\), despite having exactly nine geometric support points in every characteristic. Each nonreduced local fiber has Hilbert function \((1,2,1)\), embedding dimension two, and length four. All statements hold over every field, including characteristics two and three, by base change.

## Assumptions and scope

The displayed integer equation is fixed; the assertion concerns its relative line Hilbert scheme, not merely the reduced set of lines or the Fano scheme of a smooth cubic. The universal Grassmannian \(G=\operatorname{Gr}(2,4)_{\mathbb Z}\) parametrizes lines in \(\mathbb P^3_{\mathbb Z}\). The relative Hilbert scheme \(\mathcal F\) is the zero scheme in \(G\) of the section of \(\operatorname{Sym}^3(\mathcal S^\vee)\) obtained by restricting the cubic, where \(\mathcal S\) is the universal rank-two subbundle. A geometric support point means a closed point after passing to an algebraic closure; the Artin local algebras record the scheme-theoretic collision multiplicities.

## Proof

### 1. Exhaustion of geometric lines, in every characteristic

Fix an algebraically closed field \(k\), including any positive characteristic. Project from the coordinate point \(P=[1:0:0:0]\). With \(x=X_0\) and \((y,z,w)=(X_1,X_2,X_3)\), the equation is
\[
xQ(y,z,w)+C(y,z,w)=0,\qquad
Q=yz+yw+zw,\quad C=yzw.
\]
The conic \(Q=0\) is smooth over every \(k\): if the three partial derivatives vanish simultaneously, then in characteristic two they force \(y=z=w\), at which point \(Q\ne0\), and in all other characteristics the gradient has no nonzero common root. The scheme \(V(Q,C)\subset\mathbb P^2_k\) has length six and is supported at exactly the three coordinate points, each of local length two. The three distinct lines on \(\mathcal X_k\) through \(P\) are its three coordinate-edge lines.

A line \(L\subset\mathcal X_k\) not containing \(P\) projects isomorphically onto some line \(\ell\subset\mathbb P^2_k\), and the coordinate \(x\) on \(L\) is a linear form \(h\) on \(\ell\). Thus \(C|_\ell=-hQ|_\ell\). Because a smooth conic contains no line, the length-two divisor \(Q\cap\ell\) is a sub-divisor of \(V(Q,C)\); it is therefore either the sum of two distinct coordinate points or twice one coordinate point. In the first case, \(\ell\) is a coordinate line and its linear lift is the corresponding coordinate-edge line. In the second case, \(\ell\) is the unique tangent to \(Q\) at that coordinate point, and its unique lift is one of the three diagonal lines, e.g. \(x+y=z+w=0\). This gives precisely six edges and three diagonals over \(k\); the argument did not divide by \(2\) or \(3\).

### 2. Six explicit length-four infinitesimal families

Consider the edge spanned by the first two standard basis vectors. A Grassmannian chart near it parametrizes lines spanned by
\[
(1,0,a,b),\qquad (0,1,c,d).
\]
Expanding the cubic on a general point of this line gives its four coefficient equations
\[
ab=0,\qquad
a+b+ab+ad+bc=0,\qquad
c+d+ad+bc+cd=0,\qquad cd=0.
\]
There is a closed immersion of \(\operatorname{Spec}R\) into this chart of \(\mathcal F\), where \(R=\mathbb Z[u,v]/(u^2,v^2)\), specified by
\[
\boxed{a=u,\quad c=v,\quad b=-u+2uv,\quad d=-v+2uv.}
\]
Direct substitution makes all four coefficient equations vanish modulo \((u^2,v^2)\), and the map of coordinate rings is surjective because \(a,c\) map to \(u,v\). Thus this is a genuine **integral** length-four closed subscheme, not just a tangent-space estimate. Every other edge is obtained by a permutation of the four coordinates, giving six pairwise disjoint closed subschemes of rank four.

### 3. Three reduced line sections

For the diagonal \(X_0+X_1=X_2+X_3=0\), use the line basis \(e_0-e_1,e_2-e_3\) and complementary vectors \(e_0,e_2\). The Jacobian matrix of the four restricted-cubic coefficients with respect to the Grassmannian chart deformation coordinates at the given line is, after the corresponding row and column ordering,
\[
\begin{pmatrix}
0&-1&0&0\\
0&0&0&-1\\
-1&0&0&0\\
0&0&-1&0
\end{pmatrix},
\]
with determinant \(-1\). The same calculation for the other two diagonal pairings gives determinant \(-1\). Consequently each diagonal is a reduced \(\operatorname{Spec}\mathbb Z\) section of \(\mathcal F\) in every characteristic. Together with the edge factors we have constructed a closed subscheme \(T\subset\mathcal F\), finite flat of total rank \(3+6\cdot4=27\) over \(\mathbb Z\).

### 4. The top Chern number proves completeness and flatness

For each algebraically closed field \(k\), Step 1 shows the zero scheme \(\mathcal F_k\) is supported on nine points and hence has dimension zero. The Grassmannian \(G_k\) is smooth of dimension four, and \(\operatorname{Sym}^3(\mathcal S^\vee)\) has rank four. Thus the four equations are a regular sequence at every point of \(\mathcal F_k\), and its scheme-theoretic length equals the top Chern number. If \(\alpha,\beta\) are the formal Chern roots of \(\mathcal S^\vee\), then
\[
c_4(\operatorname{Sym}^3\mathcal S^\vee)
=(3\alpha)(2\alpha+\beta)(\alpha+2\beta)(3\beta),
\]
and the Grassmannian residue/Schubert coefficient formula gives
\[
\int_{G_k} c_4
=[\alpha^3\beta^2]\, (\alpha-\beta)
(3\alpha)(2\alpha+\beta)(\alpha+2\beta)(3\beta)=27.
\]
Every geometric fiber therefore has **exact total scheme length 27**, in all characteristics. The nine closed subschemes of \(T_k\) already contribute exactly this length, so \(T_k=\mathcal F_k\) scheme-theoretically.

The morphism \(\mathcal F\to\operatorname{Spec}\mathbb Z\) is proper because \(\mathcal F\) is closed in the projective Grassmannian, and is quasi-finite by Step 1; hence it is finite. The closed immersion \(T\hookrightarrow\mathcal F\) induces a surjection of finite \(\mathbb Z\)-algebras \(\mathcal O_\mathcal F\twoheadrightarrow\mathcal O_T\). Since \(\mathcal O_T\) is free of rank 27, its kernel commutes with every residue-field base change (vanishing \(\operatorname{Tor}_1\)); the kernel is zero after every such base change by the fiberwise length equality, and hence vanishes by Nakayama. Therefore \(\mathcal F=T\) integrally. The claimed isomorphism and finite flatness follow.

## Verification

Run `python3 verify_cayley.py` using standard Python 3, without external packages. The test computes the six-fold symmetric edge fat family in the truncated integer ring, the three integral Jacobian determinants, and the Schubert coefficient \(27\). It also enumerates **all** Grassmannian points over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), finding precisely nine Cayley lines among \(35,130,806\) respective candidate projective lines. The actual recorded output is in `verification_output.txt` and ends with `ALL_CHECKS_PASSED`. These finite-field examples corroborate, but do not replace, the geometric classification and Chern-class proof valid over all fields.

## Relationship to prior work

The reduced list of nine lines is classical; Heath-Brown's 2002 article on rational points of the Cayley cubic explicitly lists six coordinate edges and three diagonals. Derenthal, Hausen, Heim, Keicher and Laface (2014) tabulate nine reduced lines for the \(4A_1\) cubic and calculate Cox rings of its minimal resolution in characteristic zero. These results supply the reduced geometry but do not state the relative Hilbert scheme over \(\mathbb Z\), its local Artin ring structures, or its all-characteristic finite-flat decomposition in the inspected full-text material. The rank-27 top Chern computation is a standard enumerative mechanism, not a new claim of 27 lines on a smooth cubic. The contribution here is **the exact integral nilpotent scheme structure of the nine-point degeneration**.

## Limitations

The result pertains to the fixed primitive integral Cayley cubic equation and the Hilbert polynomial \(t+1\). It does not classify degenerations of arbitrary cubic families or their monodromy. Historical priority of the explicit local Artin-algebra description remains provisional pending specialist archival review; the absence of a textual match is not a proof of novelty. The supplied exact arithmetic program is not an independent scientific audit or a full symbolic-algebra certification; the printed derivation above is the proof.

## References

1. D. R. Heath-Brown, *The Density of Rational Points on Cayley's Cubic Surface*, arXiv:math/0210333, first posted 21 October 2002, especially Section 1 and the description of the nine lines. https://arxiv.org/abs/math/0210333 .
2. U. Derenthal, J. Hausen, A. Heim, S. Keicher, A. Laface, *Cox rings of cubic surfaces and Fano threefolds*, arXiv:1409.0799, first posted 2 September 2014, Section 3 (Table 1 and the \(4A_1\) case). https://arxiv.org/abs/1409.0799 .
