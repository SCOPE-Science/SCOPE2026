# Conditional Poisson law for leaf neighbors in deep peeling layers of random recursive trees

## Finding

In a uniform random recursive tree, the number of original leaf children of a vertex conditioned to survive a fixed number of simultaneous leaf-peeling rounds has an explicit Poisson-mixture limit. As the number of rounds increases, **this conditional mixture approaches unit Poisson in total variation**, despite the unconditional prevalence of leaf neighbors being different.

For every fixed integer \(h\ge2\), the conditional empirical distribution \(Q_{n,h}\) of the number \(C_n(v)\) of children that are original leaves, among vertices having leaf-peeling layer at least \(h\), converges almost surely in total variation to \(Q_h\). With \(s_0(t)=1\), recursively define
\[
s_h(t)=1-\exp\left(-\int_0^t s_{h-1}(u)\,du\right),\qquad a(t)=1-e^{-t},\qquad B_h=\int_0^\infty e^{-t}s_h(t)\,dt.
\]
Then \(B_h>0\) and, for every integer \(j\ge0\),
\[
Q_h\{j\}=\frac{1}{B_h j!}\int_0^\infty e^{-t}s_h(t)e^{-a(t)}a(t)^j\,dt.
\]
The entire family has a quantitative high-layer limit
\[
d_{\mathrm{TV}}(Q_h,\operatorname{Pois}(1))\le e^{-h/10}+\frac{1}{10}\left(\frac e5\right)^h,\qquad h\ge2.
\]
For a uniformly sampled vertex in layer at least \(h\), the probability of rank one (distance exactly one to an original leaf) consequently tends, in the two-stage limit \(n\to\infty\) then \(h\to\infty\), to \(1-e^{-1}\). This contrasts with the unconditioned rank-one probability \(e^{-1}\). For calibration at \(h=2\), the joint density of rank one and layer at least two is \(5/2+e^{-1}-e\), and the conditional rank-one probability is \((5/2+e^{-1}-e)/(3-e)\approx0.531019\).

## Assumptions and scope

For every integer \(n\ge2\), construct a uniform random recursive tree \(T_n\) on vertices labeled \(1,\ldots,n\), rooted at vertex \(1\), by independently choosing each parent of vertex \(k\ge2\) uniformly from \(1,\ldots,k-1\). Vertex degree means undirected degree; original leaves are degree-one vertices. The peeling layer \(L_n(v)\) is the number of successive simultaneous leaf-removal rounds survived before removal (original degree-one leaves have layer zero). For a nonroot vertex \(v\), \(C_n(v)\) counts its children in the recursive orientation whose original undirected degree is one. The root's possibly exceptional leaf status has negligible asymptotic effect.

