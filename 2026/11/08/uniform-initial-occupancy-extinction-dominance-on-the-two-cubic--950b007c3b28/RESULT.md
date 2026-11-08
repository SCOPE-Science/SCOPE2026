# Uniform-initial-occupancy extinction dominance on the two cubic six-patch networks

## Finding

Let \(K_{3,3}\) be the complete bipartite graph with three vertices on each side, and let \(\Pi=C_3\square K_2\) be the triangular prism. In the finite continuous-time extinction–colonization process defined below, fix an initial number of occupied patches \(k\in\{1,2,3,4,5,6\}\). Select the initial occupied \(k\)-subset uniformly among all \(\binom 6 k\) possibilities. Write \(\overline T_{G,k}(c)\) for the resulting mean time until all patches become empty, where every occupied patch becomes empty at unit rate and every occupied-to-empty incidence across an undirected graph edge recolonizes at rate \(c\ge0\). Then, simultaneously for all six initial occupancies,

\[
\overline T_{K_{3,3},k}(c)>\overline T_{\Pi,k}(c)\qquad\text{for every }c>0,\;1\le k\le6,
\]

with equality at \(c=0\), when both equal the \(k\)-th harmonic number \(H_k=\sum_{j=1}^k1/j\). In particular, the strict difference also holds for a random i.i.d. Bernoulli initial occupancy with any positive occupation probability (conditioning on nonemptiness or not). These are the only two nonisomorphic connected simple cubic graphs on six vertices. Both have six vertices, nine edges, all degrees three, adjacency spectral radius three, and identical vertex-distance distributions (three vertices at distance one and two at distance two from each vertex). Nevertheless, their finite-population persistence times are strictly ordered at every positive colonization rate.

More precisely, define

\[
\begin{aligned}
A(c)&=298c^3+402c^2+189c+30,\\
B(c)&=2912c^6+9848c^5+14579c^4+12038c^3+5813c^2+1554c+180,\\
P(c)&=635040c^{11}+4620672c^{10}+16572996c^9+37914840c^8\\
&\quad+60557352c^7+69947220c^6+58940833c^5+35930580c^4\\
&\quad+15447328c^3+4448622c^2+771816c+61176.
\end{aligned}
\]

For full initial occupancy (\(k=6\)), the exact comparison is

\[
\boxed{\overline T_{K_{3,3},6}(c)-\overline T_{\Pi,6}(c)=\frac{c^3P(c)}{12A(c)B(c)}.}
\]

For every uniform initial \(k\)-subset, the complete exact comparison is

\[
\overline T_{K_{3,3},k}(c)-\overline T_{\Pi,k}(c)=\frac{c^3P_k(c)}{s_kA(c)B(c)},\qquad(s_1,s_2,s_3,s_4,s_5,s_6)=(6,30,60,12,12,12),
\]

where \(P_4=P_5=P_6=P\) and

\[
\begin{aligned}
P_1(c)={}&317520c^{11}+2204496c^{10}+7498746c^9+16237422c^8+24545199c^7+26873516c^6\\
&+21522422c^5+12508979c^4+5142426c^3+1419420c^2+236400c+18000,\\
P_2(c)={}&1587600c^{11}+11551680c^{10}+41203170c^9+93417564c^8+147529767c^7+168217453c^6\\
&+139767745c^5+83943616c^4+35531716c^3+10067784c^2+1717224c+133680,\\
P_3(c)={}&3175200c^{11}+23103360c^{10}+82864980c^9+189508680c^8+302451624c^7+348919470c^6\\
&+293503963c^5+178514691c^4+76531438c^3+21965682c^2+3795798c+299460.
\end{aligned}
\]

All coefficients of \(A,B,P_1,P_2,P_3,P\) are strictly positive. Thus the inequalities hold for all six counts and every \(c>0\), with no need to restrict the colonization rate or the occupancy probability.

## Assumptions and scope

