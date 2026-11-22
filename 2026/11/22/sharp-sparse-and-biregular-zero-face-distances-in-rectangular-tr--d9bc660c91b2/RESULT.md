# Sharp sparse and biregular zero-face distances in rectangular transportation polytopes

## Finding
Let \(m,n\ge2\) be unequal integers. For a subset \(F\subseteq[m]\times[n]\), let \(\mathcal T(F)\) be the nonnegative \(m\times n\) matrices with every row sum \(1/m\), every column sum \(1/n\), and entries zero at all cells of \(F\). Write \(U\) for the constant matrix with entries \(1/(mn)\), and \(d(F)=\min_{X\in\mathcal T(F)}\|X-U\|_F\) whenever the face is nonempty. Let \(k=|F|\), row forbidden degrees \(r_i\) and column forbidden degrees \(c_j\).

**Sparse optimal zero patterns.** For every integer \(2\le k\le\min(m,n)\), every nonempty \(\mathcal T(F)\) satisfies
\[
d(F)^2\ge\frac{k}{mn((m-1)(n-1)+k-1)}.
\]
Equality holds **if and only if** \(F\) is a partial matching: no forbidden cells share a row or column. Consequently all such matching masks attain the global minimum, and every other feasible mask is strictly farther from \(U\).

**Biregular optimal zero patterns.** If \(0<k<mn\) is divisible by both \(m\) and \(n\), every nonempty \(\mathcal T(F)\) satisfies
\[
d(F)^2\ge\frac{k}{mn(mn-k)}.
\]
Equality holds **if and only if** each row has \(k/m\) forbidden cells and each column has \(k/n\) forbidden cells. Such biregular masks always exist, and their unique nearest matrices are zero on \(F\) and constant \(1/(mn-k)\) elsewhere.

For every nonempty proper coordinate-zero face, the universal degree-sensitive bound is
\[
d(F)^2\ge\frac{k^2}{m^2n^2G(F)},\qquad
G(F)=k-\frac{k^2}{mn}-\frac1n\sum_{i=1}^m\left(r_i-\frac{k}{m}\right)^2-\frac1m\sum_{j=1}^n\left(c_j-\frac{k}{n}\right)^2>0.
\]
This bound is attained in each of the two equality regimes above.

## Assumptions and scope
All distances use the unscaled Frobenius norm in \(\mathbb R^{m\times n}\). The transportation polytope has total mass one, not row and column sums one simultaneously. The mask is a set of **required zeros**, and \(\mathcal T(F)\) must be nonempty; the claim does not assume every mask is feasible. The condition \(m\ne n\) isolates the unequal rectangular setting. The two sharp regimes are separate; no assertion of a universal closed-form optimizer for arbitrary intermediate \(k\) is made. Biregular masks require the stated divisibility, and their existence construction below uses both conditions.

## Proof
Let \(\mathcal L\) be the linear subspace of real matrices with all row and column sums zero. Its orthogonal projector is
\[
(PY)_{ij}=Y_{ij}-\frac1n\sum_{b=1}^nY_{ib}-\frac1m\sum_{a=1}^mY_{aj}+\frac1{mn}\sum_{a,b}Y_{ab}.
\]
Let \(B=1_F\). Every \(X\in\mathcal T(F)\) has \(Z=X-U\in\mathcal L\) and \(\langle Z,B\rangle=-k/(mn)\), because its \(k\) forbidden coordinates vanish. Hence \(\langle Z,PB\rangle=-k/(mn)\). Cauchy–Schwarz gives
\[
\|X-U\|_F^2\ge\frac{k^2}{m^2n^2\|PB\|_F^2}.
\]
Expanding the projector and collecting row and column degrees gives
\[
\|PB\|_F^2=k-\frac1n\sum_i r_i^2-\frac1m\sum_jc_j^2+\frac{k^2}{mn}=G(F).
\]
Feasibility makes this quantity strictly positive, since otherwise \(\langle Z,PB\rangle\) would vanish, contradicting \(k>0\). The degree-variance version follows by completing squares.

