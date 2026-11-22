# Three two-edge paths classify minimum locating-total codes of the Petersen line graph

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph and let \(H=L(P)\) be its line graph, whose 15 vertices correspond to the edges of \(P\). A subset \(S\subseteq E(P)\) is a locating-total edge code if (i) every edge of \(P\), including a selected edge, is adjacent to a *different* selected edge, and (ii) the selected-edge neighbourhoods of all edges outside \(S\) are distinct. Equivalently, \(S\) is a locating-total dominating set in \(H\).

**Theorem.** The locating-total domination number of \(H\) equals \(6\). There are precisely \(110\) minimum codes. A six-edge subset \(S\) is such a code **if and only if** its selected-edge spanning subgraph on the ten vertices of \(P\) is \(3P_3\sqcup K_1\), a disjoint union of three two-edge paths and one isolated vertex. Exactly \(11\) of the codes isolate each prescribed vertex of \(P\). The natural automorphism group \(\operatorname{Aut}(P)\cong S_5\) acts on the \(110\) optima in precisely three orbits, of respective sizes \(10,40,60\).

The complete cardinality enumerator of locating-total codes in \(H\), with each vertex subset counted once, is
\[
\begin{aligned}
T_H(z)={}&110z^6+1590z^7+3810z^8+4150z^9\\
&+2838z^{10}+1350z^{11}+455z^{12}\\
&+105z^{13}+15z^{14}+z^{15}.
\end{aligned}
\]
The fixed-cardinality reconfiguration graph \(\mathcal R\), whose vertices are the \(110\) minimum codes and whose edges replace one selected edge of \(P\) by one unselected edge while retaining optimality, is connected with \(210\) edges, radius \(6\), and diameter \(7\). The three symmetry orbits have exchange degrees \(6,3,4\) respectively (for sizes \(10,40,60\)); their distance profiles, at distances starting with zero, are respectively
\[
(1,6,12,18,28,24,18,3),\quad
(1,3,9,21,32,36,6,2),\quad
(1,4,10,21,32,27,15).
\]
In particular, the third orbit has eccentricity \(6\); the other two have eccentricity \(7\).

## Assumptions and scope
All graphs are finite simple graphs. Write \(N_H(v)\) for the *open* neighbourhood, excluding \(v\) itself. For any \(S\subseteq V(H)\), the formal predicate is
\[
\left(\forall v\in V(H):N_H(v)\cap S\ne\varnothing\right)
\quad\land\quad
\left(\forall u\ne v\in V(H)\setminus S:
N_H(u)\cap S\ne N_H(v)\cap S\right).
\]
The identifying signatures are only compared for vertices **outside** the code; the total-domination requirement applies to all vertices. The underlying Petersen model has the ten 2-subsets of \(\{0,1,2,3,4\}\), with adjacency exactly for disjoint pairs. The line graph has fifteen vertices, each of degree four. All counts refer to literally labelled subsets of those fifteen vertices, not counts modulo automorphisms. An exchange move changes exactly one selected line-graph vertex while maintaining the same cardinality and predicate.

## Proof
**Girth and structural sufficiency.** The Petersen graph has girth five. More generally, in any graph with girth at least four, suppose a selected-edge set spans vertex-disjoint two-edge paths together with *at most one* isolated original vertex, with no other vertices. Each original vertex in a path carries its incident selected-edge label: the center has a two-element set of labels and each leaf has a unique singleton label. These nonempty label sets are pairwise different; the label families of distinct paths are disjoint. An isolated vertex has an empty label set and is unique if present. Every selected edge touches its mate in its path, so total domination holds. An unselected edge cannot have endpoints in a single path, because the only missing edge joining two vertices of a path would close a triangle; it cannot join two isolated vertices because there is at most one. Consequently its open selected-neighbourhood signature is the union of the endpoint label sets from two distinct components and is nonempty. That disjoint component decomposition uniquely reconstructs both endpoints from the signature, hence distinct unselected edges have distinct signatures. Thus every selected-edge \(3P_3\sqcup K_1\) factor in \(P\) is a locating-total edge code.

**Exhaustive necessity, optimality, and counts.** The two included independent programs construct the ten-vertex Petersen graph from (a) disjoint pairs of a five-element set and (b) the ten vertices and fifteen edges of \(\operatorname{GP}(5,2)\). An explicit vertex bijection is checked edge-by-edge, ensuring the models agree. Each program constructs all fifteen open line-graph neighbourhoods. Each inspects **every** subset among the \(2^{15}=32768\) subsets, computes whether all vertices have a selected neighbour, and whether all unselected vertices have pairwise distinct selected-neighbourhood bitsets. The resulting size histogram is precisely the displayed polynomial; in particular there are no solutions of size at most five, and there are 110 of size six. Both implementations further check the equivalence of the predicate and the \(3P_3\sqcup K_1\) condition for **each** of the \(\binom{15}{6}=5005\) possible six-edge subsets. This proves the necessity as a finite exhaustive lemma; it is not an extrapolation from random trials or from a smaller domain.

