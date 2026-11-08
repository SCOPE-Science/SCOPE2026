# Arithmetic incidence and zeta function of the Clebsch cubic's line complement

## Finding
Let \(q\) be a prime power of characteristic \(p>5\). The Clebsch diagonal cubic surface is
\[
X: \sum_{i=0}^{4}X_i=\sum_{i=0}^{4}X_i^3=0\subset\mathbf P^4_{\mathbb F_q}.
\]
Let \(U\) be its complement of the union of **all 27 geometric lines** (not only the rational lines), and let \(\varepsilon\) denote the quadratic character of \(5\) in \(\mathbb F_q\). For each integer \(n\ge1\), put \(Q=q^n\) and \(e=\varepsilon^n\). Write \(N_j(Q)\) for the number of \(\mathbb F_Q\)-points of \(X\) belonging to exactly \(j\) distinct geometric lines. The complete spectrum is

| \(e\) | \(N_0(Q)\) | \(N_1(Q)\) | \(N_2(Q)\) | \(N_3(Q)\) |
|:--:|:--|:--|:--|:--|
| \(+1\) | \(Q^2-20Q+99\) | \(27Q-213\) | \(105\) | \(10\) |
| \(-1\) | \(Q^2-10Q+21\) | \(15Q-45\) | \(15\) | \(10\) |

