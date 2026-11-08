# Two-round radiality and a sharp third-round branching defect in stochastic triadic closure

## Finding

Let \(\mathcal T_p\) be one *simultaneous stochastic triadic-closure round* on a finite simple graph: independently for each missing unordered vertex pair that has at least one common neighbor in the graph at the beginning of the round, add the edge with probability \(p\). Retain every existing edge. Use fresh independent coins in successive rounds. For an initial graph \(H\), write \(H_j=\mathcal T_p^j(H)\).

**Theorem (sharp two-round radiality and its failure at three).** Fix \(0<p<1\).

1. For any finite tree \(H\) and distinct vertices \(u,v\), the probability \(\Pr(uv\in E(H_2))\) depends only on their distance \(d=d_H(u,v)\). It equals
   \[
   w_d(p)=\begin{cases}
   1,&d=1,\\
   2p-p^2,&d=2,\\
   2p^2-p^3,&d=3,\\
   p^3,&d=4,\\
   0,&d\ge5.
   \end{cases}
   \]
   Hence, if \(N_d(H)\) counts unordered vertex pairs at distance \(d\),
   \[
   \mathbb E|E(H_2)|=N_1(H)+(2p-p^2)N_2(H)
   +(2p^2-p^3)N_3(H)+p^3N_4(H).
   \]
2. The same radiality fails after *three* rounds between two five-vertex trees. Let \(P\) be the path \(x-a-b-c-d\), and let \(B\) be the tree with path \(a-b-c-d\) and an extra leaf \(x\) joined to \(b\). The pair \(a,d\) has initial distance three in both graphs, but
   \[
   \Pr(ad\in E(\mathcal T_p^3(B)))
   -\Pr(ad\in E(\mathcal T_p^3(P)))
   =p^4(2-p)(1-p)^4>0.
   \]
   In the path \(P\) the probability is \(p^2(2-p)(p^2-3p+3)\). At \(p=1/2\), the strict difference is \(3/512\). Five vertices are the minimum possible size for a tree counterexample: all initial distances one and two remain radial at every round, and any tree with an initial distance-three pair on at most four vertices is the four-vertex path.
3. If \(H\) is instead a sparse Erdős–Rényi random graph \(G(n,c/n)\), where \(c>0\) is fixed, and \(G_2=\mathcal T_p^2(H)\), then
   \[
   \frac{2|E(G_2)|}{n}\xrightarrow{\mathbb P}
   c+(2p-p^2)c^2+(2p^2-p^3)c^3+p^3c^4.
   \]
   Thus the exact two-round radial kernel supplies an explicit macroscopic edge-density law for the natural locally tree-like random backbone.

## Assumptions and scope

All graphs are simple and undirected. A pair with several common neighbors is offered *one* Bernoulli\((p)\) coin per round, not one coin per wedge. All eligibility checks in a round use its input graph, so additions during that round cannot create new eligible pairs until the next round. Different eligible pairs and different rounds use independent coins. Parts 1 and 2 hold for every finite tree of the specified form, without bounded-degree assumptions. Part 3 holds for fixed \(c>0\) and fixed \(p\in(0,1)\), with random-graph and closure randomness both included. The exact finite-tree formula also extends continuously to \(p=0,1\), but the branching difference is strictly positive only for interior \(p\).

## Proof

**Distance kernel.** Every edge created in one round has endpoints at graph distance two in the previous graph. Therefore after two rounds an edge can only join vertices whose initial tree distance is at most four. Unique tree geodesics give the complete case classification.

At initial distance two, the original middle vertex remains a common neighbor forever. The pair receives independent coins in both rounds, giving \(1-(1-p)^2=2p-p^2\). At distance three, label the unique path \(a-b-c-d\). At the first round only the two length-two chords \(ac\) and \(bd\) can be relevant. At round two, \(ad\) is eligible if at least one of these independent Bernoulli\((p)\) chords appeared; the round-two coin then succeeds with probability \(p\). This yields \(p[1-(1-p)^2]=2p^2-p^3\). An off-path vertex cannot be a common neighbor of \(a,d\) in the first-round graph because its two distances to \(a,d\) cannot both be at most two. At distance four, label the path \(a-b-c-d-e\). The sole possible common neighbor in the first-round graph is \(c\), and the two necessary chords \(ac,ce\) are independently added at round one. The round-two closing coin then gives \(p^3\). Distances greater than four are impossible by the triangle inequality. Summing pair indicators gives the expectation identity.

**Exact third-round defect.** Couple the two trees by using identical closure coins for pairs in their common path whenever eligible, and independent additional coins for edges involving \(x\). The path chords \(ac\) and \(bd\) are eligible in each of the first two rounds whenever missing, in both trees. Write \(F\) for the event that neither is present after round two. Since each was offered two independent coins, \(\Pr(F)=(1-p)^4\). On \(F\), the pair \(ad\) is also absent after two rounds, and in either the four-vertex subpath or the five-vertex path with \(x\) attached at \(a\), it has no common neighbor at round three; outside \(F\), it has the same third-round eligibility in both coupled graphs. Indeed, the terminal \(x\) in the latter path cannot become adjacent to \(d\) by round two on \(F\): the only potential round-two witness requires \(bd\), which is absent on \(F\).

