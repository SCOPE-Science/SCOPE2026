# A single homophilic rewiring gives an unbounded cascade on bounded-degree trees

## Finding

For every integer \(m\geq 1\) and every common strict fractional adoption threshold \(\theta\in[1/4,1/3)\), there is a connected tree \(T_m\) of order \(m+6\), maximum degree four, and exactly two initially adopting seeds with the following properties. Without intervention, irreversible threshold adoption stops with exactly three adopters. Under a single homophilic rewiring selected uniformly among the three initially adopter–nonadopter edges, with the nonadopting endpoint reconnecting uniformly to a different nonadjacent nonadopter, and *then* ordinary threshold closure on the changed graph, the final number of adopters \(Z_m\) has the complete exact distribution
\[
\Pr(Z_m=m+6)=\frac23,\qquad
\Pr(Z_m=3)=\frac13,\qquad
\mathbb E Z_m=5+\frac{2m}{3}.
\]
In particular, a *single* permissible rewiring has an unbounded multiplicative effect on completion size as \(m\to\infty\), even with a fixed threshold, two seeds, an initially connected network, and bounded initial degree. The baseline-to-mean ratio is \((5+2m/3)/3\), and the favorable-outcome ratio is \((m+6)/3\). This is a one-shot adaptation result; the exact probabilities are **not** asserted for a process with continued rewiring during subsequent adoption updates.

## Assumptions and scope

All graphs are finite, undirected, unweighted, and simple. Each vertex is permanently in one of two states, adopted or not adopted. The adoption closure on a *fixed* graph repeatedly changes any nonadopter with more than a fraction \(\theta\) of already adopting neighbors to an adopter. Ties at exactly \(\theta\) do not trigger adoption. A finite monotone closure is independent of the order of enabled changes, provided enabled vertices are eventually updated.

The vertex set is \(\{a,b,u,v,x,y,w_1,\dots,w_m\}\). The original edges are
\[
\{au,bu,bv,vx,vy,vw_1\}\ \cup\ \{w_iw_{i+1}:1\le i<m\}.
\]
Initially \(a\) and \(b\) alone are adopters. This graph is a connected tree with \(m+5\) edges; \(v\) has degree four, \(b,u\) have degree two, the internal path vertices have degree two, and the other vertices have degree one.

The *one-shot homophilic rewiring* samples one of the currently adopter–nonadopter edges uniformly, removes it, and reconnects its nonadopting endpoint to a uniformly chosen nonadopter to which it is not already adjacent, excluding itself. Exactly one link is replaced; no adoption precedes this move and no further rewiring occurs. Subsequently run strict fractional-threshold closure to completion on the new graph. Every sampled rewiring is legal in this family. These assumptions isolate one elementary operation of the homophilic coevolution mechanism described by Min and San Miguel, rather than claiming equivalence to their entire evolving stochastic protocol.

## Proof

1. **Static closure.** Initially the three adopter–nonadopter edges are \(au,bu,bv\). Vertex \(u\) has two adopter neighbors and therefore adopts. Vertex \(v\) has precisely one adopter neighbor \(b\) among four, so its exposure is \(1/4\le\theta\). All of \(x,y,w_1,\ldots,w_m\) have no adopter neighbor. Hence static closure contains exactly \(\{a,b,u\}\).

2. **Rewire an edge incident to \(u\).** Suppose the sampled edge is \(au\) or \(bu\). The susceptible endpoint \(u\) remains adjacent to one seed and is reconnected to exactly one susceptible vertex. Its exposure becomes \(1/2>\theta\), so \(u\) adopts. The possible new neighbors are exactly \(v,x,y,w_1,\ldots,w_m\). Each then activates in the closure: for target \(v\), it has two adopting neighbors out of five (the seed \(b\) and \(u\)), giving exposure \(2/5>\theta\); for target \(x\) or \(y\), it has one adopter out of two, giving \(1/2>\theta\); for a path target \(w_i\) with \(i<m\), it has one adopter out of three, giving \(1/3>\theta\); and for target \(w_m\), it has one adopter out of two. If \(m=1\), this last case still has degree two after reconnecting to \(u\). Once any path vertex adopts, infection propagates in both path directions, since each originally degree-two path vertex needs only one adopting neighbor (exposure \(1/2>\theta\)). When \(w_1\) adopts, \(v\) has adopting neighbors \(b,w_1\), giving exposure \(1/2>\theta\). When either \(x\) or \(y\) adopts, the same conclusion for \(v\) follows. Once \(v\) adopts, every remaining path vertex and both pendant leaves adopt. Thus *every* permissible reconnection of \(u\) produces complete adoption of all \(m+6\) vertices.

