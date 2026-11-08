# A Pascal-line obstruction to a node-free degree-nine conic-line arrangement

## Finding
Over \(\mathbb C\), there is **no** reduced arrangement \(D=Q\cup L_0\cup\cdots\cup L_6\subset\mathbb P^2\) consisting of one smooth conic and seven distinct lines whose singularities are exclusively ordinary nodes, ordinary transverse triple points, and tacnodes, with numerical basket
\[
(n_2,t,n_3)=(0,1,11).
\]
This is a nonrealizability statement about the **incidence basket itself**, without assuming freeness or near-freeness. An equivalent geometric obstruction is that an inscribed hexagon whose three alternating sides concur in each of two pencils cannot have its Pascal line tangent to its smooth conic (under the nondegenerate, six-distinct-vertices hypotheses specified in the proof).

## Assumptions and scope
Work in \(\mathbb P^2_{\mathbb C}\), with seven pairwise distinct lines and one nonsingular irreducible conic. An ordinary triple point has exactly three smooth transverse branches (either three lines or two lines and the conic). A tacnode is an intersection of a line with the conic of contact order two, with no other component through it. Every other singularity would have to be an ordinary node, but the stated basket assumes none. Components may not coincide. No condition on syzygies, exponents, geometric freeness, or field of definition is imposed.

## Proof
**Incidence forcing.** Write \(s\) for the number of ordinary triples containing the conic (two lines and the conic), and \(h\) for triples consisting of three lines. Counting line–conic intersections with multiplicities gives \(14=2s+2\cdot1\), hence \(s=6\). Counting the \(\binom72=21\) pairs of distinct lines gives \(21=s+3h\), hence \(h=5\). There is one conic-tangent line; the six other lines are secants meeting the conic in two distinct conic–line–line triple points each.

Construct a graph on the seven line components, joining two vertices when the corresponding lines form a conic-containing triple. The tangent line is an isolated vertex, and the other six vertices form a simple \(2\)-regular graph with six edges. Thus they form either a six-cycle or two disjoint triangles. In the two-triangles case a line-only triple may contain at most one line from each graph triangle, so all five line-only triples would have to contain the isolated tangent line. But that tangent line has only six pairs with other lines, and each such triple uses two pairs, allowing at most three triples: impossible.

The graph therefore is a six-cycle, with vertices labeled cyclically \(0,1,\ldots,5\) and isolated tangent vertex \(6\). Every one of the six tangent-line pairs belongs to a line-only triple, so exactly three line-only triples contain vertex \(6\). The two other line-only triples are disjoint from the six-cycle edges. The complement of a six-cycle has only two independent triples, \(\{0,2,4\}\) and \(\{1,3,5\}\); both are forced. The three remaining edges of that complement are \(\{0,3\},\{1,4\},\{2,5\}\). Therefore the full list of line-only triples is
\[
\{0,2,4\},\quad\{1,3,5\},\quad\{0,3,6\},\quad\{1,4,6\},\quad\{2,5,6\}.
\]
In particular \(L_0,L_2,L_4\) form one pencil and \(L_1,L_3,L_5\) form another pencil, with distinct centers.

**Projective normal form.** The two centers are distinct, and neither lies on a line of the opposite pencil (that would create a forbidden intersection of at least four lines). Send them to \([1:0:0]\) and \([0:1:0]\), respectively. A further affine change of coordinates fixing both centers sends the six lines to
\[
L_0:Y=0,\quad L_2:Y=Z,\quad L_4:Y=uZ,\qquad
L_1:X=0,\quad L_3:X=Z,\quad L_5:X=vZ,
\]
where \(u,v\notin\{0,1\}\). Their six adjacent intersections must lie on the conic; in the chart \(Z=1\), these are
\[
(0,0),(0,1),(1,1),(1,u),(v,u),(v,0).
\]
Because the conic is smooth, its quadratic coefficient of \(Y^2\) is nonzero: otherwise restriction to the line \(X=0\), which contains two distinct listed conic points, forces that entire line to be a conic component. Normalize that coefficient to one. Solving the six point-incidence equations (equivalently comparing the sums and products of the two \(Y\)-roots above each of \(X=0,1,v\)) yields
\[
v=\frac{u-1}{u},\qquad
Q_u:\ u^2X^2+Y^2-uXY-u(u-1)XZ-YZ=0.
\]
The three opposite-side intersections belonging to triples \(\{0,3,6\},\{1,4,6\},\{2,5,6\}\) are \((1,0),(0,u),(v,1)\), so the forced seventh line is their Pascal line
\[
L_6:\ uX+Y-uZ=0.
\]

**Tangency contradicts smoothness.** Substitute \(Y=uZ-uX\) into \(Q_u\). The discriminant of the resulting homogeneous binary quadratic in \(X,Z\), after setting \(Z=1\), is
\[
\Delta=4u^2(u^2-u+1).
\]
The determinant of the symmetric \(3\times3\) matrix representing \(Q_u\) is
\[
\det(Q_u)=-\frac{u^2(u^2-u+1)}4=-\frac{\Delta}{16}.
\]
Since \(u\ne0\), tangency of \(L_6\) to \(Q_u\) would imply \(\Delta=0\), and hence \(\det(Q_u)=0\), contradicting smoothness. This proves the claim. All coordinates and discriminants are valid in characteristic zero; the theorem makes no assertion in characteristic two.

## Verification
The standalone `verify_pascal.py` performs exact symbolic checks of the graph complement, six point substitutions, collinearity of the three Pascal intersections, the discriminant, and the conic determinant. Run `python verify_pascal.py` with SymPy. It prints `PASS`. The graph-exclusion argument and normal-form uniqueness appear explicitly above and are not inferred from an experimental search. The proof is an infinite-field symbolic argument, not a finite computation or a bounded enumeration.

## Relationship to prior work
Gałecka (first public April 29, 2022) left existence of nearly free degree-eight and degree-nine conic-line arrangements unresolved in a class with nodes, tacnodes and ordinary triple points. Dimca–Pokora established general combinatorial and freeness restrictions for this singularity class. The present result isolates one extreme *numerically admissible* singularity basket and forbids its realization without assuming near-freeness. Earlier restrictions on nearly-free arrangements, even when they rule out all such degree-nine nearly-free examples, do not imply nonexistence of a curve arrangement with this basket and different syzygies. The degree-eight example in later published work is a different arrangement with different numerical data. The collinearity of opposite hexagon sides is classical Pascal geometry; the identified equality between Pascal-line discriminant and conic determinant in this alternating-pencil setting supplies the obstruction here.

## Limitations
This rules out only the basket \((0,1,11)\) for one conic and seven lines. It does not classify every degree-nine singularity basket, establish existence of any other basket, settle any general classification of conic-line arrangements, or claim a new version of Pascal's theorem. A historical equivalent statement in older projective-configuration literature remains a priority risk; no independent audit has been performed.

## References
- A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969 (first posted 2022-04-29); *Bol. Soc. Mat. Mex.* 28, 67 (2022). DOI: 10.1007/s40590-022-00461-4.
- A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, *J. Algebraic Combin.* 56 (2022). DOI: 10.1007/s10801-022-01116-3.
- Classical Pascal theorem and its converse: used only for background terminology; collinearity and the decisive discriminant are calculated directly above.
