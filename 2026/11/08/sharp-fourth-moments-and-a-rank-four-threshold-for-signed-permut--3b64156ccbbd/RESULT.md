# Sharp fourth moments and a rank-four threshold for signed-permutation matrix coefficients

## Finding
For each integer \(n\ge2\), let \(W\) be uniformly distributed over real signed permutation matrices of size \(n\). For every nonzero real coefficient matrix \(A\), set
\[
F_A(W)=\operatorname{tr}(A^{\mathsf T}W),\qquad
K_n(A)=\frac{\mathbb E F_A(W)^4}{(\mathbb E F_A(W)^2)^2}.
\]
Then the complete **sharp interval** is
\[
\boxed{1\le K_n(A)\le\max\{4,n\}.}
\]
All values in the interval occur. The lower equality cases are precisely the nonzero matrices having one complete row or column of entries of the same nonzero absolute value and all other entries zero. The upper equality cases have a structural transition at dimension four:

- For \(n=2,3\), all nonzero coefficients form a full permutation matching, with equal absolute values.
- For \(n=4\), all nonzero coefficients form any nonempty partial permutation matching, with arbitrary positive magnitudes.
- For \(n\ge5\), precisely one matrix entry is nonzero.

The coefficient signs are arbitrary in every case. For the full \(n^2\)-dimensional real coefficient space \(X_n\) with the induced \(L^4\) norm, its **exact real Banach--Mazur distance** is
\[
\boxed{d_{\mathrm{BM}}(X_n,\ell_2^{n^2})=\max\{4,n\}^{1/4}.}
\]

## Assumptions and scope
The group is \(B_n=(\{\pm1\})^n\rtimes S_n\), realized as the matrices having exactly one \(\pm1\) entry in each row and column. The law is uniform Haar probability on this finite group. Equivalently, choose a uniform permutation \(\pi\in S_n\) and independent fair signs \(\varepsilon_i\), then \(W_{i,\pi(i)}=\varepsilon_i\) and other entries vanish. Coefficients and functions are real, and all assertions hold for every integer \(n\ge2\). Zero coefficient matrices are excluded from normalized moment ratios.

## Proof
**Moment identity.** Let \(S=\sum_{ij}A_{ij}^2>0\) and \(U=\sum_{ij}A_{ij}^4\). Conditioning on \(\pi\) and expanding independent signs yields
\[
\mathbb E F_A^2=\frac Sn,\qquad
\mathbb E F_A^4=\frac Un+\frac{6}{n(n-1)}
\sum_{i<k}\sum_{j\ne\ell}A_{ij}^2A_{k\ell}^2.
\]
Each pair of entries from distinct rows and columns occurs together with probability \(1/[n(n-1)]\). Define \(b_{ij}=A_{ij}^2/S\), \(T=\sum_{ij}b_{ij}^2\), \(D=\sum_{i<k,j\ne\ell}b_{ij}b_{k\ell}\), and \(P\) as the sum of \(b_{ij}b_{k\ell}\) over distinct unordered pairs sharing a row or a column. Thus \(T+2P+2D=1\), and
\[
K_n(A)=nT+\frac{6n}{n-1}D
=n-2nP+\frac{2n(4-n)}{n-1}D.
\]
For \(n\ge4\), this is the exact nonnegative upper-deficit identity
\[
n-K_n(A)=2nP+\frac{2n(n-4)}{n-1}D.
\]
It gives the stated upper equality classification for these dimensions, since \(P=0\) means the positive support is a partial matching; when \(n>4\), also \(D=0\) forces that support to be one entry.

**The upper bound for \(n=2,3\).** Treat the nonnegative masses \(b_{ij}\) as variables on the probability simplex. If two positive masses share a row or column, redistribute their fixed total while holding all other masses constant. Their mutual contribution to \(D\) is zero, all contributions involving other entries are affine in the redistribution parameter, and \(nT\) is strictly convex. Therefore no global maximizer has two positive masses sharing a row or column. Every maximizing support is a matching of \(k\le n\) positions. On any matching, \(2D=1-T\) and
\[
K_n(A)=\frac{3n}{n-1}+\frac{n(n-4)}{n-1}T.
\]
For \(n=2,3\) the coefficient of \(T\) is strictly negative. With \(k\) positive masses summing to one, \(T\ge1/k\ge1/n\), with equality exactly when \(k=n\) and every mass equals \(1/n\). Substitution gives \(K_n(A)\le4\) and the full equality description.

