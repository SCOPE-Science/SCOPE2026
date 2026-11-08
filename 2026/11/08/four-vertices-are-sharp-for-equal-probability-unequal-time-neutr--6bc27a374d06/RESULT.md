# Four vertices are sharp for equal-probability unequal-time neutral mutant configurations

## Finding

For standard neutral birth–death Moran updates on connected, undirected, simple unweighted graphs, configurations with the same mutant count and the same fixation probability need not have the same expected successful fixation time. This separation is **impossible at orders at most three and first appears at order four**. Among six unlabeled connected four-vertex graph classes, precisely the path \(P_4\) and the cycle \(C_4\) exhibit it, or 15 of 38 labeled connected four-vertex graphs.

In the path with edges \(01,12,23\), the initial mutant sets \(S=\{0,1\}\) and \(S'=\{0,2\}\) both have fixation probability \(1/2\), but the conditional expected fixation times are \(20\) and \(15\) updates respectively. For the four-cycle with edges \(01,12,23,30\), the adjacent mutant pair \(\{0,1\}\) and opposite pair \(\{0,2\}\) both have fixation probability \(1/2\), but conditional fixation times \(8\) and \(7\).

## Assumptions and scope

Let \(G=(V,E)\) be a connected simple undirected unweighted graph with \(2\le |V|\le4\). Every vertex hosts either a resident or a mutant. At each discrete-time update choose the reproducing vertex uniformly from \(V\); its offspring replaces a uniformly selected neighbor's occupant. Fitness is identically one for both types. Changes and no-change events each consume one step. From a nonempty proper mutant set \(S\), write \(p_G(S)=\Pr_S(F)\) for eventual all-mutant fixation, \(T\) for first absorption time at all-mutant or all-resident consensus, and \(\tau_G(S)=\mathbb E_S[T\mid F]\). All conditional times are finite since a finite connected graph absorbs almost surely and \(p_G(S)>0\).

The comparison requires *both* equal initial mutant counts and equal probabilities \(p_G(S)=p_G(S')\); it makes no assertion for selected mutants with different relative fitness, directed/weighted networks, or different update rules.

## Proof

**Fixation probability and the key equal-probability test.** Let \(d_v\) denote a vertex degree and let \(W(S)=\sum_{v\in S}1/d_v\). For an edge \(uv\) with unlike endpoint types, a mutant reproducing at \(u\) and replacing \(v\) changes \(W\) by \(+1/d_v\) with probability \(1/(|V|d_u)\), while the reverse replacement changes \(W\) by \(-1/d_u\) with probability \(1/(|V|d_v)\). Thus the two contributions cancel in conditional expectation and \(W(S_t)\) is a bounded martingale. Almost-sure absorption and optional stopping imply

\[p_G(S)=\frac{\sum_{v\in S}1/d_v}{\sum_{v\in V}1/d_v}.\]

For \(|V|=2\), there is only one connected graph and one orbit of configurations of either proper size. For \(|V|=3\), the only connected graph classes are the triangle and the path. On the triangle every same-cardinality configuration is automorphic; on the path the two end vertices have equal degree and are exchanged by reflection while the center has a distinct reciprocal degree. The same is true for their size-two complements. Hence same-cardinality equal-probability sets are automorphic, giving equal full hitting-time distributions and equal conditional mean times.

**Exact four-vertex classification.** The six connected unweighted four-vertex classes are the complete graph, the diamond (complete minus one edge), the triangle with a pendant leaf, the star, the path, and the cycle. Enumerate all \(2^6=64\) labeled edge sets, filter for connectivity, and identify classes using all \(4!\) vertex permutations. This gives exactly 38 connected labeled graphs and six unlabeled classes. On each graph, enumerate all \(2^4-2=14\) nontrivial configurations and group by pair \((|S|,p_G(S))\). The attached exact-arithmetic checker computes every conditional mean by solving the absorbing first-step equations below. The classes with a nonzero within-group time range are precisely \(P_4\) and \(C_4\). All 12 labeled copies of \(P_4\) and three labeled copies of \(C_4\) qualify; the other 23 labeled connected graphs do not.

**First-step conditional moments.** Index the transient mutant configurations by \(S\) and let \(Q_{S,R}\) be their one-step transition probabilities, including diagonal self-transitions. Set \(m(S)=\mathbb E_S[T\mathbf1_F]\). The fixation-probability harmonic equations and first-step decomposition give

\[(I-Q)m=p,\qquad \tau_G(S)=m(S)/p_G(S).\]

The finite matrix \(I-Q\) is invertible because absorption is certain. All entries are rational. The checker constructs \(I-Q\) directly from the unlike-edge replacement rates, validates that the inverse-degree martingale formula solves the fixation equations, and solves the full \((I-Q)m=p\) system by fraction-exact Gaussian elimination. For each of the two exceptional isomorphism classes it separately verifies the conditional Doob-transform recurrence \((I-Q^h)\tau=\mathbf1\), where \(Q^h_{S,R}=Q_{S,R}p(R)/p(S)\).

For the specified four-vertex path, the exact outputs are \(p(\{0,1\})=p(\{0,2\})=1/2\), \(\tau(\{0,1\})=20\), and \(\tau(\{0,2\})=15\). For the specified cycle, the same probabilities are \(1/2\), with times \(8\) and \(7\). These inequalities establish existence and complete the sharpness assertion.

## Verification

Run `python3 verify_moran_multiseed.py` with Python 3 and no external packages. The embedded program enumerates all connected labeled graphs of orders two, three and four, and reports connected labeled counts \(1,4,38\), unlabeled classes \(1,2,6\), and labeled qualifying counts \(0,0,15\). It verifies the candidate witness times and separately solves the conditional Doob recurrence with exact rational numbers, without sampling or floating-point thresholds. No extrapolation beyond four vertices is claimed.

## Relationship to prior work

Maciejewski (2013) supplies the neutral graph-reproductive-value background; Hindersin and Traulsen (2014) investigate fixation-time contrasts for single-mutant initial conditions; Hindersin and colleagues (2015) provide generic small-state exact-calculation methodology. The present claim concerns *two-initial-mutant configurations on the same network with the same fixation probability* and gives a minimal network size and complete four-vertex graph census. Baxter, Blythe and McKane (2008), and Iwamasa and Masuda (2014), study general fixation/consensus-time methods and network dependence. These general approaches motivate but, in the specific material inspected, do not state the sharp classification reported here.

## Limitations

This is a finite unweighted, undirected, neutral-fitness, discrete-time result. It is not a claim about fixation probability alone, one-mutant starting sites, non-neutral selection, or graph orders beyond four. Since exact formulas for voter and invasion models can imply related special cases, historical-priority uncertainty remains, particularly for older studies of multi-seed consensus times. Independent mathematical auditing and literature-priority assessment have not been performed.

## References

- W. Maciejewski, *Reproductive Value in Graph-structured Populations*, arXiv:1307.4789v1 (first public 2013-07-17), https://arxiv.org/abs/1307.4789.
- L. Hindersin and A. Traulsen, *Counterintuitive properties of the fixation time in network-structured populations*, arXiv:1406.4415v1 (2014), https://arxiv.org/abs/1406.4415.
- L. Hindersin et al., *Exact numerical calculation of fixation probability and time on graphs*, arXiv:1511.02696v1 (2015), https://arxiv.org/abs/1511.02696.
- G. J. Baxter, R. A. Blythe, A. J. McKane, *Fixation and Consensus Times on a Network: A Unified Approach*, Phys. Rev. Lett. 101, 258701 (2008), https://doi.org/10.1103/PhysRevLett.101.258701.
- Y. Iwamasa and N. Masuda, *Networks maximizing the consensus time of voter models*, Phys. Rev. E 90, 012816 (2014), https://doi.org/10.1103/PhysRevE.90.012816.
