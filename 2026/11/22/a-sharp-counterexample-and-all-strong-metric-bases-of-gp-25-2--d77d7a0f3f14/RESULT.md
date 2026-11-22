# A sharp counterexample and all strong metric bases of \(GP(25,2)\)

## Finding

The generalized Petersen graph \(G=GP(25,2)\) has strong metric dimension
\[
\operatorname{sdim}(G)=34.
\]
It has exactly \(125\) minimum strong resolving sets, with the following explicit classification. Write its vertices as \(u_i,v_i\), where \(i\in\mathbb Z/25\mathbb Z\). For \(a\in\mathbb Z/25\mathbb Z\) and \(b\in\mathbb Z/5\mathbb Z\), put
\[
A_a=\{u_{a+2j}:0\le j\le5\},\qquad
B_b=\{v_i:i\equiv b\text{ or }b+2\pmod 5\}.
\]
Then the \(125\) minimum strong resolving sets are precisely
\[
S_{a,b}=V(G)\setminus(A_a\cup B_b).
\]
In particular this is a finite counterexample to the proposed equality \(\operatorname{sdim}(GP(4k+1,2))=5k+5\) for every \(k\ge5\): at \(k=6\), that proposal predicts \(35\), whereas the correct number is \(34\). The previously proved upper bound \(\operatorname{sdim}\le5k+5\) is not contradicted.

## Assumptions and scope

All graphs are finite, simple and connected. The graph \(GP(25,2)\) has vertex set \(\{u_i,v_i:i\in\mathbb Z/25\mathbb Z\}\) and edges \(u_i u_{i+1}\), \(u_iv_i\) and \(v_iv_{i+2}\), with indices modulo \(25\). A vertex \(w\) *strongly resolves* distinct \(x,y\) if either \(d(w,x)=d(w,y)+d(x,y)\) or \(d(w,y)=d(w,x)+d(x,y)\). A strong resolving set resolves every unordered pair, and \(\operatorname{sdim}\) is its least cardinality. This finding makes no assertion for other generalized Petersen orders.

## Proof

**1. Resolving graph reduction.** Two vertices \(x,y\) are mutually maximally distant (MMD) if each neighbor of either vertex is at distance at most \(d(x,y)\) from the other vertex. Form the graph \(R\) on \(V(G)\) with the MMD pairs as its edges. Strong resolving sets are exactly vertex covers of \(R\). Necessity: if an MMD pair is omitted, no other vertex can strongly resolve it, since the neighbor at the start of a hypothetical extended shortest path would increase the distance to the opposite endpoint. Sufficiency: for any pair \(x,y\), choose a longest shortest path containing both in order. Its endpoints are MMD; otherwise a path extension at an endpoint would produce a longer shortest path still containing \(x,y\). An endpoint in a vertex cover of \(R\) strongly resolves \(x,y\).

**2. Exact MMD graph.** Breadth-first distances on the \(50\)-vertex graph, together with cyclic rotation symmetry, show that the MMD edges are exactly
\[
\{u_i,u_{i+d}\}\quad(d\in\{5,7,9,11,12\}),\qquad
\{v_i,v_{i+d}\}\quad(d\in\{9,11\}),
\]
for all \(i\) modulo \(25\); these are unordered pairs, with no MMD edges between the two layers. Each difference class comprises \(25\) edges, so there are \(125\) outer-layer and \(50\) inner-layer edges. The attached independently implemented programs construct shortest paths and check this entire table using the defining inequalities, rather than assuming it.

**3. Maximum independent sets in the outer MMD layer.** Independence means avoiding cyclic pair differences \(\pm5,\pm7,\pm9,\pm11,\pm12\). After translation to include index \(0\), every other member must lie among the exactly fourteen indices
\[
T=\{1,2,3,4,6,8,10,15,17,19,21,22,23,24\}.
\]
An exhaustive finite comparison of the \(\binom{14}{5}=2002\) five-subsets of \(T\) finds exactly six for which the resulting six-set containing \(0\) is independent. They are the six translations of \(\{0,2,4,6,8,10\}\) that contain \(0\). None of the \(\binom{14}{6}=3003\) six-subsets extends \(0\) to an independent seven-set. Since every independent seven-set can be translated to contain \(0\), the independence number is \(6\). Double counting independent six-sets with a distinguished member shows their total number is \(25\), and they are precisely the \(A_a\) index patterns.

