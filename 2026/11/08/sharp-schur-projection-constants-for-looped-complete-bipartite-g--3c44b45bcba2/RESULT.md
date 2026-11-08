# Sharp Schur-projection constants for looped complete bipartite graphs

## Finding
For integers \(a,b\geq2\), partition the coordinates of \(\mathbb C^{a+b}\) into two classes of sizes \(a\) and \(b\). Let \(M_{a,b}\) be the zero-one matrix which retains every diagonal entry and every entry joining different classes, and deletes entries joining distinct vertices within either class. The Schur multiplier \(\mathcal S_{a,b}:X\mapsto M_{a,b}\circ X\) on complex \((a+b)\)-square matrices satisfies
\[
\boxed{\|\mathcal S_{a,b}\|_{B(M_{a+b})\to B(M_{a+b})}=\|\mathcal S_{a,b}\|_{\mathrm{cb}}=1+\frac{2(ab-1)}{2ab+a+b}=\frac{4ab+a+b-2}{2ab+a+b}.}
\]
The expression is symmetric in the two part sizes and is strictly below \(2\). In particular, the balanced values tend to \(2\), while for fixed \(a\geq2\) and \(b\to\infty\), the limit is \((4a+1)/(2a+1)\). The cases with a singleton class satisfy the same algebraic formula, but are not claimed as a new contribution.

## Assumptions and scope
All vector spaces and matrices are complex. Here \(B(M_n)\) denotes the space of all \(n\)-square complex matrices carrying its usual operator norm as operators on \(\ell_2^n\). The mask is the Hermitian block matrix
\[
M_{a,b}=\begin{pmatrix}I_a&J_{a,b}\\J_{b,a}&I_b\end{pmatrix},
\]
where \(J_{a,b}\) denotes the all-one \(a\)-by-\(b\) matrix. The completely bounded norm is defined using all matrix amplifications of the Schur multiplication map. For a finite Schur multiplier, the operator and completely bounded norms coincide by the Grothendieck--Haagerup factorization theorem, as recapitulated by Davidson--Donsig and Christensen.

## Proof
**1. Self-adjoint Schur norm as an order interval.** For a Hermitian matrix \(M\), the Schur norm is the least \(t\) for which some Hermitian \(P\) has all diagonal entries at most \(t\) and satisfies \(P-M\succeq0\) and \(P+M\succeq0\). Indeed, the usual Haagerup factorization says that the same norm is the smallest diagonal bound of positive block matrices \(\left(\begin{smallmatrix}U&M\\M&V\end{smallmatrix}\right)\); replacing \(U,V\) by their mean yields \(\left(\begin{smallmatrix}P&M\\M&P\end{smallmatrix}\right)\), which is unitarily equivalent to \((P+M)\oplus(P-M)\). Conversely this gives such a factorization. This is also the formula in Christensen's Theorem 2.2.

**2. Sharp feasible matrix.** Set
\[
v=\frac{2(ab-1)}{2ab+a+b},\qquad
P=\begin{pmatrix}I_a+vJ_{a,a}&(1-v)J_{a,b}\\ (1-v)J_{b,a}&I_b+vJ_{b,b}\end{pmatrix}.
\]
All diagonal entries of \(P\) are \(1+v\). The difference \(P-M_{a,b}\) is the rank-one positive matrix \(vww^*\) with \(w=(1,\ldots,1,-1,\ldots,-1)\). On vectors summing to zero in either part, \(P+M_{a,b}\) acts as multiplication by \(2\). On normalized constant vectors of the two parts its matrix is
\[
\begin{pmatrix}2+av&\sqrt{ab}(2-v)\\\sqrt{ab}(2-v)&2+bv\end{pmatrix}.
\]
Its diagonal entries are positive and its determinant vanishes, since
\[
(2+av)(2+bv)-ab(2-v)^2=4-4ab+(2a+2b+4ab)v=0.
\]
Thus \(P\pm M_{a,b}\succeq0\), giving the claimed upper bound.