3. **Rewire \(bv\).** This instead removes \(v\)'s sole adopter neighbor. The nonadopting endpoint \(v\) reconnects to either \(u\) or a path vertex \(w_i\) with \(i\ge2\), because its original other neighbors are \(x,y,w_1\). Vertex \(u\) still adopts: it has either two out of two seeded neighbors or, if chosen as the target, two out of three. If \(v\) attaches to \(u\), then after \(u\) adopts the exposure at \(v\) is just \(1/4\le\theta\); all other nonadopters have no adopter neighbors. If \(v\) attaches to a path vertex, \(v\) has no adopter neighbor and the entire path is still susceptible. No additional adoption can occur. The final set is exactly \(\{a,b,u\}\).

4. **Probability and expectation.** Two of the three initially adopter–nonadopter edges are incident to \(u\), each with uniform selection probability \(1/3\). Steps 2 and 3 show that the ultimate outcome depends *only* on which edge was selected, not on the reconnection target. Therefore the full-adoption probability is \(2/3\) and the three-adopter probability is \(1/3\). The expectation equals \((2/3)(m+6)+(1/3)3=5+2m/3\).

5. **A meaningful threshold boundary.** If \(\theta<1/4\), the original vertex \(v\) activates even without rewiring, so this family has no baseline gap. For \(m\ge2\), at \(\theta\ge1/3\) an interior path target (e.g. \(w_1\)) newly connected to \(u\) has exposure only \(1/3\) after \(u\) activates; the all-target success argument fails. Thus \([1/4,1/3)\) is the sharp common interval for the asserted original-blockade and all-target activation mechanism on the whole family \(m\ge2\). No claim of uniqueness among graphs is made.

## Verification

The standalone `verify.py` reconstructs the graphs directly, uses exact rational thresholds, enumerates all legal initial adopter–nonadopter edges and all legal susceptible reconnection targets, independently computes synchronous closure to stabilization, and checks both the full two-point distribution and the expectation. Run `python verify.py` using Python 3.9 or later; there are no external package requirements. The packaged tests cover \(1\le m\le20\) at \(\theta=1/4,3/10,333/1000\), including both endpoint and interior targets and the strict boundary \(\theta=1/4\). They test finite instances; the uniform all-size result comes from the preceding proof, not the finite tests.

## Relationship to prior work

Min and San Miguel (2023) introduce coevolving threshold contagion with homophilic rewiring from adopting–nonadopting links to nonadopting–nonadopting links. Their numerical and mean-field work reports suppression of the global-cascade region, alongside a nonmonotone cascade-size response. The present result is consistent with their acknowledged enhancement mechanism but supplies a different, precise finite claim: one rewiring before adoption, a fixed-threshold connected bounded-degree tree, exact \(2/3\) success probability, and unbounded increase of mean completion size. Their reported nonmonotone population averages do not imply this finite family or probability law.

Eckles, Mossel, Rahimian and Sen (2018) prove acceleration of threshold spreading by long ties primarily in noisy or fixed-absolute-threshold settings on cycle-derived networks. This is not a deterministic strict fractional-threshold, adopter–nonadopter-to-nonadopter–nonadopter adaptive move on a tree. Ebrahimi and coauthors (2014) study multi-seed absolute-threshold spreading on generative time-evolving preferential-attachment networks, not this one-shot finite rewiring rule. A related published threshold-diffusion graph invariant concerns static closures rather than a change of graph between exposure and closure; it does not give the probability or sensitivity here.

## Limitations

The exact probability \(2/3\) belongs only to the stated *one-shot* experiment, which is not the full stochastic coevolutionary dynamics. The result does not establish an average increase for arbitrary graphs, random initial networks, other thresholds, or repeated rewiring. Although the graph was connected before intervention, the rewiring may isolate the already adopting seed \(a\); no final connectivity is required. The outcome of a single favorable rewiring gives large cascade amplification; its actual occurrence probability under a different time-ordering or rate model requires separate analysis. Independent external validation and exhaustive literature priority certification have not been performed.

## References

1. B. Min and M. San Miguel, *Threshold cascade dynamics on coevolving networks*, arXiv:2305.13965 (first public version 2023-05-23), https://arxiv.org/abs/2305.13965 .
2. D. Eckles, E. Mossel, M. A. Rahimian and S. Sen, *Long ties accelerate noisy threshold-based contagions*, arXiv:1810.03579 (2018), https://arxiv.org/abs/1810.03579 .
3. R. Ebrahimi, J. Gao, G. Ghasemiesfeh and G. Schoenebeck, *How Complex Contagions Spread Quickly in the Preferential Attachment Model and Other Time-Evolving Networks*, arXiv:1404.2668 (2014), https://arxiv.org/abs/1404.2668 .
