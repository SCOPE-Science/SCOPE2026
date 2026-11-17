# Exact crossing–short-chord transform and Gaussian–Poisson decoupling in random chord diagrams

## Finding

For every integer \(n\ge2\), draw a uniformly random perfect matching of \(2n\) distinct points in their fixed cyclic order. Let \(S_n\) count *simple chords* (matched adjacent points, with cyclic adjacency), and let \(X_n\) count pairs of chords crossing in the circle. Put
\[
T_m(z)=\sum_{D\in\mathcal D_m}z^{X(D)},\qquad T_0(z)=T_1(z)=1,
\]
where \(\mathcal D_m\) is the set of perfect matchings of the cyclically ordered \(2m\) endpoints. Define
\[
M_{n,k}=\frac{2n}{2n-k}\binom{2n-k}{k},\qquad 0\le k\le n.
\]
Then the **complete finite bivariate enumerator** satisfies
\[
\boxed{\sum_{D\in\mathcal D_n}t^{S(D)}z^{X(D)}
=\sum_{k=0}^n M_{n,k}(t-1)^kT_{n-k}(z).}\tag{1}
\]
The right side depends only on the classical crossing polynomials \(T_m\) and the explicit number \(M_{n,k}\) of \(k\)-edge matchings of a cycle with \(2n\) vertices. In particular, the transform determines every exact joint probability \(\Pr(S_n=s,X_n=x)\) from crossing-number distributions at smaller sizes.

An unexpectedly simple consequence, valid **exactly for every** \(n\ge2\), is
\[
\boxed{\operatorname{Corr}(S_n,X_n)=-\sqrt{\frac5{n+3}}.}\tag{2}
\]
The corresponding covariance is
\[
\operatorname{Cov}(S_n,X_n)=-\frac{2n(n-1)}{3(2n-1)}.
\tag{3}
\]
Finally, with \(\mu_n=n(n-1)/6\) and \(\sigma_n^2=n(n-1)(n+3)/45\),
\[
\boxed{\left(\frac{X_n-\mu_n}{\sigma_n},S_n\right)
\xrightarrow{d}(Z,P),}\tag{4}
\]
where \(Z\) is standard normal, \(P\) is Poisson with mean one, and **\(Z\) and \(P\) are independent**. The finite covariance diverges linearly while the standardized correlation tends to zero at the exact rate \(\sqrt{5/(n+3)}\).

## Assumptions and scope

The matching on the labeled cyclic endpoints \(\{1,\ldots,2n\}\) is uniform among the \((2n-1)!!\) possibilities. Each matching edge is drawn as a chord of the same circle. A pair of chords crosses exactly when its four endpoints alternate cyclically. A simple chord joins two cyclically consecutive endpoints (including \(1\) and \(2n\)). For \(n\ge2\), these are the \(2n\) distinct potential edges of the boundary cycle. A chord connecting consecutive endpoints cannot cross any other chord. The degenerate \(n=1\) case is separate (one chord, one simple chord, no crossings); formulas (1)–(4) are asserted for \(n\ge2\) where relevant, and formula (4) concerns \(n\to\infty\).

The definitions of \(T_m\) and \(M_{n,k}\) are ordinary finite integers, not asymptotic approximations. The empty pairing contributes \(T_0(z)=1\); by convention \((-1)!!=1\). For expectations and correlations, the distribution is the uniform probability distribution on \(\mathcal D_n\).

## Proof

**Step 1: the exact weighted deletion identity.** Fix a \(k\)-element set \(F\) of distinct boundary edges that have no shared endpoints. A diagram contains all these edges as chords with probability
\[
\frac{(2n-2k-1)!!}{(2n-1)!!}.
\]
Among diagrams containing \(F\), removing the matched endpoints of those edges leaves an arbitrary perfect matching of the remaining \(2(n-k)\) cyclically ordered points, with a bijection to \(\mathcal D_{n-k}\). All chords in \(F\) are noncrossing with *every* other chord, and deleting their endpoints preserves the alternating order of every remaining four-tuple. Thus the original crossing count is exactly the remaining matching's crossing count; no probabilistic approximation is involved.

