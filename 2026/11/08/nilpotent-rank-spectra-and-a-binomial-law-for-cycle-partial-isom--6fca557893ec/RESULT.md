# Nilpotent rank spectra and a binomial law for cycle partial isometries

## Finding

For every integer \(n\ge3\), let \(\mathcal D_n\) be the monoid of partial isometries for geodesic distance on the cycle \(C_n\). Include the empty map among nilpotents, and write \(F_n\) for a uniformly sampled **distinct** nilpotent element. The rank \(\rho(F_n)\) is the size of its domain. As \(n\to\infty\),
\[
\left\|\mathcal L(\rho(F_n))-\operatorname{Bin}(n,1/2)\right\|_{\mathrm{TV}}
=O\!\left(\frac{(\log n)^3}{n^{3/2}}\right).
\]
In particular, \((\rho(F_n)-n/2)/(\sqrt n/2)\) converges in distribution to the standard normal. The density of nilpotent elements tends to \(1/2\); the proof also gives a density error bound of \(O((\log n)^2/n)\). The sharper bound for ranks uses smoothing rather than treating all rejected restrictions as an equally large bias in rank.

## Assumptions and scope

A partial isometry is an injection on a subset of the vertices that preserves distances between all pairs in its domain. Composition is ordinary partial-map composition. A map is nilpotent if some positive power is empty, equivalently if its functional digraph has no directed cycle. Total variation on the integers is half the \(\ell^1\) distance between the mass functions. The asserted bound is uniform in the cycle length, with no arithmetic restriction on \(n\). No optimality of the bound is claimed.

## Proof

**Dihedral presentations.** Every partial isometry is a restriction of a rotation or reflection, by Fernandes and Paulista, Lemma 1.1, for \(n\ge4\); for \(n=3\) the metric has all nonzero distances equal, and every partial injection extends to an element of \(S_3\). The restriction is nilpotent exactly when its domain contains no whole orbit of the ambient permutation. Let \(\sigma\) be a uniform rotation and \(E\) an independent uniform subset. If the order of \(\sigma\) is \(d\mid n\), its orbits have length \(d\), and the nilpotence acceptance probability is \(a_d=(1-p_d)^{m_d}\), with \(p_d=2^{-d}\) and \(m_d=n/d\). There are \(\varphi(d)\) rotations of that order. Conditional on order \(d\) and acceptance, the rank is distributed as a sum of \(m_d\) independent copies of a \(\operatorname{Bin}(d,1/2)\) variable conditioned to be strictly less than \(d\). Let \(\mu_d\) denote that law and let \(\beta_n=\operatorname{Bin}(n,1/2)\) denote the unconditioned rank law.

**Acceptance and density.** Put \(L=\lceil 3\log_2 n\rceil\). Rotations of order \(d\le L\) have relative frequency at most \(n^{-1}\sum_{d\le L}d=O((\log n)^2/n)\). For the other rotations \(1-a_d\le m_dp_d\le n2^{-L}\le n^{-2}\). Thus the acceptance probability \(A=\sum_{d\mid n}\varphi(d)a_d/n\) is \(1-O((\log n)^2/n)\). A nonempty rotation restriction determines the rotation from any one of its arrows, so in passing from \(n2^n A\) accepted rotation presentations to distinct maps only the \(n\) presentations of the empty map coalesce. A reflection has at most \(n/2\) transposed pairs and at most \(3^{n/2}\) nilpotent restrictions (choose neither or one vertex from each pair, and no fixed points). Thus the union with accepted reflection restrictions adds no more than \(n3^{n/2}\) maps. The known monoid size is \(2n2^n-O(n^2)\) (Fernandes and Paulista, Section 1, and directly also for \(n=3\)), giving the density estimate.

**Smoothing at short orders.** Fix \(2\le d\le L\) with \(d\mid n\); put \(m=m_d\) and \(p=p_d\). Compare the rank laws before and after conditioning the \(m\) independent orbit counts, changing one block at a time. In each step let \(W\) be the sum of the other \(m-1\) counts, each of which is either unconditioned or conditioned not to be full. Write \(X\) for an independent conditioned count in the block being changed. The unconditioned count in that block has the mixture law \((1-p)\mathcal L(X)+p\delta_d\), so the step costs at most
\[
p\,\mathbb E_X\left[\|\mathcal L(W+X\mid X)-\mathcal L(W+d)\|_{\mathrm{TV}}\right].
\]

