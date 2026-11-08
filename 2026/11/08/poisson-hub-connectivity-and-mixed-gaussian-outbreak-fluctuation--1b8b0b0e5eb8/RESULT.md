# Poisson hub connectivity and mixed-Gaussian outbreak fluctuations in bipartite bond percolation

## Finding
Fix an integer \(r\ge3\), positive real numbers \(a_1,\ldots,a_r\), and a distinguished hub \(1\). Let \(B_n\) be the complete bipartite graph with hub vertices \(1,\ldots,r\) and \(n\) ordinary vertices. Retain each edge from hub \(i\) independently with probability \(p_{i,n}=a_i/\sqrt n\); take \(n\) sufficiently large that all these probabilities are at most one. Let \(C_n\subseteq[r]\) be the hubs in the open component of hub 1, and let \(Q_n\) be the number of ordinary vertices in that component.

On \([r]\) construct a random graph \(G\) with *independent* edges \(ij\), present with probability \(1-e^{-a_i a_j}\). Denote the component of hub 1 in \(G\) by \(C\). Independently of \(G\), take independent Gaussian variables \(Z_i\sim N(0,a_i)\). Then, jointly with the entire hub-projection graph,

\[
\left(C_n,\;\frac{Q_n-\sqrt n\sum_{i\in C_n}a_i}{n^{1/4}}\right)
\;\Longrightarrow\;
\left(C,\;\sum_{i\in C}Z_i\right).
\]

In particular, \(Q_n/\sqrt n\Longrightarrow\sum_{i\in C}a_i\). Conditional on the limiting hub component \(C\), the second-scale fluctuation has centered normal distribution with variance \(\sum_{i\in C}a_i\). The total variation distance between the projected hub graph and \(G\) is \(O_{r,a}(n^{-1/2})\).

For the homogeneous three-hub case \(a_1=a_2=a_3=a\), put \(z=e^{-a^2}\) and \(S=|C|\). The exact limiting weights are

\[
\Pr(S=1)=z^2,\qquad
\Pr(S=2)=2(1-z)z^2,\qquad
\Pr(S=3)=1-3z^2+2z^3.
\]

Thus the outbreak has three possible leading sizes \(a\sqrt n\), \(2a\sqrt n\), and \(3a\sqrt n\), each with Gaussian fluctuations of order \(n^{1/4}\) and conditional variances \(a\), \(2a\), and \(3a\), respectively.

## Assumptions and scope
All hub counts and activities are fixed while \(n\to\infty\); edge states are independent. The infected set in the undirected, bond-percolation formulation of an SIR outbreak equals the open connected component of the seed. \(Q_n\) counts ordinary vertices only; no assertion is made about temporal infection dynamics, directed transmission, or a number of hubs growing with \(n\).

## Proof
For each ordinary vertex \(v\), let \(T_v\subseteq[r]\) be the exact set of its adjacent hubs through open edges. The \(n\) sets are independent with probabilities

\[
\Pr(T_v=T)=\prod_{i\in T}\frac{a_i}{\sqrt n}\,
\prod_{j\notin T}\left(1-\frac{a_j}{\sqrt n}\right).
\]

Let \(U_{i,n}\) count the ordinary vertices with \(T_v=\{i\}\), and let \(Y_{ij,n}\) count the vertices with \(T_v=\{i,j\}\). Define their one-vertex cell probabilities \(q_{i,n}\) and \(q_{ij,n}\). Since \(r\) and the activities are fixed,

\[
q_{i,n}=\frac{a_i}{\sqrt n}+O(n^{-1}),\qquad
q_{ij,n}=\frac{a_i a_j}{n}+O(n^{-3/2}),
\]

and the probability of a vertex adjacent to at least three hubs is \(O(n^{-3/2})\). By the union bound the event \(E_n\) that *some* such vertex exists has probability \(O(n^{-1/2})\).

Because the cell counts are multinomial, for arbitrary fixed real \(t_i,s_{ij}\) their exact mixed moment generating function after centering is

\[
\exp\left(-n^{1/4}\sum_i a_it_i\right)
\left[1+\sum_iq_{i,n}\left(e^{t_i/n^{1/4}}-1\right)
+\sum_{i<j}q_{ij,n}\left(e^{s_{ij}}-1\right)\right]^n.
\]

Taylor expansion of its logarithm gives the limit

\[
\exp\left(\frac12\sum_i a_it_i^2
+\sum_{i<j}a_i a_j(e^{s_{ij}}-1)\right).
\]

The order-one differences between \(nq_{i,n}\) and \(a_i\sqrt n\) vanish after division by \(n^{1/4}\); the squared bracket correction is \(o(1)\) after multiplying by \(n\). Hence

\[
\left(\left(\frac{U_{i,n}-a_i\sqrt n}{n^{1/4}}\right)_{i=1}^r,
(Y_{ij,n})_{i<j}\right)
\Longrightarrow
\left((Z_i)_i,(P_{ij})_{i<j}\right),
\]