There are exactly
\[
M_{n,k}=\frac{2n}{2n-k}\binom{2n-k}{k}
\]
possible sets \(F\): this is the standard circular-spacing count for selecting \(k\) mutually nonincident edges on the cycle with \(2n\) vertices. For \(k=n\), it gives the two alternating perfect matchings of that cycle; for \(k=0\), it equals one. Double-counting pairs \((D,F)\) with \(F\) a \(k\)-element subset of the simple chords of \(D\) gives, **for every** \(0\le k\le n\),
\[
\sum_{D\in\mathcal D_n}\binom{S(D)}kz^{X(D)}=M_{n,k}T_{n-k}(z).\tag{5}
\]
Now expand \(t^{S(D)}=(1+(t-1))^{S(D)}\) and interchange finite sums to obtain (1). Equivalently, every joint-count coefficient is
\[
\#\{D:S(D)=s,X(D)=x\}
=\sum_{k=s}^n(-1)^{k-s}\binom ks M_{n,k}[z^x]T_{n-k}(z),\tag{6}
\]
which gives the claimed complete distribution without an unproved recurrence.

**Step 2: exact correlation.** Divide (5) by \((2n-1)!!\) and set
\[
w_{n,k}=M_{n,k}\frac{(2n-2k-1)!!}{(2n-1)!!}
=\mathbb E\binom{S_n}{k}.\tag{7}
\]
The first two coefficients give
\[
\mathbb ES_n=\frac{2n}{2n-1},\qquad
\mathbb E\bigl[S_n(S_n-1)\bigr]=\frac{2n}{2n-1},
\]
and hence
\[
\operatorname{Var}(S_n)=\frac{4n(n-1)}{(2n-1)^2}.\tag{8}
\]
The known exact crossing moments (Flajolet–Noy; also Paguyo, Lemma 2.2) are
\[
\mathbb EX_n=\frac{n(n-1)}6,\qquad
\operatorname{Var}(X_n)=\frac{n(n-1)(n+3)}{45}.\tag{9}
\]
Taking the derivative of (5) in the simple-chord variable at \(t=1\), or directly setting \(k=1\) and differentiating in \(z\) at \(1\), gives
\[
\mathbb E[S_nX_n]=\frac{2n}{2n-1}\frac{(n-1)(n-2)}6.\tag{10}
\]
Subtract the product of the two means to get (3). Substituting (8) and (9) into the definition of Pearson correlation yields (2), including its strict negative sign. For \(n=2\), the correlation is exactly \(-1\); for \(n\ge3\), its magnitude is strictly between zero and one.

**Step 3: joint Gaussian–Poisson limit.** By (7), for \(0\le k\le n\) one has
\[
w_{n,k}=\frac{2n}{2n-k}\frac{2^k}{k!}
\prod_{j=0}^{k-1}\frac{n-j}{2n-j}.
\tag{11}
\]
Each factor in the product is at most \(1/2\), and \(2n/(2n-k)\le2\); therefore \(0\le w_{n,k}\le2/k!\). For any **fixed** \(k\), (11) gives \(w_{n,k}\to1/k!\).

Fix a bounded continuous function \(f\) and \(0\le t\le1\). Applying the same double-counting argument to the standardized crossing count \(W_n=(X_n-\mu_n)/\sigma_n\) gives
\[
\mathbb E[t^{S_n}f(W_n)]
=\sum_{k=0}^n(t-1)^kw_{n,k}
\mathbb E\left[f\left(\frac{X_{n-k}-\mu_n}{\sigma_n}\right)\right].\tag{12}
\]
For fixed \(k\) and \(n\to\infty\), the established univariate crossing central limit theorem applies at size \(n-k\). Furthermore,
\[
\frac{\sigma_{n-k}}{\sigma_n}\to1,\qquad
\frac{\mu_{n-k}-\mu_n}{\sigma_n}\to0.
\]
It follows that the expectation in each fixed-\(k\) summand of (12) tends to \(\mathbb E f(Z)\). Its absolute value is bounded by \(2\|f\|_\infty/k!\); dominated convergence of the series therefore gives
\[
\lim_{n\to\infty}\mathbb E[t^{S_n}f(W_n)]
=\mathbb Ef(Z)\sum_{k=0}^\infty\frac{(t-1)^k}{k!}
=e^{t-1}\mathbb Ef(Z).\tag{13}
\]
The right-hand side factors as the probability generating function of a Poisson-one random variable times the expectation of \(f(Z)\). This identity for every bounded continuous \(f\) and \(t\in[0,1]\), together with tightness of the marginals, uniquely identifies the independent joint weak limit (4). The theorem does not assert finite-size independence; (3) shows that finite-size independence is false.

