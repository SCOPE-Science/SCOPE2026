# Convex-order optimal spacing of alternating fixed opinions on a finite voter cycle

## Finding
Let a cycle have \(n\ge 4\) vertices and \(m=2r\ge2\) permanently fixed-opinion vertices, with \(m\le n\). The fixed opinions alternate \(1,0,1,0,\ldots\) in circular order; the positive integer edge gaps \(g_1,\ldots,g_m\) between consecutive fixed vertices satisfy \(\sum_{i=1}^m g_i=n\). Every other vertex copies a uniformly selected neighbor at rate one. Write \(X_g\) for the number of opinion-\(1\) vertices in the unique stationary distribution.

**Theorem.** For independent discrete uniforms \(U_{g_i}\) on \(\{0,\ldots,g_i-1\}\),
\[
 X_g\ \stackrel{d}=\ r+\sum_{i=1}^{m} U_{g_i},\quad
 \mathbb E X_g=\frac n2,\qquad
 \operatorname{Var}(X_g)=\frac1{12}\sum_{i=1}^m(g_i^2-1).
\]
For any two such gap vectors \(g,h\) with \(g\) majorizing \(h\), one has \(X_h\le_{\mathrm{cx}}X_g\): for **every** real convex function \(\varphi\) on \(\{0,\ldots,n\}\),
\[
 \mathbb E\varphi(X_h)\le\mathbb E\varphi(X_g).
\]
If the sorted gap vectors differ, the inequality is strict for **every strictly convex** \(\varphi\). In particular, if \(n=mq+s\), \(0\le s<m\), the unique multiset minimizing every strictly convex stationary count risk consists of \(m-s\) gaps \(q\) and \(s\) gaps \(q+1\). The unique multiset maximizing all such risks is \((n-m+1,1,\ldots,1)\). Here uniqueness concerns gap multisets, not physical placements, because permutations of the gaps have identical count distributions.

The exact probability-generating polynomial is
\[
 \mathbb E[z^{X_g}]=z^r\prod_{i=1}^m\frac{1+z+\cdots+z^{g_i-1}}{g_i}.
\]
Thus this ordering controls not only variance but every convex loss of the long-run opinion-count imbalance, at every finite size.

## Assumptions and scope
The cycle is simple and undirected, each unfixed vertex has an independent rate-one Poisson clock, and a clock ringing copies either of its two adjacent vertices with probability \(1/2\). Frozen vertices never update, including when adjacent. There is no mutation, exogenous noise, or long-range interaction. The number \(m\) of fixed vertices is even and their values alternate in circular order; gaps may equal one. Initially, unfixed opinions are arbitrary. The distribution and all inequalities are for the limiting stationary law of the finite process, not finite-time distributions. Convex order refers to convex real test functions of the full integer opinion count. If \(n=m\), the unique gap vector makes the extremal statements vacuous.

## Proof
**1. Recurrent domain-wall structure.** Each interval of \(g_i\) edges between opposite pinned values has \(g_i-1\) independently updating unfixed vertices. Its number of discordant edges is odd and nonincreasing: updating an interior vertex can move a wall or annihilate two adjacent walls, but cannot create walls in the nearest-neighbor voter model. From any configuration with at least three walls, there is a finite positive-probability sequence of updates eliminating an interior domain, and therefore eliminating two walls. Because the interval state space is finite, its only recurrent class consists of the \(g_i\) configurations with exactly one wall. Within that class the wall hops one edge left or right at rate \(1/2\), except that moves beyond the fixed endpoints are suppressed. The resulting finite symmetric birth–death chain has the uniform stationary law on its \(g_i\) wall positions, including \(g_i=1\), when the position is fixed. Distinct intervals share only non-updating endpoints, so their update clocks and stationary wall positions are independent.

**2. Opinion-count law.** Each alternating interval contributes a uniform count of \(1\)-opinions among its \(g_i-1\) unfixed sites: an orientation reversal merely reverses the list \(\{0,\ldots,g_i-1\}\). The pinned vertices contribute precisely \(r\) ones. Independence gives the distribution, generating polynomial, mean and variance stated above.

