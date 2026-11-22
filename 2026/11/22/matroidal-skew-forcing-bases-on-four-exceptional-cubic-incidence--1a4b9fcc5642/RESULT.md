# Matroidal skew-forcing bases on four exceptional cubic incidence graphs

## Finding

Let \(H\), \(M\), \(P\), and \(D\) respectively be the Heawood, Möbius–Kantor, Pappus, and Desargues graphs, with the concrete vertex and edge models given below. A skew-zero-forcing set is a set of initially black vertices from which the rule *any vertex having exactly one white neighbor colors that neighbor black* eventually colors every vertex black. Count all such initial sets by \(F_G(z)=\sum_S z^{|S|}\).

For these four graphs, the **complete** forcing polynomials factor as \(F_G(z)=Q_G(z)^2\), where

\[
\begin{aligned}
Q_H(z)&=28z^3+35z^4+21z^5+7z^6+z^7,\\
Q_M(z)&=48z^3+70z^4+56z^5+28z^6+8z^7+z^8,\\
Q_P(z)&=72z^3+126z^4+126z^5+84z^6+36z^7+9z^8+z^9,\\
Q_D(z)&=125z^4+222z^5+205z^6+120z^7+45z^8+10z^9+z^{10}.
\end{aligned}
\]

In particular, the minimum skew-zero-forcing numbers are \((6,6,6,8)\), with respectively \((784,2304,5184,15625)\) distinct optimal sets. Each graph's optimal sets are exactly the bases of a direct sum of two isomorphic matroids: rank-three Fano, rank-three Möbius–Kantor sparse-paving, rank-three affine-plane, and rank-four graphic matroids, respectively. For \(D\), an optimum is precisely a pair of spanning trees of \(K_5\), one on each incidence shore. For \(P\), the forbidden initial three-sets on a shore recover all twelve lines of \(\operatorname{AG}(2,3)\), including the missing parallel class of the defining nine-line configuration.

Let \(\mathcal R_{\rm TJ}(G)\) be the graph on minimum forcing sets with edges for replacement of one selected vertex by an arbitrary unselected vertex. Let \(\mathcal R_{\rm TS}(G)\) impose the further condition that the exchanged vertices are adjacent in \(G\). The jump graphs are the Cartesian squares of the corresponding one-shore matroid basis-exchange graphs, with the following *exact* metrics:

| Graph | Jump vertices | Jump edges | Jump radius | Jump diameter | Slide edges |
|---|---:|---:|---:|---:|---:|
| Heawood | 784 | 7,056 | 6 | 6 | 0 |
| Möbius–Kantor | 2,304 | 28,800 | 6 | 6 | 0 |
| Pappus | 5,184 | 77,760 | 6 | 6 | 0 |
| Desargues | 15,625 | 232,500 | 6 | 8 | 0 |

For Desargues the jump-graph eccentricity distribution is exactly 25 configurations of eccentricity six, 1,200 of eccentricity seven, and 14,400 of eccentricity eight. In all four cases, every pair of optima can be linked by the minimum possible number of one-vertex jumps, namely the number of vertices selected in the starting configuration but not the target configuration.

## Assumptions and scope

All graphs are finite, simple and labelled, with one forcing set counted once as a subset of the vertex set (there is no quotient by graph automorphisms). All set and graph counts are exact integers. The models are as follows.

1. \(H\): vertices \(p_i,\ell_j\) indexed by \(i,j\in\mathbb Z/7\mathbb Z\), with \(p_i\ell_j\) an edge exactly when \(j-i\in\{0,1,3\}\).
2. \(M\): the generalized Petersen graph \(GP(8,3)\), with \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\) as edges, indices modulo eight.
3. \(P\): points \((x,y)\in\mathbb F_3^2\), together with the nine lines \(x=c\), \(y=c\), \(y-x=c\), for \(c\in\mathbb F_3\); edges represent incidence.
4. \(D\): the 2-subsets and 3-subsets of a fixed five-element set, with containment edges.

