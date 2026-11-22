# Two distinct endpoint scales for size-marked block minima in uniform set partitions

## Finding
Let \(\Pi_n\) be a uniformly random partition of \([n]=\{1,\ldots,n\}\). For each fixed \(r\ge2\), write \(\mathcal B_{n,r}\) for its blocks of size \(r\), and let \(m(B)=\min B\). Put \(\rho_n=W(n)\), the positive solution of \(\rho_n e^{\rho_n}=n\). On \([0,\infty)\) form two point measures
\[
\Xi^{\mathrm L}_{n,r}=\sum_{B\in\mathcal B_{n,r}}\delta_{\rho_n^r m(B)/n},
\qquad
\Xi^{\mathrm R}_{n,r}=\sum_{B\in\mathcal B_{n,r}}\delta_{\rho_n(n-m(B))/n}.
\]
For every fixed \(K\ge2\), the \(2(K-1)\) point measures with \(2\le r\le K\) converge **jointly** in the vague topology to mutually independent Poisson point processes. Their respective intensity measures are
\[
\nu_r^{\mathrm L}(dx)=\frac{dx}{(r-1)!},
\qquad
\nu_r^{\mathrm R}(dx)=\frac{x^{r-1}}{(r-1)!}\,dx.
\]
In particular, let \(L_{n,r}=\min\{m(B):B\in\mathcal B_{n,r}\}\) and \(U_{n,r}=\max\{m(B):B\in\mathcal B_{n,r}\}\), with arbitrary conventions on the event that \(\mathcal B_{n,r}\) is empty. For each fixed \(r\ge2\) and \(t\ge0\),
\[
\Pr\left(\rho_n^r L_{n,r}/n>t\right)\longrightarrow\exp\left(-\frac{t}{(r-1)!}\right),
\qquad
\Pr\left(\rho_n(n-U_{n,r})/n>t\right)\longrightarrow\exp\left(-\frac{t^r}{r!}\right).
\]
These extrema converge **jointly and independently** for every finite family of sizes, including independence between the two ends. Thus the first minimum of an \(r\)-block is on scale \(n/(\log n)^r\), whereas the last such minimum is always within scale \(n/\log n\) of the right endpoint, with a size-dependent Weibull shape.

## Assumptions and scope
All set partitions of \([n]\) have equal probability \(1/B_n\), with \(B_n\) the Bell number. A block is included only when its cardinality is exactly the specified integer \(r\), and its position is its **smallest label**, not its largest label or its centroid. The number \(K\) and all sizes \(r\in\{2,\ldots,K\}\) are fixed as \(n\to\infty\). Counts on bounded Borel intervals whose boundaries have zero intensity are covered. No growing-size or uniform-in-\(r\) claim is made.

## Proof
**1. Exact block probabilities.** For any pairwise disjoint nonempty prescribed subsets \(S_1,\ldots,S_j\subseteq[n]\), the probability that all are blocks of \(\Pi_n\) is
\[
\Pr(S_1,\ldots,S_j\text{ are blocks})=\frac{B_{n-s}}{B_n},\qquad s=\sum_{a=1}^j|S_a|.
\]
For intersecting distinct prescribed subsets this joint event is impossible. Indeed, delete the prescribed blocks and partition the \(n-s\) remaining labels. Consequently the single-minimum probability is exactly
\[
\Pr(\text{the block with minimum }i\text{ has size }r)
=\binom{n-i}{r-1}\frac{B_{n-r}}{B_n}.
\]
For example, the expected number of \(r\)-blocks whose minimum is in the integer interval \([\ell,u]\) is exactly
\[
\left[\binom{n-\ell+1}{r}-\binom{n-u}{r}\right]\frac{B_{n-r}}{B_n}.
\]

**2. Bell-ratio lemma.** For every fixed positive integer \(s\),
\[
\frac{B_{n-s}}{B_n}\sim\left(\frac{\rho_n}{n}\right)^s.
\]
One way to verify the classical estimate is to apply Dobiński's formula \(B_n=e^{-1}\sum_{j\ge1}j^n/j!\). Under weights proportional to \(j^n/j!\), Stirling's formula gives a unique saddle at \(j\log j=n\), namely \(j=n/\rho_n\); the mass outside any fixed relative neighborhood of the saddle is exponentially smaller. Therefore for fixed \(s\) the weighted average of \(j^{-s}\), which equals \(B_{n-s}/B_n\), is asymptotic to \((\rho_n/n)^s\). The fixed-order moment condition is essential; this proof makes no claim for growing \(s\).

