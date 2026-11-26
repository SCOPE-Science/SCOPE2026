# Complete rank geometry of third-order Fourier minors at odd semiprime orders

## Finding
For every prime \(p\ge5\), put \(N=3p\). Every three-row, three-column submatrix of the complex discrete Fourier matrix has rank determined solely by how its row and column index triples distribute modulo \(3\) and modulo \(p\). The complete determinant-zero criterion, rank-one criterion, and rank census appear below.

The singularity criterion, with the notation from the next section, is
\[
(r_p=1\land c_3<3)\lor(c_p=1\land r_3<3)\lor(r_3=1\land c_p<3)\lor(c_3=1\land r_p<3).
\]
Rank one occurs exactly under \((r_p=1,c_3=1)\lor(c_p=1,r_3=1)\); all other singular minors have rank two. In the \(\binom{3p}{3}^2\) ordered pairs of three-element index sets, the three rank populations are
\[
\begin{aligned}
M_1&=p^2(p-1)(p-2),\\
M_2&=p^2(p-1)(9p^2-21p+18),\\
M_3&=\binom{3p}{3}^2-p^2(p-1)(9p^2-20p+16).
\end{aligned}
\]

## Assumptions and scope
Here \(p\) is an arbitrary prime at least five, \(N=3p\), and \(F_N=(\exp(2\pi i xy/N))_{x,y\in\mathbb Z/N\mathbb Z}\) is unnormalized. Row and column index sets \(R,C\) are independently chosen unordered three-element subsets; \(F_N[R,C]\) denotes their submatrix with any fixed row and column ordering. Let \(r_3\) and \(r_p\) be the numbers of distinct reductions of \(R\) modulo \(3\) and \(p\), respectively, and similarly \(c_3,c_p\). The theorem makes no claim for composite \(p\) or for minors of other sizes.

## Proof
**1. Cyclotomic independence.** By Chinese remaindering and multiplication by invertible residue factors, row/column permutations and nonzero phase multipliers turn the matrix entries into \(\omega^{ua}\zeta^{vb}\) for row coordinates \((u,v)\in\mathbb F_3\times\mathbb F_p\) and column coordinates \((a,b)\), with \(\omega=e^{2\pi i/3}\) and \(\zeta=e^{2\pi i/p}\). Since \(3\) and \(p\) are coprime, \(\mathbb Q(\omega)\cap\mathbb Q(\zeta)=\mathbb Q\), and \(\Phi_p(X)=1+X+\cdots+X^{p-1}\) remains the minimal polynomial of \(\zeta\) over \(\mathbb Q(\omega)\). Thus a sum of fewer than \(p\) distinct \(p\)-th roots of unity with coefficients in \(\mathbb Q(\omega)\) is zero only when every coefficient is zero. A sum using all \(p\) roots can vanish only if the corresponding coefficients are all equal.

**2. A triple concentrated modulo \(p\).** If \(r_p=1\), distinctness forces \(R\) to have all three residue classes modulo \(3\). Its submatrix is a nonzero column modulation of rows of the \(3\)-point Fourier matrix repeated according to the column residues modulo \(3\). It has full rank if and only if \(c_3=3\). By transposition, \(c_p=1\) forces singularity precisely when \(r_3<3\).

**3. Exactly two row residues modulo \(p\).** If \(r_p=2\), the two rows sharing a residue modulo \(p\) have different residues modulo \(3\). After subtracting common CRT coordinates they become \((0,0)\) and \((u,0)\), with \(u\ne0\); the third row is \((w,v)\), with \(v\ne0\). If \(c_3=1\), the first two rows are proportional and the determinant vanishes. If \(c_3=2\), precisely two columns share a mod-\(3\) coordinate; they have distinct mod-\(p\) coordinates. The first two rows have a unique dependence supported on those two columns, but the third row separates them by the nontrivial factor \(\zeta^{v(b_1-b_2)}\). Hence the determinant is nonzero.

If \(c_3=3\), the kernel of the first two rows is a one-dimensional vector with **all three entries nonzero**, because a nonzero multiple of the \(3\)-point Fourier Vandermonde kernel has this property. Taking its inner product with the third row produces a sum \(\sum_j\alpha_j\zeta^{vb_j}\), where every \(\alpha_j\ne0\) lies in \(\mathbb Q(\omega)\). If \(c_p\ge2\), one value of \(b_j\) occurs only once, and cyclotomic independence (at most three terms, fewer than \(p\)) prevents cancellation. If \(c_p=1\), factor out the common \(p\)-phase and obtain a \(3\)-point Fourier minor, which is nonsingular precisely when \(r_3=3\). These statements and their transposes settle all cases in which either mod-\(p\) triple has at most two distinct residues, except the case that both have three.

