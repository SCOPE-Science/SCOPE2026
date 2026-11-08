# Paired-domination distinguishes two graphs with identical total-domination polynomials

## Finding
Let \(S\) be the Shrikhande graph on \(\mathbb Z_4^2\) with connection differences \(\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\}\), and let \(R=K_4\square K_4\) be the four-by-four rook graph. Both are connected, nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\). For any graph \(G\), define \(T_G(z)\) to count total-dominating vertex subsets by size and \(P_G(z)\) to count paired-dominating subsets by size. The latter subsets are dominating sets whose induced subgraph has a perfect matching.

The **total-domination polynomials coincide**:
\[
\begin{aligned}
T_S(z)=T_R(z)={}&80z^4+1056z^5+4768z^6+9520z^7+12150z^8\\
&+11280z^9+7992z^{10}+4368z^{11}+1820z^{12}\\
&+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]
The **paired-domination polynomials differ**, with exact values
\[
\begin{aligned}
P_S(z)={}&48z^4+4384z^6+12054z^8+7992z^{10}\\
&+1820z^{12}+120z^{14}+z^{16},\\
P_R(z)={}&80z^4+4464z^6+12150z^8+7992z^{10}\\
&+1820z^{12}+120z^{14}+z^{16}.
\end{aligned}
\]
In particular,
\[
\boxed{P_R(z)-P_S(z)=32z^4+80z^6+96z^8.}
\]
Both graphs have total and paired domination numbers equal to \(4\), but among their \(80\) minimum total-dominating sets, exactly \(48\) admit a perfect matching in \(S\), compared with all \(80\) in \(R\). The other \(32\) minimum total-dominating sets of \(S\) induce stars \(K_{1,3}\): precisely two centered at each vertex.

The new claim is this exact paired-domination census for \(S\), its structural four-vertex obstruction, and the resulting comparison. Neither the foundational paired-domination definition, the rook-graph polynomial from earlier work, nor the known open-neighborhood-incidence equivalence is claimed as new.

## Assumptions and scope
All graphs are finite, simple, and undirected. Identify \((a,b)\in\mathbb Z_4^2\) with the integer \(4a+b\). In \(S\), \((a,b)\) is adjacent to \((c,d)\) exactly when \((c-a,d-b)\) modulo four is one of the six connection differences above. In \(R\), two distinct coordinate pairs are adjacent exactly when they share a coordinate. We count labeled *subsets*, not sequences, and count a paired-dominating subset once even if its induced subgraph has several perfect matchings. A set \(D\) is total dominating if every vertex, including every selected vertex, has a selected neighbor. An induced perfect matching implies the latter condition, so paired domination can equivalently be tested by total domination together with induced perfect matchability. There is no assertion for other strongly regular graphs or larger parameters.

## Proof
**1. Open-neighborhood incidence gives equal total-domination polynomials.** Number both vertex sets by \(0,\ldots,15\) using \(4a+b\). Consider the following permutations of vertex indices:

```
p=[0,8,2,10,7,3,5,1,14,6,12,4,9,13,11,15]
q=[11,1,9,3,2,4,0,6,5,15,7,13,12,10,14,8]
```

Direct modular substitution in the two graph definitions verifies, for all \(0\le u,v<16\),
\[
 v\in N_S(u)\quad\Longleftrightarrow\quad q(v)\in N_R(p(u)).
\]
Thus the map \(D\mapsto q(D)\) is a bijection between their total-dominating subsets of each fixed size: the condition \(N_G(u)\cap D\ne\varnothing\) is preserved for every \(u\). This is a *neighborhood-incidence* isomorphism, not a graph isomorphism: the independent permutations of vertices and neighborhoods need not coincide. The certificate and verifier reproduce all \(256\) incidence comparisons.

**2. Minimum total domination and four-vertex sets.** For any four-vertex total-dominating set in \(R\), every row or every column must be occupied. Otherwise an intersection of an empty row and an empty column would have no selected neighbor. If every row is occupied, there is exactly one selected vertex in each row. Each selected vertex must then have a companion in its column, forcing column occupancy profile \((4)\) or \((2,2)\). There are \(4\) choices for profile \((4)\) and \(\binom42\binom42=36\) choices for profile \((2,2)\), giving \(40\) such sets. The analogous count for the all-columns condition contributes \(40\) disjoint additional sets. There are no smaller total-dominating sets, because with fewer than four selected vertices there is both an empty row and an empty column. Therefore exactly \(80\) minimum total-dominating four-sets occur in \(R\), and, by the incidence bijection, in \(S\).

Every four-vertex graph without isolated vertices that fails to have a perfect matching is a star \(K_{1,3}\) (this follows by considering an edge and checking all possible adjacencies among its four vertices). Every total-dominating four-set induces a graph without isolated vertices. The rook graph has no induced claw: each vertex's six neighbors split into two disjoint triangles, so at most two pairwise nonadjacent neighbors are possible. Hence all \(80\) four-sets in \(R\) are paired-dominating.