where all the variables on the right are independent, \(Z_i\sim N(0,a_i)\), and \(P_{ij}\sim\operatorname{Poisson}(a_i a_j)\).

On the complement of \(E_n\), each ordinary vertex meets zero, one, or exactly two hubs. Thus two hubs share a common ordinary neighbor precisely when \(Y_{ij,n}>0\); consequently their entire connectivity partition is that of the graph with edges \(\{ij:Y_{ij,n}>0\}\). In the limit these indicators are independent Bernoulli variables with probabilities \(1-e^{-a_i a_j}\). This yields the stated hub graph and component \(C\).

Moreover, on \(E_n^c\), every ordinary vertex in the seed's component is either a singleton adjacent to a hub of \(C_n\), or belongs to one of the pair categories. Therefore

\[
0\le Q_n-\sum_{i\in C_n}U_{i,n}
\le\sum_{i<j}Y_{ij,n}.
\]

The right-hand side is tight, and \(\Pr(E_n)\to0\), so the difference divided by \(n^{1/4}\) converges to zero in probability. Because the hub-partition map from a finite collection of pair-count indicators is well-defined at every integer vector, joint convergence and the continuous-mapping theorem prove the mixed-Gaussian statement. The first-scale limit follows by division by \(\sqrt n\).

For the total variation bound: probability of \(E_n\) is \(O(n^{-1/2})\). The multinomial vector of the finitely many pair-category counts differs in total variation by \(O(n^{-1})\) from independent Poisson variables of means \(nq_{ij,n}\), by the standard rare-cell Poisson coupling (the sum of pair probabilities is \(O(n^{-1})\)). Replacing those means by \(a_ia_j\) incurs \(O(n^{-1/2})\) by Poisson coupling, and mapping counts to edge indicators does not increase total variation. Combining these bounds proves the rate.

In the three-hub homogeneous example, the probability that hub 1 has no edge to either other hub is \(z^2\). The event that its component contains exactly one other hub occurs when one of its two incident edges exists and the two edges to the excluded hub are absent. These disjoint cases give \(2(1-z)z^2\), and the remaining weight is \(1-3z^2+2z^3\).

## Verification
The accompanying standalone `verify.py` enumerates all bond patterns on three-hub networks with up to four ordinary vertices, using exact rational probabilities for three independent parameter choices. It verifies normalization, the exact seed-component probabilities, and source-size bounds. It also checks the one-row pair decomposition and deterministic convergence of finite-size component probabilities to the stated inhomogeneous independent-edge limits. Executing `python verify.py` reports **96 passed arithmetic assertions**. These finite tests do not prove the limit; the multinomial moment-generating-function derivation and the preceding tightness/coupling argument provide the all-size proof.

## Relationship to prior work
Random intersection graphs encode the same common-feature projection used here; this construction is classical. Behrisch (2007), Theorem 1, studies the largest component as **both** the number of projected vertices and the number of features grow, identifying distinct giant-component regimes. Deijfen and Kets (2009), Theorems 1.1–1.2, study degree distributions and clustering in a weighted random intersection model with a growing projected vertex set. Newman (2009), Equations (10)–(17), gives component-size and percolation generating functions for a different clustered configuration model. The present claim instead concerns a **fixed** heterogeneous hub set, an increasing population of intermediate ordinary vertices, and their joint two-scale random outbreak law: discrete limiting hub connectivity together with Gaussian ordinary-population fluctuations. These statements and parameter regimes are not implied by the cited primary results as examined; the classical Poisson and Gaussian ingredients are not individually claimed as new.

## Limitations
The theorem does not address time-to-infection, directed contagion, variable hub count, activity parameters changing with \(n\), or process-level paths. Exact historical priority of the particular joint two-scale formulation has not been independently certified, and equivalent formulations may exist under different terminology. No claim is made about a giant component containing a positive fraction of all \(n\) ordinary vertices; the natural size here is \(\sqrt n\).

## References
1. M. Behrisch, *Component Evolution in Random Intersection Graphs*, Electronic Journal of Combinatorics 14 (2007), R17, published 2007-01-29. https://doi.org/10.37236/935 (Theorem 1, Sections 2–5).
2. M. Deijfen and W. Kets, *Random Intersection Graphs with Tunable Degree Distribution and Clustering*, Probability in the Engineering and Informational Sciences 23 (2009), 661–674. https://arxiv.org/abs/1509.07019 (Sections 1.1–1.2 and Theorems 1.1–1.2; arXiv repost 2015).
3. M. E. J. Newman, *Random Graphs with Clustering*, Physical Review Letters 103 (2009), 058701. https://arxiv.org/abs/0903.4009 (Equations (10)–(17) and (24)–(25), submitted 2009-03-24).
4. K. Rybarczyk and D. Stark, *Poisson Approximation of the Number of Cliques in Random Intersection Graphs*, Journal of Applied Probability 47 (2010), 826–840. https://doi.org/10.1239/jap/1285335412 (different clique-count observable; abstract consulted).
