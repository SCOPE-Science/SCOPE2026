# Parity-selective dyadic Fourier rigidity of polygon-triangulation ear profiles

## Finding

Let \(n\ge5\) be an integer, and let \(\mathcal T_n\) be the triangulations of a convex polygon whose vertices are cyclically labelled by \(\mathbb Z/n\mathbb Z\). For \(T\in\mathcal T_n\), let \(E(T)\subseteq\mathbb Z/n\mathbb Z\) be its **original-boundary ear-tip set**: vertex \(i\) belongs to \(E(T)\) precisely when triangle \((i-1,i,i+1)\) appears in \(T\). For every frequency \(S\subseteq\mathbb Z/n\mathbb Z\), define the unnormalized Walsh sum
\[
W_n(S)=\sum_{T\in\mathcal T_n}(-1)^{|S\cap E(T)|}.
\]
Put \(C_m=\frac1{m+1}\binom{2m}{m}\), \(s_2(t)=\text{number of ones in the binary expansion of }t\), and \(v_n=s_2(n-1)-1=v_2(C_{n-2})\).

**Theorem (all orders and all frequencies).** For every integer \(n\ge5\):

1. If \(n\) is odd, then for **every** \(S\),
\[
\boxed{W_n(S)\equiv C_{n-2}\pmod{2^{v_n+1}},\qquad v_2(W_n(S))=v_n.}
\]
In particular, no Walsh multiplier vanishes. Counting convolution by ear profiles on the Boolean group \((\mathbb Z/2\mathbb Z)^n\) is invertible, and its determinant has exact valuation \(v_2(|\det T_n|)=2^n v_n\).

2. If \(n\) is even, then for **every** \(S\),
\[
\boxed{\frac{W_n(S)}{2^{v_n}}\equiv 1+|S|\pmod2.}
\]
Consequently all \(2^{n-1}\) even-cardinality frequencies are nonzero with exact valuation \(v_n\), while all odd-cardinality frequencies are divisible by \(2^{v_n+1}\) (and may be zero). The convolution rank is at least \(2^{n-1}\).

In both parity classes, the greatest common divisor of the absolute Walsh multipliers equals \(2^{v_n}\), attained by the empty frequency. Thus the result establishes Fourier invertibility even for infinitely many odd polygon sizes with an **even** Catalan number, for example \(n=2^k+3\) with \(k\ge2\). The strictly stronger-than-modulo-four regime is also infinite, for example \(n=2^k+7\) with \(k\ge3\), which has \(v_n=2\).

## Assumptions and scope

Every triangulation is counted with multiplicity one; different triangulations may produce the same binary ear profile. This is a **multiplicity-weighted** convolution kernel: \(f_n(x)=|\{T:E(T)=x\}|\) for \(x\in(\mathbb Z/2\mathbb Z)^n\). Its Walsh transform is the integer \(W_n(S)\), not its probability-normalized version. The convolution \(T_n g=f_n*g\) uses counting measure and has one eigenvalue \(W_n(S)\) for each of the \(2^n\) characters. Ear tips refer to the original polygon boundary, not to ears of recursively created subpolygons. The even-order statement does **not** claim that the odd-weight frequencies always vanish, nor that even-order convolution is always singular.

## Proof

**1. Exact prescribed-ear count.** Two adjacent vertices cannot both be original-boundary ear tips for \(n\ge5\), because their two ear diagonals cross. Thus every realizable ear-tip set is independent in the cyclic graph \(C_n\). If \(I\subseteq\mathbb Z/n\mathbb Z\) is an independent set of cardinality \(k\), specifying every ear at \(I\) and deleting these disjoint original-boundary ear triangles leaves a convex polygon with \(n-k\) vertices. Triangulating this remaining polygon is a bijection with the triangulations possessing all prescribed ears, even if there are other ears. Hence
\[
\#\{T\in\mathcal T_n:I\subseteq E(T)\}=C_{n-k-2},\qquad 0\le k\le\lfloor n/2\rfloor.
\]
The formula is valid also at maximal independent sets: \(n-k\ge3\) for every \(n\ge5\).

