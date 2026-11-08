# Abelian-cube diversity at the first nontrivial binary weight

## Finding
An *Abelian cube* is a contiguous word \(uvw\), where the three nonempty blocks have the same length and the same Parikh vector. Factors are counted as distinct literal words, not as occurrences or only up to Abelian equivalence. For a binary word containing exactly three ones, the complete count of distinct Abelian-cube factors has an explicit integer-gap formula, a rational aggregate generating function, and a nondegenerate quadratic-scale limiting law.

Write
\[
W=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0},\quad n=a+b+c+d+3.
\]
For every integer \(1\le t\le\lfloor n/3\rfloor\) set
\[
\begin{aligned}
\lambda_t&=\max\{0,a-t+1,a+b+2-2t,a+b+c+3-3t\},\\
\upsilon_t&=\min\{a,a+b+1-t,a+b+c+2-2t,n-3t\}.
\end{aligned}
\]
Then the number \(C(W)\) of distinct nonempty Abelian-cube factors is exactly
\[
\boxed{C(W)=\left\lfloor\frac{\max\{a,b,c,d\}}3\right\rfloor
 +\sum_{t=1}^{\lfloor n/3\rfloor}\max\{0,\upsilon_t-\lambda_t+1\}.}
\tag{1}
\]
The sum is the number \(D_3(W)\) of distinct Abelian-cube factors containing all three ones; the floor counts all-zero cubes.

The total counts over all length-\(n\), Hamming-weight-three words have the rational generating function
\[
\boxed{\begin{aligned}
F(z)&=\sum_{n\ge3}\Big(\sum_{|W|=n,\ |W|_1=3}C(W)\Big)z^n\\
&=\frac{z^3(1+4z^3+z^6)}{(1-z)^2(1-z^3)^4}
+\frac{z^3}{(1-z)^4}\sum_{j=1}^4(-1)^{j+1}\binom4j\frac{z^{3j}}{1-z^{3j}}.
\end{aligned}}
\tag{2}
\]

For \(W_n\) uniform among the \(\binom n3\) binary weight-three words, let \(G=(G_1,G_2,G_3,G_4)\) be uniform on the simplex \(G_i\ge0\), \(\sum_iG_i=1\) (equivalently, \(\operatorname{Dirichlet}(1,1,1,1)\)). Define, for \(0\le t\le1/3\),
\[
\begin{aligned}
\ell_G(t)&=\max\{0,G_1-t,G_1+G_2-2t,G_1+G_2+G_3-3t\},\\
u_G(t)&=\min\{G_1,G_1+G_2-t,G_1+G_2+G_3-2t,1-3t\},\\
H(G)&=\int_0^{1/3}\max\{0,u_G(t)-\ell_G(t)\}\,dt.
\end{aligned}
\]
Then
\[
\boxed{\frac{C(W_n)}{n^2}\ \xrightarrow{\ d\ }\ H(G),\qquad
\mathbb E H(G)=\frac1{270},\qquad
\Pr(H(G)=0)=\frac29.}
\tag{3}
\]
In fact, \(\Pr(D_3(W_n)>0)\to7/9\). The limit law is nonconstant and has both an atom at zero and positive continuous-scale values. In particular,
\[\mathbb E C(W_n)=\frac{n^2}{270}+O(n).\]

## Assumptions and scope
All strings are finite, linearly indexed, binary and have exactly three occurrences of the symbol \(1\). Exponents of \(0\) may vanish. An Abelian cube is defined using three *equal-length* blocks with equal numbers of both letters; the unit block size is permitted. A distinct factor refers to its literal letters, independently of its number of occurrences. No claim is made for arbitrary Hamming weight, for cyclic factors, or for a general alphabet.

## Proof
**1. Weight reduction and uniqueness.** Every Abelian cube contained in \(W\) has \(0\) or \(3\) ones: each of its three blocks contributes the same nonnegative integer number of ones, and \(W\) has only three. The zero-one case is a word \(0^{3t}\), which appears if and only if some zero gap has length at least \(3t\), yielding exactly \(\lfloor\max\{a,b,c,d\}/3\rfloor\) distinct such cubes. A three-one cube must contain every one of \(W\); hence it is uniquely determined by its starting position and block length. At the same block length, two different starting positions have different numbers of leading zeros before the *fixed first one*, so their literal factors cannot coincide.

