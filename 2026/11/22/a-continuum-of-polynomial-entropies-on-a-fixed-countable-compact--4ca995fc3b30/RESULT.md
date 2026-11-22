# A continuum of polynomial entropies on a fixed countable compactum

## Finding

For every real \(\beta\in[1,2]\) there is a continuous selfmap \(T_\beta\) of a compact countable metrizable space homeomorphic to the ordinal interval \(\omega^2+1\) such that:

1. \(T_\beta\) has a dense forward orbit;
2. its **only** invariant Borel probability is the point mass at its unique fixed point;
3. its topological entropy vanishes, while its forward Bowen polynomial entropy is exactly \(h_{\mathrm{pol}}(T_\beta)=\beta\).

More precisely, for every real \(\alpha\ge1\), set \(d_j=\lfloor j^\alpha\rfloor\) for integers \(j\ge1\), \(s_0=0\), and \(s_k=\sum_{j=1}^k d_j\). Let \(w\in\{0,1\}^{\mathbb N_0}\) have a marker \(w_i=1\) precisely at positions \(s_k\), and let \(X_\alpha\) be the closure of its forward one-sided shift orbit. The number \(p_\alpha(n)\) of distinct length-\(n\) factors for every integer \(n\ge2\) is **exactly**

\[
p_\alpha(n)=n+2+\sum_{j\ge1}\max\bigl(0,\min(d_j,n-d_{j+1})\bigr).
\]

(The sum is finite for each \(n\); \(p_\alpha(1)=2\).) Moreover,

\[
\lim_{n\to\infty}\frac{p_\alpha(n)}{n^{1+1/\alpha}}
=\frac{\alpha}{\alpha+1}\bigl(1-2^{-1/\alpha}\bigr)>0.
\]

Therefore \(h_{\mathrm{pol}}(\sigma|_{X_\alpha})=1+1/\alpha\). For the endpoint \(\beta=1\), use the same construction with \(d_j=2^{j-1}\), when \(n+2\le p(n)\le2n+2\) for \(n\ge2\). These examples are pairwise nonconjugate for distinct \(\beta\), despite having the same underlying compact-space homeomorphism type and the same single-atom invariant-measure simplex.

## Assumptions and scope

The space is the one-sided full binary shift \(\{0,1\}^{\mathbb N_0}\) with the product topology, and \(\sigma(x)_i=x_{i+1}\). A marker gap \(d_j\) is the **distance between two consecutive markers**, not the number of zeros between them. All gap sequences here are strictly increasing and unbounded; every \(d_j\) is a positive integer and \(d_1=1\). The closure includes marker-free and single-marker limits. \(p(n)\) counts factors of the infinite word (equivalently, length-\(n\) cylinders meeting its orbit closure), not words in a finite prefix.

For a continuous selfmap \(T\) of a compact metric space, with \(d_n(x,y)=\max_{0\le j<n}d(T^j x,T^j y)\), define \(s_n(\varepsilon)\) as the maximum cardinality of a set whose distinct points have \(d_n(x,y)\ge\varepsilon\). Its forward Bowen polynomial entropy is

\[
h_{\mathrm{pol}}(T)=\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}
\frac{\log s_n(\varepsilon)}{\log n}.
\]

The result concerns continuous **noninvertible** maps with a dense forward orbit; it does not claim minimality, ordinary mixing, or realization of exponents outside the stated interval.

## Proof

**1. Orbit closure and ordinal topology.** Consider first any strictly increasing unbounded positive integer gap sequence. Write \(e_r\) for the infinite binary sequence with its only \(1\) at position \(r\), for \(r\in\mathbb N_0\), and \(z=0^\infty\). Every shift \(\sigma^m w\) is distinct: otherwise the marker set would be eventually periodic, contradicting unbounded gaps. Each shift is isolated in the orbit closure because a sufficiently long prefix contains three markers, and its two successive gap distances identify their unique consecutive occurrences in \(w\), then identify the shift starting index. As \(m\to\infty\), the gaps encountered by any fixed finite window eventually grow without bound; thus every convergent subsequence of distinct orbit points has at most one marker in its limit. Conversely, \(e_r=\lim_{k\to\infty}\sigma^{s_k-r}w\) for each fixed \(r\), and shifts starting halfway across increasing gaps converge to \(z\). Hence

\[
X=\{\sigma^m w:m\ge0\}\cup\{e_r:r\ge0\}\cup\{z\},
\qquad X'=\{e_r:r\ge0\}\cup\{z\},\quad X''=\{z\},\quad X'''=\varnothing.
\]