In the Shrikhande graph, every open neighborhood induces a six-cycle. The six-cycle has exactly two independent three-sets, its alternating triples. Together with the center, each yields an induced claw. Both claws centered at \((0,0)\), with integer labels \(\{0,1,4,15\}\) and \(\{0,3,5,12\}\), can be checked directly to total dominate all \(16\) vertices. Translation of \(\mathbb Z_4^2\) takes this to the two claws at every center. Each four-vertex claw has a unique center, so these are \(32\) different total-dominating four-sets without a perfect matching. Thus \(S\) has \(80-32=48\) minimum paired-dominating sets, while \(R\) has \(80\).

**3. Complete exact enumeration for the larger coefficients.** For each graph, list its sixteen six-element open neighborhoods using the explicit adjacency rules, and visit every bitmask from \(0\) through \(2^{16}-1\). For mask \(m\), total domination is equivalent to \(m\mathbin{\&}N(u)\ne0\) for every vertex \(u\). For an even-cardinality selected set \(D\), induced perfect matchability is computed by the terminating recurrence
\[
 M(\varnothing)=\mathrm{true},\qquad
 M(D)=\bigvee_{v\in N(u)\cap(D\setminus\{u\})} M(D\setminus\{u,v\}),
\]
where \(u\) is any fixed selected vertex. This recurrence is exact: every perfect matching must pair \(u\) with one of these \(v\), and each branch strictly decreases cardinality by two. Exhausting all \(65536\) subsets for each graph gives the displayed coefficients, without probabilistic sampling or unresolved search branches. `check_bitmask.py` implements this recurrence with cached subproblems; `check_sets.py` independently enumerates combinations of coordinate pairs and matching branches using set operations. Both confirm all coefficients. The six coefficients where the graphs differ include the analytically resolved four-vertex discrepancy.

## Verification
Run `python check_bitmask.py` and `python check_sets.py` with Python 3 and the standard library. Both scripts exhaust all \(2^{16}=65536\) subsets of each graph. The first checks the incidence certificate, all polynomial coefficients, and exactly two nonpairable minimum sets per center. The second constructs each graph separately from coordinate definitions and counts each cardinality class by combinations, with an independently written perfect-matching search. `counts.json` contains the complete expected coefficient vectors and incidence-permutation witnesses. Output equality is verified by assertions; successful runs print `PASS` messages. A finite complete search here constitutes an exact proof for these two fixed sixteen-vertex graphs, not an extrapolation to an infinite family.

## Relationship to prior work
Haynes and Slater (1998) introduced paired domination and established general inequalities and complexity properties; none of those results is claimed here. Choudhary, Margulies and Hicks (2011 preprint; 2013 journal version) establish total- and paired-domination bounds for Cartesian products, but not the present exact Shrikhande census. The known folded-six-cube/bipartite-double description of the common open-neighborhood structure explains how equal total-domination polynomials can arise; it does not preserve induced matchings inside selected sets. Prior results have already determined the rook graph's paired-domination polynomial in a broader rectangular family, and that polynomial is used only as a comparison. Published work comparing the Shrikhande and rook independence complexes concerns a different invariant. No matching statement for the complete Shrikhande paired-domination polynomial was located in the accessible checked literature, but historical priority cannot be certified by search absence.

## Limitations
This is a finite exact classification for two labeled sixteen-vertex graphs, not a general formula for all strongly regular graphs, other Cartesian products, or arbitrary graph pairs with equal total-domination polynomials. The two exhaustive implementations and the combinatorial argument are internally checked rather than independently audited by an external mathematician. Some historical full texts remain inaccessible; priority is conditional on the available published records and searches. The equality of total-domination polynomials is an incidence-preservation result, not an assertion that the graphs are isomorphic.

## References
- T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206. DOI: `10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F`; first public online version December 7, 1998.
- K. Choudhary, S. Margulies and I. V. Hicks, *A Note on Total and Paired Domination of Cartesian Product Graphs*, Electron. J. Combin. 20(3) (2013), #P25. `https://arxiv.org/abs/1109.2174`; DOI: `10.37236/2535`.
- I. Martinjak, *A class of symmetric association schemes as inclusion of biplanes* (2014), `https://arxiv.org/abs/1401.5441` (historical comparison with biplane incidence structures, not paired domination).
- S. Alikhani and A. Jafari, *On roots of total domination polynomial of graphs* (2016), `https://arxiv.org/abs/1605.02222` (background on the total-domination polynomial).
- Distance-Regular Graphs, *Incidence graph of the biplane on 16 points*, `https://www.math.mun.ca/distanceregular/graphs/incidence-biplane16.html` (neighborhood-incidence context).
