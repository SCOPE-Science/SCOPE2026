# A ternary incenter transition in three-row Monge polytopes

## Finding
For every integer \(q\ge4\), consider the normalized nonsymmetric \(3\times q\) Monge polytope
\[
\mathcal M_{3,q}=\left\{C\in\mathbb R_{\ge0}^{3\times q}:\sum_{i=1}^3\sum_{j=1}^q c_{ij}=1,\quad c_{ij}+c_{i+1,j+1}\le c_{i,j+1}+c_{i+1,j}\ \ (i=1,2;\ 1\le j<q)\right\}.
\]
Equip the affine sum-one hyperplane with the intrinsic Frobenius metric. Define
\[
L_q=\sqrt{1-\frac1{3q}},\qquad T_q=2\left\lfloor\frac{q^2}{3}\right\rfloor,\qquad
\boxed{\ r_q=\frac1{3qL_q+2T_q}=\frac1{3q\sqrt{1-1/(3q)}+4\lfloor q^2/3\rfloor}.\ }
\]
Then \(r_q\) is the exact radius of the largest contained Euclidean ball. Every possible center of such a ball is parametrized as follows. Choose \((a,b)\) in the indicated set:
\[
\begin{array}{c|c|c}
q & a & b\\ \hline
3m\ (m\ge2)&[m,m+1]&[2m,2m+1]\\
3m+1&m+1&2m+1\\
3m+2&m+1&2m+2
\end{array}
\]
For each column \(1\le j\le q\), put
\[
h_j=\max\{0,a-j,j-b\},\qquad
z_{1j}=h_j+j-a,\quad z_{2j}=h_j,\quad z_{3j}=h_j+b-j,
\]
and set
\[
\boxed{\ c_{ij}=r_qL_q+2r_q z_{ij}.\ }
\]
These formulas produce *all* maximum-ball centers without duplication. Hence the incenter locus is a two-dimensional affine parallelogram when \(3\mid q\), and a single point when \(3\nmid q\). This gives a genuine period-three transition in center uniqueness, rather than a parity effect.

Every maximum ball touches all \(2(q-1)\) adjacent Monge facets. When \(3\nmid q\), precisely \(q+2\) coordinate facets also touch it, for a total of \(3q\) tangent facets. When \(q=3m\), a center with parameters \((a,b)\) has exactly
\[
\boxed{\ 3q-2+\mathbf1_{a\in\{m,m+1\}}+\mathbf1_{b\in\{2m,2m+1\}}\ }
\]
tangent facets. Thus the interior of the incenter parallelogram has \(3q-2\) tangencies, its open sides have \(3q-1\), and its four vertices have \(3q\). The already-known square case \(q=3\) also satisfies the same formulas, but is excluded from the originality claim.

## Assumptions and scope
The matrix is normalized by the sum of all \(3q\) entries and is not assumed symmetric. Coordinates are in the standard orthonormal matrix basis; arbitrary affine transformations need not preserve these radii. The inequalities written above are irredundant facets by Erickson and Kretschmann, Theorem 5.3 (2023), including the \(3q\) coordinate facets. In particular, distances to their supporting hyperplanes characterize ball containment. The result is about maximum inscribed *balls*, not minimum enclosing balls or maximum-volume ellipsoids.

## Proof
**1. Intrinsic facet distances.** The tangent space to the sum-one affine hyperplane is \(H=\{X:\sum_{ij}X_{ij}=0\}\). The orthogonal projection of a coordinate unit normal to \(H\) has length \(L_q\); an adjacent four-term Monge normal already lies in \(H\) and has length \(2\). Therefore a ball with center \(C\) and radius \(r>0\) lies inside \(\mathcal M_{3,q}\) if and only if
\[
c_{ij}\ge rL_q,\qquad
c_{i,j+1}+c_{i+1,j}-c_{ij}-c_{i+1,j+1}\ge2r
\]
for each specified index. Setting \(Z=(C-rL_q\mathbf1)/(2r)\) turns these into \(Z\ge0\) and adjacent Monge slacks \(A_{ij}\ge1\), while the normalization becomes
\[
1=r\bigl(3qL_q+2\sum_{ij}z_{ij}\bigr).
\]
It remains to minimize \(\sum z_{ij}\) over these nonnegative slack arrays and classify equality.

