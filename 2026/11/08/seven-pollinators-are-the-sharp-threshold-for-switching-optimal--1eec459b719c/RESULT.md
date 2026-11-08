# Seven pollinators are the sharp threshold for switching optimal interaction augmentation in a capacity-limited plant guild

## Finding

**Theorem.** Let a connected bipartite interaction network have precisely three permanently present plant species and \(n\ge3\) pollinator species. Each pollinator can service at most one plant during the modeled interval; every plant needs one distinct live pollinator. Independently, each pollinator survives with the same probability \(p\in(0,1)\). Assume every pollinator has at least one plant neighbor, the intact network can service all three plants, and at least one plant–pollinator interaction is absent. Choose exactly one absent interaction and maximize the probability that all three plants can simultaneously be serviced.

For \(3\le n\le6\), there is always one added interaction which is optimal **for every** \(p\in(0,1)\). For \(n=7\), this conclusion fails: precisely 24 connected, initially fully serviceable networks, when pollinators are unlabeled but plants retain their labels, have no universally optimal added interaction. Their optimal interaction changes once at \(p=1/2\) (nine networks) or \(p=2/3\) (fifteen networks). Up to permutation of the three plant labels, these 24 networks form five classes, represented by the sorted pollinator-neighborhood bitmasks

\[
(1,1,2,4,6,6,7),\ (1,1,2,5,6,6,6),\ (1,1,2,6,6,6,7),\ (1,1,3,6,6,6,6),\ (1,1,6,6,6,6,7).
\]

Bitmask \(1\), \(2\), or \(4\) denotes a pollinator serving only plant \(A\), \(B\), or \(C\); bitmask \(6\) denotes service to \(B,C\); and \(7\) denotes all three. The enumeration concerns a model of **simultaneously capacity-limited service**, not the more permissive event that each plant merely has at least one living pollinator.

In the first representative network, with seven pollinators indexed \(0,\ldots,6\), the baseline plant neighborhoods are \(A=\{0,1,6\}\), \(B=\{2,4,5,6\}\), and \(C=\{3,4,5,6\}\). Adding the formerly absent link from plant \(B\) to pollinator \(0\) improves full-service reliability by \(4p^3(1-p)^4\); adding that from plant \(A\) to pollinator \(2\) improves it by \(3p^3(1-p)^4+p^4(1-p)^3\). These are globally best among the allowed single links, respectively, when \(0<p<1/2\) and when \(1/2<p<1\). Their improvement difference is

\[
\Delta_{B0}(p)-\Delta_{A2}(p)=p^3(1-p)^3(1-2p).
\]

## Assumptions and scope

A *live pollinator set* \(S\) can service all three plants if the bipartite subgraph induced by the three plants and \(S\) has a matching covering every plant. The baseline graph is simple and connected; every pollinator's original neighborhood is a nonempty subset of \(\{A,B,C\}\). All three plants must be serviceable when all pollinators survive. The only permitted modification is addition of one originally absent incidence. The added incidence incurs equal unit cost regardless of which pair is selected. No pollinator capacities above one, recovery, temporal adaptation, nonuniform extinction probabilities, or dependence between pollinator failures are assumed.

Plants retain labels in the 24-network count, while pollinators with identical neighborhoods are exchangeable and unlabeled. The five-class count additionally identifies plant-label permutations. For \(n<3\), servicing all three plants with distinct pollinators is impossible; those sizes are excluded by feasibility.

## Proof

**Exact reliability coefficients.** Encode each pollinator neighborhood by one of the seven nonempty masks \(1,\ldots,7\). For a network \(G\), define \(C_k(G)\) as the number of \(k\)-element pollinator subsets whose surviving induced graph contains a plant-covering matching. Hall's marriage theorem gives the exact Boolean test: for every nonempty plant set \(T\subseteq\{A,B,C\}\), its neighboring pollinators in the selected live set must number at least \(|T|\). Independence gives the identity, for every \(0\le p\le1\),

\[
R_G(p)=\sum_{k=0}^{n} C_k(G)p^k(1-p)^{n-k}.
\]

For each initially absent link \(e\), set \(d_{e,k}=C_k(G+e)-C_k(G)\). Every \(d_{e,k}\) is nonnegative since an additional edge cannot invalidate a matching. Consequently

\[
\Delta_e(p)=\sum_{k=0}^{n}d_{e,k}p^k(1-p)^{n-k}.
\]

If one candidate \(e\) satisfies \(d_{e,k}\ge d_{f,k}\) for all \(k\) and for every alternative \(f\), then \(e\) is optimal uniformly over the full interval \((0,1)\). This is a sufficient certificate, not a generally necessary criterion.

**Exhaustive small-network certificate.** Since pollinators are unlabeled, every graph with \(n\) pollinators appears exactly once among the sorted \(n\)-tuples of masks \(1,\ldots,7\). There are exactly \(\binom{n+6}{6}\) such tuples. The accompanying standalone program `VERIFY.py` enumerates *every* tuple for \(3\le n\le7\), checks connectedness, all-pollinator service feasibility and existence of a missing link, enumerates *every* of its \(2^n\) live sets using the seven Hall inequalities, and computes every allowed one-edge coefficient vector exactly in integer arithmetic. The resulting exhaustive counts are:

| \(n\) | All mask multisets | Connected | Connected and serviceable | Eligible with a uniformly coefficientwise-best addition | Eligible without one |
|---|---:|---:|---:|---:|---:|
| 3 | 84 | 44 | 41 | 40 | 0 |
| 4 | 210 | 135 | 132 | 131 | 0 |
| 5 | 462 | 336 | 333 | 332 | 0 |
| 6 | 924 | 728 | 725 | 724 | 0 |
| 7 | 1716 | 1428 | 1425 | 1400 | 24 |