On \(F\), the extra vertex \(x\) makes \(a,d\) eligible at round three exactly when \(ax\) and \(xd\) are both present after round two. The first edge has probability \(2p-p^2\) because \(a-b-x\) is a length-two path. The second is present precisely when the first-round chord \(xc\) is added and the second-round coin for \(xd\) succeeds: the alternative witness through \(b\) is absent on \(F\). Their conditional probabilities are independent of each other and of \(F\), so
\[
\Pr(F,ax\in E(B_2),xd\in E(B_2))
=(1-p)^4(2p-p^2)p^2.
\]
Multiplying by the third-round edge coin \(p\) proves the exact difference \(p^4(2-p)(1-p)^4\). In the four-vertex subpath, and equally in the five-vertex path \(P\), the second-round probability for \(ad\) is \(p(2p-p^2)\). At round three the pair is eligible whenever either \(ac\) or \(bd\) survived two rounds; these two chords are independent with individual probability \(2p-p^2\). Hence the final path probability is
\[
(1-p)p(2p-p^2)+p[1-(1-p)^4]
=p^2(2-p)(p^2-3p+3).
\]
For the minimality claim, every initial edge remains present. A distance-two pair has its original middle neighbor available at every round, so after \(j\) rounds its connection probability is \(1-(1-p)^j\) in every tree. With at most four vertices, the only possible distance-three pair lies at the endpoints of \(P_4\); no longer distance exists. Thus five is the first possible tree order for failure.

**Sparse random graph corollary.** The well-known local limit of \(G(n,c/n)\) is the Poisson\((c)\) Galton–Watson tree. The fixed-round local-convergence theorem (Talukdar, Corollary 4.1) transfers this to two independent simultaneous closure rounds. The degree after two rounds is dominated by the number of original vertices within distance four. Its squared expectation is uniformly bounded for fixed \(c\), by the breadth-first-search domination with a fixed-depth binomial branching process. Therefore the empirical average degrees converge in probability by truncation and uniform integrability. The expected number of original tree vertices at depth \(d\) is \(c^d\). Apply the first part of the theorem to these vertices and sum \(w_d(p)c^d\) for \(d=1,2,3,4\), obtaining the displayed limit.

## Verification

Run `python3 check.py` with Python 3's standard library. The checker enumerates all labeled trees on two through five vertices via Prüfer codes, computes each two-round pair probability exactly at \(p=1/2\), and compares it with the claimed distance kernel. It performs 1,356 pair checks. Separately, exact integer-polynomial state propagation reconstructs the full two-round path probabilities and the third-round difference as an identity in \(p\), with no floating-point rounding; it also checks equality between the five-vertex path and its four-vertex subpath through round three. These finite checks corroborate the local calculations; the universal tree assertions and random-graph convergence are justified by the preceding proof.

## Relationship to prior work

Talukdar (2026) established local convergence for stochastic triadic closure, including arbitrary fixed repetitions, and applied it to clustering coefficients. Its Corollary 4.1 supplies the convergence mechanism used above, not the stated pairwise two-round kernel, the precise third-round branch defect, or the resulting explicit two-round density polynomial. Cirigliano–Castellano–Baxter–Timár (2023/2024) analyzed a single static closure round, including degree and small-motif counts. Cirigliano–Baxter–Timár (2026) developed the one-round degree correlations and clustering spectrum. The current calculation addresses the structural distinction between two and three *separate simultaneous closure rounds*, not an alternative formula for the single-round models.

## Limitations

The two-round formula is exact on trees; finite backbones with multiple short paths need not obey it. The convergence corollary requires fixed finite mean degree; it is not a uniform statement over diverging \(c\). The third-round identity compares two specific trees and does not classify third-round probabilities on all trees. No independent audit or definitive exhaustive priority determination is claimed.

## References

1. H. Talukdar, *Local Convergence of Triadic Closures of Sparse Random Graphs*, arXiv:2610.39535v1 (first posted 2026-10-29), especially the definition of \(\mathcal T_p\), Corollary 4.1, Section 7.1, and the discussion of repeated closure. https://arxiv.org/abs/2610.39535
2. L. Cirigliano, C. Castellano, G. J. Baxter, and G. Timár, *Strongly clustered random graphs via triadic closure: An exactly solvable model*, arXiv:2311.05312 (2023); Phys. Rev. E 109, 024306 (2024). https://arxiv.org/abs/2311.05312
3. L. Cirigliano, G. J. Baxter, and G. Timár, *Strongly Clustered Random Graphs via Triadic Closure: Degree Correlations and Clustering Spectrum*, Complexities 2(2), 13 (2026). https://doi.org/10.3390/complexities2020013
