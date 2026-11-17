# Exact fixed-point projection shells and a nuclear-norm plateau for the derangement face

## Finding
Let \(n\ge3\), and equip real \(n\times n\) matrices with their Frobenius or Schatten metrics. Let \(\mathcal B_n\) be the polytope of doubly stochastic matrices and let
\[
\mathcal D_n=\{X\in\mathcal B_n:X_{11}=\cdots=X_{nn}=0\}.
\]
By the bipartite perfect-matching theorem, \(\mathcal D_n\) is exactly the convex hull of permutation matrices with no fixed points. For a permutation matrix \(P\), denote the number of its fixed points by \(k(P)\). The squared Frobenius distance to this face is
\[
\boxed{\operatorname{dist}_{F}(P,\mathcal D_n)^2=k(P)+\frac{k(P)(k(P)+2)}{n+k(P)^2-2}.}\tag{1}
\]
All \(n\) possible fixed-point counts except \(n-1\) occur as distinct distance shells (the latter count is impossible). The shell with \(k\) fixed points contains exactly \(\binom nk\,! (n-k)\) permutation vertices, where \(!m=m!\sum_{j=0}^{m}(-1)^j/j!\) counts derangements and \(!0=1\).

The exact Frobenius Hausdorff separation and its unique farthest point are
\[
\boxed{d_H^F(\mathcal B_n,\mathcal D_n)=\frac{n}{\sqrt{n-1}},\qquad \operatorname*{argmax}_{X\in\mathcal B_n}\operatorname{dist}_F(X,\mathcal D_n)=\{I_n\}.}\tag{2}
\]
Among permutation vertices other than the identity, the maximal squared distance is \(n^2/(n-1)-2\), attained precisely at the \(\binom n2\) transpositions. Thus the first **vertex-supported** squared-distance gap is exactly \(2\) in every order. This is not a gap for arbitrary points of \(\mathcal B_n\), whose distances vary continuously.

More generally, with \(1\le p\le\infty\), \(1/\infty=0\), and the Schatten norm \(\|\cdot\|_{S_p}\),
\[
\boxed{d_H^{S_p}(\mathcal B_n,\mathcal D_n)=n(n-1)^{1/p-1}.}\tag{3}
\]
For all finite \(p\), the identity is the **unique** farthest point of \(\mathcal B_n\); for \(p=\infty\), the identity is a farthest point, without a claim classifying all other possible farthest points. Define \(U_n=(\mathbf1\mathbf1^{\mathsf T}-I_n)/(n-1)\). The unique Schatten-nearest point of \(\mathcal D_n\) to \(I_n\) is \(U_n\) for every \(1<p\le\infty\). In contrast, at \(p=1\) the complete nearest-point locus is
\[
\boxed{\{X\in\mathcal D_n:X=X^{\mathsf T}\}},\tag{4}
\]
a fractional perfect-matching polytope of affine dimension \(n(n-3)/2\) (zero-dimensional at \(n=3\)).

## Assumptions and scope
The ambient space is the actual \(n\times n\) real matrix space with its unscaled Frobenius and Schatten norms. A permutation matrix has entries \(P_{ij}=\mathbf1_{\{j=\pi(i)\}}\). Equation (1) is a distance to the whole convex face, not a minimum over derangement vertices. Equation (2) concerns the full Birkhoff body; the second-largest statement concerns **only permutation vertices**. The Schatten index includes the nuclear endpoint \(p=1\) and spectral endpoint \(p=\infty\). The claim does not concern arbitrary forbidden-edge patterns or all Schatten-nearest points from nonidentity permutations.