The two bipartition shores in each model each have \(m=7,8,9,10\) vertices, respectively. For the Desargues graph, the 3-subset shore can be identified with the 2-subset shore by complementation. We consider ordinary skew forcing, not standard zero forcing or positive-semidefinite forcing. Forcing is irreversible, and a forcing vertex may itself be white.

## Proof

**1. Bipartite decomposition.** Let \(G\) be any bipartite graph with shores \(A,B\). A vertex in \(B\) can only force a vertex in \(A\); whether this force is available depends entirely on the current white vertices of \(A\), not the colors of vertices in \(B\). Symmetrically, vertices in \(A\) force only those in \(B\), depending entirely on the white vertices of \(B\). Every forced color persists. Consequently the two shore processes can be completed independently, and \(S\subseteq V(G)\) is skew forcing exactly when both \(S\cap A\) and \(S\cap B\) complete their respective shore processes. Hence \(F_G(z)=Q_A(z)Q_B(z)\), with the two factors equal in the four models through shore symmetry.

**2. Three small incidence configurations.** An exhaustive finite shore check establishes, separately on both shores of \(H,M,P\), that no black starting set of size at most two forces its shore, and all starting sets with four or more vertices do. Among three-sets, precisely \(7,8,12\), respectively, fail. More sharply, for \(H\) those seven nonforcing triples are the seven opposite-shore neighborhoods (Fano lines); for \(M\) the eight nonforcing triples are its eight opposite-shore neighborhoods (the linear \(8_3\) configuration); and for \(P\) they form the twelve lines of \(\operatorname{AG}(2,3)\) on each shore. On the point shore of \(P\), the nine original blocks are supplemented by \(y+x=c\) for \(c\in\mathbb F_3\). On the line shore (ordered by \(x=0,1,2\), \(y=0,1,2\), \(y-x=0,1,2\)), the index permutation \((0,1,2,3,5,4,6,7,8)\) carries the nonforcing triple system to the standard affine-plane line system. This is an explicit finite comparison, not an appeal to a numerical guess. Both independent verifiers enumerate each of the at most \(2^9\) one-shore subsets, and the Python verifier checks these geometric descriptions.

The forbidden triples in each case are pairwise disjoint on any chosen pair, so no four-set can have all its contained triples forbidden; adding black vertices cannot obstruct successful forcing. Therefore every set of size at least four works. The complete one-shore polynomials are \(Q_G(z)=(1+z)^m-1-mz-\binom m2z^2-bz^3\), with \((m,b)=(7,7),(8,8),(9,12)\). The forcing triples are the bases of the rank-three matroids described above; the sparse-paving property in the eight-element case follows from distinct forbidden triples intersecting in at most one element.

**3. Desargues has a graphic-matroid closure.** Identify a shore vertex (a two-element subset) with an edge of \(K_5\). Its opposite-shore vertices are all triples of ground elements, hence all edge-triangles of \(K_5\). A triangle with exactly one white edge permits precisely the rule of adding the third edge to an already black two-edge path. This closure never joins different initially black connected components; within each connected component, repeated path-shortening by such additions fills all missing edges. Thus one shore becomes entirely black **if and only if** the graph of its initially black edges is connected on all five ground vertices. The other shore has the same property by complementation. A minimum connected edge set has four edges and is a spanning tree, of which \(K_5\) has \(5^3=125\). Counting connected labelled five-vertex graphs by edges gives \(Q_D\) above. A self-contained coefficient recurrence is obtained by separating the connected component containing a distinguished vertex: \(C_1(z)=1\), and for \(n\ge2\),
\[
C_n(z)=(1+z)^{\binom n2}-\sum_{j=1}^{n-1}\binom{n-1}{j-1}C_j(z)(1+z)^{\binom{n-j}{2}}.
\]
Here \(Q_D(z)=C_5(z)\). This also proves that all minimum shore forcing sets are precisely the bases of the graphic matroid of \(K_5\).

