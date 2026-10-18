# Exact norm geometry of the canonical Lotz semigroup on 1-unconditional decompositions
## Finding
Let \(X=\bigoplus_{n\ge1}X_n\) be a Banach space with a 1-unconditional Schauder decomposition in the following precise sense: every bounded scalar sequence \(c=(c_n)\) defines the diagonal multiplier
\[
M_c\Big(\sum_{n\ge1}x_n\Big)=\sum_{n\ge1}c_nx_n
\]
and satisfies
\[
\|M_c\|\le \sup_{n\ge1}|c_n|.
\]
For the diagonal semigroup
\[
T(t)\Big(\sum_{n\ge1}x_n\Big)=\sum_{n\ge1}n^{-t}x_n,\qquad t\ge0,
\]
which is the canonical coefficient choice used in the recent Lotz-property construction, the full pairwise operator-norm metric is
\[
\|T(t)-T(s)\|=\sup_{n\ge1}|n^{-t}-n^{-s}|\qquad(s,t\ge0).
\]
Consequently,
\[
\|T(t)-I\|=1\qquad(t>0),
\]
even though \(T(t)x\to x\) for every \(x\in X\) as \(t\downarrow0\).

For \(0<s<t\), put
\[
r_*=(t/s)^{1/(t-s)},\qquad m=\lfloor r_*\rfloor.
\]
Then the supremum is a maximum and has the explicit two-point formula
\[
\|T(t)-T(s)\|=
\max\{m^{-s}-m^{-t},(m+1)^{-s}-(m+1)^{-t}\}.
\]
The same diagonal family extends to a norm-holomorphic semigroup on the open right half-plane. For \(\operatorname{Re}z>0\),
\[
T(z)\Big(\sum_{n\ge1}x_n\Big)=\sum_{n\ge1}n^{-z}x_n,
\qquad \|T(z)\|=1,
\]
and for every integer \(k\ge1\) and every \(t>0\),
\[
\|T^{(k)}(t)\|=
\sup_{n\ge1}(\log n)^k n^{-t}.
\]
Thus the only operator-norm singularity of this path is at time zero: it has a persistent unit jump there but is norm-analytic at every positive time.

If, additionally, every \(X_n\) is finite-dimensional, define
\[
F_N(t)=\sum_{n=1}^{N} n^{-t}P_n.
\]
Then \(F_N(t)\) is finite rank and
\[
\|T(t)-F_N(t)\|=(N+1)^{-t}.
\]
Hence \(T(t)\) is compact for every \(t>0\), with an exact canonical finite-rank approximation rate.

## Assumptions and scope
The decomposition is assumed 1-unconditional in the multiplier sense stated above; this normalization is essential for the exact constant-one multiplier formula. Every block \(X_n\) is assumed nonzero. The compactness conclusion requires a finite-dimensional decomposition, meaning that every block \(X_n\) is finite-dimensional. No compactness assertion is made for decompositions having infinite-dimensional blocks.

The result concerns this specific diagonal semigroup. It does not classify all strongly continuous semigroups on spaces with unconditional decompositions, and it does not assert that the same exact formulas survive after replacing the 1-unconditional norm by an arbitrary equivalent unconditional norm.

## Proof
First observe that the assumed multiplier inequality is automatically sharp. If \(j\ge1\) and \(0\ne x\in X_j\), then
\[
M_cx=c_jx,
\]
so \(\|M_c\|\ge |c_j|\). Taking the supremum over \(j\) gives
\[
\|M_c\|=\sup_{n\ge1}|c_n|.
\]
Applying this identity to the coefficient sequence \(c_n=n^{-t}-n^{-s}\) proves
\[
\|T(t)-T(s)\|=\sup_{n\ge1}|n^{-t}-n^{-s}|.
\]
If \(s=0<t\), the coefficients are \(1-n^{-t}\). They are strictly below \(1\) for every finite \(n\) and converge to \(1\), so the operator norm is exactly \(1\), with no maximizing block.

For \(0<s<t\), consider
\[
h(r)=r^{-s}-r^{-t}\qquad(r\ge1).
\]
Its derivative is
\[
h'(r)=r^{-t-1}\bigl(t-sr^{t-s}\bigr).
\]
Thus \(h\) increases up to the unique critical point
\[
r_*=(t/s)^{1/(t-s)}
\]
and decreases afterwards. The maximum over positive integers is therefore attained at one of the two integers adjacent to \(r_*\), giving the stated formula.

