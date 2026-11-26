# The 72-phase Möbius–Kantor majority attractor and its nine basin strata

## Finding

For synchronous binary strict-neighbor majority on the Möbius–Kantor graph, the global update \(F\) obeys the sharp identity \(F^5=F^3\), and its recurrent configurations form a 72-by-72 two-shore phase space. There are exactly **72 fixed configurations** and **2,556 primitive temporal two-cycle orbits**. Every one of the \(2^{16}=65,536\) labelled initial configurations is periodic after at most three updates, and some require exactly three.

The **complete individual attraction-basin spectrum**, where each basin includes every initial labelled configuration eventually reaching the corresponding temporal orbit, is:

| Attractor | Basin size | Number of distinct temporal orbits |
|---|---:|---:|
| Fixed point | 1 | 22 |
| Fixed point | 4 | 48 |
| Fixed point | 4,761 | 2 |
| Primitive two-cycle | 2 | 231 |
| Primitive two-cycle | 4 | 1,056 |
| Primitive two-cycle | 8 | 1,128 |
| Primitive two-cycle | 138 | 44 |
| Primitive two-cycle | 276 | 96 |
| Primitive two-cycle | 9,522 | 1 |

The counts of states whose *first* periodic time is \(t=0,1,2,3\) are respectively \(5,184,15,552,22,528,22,272\). In particular, the two consensus fixed points each have basin size \(4,761=69^2\), and the two-cycle between the unanimous phases has basin size \(9,522\), their sum. There is no other nontrivial period.

## Assumptions and scope

Write the labelled sixteen vertices as \(o_i\) and \(p_i\), with \(i\in\mathbb Z/8\mathbb Z\). The graph is the simple generalized Petersen graph \(\operatorname{GP}(8,3)\), with exactly the 24 undirected edges \(o_io_{i+1}\), \(o_ip_i\), and \(p_ip_{i+3}\), for each \(i\). A vertex with three neighbors is updated to one if at least two of those neighbors are one, and to zero otherwise. Every vertex updates simultaneously. The two global unanimous assignments are fixed. All configurations, attractors and basins use labelled vertex assignments; no spatial rotations, automorphisms, complementation or isomorphism are quotiented out. Only the two temporal phases of one primitive two-cycle are identified as a single temporal orbit.

The graph is bipartite, with shores \(U=(o_0,o_2,o_4,o_6,p_1,p_3,p_5,p_7)\) and \(V=(o_1,o_3,o_5,o_7,p_0,p_2,p_4,p_6)\). Each shore has eight vertices; 8-bit strings are interpreted in the specified order.

## Proof

**Step 1: exact phase maps.** For an 8-bit word \(u\) on \(U\), define \(h(u)\) on \(V\) by taking the three-neighbor majority at each vertex of \(V\). Define \(g(v)\) on \(U\) similarly for \(v\) on \(V\). The full synchronous update is precisely
\[
F(u,v)=(g(v),h(u)).
\]
Put \(P=g\circ h\) and \(Q=h\circ g\). Then \(F^2(u,v)=(P(u),Q(v))\). Each map is a completely defined Boolean function on the 256 8-bit words; no probabilistic or numerical approximation is involved.

**Step 2: finite phase-table certificate.** Exhaustively evaluate these 256 inputs from the explicit 24-edge definition. The reproducible `check_projection.py` tests all 256 inputs and establishes these exact identities and cardinalities:
\[
\begin{gathered}
|\operatorname{im}h|=|\operatorname{im}g|=136,\\
|\operatorname{im}P|=|\operatorname{im}Q|=88,\\
|\operatorname{im}P^2|=|\operatorname{im}Q^2|=72,\\
P^3=P^2,\quad Q^3=Q^2,\\
P^2\circ g=P\circ g,\quad Q^2\circ h=Q\circ h.
\end{gathered}
\]
Both images \(S_U=\operatorname{im}P^2\) and \(S_V=\operatorname{im}Q^2\) are fixed pointwise by \(P,Q\), respectively. The restricted maps \(h:S_U\to S_V\) and \(g:S_V\to S_U\) are mutual inverses. The exact fiber size distribution of the retraction \(P^2\) is **22 targets of weight one, 48 targets of weight two, and two targets of weight 69**; the same holds for \(Q^2\). Furthermore, for every \(s\in S_U\), the fiber weights agree under the bijection: \(|(P^2)^{-1}(s)|=|(Q^2)^{-1}(h(s))|\). These are 256-element exhaustive identities, not extrapolations from sample lengths.

**Step 3: recurrent configurations and temporal cycles.** The recurrent subset is exactly \(S_U\times S_V\), because \(F^2=(P,Q)\) and each projected factor is fixed pointwise on its 72-element image. On that subset, use the coordinate change \((u,v)\mapsto(u,g(v))\), so the update becomes \((a,b)\mapsto(b,a)\) on \(S_U\times S_U\). Hence exactly 72 diagonal pairs are fixed and the remaining \(72^2-72\) states form \((72^2-72)/2=2,556\) temporal two-cycles. The identities \(P^2\circ g=P\circ g\) and \(Q^2\circ h=Q\circ h\) imply \(F^5=F^3\) for every input. There are inputs with first entry time three, as certified independently below, so the bound is sharp.