The state space is the set of occupied subsets \(S\subseteq V(G)\); the empty set is absorbing. At each occupied vertex, local extinction occurs independently at rate one. A vacant vertex \(v\) is recolonized at rate \(c\) times its number of currently occupied neighbors. There are no spontaneous immigrations, no background catastrophes, no density dependence, and no new infections once the whole graph is empty. For each \(k\), the initial pattern is selected uniformly among all \(k\)-subsets; particular individual initial patterns need not obey the ordering. Any common mixture over initial occupancy sizes, with the occupied subset chosen uniformly conditional on its size, inherits weak dominance, strict whenever it assigns positive mass to at least one nonempty initial size at positive colonization. In particular, independent identically distributed Bernoulli initial occupancy with \(q\in(0,1]\) obeys the strict comparison (unconditional or conditioned on nonemptiness). The result holds for all real \(c\ge0\), including the zero-colonization boundary, not merely a parameter grid. The comparison is for the mean hitting time of the empty state, not for deterministic mean-field persistence, the tail of the extinction-time distribution, or a quasi-stationary distribution.

The triangular prism has edges \((0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)\). The complete bipartite graph has edges \((i,j)\) for \(i\in\{0,1,2\}\) and \(j\in\{3,4,5\}\). Both have maximum and minimum degree three, and their largest adjacency eigenvalue is exactly three by regularity and connectedness.

## Proof

**1. Minimal exhaustive graph classification.** A simple cubic graph must have at least four vertices and an even number of vertices. The only four-vertex cubic graph is \(K_4\). For six vertices, the complement of a cubic graph is two-regular. A simple two-regular six-vertex graph is either \(C_6\) or a disjoint pair of triangles. Their complements are respectively \(\Pi\) and \(K_{3,3}\), both connected and nonisomorphic because one has triangles and the other is bipartite. Therefore this is the first order admitting two distinct connected cubic graphs. Both graphs have diameter two; each vertex has three neighbors and two other vertices at distance two.

**2. Exact transient equations.** For each nonempty occupied subset \(S\), denote the expected extinction time by \(t_G(S)\), with \(t_G(\varnothing)=0\). Conditioning on the first transition gives

\[
\left(|S|+c\sum_{v\notin S}|N(v)\cap S|\right)t_G(S)
=1+\sum_{u\in S}t_G(S\setminus\{u\})
+c\sum_{v\notin S}|N(v)\cap S|t_G(S\cup\{v\}).
\]

The system is finite and uniquely solvable for every \(c\ge0\): from any nonempty state a finite sequence of local extinctions reaches the absorbing state with positive probability, so all transient states have finite expected absorption times. Vertex automorphisms collapse the 63 nonempty states into nine orbits for \(K_{3,3}\) and twelve for \(\Pi\); the automorphism counts are respectively 72 and 12. Solving the reduced systems over \(\mathbb Q(c)\), and evaluating the full-occupancy state \(S=V(G)\), yields

\[
T_{K_{3,3}}(c)=\frac{1620c^8+5832c^7+10548c^6+13008c^5+12657c^4+10952c^3+6671c^2+2223c+294}{4A(c)}
\]

and

\[
T_{\Pi}(c)=\frac{45360c^{11}+254880c^{10}+696960c^9+1245708c^8+1659000c^7+1797048c^6+1627274c^5+1182129c^4+639161c^3+235641c^2+52362c+5292}{12B(c)}.
\]

**3. Exact uniform-initial-occupancy comparisons.** The same unique symbolic orbit solution assigns \(t_G(S)\) to each nonempty state. Average these quantities over all states with \(|S|=k\) to obtain

\[
\overline T_{G,k}(c)=\frac1{\binom 6 k}\sum_{\substack{S\subseteq V(G)\\|S|=k}}t_G(S).
\]