For complex \(z\) with \(\operatorname{Re}z>0\), the coefficient sequence \((n^{-z})_n\) belongs to \(\ell_\infty\), so the multiplier identity gives \(\|T(z)\|=1\), attained on the first block. On every closed half-plane \(\operatorname{Re}z\ge\delta>0\), each coefficient derivative
\[
(-\log n)^k n^{-z}
\]
is uniformly bounded in \(n\). Difference quotients converge uniformly in the coefficient \(\ell_\infty\)-norm on compact subsets, and the multiplier map from \(\ell_\infty\) into \(\mathcal L(X)\) is isometric. Hence \(z\mapsto T(z)\) is operator-norm holomorphic, with
\[
T^{(k)}(t)=M_{(( -\log n)^k n^{-t})_n}
\]
and the asserted derivative norm.

Strong continuity at zero follows directly from finite-coordinate approximation. Given \(x=\sum_nx_n\) and \(\varepsilon>0\), choose a finite partial sum \(x^{(N)}\) with \(\|x-x^{(N)}\|<\varepsilon\). Since \(\|T(t)\|=1\), the tail contributes at most \(2\varepsilon\), while \(T(t)x^{(N)}\to x^{(N)}\) in its finite sum of blocks.

Finally, in the finite-dimensional-block case, \(F_N(t)\) has finite-dimensional range. Its tail is the multiplier with coefficients \(0\) for \(n\le N\) and \(n^{-t}\) for \(n>N\), so
\[
\|T(t)-F_N(t)\|=\sup_{n>N}n^{-t}=(N+1)^{-t}.
\]
This tends to zero, proving compactness.

## Verification
All equalities reduce to the exact multiplier norm formula above and one-variable calculus. The endpoint \(s=0\) was treated separately because its supremum is not attained. The positive-time formula was checked for both orders of \(s,t\) by symmetry of the operator norm, and the case \(s=t\) gives zero.

The holomorphic statement uses uniform convergence in the coefficient \(\ell_\infty\)-norm on compact subsets of the right half-plane, not pointwise differentiation alone. The compactness statement uses actual finite-rank truncations and an exact norm tail, so no finite experiment is extrapolated to an infinite conclusion.

## Relationship to prior work
Araújo, Barbosa, and Seoane-Sepúlveda construct the relevant diagonal semigroup while proving that Banach spaces with unconditional Schauder decompositions fail the Lotz property. Their unconditional multiplier estimate is stated with an unspecified constant, and the inspected argument is qualitative: it establishes failure of norm continuity at zero rather than the complete pairwise operator-norm metric, the exact positive-time derivative norms, or the finite-dimensional-decomposition approximation law recorded here.

A companion 2026 paper on the Lotz property in weakly compactly generated spaces constructs the related semigroup with coefficients \(e^{-nt}\) on an arbitrary Schauder decomposition and gives an Abel-summation upper bound in terms of the decomposition constant. That estimate does not imply the exact 1-unconditional metric above. An older paper by Bárcenas and Mármol notes a qualitative diagonal semigroup example on \(\ell^p\) in a discussion of non-uniform continuity, but the inspected material does not state the all-pairs exact formula or the positive-time holomorphic norm profile.

Targeted statement-level searches for diagonal semigroups, 1-unconditional decompositions, exact norm jumps, and the coefficient family \(n^{-t}\), together with searches of the current and prior owned ledgers, located no result implying the theorem above. The remaining originality risk is that the exact multiplier calculation may appear in older semigroup or unconditional-decomposition literature under different terminology.

## Limitations
The exact constants use the 1-unconditional multiplier normalization. For a merely unconditional decomposition with constant greater than one, the same scalar formulas give lower bounds and standard unconditionality gives upper bounds, but equality need not follow from the present argument. No converse characterization of 1-unconditional decompositions is claimed.

The positive-time compactness conclusion is restricted to finite-dimensional blocks. No claim is made about trace ideals, approximation numbers beyond the displayed canonical truncations, or optimality among all rank-\(N\) approximants.

## References
1. Gustavo Araújo, Anderson Barbosa, Juan B. Seoane-Sepúlveda, *The Separable Quotient Problem and the Lotz Property in Banach Spaces*, arXiv:2610.00584v1, first public version 2026-09-30.
2. Gustavo Araújo, Anderson Barbosa, Juan B. Seoane-Sepúlveda, *The Lotz Property in Weakly Compactly Generated Spaces*, arXiv:2609.38396v1, first public version 2026-09-29.
3. Diómedes Bárcenas and Luis Gerardo Mármol, *On the Adjoint of a Strongly Continuous Semigroup*, International Journal of Mathematics and Mathematical Sciences (2008), DOI:10.1155/2008/651294.
