# Four variables characterize finite projective-plane incidence graphs, and three cannot

## Finding

On finite nonempty simple undirected graphs in the pure adjacency-and-equality language, the minimum number of variable names in a counting-free first-order sentence defining the class of Levi graphs of finite projective planes of order at least two is four. The upper bound is an intrinsic four-name recognizer without point or line labels. The lower bound uses the previously recorded three-variable equivalence of the Fano Levi graph and the Levi graph of its block-complement design [1]. No quantifier-rank optimum is asserted.

## Assumptions and scope

Write \(E\) for graph adjacency. A projective plane here has unique joining lines for distinct points, unique intersections for distinct lines, and four points with no three collinear. Its Levi graph has points and lines as vertices and incidences as undirected edges. The definition concerns membership among all finite nonempty simple undirected graphs, not just among structures already labelled as incidence graphs. No assumption of coordinatizability is used.

## Four-variable recognition

For each occurrence below expand \(S(a,b)\) as \(a=b\lor\exists w\,(E(a,w)\land E(b,w))\). Take the conjunction of the following six sentences:

\[
\begin{aligned}
&\exists x\exists y\,\neg S(x,y);\\
&\forall x\forall y\forall z\,[(S(x,y)\land S(y,z))\to S(x,z)];\\
&\forall x\forall y\forall z\,[(\neg S(x,y)\land\neg S(x,z))\to S(y,z)];\\
&\forall x\forall y\,[E(x,y)\to\neg S(x,y)];\\
&\forall x\exists y\exists z\exists w\,[E(x,y)\land E(x,z)\land E(x,w)\land y\ne z\land y\ne w\land z\ne w];\\
&\forall x\forall y\forall z\forall w\,[(x\ne y\land E(x,z)\land E(y,z)\land E(x,w)\land E(y,w))\to z=w].
\end{aligned}
\]

The first four clauses use only \(x,y,z\) outside the abbreviation, and each \(\exists w\) in the expansion is local. The last two clauses use no abbreviation. The sentence therefore uses only the four names \(x,y,z,w\).

The relation \(S\) is reflexive and symmetric, and the second clause makes it transitive. The first clause forces at least two equivalence classes; the third forces at most two, since any two vertices outside the class of a given vertex must be related. The fourth clause places all edges between classes. Distinct vertices of one class share a neighbor by the definition of \(S\), and the sixth clause makes the neighbor unique. Interpret one class as points and the other as lines; this gives both pair axioms. For a quadrangle, choose two different lines through a point \(p\), then two further points on each line, possible by the fifth clause. These four points are distinct by uniqueness of the intersection, and every three contain two on one chosen line and one outside it. Thus the graph is the Levi graph of a finite nondegenerate projective plane. Conversely, a finite projective plane of order at least two satisfies all six clauses: \(S\) defines equality of sides, each vertex has degree at least three, and every pair of distinct vertices on the same side has a unique common neighbor. No side labels or additional axioms of connectedness or regularity are needed.

## Sharpness using the known obstruction

The Fano plane has symmetric design parameters \((v,r,\lambda)=(7,3,1)\), where \(v\) is the number of vertices on each side, \(r\) the degree and \(\lambda\) the number of common neighbors of a distinct same-side pair. Its block complement has \((7,4,2)\): two Fano blocks (and dually two point neighborhoods) of size three intersect in one element, so their complements intersect in \(7-6+1=2\). The block-complement Levi graph fails the sixth clause and is outside the class. These two fourteen-vertex graphs are equivalent in counting-free \(\mathrm{FO}^3\) by the symmetric-design collapse in [1].

For a direct check of the witness argument, preserve side, equality and adjacency after every pebble move. With two distinct stationary vertices on one side, the four opposite-side adjacency cells have sizes \(\lambda,r-\lambda,r-\lambda,v-2r+\lambda\); these are \((1,2,2,2)\) for Fano and \((2,2,2,1)\) for its complement. On the same side there is also a fresh vertex. For stationary vertices on opposite sides, a fresh vertex on either side can realize either adjacency bit after excluding the stationary vertex of that side: each degree and each opposite-side nonneighbor count is at least three in both graphs. Repeated anchors and fewer stationary vertices present no additional requirement. Hence the response can preserve the invariant in either direction on every move, giving unrestricted-depth \(\mathrm{FO}^3\) equivalence. A sentence with three names cannot separate a member from this nonmember. This proof uses the existing obstruction rather than claiming a new design-collapse theorem.

## Verification and relation to prior work

The accompanying standard-library scripts can be run with \(\texttt{python3}\): `recognition_check.py` checks the semantic clauses on the Fano and ternary planes, the block-complement design and the 91 one-edge perturbations of the Fano graph; `formula_check.py` checks the actual closed syntax and interprets it on the three unperturbed graphs; `pebble_check.py` compares the refined extension profiles on those same three graphs. Their respective `_output.txt` files contain the recorded results. These are finite diagnostics, not the proofs of recognition or unrestricted-depth nondefinability.

The indexed symmetric-design theorem [1] already supplies the lower bound, including the explicit Fano/complement pair. Within-family incidence equivalence is a different question: it concerns agreement on every formula within a variable fragment, not membership among arbitrary graphs. The classical generalized-triangle description and the extremal characterization of De Winter, Lazebnik and Verstraëte [2] concern the same graphs, but do not give the variable-width result in the uncoloured signature. The finite-variable framework is standard [3]. The distinct contribution here is the four-name definition of the entire graph class and its combination with the known obstruction to yield an exact ambient recognition width. Earlier equivalent first-order formulations not identified in these comparisons remain possible.

## References

1. *Three-variable collapse of nontrivial symmetric design incidence graphs*, Resultary, Finding, [record](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-three-variable-collapse-of-nontrivial-symmetric-design-incidence--29e921d9f46f).
2. J. De Winter, F. Lazebnik and J. Verstraëte, *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics 15 (2008), R143, DOI:10.37236/867, introduction and Theorem 1.
3. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, §1.2.1 and Theorem 3.3.