In the sparse regime, nonnegative integer degrees satisfy \(\sum_i r_i^2\ge k\) and \(\sum_jc_j^2\ge k\); simultaneous equality means every degree is zero or one, exactly the partial-matching property. Consequently
\[
G(F)\le \frac{k((m-1)(n-1)+k-1)}{mn}.
\]
Set \(D=(m-1)(n-1)+k-1\). For a matching mask, let \(B=1_F\) and put \(X^*=U-PB/D\). On each forbidden cell \((PB)_{ij}=D/(mn)\), so \(X^*_{ij}=0\). On other cells the four possible entries of \(X^*\), according to whether their row and column are used by \(F\), are
\[
\begin{array}{c|cc}
&\text{used column}&\text{unused column}\\\hline
\text{used row, off }F&1/D&(m-1)/(mD)\\
\text{unused row}&(n-1)/(nD)&(mn-m-n)/(mnD)
\end{array}.
\]
All are nonnegative because \(m,n\ge2\) and \(m\ne n\) imply \(mn-m-n\ge0\). Since \(PB\in\mathcal L\), the row and column sums of \(X^*\) are the required margins. Thus it is feasible. It is a scalar multiple of \(PB\) away from \(U\), so Cauchy–Schwarz is equality and its squared distance is exactly \(k/(mnD)\). Strict convexity of squared Euclidean distance gives uniqueness of the nearest matrix. Conversely, attaining this global minimum forces both degree-square inequalities to be equalities, hence a matching.

In the biregular regime, Cauchy–Schwarz applied separately to the degree sequences yields \(\sum_i r_i^2\ge k^2/m\), \(\sum_jc_j^2\ge k^2/n\), with simultaneous equality exactly when \(r_i=k/m\) and \(c_j=k/n\). It follows that \(G(F)\le k(1-k/(mn))\). If the mask is biregular, define \(X^*_{ij}=0\) on \(F\) and \(X^*_{ij}=1/(mn-k)\) off it. Each row has \(n-k/m\) allowed cells, and each column has \(m-k/n\). Hence the row sum is \(1/m\), the column sum is \(1/n\), and direct subtraction from \(U\) gives \(\|X^*-U\|_F^2=k/[mn(mn-k)]\). This attains the lower bound, proves uniqueness of the nearest point, and forces biregularity in every equality case. To construct a biregular mask, put \(r=k/m\) and, in row \(i=0,\dots,m-1\), forbid the columns \((ir+t)\bmod n\) for \(t=0,\dots,r-1\). Because \(mr=k\) is divisible by \(n\) and \(r<n\), every column is forbidden exactly \(k/n\) times.

## Verification
The standalone program `verify_transport.py` checks the projection and degree identities using exact rational arithmetic, constructs the nearest matrices and verifies their row sums, column sums, nonnegativity, zero constraints and squared distances in all unequal dimensions \(2\le m,n\le15\). It checks matching masks for all \(1\le k\le\min(m,n)\) and all existing nontrivial biregular sizes. Optional SciPy constrained quadratic optimizations test 941 feasible nonmatching masks of sizes up to \(4\times5\), including strict gaps when degrees collide. These finite computations are diagnostics, not substitutes for the two arbitrary-dimension proofs above.

## Relationship to prior work
Torres (2023) develops the convex framework of bipartite matching polytopes, while Koehl (2024) studies the combinatorics and extreme points of rectangular transportation polytopes. Neither inspected text addresses the distance from the uniform matrix to coordinate-zero faces *optimized over all masks of a fixed size*. Calvillo and Romero (2016) give an algorithm for the closest-to-origin point in a general transportation polytope with specified positive margins; that algorithm is distinct from the present classification of masks minimizing center-to-face Euclidean distance. Achilles (1977) investigates doubly stochastic matrices with prescribed zeros and is a relevant historical priority risk for square specializations, which are not claimed here. Other general quadratic-programming methods provide algorithms, not these sharp mask classifications as stated. This distinction does not establish global priority beyond the inspected sources.

## Limitations
This is a result for unequal rectangular uniform-margin polytopes and the two stated mask-density regimes. It does not solve arbitrary intermediate cardinalities, unequal margins, or a full face-distance spectrum. A 1977 paper on fixed zero patterns in square doubly stochastic matrices was available only through bibliographic and abstract material during this review; its full theorem could not be compared. The earlier general minimum-norm transportation literature could conceivably yield a stronger reformulation; historical-priority uncertainty remains. No independent audit has been performed.

## References
1. J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1 (first public June 20, 2023). https://arxiv.org/pdf/2306.11910
2. P. Koehl, *Extreme Points of General Transportation Polytopes*, arXiv:2404.16791v1 (first public April 25, 2024). https://arxiv.org/pdf/2404.16791
3. G. Calvillo and D. Romero, *On the Closest Point to the Origin in Transportation Polytopes*, Discrete Applied Mathematics 210 (2016), 88–102. DOI: 10.1016/j.dam.2015.01.027.
4. A. Bachem and B. Korte, *Minimum Norm Problems over Transportation Polytopes*, Linear Algebra and its Applications 31 (1980), 103–118.
5. E. Achilles, *Permanents of Doubly Stochastic Matrices with Fixed Zero Pattern*, Linear and Multilinear Algebra 5 (1977), 63–70. DOI: 10.1080/03081087708817175.
