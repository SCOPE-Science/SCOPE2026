# Full-outbreak source ranking depends only on degree on every homogeneous tree

## Finding
Let a finite undirected tree have at least two vertices. A single initially infectious vertex initiates a susceptible–infectious–removed epidemic. Each newly infectious vertex has an independent identically distributed positive finite infectious lifetime \(T\); during its lifetime, contacts to each neighbor occur as independent rate-\(\lambda\) Poisson processes, with \(\lambda>0\). Write \(X=1-e^{-\lambda T}\), \(m_j=\mathbb E[X^j]\) for integers \(j\ge0\), and \(m_0=1\). All vertices are initially susceptible except the source \(s\).

The exact probability \(P_s\) that *every vertex is ever infected* is
\[
P_s=C_G\frac{m_{d_s}}{m_{d_s-1}},\qquad
C_G=\prod_{v\in V(G)}m_{d_v-1},
\]
where \(d_v\) is the ordinary vertex degree. In particular, for a fixed tree, complete-outbreak probabilities are nondecreasing in source degree, and are strictly increasing when \(T\) is not almost surely constant. Any two trees with the same degree multiset have the same complete-outbreak probability for source vertices of the same degree, regardless of the arrangement of their edges.

If the tree has vertices of degrees one and two, the exact risk ratio is the same for every such tree:
\[
\frac{P_{\mathrm{degree\ 2}}}{P_{\mathrm{degree\ 1}}}
=\frac{\mathbb E[X^2]}{(\mathbb E X)^2}
=1+\frac{\operatorname{Var}(X)}{(\mathbb E X)^2}.
\]
Thus this degree-comparison ratio measures heterogeneity of individual transmissibility, rather than contact-network topology. For independent exponential infectious lifetimes of recovery rate \(\mu>0\),
\[
P_s=\left[\prod_{v\in V(G)}\frac{(d_v-1)!\lambda^{d_v-1}}{\prod_{j=1}^{d_v-1}(\mu+j\lambda)}\right]
\frac{d_s\lambda}{\mu+d_s\lambda},
\]
with empty products equal to one. In that model the degree-two to degree-one ratio is \(2(\mu+\lambda)/(\mu+2\lambda)\).

## Assumptions and scope
The graph is a finite simple connected undirected acyclic graph on \(n\ge2\) vertices. Infectious lifetimes are iid, almost surely in \((0,\infty)\), and are independent of all edge-contact Poisson processes. A vertex is infectious once and then permanently removed; transmission is immediate on its first infectious contact with a susceptible neighbor. There are no infections from outside, no preexisting immunity, no latent transmission, no reinfection, and no cycle providing an alternate route. The rates of contact are homogeneous and symmetric. The event is eventual infection of **all** vertices, not simultaneous infection or survival past a deadline. In the equivalent conditionally independent outgoing-bond model, the theorem holds for any iid latent \(X\) supported in \((0,1)\), without specifying a lifetime distribution.

## Proof
Root the tree at the initial source \(s\), and orient every edge away from \(s\). Every vertex except \(s\) has exactly one parent. By uniqueness of paths, a vertex can be reached only after its parent is infected. Consequently the event that all vertices are ever infected is exactly the intersection of the events that every parent manages at least one transmission to **each** of its children before its own removal.

Condition on the infectious lifetime \(T_v=t\) of a given vertex \(v\). Each of its \(c_v\) child-directed contact processes independently has a contact in this interval with probability \(1-e^{-\lambda t}\). Conditional probability of all required transmissions is therefore \((1-e^{-\lambda t})^{c_v}\). Taking expectations gives \(m_{c_v}\). Since distinct parents' lifetimes and outbound contact processes are independent, the child-transmission success events for distinct parents are independent, so
\[
P_s=\prod_{v\in V(G)}m_{c_v}.
\]
The root has \(c_s=d_s\), and every other vertex has \(c_v=d_v-1\). As \(T>0\) almost surely, all moments \(m_j\) are positive. Factoring out \(m_{d_s-1}\) gives the displayed formula. Its common product depends only on the degree multiset, proving both the exact source-degree reduction and the degree-preserving rewiring invariance.

