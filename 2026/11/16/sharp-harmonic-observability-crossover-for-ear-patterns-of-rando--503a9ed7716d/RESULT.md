# Sharp harmonic observability crossover for ear patterns of random polygon triangulations

## Finding

Fix an integer \(n\ge5\) and a strictly convex polygon with cyclically labeled vertices \(0,\ldots,n-1\). Choose uniformly one of its \(C_{n-2}\) triangulations, where \(C_m=\binom{2m}{m}/(m+1)\). Let \(X_i\in\{0,1\}\) indicate that the triangle with vertices \(i-1,i,i+1\) (indices modulo \(n\)) belongs to the triangulation. Thus \(X_i\) records an original-boundary ear, not an ear of a subpolygon. Write \(K_n=\operatorname{Cov}(X)\), with unnormalized Euclidean coordinate inner product.

Set
\[
p_n=\frac{n-1}{2(2n-5)},\qquad q_n=\frac{(n-1)(n-2)}{4(2n-7)(2n-5)}.
\]
For every \(n\ge5\), the complete orthonormal discrete Fourier eigenvalues of \(K_n\) are
\[
\Lambda_{n,0}=\frac{(n-5)(n-4)(n-1)}{2(2n-7)(2n-5)^2},
\qquad
\Lambda_{n,j}=p_n-q_n-2q_n\cos(2\pi j/n),\quad 1\le j<n.
\]
The rank equals \(n-1\) at \(n=5\), with only the constant Fourier mode null, and equals \(n\) for all \(n\ge6\). The largest eigenvalue always occurs at the spatial frequency or frequencies closest to \(\pi\): at \(j=n/2\) for even \(n\), and at \(j=(n\pm1)/2\) for odd \(n\). Its exact value is \(p_n+q_n\) for even \(n\), and \(p_n-q_n+2q_n\cos(\pi/n)\) for odd \(n\).

**Sharp least-observable mode transition.** Among the strictly positive eigenvalues, the minimizing frequencies are precisely \(j=\pm1\) when \(n=5\); uniquely \(j=0\) for every integer \(6\le n\le20\); and precisely \(j=\pm1\) for every integer \(n\ge21\). This is a change from uncertainty in the total number of ears to uncertainty in the longest nonconstant spatial wavelength, at exactly twenty-one vertices.

Let \(\kappa_n=\Lambda_{n,\max}/\Lambda_{n,\min}^{+}\) denote the condition ratio on the strictly positive covariance eigenspace. It obeys the **sharp dimension-uniform bound**
\[
\boxed{\sup_{n\ge5}\kappa_n=\kappa_6=\frac{49}{2}},
\]
with equality **only** at \(n=6\), and \(\lim_{n\to\infty}\kappa_n=5\). For \(n\ge6\) this is also the squared condition number of the centered ear-observation frame; at \(n=5\), the constant direction is removed.

## Assumptions and scope

The polygon is strictly convex and all its vertices are distinguished by their cyclic positions. Every triangulation has equal probability, regardless of geometry. A boundary ear at \(i\) is the triangle \((i-1,i,i+1)\) using both original polygon edges adjacent to \(i\). The covariance uses centered Bernoulli indicators and ordinary, not probability-normalized or trace-normalized, Euclidean coordinates; hence its eigenvalues have units of variance. We use the unitary Fourier matrix \(n^{-1/2}e^{2\pi i ij/n}\). All rank, equality and crossover assertions hold for every integer \(n\ge5\), without asymptotic exceptions.

## Proof

**1. Catalan joint probabilities.** Cutting off a specified ear leaves an \((n-1)\)-gon and establishes \(\Pr(X_i=1)=C_{n-3}/C_{n-2}=p_n\). Adjacent boundary ears cannot coexist (they would use crossing or incompatible ear diagonals). Any two distinct nonadjacent ear triangles can be deleted simultaneously; doing so leaves an \((n-2)\)-gon, with exactly \(C_{n-4}\) completions. Thus \(\mathbb E[X_iX_j]=0\) for cyclic neighbors and \(\mathbb E[X_iX_j]=C_{n-4}/C_{n-2}=q_n\) for all other distinct pairs. These counts remain valid for the pentagon, where the only compatible pairs are nonadjacent.