Here primes denote successive Cantor–Bendixson derivatives. The first derivative is a convergent sequence with unique accumulation point \(z\), and the second derivative is a singleton. By the classical Mazurkiewicz–Sierpiński classification of countable compact metrizable spaces (as restated in Pérez-Remolina–Uzcátegui-Aylwin, Theorem 2.1), \(X\) is homeomorphic to \(\omega^2+1\). It is shift invariant and compact, and \(w\) has a dense forward orbit by definition. The shift fixes \(z\) and maps \(e_{r+1}\) to \(e_r\), with \(e_0\mapsto z\), so \(z\) is its only periodic point.

**2. Exact factor census for strictly increasing gaps.** For every \(n\ge1\), all \(n\) different one-marker length-\(n\) words occur by centering a window in a sufficiently large gap, and the all-zero factor also occurs. For any other factor, let its first two markers be the consecutive global markers \(s_{k-1}\) and \(s_k\), with internal distance \(d_k\). Since the distances \(d_k\) are pairwise different, a factor with at least two markers uniquely determines \(k\), together with the number of leading zeros (hence its starting position); it cannot be double-counted even if it contains additional markers.

For \(k=1\), its starting position must be zero and its window must contain \(s_1=d_1=1\), yielding one such factor for every \(n\ge2\). For \(k\ge2\), if the window begins at integer \(t\), the first two marked positions require

\[
s_{k-2}<t\le s_{k-1},\qquad t+n-1\ge s_k.
\]

The number of permitted starting points is therefore exactly

\[
\max\bigl(0,\min(d_{k-1},n-d_k)\bigr).
\]

Summing and reindexing gives the formula in the Finding. The orbit closure introduces no new factors because each finite prefix of each limit point already occurs in the original word. This is an **all-length identity**, not an asymptotic approximation.

**3. Polynomial-gap asymptotics.** For fixed \(\alpha\ge1\), the sequence \(d_j=\lfloor j^\alpha\rfloor\) is strictly increasing: consecutive real powers differ by at least one. Put \(N=n^{1/\alpha}\). Only indices \(j=O(N)\) can contribute to the formula. Uniformly for \(0\le j\le 2N\), the scaled floor values satisfy

\[
\frac{d_j}{n}=\left(\frac jN\right)^\alpha+o(1),\qquad
\frac{d_{j+1}}{n}=\left(\frac jN\right)^\alpha+o(1),
\]

with the first formula applied to positive \(j\). Thus the finite sum is a Riemann sum for \(\max(0,\min(x^\alpha,1-x^\alpha))\) on \([0,1]\). The exact integral is

\[
\int_0^1\min(x^\alpha,1-x^\alpha)\,dx
=\frac\alpha{\alpha+1}\bigl(1-2^{-1/\alpha}\bigr),
\]

by splitting at \(x=2^{-1/\alpha}\). As \(n+2=o(nN)\), the claimed positive asymptotic follows. In particular, \(\alpha=1\) gives \(p(n)\sim n^2/4\).

**4. Geometric endpoint.** If \(d_j=2^{j-1}\), the sum from Step 2 is nonnegative and at most \(\sum_{d_{j+1}<n}d_j<n\). Consequently \(n+2\le p(n)\le2n+2\) for \(n\ge2\), so the word growth exponent is exactly one.

**5. Bowen complexity and ordinary entropy.** Equip the one-sided shift with the standard ultrametric \(d(x,y)=2^{-\min\{i:x_i\ne y_i\}}\) (and zero on the diagonal). For \(\varepsilon=1\), maximal \((n,\varepsilon)\)-separated cardinality is exactly \(p(n)\), since distinct first-\(n\) blocks differ at one of the first \(n\) time-zero coordinates. For any fixed integer \(r\ge1\), an \((n,2^{-r})\)-separated set has at most \(p(n+r+1)\) points, as agreement on the first \(n+r+1\) symbols prevents such separation. Taking logarithmic rates and then \(r\to\infty\), the polynomial entropy equals the exponent of \(p(n)\), which is \(1+1/\alpha\) for polynomial gaps and one for geometric gaps. Since \(\log p(n)/n\to0\), all the systems have zero ordinary topological entropy.

**6. Uniqueness of the invariant probability.** For every increasing unbounded gap sequence, the number \(R(n)\) of markers among the first \(n\) positions of the original word is \(o(n)\): if the marker count is \(k\), its interval length exceeds the sum of its first \(k-1\) gaps, whose average tends to infinity. Among **any** \(n\) consecutive positions of the word, the marker count is at most \(R(n)+1\), since consecutive gap lengths increase. Points in \(X\) that are limits have at most one marker. Hence \(\sup_{x\in X}n^{-1}\sum_{i=0}^{n-1}x_i\to0\). For every invariant Borel probability \(\mu\), shift invariance and integration yield