**Symmetry, isolated-vertex balance, and exchange geometry.** The first verifier constructs every one of the \(5!=120\) permutations of the five Kneser symbols and takes induced images of all 110 codes. This exhausts the natural \(S_5\) action and gives orbit sizes 10, 40 and 60. Every optimum covers exactly nine of the Petersen vertices with selected edges. Counting the omitted vertex gives eleven codes for each of its ten possible values. The exchange graph is built by testing every removal of a selected edge and addition of an unselected edge among the 110 optimal codes, so its 210 edges are exhaustive. Separate breadth-first searches from **all 110** code states establish connectivity, the three indicated orbit distance profiles and all eccentricities, yielding radius six and diameter seven. The second verifier independently reconstructs the exchange edges and reruns all breadth-first searches in the generalized-Petersen model; it agrees on every aggregate.

## Verification
Run `python3 verify_subset.py` in a Python 3 standard-library environment. It ends in `PASS_PETERSEN_LINE_LTD_SET_32768` and prints the coefficient array, orbit profiles, and exact exchange statistics. Independently run `g++ -std=c++17 -O2 verify_petersen_gp.cpp -o verify_petersen_gp && ./verify_petersen_gp`; it ends in `PASS_PETERSEN_LINE_LTD_GP_32768`. Both programs enumerate all 32768 subsets; the Python checker additionally inspects all group actions, and both check every six-edge subset and the full exchange distance matrix. Their exact, transparent finite search bounds can be verified directly in the supplied source. All quantitative assertions in the Finding section appear as explicit assertions in these programs.

## Relationship to prior work
Foucaud and Henning, *Location-domination in line graphs* (first publicly posted 2015-06-08, arXiv:1506.02623), define and study precisely the locating-total domination predicate on line graphs, deriving general inequalities (including a two-thirds-order bound) rather than a Petersen-specific minimum, all optimum configurations or exact polynomial. The present size-six calculation is not a consequence of those general inequalities.

Foucaud, Gravier, Naserasr, Parreau and Valicov, *Identifying codes in line graphs* (first public 2011-07-01, arXiv:1107.0207), exhibit a five-edge perfect matching as an optimal **closed-neighbourhood edge-identifying code** on the Petersen graph. Identifying codes use closed-neighbourhood signatures on **all** vertices, whereas locating-total codes require **open** domination of selected vertices and separation only of unselected vertices. In particular, the five edges of a perfect matching have no selected-edge neighbours, so this earlier construction is not a locating-total code and does not imply the new classification.

An exact publicly available enumeration of **ordinary** locating-dominating sets of \(L(P)\) gives 246 minimum five-sets and an exchange graph on those sets. It explicitly imposes no requirement that chosen vertices themselves be dominated. Accordingly, its count and reconfiguration conclusions do not imply the 110 six-sets, the forced three-path decomposition, or the 210-edge exchange graph here. The complete claim and close equivalent formulations were also compared against available mathematical records; no covering statement was identified.

## Limitations
The exact finite enumeration is a computer-assisted proof whose trust ultimately depends on two separately constructed and inspectable programs, their graph representations and standard computation semantics. The structural sufficiency lemma does not by itself classify every six-edge code; the necessity and finite exchange distances rely on exhaustive checking of a fully specified finite universe. There is no claim about arbitrary cubic graphs, other generalized Petersen graphs or asymptotic behaviour. Although multiple relevant sources were compared on their substantive predicates, unindexed earlier computational tables could in principle duplicate the finite enumeration. No independent scholarly audit has been performed.

## References
- F. Foucaud, M. A. Henning, *Location-domination in line graphs*, arXiv:1506.02623, first publicly posted 2015-06-08, https://arxiv.org/abs/1506.02623.
- F. Foucaud, S. Gravier, R. Naserasr, A. Parreau, P. Valicov, *Identifying codes in line graphs*, arXiv:1107.0207, first publicly posted 2011-07-01, https://arxiv.org/abs/1107.0207.
- *Petersen edge-location-domination: ten complete-bipartite obstructions to geodesic exchanges*, full public result at https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-petersen-edge-location-domination-ten-complete-bipartite-obstruc--5291df073dcf/RESULT.md (ordinary locating-domination, not locating-total domination).