For every \(k=1,\ldots,6\), direct symbolic common-denominator reduction produces the exact rational identities for \(P_k\) and \(s_k\) displayed above. All their listed coefficients, and those of \(A,B\), are strictly positive. Therefore each difference is strictly positive for all \(c>0\). At \(c=0\), the graph has no recolonizations, so the death process started with \(k\) occupied patches has expected extinction time \(H_k\), independent of graph structure. Any mixture over initial sizes, retaining uniformity of the subset conditional on its size, has the corresponding weighted-average difference and is strictly positive when there is a positive chance of at least one initially occupied patch. The finite symbolic rational identities supply the all-real-parameter proof, not a numeric extrapolation. `verify.py` builds the exact orbit systems, reconstructs the six symbolic mean-gap identities and verifies all polynomial signs.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The independent graph construction enumerates all \(6!\) possible vertex permutations to obtain automorphism groups, constructs the occupancy-transition matrices, and solves them over the rational-function field. It checks the two full-occupancy formulas, all six uniform-initial-count difference identities, and every coefficient sign; it independently constructs all 63 transient states (without symmetry reduction) for both graphs at \(c=1/3,1,3\), solving exactly over the rationals and comparing their averages for every occupancy count. All checks pass. Symbolic identities provide the all-real-parameter certificate; the six full-state systems and 36 independently evaluated occupancy-count comparisons detect mistakes in lumping or graph construction but are not used as an infinite proof. The complete verifier is contained in this package; Python 3 and the external SymPy library are required and are not vendored.

## Relationship to prior work

Barbillon et al. (arXiv:1404.4287, first posted 2014-04-16) investigate finite stochastic extinction–colonization processes and network-topology effects, with exact finite-size computations at selected experimental settings. Shtilerman and Stone (2015) examine adjacency spectral radius and in/out-degree structure as predictors of metapopulation persistence, principally in a mean-field framework. Van de Bovenkamp and Van Mieghem (2015) obtain exact SIS survival-time expressions for complete and star graphs. Holme and Tupikina (arXiv:1802.08849, first posted 2018-02-24) calculate exact SIS extinction-time expressions for every connected graph on three through eight vertices, including the present two; their paper explicitly states that they did not retain the full symbolic expressions, and concentrates on limits, structural correlations and rankings of *initial states within a given graph*. Their general master-equation method permits the current computation, but the all-positive-rate uniform-by-initial-count domination of one cubic graph by the other, with an explicit positive-coefficient certificate for all six counts, was not located as a stated theorem or displayed table comparison in the inspected text. The general computation framework itself is not claimed as new.

## Limitations

This is a finite six-patch comparison under equal local-extinction rates and edge-additive recolonization. Equal spectral radii do not imply equal mean extinction times in this stochastic setting; the result does not disprove the authors' deterministic spectral invasion criteria. It is not a general extremal theorem for all regular graphs, nor a per-state ranking for arbitrary specified initial occupancy patterns. Published exact-small-graph computations create a nontrivial historical-priority risk: the comparison may be implicit in unavailable computed data or other studies. No independent audit or external validation has been performed.

## References

- Barbillon, P., Thomas, M., Goldringer, I., Hospital, F., Robin, S. *Network impact on persistence in a finite population dynamic diffusion model: application to an emergent seed exchange network*. arXiv:1404.4287, first posted 2014-04-16. https://arxiv.org/abs/1404.4287
- Shtilerman, E., Stone, L. *The effects of connectivity on metapopulation persistence: network symmetry and degree correlations*. Proc. R. Soc. B **282** (2015), 20150203. https://pmc.ncbi.nlm.nih.gov/articles/PMC4426627/
- van de Bovenkamp, R., Van Mieghem, P. *Survival time of the susceptible-infected-susceptible infection process on a graph*. Phys. Rev. E **92** (2015), 032806. https://doi.org/10.1103/PhysRevE.92.032806
- Holme, P., Tupikina, L. *Epidemic extinction in networks: Insights from the 12,110 smallest graphs*. arXiv:1802.08849, first posted 2018-02-24. https://arxiv.org/abs/1802.08849
