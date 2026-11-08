# Strict all-time monomer-adsorption ordering of two cubic twenty-site networks

## Finding
Consider rate-one irreversible hard-core monomer adsorption on the dodecahedral graph \(D=GP(10,2)\) and the Desargues graph \(H=GP(10,3)\). These are two canonical connected cubic, distance-transitive graphs, each with twenty vertices and thirty edges. If \(X_G(t)\) is the number of occupied vertices by time \(t\), then
\[
\mathbb E X_H(t)>\mathbb E X_D(t)\quad\text{for every real }t>0.
\]
The inequality remains true after replacing the independent rate-one arrivals by *exactly* \(k\) uniformly selected potential arrivals in uniformly random order, for every integer \(5\le k\le20\). For \(0\le k\le4\) the two expected occupancies coincide.

Writing \(p=1-e^{-t}\), the difference begins precisely at fifth order:
\[
\mathbb E X_H(t)-\mathbb E X_D(t)=4p^5+O(p^6)\quad(p\downarrow0),
\]
and the exact jammed-mean gap is
\[
\lim_{t\to\infty}(\mathbb E X_H(t)-\mathbb E X_D(t))
=\frac{2030003}{3144960}.
\]

The complete terminal laws are

| Occupied sites \(j\) | \(\Pr[X_D(\infty)=j]\) | \(\Pr[X_H(\infty)=j]\) |
|---|---:|---:|
| \(6\) | \(1/90\) | \(1055/6912\) |
| \(7\) | \(302009/336960\) | \(2152/7371\) |
| \(8\) | \(31207/336960\) | \(81557/207360\) |
| \(10\) | \(0\) | \(37763/232960\) |

and all other terminal sizes have probability zero. Hence the strict mean ordering does **not** reflect first-order stochastic dominance of the terminal laws: \(\Pr[X_D(\infty)\ge7]>\Pr[X_H(\infty)\ge7]\), but \(\Pr[X_D(\infty)\ge8]<\Pr[X_H(\infty)\ge8]\).

## Assumptions and scope
For either \(k=2\) or \(k=3\), the graph \(GP(10,k)\) has vertices \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+k}\); all edges are undirected and each cyclic index is taken modulo ten. Thus the graph definitions are fully specified without any graph database. In the adsorption process each vertex has an independent exponential first-attempt time of rate one. The attempt succeeds precisely when none of the vertex's neighbors is already occupied; rejected attempts have no subsequent effect. No desorption, diffusion, additional particles, or time-dependent attempt rate is assumed. The assertions are exact for these two fixed graphs, for all real \(t\ge0\).

## Proof
Let \(N_G[v]\) be the closed neighborhood of \(v\). For every finite candidate set \(S\subseteq V(G)\), let \(f_G(S)\) be the mean number of accepted vertices when precisely the vertices of \(S\) are attempted in a uniformly random order. Exchangeability of the first attempted vertex gives
\[
f_G(\varnothing)=0,\qquad
f_G(S)=1+\frac{1}{|S|}\sum_{v\in S}f_G(S\setminus N_G[v]).
\]
This is exact because the first attempted vertex is accepted, and deleting its closed neighborhood removes exactly the candidates that can no longer be accepted. Set \(a_G(S)=|S|!f_G(S)\). The recurrence becomes the integer identity
\[
a_G(S)=|S|!+\sum_{v\in S}
\frac{(|S|-1)!}{|S\setminus N_G[v]|!}\,
a_G(S\setminus N_G[v]).
\]
All factors are integers. Applying this recurrence in increasing subset size to all \(2^{20}\) bitmasks, and accumulating \(a_G(S)\) by cardinality, gives the exact rational values
\[
\mu_G(k)=\binom{20}{k}^{-1}\sum_{|S|=k}f_G(S).
\]
Let \(\delta_k=\mu_H(k)-\mu_D(k)\). The full twenty-one-entry exact table in `bernstein_differences.tsv` satisfies
\[
\delta_0=\cdots=\delta_4=0,\qquad
\delta_5=\frac1{3876},\qquad
\delta_k>0\quad(5\le k\le20),\qquad
\delta_{20}=\frac{2030003}{3144960}.
\]
Each integer operation and each comparison is reproducibly implemented in `verify_kinetics.py`; no floating-point sign test is used.

For independent exponential arrival times, the set of vertices that have attempted by time \(t\) is a Bernoulli-\(p\) random subset of the twenty vertices with \(p=1-e^{-t}\). Conditional on its cardinality and identity, arrival order is uniform. Therefore
\[
\mathbb E X_H(t)-\mathbb E X_D(t)
=\sum_{k=0}^{20}\binom{20}{k}p^k(1-p)^{20-k}\delta_k.
\]
Every summand is nonnegative for \(0\le p\le1\), and the \(k=5\) term is strictly positive for \(0<p<1\), while the \(k=20\) term is positive at \(p=1\). This proves the all-time inequality, including the terminal limit. Since \(\binom{20}{5}\delta_5=4\), the fifth-order coefficient is exactly four.

