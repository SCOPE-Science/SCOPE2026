# Five vertices are sharp for disagreement between mean-outbreak and three-case-risk vaccination

## Finding
For finite simple undirected contact graphs with one perfectly removed vaccinee, uniform selection of a single infection source from the remaining vertices, and independently open edges with common probability \(p\), let \(K_v\) be the size of the source's open cluster after removing vertex \(v\). Write
\[
M_v(p)=\mathbb E K_v,\qquad T_v(p)=\Pr(K_v\ge3).
\]
For every graph with at most four vertices, a single vaccination vertex minimizes both criteria simultaneously for **every** \(p\in[0,1]\). Among connected graphs on exactly five vertices there are precisely **two** isomorphism types for which the two argmin sets can be disjoint. For each type, they are disjoint **exactly when** \(1/4<p<3/4\). For the other nineteen connected five-vertex types, there is a fixed vertex minimizing both objectives for every \(p\in[0,1]\). At \(p=1/4\) and \(p=3/4\), each exceptional type has a common optimum.

Two labelled representatives, with vertices \(0,1,2,3,4\), are
\[
E_A=\{01,13,14,23,24,34\},\qquad
E_B=\{02,03,04,12,13,14,24\}.
\]
For \(G_A\), comparing vaccination of vertex \(1\) (leaving a triangle and an isolated vertex) with vaccination of vertex \(3\) (leaving a four-vertex path) gives
\[
M_1-M_3=\frac{p^2(1-4p)}2,\qquad
T_1-T_3=\frac{p^2(3-4p)}4.
\]
For \(G_B\), comparing vaccination of vertex \(0\) (leaving a triangle with a pendant leaf) with vaccination of vertex \(2\) (leaving a four-cycle) gives
\[
M_0-M_2=\frac{p^2(p-1)(4p-1)}2,\qquad
T_0-T_2=\frac{p^2(p-1)(4p-3)}4.
\]
All additional vaccination choices are either equivalent to one of the displayed alternatives or strictly worse for both objectives throughout \(0<p<1\).

## Assumptions and scope
There are \(n\ge2\) unweighted contacts, no self-loops and no repeated edges. Vaccination deletes exactly one vertex and every incident edge before any transmission. A seed is sampled uniformly from the \(n-1\) remaining vertices. Each remaining undirected edge is retained independently with probability \(p\in[0,1]\); infections reach exactly the open component of the seed. The threshold three includes the seed. All minimizations are over vaccination vertices, with ties retained. The classification for five vertices assumes the original graph is connected; the four-vertex-or-smaller statement allows disconnected graphs. This independent-edge model is not asserted to be equivalent to a general continuous-time SIR model.

## Proof
**(1) Lower-order guarantee.** After removing one vertex from a graph with at most four vertices, at most three vertices remain. Up to isomorphism, every graph on at most three vertices is nested by spanning-subgraph containment: the empty graph, one-edge graph, two-edge path, and triangle (with trivial adaptations for fewer vertices). Choose a deletion whose residual graph is smallest in this chain. Coupling all remaining percolation edges shows that its cluster size is stochastically no greater for any seed chosen uniformly among the remaining vertices; the permutation used in the embedding preserves the uniform seed law. It therefore minimizes \(M_v\) and every upper-tail probability, including \(T_v\), simultaneously for every \(p\).

**(2) Exact cluster probabilities.** Let \(H=G-v\) and \(r=n-1\). For each nonempty \(S\subseteq V(H)\), let \(R(H[S],p)\) be the probability that the independently retained induced edges connect \(S\), and let \(b_H(S)\) be the number of edges between \(S\) and its complement. Then
\[
\Pr(V(C_{\rm seed})=S)
=\frac{|S|}{r}R(H[S],p)(1-p)^{b_H(S)}.
\]
Indeed, the uniformly chosen source must belong to \(S\), its induced open subgraph must be connected, and every boundary edge must be closed; edges wholly outside \(S\) are unrestricted. Summing over \(S\) gives both objective polynomials. Independently, direct enumeration of every retained-edge subset yields the same polynomials. The included checker verifies the two identities for all \(105\) vertex deletions in the \(21\) connected five-vertex isomorphism classes.

**(3) Exhaustiveness and optimization for five vertices.** The accompanying `check.py` enumerates all \(2^{10}\) labelled graphs on five vertices, checks connectivity, and canonicalizes each connected graph by all \(5!\) vertex permutations. This produces exactly \(21\) classes without importing a graph catalogue. For each class and each of five possible deletions, it forms exact rational-coefficient polynomials for \(M_v,T_v\). Its inequalities are decided on the **whole continuum** \(p\in[0,1]\) using complete rational isolation of the real roots of each difference polynomial: signs are checked on every complementary root-free interval and at rational isolating endpoints. For \(19\) classes the checker exhibits a single deletion whose mean and three-case tail are no larger than any competitor for all \(p\). For the other two classes the checker identifies exactly the representatives above, proves that every additional deletion is a duplicate of one displayed option or strictly worse for both outcomes for \(0<p<1\), and verifies the four displayed polynomial identities symbolically. Factoring these differences yields the disagreement interval \(1/4<p<3/4\) and common-optimum boundaries. The full class and dominating-vertex table is supplied as `census.txt`.

## Verification
Run `python check.py` using Python 3 and SymPy (version \(1.11\) or later). The checker enumerates labelled graphs independently of graph catalogues, verifies exact polynomial agreement by two decompositions, uses rational real-root isolation for global inequalities, and asserts both exceptional factorizations. Successful execution prints \(21\) five-vertex classes, \(19\) universally dual-optimal classes, and exactly two exceptional classes. All symbolic comparisons are exact. The finite classification follows from exhaustive enumeration of an explicitly bounded set; no numerical grid or extrapolation from small graphs is used.

## Relationship to prior work
Kenah and Miller (2011) study vaccination strategies through epidemic percolation networks, including the distinction between major-epidemic probability and epidemic attack rate. Keeling and Shattock (2012) optimize expected epidemic final size in structured populations. Holme (2017) exactly compares three **different centrality tasks**—expected-outbreak influence, mean-outbreak vaccination, and sentinel surveillance—on small graphs; the present comparison instead concerns **two risk functionals of the same vaccination decision** in the independent-undirected-bond model. A prior result on the five-vertex graph \(G_A\) determines the mean-optimal vaccination and its \(p=1/4\) transition, but does not determine the three-case tail, the second exceptional isomorphism class, or the complete dual-objective census. The mean-only comparison for \(G_A\) is therefore acknowledged as previously established and not claimed anew here.

## Limitations
The result is specific to a single perfectly removed vertex, a uniformly random remaining seed, homogeneous independent undirected bond transmission, and a three-infection tail threshold. The two smallest non-equivalent graph classes are theoretical examples, not empirically optimized vaccination recommendations. No uniqueness is claimed for larger graph sizes, and no equivalence is asserted for correlated, directed, temporally evolving, or general Markovian SIR contact laws. Independent historical-priority and implementation review has not been performed; related formulations in reliability theory may exist.

## References
- Kenah, E. and Miller, J. C. (2011), *Epidemic Percolation Networks, Epidemic Outcomes, and Interventions*, DOI: 10.1155/2011/543520, first published 21 February 2011. https://doi.org/10.1155/2011/543520
- Keeling, M. J. and Shattock, A. (2012), *Optimal but unequitable prophylactic distribution of vaccine*, *Epidemics* 4:78–85, first online 7 March 2012. https://doi.org/10.1016/j.epidem.2012.03.001
- Holme, P. (2017), *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (first posted 22 August 2017); https://arxiv.org/abs/1708.06456
