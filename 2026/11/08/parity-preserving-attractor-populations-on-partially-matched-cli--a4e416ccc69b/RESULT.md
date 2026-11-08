# Parity-preserving attractor populations on partially matched clique pairs

## Finding

Let \(G_{n,t}\) comprise two labelled, disjoint cliques of order \(n\) with \(t\) disjoint cross-clique matching edges, where \(n\ge2\) and \(0\le t\le n\). Under uniform random sequential binary closed-neighborhood minority updates, **all recurrent configurations are exactly the maximum cuts**. The recurrent communication classes admit a complete description and census below. In particular, for every \(k\ge1\) and \(0\le t\le 2k+1\),
\[
R_{2k+1,t}=R_{2k+2,t},
\]
although all recurrent states on \(G_{2k+2,t}\) are absorbing, while the recurrent classes on \(G_{2k+1,t}\) are products of adjacent-rank Boolean inclusion graphs. This identity has an explicit bijection: append one unmatched vertex to each clique and give it the spin needed to balance the enlarged clique.

Set \(B(u,j)=\binom{u}{j}\) for integer \(0\le j\le u\) and \(B(u,j)=0\) otherwise, and \(F_u(j)=B(u,j)+B(u,j+1)\). The maximum cut size of \(G_{n,t}\) is \(2\lfloor n^2/4\rfloor+t\).

If \(n=2k\), put \(u=n-t\). Every recurrent state is absorbing, and the number of recurrent states (and classes) is
\[
R_{2k,t}=K_{2k,t}=\sum_{a=0}^{t}\binom ta B(u,k-a)B(u,k-t+a).
\]

If \(n=2k+1\), put \(u=n-t\), \(L=\max(0,t-k-1)\), and \(U=\min(t,k+1)\). The recurrent classes are indexed by the subsets \(M\subseteq\{1,\dots,t\}\) with \(L\le |M|\le U\), where \(M\) is the set of matched vertices in the first clique holding spin one. The class indexed by \(M\), of cardinality \(a=|M|\), has exactly
\[
S(M)=F_u(k-a)F_u(k-t+a)
\]
configurations. It is the Cartesian product of the inclusion graphs between the permitted consecutive Boolean ranks \(k-a,k+1-a\) and \(k-t+a,k+1-t+a\), respectively, on the two unmatched vertex sets. Thus
\[
K_{2k+1,t}=\sum_{a=L}^{U}\binom ta,\qquad
R_{2k+1,t}=\sum_{a=0}^{t}\binom ta F_u(k-a)F_u(k-t+a).
\]
Every such class is connected, and its invariant distribution is uniform. In particular, if \(0\le t\le k+1\), every matched-spin vector is admissible and there are exactly \(2^t\) classes on the odd graph. In both parities every initial state almost surely enters the recurrent set.

For instance, \(G_{5,2}\) has four classes of sizes \(16,36,36,16\). The graph \(G_{6,2}\) instead has \(104\) absorbing states, precisely the same total recurrent population.

## Assumptions and scope

The vertices are \(A_1,\dots,A_n,B_1,\dots,B_n\); each set of \(n\) spans a complete graph, and the only cross edges are \(A_iB_i\) for \(1\le i\le t\). Vertices are labelled, each spin is in \(\{0,1\}\), and a uniformly selected vertex updates to the minority spin among itself and its graph neighbors, staying unchanged on a tie. Only one vertex is considered per discrete step. Recurrent communication classes refer to the finite-state Markov chain including self-loops. No claim is made about consensus, hitting-time rates, or the spectral gap of an individual class.

## Proof