**2. An exact dual bound.** For \(0\le j\le q\), define the two integer tents
\[
u_j=\min\{2j,q-j\},\qquad v_j=\min\{j,2(q-j)\},
\]
so \(u_0=u_q=v_0=v_q=0\) and \(u_j,v_j>0\) for \(1\le j<q\). Let \(\delta u_j=u_j-u_{j-1}\) and similarly \(\delta v_j\). Summation by parts gives the exact identity
\[
\sum_{j=1}^{q-1}(u_j A_{1j}+v_j A_{2j})=
\sum_{j=1}^q\bigl[-\delta u_j\,z_{1j}+(\delta u_j-\delta v_j)z_{2j}+\delta v_j\,z_{3j}\bigr].
\]
Each of the three displayed coefficients is at most \(1\): the first differences of the two minimum-of-lines tents are piecewise \((2,1)\), \((-1,1)\), \((-1,-2)\), with one intermediate transition pair \((0,1)\) and \((-1,0)\) if \(q\equiv1\pmod3\), or \((1,1)\) and \((-1,-1)\) if \(q\equiv2\pmod3\). Hence for nonnegative \(Z\) with all \(A_{ij}\ge1\),
\[
\sum_{ij}z_{ij}\ \ge\ \sum_{j=1}^{q-1}(u_j A_{1j}+v_j A_{2j})\ \ge\ \sum_{j=1}^{q-1}(u_j+v_j)
=2\left\lfloor\frac{q^2}{3}\right\rfloor=T_q.
\]
The final sum follows by splitting the integer tents at the nearest one-third positions (and using \(v_j=u_{q-j}\)). Equality forces *every* adjacent slack to equal \(1\), because all interior tent weights are positive.

