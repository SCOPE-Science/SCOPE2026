# A sharp nine-species reversal of coextinction-richness variance under identical bipartite degrees

## Finding

**Theorem (sharp fixed-degree variance-ranking reversal).** In the one-step secondary-coextinction model described below, there are two connected simple bipartite species networks on **nine vertices and eight links** such that (i) every labeled vertex has the same degree in both networks; (ii) the expected surviving secondary richness agrees at every fixed number of surviving primary species; but (iii) the variance ranking of secondary richness reverses between two and three surviving primary species. **No such pair of connected networks exists on eight or fewer vertices.** The nine-vertex examples have the minimum possible number of edges among connected nine-vertex graphs.

Let primary species be \(P_1,\ldots,P_5\), secondary species \(S_1,\ldots,S_4\), and specify the secondary neighborhoods as follows:

| Secondary species | Network A | Network B |
|---|---|---|
| \(S_1\) | \(\{P_1,P_2,P_4,P_5\}\) | \(\{P_1,P_3,P_4,P_5\}\) |
| \(S_2\) | \(\{P_2,P_3\}\) | \(\{P_1,P_2\}\) |
| \(S_3\) | \(\{P_1\}\) | \(\{P_2\}\) |
| \(S_4\) | \(\{P_1\}\) | \(\{P_1\}\) |

Both labeled secondary degree vectors are \((4,2,1,1)\), and both labeled primary degree vectors are \((3,2,1,1,1)\). Both graphs are connected and have exactly eight edges; therefore both are bipartite trees. If \(Y_k\) counts functional secondary species after uniform survival of exactly \(k\) of the five primaries, then

\[
\begin{aligned}
(\operatorname{Var}_A(Y_k))_{k=1}^4
 &=\left(\frac{16}{25},\frac{17}{20},\frac{89}{100},\frac{16}{25}\right),\\
(\operatorname{Var}_B(Y_k))_{k=1}^4
 &=\left(\frac{16}{25},\frac{21}{20},\frac{69}{100},\frac{6}{25}\right).
\end{aligned}
\]

In particular \(\operatorname{Var}_A(Y_2)-\operatorname{Var}_B(Y_2)=-1/5\), whereas \(\operatorname{Var}_A(Y_3)-\operatorname{Var}_B(Y_3)=1/5\). The mean sequence is the same in both networks: \((8/5,5/2,31/10,18/5)\) for \(k=1,2,3,4\).

## Assumptions and scope

A network is a finite **simple, connected, unweighted bipartite graph**, with a nonempty primary guild and a nonempty secondary guild, and no isolated vertices. Exactly \(k\) of \(q\) primary vertices are sampled uniformly without replacement to survive; all other primary species are lost. A secondary species remains functional if and only if **at least one** of its primary neighbors remains. There are no further cascades, interaction-strength thresholds, spatial effects, or demographic feedback. \(Y_k\) is the integer number of functional secondary vertices. The comparison preserves degrees **at every labeled vertex of both guilds**, stronger than preserving each guild's degree distribution. A strict reversal requires distinct budgets \(k,\ell\) with opposite strict signs of the variance differences.

This is an exact finite mathematical result in a stylized coextinction model, not an ecological measurement or forecast.

## Proof

**1. Fixed-degree expectation and a pair-union variance formula.** Write \(N_i\) for the primary neighborhood of secondary vertex \(S_i\), with \(d_i=|N_i|\). Let

\[
 a_i(k)=\frac{\binom{q-d_i}{k}}{\binom qk},\qquad
 a_{ij}(k)=\frac{\binom{q-|N_i\cup N_j|}{k}}{\binom qk},
\]

with \(\binom nk=0\) when \(k>n\). These are the probabilities that a particular secondary species, or a specified pair, has no surviving primary neighbor. If \(I_i\) is its functional-survival indicator, then \(I_i=1-\mathbf1_{\{N_i\cap K=\varnothing\}}\). Consequently,

\[
\mathbb E Y_k=\sum_i(1-a_i(k))
\]

and the exact variance is

\[
\operatorname{Var}(Y_k)
 =\sum_i a_i(k)(1-a_i(k))
 +2\sum_{i<j}\left(a_{ij}(k)-a_i(k)a_j(k)\right).
\tag{1}
\]

For networks with the same secondary degrees, all terms except the pair-union probabilities are equal. This identifies the joint-neighborhood geometry as the source of any variance difference, despite equality of the expected values.

**2. Nine-vertex witness.** Directly inspecting the displayed neighborhoods gives the two identical labeled degree vectors and connectedness. For \(k=2\), enumerate the ten possible surviving primary pairs. In network A, the counts of subsets producing secondary richness \(1,2,3,4\) are respectively \(1,5,2,2\); in network B they are \(3,0,6,1\). For \(k=3\), the ten triple-subset outcomes in A have richness counts \(0,4,1,5\) for richness \(1,2,3,4\); in B they have counts \(1,0,6,3\). Their exact first and second moments yield the stated variance differences, and the independent formula (1) yields the same fractions. The cases \(k=1,4\) follow from the same ten-or-five-subset enumeration. The common expectations also follow directly from the identical secondary degrees.

