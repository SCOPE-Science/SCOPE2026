# Exact orthogonality locus and two basis strata for four-sample quadratic chirps

## Finding

Let \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). For \((\alpha,\beta)\in(\mathbb R/2\pi\mathbb Z)^2\), define the four-sample quadratic-phase vector
\[
U(\alpha,\beta)=\bigl(e^{i(\alpha n+\beta n^2)}\bigr)_{n=0}^{3}\in\mathbb C^4.
\]
The exact zero-coherence locus of \(U(0,0)\) is one closed circle and six isolated points in the phase torus. More precisely, put
\[
r=e^{i(\alpha+\beta)},\qquad t=e^{i(\alpha+3\beta)}.
\]
Then
\[
\langle U(0,0),U(\alpha,\beta)\rangle=0
\quad\Longleftrightarrow\quad
(r,t)\in E,
\qquad
E=\{(z,-1):z\in\mathbb T\}\cup\{(-1,1),(i,i),(-i,-i)\}.
\]
Each isolated point of \(E\) has exactly two lifts in the original phase torus; the circle has one connected lift.

**Complete-basis classification.** Four vectors from this phase family are mutually orthogonal if and only if, after a common phase-parameter translation, reordering columns, and identifying parameter pairs producing the same sample vector, their associated \((r,t)\)-pairs are exactly one of the following two types:
\[
\begin{aligned}
\mathrm{A}(z)&=\{(1,1),(-1,1),(z,-1),(-z,-1)\},&&z\in\mathbb T,\\
\mathrm{B}&=\{(1,1),(i,i),(-1,-1),(-i,-i)\}.
\end{aligned}
\]
Thus every orthogonal quadratic-chirp basis of \(\mathbb C^4\) belongs to one continuous normalized stratum or one isolated normalized configuration, under **only the stated chirp-preserving equivalences**. In particular, if the four combined phase coordinates \(e^{i(\alpha+3\beta)}\) are distinct, they form a rotated fourth-root set; three distinct values never occur in a four-column orthogonal basis. If they are not all distinct, exactly two values occur, each twice, and those two are antipodal. Every basis has four vectors of squared norm \(4\), so division by \(2\) makes it orthonormal.

## Assumptions and scope

All \(\alpha,\beta\) are unrestricted real phases modulo \(2\pi\); no rationality, finite alphabet, physical range-angle feasibility, or nonzero-curvature restriction is imposed. Inner products are the standard Hermitian product on \(\mathbb C^4\). The parameter-map alias \((\alpha,\beta)\mapsto(\alpha+\pi,\beta+\pi)\) leaves all four entries unchanged; this is the only nontrivial alias. A common phase-parameter translation means adding a fixed pair \((\alpha_0,\beta_0)\) to all parameters. It is not permission to permute measurement rows or apply an arbitrary diagonal unitary, which would change the sampled-chirp parameterization.

The claim concerns the exact finite four-sample quadratic exponential sum and maximal orthogonal families of cardinality four. It does not classify arbitrary nonmaximal families, physical steering geometries with constrained angles/ranges, nor general aperture sizes.

## Proof

### 1. Parametrization and the twofold alias

The linear phase-coordinate map is
\[
(\alpha,\beta)\longmapsto(\alpha+\beta,\alpha+3\beta)\pmod{2\pi}.
\]
Its integer matrix has determinant \(2\), so it is onto the two-torus with a two-element kernel \(\{(0,0),(\pi,\pi)\}\). Directly evaluating the four samples gives the exact identity
\[
U(\alpha,\beta)=V(r,t):=(1,r,rt,t^3).
\]
In particular, the vector is entirely specified by \((r,t)\in\mathbb T^2\), and conversely every such pair occurs.

### 2. All coherence zeros

For \(V(1,1)=(1,1,1,1)\), the inner product is
\[
F(r,t):=\langle V(1,1),V(r,t)\rangle=1+r+rt+t^3.
\]
If \(t=-1\), both \(1+t\) and \(1+t^3\) vanish, so \(F(r,-1)=0\) for every \(r\in\mathbb T\). If \(t\ne-1\), the equation uniquely determines
\[
r=-\frac{1+t^3}{1+t}=-(t^2-t+1).
\]
Writing \(t=e^{i\theta}\) yields \(t^2-t+1=t(2\cos\theta-1)\). Therefore \(|r|=1\) is equivalent to \(|2\cos\theta-1|=1\), whence \(\cos\theta\in\{0,1\}\). Consequently \(t\in\{1,i,-i\}\), with respectively \(r=-1,i,-i\). This proves the displayed zero set \(E\) without omitted boundary cases.

Because \(\alpha+3\beta=\pi\pmod{2\pi}\) is one primitive integral torus equation, its lift is one connected circle. Each of the three remaining points of \(E\) has two lifts under the determinant-two covering, giving exactly six isolated phase points.

### 3. The complete pairwise-orthogonality graph

Entrywise multiplication by a quadratic-phase vector is unitary. Hence
\[
\langle V(r_1,t_1),V(r_2,t_2)\rangle=0
\quad\Longleftrightarrow\quad
(r_2/r_1,t_2/t_1)\in E.
\]
Translate all parameters to make one of any four selected points equal to \((1,1)\). Every other point must lie in \(E\). Write the continuous branch as \(L_z=(z,-1)\), and the three off-circle points as \(A=(-1,1)\), \(B=(i,i)\), \(C=(-i,-i)\).