**2. An exact signed enumerator.** For a chosen frequency \(S\), write \(i_k(S)\) for the number of size-\(k\) independent subsets of \(S\) in the cyclic graph, with \(i_0(S)=1\). Expanding the sign of each ear as \((-1)^{\mathbf1_{i\in E(T)}}=1-2\mathbf1_{i\in E(T)}\), and interchanging two finite sums, gives the exact identity
\[
\boxed{W_n(S)=\sum_{k=0}^{\lfloor n/2\rfloor}(-2)^k i_k(S)C_{n-k-2}.}\tag{1}
\]
This identity makes no independence assumption on \(S\) itself; only the prescribed subsets of actual ears must be independent. In particular \(i_1(S)=|S|\), so the first two terms are \(C_{n-2}-2|S|C_{n-3}\).

**3. Two-adic bound for all higher terms.** The classical Catalan valuation formula (Legendre's formula or the binary-digit criterion) is
\[
v_2(C_t)=s_2(t+1)-1\qquad(t\ge0).
\]
Put \(N=n-1\), so \(v_n=s_2(N)-1\). For each \(k\ge2\) appearing in (1), the factor \(2^kC_{n-k-2}\) has valuation
\[
k+s_2(N-k)-1\ \ge\ s_2(k)+s_2(N-k)\ \ge\ s_2(N)=v_n+1.
\]
The first inequality uses \(k\ge s_2(k)+1\) for every integer \(k\ge2\), and the second follows from the digit-sum inequality \(s_2(a+b)\le s_2(a)+s_2(b)\). Consequently **all** terms of (1) with \(k\ge2\) vanish modulo \(2^{v_n+1}\).

**4. The parity dichotomy.** For the singleton term \(2C_{n-3}\), its valuation is \(s_2(N-1)\). When \(n\) is odd, \(N\) is even, and subtracting one from an even binary integer never decreases its binary digit sum: \(s_2(N-1)\ge s_2(N)=v_n+1\). Hence the singleton term also vanishes modulo \(2^{v_n+1}\). Formula (1) yields \(W_n(S)\equiv C_{n-2}\pmod{2^{v_n+1}}\), and \(C_{n-2}/2^{v_n}\) is odd; therefore the valuation is exactly \(v_n\) at every frequency.

When \(n\) is even, \(N\) is odd, so \(s_2(N-1)=s_2(N)-1=v_n\). Thus the constant and the singleton term each have exact valuation \(v_n\). After division by \(2^{v_n}\), their odd units reduce modulo two to \(1\) and \(|S|\); all terms with \(k\ge2\) reduce to zero. This proves \(W_n(S)/2^{v_n}\equiv1+|S|\pmod2\). It also proves that every \(W_n(S)\) is divisible by \(2^{v_n}\). Taking \(S=\varnothing\) shows the gcd is exactly \(2^{v_n}\).

**5. Convolution consequences.** The Walsh characters form a basis of \(\mathbb C^{(\mathbb Z/2\mathbb Z)^n}\) and diagonalize counting convolution by \(f_n\), with eigenvalues exactly \(W_n(S)\). For odd \(n\), all \(2^n\) eigenvalues are nonzero, and each has valuation \(v_n\), yielding \(v_2(|\det T_n|)=2^n v_n\). For even \(n\), the \(2^{n-1}\) even-cardinality characters survive, proving the rank bound. The explicit odd sequence \(n=2^k+3\) has \(s_2(n-1)=2\), hence \(v_n=1\); its Catalan count is even, yet every multiplier has exact valuation one.

## Verification

The complete standard-library script `check.py` computes formula (1) using independent-set subset enumeration and the subset-zeta transform. It separately enumerates convex polygon triangulations from the geometric diagonal-splitting recurrence, converts the resulting polygons into original-boundary ear masks, and applies the exact integer fast Walsh–Hadamard transform to their multiplicity histogram. Both procedures give identical individual Walsh coefficients for all \(5\le n\le11\), a total of \(4064\) independently compared frequencies. It additionally checks the stated parity and valuation congruences by exact arithmetic for all \(5\le n\le18\), not merely for sample signings. Run `python3 check.py` to reproduce the checks. The all-order proof above is independent of the finite computation; an exhaustive finite check would not establish the infinite theorem.

## Relationship to prior work

Hurtado and Noy's classical ear enumeration establishes total and specified ear counting, while Callan, Asinowski–Regev, and Mansour–Rastegar study aggregate ear statistics, symmetry, and generating functions. None of the inspected primary texts states the above **positionwise, all-frequency dyadic valuation law**. Postnikov–Sagan's Catalan valuation identity is used as an explicit known input rather than claimed as a new result.

The published study *Sharp harmonic observability crossover for ear patterns of random polygon triangulations* concerns the covariance and discrete spatial Fourier eigenvalues of the first-order ear-tip observation vector. Those pairwise moments do not give all \(2^n\) binary Walsh multipliers or the all-order dyadic modulus. The separate published study *Fourier rigidity and cancellation for convex-polygon triangulations* uses **all nonboundary diagonal-incidence coordinates**. Importantly, each original-boundary ear tip is indeed equivalent to the presence of its corresponding short diagonal \((i-1,i+1)\): consequently the present frequency space embeds as the *ear-diagonal-restricted* Walsh sector of that earlier, larger diagonal Fourier space. Its published uniform modulo-four congruence for odd polygons **already implies** the present odd-order exact valuation when \(v_n=0\) or \(v_n=1\); these lower-valuation cases are not independently new. It does **not** establish the present sharper congruence modulo \(2^{v_n+1}\) for the infinitely many odd sizes with \(v_n\ge2\), or the even-size ear-frequency parity stratum. In particular, that work has a singular unrestricted diagonal Walsh frequency at the 15-gon, while the present theorem proves every frequency supported only on the ear diagonals is nonzero there. Related noncrossing-matching and partition Fourier results use different statistical supports. The current contribution is the exact joint-ear identity (1) combined with a uniform binary-digit valuation argument, not a redistribution of an earlier pair-covariance theorem.

## Limitations

The theorem gives a common two-adic valuation for **all** odd-order multipliers and one exact valuation stratum for even orders; it does not give the entire signed magnitude spectrum, sharp real/complex inverse norms, nor a full singularity classification for even polygon sizes. No claim concerns random nonconvex triangulations, an unweighted indicator kernel discarding ear-profile multiplicities, or the spectrum of a triangulation-flip Markov chain. The published literature search and inspection reduce but cannot eliminate the possibility of a historical multivariate signed-ear identity with a stronger consequence. Independent mathematical validation is not claimed.

## References

1. F. Hurtado and M. Noy, *Ears of triangulations and Catalan numbers*, Discrete Mathematics 149 (1996), 319–324. Full text: https://core.ac.uk/download/pdf/82091698.pdf . The publication year is known; a precise earliest online release date was not established.
2. A. Postnikov and B. E. Sagan, *What power of two divides a weighted Catalan number?*, first public arXiv version 2006-01-13, https://arxiv.org/abs/math/0601339 .
3. D. Callan, *A variant of Touchard's Catalan number identity*, first public arXiv version 2012-04-25, https://arxiv.org/abs/1204.5704 .
4. A. Asinowski and A. Regev, *Triangulations with few ears: symmetry classes and disjointness*, first public arXiv version 2013-09-03, https://arxiv.org/abs/1309.0743 .
5. T. Mansour and R. Rastegar, *On typical triangulations of a convex n-gon*, https://arxiv.org/abs/1911.04025 .
6. *Sharp harmonic observability crossover for ear patterns of random polygon triangulations*, published scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-harmonic-observability-crossover-for-ear-patterns-of-rando--503a9ed7716d .
7. *Fourier rigidity and cancellation for convex-polygon triangulations*, published scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-fourier-rigidity-and-cancellation-for-convex-polygon-triangulati--e73d48554b89 .
