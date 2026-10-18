# A coordinate-subspace dichotomy inside a strongly unique-predual renorming of \(\ell_1\)
## Finding
Let \(Y\) be the equivalent renorming of \(c_0\) used in Appendix A of Aliaga--Cúth--Vico, and let \(X=Y^*\). The source proves that \(X\) has a strongly unique predual and that, on the underlying vector space \(\ell_1\),
\[
\|x\|_X=\max\left\{\sum_{n\ge2}|x_n|,\ |x_1|+\max_{n\ge2}|x_n|\right\}.
\]
For every nonempty set \(I\subset\mathbb N\), define
\[
X_I=\{x\in X:x_n=0\text{ for }n\notin I\}
\]
and let \(P_I\) be the coordinate projection onto \(I\). Then \(X_I\) is weak-* closed and \(\|P_I\|=1\).

For every infinite \(I\), there is an exact dichotomy:
\[
1\in I \quad\Longrightarrow\quad X_I\cong X\text{ isometrically},
\]
whereas
\[
1\notin I \quad\Longrightarrow\quad X_I\cong \ell_1\text{ isometrically}.
\]
Hence the first class has a strongly unique predual, while the second class does not even have a unique isometric predual.

There are continuum many infinite sets in each class. In addition, for every integer \(k\ge1\), the same space \(X\) contains both a codimension-\(k\) weak-* closed \(1\)-complemented coordinate subspace with a strongly unique predual and a codimension-\(k\) such subspace without a unique predual.

## Assumptions and scope
All spaces are real. The space \(X\) is exactly the dual renorming constructed in Appendix A of the cited source; no assertion is made for arbitrary strongly unique-predual spaces. The coordinate subspaces considered here are those determined by the canonical coordinates of the underlying \(\ell_1\) vector space.

The statement about nonuniqueness uses the classical fact that \(\ell_1\) has nonisometric isometric preduals, for example \(c_0\) and \(c\).

## Proof
Write
\[
S(x)=\sum_{n\ge2}|x_n|,\qquad M(x)=\max_{n\ge2}|x_n|.
\]
The source norm is \(\|x\|_X=\max\{S(x),|x_1|+M(x)\}\).

Fix nonempty \(I\subset\mathbb N\). Coordinate deletion can only decrease \(S\), \(M\), and \(|x_1|\). Therefore
\[
\|P_Ix\|_X\le \|x\|_X
\]
for every \(x\in X\). Since \(P_I\) is the identity on the nonzero space \(X_I\), it follows that \(\|P_I\|=1\).

Because \(X=Y^*\) and every canonical vector \(e_n\) belongs to the underlying vector space \(Y=c_0\),
\[
X_I=\bigcap_{n\notin I}\ker(e_n).
\]
Each kernel is weak-* closed, so \(X_I\) is weak-* closed.

Suppose now that \(I\) is infinite and \(1\notin I\). For \(x\in X_I\), one has \(x_1=0\), and therefore
\[
\|x\|_X
=\max\left\{\sum_{n\in I}|x_n|,\max_{n\in I}|x_n|\right\}
=\sum_{n\in I}|x_n|.
\]
Thus \(X_I\) is isometric to \(\ell_1(I)\), hence to \(\ell_1\). The latter does not have a unique isometric predual.

If instead \(1\in I\) and \(I\setminus\{1\}\) is infinite, choose a bijection from \(\mathbb N\setminus\{1\}\) onto \(I\setminus\{1\}\) and keep coordinate \(1\) fixed. The displayed norm formula is invariant under such a permutation of the tail coordinates, so the induced coordinate relabelling is a surjective linear isometry from \(X\) onto \(X_I\). Hence \(X_I\) has a strongly unique predual because \(X\) does.

There are continuum many infinite subsets of \(\mathbb N\setminus\{1\}\), and also continuum many infinite subsets containing \(1\) and infinitely many tail coordinates, giving continuum many distinct subspaces of each type.

Finally fix \(k\ge1\). Put
\[
I_k^- = \mathbb N\setminus\{1,2,\ldots,k\}
\]
and
\[
I_k^+ = \mathbb N\setminus\{2,3,\ldots,k+1\}.
\]
Both coordinate subspaces have codimension \(k\). The first omits coordinate \(1\), so it is isometric to \(\ell_1\) and lacks a unique predual. The second contains coordinate \(1\) and infinitely many tail coordinates, so it is isometric to \(X\) and has a strongly unique predual.

## Verification
The argument is symbolic. The only nonstandard input is the source's explicit dual norm formula and its proof that \(X\) has a strongly unique predual. Every later step follows directly from coordinate monotonicity, weak-* continuity of the coordinate functionals from \(Y\), and coordinate relabelling.

The codimension statement is checked by noting that the quotient by a coordinate subspace obtained by deleting exactly \(k\) coordinates is \(k\)-dimensional. No finite experiment or enumeration is used.

## Relationship to prior work
Aliaga--Vico first published the explicit counterexample on September 1, 2026, showing that strong uniqueness of a predual need not pass to a weak-* closed, \(1\)-complemented subspace of codimension one. The superseding Aliaga--Cúth--Vico paper retains that construction in Appendix A and gives the exact norm formula used here.

The present finding extracts the complete behavior of all infinite canonical coordinate subspaces of that example. It shows that the codimension-one failure is not isolated: within one fixed strongly unique-predual space, the same weak-* closed and norm-one complemented coordinate mechanism gives both preservation and failure at every positive finite codimension, and continuum many subspaces of each behavior.

The classical nonuniqueness of the predual of \(\ell_1\) is documented, for example, by Brown--Ito, who note that \(c_0\) and \(c\) are nonisometric isometric preduals of \(\ell_1\).

## Limitations
This is a structural classification only for the canonical coordinate subspaces of the specific renormed \(\ell_1\) example. It does not classify arbitrary weak-* closed complemented subspaces of \(X\), does not assert that every strongly unique-predual space has such a dichotomy, and does not extend the conclusion to arbitrary non-coordinate projections.

For finite coordinate sets, the infinite-dimensional dichotomy above is not asserted. No claim is made about uniqueness among merely isomorphic preduals.

## References
1. R. J. Aliaga and F. Vico, *The unique predual problem for Lipschitz spaces, revisited*, arXiv:2609.00970v1, 2026.
2. R. J. Aliaga, M. Cúth, and F. Vico, *Lipschitz-free spaces are strongly unique preduals*, arXiv:2609.24392v1, 2026, Appendix A.
3. L. Brown and T. Ito, *Isometric Preduals of James Spaces*, Canadian Journal of Mathematics 32 (1980), 59--69, DOI 10.4153/CJM-1980-006-2.