**2. Integer feasibility.** Index \(W\) from zero. Its ones occupy positions \(p_1=a\), \(p_2=a+b+1\), \(p_3=a+b+c+2\). A three-one factor starting at integer \(s\) with three blocks of length \(t\) is an Abelian cube precisely when
\[
s\le p_1<s+t,\quad s+t\le p_2<s+2t,\quad s+2t\le p_3<s+3t,
\quad0\le s\le n-3t.
\]
Solving these inequalities for \(s\) gives \(\lambda_t\le s\le\upsilon_t\), and there are \(\max\{0,\upsilon_t-\lambda_t+1\}\) possible integers. This proves (1), without counting duplicate occurrences.

**3. Aggregate generating function.** Over all length-\(n\) weight-three words, the triples \((s,t,W)\) in part 2 can instead be counted by selecting the start \(s\) of a length-\(3t\) factor, then independently choosing one of the \(t\) positions for each of the three ones. Thus
\[
\sum_{|W|=n,\ |W|_1=3}D_3(W)
=\sum_{t=1}^{\lfloor n/3\rfloor}(n-3t+1)t^3.
\tag{4}
\]
Summing over \(n\) and using \(\sum_{t\ge1}t^3q^t=q(1+4q+q^2)/(1-q)^4\) gives the first term of (2). For zero-only cubes, sum \(\lfloor\max\{a,b,c,d\}/3\rfloor\) over all nonnegative four-gap compositions of \(n-3\). By indicator summation and inclusion-exclusion, the number having at least one gap of length \(3t\) or more is
\[
\sum_{j=1}^4(-1)^{j+1}\binom4j\binom{n-3tj}{3},
\]
with \(\binom r3=0\) for \(r<3\). Summing in \(t\) and then \(n\) yields the second term of (2).

**4. Quadratic scaling.** The uniformly chosen gap vector \((a,b,c,d)\) is uniformly distributed among compositions of \(n-3\). Its vector divided by \(n\) converges weakly to \(G\), the uniform distribution on the three-simplex. Dividing the expressions for \(\lambda_t,\upsilon_t\) by \(n\), and reading the sum in (1) as a Riemann sum, gives \(D_3(W_n)/n^2\to H(G)\) in distribution. The discarded floor term is at most \(n/3\), so it vanishes after division by \(n^2\). The Riemann approximation is uniform up to \(O(1/n)\), since minima and maxima of the defining affine functions are uniformly Lipschitz and the integer endpoints differ from their scaled counterparts by \(O(1/n)\).

By (4), the numerator of \(\mathbb E D_3(W_n)\) is \(n^5/1620+O(n^4)\): the leading term is \(n^5\int_0^{1/3}(1-3t)t^3dt=n^5/1620\). Since \(\binom n3=n^3/6+O(n^2)\), \(\mathbb E D_3(W_n)=n^2/270+O(n)\). The bound \(C(W_n)=O(n^2)\) holds uniformly, so convergence in distribution also gives the asserted expectation for \(H(G)\).

**5. Exact mass at zero.** Let \(x=G_1\), \(y=G_1+G_2\), \(z=G_1+G_2+G_3\). Almost surely \(0<x<y<z<1\), and these have the joint distribution of three ordered independent uniform points, with density \(6\). For a positive-length continuum family of three-one Abelian cubes, there must be numbers \(s,t\) with \(0<t<1/3\) satisfying
\[
0\le s\le1-3t,\quad s\le x\le s+t,\quad s+t\le y\le s+2t,\quad s+2t\le z\le s+3t.
\]
For fixed \(t\), a permissible \(s\) exists exactly when
\[
\max\{0,x-t,y-2t,z-3t\}\le
\min\{x,y-t,z-2t,1-3t\}.
\]
Checking every lower-bound/upper-bound pair shows that such a \(t\) exists exactly when
\[
\max\!\left\{\frac{y-x}{2},\frac{z-x}{3},\frac{z-y}{2}\right\}
\le\min\!\left\{y,\frac z2,\frac13,z-x,\frac{1-x}{2},1-y\right\}.
\tag{5}
\]
For ordered points in \([0,1]\), the inequalities in (5) are equivalent to \(z\le3y\) and \(3y-x\le2\): the only potentially restrictive upper constraints are \(t\le y\), \(t\le1-y\), and \(t\le1/3\), and the last is redundant when the first two hold. Off the measure-zero boundary, strict versions characterize \(H(G)>0\).