**4. Exchange geometry and radii.** In a matroid basis graph, exchanging a basis element always permits a shortest sequence transforming any basis \(X\) into another basis \(Y\) in exactly \(|X\setminus Y|\) steps, by the basis-exchange axiom. The independent shore processes and fixed minimum cardinalities force every minimum whole-graph set to use exactly the minimum number on *each* shore. Thus every one-token jump changes only one shore, yielding the Cartesian-product basis graph and the asserted exact distance formula. No token slide preserves these minimum shore cardinalities, because all edges of the original graph cross the bipartition. Therefore every minimum set is slide-frozen.

For the three rank-three matroids, the complement of each three-element basis contains another basis, so all one-shore eccentricities are three; their Cartesian squares are self-centered with radius and diameter six. In the Desargues shore, spanning trees \(T,T'\) have exchange distance \(|E(T)\setminus E(T')|\). The complement of a star has an isolated vertex and cannot contain a spanning tree, so the five stars have eccentricity three. Every other spanning tree has connected complement, hence an edge-disjoint spanning tree and eccentricity four. Taking the Cartesian square gives 25, 1,200, 14,400 eccentricities of six, seven, eight. The one-shore edge counts, respectively \(126,300,540,930\), are verified exhaustively; multiplying by twice the number of one-shore bases gives the four reported whole-graph jump-edge counts.

## Verification

Two standalone scripts are included. Run `python3 verify.py` and compile/run `c++ -std=c++17 -O2 verify.cpp -o verify && ./verify`. The Python script constructs all four graphs from their mathematical descriptions, exhausts every one-shore initial set, validates both shore polynomials, all minimum configurations, exceptional geometric triple systems, exact matroid-exchange distances, degree distributions and eccentricities. The C++17 program independently constructs all graphs, exhausts all \(2^{14}\), \(2^{16}\), \(2^{18}\), and \(2^{20}\) whole-graph initial subsets under the full skew rule, and matches every full cardinality coefficient with the separately enumerated shore convolutions. It also independently checks minimum-set exchange-graph connectivity, degrees, eccentricities and exact exchange distances. Both were executed successfully with their specified commands.

## Relationship to prior work

DeAlba's 2014 preprint defines skew zero forcing and proves a matroid description for a conditional family of bipartite graphs whose maximum matchings are all uniquely restricted. The four cubic graphs here have multiple perfect matchings and alternating cycles, so they do not satisfy that sufficient hypothesis. The current result instead identifies graphic and rank-three matroid base families through the concrete incidence geometries and gives full polynomial and exchange classifications. Kutnar and Marušič's classification distinguishes the four exceptional cubic symmetric girth-six graphs but addresses graph symmetry rather than skew forcing. Bong and coauthors' 2025 primary preprint studies general skew-forcing reconfiguration, including cycles, complete graphs, baskets, and trees, and contains no theorem yielding these four matroid-basis identifications or exact enumerators. Indexed work on skew forcing of crown and book graphs has distinct graph families; work on ordinary forcing for these four graphs has a stricter rule and does not imply the present quantities. The earlier general framework and graph classification are credited rather than presented as new.

## Limitations

The theorem concerns the four explicitly defined graphs only; it does not establish a general classification of all cubic symmetric graphs or of all bipartite skew-forcing matroids. The numerical portions use finite exhaustive certificates, not extrapolation from samples. The underlying one-shore classification is proven for these exact small objects; it has not been extended to arbitrary incidence configurations. Published-literature priority was investigated with available indexed and primary sources but cannot be guaranteed against inaccessible or unindexed treatments. Independent scholarly validation has not been performed.

## References

- L. M. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number*, first arXiv version dated 6 April 2014, arXiv:1404.1618, https://arxiv.org/abs/1404.1618.
- K. Kutnar and D. Marušič, *A complete classification of cubic symmetric graphs of girth 6*, Journal of Combinatorial Theory, Series B 99 (2009), 162–184, https://doi.org/10.1016/j.jctb.2008.06.001.
- N. Bong et al., *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642 (2025), https://arxiv.org/abs/2501.03642.
