# Sharp fourth moments of rank-one permutation matrix coefficients

## Finding
Let \(n\ge2\), let \(\pi\) be uniform on the symmetric group \(S_n\), and take nonzero real vectors \(a,b\in\mathbb R^n\) with \(\sum_i a_i=\sum_j b_j=0\). Set
\[
X_{a,b}(\pi)=\sum_{i=1}^n a_i b_{\pi(i)}.
\]
The exact maximal normalized fourth moment is
\[
\boxed{\sup_{a,b}\frac{\mathbb E X_{a,b}^4}{(\mathbb E X_{a,b}^2)^2}=\begin{cases}
1,&n=2,\\
\frac32,&n=3,\\
3,&n=4,\\
\frac{n^2-3n+3}{n-1},&n\ge5.
\end{cases}}
\]
All nonzero admissible pairs attain the bound for \(n=2,3\). For \(n=4\), equality holds exactly when **both** vectors, independently, are nonzero scalar multiples of a permutation of \((1,1,-1,-1)\). For \(n\ge5\), equality holds exactly when **both** vectors, independently, are nonzero scalar multiples of a permutation of \((n-1,-1,\ldots,-1)\). In the latter case \(X_{a,b}\) is proportional to the centered indicator of one permutation-coordinate event \(\{\pi(i)=j\}\). The optimizer changes from balanced coefficients at \(n=4\) to a unique exceptional coordinate in each vector at \(n=5\).

## Assumptions and scope
The field is real, the measure on \(S_n\) is uniform, and the two coefficient vectors have length \(n\), nonzero Euclidean norm, and coordinate sum zero. The class consists of **rank-one** matrix coefficients of the standard \((n-1)\)-dimensional real representation, not all linear combinations of permutation-coordinate indicators. The quotient is homogeneous under independent nonzero rescaling of either coefficient vector. The primary subject is sharp \(L^p\)-embedding constants in a finite-dimensional family.

## Proof
Normalize \(\sum_i a_i^2=\sum_j b_j^2=1\), and put \(u=\sum_i a_i^4\), \(v=\sum_j b_j^4\). By sampling a permutation without replacement,
\[
\mathbb E X_{a,b}=0,\qquad \mathbb E X_{a,b}^2=\frac1{n-1}.
\]
For \(n\ge4\), expand four copies of the sum according to the equality partition of their position indices. For a fixed partition of four positions with block sizes \(\lambda\), the ordered distinct-index sum from \(a\), multiplied by the corresponding sum from \(b\), is divided by the falling factorial \((n)_{|\lambda|}\). The five block types, their multiplicities, and their distinct-index sums for \(a\) are:

| Block sizes | Multiplicity | Distinct-index sum |
| --- | ---: | ---: |
| \((4)\) | 1 | \(u\) |
| \((3,1)\) | 4 | \(-u\) |
| \((2,2)\) | 3 | \(1-u\) |
| \((2,1,1)\) | 6 | \(2u-1\) |
| \((1,1,1,1)\) | 1 | \(3-6u\) |

The same formulas with \(v\) hold for \(b\). Summing gives the exact identity
\[
\frac{\mathbb E X_{a,b}^4}{(\mathbb E X_{a,b}^2)^2}=
R_n(u,v):=\frac{n-1}{n(n-2)(n-3)}\Bigl[n^2(n+1)uv-3n(n-1)(u+v)+3(n^2-3n+3)\Bigr]. \tag{1}
\]
For \(n=3\), the zero-sum three-coordinate identity \(\sum_i a_i^4=\frac12(\sum_i a_i^2)^2\) forces \(u=v=\frac12\). Summing only the partitions with at most three blocks yields \(\mathbb E X^4=3/8\) and \(\mathbb E X^2=1/2\), hence the quotient \(3/2\). For \(n=2\), the nonzero random variable has equiprobable opposite values, giving quotient \(1\).

We next prove a sharp **zero-sum fourth-power lemma**, also used in classical sample-kurtosis estimates. For any \(n\ge4\), every nonzero real zero-sum vector \(z\) satisfies
\[
L_n\le \frac{\sum_i z_i^4}{(\sum_i z_i^2)^2}\le U_n,\quad
L_n=\frac{n}{\lfloor n/2\rfloor\lceil n/2\rceil}-\frac3n,\quad
U_n=\frac{n^2-3n+3}{n(n-1)}. \tag{2}
\]
Both extrema have only two coordinate values. Here is an argument that excludes all other global extrema rather than assuming two values. Consider an extremizer on the compact zero-mean unit sphere and suppose it has three distinct coordinates \(x,y,z\). Vary just these three, keeping their sum \(s\) and their sum of squares fixed. Writing the elementary symmetric polynomials of these three coordinates as \(s,e_2,e_3\), Newton's identities show
\[
x^4+y^4+z^4=s^4-4s^2e_2+2e_2^2+4s e_3.
\]
At distinct coordinates the tangent vector \((y-z,z-x,x-y)\) preserves the sum and the squared sum to first order, and changes \(e_3=xyz\) at the nonzero rate \((x-y)(x-z)(y-z)\). Hence an extremizer with three distinct coordinates must have \(s=0\). For \(s=0\), however, the triple's fourth-power sum is fixed at half the square of its squared sum along the entire constraint circle. Because \(n\ge4\), retain one further coordinate \(t\), vary the selected triple a small amount on its constraint circle, and choose two of its distinct perturbed coordinates \(x',y'\) with \(t,x',y'\) distinct and \(t+x'+y'\neq0\) (possible outside finitely many circle points). The new full vector is again a global extremizer, but the triple \((t,x',y')\) contradicts the preceding nonzero-sum necessary condition. Thus every global maximum and minimum has at most two coordinate values.