## Proof
**1. Complete Frobenius projection.** Fix a permutation \(\pi\) with \(k\ge1\) fixed points and let \(F=\{i:\pi(i)=i\}\), \(M=[n]\setminus F\), \(m=n-k\), and \(D=n+k^2-2\). Define \(X=X(P)\) by zero diagonal and, for \(i\ne j\),
\[
X_{ij}=\begin{cases}
(k+2)/D,&i,j\in F,\\
1/D,&\text{exactly one of }i,j\text{ belongs to }F,\\
1-k/D,&i,j\in M\text{ and }j=\pi(i),\\
0,&\text{otherwise}.
\end{cases}\tag{5}
\]
Every displayed positive entry is indeed positive: \(D>k\) for \(n\ge3\), \(k\ge1\). A fixed row sums to \(((k-1)(k+2)+m)/D=1\); a moved row sums to \(k/D+(1-k/D)=1\). The same holds for columns, so \(X\in\mathcal D_n\), including the boundary cases \(k=1\) and \(k=n\). Set \(b=1/D\) and introduce scalar row/column potentials
\[
u_i=\begin{cases}-(k+2)b/2,&i\in F,\\kb/2,&i\in M.\end{cases}
\]
On all allowed entries with \(X_{ij}>0\), the residual \(P_{ij}-X_{ij}=u_i+u_j\). On allowed zero entries, which can only be non-permutation positions within \(M\times M\), one has \(P_{ij}-X_{ij}=0\le u_i+u_j=kb\). For every feasible \(Y\in\mathcal D_n\), its row and column sums equal those of \(X\); hence
\[
\langle P-X,Y-X\rangle_F
=\sum_{i\ne j}\bigl(P_{ij}-X_{ij}-u_i-u_j\bigr)(Y_{ij}-X_{ij})\le0.\tag{6}
\]
Thus \(X\) is the Euclidean projection of \(P\) onto the convex set \(\mathcal D_n\), and it is unique. When \(k=0\), \(P\in\mathcal D_n\) and its own projection is itself. Directly summing the diagonal contribution \(k\), the \(k(k-1)\) fixed-to-fixed entries, the \(2km\) cross entries, and the \(m\) moved permutation entries gives
\[
\|P-X\|_F^2=k+\frac{k(k-1)(k+2)^2+2km+mk^2}{D^2}
=k+\frac{k(k+2)}D,
\]
which proves (1) in all cases.

**2. Strict shell ordering, counts, and sharp gap.** On the real interval \(0\le x\le n\), set \(f_n(x)=x+x(x+2)/(n+x^2-2)\). Differentiation yields
\[
f_n'(x)=1+\frac{2(x+1)(n-2)-2x^2}{(n+x^2-2)^2}>0.
\]
Indeed \(n+x^2-2\ge x^2+1\), so the derivative's numerator after clearing the positive square is at least \(x^4+1+2(x+1)(n-2)>0\). A permutation with exactly \(n-1\) fixed points cannot exist. The largest remaining count below \(n\) is \(n-2\), characterizing transpositions. Substitution gives \(f_n(n)=n^2/(n-1)\) and \(f_n(n-2)=n^2/(n-1)-2\). Choosing fixed positions and deranging the remainder gives the stated multiplicities.

Distance to any nonempty convex set is convex. Expressing an arbitrary \(A\in\mathcal B_n\) as a convex combination of permutation matrices and using the strict vertex inequality for \(P\ne I_n\) proves the full-body statement in (2), including uniqueness.

**3. Universal Schatten Hausdorff formula.** Every \(X\in\mathcal D_n\) has \(\mathbf1\) as both left and right eigenvector with eigenvalue \(1\). Averaging \(X\) over all simultaneous row-column conjugations by permutation matrices yields \(U_n\). The Schatten norms are convex and invariant under orthogonal conjugation; since \(I_n\) is fixed by these conjugations,
\[
\operatorname{dist}_{S_p}(I_n,\mathcal D_n)=\|I_n-U_n\|_{S_p}=\frac n{n-1}(n-1)^{1/p}.\tag{7}
\]
Write \(E=\mathbf1\mathbf1^{\mathsf T}/n\). A permutation matrix \(P\) acts orthogonally on \(\mathbf1^\perp\) and fixes \(\mathbf1\). On \(\mathbf1^\perp\), the normal matrix \(P-U_n\) is \(P+I_n/(n-1)\); on \(\mathbb R\mathbf1\), it vanishes. Its singular values are \(|\lambda+1/(n-1)|\), where \(\lambda\) ranges through the \(n-1\) unit-modulus eigenvalues of the restricted permutation. Each is at most \(n/(n-1)\), with equality only for \(\lambda=1\). Therefore
\[
\operatorname{dist}_{S_p}(P,\mathcal D_n)\le\|P-U_n\|_{S_p}
\le n(n-1)^{1/p-1}.
\]
For finite \(p\), the second inequality is strict unless \(P=I_n\). Convexity then extends (7) to all \(A\in\mathcal B_n\), with the stated farthest-point uniqueness for finite \(p\). For \(p=\infty\), the same argument proves the exact supremum without an exclusivity assertion.