**Lower bound and rigidity.** Jensen's inequality implies \(\mathbb E F_A^4\ge(\mathbb E F_A^2)^2\). More quantitatively, with \(Y_\pi=\sum_i A_{i,\pi(i)}^2\), the variance decomposition across independent signs gives
\[
(\mathbb E F_A^2)^2(K_n(A)-1)
=\operatorname{Var}_{\pi}(Y_\pi)
+\frac4{n(n-1)}\sum_{i<k}\sum_{j\ne\ell}A_{ij}^2A_{k\ell}^2.
\]
Both terms are nonnegative. Equality forces the support to contain no two entries in distinct rows and columns; a pairwise-intersecting family of edges in a bipartite graph is contained in a single row or a single column. The zero permutation variance then says that the squared entries along that complete row or column are all equal. Since \(S>0\), their common value is positive. Conversely, every such coefficient matrix makes \(|F_A|\) a positive constant, and hence attains the lower bound.

**Intermediate values.** On the Euclidean unit sphere of coefficient matrices, the normalized moment ratio is continuous. This sphere is connected for \(n\ge2\). Its image is therefore the entire interval between its attained extrema.

**Optimal Euclidean distortion.** Identify \(X_n\) with \(\mathbb R^{n^2}\) through \(A\mapsto F_A\); the map is injective because \(\mathbb E F_A^2=S/n\). The sharp endpoint inequalities give
\[
\|F_A\|_2\le\|F_A\|_4\le\max\{4,n\}^{1/4}\|F_A\|_2.
\]
To prove that no different inner product improves this ratio, let \(q(A)\) be any positive-definite quadratic form realizing a competing pair of two-sided comparison constants. Average \(q\) over independent signed row and column permutations; averaging preserves both squared norm inequalities because the \(L^4\) norm is invariant. Row and column sign changes kill every off-diagonal coefficient of the averaged quadratic form, while row and column permutations make all diagonal coefficients equal. Thus the average is a positive multiple of \(S\). The attained fourth-moment extrema now force a distortion ratio at least \(\max\{4,n\}^{1/4}\); the \(L^2\) norm realizes it.

## Verification
The included standalone `signed_perm_checker.py` enumerates all signed permutations for eighteen explicitly specified integer matrices in dimensions \(2,3,4\), comparing exact rational moments with the formula. It checks the three extremal witness families for dimensions \(2\) through \(17\), verifies the upper-deficit identity on their supports, and independently tests the lower variance decomposition in dimensions \(2\) through \(6\). Run `python signed_perm_checker.py` with Python 3. The enumeration verifies the stated finite instances, not the universal theorem; the preceding argument proves all dimensions.

## Relationship to prior work
Hughes, Najnudel, Nikeghbali, and Zeindler study spectral traces and generalized Ewens statistics for permutation matrices and wreath products; their trace-class functions do not give this arbitrary-coefficient extremal norm. Stasinski and Voll identify the signed-permutation group representation while studying different Coxeter statistics. Collins and Nagatsu develop general moment calculus for centered ordinary permutation matrices, without the present sharp signed-matrix coefficient extremizers. The signed group is not merely the ordinary permutation-coefficient problem: the independent signs remove cross terms and change both the lower endpoint and the complete set of upper extremizers.

## Limitations
The result is specific to real coefficients, uniform Haar measure on full signed-permutation groups, and second/fourth moments. It does not determine sharp constants on type-\(D\) subgroups, under biased sign laws, for complex coefficients, or at higher exponents. The historical literature comparison is not a proof of absolute novelty; specialized unindexed results might contain an equivalent statement.

## References
1. C. Hughes, J. Najnudel, A. Nikeghbali and D. Zeindler, *Random permutation matrices under the generalized Ewens measure*, arXiv:1109.5010, first publicly posted 2011-09-23; Annals of Applied Probability 23 (2013), 987–1024.
2. A. Stasinski and C. Voll, *A new statistic on the hyperoctahedral groups*, arXiv:1303.0990, first publicly posted 2013-03-05; Electronic Journal of Combinatorics 20 (2013), P50.
3. B. Collins and M. Nagatsu, *Weingarten calculus for centered random permutation matrices*, arXiv:2503.18453, first publicly posted 2025-03-24.