## Verification

A standalone Python 3 standard-library program, `verify.py`, enumerates all perfect matchings through six chords, constructs the joint \((S,X)\) census, independently checks the cycle-matching coefficient \(M_{n,k}\) through five chords, checks every integer weighted factorial identity (5), inverts (6) coefficient by coefficient, and verifies the exact means, variances, covariance, and squared correlation as rational numbers. It reports **385 exact assertions passed**. It independently enumerates all \((2n-1)!!\) diagrams for \(n=1,\ldots,6\). Run `python3 verify.py` from a directory containing the embedded program; no data files, libraries, randomness, or network access are required.

The computation checks finite instances, not the infinite assertion (4). The latter follows from the deletion identity, summable bound (11), and the established univariate crossing CLT, as reconstructed in Step 3.

## Relationship to prior work

Acan, *On a uniformly random chord diagram and its intersection graph* (arXiv:1501.01489, first posted January 7, 2015), studies the same exact uniform chord-diagram model; its manuscript identifies primary MSC 60C05. It develops intersection-graph structure, chord degrees, components, and evolution, not a crossing-versus-simple-chord joint enumerator. Flajolet–Noy, *Analytic Combinatorics of Chord Diagrams* (INRIA RR3914, 2000), establish univariate crossing moments/CLT and component laws. These univariate results are used but not claimed anew. Paguyo, *Convergence Rates of Limit Theorems in Random Chord Diagrams* (arXiv:2104.01134, first posted April 2, 2021), provides separate quantitative Gaussian approximations for crossings and Poisson approximations for simple chords; its Sections 2 and 3 do not state the exact bivariate deletion transform, correlation (2), or a joint asymptotic-independence theorem. Thus separate marginal convergence does not, by itself, imply (4). The Pilaud–Rué fixed-crossing perfect-matching generating functions (arXiv:1307.6440) mark vertices and crossings, not cyclicly adjacent matched pairs, so they do not provide the joint law. The explicit full joint transform (1) and its exact nonzero dependence (2) are the primary contribution.

## Limitations

This is a purely combinatorial uniform perfect-matching model; no weighted, nonuniform, geometric-length, or conditioned-crossing ensemble is treated. For the exceptional \(n=1\) case, boundary adjacency is degenerate and correlation is undefined. The limiting independence is weak convergence under the stated normalization; no uniform bivariate total-variation bound or numerical convergence rate is asserted. Prior-art searches and targeted inspection of the relevant manuscripts support provisional originality, but an unindexed or implicit older enumeration could already subsume (1). This is not an independently audited publication or uniqueness certificate.

## References

1. Hüseyin Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489 (first public arXiv version 2015-01-07), https://arxiv.org/abs/1501.01489 . Primary MSC 60C05 stated on the first page.
2. Philippe Flajolet and Marc Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA RR3914 (March 2000), https://algo.inria.fr/flajolet/Publications/FlNo00.pdf .
3. J. E. Paguyo, *Convergence Rates of Limit Theorems in Random Chord Diagrams*, arXiv:2104.01134 (initial arXiv submission 2021-04-02), https://arxiv.org/abs/2104.01134 .
4. J. Riordan, *The distribution of crossings of chords joining pairs of \(2n\) points on a circle*, Mathematics of Computation 29 (1975), 215–222, DOI:10.2307/2005477 (historical crossing-number marginal, not asserted as newly derived here).
5. Vincent Pilaud and Juanjo Rué, *Analytic Combinatorics of Chord and Hyperchord Diagrams with \(k\) Crossings*, arXiv:1307.6440 (first posted 2013-07-24), https://arxiv.org/abs/1307.6440 . Their full paper treats fixed-crossing enumerators, not simple-chord/crossing bivariate marking.
