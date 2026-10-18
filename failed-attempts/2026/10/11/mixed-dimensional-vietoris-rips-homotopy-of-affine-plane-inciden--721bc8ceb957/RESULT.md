# Mixed-dimensional Vietoris–Rips homotopy of affine-plane incidence graphs

## Finding
For every finite affine plane \(\mathcal A\) of order \(q\ge2\), let \(G\) be its undirected bipartite point–line incidence graph with every edge of length one. The *inclusive* scale-two Vietoris–Rips complex has homotopy type
\[
\mathrm{VR}(G;2)\simeq
\bigvee^{(q-1)^2(q+1)} S^2\ \vee\
\bigvee^{(q-1)^{q+1}} S^q.
\]
When \(q=2\), both kinds of summands are two-dimensional, yielding \(\bigvee^4 S^2\). When \(q=3\), the result is \(\bigvee^{16}S^2\vee\bigvee^{16}S^3\). The formula gives the entire integral homotopy type, not just field-dependent Betti numbers.

## Assumptions and scope
An affine plane of order \(q\ge2\) has exactly \(q^2\) points and \(q(q+1)\) lines, with exactly \(q\) points on each line and \(q+1\) lines through each point. Each pair of distinct points lies on one line. Lines partition into \(q+1\) parallel classes, each of size \(q\); lines in different classes intersect in one point, and lines in the same class are disjoint. These axioms, not field coordinates, are the hypotheses. The theorem is conditional on the existence of such a plane, and therefore includes non-Desarguesian planes.

Write \(P\) and \(L\) for the two vertex classes of \(G\). For a finite vertex set \(S\), write \(\Delta(S)\) for the full simplex on \(S\). Write \(P(\ell)\) for points on line \(\ell\) and \(L(p)\) for lines through point \(p\). By definition, \(\mathrm{VR}(G;2)\) contains a simplex for each nonempty set of vertices whose pairwise graph distances are at most \(2\). No inequality is strict at the scale boundary.

## Proof
**Distances and clique cover.** Every two distinct points have distance \(2\), every two intersecting lines have distance \(2\), and every two parallel lines have distance \(4\). Incident point–line pairs have distance \(1\); nonincident point–line pairs have distance \(3\). Hence a clique of the distance-two graph containing at least two points and a line has all its points on that line. Similarly a clique containing at least two lines and a point has all its lines through that point. A clique cannot contain two distinct points and two distinct lines, since two points have only one common line.

Let \(B\) be the subcomplex on line vertices alone. Since two lines are adjacent precisely when they belong to different parallel classes, the entire line complex is
\[
B=D_q*D_q*\cdots*D_q\quad(q+1\text{ factors}),
\]
where \(D_q\) is a discrete set of \(q\) points and \(*\) denotes the simplicial join. In particular, the clique cover above gives two subcomplexes
\[
U=\Delta(P)\ \cup\ \bigcup_{\ell\in L}\Delta(\{\ell\}\cup P(\ell)),
\qquad
V=B\ \cup\ \bigcup_{p\in P}\Delta(\{p\}\cup L(p)),
\]
with \(\mathrm{VR}(G;2)=U\cup V\) and \(U\cap V=G\), the original incidence graph as a one-dimensional simplicial complex. To verify the intersection claim, both subcomplexes contain every point–line incidence edge; neither contains a simplex with two vertices of each kind, while only \(U\) has point–point edges and only \(V\) has line–line edges.

**Two collapses.** Inside \(U\), each line vertex \(\ell\) lies only in the full simplex \(\Delta(\{\ell\}\cup P(\ell))\). Its link is the full simplex on \(P(\ell)\), so \(\ell\) is a dominated vertex; deleting these line vertices one by one yields a strong simplicial collapse \(U\searrow\Delta(P)\). Thus \(U\) is contractible.

Inside \(V\), each point vertex \(p\) lies only in the full simplex \(\Delta(\{p\}\cup L(p))\). Its link is the full simplex on \(L(p)\); deleting all point vertices yields \(V\searrow B\). In particular the inclusion \(B\hookrightarrow V\) is a homotopy equivalence.

**The homotopy pushout.** Since \(q\ge2\), each \(D_q\) is homotopy equivalent to a wedge of \(q-1\) copies of \(S^0\). The reduced chain or join formula therefore gives
\[
B\simeq\bigvee^{(q-1)^{q+1}}S^q.
\]
In particular \(B\) is simply connected. As \(G\) is a connected graph, every map \(G\to B\) is nullhomotopic (collapse a spanning tree, then kill each loop using \(\pi_1(B)=0\)). Thus the composite \(G=U\cap V\hookrightarrow V\simeq B\) is nullhomotopic.

