# Exact spectrum and fourth-power conditioning of the quadratic Walsh transform on Boolean two-balls

## Finding
For every integer \(n\ge4\), consider the square real matrix \(H_n\) indexed by the Boolean two-ball \(B_{n,2}=\{A\subseteq[n]:|A|\le2\}\), with entries \(H_n(A,B)=(-1)^{|A\cap B|}\). The full real eigenvalue multiset is: the three roots of
\[
P_n(t)=t^3-\frac{n^2-7n+14}{2}t^2-(n^2-n+2)t+8,
\]
each counted once; the two numbers
\[
-(n-3)\pm\sqrt{(n-3)^2+8},
\]
each with multiplicity \(n-1\); and \(4\) with multiplicity \(n(n-3)/2\). Coincident values are counted with their listed multiplicities. In particular \(H_n\) is invertible,
\[
\det H_n=(-2)^{n^2},\qquad\operatorname{inertia}(H_n)=\left(1+\binom n2,n,0\right),
\]
and its spectral two-norm condition number satisfies
\[
\lim_{n\to\infty}\frac{\kappa_2(H_n)}{n^4}=\frac1{16}.
\]

## Assumptions and scope
The matrix is unnormalized; row and column indices are all subsets of cardinality zero, one or two, in any matching order. The eigenvalues are independent of a common simultaneous permutation. The spectral condition number is the ratio of the largest to smallest singular value. No assertion is made about degrees above two, other sample domains, or numerical floating-point stability beyond the exact asymptotic condition ratio.

## Proof
For \(A,B\subseteq[n]\) the binomial identity gives
\[
(-1)^{|A\cap B|}=\sum_{C\subseteq A\cap B}(-2)^{|C|}.
\]
Let \(Z_{A,C}={\bf1}_{C\subseteq A}\) for \(A,C\in B_{n,2}\), and \(D_{C,C}=(-2)^{|C|}\). Then \(H_n=ZDZ^{\mathsf T}\). Ordering subsets by size makes \(Z\) unit triangular. Thus its determinant is one, and Sylvester's inertia law gives exactly \(1+\binom n2\) positive, \(n\) negative and no zero eigenvalues, while
\[
\det H_n=(-2)^{n+2\binom n2}=(-2)^{n^2}.
\]

We now diagonalize with respect to coordinate permutations. The spaces of functions on subsets of cardinalities zero, one and two decompose orthogonally into: a three-dimensional constant-on-each-size sector, two copies of the standard representation of dimension \(n-1\), and one degree-two sector of dimension \(n(n-3)/2\). For the latter sector a vector supported on unordered pairs with vanishing sum over all pairs incident to every coordinate is orthogonal to constant and standard sectors. On the pair level, \((-1)^{|A\cap B|}=1-2|A\cap B|+4{\bf1}_{A=B}\), so every such vector is an eigenvector of eigenvalue \(4\), and its dimension is \(\binom n2-n=n(n-3)/2\).

In the standard sector, take any singleton coefficient vector \((x_i)\) with \(\sum_ix_i=0\), and pair coefficients \((x_i+x_j)/\sqrt{n-2}\). Each has the same squared norm, and these bases are mutually orthogonal. Directly summing intersections gives the symmetric block
\[
-2\begin{pmatrix}1&\sqrt{n-2}\\\sqrt{n-2}&n-4\end{pmatrix},
\]
whose eigenvalues are \(-(n-3)\pm\sqrt{(n-3)^2+8}\).

On the three unit cardinality-indicator vectors the matrix is
\[
R_n=\begin{pmatrix}
1&\sqrt n&\sqrt{\binom n2}\\
\sqrt n&n-2&(n-4)\sqrt{(n-1)/2}\\
\sqrt{\binom n2}&(n-4)\sqrt{(n-1)/2}&\binom n2-4(n-2)
\end{pmatrix}.
\]
Its trace is \((n^2-7n+14)/2\), sum of pairwise eigenvalue products is \(-(n^2-n+2)\), and determinant is \(-8\). Its characteristic polynomial is therefore \(P_n\), completing the multiplicity classification since the sector dimensions sum to \(1+n+\binom n2\).

For asymptotic conditioning, the largest radial root is asymptotic to \(n^2/2\). Dividing \(P_n(t)\) by \(n^2\) at bounded \(t\) shows that a second radial root tends to \(-2\), while the third tends to zero. The product of the roots equals \(-8\), hence the small positive radial root is asymptotic to \(8/n^2\). The two standard eigenvalues are asymptotic to \(-2n\) and \(4/n\), and all remaining eigenvalues are \(4\). Consequently the smallest singular value is asymptotic to \(8/n^2\), and the largest is asymptotic to \(n^2/2\). Their ratio is asymptotic to \(n^4/16\). This also proves the claimed asymptotic independent of accidental eigenvalue coincidences.

## Verification
The finite checker `CHECK.py` directly constructs the unnormalized Walsh matrix and compares its numerical symmetric eigenspectrum to the three predicted spectral sectors for every integer dimension from four through thirteen. It separately checks inertia and the logarithm of the absolute determinant. These finite computations are corroboration only; all-dimensional claims follow from the exact incidence factorization and the symmetry decomposition given above. Run with `python CHECK.py` in a Python environment with NumPy.

## Relationship to prior work
This is a discrete analogue of spatial-spectral concentration and concerns recovering all quadratic-degree Boolean Fourier coefficients from values on a sparse radius-two Hamming ball. The Slepian ball setting of Khalid, Kennedy and McEwen concerns continuous Fourier-Bessel and Fourier-Laguerre transforms in a three-dimensional ball. Mixon and Peterson address learning Boolean functions with concentrated Fourier spectra, not the exact eigenvalues of this square radius-two Walsh submatrix. Related known results on first-degree bands over Boolean balls, and quadratic bands over fixed-weight shells, involve different row/column sets; fixed-weight sampling has a degree-one nullspace whereas this square two-ball matrix is invertible. The present statement is narrower than arbitrary ball/spectral-band theory and does not assert novelty against every possible earlier representation-theoretic reformulation.

## Limitations
The result gives an exact spectrum and asymptotic two-norm conditioning, not a uniform finite-dimensional error bound in a specified machine model. Historical priority against an unindexed or broader association-scheme theorem remains a risk. The numerical experiment is not a proof for untested dimensions. Independent validation has not been performed.

## References
1. Z. Khalid, R. A. Kennedy and J. D. McEwen, *Slepian Spatial-Spectral Concentration on the Ball*, arXiv:1403.5553v1 (2014-03-21), https://arxiv.org/abs/1403.5553.
2. D. G. Mixon and C. Peterson, *Learning Boolean Functions with Concentrated Spectra*, arXiv:1507.04319v1 (2015-07-15), https://arxiv.org/abs/1507.04319.