**4. Nearest-point endpoint transition.** For \(1<p<\infty\), the strictly convex Schatten norm gives uniqueness of the nearest point \(U_n\). At \(p=\infty\), put \(T=I_n-X\) for \(X\in\mathcal D_n\). On \(\mathbf1^\perp\) this operator has trace \(n\) and dimension \(n-1\). Equality in \(\|T\|_{\mathrm{op}}\ge \operatorname{tr}(T)/(n-1)=n/(n-1)\) forces its symmetric part to be the scalar \(n/(n-1)\) identity; the operator-norm equality then forces its skew part to vanish. Hence \(T=n(I_n-E)/(n-1)\), so \(X=U_n\).

For \(p=1\), since every \(X\in\mathcal D_n\) has zero trace, \(\|I_n-X\|_{S_1}\ge\operatorname{tr}(I_n-X)=n\). Equality in this trace-nuclear inequality holds exactly when \(I_n-X\) is positive semidefinite, implying \(X\) symmetric. Conversely, a symmetric doubly stochastic \(X\) has all eigenvalues at most \(1\), so \(I_n-X\) is positive semidefinite. This proves (4). With off-diagonal symmetric entries regarded as \(\binom n2\) edge weights, the \(n\) independent vertex-sum constraints have rank \(n\) for \(n\ge3\): a dependency would satisfy \(a_i+a_j=0\) for all distinct \(i,j\), implying all \(a_i=0\). Since \(U_n\) has strictly positive allowed entries, the affine dimension is \(\binom n2-n=n(n-3)/2\).

## Verification
Run `python3 verify_derangement_projection.py` with the Python standard library to enumerate every permutation of orders \(3\) through \(7\) (\(5{,}910\) total), reconstruct its proposed projection as exact fractions, check all doubly stochastic constraints and row/column-potential optimality inequalities, and confirm every shell and multiplicity. Run `python3 independent_scipy.py` where NumPy and SciPy are available for an independent constrained least-squares comparison and spectral singular-value checks. The independent minimization inspected \(18\) representative permutation cases at orders \(3\)–\(6\), with maximum entry discrepancy below \(5\times10^{-15}\). A separate spectral test checked \(870\) permutation matrices. The all-order proof is the explicit inequalities and spectral argument above, not extrapolation of these finite checks.

## Relationship to prior work
Johnston–Kayll–Palmer [1] identify derangements with perfect matchings of a complete bipartite graph with a diagonal matching removed, and study matching counts, not the least-squares projection or the geometry of distance shells. Torres [2] proves the fractional matching description for bipartite matching polytopes, justifying the face's convex representation; it does not supply a metric nearest-point formula. Bouthat–Mashreghi–Morneau-Guérin [3] compute Chebyshev centers and radii of the **whole** Birkhoff polytope under Schatten norms; enclosing balls about fixed centers do not determine projections **onto the zero-diagonal face**. A related public calculation [4] determines the Löwner ellipsoid *enclosing* the derangement polytope; it does not cover its distance from individual full-Birkhoff vertices, the sharp gap, or the nuclear nearest-point locus. The unscaled projection formula (5), full fixed-point spectrum (1), and nearest-point endpoint transition (4) are the substantive contributions proposed here. No claim is made that the face description, derangement counts, or Schatten norm definitions are new.

## Limitations
Historical originality is best-knowledge, not a proof of priority: an older unindexed result under zero-diagonal transportation, assignment-projection, or derangement-polytope terminology could imply some or all statements. The full Schatten nearest-point maps away from the identity are not classified, nor are all spectral-norm farthest points. The squared gap applies only to permutation vertices. Finite computational checks are not infinite proofs. No independent mathematical audit has been performed.

## References
1. D. Johnston, P. M. Kayll, C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319, first publicly submitted 2022-09-22, https://arxiv.org/abs/2209.11319.
2. J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910, first publicly submitted 2023-06-20, https://arxiv.org/abs/2306.11910.
3. L. Bouthat, J. Mashreghi, F. Morneau-Guérin, *On the Geometry of the Birkhoff Polytope. II. The Schatten p-norms*, arXiv:2310.14043, first publicly submitted 2023-10-21, https://arxiv.org/abs/2310.14043.
4. *Exact Löwner ball and two-class isotropic contacts of derangement matching polytopes*, publicly indexed mathematical record (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-l-wner-ball-and-two-class-isotropic-contacts-of-derangemen--eeae40a3d5d5.