Let \(A_n\) denote the ordinary adjacency matrix of the \(n\)-cycle and \(J_n\) the all-ones matrix. The covariance is exactly
\[
K_n=(p_n-q_n)I_n-q_nA_n+(q_n-p_n^2)J_n.
\]
The Fourier characters diagonalize all three matrices: \(A_n\) has eigenvalues \(2\cos(2\pi j/n)\), and \(J_n\) has eigenvalues \(n\) at \(j=0\) and zero elsewhere. Consequently
\[
\Lambda_{n,0}=p_n-3q_n+n(q_n-p_n^2),\qquad
\Lambda_{n,j}=p_n-q_n-2q_n\cos(2\pi j/n).
\]
The Catalan ratios give the stated closed form for \(\Lambda_{n,0}\) and the identity \(q_n-p_n^2=3(n-1)/[4(2n-7)(2n-5)^2]\).

**2. Ranks and spectral order.** Since \(q_n>0\), the nonconstant eigenvalues increase strictly with the cyclic frequency distance \(\min(j,n-j)\), and the largest modes are exactly those specified above. At \(n=5\), \(\Lambda_{5,0}=0\), whereas \(\Lambda_{5,1}=(3-\sqrt5)/10>0\). At \(n=6\), the least nonconstant eigenvalue is \(1/14>0\); at \(n=7\) it is positive because \(\cos(2\pi/7)<\cos(\pi/4)<3/4\). For \(n\ge8\), \(p_n-3q_n=(n-8)(n-1)/[4(2n-7)(2n-5)]\ge0\), and \(\Lambda_{n,j}=p_n-3q_n+2q_n(1-\cos(2\pi j/n))>0\) for \(j\ne0\). Finally \(\Lambda_{n,0}>0\) exactly for \(n\ge6\). This proves every rank and the ordering of nonconstant modes.

**3. Exact crossover.** Algebra yields
\[
\Lambda_{n,1}-\Lambda_{n,0}
=2q_n\left[1-\cos(2\pi/n)-\frac{3n}{2(n-2)(2n-5)}\right].
\]
For \(5\le n\le20\), use \(1-\cos t\ge t^2/2-t^4/24\) with \(t=2\pi/n\), the classical bounds \(223/71<\pi<22/7\), and thus \(\pi^2>986/100\), \(\pi^4<98\). The bracket is strictly greater than
\[
\frac{986}{50n^2}-\frac{196}{3n^4}-\frac{3n}{2(n-2)(2n-5)}.
\]
For each of the sixteen integers \(5\le n\le20\) this exact rational expression is positive. Its least value on these integers is \(1069/840000>0\), at \(n=20\); the supplied finite exact-rational certificate checks every integer. For every integer \(n\ge21\), use \(1-\cos t<t^2/2\) and \(\pi<22/7\). The bracket is strictly negative whenever \(3n^3-4(22/7)^2(n-2)(2n-5)>0\). Writing \(n=21+t\), the latter is equivalent to
\[
147t^3+5389t^2+49281t+359>0,
\]
which holds for all real \(t\ge0\). Therefore the sign changes exactly between \(20\) and \(21\); the strictly increasing nonconstant frequency spectrum then identifies precisely the minimizers, including the singular pentagon's positive-spectrum convention.

**4. Sharp condition bound.** Direct substitution gives \(\Lambda_{6,0}=1/49\) and \(\Lambda_{6,3}=1/2\), hence \(\kappa_6=49/2\). At \(n=5\), the two positive distinct eigenvalues are \((3\mp\sqrt5)/10\), so \(\kappa_5=(7+3\sqrt5)/2<8\). For \(n\ge7\), the maximum is at most \(p_n+q_n\le p_7+q_7=19/42\). To lower-bound the positive minimum, the displayed rational expression for \(\Lambda_{n,0}\) is strictly increasing for real \(n\ge6\): its derivative has strictly positive numerator \(3(2n^3-9n^2-18n+85)\). Thus for \(7\le n\le20\), \(\Lambda_{n,\min}^{+}=\Lambda_{n,0}\ge\Lambda_{7,0}=2/63\). For \(n\ge21\), \(\Lambda_{n,\min}^{+}=\Lambda_{n,1}\ge p_n-3q_n\ge p_{21}-3q_{21}=13/259>2/63\), using the positive derivative of \(p_n-3q_n\) for real \(n\ge21\). The rational function \(p_n+q_n\) decreases on real \(n\ge7\). Consequently every \(n\ge7\) satisfies
\[
\kappa_n\le\frac{19/42}{2/63}=\frac{57}{4}<\frac{49}{2},
\]
proving uniqueness at \(n=6\). Finally \(p_n\to1/4\), \(q_n\to1/16\), \(\Lambda_{n,0}\to1/16\), and \(\Lambda_{n,1}\to1/16\), while the largest eigenvalue tends to \(5/16\); hence \(\kappa_n\to5\).

