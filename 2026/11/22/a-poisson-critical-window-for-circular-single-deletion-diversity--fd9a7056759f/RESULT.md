# A Poisson critical window for circular single-deletion diversity at fixed binary weight

## Finding
Let \(W_{n,k}\) be uniform among the \(\binom nk\) **indexed** binary words of length \(n\) and weight \(k\). After deleting exactly one symbol, identify outputs differing only by cyclic rotation, and write \(D_{n,k}\) for the number of different resulting necklaces. Let \(R_{n,k}\) count the cyclic runs of ones, and let \(Z_{n,k}\) count adjacent one-one edges of the source circle. In particular \(R_{n,k}=k-Z_{n,k}\).

For every \(1\le k\le n/2\) and integer \(1\le \ell\le(n-2)/2\), put \(p=k/n\) and \(b_{n,k}=\binom nk p^k(1-p)^{n-k}\). The following **finite-size total-variation comparison** holds:
\[
 d_{\rm TV}\bigl(\mathcal L(D_{n,k}),\mathcal L(2R_{n,k})\bigr)
 \le \frac{\binom n2(1-p)^\ell}{b_{n,k}}.
\]
The reference law is explicit: for \(1\le r\le\min(k,n-k)\),
\[
 \Pr(R_{n,k}=r)=\frac{n}{r\binom nk}
 \binom{k-1}{r-1}\binom{n-k-1}{r-1}.
\]
Thus this distribution gives every point probability for the actual circular deletion degree, with the same uniform additive error as the displayed total-variation bound.

In particular, for every integer sequence \(k=k_n\) with \(k_n\to\infty\) and \(k_n^2/n\to\lambda\in(0,\infty)\),
\[
 2k_n-D_{n,k_n}\ \Longrightarrow\ 2\operatorname{Poisson}(\lambda),
\quad \mathbb E(2k_n-D_{n,k_n})\to2\lambda,
\quad \operatorname{Var}(D_{n,k_n})\to4\lambda.
\]
Also \(\Pr(D_{n,k_n}=2k_n)\to e^{-\lambda}\). In this critical window the full circular deletion shadow has an **even-valued non-Gaussian deficit**. The result concerns indexed, fixed-content source sampling, not uniform sampling of rotation classes.

## Assumptions and scope
Words are binary, circular, and indexed before sampling; their deletion outputs are unindexed rotation classes of length \(n-1\). A cyclic run is maximal under circular adjacency. The symbol-count assumption \(0<k<n\) excludes constant words. The finite bound assumes \(k\le n/2\) and \(2\ell\le n-2\). The limit assumes the precise critical scaling \(k_n^2/n\to\lambda>0\). No statement about two or more deletions is made.

## Proof
**1. Uniqueness implies exact run diversity.** For any nonconstant circular word \(w\), deletions within one cyclic constant-symbol run produce the same necklace; consequently its deletion degree is at most the number \(S(w)\) of its cyclic runs. Suppose every cyclic factor of length \(\ell\) occurs at a unique phase and \(2\ell<n-1\). If deleting at two positions produces necklaces related by a rotation, align their surviving \(n-1\) symbols in that rotation. At most \(\ell\) starting phases on each side correspond to length-\(\ell\) blocks crossing a deletion. Because \(n-1>2\ell\), one aligned block avoids both deletion sites and equals two source factors. Uniqueness forces its two source starting positions to agree. Consequently the order-preserving alignment of survivors fixes that source phase. Along the two arcs between deletion sites, the aligned source indices now either agree or are shifted by one; the symbols on the shifted arc must all coincide. The deleted sites therefore lie in the same cyclic constant-symbol run. Distinct runs give distinct output necklaces. Hence \(D(w)=S(w)\) under factor uniqueness. In a binary nonconstant circle \(S(w)=2R(w)=2(k-Z(w))\).

**2. A collision bound for long factors.** First sample independent Bernoulli\((p)\) bits around the circle. Fix two distinct phase starts and demand that their length-\(\ell\) factors agree. The equality constraints form edges \(t\leftrightarrow t+s\) on the \(n\)-cycle, for a fixed nonzero shift \(s\), with the \(\ell\) edge starts in a contiguous circular interval. For \(\ell<n/2\) this undirected graph is a forest: a cycle would require all members of a translation orbit, which occupy an arc of span at least \(n/2\). In any component of \(v\) vertices, equality has probability \(p^v+(1-p)^v\le(1-p)^{v-1}\) since \(p\le1/2\). Multiplying over components yields a factor-collision probability at most \((1-p)^\ell\). Union bound over \(\binom n2\) phase pairs and conditioning on total weight exactly \(k\) divide this probability by \(b_{n,k}\). Coupling \(D\) to \(2R\) on the same source then proves the stated total-variation inequality.