**1. Cut monotonicity and the maximum.** Let \(Q\) be the number of graph edges with different endpoint spins. At a selected vertex, let \(s\) count neighbors with the current spin and \(d\) those with the opposite spin. The closed-neighborhood minority rule flips the vertex precisely when \(s+1>d\), in which case the cut changes by \(s-d\ge0\). Every clique of order \(n\) contributes at most \(\lfloor n^2/4\rfloor\) cut edges; the matching contributes at most \(t\). The two maxima can be attained simultaneously: choose near-half spins in the first clique, impose opposite spins on the matched partners in the second clique, and assign unmatched spins to balance the second clique. Such an assignment exists for all \(t\le n\), by choosing the number of ones on the matched vertices near \(t/2\). Therefore \(Q_{\max}=2\lfloor n^2/4\rfloor+t\); it is attained exactly when each clique has a maximally balanced spin count and every matching edge is cut.

**2. Constructive escape from non-maximal configurations.** A clique with more than \(\lceil n/2\rceil\) ones can decrease its number of ones by flipping any one-vertex; a clique with fewer than \(\lfloor n/2\rfloor\) ones can analogously flip any zero-vertex. All these flips obey the minority rule regardless of the matched partner: for a vertex whose spin is in the overrepresented class, its closed-neighborhood same-spin count exceeds the opposite count even if its matched neighbor has the opposite spin. Repeating these flips balances both cliques without decreasing \(Q\).

Assume now both cliques balanced and a matching edge is uncut. If \(n=2k+1\), a spin appearing \(k+1\) times in a clique is its majority spin. If the common spin of the uncut matching edge is a majority in either clique, firing that endpoint gives a strict increase of \(Q\) by one. Otherwise its common spin is a minority in both cliques. Among the \(k+1\) vertices of the opposite (majority) spin in the first clique, at least one is unmatched or matched to the *same* spin: there are only \(k\) opposite-spin potential partners in the second clique. In the latter case firing this majority vertex immediately increases \(Q\) by one; in the former, firing the unmatched majority vertex is a neutral update and makes the original uncut endpoint a majority-spin vertex, which can then be fired for a strict increase. (Only one neutral update is needed.)

If \(n=2k\), firing one endpoint of the uncut matching edge is a neutral update. This creates a clique with \(k+1\) vertices holding the now-majority spin. The other clique remains balanced and contains only \(k\) vertices of the opposite spin, so among these \(k+1\) majority vertices at least one is unmatched or paired with the same spin. Firing that vertex increases \(Q\) strictly, by one or two. Consequently, from any balanced state with an uncut matching edge a sequence of at most two legal updates strictly increases \(Q\).

After each strict increase rebalance the cliques as in the first paragraph. Since \(Q\) is a bounded integer and never falls, the process can be repeated only finitely many times before both cliques are balanced and all matching edges are cut. Thus from every configuration a finite positive-probability legal update path reaches a maximum cut. The maximum-cut set is closed because \(Q\) cannot exceed \(Q_{\max}\). A recurrent communicating class disjoint from it would contain a state with a path leaving the class, which is impossible. Standard finite-chain recurrence therefore proves almost-sure eventual arrival at a maximum cut.

**3. Transitions within maximum cuts.** Fix a maximizer. If \(n=2k\), each clique contains \(k\) ones and \(k\) zeros. No unmatched vertex is active. A matched vertex sees its opposite-spin partner and is also inactive. Every maximizing configuration is therefore absorbing.

If \(n=2k+1\), each clique has \(k\) or \(k+1\) ones. Every matched vertex sees an opposite-spin partner and is inactive. Among unmatched vertices, exactly the majority-spin vertices may flip, interchanging the two balanced ranks while keeping all matching edges cut. Hence the matched spin vector is constant on every recurrent trajectory. With that vector fixed, the two cliques evolve independently on the inclusion graph of subsets of unmatched vertices of two consecutive allowed sizes. If both ranks are present, their inclusion graph is connected (two subsets of equal size are joined by successive single-element exchanges via the intervening rank). If only one rank is present, it is rank zero or rank \(u\), so there is exactly one vertex. This proves both the classification and connectivity. Every active move has an equally likely reverse move, namely probability \(1/(2n)\), so the stationary law on a class is uniform. Self-loops make the nontrivial classes aperiodic.