For fixed \(h\ge2\), define \(N_{n,h}=\#\{v:L_n(v)\ge h\}\) and, whenever \(N_{n,h}>0\),
\[
Q_{n,h}\{j\}=\frac{\#\{v:L_n(v)\ge h,\ C_n(v)=j\}}{N_{n,h}},\qquad j\in\{0,1,2,\ldots\}.
\]
The theorem concerns fixed \(h\) followed by \(n\to\infty\), and only then the family \(h\to\infty\); no joint growth rate of \(h\) with \(n\) is asserted.

## Proof

**1. Fringe-tree reduction.** The standard random-recursive-tree fringe theorem identifies the limiting rooted fringe tree of a uniform vertex with a continuous-time Yule tree, every individual giving birth at rate one, stopped after an independent \(T\sim\operatorname{Exp}(1)\). Conditional on \(T=t\), the root's children's birth times form a unit-rate Poisson process on \([0,t]\), and their descendant processes are independent. For every fixed finite rooted fringe-tree property, its frequency converges to its probability in this limit.

For the almost-sure version, truncate to fringe subtrees of at most \(K\) nodes. Changing one independent parent choice changes the truncated-property indicator for at most a constant multiple of \(K\) ancestral vertices along the old and new parent paths; descendants of the moved vertex keep identical fringe shapes. Hence the total count of a fixed truncated fringe property has bounded differences \(O(K)\), and its frequency has summable exponential concentration by the bounded-differences inequality. The expectation converges by the fringe theorem, so the frequency converges almost surely. The limiting size law is \(\Pr(|\mathcal T|=k)=1/[k(k+1)]\), giving tail \(1/(K+1)\). Taking \(K\to\infty\) extends the almost-sure convergence to every fixed fringe-measurable property. This also works for countably many such properties simultaneously.

Except among vertices within distance at most \(h+1\) from the original root, \(L_n(v)\ge h\) holds exactly when the rooted fringe subtree of \(v\) has height at least \(h\): the ancestor path acts as an exterior support through the first \(h\) peeling rounds. For each fixed depth the expected number of its vertices is bounded by a fixed power of \(\log n\); applying Markov along dyadic \(n\) and monotonic interpolation shows the fraction at depth at most \(h+1\) tends to zero almost surely. Therefore the empirical joint frequencies of peeling-layer survival and leaf-child counts equal their fringe-tree limits almost surely.

**2. Independent Poisson categories.** In the Yule fringe tree conditional on \(T=t\), a root child born at time \(u\) is still a leaf at time \(t\) exactly when it has no births in its remaining time, an event of probability \(e^{-(t-u)}\). Thus original leaf children form a Poisson category of mean
\[
\int_0^t e^{-(t-u)}\,du=1-e^{-t}=a(t).
\]
Write \(H\) for fringe height, with leaves having height zero. The event \(H\ge h\) occurs exactly when some child branch has height at least \(h-1\). If \(h\ge2\), such a child is not an original leaf. Independent thinning of the Poisson process of children therefore makes \(C\sim\operatorname{Pois}(a(t))\) independent of \(\{H\ge h\}\), conditional on \(T=t\). If \(s_h(t)=\Pr(H\ge h\mid T=t)\), branch independence gives the stated recursive integral formula. Integrating over the exponential density of \(T\) proves \(Q_h\{j\}\) and the fixed-layer empirical convergence. Pointwise convergence for all \(j\) plus the fact that \(\sum_jQ_h\{j\}=1\) implies total-variation convergence of the empirical mass functions.

**3. High-layer bound.** A Yule population at age \(t\) has expected generation-\(h\) size \(t^h/h!\), so \(s_h(t)\le t^h/h!\). Conversely, following the earliest-born child in every generation produces a lineage whose first \(h\) waiting times are independent unit exponentials. If \(G_h\sim\operatorname{Gamma}(h,1)\), independent of \(T\),
\[
B_h\ge\Pr(T\ge G_h)=\mathbb E e^{-G_h}=2^{-h}.
\]
For any \(0<\alpha<1\),
\[
\Pr(T<\alpha h\mid H\ge h)
\le 2^h\int_0^{\alpha h}\frac{t^h}{h!}\,dt
\le\alpha(2e\alpha)^h,
\]
where the last inequality uses \(h!\ge(h/e)^h\). Coupling \(\operatorname{Pois}(a(t))\) with \(\operatorname{Pois}(1)\) by adding an independent Poisson variable of mean \(e^{-t}\) yields \(d_{\mathrm{TV}}\le e^{-t}\). Splitting the conditional age mixture at \(\alpha h\) therefore gives
\[
d_{\mathrm{TV}}(Q_h,\operatorname{Pois}(1))\le e^{-\alpha h}+\alpha(2e\alpha)^h.
\]
Choosing \(\alpha=1/10\) proves the advertised explicit inequality and strong convergence.

**4. Rank interpretation and calibration.** For any nonroot vertex, rank one is the existence of an original undirected leaf neighbor. Such a neighbor is a leaf child, except when it is the original root, which is an exceptional vertex only for a degenerate initial root edge; the fraction of exceptional vertices vanishes. Hence, among deep-layer vertices, rank one is exactly \(\{C\ge1\}\) asymptotically. Under unit Poisson, this has probability \(1-e^{-1}\). The calibration \(B_2=3-e\) and the stated joint rank-one mass follow by integrating the same conditional Poisson construction; independently, they agree with the difference of two known one-dimensional margins.

## Verification

Run \(`python3 verify_joint_rank_layer.py`\) from the directory containing the standalone script. Python standard library suffices. It enumerates every parent-choice history up to eight vertices, verifies the peeling/fringe correspondence outside the fixed-root exception, integrates the recursion by a trapezoid rule, tests the exact \(B_2\) and joint-rank-one calibrations, and compares with a reproducible random recursive tree of 90,000 vertices. On the supplied code, all 53,374 finite assertions passed. For \(h=2,4,12\), computed limiting conditional rank-one frequencies are approximately \(0.531019,0.589572,0.630298\). These finite checks test calculations and modeling conventions; the proof of the infinite and almost-sure claims is analytic.

## Relationship to prior work

Stepanyants, Krapivsky, Hartle and Krioukov (2026) derive the separate rank and leaf-peeling-layer distributions for random recursive trees, including the layer recursion used here. They do not supply this full conditional distribution of leaf-child counts given layer survival, or its high-layer unit-Poisson limit in the material examined. Devroye and Janson (2014) establish the Yule fringe limit and separately analyze protected nodes and Poisson leaf-child processes. The independent-Poisson-category argument for **joint** high peeling layers and leaf neighbors, plus the explicit conditional total-variation bound, is the new result here. Previously established Yule embedding, fringe convergence and one-dimensional formulas are expressly credited, not claimed as new.

## Limitations

The limits are sequential, with fixed peeling depth while tree size tends to infinity; uniformity for peeling depths increasing with tree size is not proved. The convergence of the empirical conditional law is almost sure, but no rate in tree size is claimed. This result does not give a new limit for the separate marginal layer or rank distributions. The historical-priority assessment is based on inspected related results and searches, not a proof that no unpublished or unindexed equivalent theorem exists. There has been no independent mathematical audit.

## References

1. H. Stepanyants, P. L. Krapivsky, H. Hartle and D. Krioukov, *The rank and layer distributions in random recursive trees*, arXiv:2608.04303 (first public version 2026-08-05), https://arxiv.org/abs/2608.04303 .
2. L. Devroye and S. Janson, *Protected nodes and fringe subtrees in some random trees*, arXiv:1310.0665 (first public 2013-10-02), https://arxiv.org/abs/1310.0665 .
3. D. Aldous, *The continuum random tree II: an overview*, in Stochastic Analysis, Durham (1991), on fringe subtree methodology. [General background, not required as a standalone quantitative lemma.]
