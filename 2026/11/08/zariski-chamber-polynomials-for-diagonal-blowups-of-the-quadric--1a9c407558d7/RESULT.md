# Zariski chamber polynomials for diagonal blowups of the quadric surface

## Finding
Let \(X_n\) be the blowup of \(\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}\) at \(n\ge5\) distinct points on one smooth curve of bidegree \((1,1)\). Write \(Z_n(t)=\sum_{r\ge0}z_{n,r}t^r\), where \(z_{n,r}\) counts Zariski chambers whose negative parts have precisely \(r\) irreducible support curves, and include the nef chamber in \(z_{n,0}\). Put
\[
F_n(t)=2(1+2t)^n-(1+t)^n+n t^2(1+t)^{n-1}.
\]
Then the complete support-size distribution is
\[
\boxed{Z_n(t)=(1+t)F_n(t)-t\left[\binom n2t^{n-2}+(2n^2-n)t^{n-1}+(2n^2+1)t^n+n t^{n+1}\right].}
\]
In particular the exact number of chambers is
\[
\boxed{z(X_n)=4\cdot3^n+(n-2)2^n-\frac{9n^2-n+2}{2}.}
\]
For \(n=5\), the polynomial is \(1+16t+90t^2+245t^3+345t^4+223t^5+37t^6\), with \(957\) chambers. For \(n=6\), it is \(1+19t+129t^2+441t^3+855t^4+948t^5+529t^6+90t^7\), with \(3012\) chambers. Thus the entire support distribution is independent of the positions of the distinct marked points, and the total is asymptotic to \(4\cdot3^n\).

## Assumptions and scope
All surfaces and curves are over \(\mathbb C\). Denote the pullbacks of the two ruling classes by \(U,V\), with \(U^2=V^2=0\) and \(U\cdot V=1\). The points lie on a smooth, irreducible \((1,1)\)-curve \(\Gamma\); the points need not be general on \(\Gamma\), only distinct. Denote exceptional curves by \(E_i\), their two ruling-fiber transforms by \(A_i\sim U-E_i\) and \(B_i\sim V-E_i\), and the strict transform of the diagonal by \(D\sim U+V-\sum_i E_i\). The assertion concerns chambers in the big cone, not Mori chambers or chamber volumes. All \(n\ge5\) are covered, including \(n\ge9\), when the anticanonical self-intersection is nonpositive.

## Proof
**1. Exhaustiveness of the negative curves.** The curves \(E_i,A_i,B_i,D\) are irreducible and have respective self-intersections \(-1,-1,-1,2-n\). Every irreducible curve \(C\) other than an exceptional curve is the strict transform of an integral bidegree-\((a,b)\) curve, with \(a,b\ge0\). Since
\[
-K_{X_n}=2U+2V-\sum_iE_i=(U+V)+D,
\]
for \(C\ne D\) the nonnegativity of intersections between distinct irreducible curves gives
\[
-K_{X_n}\cdot C=(U+V)\cdot C+D\cdot C\ge a+b.
\]
The adjunction formula then gives \(C^2=2p_a(C)-2-K_{X_n}\cdot C\ge a+b-2\), since an integral projective curve has nonnegative arithmetic genus. Thus if \(a+b\ge2\), its strict transform is not negative. When \(a+b=1\), \(C\) is a ruling fiber. Each ruling fiber meets \(\Gamma\) in precisely one point, so its strict transform is negative exactly when it contains one of the marked points; these are precisely the \(A_i,B_i\). When \(a+b=0\), the only irreducible curves contracted by the blowup are the \(E_i\). This proves that the above \(3n+1\) curves are the complete set of negative irreducible curves.

**2. Exact negative-definiteness rule.** In addition to diagonal entries, the only nonzero off-diagonal intersections among these curves are
\[
E_i\cdot A_i=E_i\cdot B_i=1,\qquad A_i\cdot B_j=1\ (i\ne j),\qquad D\cdot E_i=1.
\]
The diagonal is orthogonal to all \(A_i,B_i\). A negative-definite matrix cannot contain two \((-1)\)-curves meeting once: their two-by-two principal matrix has determinant zero. Therefore a support must choose subsets \(I,J,K\subseteq\{1,\ldots,n\}\) of the \(A\)-, \(B\)-, and \(E\)-curves such that \(K\cap(I\cup J)=\varnothing\) and either \(I\) or \(J\) is empty, or \(I=J=\{i\}\) for some index \(i\). Without \(D\), these conditions suffice because all selected curves are mutually orthogonal. With \(D\), the only remaining nontrivial intersection block consists of \(D\) and the \(|K|\) selected exceptional curves. Its Schur complement is \(-(n-2)+|K|\), so the block is strictly negative definite if and only if \(|K|<n-2\), or equivalently \(|K|\le n-3\).