Conditional on the median \(y\), the possible \(x,z\) ranges have planar area \(2y^2\) for \(0<y<1/3\), \(y(1-y)\) for \(1/3<y<2/3\), and \(2(1-y)^2\) for \(2/3<y<1\). Therefore
\[
\Pr(H(G)>0)=6\left(\int_0^{1/3}2y^2dy
+\int_{1/3}^{2/3}y(1-y)dy
+\int_{2/3}^{1}2(1-y)^2dy\right)=\frac79.
\]
The strict feasible region has positive two-dimensional \((s,t)\) area; its complement is open away from the two bounding hyperplanes. The same Riemann-sum argument shows that \(\Pr(D_3(W_n)>0)\to7/9\). This completes (3).

## Verification
`verify.py` independently enumerates all distinct Abelian-cube factors by literal substring comparison, for every binary three-one word through length 26. It checks (1), the aggregate counts from (4) and inclusion-exclusion, and exact rational integration for the limiting probability. Its optional extended tests check the continuum feasibility reduction on a deterministic rational grid. The checker is a finite sanity check; the preceding combinatorial and limiting arguments establish the infinite claims.

## Relationship to prior work
Cassaigne, Richomme, Saari and Zamboni (2010), *Avoiding Abelian powers in binary words with bounded Abelian complexity*, analyze Abelian-power occurrence and avoidance in infinite words, including cubes, but not exact distinct-cube counts under fixed finite Hamming weight. Rao and Rosenfeld (2015), *Avoidability of long \(k\)-abelian repetitions*, prove impossibility of indefinite binary avoidance of Abelian cubes of block length at least two using a finite search and a Lyndon-factorization argument; their theorem does not yield the formulas (1)–(3). Christodoulakis, Christou, Crochemore and Iliopoulos (2014), *On the average number of regularities in a word*, analyze occurrence-count expectations for unrestricted random words, including an Abelian-cube average expressed through Franel numbers; this is a different measure and sampling law from distinct factors conditioned on exactly three ones. The accessible abstract and bibliographic review were inspected, but full text could not be obtained, and thus an equivalent conditional refinement in that paper is an explicit residual risk. Fici and Mignosi (2015), *Words with the Maximum Number of Abelian Squares*, consider two-block Abelian repetitions, predominantly for infinite words; no three-block fixed-three-one count follows from their assertions. Recorded related finite-word results on Abelian-square counts for two-marker words and five-run words concern two blocks, not three. Searches of indexed research and sequence records did not identify this exact three-marker cube distribution; this is not a proof of priority.

## Limitations
The distribution is expressed as an explicit piecewise-quadratic functional of a Dirichlet vector, not as a closed-form continuous density. No asymptotic variance is claimed. The zero-only cubes contribute only lower-order terms; they must not be confused with the probability that a word is entirely Abelian-cube-free. An unindexed equivalent result remains a historical-priority risk. The full text of the especially relevant 2014 unrestricted-average study was not accessible, so exact theorem-by-theorem exclusion of a conditional refinement there remains unverified. Independent audit has not been conducted.

## References
- J. Cassaigne, G. Richomme, K. Saari, L. Q. Zamboni, *Avoiding Abelian powers in binary words with bounded Abelian complexity*, arXiv:1005.2514 (first posted 2010-05-14), https://arxiv.org/html/1005.2514v1 .
- M. Rao, M. Rosenfeld, *Avoidability of long \(k\)-abelian repetitions*, arXiv:1507.02581 (first posted 2015-07-09), https://arxiv.org/abs/1507.02581 .
- G. Fici, F. Mignosi, *Words with the Maximum Number of Abelian Squares*, arXiv:1506.03562 (first posted 2015-06-11), https://arxiv.org/abs/1506.03562 .
- OEIS A141057, unrestricted number of three-letter Abelian cubes of a fixed length, https://oeis.org/A141057 (different counting model).
- M. Christodoulakis, M. Christou, M. Crochemore, C. S. Iliopoulos, *On the average number of regularities in a word*, Theoretical Computer Science 525 (2014), 3–9, https://doi.org/10.1016/j.tcs.2013.10.007 (abstract and bibliographic review inspected; full text unavailable).