Two distinct points \(L_z,L_w\) are orthogonal exactly when \(w=-z\), because their ratio has second coordinate \(1\) and \(E\) has exactly the off-circle point \((-1,1)\) with that coordinate. Thus an orthogonal set contains at most two points on the continuous branch. Among the three off-circle points, \(B\) and \(C\) are orthogonal (ratio \((-1,-1)\)), but \(A\) is orthogonal to neither \(B\) nor \(C\) (their ratios have second coordinate \(i\) or \(-i\) with the wrong first coordinate).

To make a four-point clique including the identity, at least one of the three other points must lie on the continuous branch. If two do, they are \(L_z,L_{-z}\), and the remaining off-circle point must be \(A\): \(A\) is orthogonal to both, while \(B\) and \(C\) each require its line partner to have first coordinate \(-1\), impossible simultaneously for \(z\) and \(-z\). This is precisely \(\mathrm{A}(z)\).

If only one point lies on the continuous branch, the other two must be \(B,C\). For \(L_z\) to be orthogonal to either \(B\) or \(C\), the exact ratio criterion forces \(z=-1\). This gives precisely \(\mathrm{B}\). No four-point clique can have zero or three line-branch elements. Thus the listed types exhaust every possibility.

### 4. Attainment and rigidity

For every \(z\in\mathbb T\), the four vectors corresponding to \(\mathrm{A}(z)\) are the columns of
\[
H_{\mathrm A}(z)=
\begin{pmatrix}
1&1&1&1\\
1&-1&z&-z\\
1&-1&-z&z\\
1&1&-1&-1
\end{pmatrix}.
\]
Their pairwise inner products vanish by the preceding ratio test, or by direct multiplication, and every column has squared norm \(4\). For \(\mathrm B\), the corresponding four columns form the discrete Fourier matrix
\[
H_{\mathrm B}=\begin{pmatrix}
1&1&1&1\\
1&i&-1&-i\\
1&-1&1&-1\\
1&-i&-1&i
\end{pmatrix},
\qquad H_{\mathrm B}^{*}H_{\mathrm B}=4I.
\]
Thus both types are attained. The second coordinates of the four points are \(\{1,1,-1,-1\}\) for type A and \(\{1,i,-1,-i\}\) for type B. Multiplying all of them by a common phase and permuting the four points preserves multiplicities, so no allowed chirp-preserving equivalence identifies the types. This also proves the distinct-coordinate and no-three-coordinate consequences.

## Verification

The standalone file `checker.py` performs exact rational-complex arithmetic, tests all rational unit-circle parameters obtained from the stated bounded rational parametrization, verifies the Fourier configuration, and exhaustively classifies four-cliques in the sixteen-point fourth-root phase grid. On execution it reports \(48\) distinct rational-circle parameters, \(16\) phase-grid vertices, \(12\) four-cliques (\(8\) continuous-type and \(4\) isolated-type), and \(56\) zero-orthogonality edges. The universal classification is proved analytically above; neither the rational samples nor the fourth-root grid establish it on their own.

Run with `python3 checker.py` in a directory containing the standalone checker; no third-party packages are required.

## Relationship to prior work

Daei, Fodor and Skoglund (first posted 2026-09-25) formulate Fresnel steering atoms on a finite aperture as quadratic exponential phases and study uniform sparse super-resolution via QPAC (model in §2.1 and Theorem 2.3). Their main theorem assumes at least ten aperture samples and concerns support recovery, not all zero-coherence differences or orthogonal bases for exactly four samples.

Tadej and Życzkowski's earlier classification (§5.4) establishes that every abstract \(4\times4\) complex Hadamard matrix is equivalent to a member of a one-parameter family under arbitrary diagonal-unitary factors and row/column permutations. That is a stronger ambient-matrix classification but uses a broader equivalence relation: it does **not** identify the complete inverse image inside the constrained quadratic-phase steering manifold or distinguish the two patterns under common chirp-parameter translation and column permutation. The displayed exact zero set and coordinate-multiplicity rigidity are additional, structure-preserving statements; no novelty is claimed for the abstract Hadamard family itself.

Indexed related work on finite prime-field parabola Fourier zeros, phase-only four-point finite Fourier supports, and odd-prime quadratic-chirp phase Hessians concerns different discrete fields, supports, or objectives. Their known conclusions do not imply the stated four-sample continuous two-torus zero locus or basis stratification.

## Limitations

This is a complete result only for four consecutive unweighted samples, unrestricted two-phase torus parameters, and exactly four mutually orthogonal vectors. The phase-parameter torus can contain combinations of frequencies/curvatures that are not simultaneously physically accessible under fixed ranges, angular windows, or wavelength constraints; no physical four-source realization is claimed. The full four-dimensional complex Hadamard classification is pre-existing. A mathematically equivalent formulation may exist in older phased-array or Hadamard design literature; independently exhaustive bibliographic review is not asserted. There is no theorem here about larger apertures, nonuniform tapers, approximate orthogonality, or incomplete orthogonal families.

## References

1. S. Daei, G. Fodor, M. Skoglund, *A Mathematical Theory of Near-Field Super-Resolution*, arXiv:2609.31299, first publicly posted 2026-09-25, §2.1 and Theorem 2.3. https://arxiv.org/abs/2609.31299
2. W. Tadej, K. Życzkowski, *A concise guide to complex Hadamard matrices*, arXiv:quant-ph/0512154, §2 Definition 2.2 and §5.4 (originally posted 2005-12-19). https://arxiv.org/abs/quant-ph/0512154