**4. Class sizes and the parity bijection.** Fix the matched vector with \(a\) ones in clique A and \(t-a\) in B. For odd \(n=2k+1\), the unmatched subsets in A have sizes \(k-a\) or \(k+1-a\), and those in B have sizes \(k-t+a\) or \(k+1-t+a\). Their product has \(F_u(k-a)F_u(k-t+a)\) elements and is nonempty exactly when \(\max(0,t-k-1)\le a\le\min(t,k+1)\). Summation over the \(\binom ta\) matched vectors gives both odd formulas. For even \(n=2k\), both clique spin counts must equal \(k\); the product \(B(u,k-a)B(u,k-t+a)\) gives the even formula.

Finally, take an odd graph \(G_{2k+1,t}\) and add one new unmatched vertex to each clique. For each odd maximum-cut configuration, set the new vertex spin to one exactly when its old clique had \(k\) ones; otherwise set it to zero. Each enlarged clique then has \(k+1\) ones, and all matching edges remain cut. Deleting the two new vertices recovers the odd maximizer, so this is a bijection between the recurrent configurations of \(G_{2k+1,t}\) and \(G_{2k+2,t}\). Equivalently, its cardinality identity is Pascal's rule \(B(u,j)+B(u,j+1)=B(u+1,j+1)\). The even configurations are absorbing whereas odd configurations carry the class structure proved above.

## Verification

Two independently implemented programs accompany this result. `verify_components.py` constructs the full directed update graph and independently computes all terminal strongly connected components using NetworkX for every \(2\le n\le6\) and \(0\le t\le n\), comparing each component **as a set of states** against the claimed decomposition (25 graphs, 36,400 labelled states). `verify_parity.py` independently computes clique cuts using integer bitsets, enumerates all cut maximizers, checks their closure under every allowed update, compares rank-enumeration formulas, and verifies all parity-paired census equalities for \(2\le n\le8\) (42 graph instances, 757,296 labelled states; 15 odd-even equalities). The captured outputs are `components.log` and `parity.log`. Reproduce with `python verify_components.py` and `python verify_parity.py` after installing `requirements.txt`. These finite tests cross-check the infinite-family proof; they do not replace it.

## Relationship to prior work

Rouquier, Regnault and Thierry (2010/2011) introduced this exact closed-neighborhood asynchronous minority rule, proved cut/energy monotonicity, and classified ordinary clique attractors. Their Theorem 4.1 covers the case without matching edges by separate clique analysis but does not state the matched-coupling classification, class-size formulas, or odd-even population-preserving bijection. Those established ingredients are used here, not claimed as new. Gastner and Ishida (2019) studied two-community clique graphs under the **voter-copying** rule with random cross edges; that rule drives consensus and is not the anti-coordination rule studied here. Previous graph-specific results on other minority-update graphs do not imply this matching-bridge interpolation. The present contribution is a complete recurrent-class classification and its parity correspondence for this particular graph family, not a claim to invent the dynamics or the Boolean-lattice incidence graph.

## Limitations

The results are exact for simple unweighted graphs with two equally sized cliques and disjoint, unit-weight matching links. They do not extend without proof to arbitrary cross edges, unequal clique sizes, weighted spins, different tie rules, simultaneous updates, or positive-temperature Glauber dynamics. Absorption times, hitting probabilities among classes, within-class mixing times, and complete eigenvalue formulas are not determined. Novelty is supported by comparisons of accessible published material and relevant prior statements, not by a proof that no unindexed equivalent theorem exists. Independent external validation has not been carried out.

## References

1. J.-B. Rouquier, D. Regnault, and É. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119v1 (first posted 2010-11-23); Theoretical Computer Science **412** (2011), 3947–3963, DOI:10.1016/j.tcs.2011.02.028. Full-text accessible at https://ar5iv.labs.arxiv.org/html/1011.5119.
2. M. T. Gastner and K. Ishida, *Voter model on networks partitioned into two cliques of arbitrary sizes*, arXiv:1908.00849v1 (2019-08-02); Journal of Physics A **52** (2019), 505701, DOI:10.1088/1751-8121/ab542f. Accessible at https://arxiv.org/pdf/1908.00849.
