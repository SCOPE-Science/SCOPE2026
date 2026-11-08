# Two sharp degree-rule failure thresholds in unweighted habitat capacity

## Finding

Let \(G\) be a connected simple undirected graph of \(n\ge2\) equal-quality habitat patches. Each corridor contributes unit symmetric exchange and no patch has self-exchange; the landscape matrix is exactly the adjacency matrix \(A(G)\). The spectral metapopulation-capacity proxy is \(\Lambda(G)=\rho(A(G))\). If patch \(v\) is permanently lost, the remaining capacity is \(R_G(v)=\rho(A(G-v))\). A most-damaging patch loss minimizes \(R_G(v)\); a degree-only screening rule chooses a maximum-degree vertex of \(G\).

**Theorem (complete first two failure layers).**

1. For every connected graph with \(2\le n\le4\), **every** maximum-degree vertex is a most-damaging patch to lose.
2. For every connected five-vertex graph, **some** maximum-degree vertex is most damaging, but arbitrary tie-breaking can fail. Exactly three isomorphism classes exhibit a non-optimal maximum-degree choice; their numbers of labelled realizations are \(60,60,30\), respectively.
3. Six is the **smallest** number of patches for which **no** maximum-degree vertex need be most damaging. Among all connected six-vertex graphs, exactly two isomorphism classes have this property, accounting for \(180\) and \(360\) labelled graphs. All other connected six-vertex classes have a maximum-degree optimum.

A representative of the first six-vertex class has vertices \(0,\ldots,5\) and edges
\[
\{01,02,04,05,12,13,23\}.
\]
The unique maximum-degree vertex is \(0\), with \(R_G(0)=2\). Instead, deleting vertex \(1\) or \(2\) leaves capacity
\[
R_G(1)=R_G(2)=\sqrt{2+\sqrt 2}<2.
\]

A representative of the second class has edges
\[
\{02,03,04,05,12,13,14,23\}.
\]
Its unique maximum-degree vertex is \(0\). Its residual capacity is the largest real root \(r\) of
\[
r^3-r^2-3r+1=0,\qquad 2.17<r<2.18.
\]
Deleting vertex \(2\) or \(3\), each of degree three rather than four, instead gives
\[
R_G(2)=R_G(3)=\sqrt{(5+\sqrt{17})/2}\in(2.13,2.14).
\]
Both inequalities are strict. These are **capacity rankings in a deliberately simplified network model**, not quantified extinction probabilities or universal prescriptions for real landscapes.

## Assumptions and scope

All edges are unweighted, undirected and simultaneous; the effective exchange matrix has zeros on the diagonal. All patches have equal quality, and intervention means removing exactly one vertex with all incident edges. The graph is connected before loss but need not remain connected after loss. Spectrum means the largest real eigenvalue of a symmetric matrix; it is zero for an edgeless residual graph. The threshold statements exhaust orders \(2\) through \(6\), with no claim about full classification beyond six, weighted corridors or more than one removal.

## Proof

Fix \(n\in\{2,3,4,5,6\}\). There are \(\binom n2\) potential undirected edges. Encode every labelled simple graph by an integer \(m\) between \(0\) and \(2^{\binom n2}-1\), whose bits choose the edges \((i,j)\), listed in lexicographic order. A breadth-first search from vertex \(0\) decides connectivity exactly; no graph is omitted. In every connected graph compute all vertex degrees and each induced residual \(G-v\).

For a residual on at most five vertices compute its characteristic polynomial \(f_v(x)=\det(xI-A(G-v))\) in exact integer arithmetic. Since the adjacency matrix is symmetric, all roots are real. A rational root-isolation algorithm supplies a guaranteed interval of width at most \(10^{-9}\) containing the greatest real root. For distinct intervals, the ordering is certified by rational comparison; if intervals overlap, a polynomial greatest-common-divisor computation establishes whether the two greatest roots coincide. Overlap without a certified common root aborts the computation. Thus all comparisons of the \(R_G(v)\) values are exact, not floating-point approximations.