**4. Maximum independent sets in the inner MMD layer.** For each \(j\in\{0,1,2,3,4\}\), the cyclic five-tuple
\[
(5j,\,5j+9,\,5j+18,\,5j+2,\,5j+11)\pmod{25}
\]
is a five-cycle using MMD edges of index differences \(\pm9,\pm11\). These five cycles are vertex disjoint and partition the \(25\) inner indices. Hence an independent set has at most two vertices in each cycle, at most ten total. Each cycle has five two-vertex independent choices, so there are exactly \(5^5=3125\) candidates of size ten before imposing inter-cycle edges. Direct comparison against differences \(\pm9,\pm11\) retains exactly five, namely the patterns \(i\equiv b\) or \(b+2\pmod 5\), as \(b\) varies. Thus the inner independence number is \(10\) and it has exactly five maximum independent sets.

**5. Conclusion.** The graph \(R\) has no cross-layer edges. A largest independent set in \(R\) consists of independently chosen maximum independent sets on its two layers; it has \(6+10=16\) vertices, with exactly \(25\cdot5=125\) choices. Its complement is a minimum vertex cover of size \(50-16=34\), hence a minimum strong resolving set. This proves both the dimension and the complete classification. The finite comparisons in steps 2–4 are fully specified, checked by two standalone programs and do not extrapolate from small instances to an infinite claim.

## Verification

From the directory containing the embedded sources, execute `g++ -O2 -std=c++17 gp25_independent.cpp -o gp25_independent` and then `./gp25_independent`, and separately `python3 gp25_crosscheck.py` (standard Python 3 libraries only). The C++ implementation generates all graph distances and MMD pairs, verifies every proposed MMD difference class, checks direct strong resolution of all \(\binom{50}{2}=1225\) pairs for an explicit 34-vertex set, and exactly enumerates independent sets of sizes \(6,7\) and \(10,11\) in the two layers. It returns layer counts \(25,0\) and \(5,0\), respectively. The independently structured Python implementation uses translation to restrict the outer case to \(2002+3003\) candidates and a five-cycle product to restrict the inner case to \(3125\) candidates. It then directly verifies the strong-resolution condition for each of all \(125\) classified bases. Both implementations produced the stated results with assertion checking enabled.

## Relationship to prior work

Kratica, Kovačević-Vujčić and Čangalović introduced the relevant \(GP(n,2)\) strong metric dimension bounds in their 2015 preprint (later 2017 journal paper). Their Corollary 1 proves an upper bound \(5k+5\) at \(n=4k+1\), and the conclusion proposes equality for all \(k\ge5\). Their exact finite table ends at \(n=19\); it does not include \(n=25\). This result disproves the proposed equality at \(k=6\) and supplies a complete minimum-basis classification at that order. The MMD-to-vertex-cover reduction is standard (Oellermann and Peters-Fransen, 2007) and is proved again above for completeness. Related published results on the *mixed*, *edge* and *threshold* metric dimensions use distinct invariants and do not imply the strong metric dimension or its minimum-basis count asserted here.

## Limitations

This is an exact finite result for a specified \(50\)-vertex graph, not a formula for all \(GP(n,2)\). The outer-layer independence classification and the five inter-cycle compatibility cases are short exhaustive finite checks, not a symbolic all-order theorem. Independent peer review has not occurred, and historical priority could still be affected by an earlier unindexed computation of the same case.

## References

1. J. Kratica, V. Kovačević-Vujčić, M. Čangalović, *The strong metric dimension of some generalized Petersen graphs*, arXiv:1507.00881, first public version 3 July 2015; journal version *Applicable Analysis and Discrete Mathematics* **11** (2017), 1–10, https://doi.org/10.2298/AADM161110032K.
2. O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, *Discrete Applied Mathematics* **155** (2007), 356–364, https://doi.org/10.1016/j.dam.2006.06.009.
3. H. Raza and Y. Ji, *Computing the mixed metric dimension of a generalized Petersen graph \(P(n,2)\)*, *Frontiers in Physics* **8** (2020), 211, https://doi.org/10.3389/fphy.2020.00211.
4. N. Benakli, N. H. Bong, S. Dueck (Gosselin), B. Novick, O. R. Oellermann, *The threshold dimension and threshold strong dimension of a graph: a survey*, in *Research Trends in Graph Theory and Applications* (2021), 73–98, https://doi.org/10.1007/978-3-030-77983-2_4.