**4. Three distinct residues modulo \(p\) in both triples.** Nonzero row/column scalings and affine changes over \(\mathbb F_p\) normalize row \(p\)-coordinates to \((0,1,t)\) and column \(p\)-coordinates to \((0,1,s)\), where \(s,t\notin\{0,1\}\). The six terms of the determinant, in fixed permutation order, have \(p\)-exponents and signs
\[
(1+ts,+),\quad(s+t,-),\quad(ts,-),\quad(s,+),\quad(t,+),\quad(1,-),
\]
with each signed coefficient multiplied by a third root of unity from the corresponding mod-\(3\) coordinates. If \(s\ne t\), at least one of the two exponents \(s,t\) appears **exactly once**: neither can coincide with \(s+t,ts,1\), and both cannot coincide with the lone exponent \(1+ts\) while remaining distinct. If \(s=t\), the exponent \(1\) is a singleton unless \(t=1/2\) or \(t=-1\); at those exceptional values, the exponents \(t^2\) and \(2t\), respectively, are singletons. Thus the grouped cyclotomic expression has a nonzero singleton coefficient. For \(p\ge7\), six terms leave at least one exponent unused, so cyclotomic independence implies that the determinant cannot vanish. When \(p=5\), if there is an unused exponent the same argument applies; otherwise precisely one exponent repeats among the six terms, leaving four singleton classes. At least one singleton comes from a positive determinant term and at least one from a negative term. Their nonzero coefficients are respectively third roots of unity and their negatives, and hence cannot be equal. The minimal-polynomial criterion again rules out zero. This settles the remaining case for every \(p\ge5\), regardless of the mod-\(3\) indices.

Combining the four cases gives the displayed singularity criterion.

**5. Rank-one classification.** All \(2\)-by-\(2\) minors vanish exactly when \(N\) divides \((r_i-r_j)(c_k-c_l)\) for every row difference and every column difference. Since \(N=3p\) is squarefree, this holds only when the row triple is concentrated modulo \(p\) and the column triple modulo \(3\), or conversely. This is exactly the rank-one criterion; no rank-zero submatrix is possible because every entry is nonzero.

**6. Counting.** Write \(K=\binom{3p}{3}\). The number of row triples contained in a single mod-\(p\) fiber is \(P=p\), and the number contained in a single mod-\(3\) fiber is \(T=3\binom p3\). These families are disjoint. The number of column triples with fewer than three residues modulo \(3\) equals \(X=K-p^3=p(p-1)(7p-2)/2\); the number with fewer than three residues modulo \(p\) equals \(Y=K-27\binom p3=p(9p-8)\). The four singularity events contain \(2PX+2TY\) pairs before overlap. Only the two rank-one event intersections overlap, each on \(PT\) pairs. Therefore their union has size
\[
2PX+2TY-2PT=p^2(p-1)(9p^2-20p+16).
\]
Rank one occurs on precisely \(2PT=p^2(p-1)(p-2)\) pairs. Subtracting yields the rank-two count; the nonsingular count is the complement in \(K^2\).

## Verification
The standalone source `verify.cpp` enumerates every pair of three-element row and column sets for \(p=5,7,11\), computes determinant vanishing exactly in \(\mathbb Z[\omega,\zeta]\) via the minimal polynomial \(\Phi_p\), and determines rank one independently from all nine \(2\)-by-\(2\) determinants. The observed ranks are \((300,13800,192925)\), \((1470,91728,1675702)\), and \((10890,1059960,28697086)\), respectively, with zero prediction mismatches. The analytic proof, not these finite tests, establishes the result for all primes.

## Relationship to prior work
Caragea and Lee (first public 2024-09-15, arXiv:2409.09793v1) prove that **principal** third-order Fourier minors do not vanish when the order is squarefree. That statement is recovered here only as a corollary, since the nonprincipal row-column pairing can have rank one or two. Loukaki's later criterion for selected cyclic semiprime minors with **matched mod-prime residue populations** guarantees nonsingularity under its own prime hypotheses; it does not classify all independently chosen triples or count their rank populations. Other existing exact third-minor classifications concern even semiprime orders, prime squares, or elementary abelian prime squares; their group structures and implications differ.

## Limitations
This is a complete complex-rank classification for minors of order three and cyclic size \(3p\) only. No conclusion is drawn for other minors, prime powers, weighted matrices, or uniform singular-value bounds. Finite tests corroborate but do not certify the universal argument. The best-knowledge bibliographic comparison cannot exclude every older or differently formulated equivalent result.

## References
1. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793v1, publicly submitted 2024-09-15; https://arxiv.org/html/2409.09793v1 .
2. M. Loukaki, *Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle*, Bulletin of the London Mathematical Society (2025), doi:10.1112/blms.70192; https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70192 .