Define \(M_G\) to be the maximum-degree vertex set and \(O_G=\operatorname*{argmin}_v R_G(v)\). Test the two independent statements \(M_G\subseteq O_G\) (tie-breaking never fails) and \(M_G\cap O_G\ne\varnothing\) (at least one maximum-degree optimum). The exhaustive connected labelled counts for \(n=2,3,4,5,6\) are, respectively, \(1,4,38,728,26704\). Their corresponding failure counts for \(M_G\subseteq O_G\) are \(0,0,0,150,7740\), and for \(M_G\cap O_G\ne\varnothing\) are \(0,0,0,0,540\). Every failure at \(n=5\) and every complete failure at \(n=6\) is mapped to its minimum edge-mask representative under all \(n!\) vertex permutations. At five vertices the 150 labelled failures partition into exactly three orbits of sizes \(60,60,30\). At six vertices the 540 complete failures partition into exactly two orbits of sizes \(180,360\), with representatives above. This is a finite exhaustive proof: every candidate edge set is checked, each eigenvalue ordering is certified symbolically, and equivalence of graphs is checked by exhaustive permutation.

For transparency, the first witness has the residual characteristic polynomials \(x^2(x-2)(x+1)^2\) at the degree-four vertex and \(x(x^4-4x^2+2)\) at either optimum degree-three vertex. The second witness has \(x(x+1)(x^3-x^2-3x+1)\) at its degree-four vertex and \(x(x^4-5x^2+2)\) at either optimum degree-three vertex. Root isolation determines the full optimal sets, not merely these comparisons.

## Verification

Run `python checker.py` with a Python 3 interpreter and SymPy installed. It performs all labelled-graph connectivity tests, exact integer characteristic-polynomial computations, certified rational root comparisons, exhaustive vertex-permutation isomorphism reduction, and the two explicit-witness checks. It prints JSON that must match `COUNTS.json` byte-for-byte on the same SymPy serialization behavior; the salient exact counts are stated in the proof. The script has assertions for each layer and stops on an undecidable root comparison. In particular the counts at six vertices refer to **all** \(2^{15}=32768\) labelled simple graphs, including 26704 connected ones, not to a sampling experiment.

## Relationship to prior work

Hanski and Ovaskainen (2000) introduced leading-eigenvalue metapopulation capacity and habitat-loss comparisons. Ovaskainen (2003) developed general eigenvalue/eigenvector relations for deleting patches; those identities motivate the loss problem but do not, in accessible material, specify the complete degree-heuristic exception layers on five and six equal-weight patches. Saha et al. (first public preprint 2015) study graph spectral-radius reduction by node removal and show limitations of degree-based intervention heuristics, but the inspected full text concerns general algorithms and large-network performance, not the smallest orders and full isomorphism-class census here. The result therefore establishes a finite exact boundary within the restricted unweighted model; it does **not** claim discovery of degree heuristics or of the general fact that degree can be misleading.

## Limitations

A six-patch cutoff in this equal-weight adjacency model cannot be transferred unchanged to spatially decaying connections, weighted patch areas, directed dispersal, or detailed occupancy Markov chains. A static spectral radius is a persistence-capacity proxy, not a probability that a real species persists after patch loss. General perturbation formulas already exist, and published graph-spectral optimization work may imply isolated counterexamples; independent historical-priority assessment remains necessary. The full texts of the most relevant 2000 and 2003 metapopulation papers were inaccessible at this examination: their public abstracts/figures and metadata, rather than unseen content, were compared. The accessible full text of the 2015 spectral intervention paper was inspected. Exhaustive computation establishes the stated finite domain only; it is not an analytic theorem for all graph orders.

## References

1. Hanski, I., and Ovaskainen, O., *The metapopulation capacity of a fragmented landscape*, Nature 404 (2000), 755–758. DOI: https://doi.org/10.1038/35008063 (public April 13, 2000).
2. Ovaskainen, O., *Habitat destruction, habitat restoration and eigenvector–eigenvalue relations*, Mathematical Biosciences 181 (2003), 165–176. DOI: https://doi.org/10.1016/S0025-5564(02)00150-5.
3. Saha, S., Adiga, A., Prakash, B. A., and Vullikanti, A. K. S., *Approximation Algorithms for Reducing the Spectral Radius to Control Epidemic Spread*, arXiv:1501.06614 (first version January 26, 2015). https://arxiv.org/abs/1501.06614.