The two inclusions of finite simplicial subcomplexes are cofibrations, so \(U\cup_G V\) realizes their homotopy pushout. Replacing \(U\) by a point and \(V\) by \(B\), and using nullhomotopy of the attaching map \(G\to B\), yields the standard mapping-cone splitting
\[
U\cup_G V\simeq B\vee\Sigma G,
\]
where \(\Sigma G\) is the unreduced suspension of the connected graph \(G\). This step is an actual homotopy equivalence, not merely an isomorphism in homology.

**Cycle rank.** The graph \(G\) is connected because every two points share a line and every line contains points. It has \(q^2(q+1)\) edges and \(q^2+q(q+1)\) vertices. Its first Betti number is
\[
q^2(q+1)-q^2-q(q+1)+1=(q-1)^2(q+1).
\]
Every connected finite graph with this cycle rank has the homotopy type of a wedge of that many circles. Its suspension is therefore \(\Sigma G\simeq\bigvee^{(q-1)^2(q+1)}S^2\). Combining this with the splitting proves the theorem for every affine plane of order \(q\ge2\).

## Verification
The accompanying self-contained `verify.py` constructs the affine planes over the prime fields of orders \(2\) and \(3\) independently from coordinates. It verifies all incidence counts and uniqueness axioms; constructs graph distances using breadth-first search; obtains *all* maximal cliques of the squared incidence graph using Bron–Kerbosch enumeration; separately derives the predicted maximal cliques from the point, line, and parallel-class description; checks exact agreement; then constructs every simplex and computes all reduced simplicial boundary ranks over \(\mathbb F_2\).

The verifier returns \(\widetilde\beta_2=4\) and no other reduced homology for order \(2\), and \(\widetilde\beta_2=\widetilde\beta_3=16\) and no other reduced homology for order \(3\), with `VERIFY_OK`. Finite checks corroborate, rather than establish, the universal proof above. Run `python3 verify.py` with standard Python 3 and no extra dependencies.

## Relationship to prior work
The 2025 work of Adams, Karassev, and Virk studies homotopy equivalences between Vietoris–Rips simplicial complexes and metric thickenings. It supplies a current geometric-topology setting, but no calculation for finite affine-plane Levi graphs. Its paper uses a strict-radius convention, whereas the present statement explicitly uses the inclusive convention.

Larrión, Pizaña, and Villarroel-Flores prove a fundamental-group comparison for flag complexes of squares of bipartite graphs. Kawamura extends comparisons to appropriate homological and higher-homotopy equivalence conditions. Their general statements, as inspected, do not calculate affine-plane line-parallel-class joins or the two independent wedge multiplicities displayed above.

A publicly available projective-plane incidence-graph computation obtains only \(q^3\) two-sphere summands at scale two. An affine plane is not a projective plane: parallel lines remain distance four rather than distance two, and the line-only subcomplex is a noncontractible join. The projective formula therefore does not imply the extra \(q\)-sphere contribution or either coefficient here. In contrast to a cycle-power computation, the proof uses the incidence axioms and a nullhomotopic attaching map to produce the full affine-plane homotopy type.

## Limitations
The result assumes a finite affine plane exists; it does not assert existence at all positive integer orders. It uses the unweighted point–line graph metric and includes the scale boundary. The verifier samples only orders \(2\) and \(3\), but the proof covers non-Desarguesian planes by the axioms alone. The formula neither provides a classification of the planes themselves nor addresses arbitrary partial linear spaces or arbitrary weighted metrics. A future literature comparison may uncover an unindexed equivalent statement; no independent external audit is claimed.

## References
Adams, H.; Karassev, A.; Virk, Ž. *Vietoris thickenings and complexes of manifolds are homotopy equivalent*. arXiv:2512.23108, first submitted 2025-12-28, MSC 55N31, 54F45, 54C55, 54C65.

Larrión, F.; Pizaña, M. A.; Villarroel-Flores, R. *The fundamental group of the clique graph*. European Journal of Combinatorics 30 (2009), 288–294. DOI: 10.1016/j.ejc.2007.12.006.

Kawamura, K. *A variant of the bipartite relation theorem and its application to clique graphs*. Contributions to Discrete Mathematics 6 (2011), 91–100. DOI: 10.55016/ojs/cdm.v6i2.62059.