If one value occurs \(k\) times and the other \(n-k\) times, the zero-sum condition determines their relative values and gives exactly
\[
\frac{\sum_i z_i^4}{(\sum_i z_i^2)^2}=\frac{n}{k(n-k)}-\frac3n.
\]
This is largest precisely at \(k=1,n-1\) and smallest precisely when \(k\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\), proving (2) and the equality classifications. In particular \(u,v\ge1/n\) by Cauchy--Schwarz.

It remains to maximize the bilinear polynomial (1). For \(n\ge5\), place \((u,v)\) in the *larger* rectangle \([1/n,U_n]^2\). Since \(R_n\) is separately affine, its maximum occurs at a corner, and every point is a convex combination of the four corner values. Exact substitution gives
\[
R_n(U_n,U_n)=\frac{n^2-3n+3}{n-1},\quad
R_n(1/n,U_n)=R_n(U_n,1/n)=1,\quad
R_n(1/n,1/n)=\frac{(n-1)(3n-8)}{n(n-3)}.
\]
The last corner is strictly smaller than the first for every \(n\ge5\), because their difference is
\[
\frac{(n-2)^2(n^2-5n+2)}{n(n-3)(n-1)}>0.
\]
The first corner is strictly largest, hence equality forces \(u=v=U_n\). Formula (2) then proves exactly the stated single-outlier equality cases. In the \(n=4\) case use the *exact* rectangle \([L_4,U_4]=[1/4,7/12]\). Its corner values are \(3,1,1,7/3\) in the order \((L_4,L_4),(L_4,U_4),(U_4,L_4),(U_4,U_4)\). The strict maximum is at the balanced-balanced corner; (2) supplies all equality cases. This completes the proof.

## Verification
The standalone `check.py` uses only Python's standard library and rational arithmetic. Executing `python check.py` directly checks the full formula against direct permutation enumeration in 136 nondegenerate profile pairs for \(2\le n\le7\), verifies 197 exact bilinear corner comparisons, checks 3,157 two-valued power-sum configurations, and reproduces attaining cases. The algebraic proof, not those bounded computations, establishes all dimensions.

## Relationship to prior work
The permutation sums are Hoeffding combinatorial statistics. Barbour and Janson (2009, Introduction and Theorem 2.1) develop normal approximation for general arrays \(c(i,\pi(i))\) and give their variance normalization, rather than exact maximization of a rank-one fourth moment. Filmus, Kindler, Lifshitz and Minzer (2020, Theorems 1.2 and 1.4, and Section 6) study hypercontractivity on \(S_n\), especially global low-degree functions; their inequalities do not give the stated finite-dimensional equality classification for localized rank-one coefficients. The sharp mean-zero-vector fourth-power inequality in (2) is independently known and is **not** claimed as a new fact; it also underlies a finite abelian co-singleton Fourier result with the same value as our \(n\ge5\) constant. The equal numerical constant there does not imply the present estimate, since that result concerns a zero-mean function on \(n\) points, whereas our statistic is defined on \(n!\) permutations and ranges over a distinct rank-one coefficient family. The new assertion is the exact permutation fourth-moment optimization, including the exceptional balanced \(n=4\) classification. See the detailed comparison in `AUDIT.json`.

## Limitations
The result makes no assertion about arbitrary doubly centered matrices \(c_{ij}\), general degree-one functions on \(S_n\), higher moments, complex coefficient vectors, nonuniform permutation distributions, or tail probabilities. The combinatorial fourth-moment identity and the standard zero-sum fourth-power bound are elementary; mathematical interest lies in their nontrivial interaction and sharp equality transition, not in either identity alone. Although the literature comparison found no equivalent rank-one statement, historical or unindexed coverage remains possible. Independent external mathematical validation has not been performed.

## References
1. A. D. Barbour and S. Janson, *A functional combinatorial central limit theorem*, arXiv:0907.0347v1, first public July 2, 2009, https://arxiv.org/html/0907.0347v1.
2. Y. Filmus, G. Kindler, N. Lifshitz and D. Minzer, *Hypercontractivity on the symmetric group*, arXiv:2009.05503, first public September 11, 2020, https://arxiv.org/abs/2009.05503.
3. M. E. Johnson and V. W. Lowe, *Bounds on the Sample Skewness and Kurtosis*, Technometrics 21 (1979), 377–378, DOI:10.1080/00401706.1979.10489785 (only the public abstract was available for the current comparison).
4. *Sharp \(\Lambda(4)\) constant for the co-singleton spectrum of a finite abelian group*, published research record, October 2026 (full theorem and proof of the zero-sum-vector bound inspected; this is comparison literature and not the archival anchor).