**Step 4: full basin sizes.** Iterating four times maps \((u,v)\) to \((P^2(u),Q^2(v))\), the periodic phase destination. If two phase symbols \(a,b\in S_U\) have fiber sizes \(m(a),m(b)\) under \(P^2\), their diagonal fixed attractor has basin size \(m(a)^2\), and their unordered two-cycle \(\{a,b\}\), with \(a\neq b\), has basin size \(2m(a)m(b)\), by the corresponding two disjoint product fibers under \(F^4\). Substituting the exact 22/48/2 fiber multiplicities at weights 1/2/69 gives all nine rows in the finding. For example, the two large weights produce a single two-cycle basin \(2\cdot69^2=9,522\); the 22-by-48 combinations give 1,056 two-cycles of basin size four. Summing basin size times orbit count gives exactly 65,536, ruling out unaccounted initial states.

**Step 5: first-entry times.** The same 256-by-256 phase-pair enumeration tests \(F^{t+2}(x)=F^t(x)\) at \(t=0,1,2,3\) and first-occurrence counting gives \((5,184,15,552,22,528,22,272)\). These values sum to all 65,536 configurations and the positive final entry shell proves sharpness. The independent full-configuration checker directly enumerates all 65,536 states and obtains the same result by an unrelated functional-digraph decomposition.

## Verification

The two necessary self-contained source files are `check_projection.py` (Python 3, standard library only) and `check_direct.cpp` (C++17, standard library). From their containing directory run:

```sh
python3 check_projection.py
c++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct
./check_direct
```

Their assertion-checked terminating markers are `PROJECTION_CERTIFICATE_OK` and `DIRECT_CENSUS_OK`. The Python program independently builds the two-shore Boolean projection from incidence and verifies every finite phase claim, including target-specific basin fibers and first-entry counts. The C++ program independently constructs the 24 edges, evaluates all 65,536 full configurations, removes transient functional-digraph vertices by indegree peeling, reconstructs all cycle basins in reverse topological order and verifies the nine numerical classes and sharp transient. Both programs were executed successfully on the accompanying source files. The program sources, not detached historical logs, form the exact reproducible finite certificates.

## Relationship to prior work

The theorem that synchronous symmetric finite threshold systems eventually reach periods at most two is classical (Goles–Olivos, 1980). Adam, Dahleh and Ozdaglar (first arXiv public version 2012-11-04, Sections 4 and 6) prove a general bipartite expansion and the recurrent orbit-count identity for bipartite networks. These results already imply the counting relationship between 72 fixed points and 2,556 two-cycles *once the 72 is known*: neither the general period bound nor that elementary implication is asserted as new here.

Published exact censuses on the Heawood graph (the seven-point Fano configuration) and the 20-vertex Desargues graph likewise illustrate bipartite phase decompositions, but their graphs have different incidence relations and different one-shore fiber distributions. In particular, the Heawood projection has two fibers of weight 36 and 56 singleton fibers, rather than the present 22/48/2 distribution at weights 1/2/69. Their formulas do not determine the nine basin classes above. The distinctive contribution is the **complete specific 8-point Möbius–Kantor incidence projection and individual-basin spectrum**, including the exact three-update bound.

## Limitations

The claim is an exact finite graph classification, not a universal theorem for all cubic bipartite graphs or generalized Petersen graphs. It concerns strict open-neighbor majority only, not noisy, self-inclusive or asynchronous majority. The finite certificates exhaust the explicitly specified finite domain; they do not provide independent external mathematical validation. Searches of indexed literature and selected closely related published results did not identify a prior equivalent Möbius–Kantor basin tabulation; unindexed equivalent work remains possible. The known general bipartite orbit-count relation cannot itself be counted as novel.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1 .
2. E. M. Adam, M. A. Dahleh and A. Ozdaglar, *On Threshold Models over Finite Networks*, first publicly posted 2012-11-04, arXiv:1211.0654, Sections 4, 6. https://arxiv.org/html/1211.0654v2 .
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first posted 2014-05-11, arXiv:1405.2486. https://arxiv.org/html/1405.2486v1 .
4. H. S. M. Coxeter, *Self-Dual Configurations and Regular Graphs*, Bulletin of the American Mathematical Society 56 (1950), 413–455; graph background. https://mathworld.wolfram.com/Moebius-KantorConfiguration.html .
5. *A two-step majority projection and exact attraction basins on the Heawood graph*, published 2026, publicly available exact graph-specific census. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93 .
6. *Exact attraction-basin spectrum for binary majority dynamics on the Desargues graph*, publicly available 2026 exact finite-graph census (20-vertex graph); distinct object and basin values.