**3. Matching lower bound.** Let \(t\) be any feasible diagonal bound. Averaging \(P\) over permutations within both parts, complex conjugation, and transposition does not change its diagonal bound or the semidefinite inequalities. The resulting real symmetric \(P\) is block-permutation invariant. On the respective zero-sum subspaces its eigenvalues \(x,y\) must be at least \(1\). On the span of the normalized part-constant vectors write its compression \(\left(\begin{smallmatrix}p&q\\q&r\end{smallmatrix}\right)\). The diagonal constraints imply
\[
p\leq 1+a(t-1),\qquad r\leq1+b(t-1).
\]
The two positive-semidefinite \(2\)-square blocks of \(P\pm M_{a,b}\) imply that the intervals
\[
[-\sqrt{ab}-\sqrt{(p+1)(r+1)},-\sqrt{ab}+\sqrt{(p+1)(r+1)}]
\]
and
\[
[\sqrt{ab}-\sqrt{(p-1)(r-1)},\sqrt{ab}+\sqrt{(p-1)(r-1)}]
\]
intersect (each contains \(q\)). Consequently
\[
2\sqrt{ab}\leq\sqrt{(p+1)(r+1)}+\sqrt{(p-1)(r-1)}.
\]
Put \(u=t-1\). Since the explicit upper bound is less than \(2\), it suffices to consider \(0\leq u<1\); then the preceding inequalities force
\[
2\sqrt{ab}\leq\sqrt{(2+au)(2+bu)}+\sqrt{ab}\,u.
\]
Both sides of \(\sqrt{(2+au)(2+bu)}\geq\sqrt{ab}(2-u)\) are nonnegative. Squaring and cancelling the common \(ab u^2\) gives
\[
4+2(a+b)u\geq 4ab-4ab u,
\]
hence \(u\geq2(ab-1)/(2ab+a+b)\), proving equality. No finite-dimensional numerical search is used in this argument.

**4. Limits.** Direct division of the rational formula gives
\[
\lim_{b\to\infty}\|\mathcal S_{a,b}\|=\frac{4a+1}{2a+1},\qquad
\lim_{n\to\infty}\|\mathcal S_{n,n}\|=2.
\]
The graph changes from a single-hub tree in the singleton-part boundary to a graph with many four-cycles when both parts have size at least two. The two-parameter formula quantifies its operator-norm projection cost in every finite size.

## Verification
Run the standalone standard-library program `VERIFY.py` with Python 3. It checks the exact determinant identity, lower-bound equality, symmetry, and representative finite-size and limiting computations using rational arithmetic for 1,610 parameter combinations/comparisons. These finite tests are diagnostic only; the proof above is for all positive integers.

## Relationship to prior work
Christensen (2025) proves the self-adjoint Schur-norm positive-order formulation that underlies the reduction. Davidson and Donsig (2005) provide the general factorization and an exact trace formula in *transitive* permutation-symmetric patterns; for equal part sizes, their transitive result already implies a special case of the present numerical value. Levene (2014) gives fundamental idempotent-mask gap and finite-pattern results, not the displayed unbalanced all-size formula in the inspected results. The new assertion concerns **all unequal part sizes**, including unbounded ratios, rather than another calculation of the known singleton-part or equal-part cases. The 2026 results of Arhancet and of González-Pérez--Parcet--Pérez García--Wang motivate sharp multiplier norms and the contrast between endpoint and interior Schatten exponents; neither establishes the present parameter formula.

## Limitations
The result concerns the operator-norm/complete-bound endpoint only; it does not determine the Schur multiplier norms on intermediate Schatten classes. It concerns a particular complete bipartite graph with diagonal loops, not arbitrary bipartite graphs or larger multipartite graphs. Literature priority may require further examination of older general symmetric-matrix or graph-multiplier results.

## References
1. C. Arhancet, *Optimal square size for separating the operator and completely bounded norms of Schur multipliers on \(S^4\)*, arXiv:2609.29643, first version September 3, 2026.
2. A. González-Pérez, J. Parcet, J. Pérez García, S. Wang, *Radial Schur multipliers on trees and the failure of Fourier-Schur transference*, arXiv:2610.15881, October 11, 2026.
3. E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670, Theorem 2.2.
4. K. R. Davidson and A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073, Section 4.
5. R. H. Levene, *Norms of idempotent Schur multipliers*, New York J. Math. 20 (2014), 325–352, arXiv:1302.4849.
6. C. Beke, M. K. Goh, H. Hatami, S. Jaffe, D. Naylor, *A characterization of idempotent Schur multipliers*, arXiv:2607.14316, 2026.