In each of the other \(m-1\) blocks expose just the first inclusion bit. Independently for each block the probability of seeing a zero is at least \(1/2\), including for a conditioned block (where it equals \(1/[2(1-p)]\)). Conditional on a first bit equal to zero, the other \(d-1\) bits are independent fair bits even in a conditioned block. Let \(J\) be the number of exposed zeros. Then \(\mathbb E J\ge(m-1)/2\), \(\operatorname{Var}J\le(m-1)/4\), and Chebyshev's inequality gives \(\Pr(J<(m-1)/4)\le 4/(m-1)\). On the complementary event, conditional on the exposed bits and on all counts in the blocks whose first bit is one, \(W\) is a translate of a binomial law with \((d-1)J\) fair bits. This number is at least \(n/16\) for all sufficiently large \(n\), since \(d\ge2\), \(d\le L\), and \(md=n\).

The total variation of a binomial mass function from its translate by one is its maximum mass, by unimodality; for \(M\) fair bits this is \(O(M^{-1/2})\) by the central binomial coefficient bound. A shift of at most \(d\) therefore costs \(O(d/\sqrt n)\) on the event just described. The exceptional probability \(4/(m-1)\) is \(O(d/n)\), which fits the same bound. It follows, by convexity of total variation and telescoping the \(m\) changes, that
\[
\|\mu_d-\beta_n\|_{\mathrm{TV}}\le C\,mpd/\sqrt n.
\]
When forming the accepted rotation mixture, this bound is multiplied by \(a_d\le e^{-mp}\). Since \(v e^{-v}\) is bounded for \(v\ge0\), the resulting bound on \(a_d\|\mu_d-\beta_n\|_{\mathrm{TV}}\) is \(O(d/\sqrt n)\), uniformly over these short orders.

**Combining orders and passing to maps.** At \(d=1\) the only accepted domain is the empty set, so the contribution before normalization is at most \(2^{-n}/n\). For \(d>L\), conditioning on an event of probability \(a_d\) changes the rank law by at most \(1-a_d\le n^{-2}\), which also bounds the total contribution of these orders before normalization. For the remaining orders the mixture weights are \(\varphi(d)a_d/(nA)\). The preceding estimate, \(\varphi(d)\le d\), and \(A\to1\) give an error of at most a constant times
\[
\frac{1}{n^{3/2}}\sum_{d\le L}d^2=O((\log n)^3/n^{3/2}).
\]
Identifying the empty map and adding the reflection-only maps changes the rank distribution by \(O(2^{-n}+(\sqrt3/2)^n)\), using the counts above. The binomial central limit theorem transfers through the resulting total-variation bound.

## Verification and limitations

The bound follows from the proof, not from checking finite histograms. The companion finite enumeration `verify.py` counts distinct restrictions and checks the known exact rank polynomial and monoid size for \(3\le n\le11\); it does not test the order of the asymptotic error. The argument does not give a lower bound on the approximation error or a typical nilpotency index.

## Relationship to prior work

Fernandes and Paulista, *On the monoid of partial isometries of a cycle graph*, Turkish Journal of Mathematics **47** (2023), 1746–1760, [arXiv:2205.02196](https://arxiv.org/abs/2205.02196), Lemma 1.1 and Section 1, establish the restriction theorem and monoid size. The result *Rank and nilpotency-index enumerators for partial isometries of finite cycles* ([Resultary, 2026-10-12](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-rank-and-nilpotency-index-enumerators-for-partial-isometries-of--32e0cfa664d8), Finding and Proof §6) already gives the exact all-nilpotent rank polynomial for \(n\ge4\) as a specialization of its joint rank and index theorem. That polynomial is not claimed here as a new result. Its orbit factors give the exact finite law, but the uniform rank-error estimate above uses the conditional distribution within each orbit, smoothing across the other orbits and retention of the acceptance weights. Dimitrova, Fernandes, Koppitz and Quinteiro, [arXiv:2301.01519](https://arxiv.org/abs/2301.01519), study cardinalities and structure of oriented and order-preserving submonoids. The comparisons do not establish exhaustive literature priority for the quantitative estimate.