**3. Sharp lower boundary.** If either guild contains just one vertex, connectedness forces a star and fixes the entire network at a given degree vector, so reversal between degree-matched networks is impossible. Otherwise let the guild sizes be \(p,q\ge2\). For every \(p+q\le8\), the included `check.py` enumerates all \(2^{pq}\) labeled binary incidence matrices by representing every possible row-neighborhood configuration with an integer bit mask. It rejects only disconnected graphs by an explicit bipartite breadth-first search. It then groups the complete set of connected graphs by the **sorted** secondary- and primary-degree sequences (a more permissive equivalence class than equal labeled degrees). For each graph and every nontrivial budget \(1\le k<q\), it calculates

\[
 v_k(G)=\binom qk^2\operatorname{Var}(Y_k)
 =\binom qk\sum_{|K|=k}Y_k(K)^2-
 \left(\sum_{|K|=k}Y_k(K)\right)^2,
\]

using integer arithmetic. Within each degree class it compares **every distinct variance vector** with every other; each component is divided by the same positive \(\binom qk^2\) for the two compared networks, so its sign is unchanged. Across all pairs of guild sizes with total at most eight, the complete sweep contains **70,479 connected labeled graphs, 352 degree classes, and 403 distinct degree-class variance profiles**. No pair of profiles has opposite strict signs at two budgets. As the enumeration ranges over all graph incidence matrices and all subsets, this is an exhaustive finite proof of the minimum order; it does not infer infinitary minimality from sampled experiments.

Finally, a connected graph on nine vertices has at least eight edges. Both exhibited networks have eight edges, proving minimality of their interaction count **at the minimal vertex order**. This does not assert global edge minimality without the connectedness and nine-vertex qualifications.

## Verification

Run `python3 check.py` using Python 3.8 or later. The standard-library-only checker independently computes the witness probabilities by subset enumeration and by the pair-union formula, tests connectedness and exact degrees, and performs the complete integer-exact census through eight vertices. Its replay yields `WITNESS_OK` and `MINIMALITY_OK`, reporting 70,479 connected graphs and no earlier reversal. The executable code, not an external log, defines all loops and assertions needed to reproduce the finite cutoff. The non-enumerative identity (1) is derived above from indicator covariance.

## Relationship to prior work

Memmott, Waser and Price (2004) introduced the one-step loss-of-all-partners framework for species-extinction simulations in pollination networks and established the relevance of linkedness and nestedness. Pastor and colleagues (2012) examined how network topology and degree-distribution changes influence ecological robustness using simulated extinction scenarios and an \(R_{50}\) index. Bane, Pocock and James (2018) studied distributions of robustness **integrated over primary-extinction sequences**, with different knockout rules and degree manipulations. Jones, Zurell and Wiesner (2024) gave analytic secondary-extinction predictions, including degree-driven **expectations**. Chabert-Liddell, Barbillon and Donnet (2022; first available preprint 2021) derive expectation and variance of ecological robustness under a stochastic-block-network model; the available abstract concerns network-ensemble robustness and does not itself establish the sharp fixed-realization degree-preserving crossover, although the full text could not be inspected. These developments motivate the problem but, in the materials inspected, do not specify the pointwise conditional-variance crossover **between two fixed-degree connected networks**, nor its sharp nine-vertex boundary. The claim is that exact new finite statement, not that architecture affects ecological robustness for the first time.

## Limitations

This is a model-specific nine-species extremal cutoff; it does not prove any empirical effect, encompass weighted interactions or recovery, or compare all higher moments. The finite proof relies on a fully specified exhaustive search over graphs of size at most eight; its runtime and result are reproducible with the supplied checker. Historical priority may require broader investigation of coverage-function variance, combinatorial reliability and ecological network null models; full text of the particularly relevant stochastic-block-model variance paper by Chabert-Liddell, Barbillon and Donnet (2022) was unavailable, so no whole-document noncoverage claim is made; absence of a retrieved matching statement is not a general uniqueness certificate. No independent scientific audit is claimed.

## References

- Memmott, J., Waser, N. M., and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B 271, 2605–2611. First published online 6 December 2004. https://doi.org/10.1098/rspb.2004.2909
- Pastor, J. M., Santamaría, S., Méndez, M., and Galeano, J. (2012). *Effects of topology on robustness in ecological bipartite networks*. Networks and Heterogeneous Media 7, 429–440. https://doi.org/10.3934/nhm.2012.7.429
- Bane, M. S., Pocock, M. J. O., and James, R. (2018). *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*. Ecology and Evolution 8, 10794–10804. https://doi.org/10.1002/ece3.4529
- Chabert-Liddell, S.-C., Barbillon, P., and Donnet, S. (2022). *Impact of the mesoscale structure of a bipartite ecological interaction network on its robustness through a probabilistic modeling*. Environmetrics 33, e2709. First preprint available 11 June 2021. https://doi.org/10.1002/env.2709
- Jones, C., Zurell, D., and Wiesner, K. (2024). *Novel analytic methods for predicting extinctions in ecological networks*. Ecological Monographs 94, e1601. https://doi.org/10.1002/ecm.1601