For monotonicity, put \(r_j=m_j/m_{j-1}\) for \(j\ge1\). Cauchy–Schwarz implies
\[
m_j^2\le m_{j-1}m_{j+1},\quad r_{j+1}\ge r_j.
\]
If \(X\) is nonconstant and strictly positive almost surely, equality in Cauchy–Schwarz would require \(X^{(j-1)/2}\) and \(X^{(j+1)/2}\) to be proportional, forcing \(X\) to be constant. Hence every inequality is strict. Because \(T\mapsto1-e^{-\lambda T}\) is strictly increasing, strictness is equivalent to nonconstant \(T\). The case of constant \(T\) gives \(m_j=(\mathbb E X)^j\), so every source has the same probability \((\mathbb E X)^{n-1}\). The degree-one to degree-two ratio follows from \(r_2/r_1=m_2/m_1^2\).

If \(T\sim\operatorname{Exp}(\mu)\), the substitution \(y=e^{-\lambda t}\) yields
\[
m_j=\int_0^\infty\mu e^{-\mu t}(1-e^{-\lambda t})^j\,dt
=\frac{j!\lambda^j}{\prod_{i=1}^j(\mu+i\lambda)}.
\]
Thus \(r_j=j\lambda/(\mu+j\lambda)\), giving the Markovian formulas. All formulae include the boundary case \(n=2\), for which the two source degrees coincide.

## Verification
`CHECKER.py` performs two independently constructed exact tests. First, it solves the full susceptible–infectious–removed continuous-time Markov chain by a finite-state absorption recurrence using rational arithmetic at three rational contact/recovery rate pairs. It compares complete-infection probabilities for every source on six tree instances (four through six vertices) with the product formula, with no numerical tolerances. Second, it directly enumerates all iid two-point infectiousness assignments and directed transmission outcomes on the same trees and compares exact probabilities to the arbitrary-lifetime moment formula. A total of 120 source/rate or source/distribution checks pass. The checker also confirms the invariant probabilities \(1/24\), \(1/18\), and \(1/16\) for degrees one, two, and three on two nonisomorphic six-vertex trees at \(\lambda=\mu=1\). These finite tests check implementation and edge cases; the proof above supplies the statement for arbitrary tree size.

Run `python CHECKER.py` with Python 3.9 or newer; it uses only the standard library.

## Relationship to prior work
Karrer and Newman (arXiv:1003.5673, first posted March 29, 2010) developed exact message passing for arbitrary infectious-period distributions on trees, and described correlations arising from shared recovery times. Their general equations address node infection probabilities and percolation behavior, whereas the present claim identifies a specific **joint event** (infection of every vertex) and a topology-invariant source-degree quotient using higher moments of a single individual's transmissibility. Sharkey et al. (DOI:10.1007/s11538-013-9923-5, online December 2013) establish exact Markovian tree epidemic moment equations. Hall and Siebert (DOI:10.1007/s00285-022-01854-9, 2023) derive exact node-state marginals on rooted trees. The full-outbreak moment product and its strict degree-ordering/heterogeneity identity were not located in the inspected relevant sections of these primary studies. Their more general modelling frameworks do make the product construction accessible; absence of an explicit match is not proof of worldwide novelty.

Unlike independent-bond percolation with a deterministic edge transmissibility, a random common infectious lifetime makes transmissions from one vertex to several children positively dependent. This is precisely what yields a degree-dependent probability of infecting the entire tree. For source-degree comparisons, conditioning on the *same* lifetime for all children is essential; assigning independent infectious lifetimes separately to edges would invalidate the strict ordering.

## Limitations
The theorem does not apply to networks with cycles, multiple sources, directed/heterogeneous contact rates, different infectious-period distributions by vertex, or simultaneous-all-infectious events. It makes no universal claim about expected outbreak size, peak prevalence, duration, or all other final-size thresholds, which can depend on more of the tree structure. The exact risk may be very small on large trees, limiting empirical measurability. Unindexed earlier general epidemic-percolation formulations may already contain an equivalent statement; independent historical-priority checking remains necessary. The separate reproducibility program checks finitely many examples and cannot replace the general proof.

## References
1. Karrer, B. and Newman, M. E. J. (2010). *A message passing approach for general epidemic models*. Physical Review E 82, 016101. First public preprint 2010-03-29, https://arxiv.org/abs/1003.5673 ; DOI:10.1103/PhysRevE.82.016101.
2. Sharkey, K. J., Kiss, I. Z., Wilkinson, R. R. and Simon, P. L. (2013 online). *Exact Equations for SIR Epidemics on Tree Graphs*. Bulletin of Mathematical Biology 77, 614–645. https://doi.org/10.1007/s11538-013-9923-5.
3. Hall, C. L. and Siebert, B. A. (2023). *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation*. Journal of Mathematical Biology 86, article 22. https://doi.org/10.1007/s00285-022-01854-9.