There is an additional local explanation for the first difference. An independent enumeration of all \(\binom{20}{5}=15504\) five-vertex induced subgraphs finds eight differing motif profiles, with the difference of their count-weighted five-vertex greedy expectations exactly \(4\). In particular, \(D\) has twelve induced five-cycles and \(H\) has none. The complete motif computation and its exact weighted identity are in `verify_five_cycles.py`.

Finally, the terminal probability generating function \(P_G(S;z)\) for the available candidate set obeys
\[
P_G(\varnothing;z)=1,\qquad
P_G(S;z)=\frac z{|S|}\sum_{v\in S}P_G(S\setminus N_G[v];z).
\]
Exact rational evaluation at \(S=V(G)\) yields the displayed two terminal distributions. An independently structured recursion over *occupied independent sets*, with uniform selection among currently eligible vertices, reproduces both distributions; see `verify_independent.py`. Their means equal \(\mu_D(20)=2386183/336960\) and \(\mu_H(20)=72903133/9434880\), respectively. The two terminal-tail inequalities follow by summing the listed exact probabilities.

## Verification
Run from the extracted artifact directory using Python 3 and only the standard library:

```
python3 verify_kinetics.py
python3 verify_independent.py
python3 verify_five_cycles.py
```

The first script calculates the complete twenty-one-coefficient exact Bernstein certificate via integer subset dynamic programming, the terminal distributions via a separate polynomial recursion, and the tail crossing. The second script uses occupied-state rather than available-set states and additionally enumerates all orderings of selected five-site sets. The third script classifies all five-site induced subgraphs and verifies their contribution to the first nonzero coefficient. Assertions fail immediately on disagreement. All computations are finite and exhaustive within the claimed twenty-vertex graphs; they do not constitute an extrapolation to arbitrary graph order.

## Relationship to prior work
Pippenger's *Random Sequential Adsorption on Graphs* (1989) introduced graph RSA and treats degree-regular graphs, high-girth asymptotics, and finite-cycle effects. Its available abstract does not give this evaluated pairwise kinetic ordering; its full text was not accessible for inspection. Brightwell, Janson, and Łuczak (2015, arXiv:1510.05560) study the large-order greedy independent-set law on random graphs with specified degrees, not exact kinetics for these two fixed graphs. Dhara, van Leeuwaarden, and Mukherjee (2016, arXiv:1604.03918) study generalized adsorption on Erdős–Rényi graphs and derive large-network jamming limits, not this finite-graph all-time inequality. These are pertinent model frameworks, not claimed discoveries here.

Published calculations of the independence complexes of \(GP(10,2)\) and \(GP(10,3)\) evaluate static topological invariants of independent sets, including their face counts. Such counts do not assign probabilities to greedy histories and do not imply either the exact kinetic Bernstein coefficients or the all-time inequality; those published static results are not claimed as new. Semantic and literal literature searches found no explicit evaluated comparison that implies the assertion, but unsuccessful searches do not prove absolute priority.

## Limitations
The result concerns exactly two twenty-site cubic networks and the stated independent-rate irreversible monomer process. It does not claim a general ordering between graphs of different girth, bipartite and non-bipartite cubic graphs, or entire generalized-Petersen families. Its coefficientwise proof relies on complete finite integer enumeration with replayable code rather than a closed symbolic formula for the sixteen positive coefficients. The foundational 1989 source could not be read in full, and unindexed finite-graph adsorption computations could exist. No independent external audit has been performed.

## References
1. G. Brightwell, S. Janson, and M. Łuczak, *The greedy independent set in a random graph with given degrees*, arXiv:1510.05560, first public 2015-10-19, https://arxiv.org/abs/1510.05560.
2. S. Dhara, J. S. H. van Leeuwaarden, and D. Mukherjee, *Generalized random sequential adsorption on Erdős–Rényi random graphs*, arXiv:1604.03918, first public 2016-04-13, https://arxiv.org/abs/1604.03918.
3. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, https://doi.org/10.1137/0402034 (full text not inspected).
4. *The dodecahedral independence complex is a wedge of four 5-spheres*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-dodecahedral-independence-complex-is-a-wedge-of-four-5-spher--ba0161fd495f.
5. *The Desargues independence complex is \(S^4\vee\bigvee^5S^5\)*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-independence-complex-is-s-4-vee-bigvee-5-s-5--e9aae0fc2563.