\[
\mu\{x:x_0=1\}=\int_X\frac1n\sum_{i=0}^{n-1}x_i\,d\mu(x)\longrightarrow0.
\]

Invariance makes \(\mu\{x:x_i=1\}=0\) for each \(i\ge0\), so the countable union of all these cylinders has measure zero; therefore \(\mu=\delta_z\). This establishes unique ergodicity in the invariant-probability sense, without claiming minimality.

Finally, set \(\alpha=1/(\beta-1)\) for each \(1<\beta\le2\), and use the geometric-gap case for \(\beta=1\). All systems have the same ordinal compactum as underlying space. Polynomial entropy is invariant under topological conjugacy, so the distinct exponents imply pairwise nonconjugacy.

## Verification

The bundled Python 3 standard-library script `verify.py` independently enumerates all factors of sufficiently long finite marker prefixes and compares them against the derived exact formula. It tests every length \(1\le n<130\) for each exponent \(\alpha=1,1.01,1.25,1.5,2,2.25,3,4\) and for geometric gaps. For each tested \(n\), the prefix extends past a gap longer than \(n\) and contains the full set of relevant two-marker pairs, making the finite factor test exhaustive at **that** length. The checks passed. These finite checks corroborate the classification but do not establish the limit theorem, topology, uniqueness of invariant measure, or infinite quantifiers; those are proved above.

## Relationship to prior work

Pérez-Remolina and Uzcátegui-Aylwin (2026) prove the existence of dense-orbit continuous maps on every countable compact metrizable space and continuum many conjugacy classes when the second derivative is nonempty. Their inspected manuscript, including the constructions on \(\omega^2+1\), does not determine forward polynomial entropy, unique invariant probability or any exact factor-growth constant. The present result supplies a quantitative spectrum **inside one fixed ordinal homeomorphism type**, not a new proof of their general existence theorem.

Artigue, Carrasco-Olivera and Monteverde (2018) explicitly cite older word-complexity constructions with polynomial entropy spanning \((1,2)\) for subshifts; this precedes and covers the unrestricted assertion that such exponents are possible in some subshift. The distinct statement here is simultaneous realization on a compact **countable** rank-three ordinal space, with one dense forward orbit, a unique invariant point mass, and a family-specific asymptotic constant. A previously published closed-factor classification for increasing-gap binary words treats the different invariant of *closed factors* of finite words; it does not assert the all-factor finite-window census or the stated ordinal dynamical spectrum. A separate perfect-square indicator calculation gives an ordinary factor-growth comparison at one quadratic-support example, not the general continuum and ordinal topology.

## Limitations

No claim is made that \([1,2]\) is the entire set of polynomial entropies possible for **all** continuous maps on \(\omega^2+1\); only this interval is realized. The examples are noninvertible and not minimal. The historical literature already establishes unrestricted fractional polynomial entropy in larger spaces, and earlier binary-word techniques may provide implicit shortcuts for part of the counting argument. The full text of Cassaigne's 1997 general word-complexity paper was not accessible during this comparison, so a hidden equivalent specific sparse-word asymptotic remains a priority risk. The exact ordinal realization and unique invariant-measure conjunction was not found in the inspected literature. Finite computations are not a substitute for the proof. No independent external mathematical audit was performed.

## References

1. J. Pérez-Remolina and C. Uzcátegui-Aylwin, *Countable dynamical systems with a dense orbit*, arXiv:2611.17315v1, first public 2026-11-12, https://arxiv.org/html/2611.17315v1 .
2. A. Artigue, D. Carrasco-Olivera and I. Monteverde, *Polynomial Entropy and Expansivity*, arXiv:1801.08774 (2018), https://arxiv.org/abs/1801.08774 .
3. J. Cassaigne, *Complexité et facteurs spéciaux*, Bull. Belg. Math. Soc. Simon Stevin 4 (1997), 67–88, DOI:10.36045/bbms/1105730624 .
4. *Exact closed-factor counts for increasing-gap binary words*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-closed-factor-counts-for-increasing-gap-binary-words--134b7695e707 (full scientific result inspected).
5. *Exact reflection complexity of the perfect-square indicator word*, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-reflection-complexity-of-the-perfect-square-indicator-word--fe330b1e5833 (full scientific result inspected).