## Verification

The standalone Python-3 standard-library script `check.py` reconstructs every triangulation of the labeled convex polygons with \(5\le n\le11\), counts every one- and two-ear event exactly, and checks the constant-mode variance identity. It verifies all sixteen rational inequalities in the finite half of the crossover proof and stress-tests the claimed mode order and spectra through \(n=1000\). On execution it reports `PASS 6100 assertions`. All identities and the infinite bound are proved above; finitely many tested lengths are not used as a substitute for the proof at unbounded size.

## Relationship to prior work

The Catalan count of polygon triangulations, their ear counts and ear-count variance predate this result. Mansour and Rastegar (2019, Sections 1 and 3.2) develop ear-count distributions and a general triangle-weight variance formula under a side-length-invariance hypothesis. Their variance theorem is not a position-weighted Fourier-frame theorem and does not directly include a nonzero Fourier weight on individual ear tips. The present result uses the known Catalan counts as inputs but adds exact spatial frequency-resolved variances, the sharp least-mode switch at \(n=21\), and the global extremal condition bound at \(n=6\).

The previously published results *A sharp diagonal–ear dependence dichotomy in uniform polygon triangulations* and *Conditional correlation signs and compatible-family association in uniform polygon triangulations* analyze a distinguished diagonal's dependence on the total ear count, and covariance signs between prescribed diagonals, respectively. Their counting arguments supply closely related pair statistics but neither published statement orders the Fourier modes of the entire ear-tip vector nor determines the unique size-crossover and the sharp all-size frame bound. Deriving the full covariance by known Catalan enumeration is elementary; the mathematically distinctive contribution is the global spectral classification and two exact sharp thresholds. Earlier specialized harmonic treatments may exist and historical priority is not independently established.

## Limitations

The law is uniform over triangulations of convex polygons only. The condition ratio concerns a *covariance* (equivalently squared singular-value ratio of centered observations), not the condition ratio of the random triangulation flip Markov chain. At \(n=5\), the constant mode is exactly unobservable, so the condition ratio is defined on the positive eigenspace. No claim is made about higher-order correlations, convergence rates of random ear-count laws, weighted triangulations, or arbitrary planar point sets. The same pairwise Catalan counts appear in older literature; independent historical comparison is still warranted for the sharp Fourier transition and conditioning classification.

## References

1. T. Mansour and R. Rastegar, *On typical triangulations of a convex n-gon*, arXiv:1911.04025, first public version 2019-11-11, especially Theorem 1.1 and Lemma 1.4, https://arxiv.org/html/1911.04025v2.
2. A. Kupavskii, A. Volostnov and Y. Yarovikov, *Minimum number of partial triangulations*, arXiv:2104.05855, first public version 2021-04-12, Catalan triangulation count and the convex base case, https://arxiv.org/abs/2104.05855.
3. D. Eppstein and D. Frishberg, *Improved mixing for the convex polygon triangulation flip walk*, arXiv:2207.09972, first public version 2022-07-20, a distinct sampling-dynamics question, https://arxiv.org/abs/2207.09972.
4. *A sharp diagonal–ear dependence dichotomy in uniform polygon triangulations*, published scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-diagonal-ear-dependence-dichotomy-in-uniform-polygon-tri--20dbadd10529.
5. *Conditional correlation signs and compatible-family association in uniform polygon triangulations*, published scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-conditional-correlation-signs-and-compatible-family-association--430feb7408bd.
