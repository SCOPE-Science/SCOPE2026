# Four variables characterize finite projective-plane incidence graphs, and three cannot

## Finding

**Theorem.** In the pure adjacency-and-equality language of finite, nonempty, simple undirected graphs, the class of incidence (Levi) graphs of *all* finite projective planes of order at least two is defined by a single counting-free first-order sentence using at most four variable names. No sentence using at most three variable names defines this class, regardless of quantifier rank. This includes the non-Desarguesian projective planes wherever they exist.

More strongly, the incidence graphs of any two finite symmetric \(2\)-\((v,r,\lambda)\) designs satisfying \(r\ge3\), \(1\le\lambda<r\), and \(v-2r+\lambda>0\) are equivalent in \(\mathrm{FO}^{3}\), with *unrestricted* quantifier depth. In particular, the incidence graphs of the Fano plane \(2\)-\((7,3,1)\) and its block-complement design \(2\)-\((7,4,2)\) are \(\mathrm{FO}^{3}\)-equivalent, although only the first is a projective-plane incidence graph. Both witnesses have fourteen vertices.

## Assumptions and scope

All graphs are finite, simple, undirected and nonempty. The language has one adjacency relation \(E\) and equality, without color predicates, point/line predicates, constants, counting quantifiers or order. A finite projective plane is an incidence system of points and lines such that every two distinct points lie on exactly one line, every two distinct lines meet in exactly one point, and four points exist with no three collinear. Its incidence graph has the points and lines as its vertices and incidence as adjacency. A symmetric \(2\)-design has equally many points and blocks (\(v\)), every point and block of incidence degree \(r\), every pair of points on exactly \(\lambda\) blocks and every pair of blocks meeting in exactly \(\lambda\) points.

Use the following abbreviation, in contexts where \(w\) is not an outer free variable:
\[
S(x,y):=(x=y)\lor\exists w\,[E(x,w)\land E(y,w)].
\]
This is an ordinary formula, not an additional relation symbol. The following six clauses comprise the promised sentence \(\Phi\), with the abbreviation expanded separately in each clause:
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
Every expanded clause uses only the names \(x,y,z,w\); in the first four, every occurrence of the internal \(\exists w\) belongs to its own \(S\)-subformula. The last two clauses do not use \(S\). In particular, there is no variable capture.

## Proof

**Recognition, sufficiency.** The relation defined by \(S\) is reflexive and symmetric. The second clause makes it transitive. The first clause says there are at least two \(S\)-classes. Given an element \(x\), if \(y,z\) lie outside its class, the third clause forces \(S(y,z)\); consequently there are exactly two nonempty classes. The fourth clause places every edge between the two classes. Two *distinct* vertices of the same class must have a common neighbor, by the definition of \(S\). The sixth clause says that two distinct vertices have at most one common neighbor, so two vertices on either side have *exactly* one neighbor in common on the opposite side. These are precisely the point-pair and line-pair uniqueness axioms in the corresponding incidence structure.

The fifth clause ensures each vertex has at least three neighbors. To obtain a quadrangle, choose a point \(p\), two different lines \(\ell_1,\ell_2\) through it, and two distinct further points on each line. The resulting four points are distinct because the two lines meet only at \(p\); no three are collinear because any triple has two points on one of the chosen lines and a third point outside it. Thus the incidence structure satisfies all projective-plane axioms. In particular, no connectedness, regularity, equality-of-side-size, or prescribed order axiom is missing: all follow from the projective-plane axioms.

**Recognition, necessity.** In the incidence graph of every projective plane, \(S\) relates two vertices precisely when they belong to the same point or line side. Each side is nonempty, every line/point has at least three incident partners, edges cross sides, and two distinct vertices have at most one common neighbor. Hence every clause of \(\Phi\) holds. Therefore \(\Phi\) defines exactly the claimed graph family.