**3. Candidate-set intensities.** Fix \(r\ge2\) and \(0\le a<b<\infty\). Let \(\mathcal A^{\mathrm L}_{n,r}(a,b]\) be the family of \(r\)-subsets \(S\) with \(\rho_n^r\min S/n\in(a,b]\). Then
\[
|\mathcal A^{\mathrm L}_{n,r}(a,b]|
=\sum_{a n/\rho_n^r<i\le b n/\rho_n^r}\binom{n-i}{r-1}
\sim\frac{b-a}{(r-1)!}\left(\frac n{\rho_n}\right)^r.
\]
Likewise, if \(\mathcal A^{\mathrm R}_{n,r}(a,b]\) contains the \(r\)-subsets with \(\rho_n(n-\min S)/n\in(a,b]\), write \(d=n-\min S\) to obtain
\[
|\mathcal A^{\mathrm R}_{n,r}(a,b]|
=\sum_{a n/\rho_n<d\le b n/\rho_n}\binom{d}{r-1}
\sim\frac{b^r-a^r}{r!}\left(\frac n{\rho_n}\right)^r.
\]
Combining these counts with the one-block probability from steps 1–2 yields the stated limiting left and right intensity measures.

**4. Joint factorial moments and independence.** Consider any finite set of disjoint test intervals in the left and right processes, with sizes in \(\{2,\ldots,K\}\), and any fixed nonnegative factorial-moment orders. Expand the joint falling-factorial product as a sum over ordered, **distinct** candidate blocks. Only pairwise disjoint candidate subsets contribute, and every such tuple of total cardinality \(s\) has exactly the factor \(B_{n-s}/B_n\). The proportion of candidate tuples that have an intersection is \(o(1)\): on the left, minima lie in ranges of length \(n/\rho_n^r\to\infty\) while any additional fixed number of labels are spread over \(n(1+o(1))\) possibilities; on the right, each candidate block lies in a terminal range of length \(O(n/\rho_n)\to\infty\); a left candidate meets any right candidate with probability \(O(1/\rho_n)\), apart from impossible boundary overlaps which vanish. These bounds also hold for different fixed sizes and for any fixed tuple length. Hence the joint factorial moments converge to products of the Poisson means computed in step 3. Multivariate factorial-moment determinacy of finite vectors of independent Poisson variables gives convergence of bounded-interval counts. Standard point-process convergence criteria then give joint vague convergence of all the processes.

**5. Extremes.** The absence of left points in \([0,t]\) has limiting probability \(e^{-t/(r-1)!}\), and the absence of right points in \([0,t]\) has limiting probability \(e^{-t^r/r!}\). Joint convergence gives independence of these limiting gaps. Sending \(t\to\infty\) shows that a size-\(r\) block exists with probability tending to one, so the convention on empty classes does not affect the limits.

## Verification
A standalone standard-library Python checker, `check.py`, enumerates every set partition through eight vertices, directly computes size-marked minimum counts, and independently checks the exact Bell-ratio expectation and two-count mixed/factorial-moment formulas by enumerating disjoint proposed blocks. It performs 520 exact checks, with rational arithmetic throughout. These finite checks do **not** prove point-process convergence; the infinite proof uses steps 2–5.

## Relationship to prior work
Sun and Wu's 2010 work studies largest singleton labels and exact Bell-number identities, but its reported results do not give the joint fixed-size, two-endpoint Poisson limits for sizes at least two. Arratia and Tavaré's independent-process approach treats component-size counts in set partitions, not the positions of their smallest labels; the latter spatial information and the two different boundary scalings require a separate overlap/factorial-moment calculation. A separately published singleton endpoint law supplies the \(r=1\) counterpart and is **not** claimed anew here. The contribution is confined to the fixed \(r\ge2\) multitype two-endpoint law and its paired extreme-value limits.

## Limitations
Only fixed block sizes are covered. The result gives weak and vague convergence, not rates, moment convergence of the rescaled extreme gaps, or independence at finite \(n\). General assembly component-count approximations could suggest these spatial limits, and a fuller historical survey may identify an earlier equivalent formulation; absolute priority is not certified. The computer checks certify only exact identities at the enumerated finite sizes.

## References
- Y. Sun and X. Wu, *The largest singletons of set partitions*, arXiv:1007.1341 (first posted 2010-07-08), https://arxiv.org/abs/1007.1341.
- R. Arratia and S. Tavaré, *Independent process approximations for random combinatorial structures*, Advances in Mathematics **104** (1994), 90–154; accessible manuscript https://arxiv.org/abs/1308.3279, Sections 5.3, 6 and 10.1. The arXiv posting in 2013 is not its first publication.
- S. DeSalvo and G. Menz, *A robust quantitative local central limit theorem with applications to enumerative combinatorics and random combinatorial structures*, arXiv:1610.07664 (first posted 2016-10-24), https://arxiv.org/abs/1610.07664.
- *Independent endpoint Poisson laws and the sharp singleton gap scale in uniform set partitions*, published research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-independent-endpoint-poisson-laws-and-the-sharp-singleton-gap-sc--2fce199f94b2 (singleton-only predecessor).