The one serviceable but ineligible network at each size is the complete bipartite graph, which has no missing incidence. Thus the coefficientwise certificates prove a uniform optimum in every eligible graph through six pollinators.

For each of the 24 exceptional seven-pollinator networks, the complete set of distinct candidate gain vectors \((d_{e,0},\ldots,d_{e,7})\) is contained in

\[
\{(0,0,0,0,0,0,0,0),\ (0,0,0,4,0,0,0,0),\ (0,0,0,3,1,0,0,0),\ (0,0,0,5,0,0,0,0)\}.
\]

Each exceptional graph contains a candidate with gain vector \((0,0,0,3,1,0,0,0)\), and contains a candidate with either the \(4\)-or-\(5\) leading vector. Exactly nine exceptional graphs contain a \(4\)-leading vector but no \(5\)-leading vector; fifteen contain a \(5\)-leading vector. Since any zero vector is dominated, these are comparisons of the globally optimal candidate set. In the nine former cases, the relevant gain difference is \(p^3(1-p)^3(1-2p)\). In the latter cases, it is \(p^3(1-p)^3(2-3p)\). Each has exactly one strict sign change in \((0,1)\). Exhaustive permutation-normalization identifies exactly the five stated plant-unlabeled classes.

**Witness cross-check.** For the first representative the directly counted baseline coefficients are \((0,0,0,26,34,21,7,1)\). All allowed additions have gains equal to either zero or the two \(4\)-leading and \((3,1)\) vectors stated above. Independent direct enumeration of all injective three-plant assignments, without using Hall's test, agrees on every live subset of the witness and every witness intervention. This proves the exhibited switch without relying on the global enumeration.

## Verification

Run `python VERIFY.py` using Python's standard library. Its output ends with `VERIFIED` if all exact assertions hold. It checks every mask multiset and every survival subset through seven pollinators; replays the stated counts, all 24 exceptional profiles, both switch thresholds, five orbit representatives, and 1408 independent Hall-versus-direct-assignment cases in the witness family. All calculations use integer arithmetic; the parameter-dependent conclusions follow from symbolic polynomial factorization displayed above, not a numeric parameter grid. The proof relies on the exhaustiveness of the explicitly inspected finite mask space and elementary Hall's theorem, and does not claim a symbolic all-\(n\) classification.

## Relationship to prior work

Kaiser-Bunbury and coauthors (2010) motivate robustness to loss of pollinator species and possible rewiring; their studied ecological robustness quantities and pollinator behavior do not assert this capacity-limited, single-edge augmentation threshold. Dietzfelbinger and Rink (2012) study left-perfect matchings in *randomly generated* bipartite graphs and optimal degree distributions, whereas this work fixes a graph and selects one new incidence to optimize robustness against independent failures of existing right-side vertices. Hommelsheim, Mühlenthaler and Schaudt (2018/2019) study adding a minimum-cost collection of edges so matching remains possible after any *one edge* fails adversarially; neither its failure model nor its optimization objective implies the present probability-dependent single-link choice. Sha and Steiglitz (1993) treat maintaining matchings under failures by dynamic algorithms rather than probabilistic pre-failure incidence selection. Classic node-reliability results for *connectivity* concern a different graph property. These are substantive distinctions in statements and objectives, not claims that broad matching or network-reliability methods are novel.

## Limitations

The claim applies to exactly three plant species, connected initially feasible incidence graphs, identical independent pollinator survival, capacity one per pollinator, and one added interaction. It is a mathematical service-allocation surrogate; a real pollinator may serve many plants and ecological dynamics can violate the assumptions. The exact counts distinguish unlabeled pollinators from labeled plants; the five representatives further quotient plant permutations. This finite classification does not yield a general algorithmic lower bound for arbitrarily many plants or a real-world intervention recommendation. Historical priority remains conditional on a finite but necessarily nonexhaustive literature review; independent audit has not been performed.

## References

- Olesen, J. M., Bascompte, J., Dupont, Y. L., and Jordano, P., *The modularity of pollination networks*, Proceedings of the National Academy of Sciences (2007), DOI: https://doi.org/10.1073/pnas.0706375104 (online December 4, 2007).
- Kaiser-Bunbury, C. N. et al., *The robustness of pollination networks to the loss of species and interactions*, Ecology Letters (2010), DOI: https://doi.org/10.1111/j.1461-0248.2009.01437.x (online March 15, 2010).
- Dietzfelbinger, M. and Rink, M., *Towards Optimal Degree-distributions for Left-perfect Matchings in Random Bipartite Graphs*, arXiv:1203.1506 (March 7, 2012), https://arxiv.org/abs/1203.1506.
- Sha, E. H. M. and Steiglitz, K., *Maintaining Bipartite Matchings in the Presence of Failures*, Networks 23 (1993), 459–471, https://www.cs.princeton.edu/~ken/maintaining_matchings93.pdf.
- Hommelsheim, F., Mühlenthaler, M., and Schaudt, O., *How to Secure Matchings Against Edge Failures*, arXiv:1805.01299 (May 3, 2018), https://arxiv.org/abs/1805.01299; STACS (2019), DOI: https://doi.org/10.4230/LIPIcs.STACS.2019.38.
- Goldschmidt, O., Jaillet, P., and Lasota, R., *On reliability of graphs with node failures*, Networks 24 (1994), 251–259, DOI: https://doi.org/10.1002/net.3230240407.