**3. One balancing transfer is a strict convex-order improvement.** Fix integers \(1\le a\le b-2\). Put \(T=U_a+U_b\) and \(T'=U_{a+1}+U_{b-1}\), and write \(s=a+b\). At each integer \(0\le k\le s-2\), set \(q_k=\min\{k+1,s-1-k\}\). The exact probabilities are
\[
 \Pr(T=k)=\frac{\min\{q_k,a\}}{ab},\qquad
 \Pr(T'=k)=\frac{\min\{q_k,a+1\}}{(a+1)(b-1)}.
\]
Their signed difference \(\delta_k=\Pr(T=k)-\Pr(T'=k)\) is strictly positive on the two tails \(k\le a-1\) and \(k\ge b-1\), and strictly negative in the middle \(a\le k\le b-2\). Indeed, the second denominator exceeds the first by \(b-a-1>0\), while on the middle the probabilities equal \(1/b\) and \(1/(b-1)\), respectively. Both random variables have mean \((s-2)/2\), so \(\sum_k\delta_k=\sum_k k\delta_k=0\).

For any convex \(\varphi\), draw the affine secant \(\ell\) through \((a-1,\varphi(a-1))\) and \((b-1,\varphi(b-1))\). Convexity gives \(\varphi-\ell\ge0\) outside these endpoints and \(\varphi-\ell\le0\) between them. Consequently every summand of
\[
 \mathbb E\varphi(T)-\mathbb E\varphi(T')
 =\sum_{k=0}^{s-2}\delta_k\,[\varphi(k)-\ell(k)]
\]
is nonnegative. For strictly convex \(\varphi\), the term at \(k=a\) is strictly positive; hence \(T' <_{\mathrm{cx}} T\) in the strict-test-function sense. Convolution with any independent integer-valued variable preserves the inequality and strictness: for strictly convex \(\varphi\), \(k\mapsto\mathbb E\varphi(k+W)\) remains strictly convex.

**4. Majorization and extremizers.** A positive-integer vector can be transformed into any positive-integer vector it majorizes (up to coordinate permutations) by finitely many balancing steps \((a,b)\mapsto(a+1,b-1)\) with \(b-a\ge2\). Applying Step 3 to the independent uniform summands at each transfer proves the stated convex order, strictly if any transfer is nontrivial. Every positive-integer \(m\)-vector of sum \(n\) majorizes the balanced vector, and the concentrated vector majorizes every such vector. Hence the sharp simultaneous extrema and their unique multisets follow.

## Verification
The accompanying `checker.py` independently solves the exact full-state Markov generators on all rings of sizes \(4\) to \(7\) with two or four alternately fixed agents, and compares their stationary count laws against the uniform-wall convolution. It also performs exact-rational finite checks of elementary balancing transfers, all call-function inequalities for small compositions, and the variance identity. Run with `python3 checker.py` using Python 3 and SymPy. The verified run returned `PASS 39942 exact assertions`.

For \(n=12\), \(m=4\), balanced gaps \((3,3,3,3)\) give \(\mathbb E X=6\), \(\operatorname{Var}(X)=8/3\); maximally concentrated gaps \((9,1,1,1)\) give the same mean but variance \(20/3\). The exhaustive finite tests corroborate, but do not replace, Steps 1–4, which quantify over every eligible finite cycle and convex payoff.

## Relationship to prior work
Mobilia, Petersen and Redner (2007), Sections 4.1–4.2, **already establish** the independent uniformly wandering domain walls between oppositely pinned neighbors, study alternating zealots, and derive approximate continuous and large-segment magnetization laws. This theorem does not claim originality for that mechanism. It gives an exact finite-cycle law as an intermediate step and, importantly, proves the further all-convex-payoff, all-integer-spacing optimization and strict-majorization theorem. Yildiz and collaborators (2011 manuscript; 2013 publication) develop exact stationary mean and variance via coalescing random walks on general graphs and optimize mean bias of stubborn-agent placements. In their manuscript conclusion, they explicitly reserve minimizing stationary variance under placement for future work. The exact strict convex-order optimality and simultaneous extremizers here are more specific than general variance formulas or qualitative claims about distributed zealots. Searches of semantically indexed related mathematical findings and targeted original-literature comparisons found no statement implying this strict convex-order result; that absence alone is not proof of priority.

## Limitations
Alternation is essential: if successive fixed vertices have the same opinion, their connecting interval freezes and the independent-uniform formula no longer applies without adjustment. The theorem concerns the opinion count, not arbitrary functions of the full spatial configuration or mixing time. It does not establish which arrangements are optimal on general graphs, directed networks, or with heterogeneous update rates. The historical-priority assessment is bounded by the inspected full texts and searches; further work could identify a previously published convex-order or majorization formulation.

## References
1. M. Mobilia, A. Petersen, S. Redner, *On the Role of Zealotry in the Voter Model*, Journal of Statistical Mechanics (2007), P08029, DOI: https://doi.org/10.1088/1742-5468/2007/08/P08029 ; first public preprint https://arxiv.org/abs/0706.2892 (20 June 2007); author-hosted full text https://faculty.ucmerced.edu/apetersen3/MyPapers/Zealot.pdf . Relevant Sections 4.1–4.2, especially pages 9–12.
2. E. Yildiz, A. Ozdaglar, D. Acemoglu, A. Saberi, A. Scaglione, *Discrete Opinion Dynamics with Stubborn Agents* (submitted 2011, later published as *Binary Opinion Dynamics with Stubborn Agents*), full manuscript https://paperzz.com/doc/8168395/discrete-opinion-dynamics-with-stubborn-agents ; published DOI https://doi.org/10.1145/2538508 . Relevant stationary-moment analysis and Section 7 conclusion.