**3. Exact fixed-weight run law.** A binary circle with \(r\) positive one-runs and \(r\) positive zero-runs is specified by two positive compositions of \(k\) and \(n-k\) into \(r\) parts and an indexed run-start position; each indexed word is counted \(r\) times. Thus the number is \(n\binom{k-1}{r-1}\binom{n-k-1}{r-1}/r\), proving the reference probabilities.

**4. Critical-limit and moments.** The number of adjacent one-one edges is \(Z=\sum_{i\bmod n}\mathbf1_{\{W_i=W_{i+1}=1\}}\). For fixed positive integer \(j\), in its factorial moment \(\mathbb E(Z)_j\), ordered collections of \(j\) pairwise vertex-disjoint edges give the main contribution
\[
 (n^j+O_j(n^{j-1}))\frac{(k)_{2j}}{(n)_{2j}}\longrightarrow\lambda^j.
\]
A collection with \(c<j\) connected components uses \(j+c\) occupied vertices; it contributes at most \(O_j(n^c(k/n)^{j+c})=o(1)\). Hence all factorial moments converge to those of \(\operatorname{Poisson}(\lambda)\), and \(Z\) converges to that law. The finite exact first two factorial moments are
\[
 \mathbb E Z=\frac{k(k-1)}{n-1},\qquad
 \mathbb E(Z)_2=2n\frac{(k)_3}{(n)_3}
 +n(n-3)\frac{(k)_4}{(n)_4}.
\]
For \(\ell=\lceil6(n/k)\log n\rceil\), the scaling assumptions ensure \(2\ell\le n-2\) eventually; the finite error is \(O(n^{-4}\sqrt k)=O(n^{-15/4})\), using the binomial local mass estimate \(b_{n,k}=\Theta(k^{-1/2})\). Since \(0\le2R-D\le 2k\), the first two moments differ from those of \(2R\) by \(o(1)\). This proves distributional and moment convergence and the full-degree probability.

## Verification
Run `python3 verify.py` alongside this document. The script independently generates circular deletion outputs by literal deletion and canonical rotation, tests the implication from factor uniqueness, verifies exact fixed-weight run counts and the cyclic adjacent-pair mean for all \(8{,}164\) nonconstant indexed binary words of lengths three through twelve, and verifies the forest assertion for \(9{,}690\) finite graph cases with lengths up to forty. The actual run returned `VERIFY_OK binary_sources 8164 forest_cases 9690`. These are finite checks, not substitutes for the infinite proof above.

## Relationship to prior work
Sloane's 2002 survey establishes classical linear one-deletion descendant counting by runs, but does not analyze circular deletion outputs under growing, sparse, fixed weight. The earlier short-factor uniqueness result for circular deletion shadows establishes the deterministic lemma and an i.i.d. fixed-alphabet Gaussian regime; that deterministic conclusion is a credited antecedent, not claimed as new. The substantial additional step here is an explicit **weight-conditioned** factor-collision bound with its \(k\asymp\sqrt n\) scaling, yielding a quantitative finite-source law and a Poisson rather than Gaussian deletion-degree correction. Balado and Silvestre (2026) survey fixed-content run enumerations, not this circular deletion-channel coupling. The exact fixed-weight run count is classical and explicitly not claimed as new.

## Limitations
This is an asymptotic limit theorem for indexed uniformly chosen fixed-weight words. It does not assert that all sources have run-exact circular deletion degree, and finite outliers exist. It also does not assert novelty for the classical Poisson run count, the reference run enumerator, or the deterministic short-factor lemma. The conditional factor-collision bound can be weak outside the specified scaling. Earlier specialized literature that directly identifies the same deletion-degree Poisson critical law would subsume the stated contribution; no proof of global literature uniqueness is claimed. Independent mathematical review has not been performed.

## References
1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197, first posted 2002-07-22, https://arxiv.org/html/math/0207197v1 .
2. F. Balado and G. C. M. Silvestre, *Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings*, arXiv:2602.10005, first posted 2026-02-10, especially §7.2, https://arxiv.org/html/2602.10005v2 .
3. F. Makri, Z. Psillakis, A. Arapis, *Counting Runs of Ones with Overlapping Parts in Binary Strings Ordered Linearly and Circularly*, International Journal of Statistics and Probability (2013), DOI:10.5539/ijsp.v2n3p50, https://ccsenet.org/journal/index.php/ijsp/article/view/28864 .
4. *Short-factor uniqueness makes circular one-deletion shadows asymptotically run-exact*, earlier related mathematical record, identifier `eef1c860-4afc-4b82-96f7-f580780ad6d6`.