**3. Complete equality classification.** If each slack equals \(1\), the difference between the first and second rows rises by one per column, as does the difference between the second and third. Thus, for real constants \(a,b\), necessarily
\[
z_{1j}=h_j+j-a,\qquad z_{2j}=h_j,\qquad z_{3j}=h_j+b-j.
\]
The dual coefficient of \(z_{2j}\) at \(j=\lceil q/2\rceil\) is strictly below \(1\); equality in step 2 therefore forces this middle entry to vanish. Nonnegativity of the first and third entries there gives \(a\le\lceil q/2\rceil\le b\), so \(a\le b\). For any column, if the three entries had a common strictly positive offset above their smallest feasible value, decreasing that column's three entries together would preserve all slacks and nonnegativity while decreasing the total mass, contradicting step 2. Consequently equality requires
\[
h_j=\max\{0,a-j,j-b\}.
\]
For \(a\le b\), the resulting mass separates into two convex piecewise-linear functions:
\[
S_q(a,b)=q(b-a)+3\sum_{j=1}^q(a-j)_++3\sum_{j=1}^q(j-b)_+.
\]
The minimizers of the \(a\)-part have \(\#\{j<a\}\) closest to \(q/3\); those of the \(b\)-part have \(\#\{j>b\}\) closest to \(q/3\). Explicitly, if \(q=3m\), the minimizing \(a\) range is \([m,m+1]\) and minimizing \(b\) range is \([2m,2m+1]\); if \(q=3m+1\) they are \(a=m+1,b=2m+1\); if \(q=3m+2\), they are \(a=m+1,b=2m+2\). All these pairs satisfy \(a\le b\). At the convenient integral choice \(a=\lceil q/3\rceil\), \(b=q+1-a\),
\[
S_q(a,b)=q(q+1-2a)+3a(a-1)=2\left\lfloor\frac{q^2}{3}\right\rfloor=T_q.
\]
Therefore the dual bound is attained, and the listed pairs are exactly its minimizers.

**4. Inradius, centers and all tangent facets.** Step 1 and the lower bound give \(r\le(3qL_q+2T_q)^{-1}\). For each minimizing pair from step 3, the constructed nonnegative matrix has every adjacent Monge slack exactly one and total mass \(T_q\); scaling as in step 1 gives a feasible radius-\(r_q\) ball, so the bound is sharp. Conversely every maximum-radius center must come from a minimum-mass \(Z\), for which step 3 exhausts all possibilities. Both \(a\) and \(b\) can be recovered from the two row differences, giving injectivity; for \(3\mid q\), dependence on \((a,b)\) is affine on the indicated rectangle, so the image is a genuine parallelogram.

Every Monge facet is tangent because its slack is exactly \(2r_q\). A coordinate facet is tangent precisely when the corresponding \(z_{ij}=0\). At each column there is exactly one zero entry, except that an integer value of \(a\) adds one at column \(j=a\), and an integer value of \(b\) adds one at column \(j=b\); when \(a=b\), the common column has three zeros, which counts both extras. The parameters above give the stated counts of tangent facets. This completes the proof.

## Verification
The accompanying self-contained program `verify_monge3.py` checks exact integer dual coefficients and rational feasible minimizers, including all vertices and midpoints of the two-parameter optimal-center rectangle for \(3\mid q\), for each \(3\le q\le36\). It also checks the original ball-normalization and facet-distance identities. For \(3\le q\le16\), an independently constructed SciPy/HiGHS linear program minimizes the sum of nonnegative slack arrays and compares with \(T_q\). It passed 17,138 assertions. These finite checks do not prove the theorem for arbitrary \(q\), which follows instead from steps 1–4. The \(q=3\) calculation is included only as a compatibility check with prior square results.

Reproduction: from a directory containing `verify_monge3.py`, run `python verify_monge3.py` with Python 3, NumPy, and SciPy installed. No other files are required.

## Relationship to prior work
Erickson and Kretschmann (2023, arXiv:2311.07522, full text, especially Theorem 5.3) establish the exact polytope and its facets but not this intrinsic Euclidean classification. Erickson and Jones (2026, arXiv:2609.09508) study volume, lattice paths, and Ehrhart series of the same general family; their abstract does not state an inball or center theorem. The full 2026 text was inaccessible and is an explicit historical-priority risk, not a source of a claimed noncoverage proof.

Previously reported Euclidean incenter classifications cover the *square* normalized Monge polytope \(n\times n\) (including \(n=3\)) and the *two-row* rectangular Monge polytope \(2\times q\). The square formula has an \((n-1)\)-cube of incenters; the two-row rectangular formula has a parity-dependent segment/point locus. Neither statement implies the present \(3\times q\), \(q\ge4\), result or its period-three uniqueness and full facet-contact transition. The \(3\times3\) case of this proof agrees with and is not claimed beyond the previously reported square case. Searches for aliases including Chebyshev centers, Frobenius inballs and metric Monge polytopes did not reveal a result covering these nonsquare three-row classifications; lack of hits alone is not a proof of priority.

## Limitations
The classification requires precisely three rows, at least four columns, ordinary nonnegative normalized Monge matrices, and the induced Frobenius metric. It does not classify general rectangular \(p\times q\) Monge inballs when \(p\ge4\), weighted norms, other scalings, maximum-volume inscribed ellipsoids, or Euclidean circumradii. Independent external audit has not been performed. Historical priority is provisional because the full 2026 motivating paper and every possibly relevant unindexed source could not be exhaustively inspected.

## References
- W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first posted 2023-11-13, especially Section 5 and Theorem 5.3. https://arxiv.org/abs/2311.07522.
- W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, first posted 2026-09-08; abstract inspected, complete text not accessible. https://arxiv.org/abs/2609.09508.
- *An affine \((n-1)\)-cube of Euclidean incenters for square Monge polytopes*, publicly available manuscript, 2026-10-11, `RESULT.md`. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-affine-n-1-cube-of-euclidean-incenters-for-square-monge-polyt--b3dc6b94166a.