No point lies on more than three geometric lines. In particular, \(\#U(\mathbb F_q)=0\) **if and only if** \(q\in\{7,11\}\) within the stated characteristic range. The complete Hasse–Weil zeta function \(Z(U,T)=\exp(\sum_{n\ge1}\#U(\mathbb F_{q^n})T^n/n)\) is
\[
Z(U,T)=\begin{cases}
\displaystyle\frac{(1-qT)^{20}}{(1-q^2T)(1-T)^{99}},&\varepsilon=+1,\\[6pt]
\displaystyle\frac{(1-qT)^{15}(1+qT)^5}{(1-q^2T)(1-T)^{60}(1+T)^{39}},&\varepsilon=-1.
\end{cases}
\]
The split-case ground-field complement count follows already from classical split-line incidence formulas; the nonsplit geometric-line complement, the full multiplicity distribution over every extension, and the corresponding two zeta-function formulas are the specific assertions investigated here.

## Assumptions and scope
The base field is \(\mathbb F_q\), \(p=\operatorname{char}(\mathbb F_q)>5\); arbitrary prime powers are allowed. All point counts are for the fixed displayed rational model, not for twists, and \(U\) removes the full geometric exceptional divisor. The quadratic character has values \(\pm1\) since \(p\ne5\). The condition \(e=+1\) is equivalent to \(Q\equiv\pm1\pmod5\), while \(e=-1\) is equivalent to \(Q\equiv\pm2\pmod5\).

## Proof
**1. Smoothness and the 27 lines.** A singular point of the cubic in the hyperplane \(\sum X_i=0\) would satisfy \(3X_i^2=c\) for all five coordinates. Over an algebraic closure the coordinates would therefore equal \(\pm a\). The sum of five signs is one of \(\pm1,\pm3,\pm5\); it cannot be zero when \(p>5\), so the cubic is smooth. Its 27 lines split into 15 *diagonals*: for a zero-coordinate index and a matching of the other four indices, set their coordinates \((a,-a,b,-b,0)\). The remaining twelve lines arise from the permutation orbit of the span of the vectors \(v_1=(\zeta^i)_{i=0}^4\) and \(v_4=(\zeta^{4i})_{i=0}^4\), where \(\zeta\) is a primitive fifth root of unity. The cubic vanishes on these spans by the sums of fifth roots, and the resulting 12 distinct spans plus the 15 diagonals exhaust the classical 27 lines of a smooth cubic surface. The coefficients of the 12 lines lie in the quadratic subfield of the fifth cyclotomic extension, and Frobenius acts on them trivially precisely when \(Q\equiv\pm1\pmod5\).

**2. Nonrational lines contain no rational points in the nonsplit case.** When \(Q\equiv\pm2\pmod5\), the Frobenius image of \(\langle v_1,v_4\rangle\) is \(\langle v_2,v_3\rangle\). These two lines are disjoint: the four vectors are linearly independent by the Fourier/Vandermonde determinant, whose fifth-root factors remain distinct in characteristic different from five. This is preserved under all coordinate permutations. Thus every nonrational line is exchanged with a *skew* partner, and any \(\mathbb F_Q\)-point on such a line would have to lie on both, which is impossible. Only the 15 diagonal lines can contain rational points in this case.

**3. Diagonal-line incidence.** Any diagonal meets exactly six other diagonals, at four distinct points: two Eckardt points, each shared by three diagonals, and two ordinary double-line points. Globally this gives ten points shared by three diagonals and fifteen points shared by two. One can check the statement directly by solving two sets of linear equations for the 15 explicitly parameterized diagonals, or equivalently using the strongly regular diagonal incidence graph with parameters \((15,6,1,3)\). Accordingly, for nonsplit \(Q\), the total line-point incidence count is \(15(Q+1)\), while triple and double points contribute \(3\cdot10+2\cdot15\) incidences. Hence \(N_1=15Q-45\), \(N_2=15\), and \(N_3=10\).

In the split case, every geometric line is rational, and a cubic-surface line meets ten of the other 26 lines. There are \(27\cdot10/2=135\) meeting line-pairs, of which \(3\cdot10=30\) are realized at the ten Eckardt points; the remaining 105 pairs meet at distinct ordinary double points. Therefore \(N_3=10\), \(N_2=105\), and \(N_1=27(Q+1)-3\cdot10-2\cdot105=27Q-213\).

**No exceptional-characteristic increase in the ten Eckardt points.** To justify the geometric triple count uniformly in characteristic \(p>5\), suppose three geometric lines meet at a point \(P\). The tangent plane is the three-dimensional vector space \(W_P=\{Y:\sum Y_i=\sum P_i^2Y_i=0\}\), and the cubic's quadratic term there is \(3\sum P_iY_i^2\). Since a triple-line section has no quadratic term at its common point, \(W_P\) is totally isotropic for the diagonal quadratic form \(B_P(Y)=\sum P_iY_i^2\). If exactly \(z\) coordinates of \(P\) vanish, this quadratic form has radical dimension \(z\), whose intersection with \(W_P\) has dimension at most \(z-1\) for \(z\ge1\) (the sum-of-coordinates condition). On its nondegenerate quotient, the maximal isotropic dimension is \(\lfloor(5-z)/2\rfloor\). For \(z=0,1,2\) these bounds give at most two dimensions, contradicting \(\dim W_P=3\). Thus \(z\ge3\). Four zero coordinates cannot satisfy the defining sum, so \(z=3\), and \(P\) is a permutation of \([1:-1:0:0:0]\). These ten points are indeed Eckardt by the diagonal construction. Therefore exactly ten triple points occur for **every** \(p>5\), not merely over characteristic zero.

**4. Frobenius trace.** A smooth cubic surface has \(\operatorname{Pic}\)-rank seven over the algebraic closure, with point count \(Q^2+Q\operatorname{tr}(\mathrm{Frob}_Q\mid\operatorname{Pic})+1\). For split \(Q\), all 27 lines are rational and span the Picard group, so the trace is seven. In the nonsplit case the 15 diagonal line classes are fixed and span a dimension-six subspace: their intersection matrix is \(M=A-I\), where \(A\) is the adjacency matrix of the 15-line intersection graph. Strong regularity gives \(A^2=3I-2A+3J\), so its eigenvalues are \(6\) once, \(1\) nine times, and \(-3\) five times. Consequently \(M\) has rank six. This is the actual span rank: the span contains an ample class (the sum of the 15 line classes is a positive multiple of the hyperplane class) and hence has nondegenerate intersection form by the Hodge index theorem. Frobenius squared fixes all 27 lines, hence the Picard group, but Frobenius itself moves the other twelve distinct exceptional classes. Its remaining eigenvalue is \(-1\), and its trace is five. Thus \(\#X(\mathbb F_Q)=Q^2+7Q+1\) in the split case and \(Q^2+5Q+1\) in the nonsplit case.

**5. Complement, zeta function, and sharp emptiness.** Subtract \(N_1+N_2+N_3\) from the corresponding surface count. This gives \(N_0=Q^2-20Q+99=(Q-9)(Q-11)\) if split and \(N_0=Q^2-10Q+21=(Q-3)(Q-7)\) if nonsplit. Because split fields with characteristic \(p>5\) satisfy \(Q\ge11\), and nonsplit fields satisfy \(Q\ge7\), the only zero counts at the ground level are \(q=11\) (split) and \(q=7\) (nonsplit). For every extension \(n\ge1\), substitute \(\varepsilon^n\) and expand the exponential generating function, using \(\exp(\sum_{n\ge1}c^nT^n/n)=(1-cT)^{-1}\). This yields the stated rational functions.

## Verification
The standalone program `verify_incidence.py` builds all 15 diagonal two-dimensional subspaces with rational integer coefficients, computes their pairwise intersections, verifies the graph parameters and the rank-six intersection matrix. It completed with `VERIFY_CLEBSCH_INCIDENCE_OK lines=15 graph_edges=45 picard_span=6`. A separate `verify_finite.py` enumerates rational projective points and all rational lines of the cubic over the six prime fields of orders \(7,11,13,17,19,23\), independently reconstructs the multiplicity spectrum, and compares with the formula. It completed with `VERIFY_CLEBSCH_FINITE_OK fields=6`. Finite enumeration tests only those six fields; the proof covers all specified prime powers and extensions.

## Relationship to prior work
The 15 diagonal lines, 12 additional lines, ten Eckardt points and classical 27-line incidence are established geometry, not new claims. Brundu–Logar–Polli (2022) treat the geometry and automorphisms of the symmetric cubic and identify the ten-Eckardt configuration. Debarre describes the rational 15-line versus quadratic 12-line split of the Clebsch model. McKean discusses rational-line counts and Frobenius actions on smooth cubic surfaces. Hirschfeld's 1981 chapter explicitly gives the **already known** split point count and split 27-line union count \(27(Q-4)+e\); substituting the Clebsch value \(e=10\) recovers the split \(N_0\) formula here. The present full-extension nonsplit count is not a claim about a new surface or a new line configuration. It arises from the arithmetic incidence of the Galois-paired skew lines and the Picard trace; priority for an unlocated older equivalent finite-field formula remains uncertain.

## Limitations
All assertions are restricted to the displayed untwisted Clebsch surface in characteristic greater than five. No classification of twists or other cubic surfaces is claimed. The split ground-field complement count is preexisting. The chapter by Hirschfeld was accessible only through its posted detailed summary; its complete chapter might contain additional implications that have not been excluded. This theorem does not claim an independent external audit.

## References
- M. Brundu, A. Logar, F. Polli, *Construction of Symmetric Cubic Surfaces* (2022), arXiv:2207.04493, https://arxiv.org/abs/2207.04493 (first version dated 2022-07-10).
- S. McKean, *Rational Lines on Smooth Cubic Surfaces* (2021), arXiv:2101.08217, https://arxiv.org/abs/2101.08217.
- O. Debarre, *Rational curves on hypersurfaces*, lecture notes (2016), https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/Busan2016.pdf.
- J. W. P. Hirschfeld, *Cubic surfaces whose points all lie on their 27 lines*, in *Finite Geometries and Designs* (1981), doi:10.1017/CBO9781107325579.020.