**3. Count all supports.** First omit \(D\). Supports with no ruling fibers contribute \((1+t)^n\). Supports using only \(A\)'s, or only \(B\)'s, but at least one, contribute \(2[(1+2t)^n-(1+t)^n]\). If both families occur, they must be the two fibers indexed by the same \(i\), yielding \(n t^2(1+t)^{n-1}\). Summing gives exactly \(F_n(t)\).

Now add \(D\). The allowed supports are the same as before, except that selections containing \(k\ge n-2\) exceptional curves are excluded. The forbidden-support polynomial *before* inserting \(D\) is
\[
P_n(t)=\binom n2t^{n-2}+(2n^2-n)t^{n-1}+(2n^2+1)t^n+n t^{n+1}.
\]
Indeed, forbidden choices with no ruling fibers have exceptional count \(n-2,n-1,n\); with ruling fibers from one family, there can be only one or two selected fibers; with both families, they must be the two fibers of one index. Counting these four disjoint cases produces the displayed four coefficients. Therefore the generating polynomial for supports containing \(D\) is \(t[F_n(t)-P_n(t)]\). Adding the supports omitting \(D\) gives the boxed expression. Evaluating at \(t=1\) yields the exact chamber count. Every negative-definite support corresponds to a unique Zariski chamber by the standard chamber-support correspondence of Bauer--Funke--Neumann (2009, Proposition 1.1), including the empty nef support. \(\square\)

## Verification
The accompanying pure-Python program `verify.py` builds the full integral intersection matrix of \(E_i,A_i,B_i,D\) and, independently of the generating-function argument, enumerates all \(2^{3n+1}\) candidate supports for \(n=3,4,5,6\). Every possible surviving support is checked by an exact rational \(LDL^\mathsf T\) positive-definiteness test of the negative intersection matrix; a necessary two-by-two obstruction is used only for pruning. The program then independently expands the closed polynomial and compares every coefficient. It prints `ALL_CHECKS_PASSED` on success. The \(n=3,4\) counts are boundary controls outside the novel \(n\ge5\) range, not extensions claimed as new. Finite enumeration supports, but does not replace, the proof for every \(n\ge5\).

## Relationship to prior work
Bauer, Funke and Neumann's 2009 paper proves the general correspondence between chambers and negative-definite supports and tabulates ordinary del Pezzo blowups at points in general position, not the present diagonal \((1,1)\)-configuration for all \(n\ge5\). Bauer and Schmitz (2012) study chamber volumes and illustrate methods on collinear-plane blowups, not this support distribution. Brugalle (2014) treats enumerative Gromov--Witten and Welschinger invariants for points on a plane conic, which are different invariants on a different configuration. The present statement is the closed \(n\)-parameter support enumerator for blowups of the quadric along one smooth diagonal, including the full indefinite-anticanonical range. The general support-counting algorithm is a method, not an explicit assertion of this polynomial.

## Limitations
No chamber volumes, adjacency graph, boundary incidence, or effective nef-cone generators are claimed. The result is limited to point sets on a single smooth \((1,1)\)-curve; arbitrary configurations of points on the quadric have different negative-curve sets. The originality comparison is based on the inspected literature and may be affected by unlocated specialist computations. Independent scientific validation has not been performed.

## References
1. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (first posted 2009-12-04), especially Proposition 1.1 and Section 3. https://arxiv.org/abs/0912.0958
2. T. Bauer, D. Schmitz, *Volumes of Zariski chambers*, arXiv:1205.3817 (first posted 2012-05-16), especially Section 3. https://arxiv.org/abs/1205.3817
3. E. Brugalle, *Floor diagrams relative to a conic, and GW-W invariants of Del Pezzo surfaces*, arXiv:1404.5429 (first posted 2014-04-22), especially Section 1. https://arxiv.org/abs/1404.5429