**The three-variable collapse.** Let \(G,H\) be incidence graphs of symmetric designs with the stated parameter inequalities (parameters may differ). We give a permanent three-pebble Duplicator strategy. Match sides (point to point, block to block), equality and cross-side adjacency among the occupied vertices. A move leaves at most two stationary pebbles. For two distinct fixed vertices on the same side, the opposite side is divided into vertices adjacent to both, only the first, only the second, and neither. The respective cardinalities are
\[
\lambda,\quad r-\lambda,\quad r-\lambda,\quad v-2r+\lambda,
\]
all positive by hypothesis. On the fixed side, at least one other vertex exists. Thus *every* consistent one-vertex adjacency pattern relative to two same-side fixed vertices can be met in either graph. For fixed vertices on opposite sides, whether they are incident or not, choosing the new vertex on either side reduces to choosing it adjacent or nonadjacent to the fixed opposite-side vertex. Excluding the already occupied vertex if necessary leaves at least one option: an incident fixed pair offers \(r-1\) other neighbors and \(v-r\) nonneighbors; a nonincident pair offers \(r\) neighbors and \(v-r-1\) other nonneighbors. They are all positive because \(r\ge3\) and \(v-2r+\lambda>0\) with \(\lambda<r\). Cases of fewer than two fixed distinct vertices are easier. Hence each move can preserve the pebbled partial isomorphism forever. The unlimited-round three-pebble characterization of \(\mathrm{FO}^{3}\) proves \(G\equiv_{\mathrm{FO}^{3}}H\).

Every finite projective-plane design \(2\)-\((q^2+q+1,q+1,1)\) with \(q\ge2\) satisfies the inequalities. In the Fano plane, \((v,r,\lambda)=(7,3,1)\); its complementary symmetric design has \((7,4,2)\), also satisfying all inequalities. In its incidence graph, two distinct point vertices have *two* common neighbors; therefore the sixth clause of \(\Phi\) fails. Since one graph is in the class and the other is not, while no \(\mathrm{FO}^{3}\) sentence distinguishes them, the required four-variable width is **sharp**.

## Verification

The standalone programs `recognition_check.py`, `formula_check.py` and `pebble_check.py` use only the Python standard library. Execute each with `python3 <filename>` in any order. The first builds the Fano and ternary projective planes and the complementary Fano symmetric biplane, checks the six semantic conditions and all ninety-one single-edge perturbations of the fourteen-vertex Fano Levi graph. The second constructs the actual first-order syntax tree of each expanded clause, checks closure and the four-name restriction, and directly interprets the sentences on all three examples. The third verifies exact one-vertex extension-support agreement for every ordered two-pebble type, independently of the proof's cardinality calculation. Recorded outputs are supplied as `recognition_output.txt`, `formula_output.txt`, and `pebble_output.txt`.

Finite tests are corroboration, **not** an exhaustive enumeration of all finite graphs, all designs, or all pebble-game lengths. The unrestricted theorem is proved by the structural recognition argument and the permanent strategy above.

## Relationship to prior work

De Winter, Lazebnik and Verstraëte (2008) characterize incidence graphs of projective planes through extremal graph-theoretic properties, notably an eight-cycle bound, rather than by the minimum number of first-order variables. Pikhurko and Verbitsky (2010) present the general finite-variable/pebble-game framework, not this projective-plane recognition boundary. Venema (1999) treats modal logic and two-sorted point/line projective-plane semantics, including axiomatizations, not one-sorted unlabeled graph membership in \(\mathrm{FO}^{k}\) with a sharp three-pebble obstruction. Thus these inspected results supply the objects and proof methodology but do not state or imply the claimed exact four-variable recognition over all simple graphs. A more general or older definability theorem not located in the comparison could still subsume the result.

## Limitations

The result concerns *finite* simple graphs in the pure adjacency language. It does not assert an optimal quantifier rank, nor extend unchanged to directed incidence structures, enriched signatures, counting logics, or infinite projective planes. The three-pebble collapse holds for the specified symmetric-design parameter regime, not all symmetric designs. Literature priority is provisional; an independent mathematical audit has not been performed.

## References

1. J. De Winter, F. Lazebnik and J. Verstraëte, *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics 15 (2008), R143, DOI:10.37236/867, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r143/pdf (full article inspected).
2. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865 (2010), https://arxiv.org/abs/1003.4865 (full article inspected, including pebble-game exposition).
3. Y. Venema, *Points, Lines and Diamonds: A Two-Sorted Modal Logic for Projective Planes*, Journal of Logic and Computation 9 (1999), 601–621, DOI:10.1093/logcom/9.5.601 (author-accessible full text inspected).
