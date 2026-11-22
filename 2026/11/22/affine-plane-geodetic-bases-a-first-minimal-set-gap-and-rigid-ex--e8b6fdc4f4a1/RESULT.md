# Affine-plane geodetic bases, a first minimal-set gap, and rigid exchanges

## Finding

Let \(\mathcal A\) be any **existing** finite affine plane of order \(q\ge2\), Desarguesian or otherwise, and let \(G_{\mathcal A}\) be its ordinary undirected point–line incidence graph. A geodetic set is a vertex set whose union of all shortest-path intervals covers every graph vertex. Then
\[
 g(G_{\mathcal A})=q.
\]
Its **only** minimum geodetic sets are the \(q+1\) parallel classes of \(q\) line-vertices. Consequently their simultaneous replacement graph, joining two minimum sets whose same-size symmetric difference replaces at most \(t\) vertices, is \((q+1)K_1\) for \(t<q\), and \(K_{q+1}\) for \(t\ge q\). The exact mobility threshold is \(q\).

There is also a sharp near-minimum rigidity phenomenon. For \(q\ge3\), **every** geodetic set of cardinality \(q+1\) contains a minimum geodetic set. Precisely \(2(q+1)q^2\) such sets exist: extend any one parallel class by either one point-vertex or one further line-vertex. Thus **no inclusion-minimal geodetic set of size \(q+1\)** exists when \(q\ge3\). At the exceptional order \(q=2\), there are \(30\) geodetic sets of size three: \(24\) extensions of parallel classes, and exactly six further inclusion-minimal sets of three vertices, each made of one line-vertex together with the two point-vertices on its disjoint parallel mate.

These statements concern ordinary geodetic intervals, not the *strong geodetic* variant that commits to only one chosen shortest path per endpoint pair.

## Assumptions and scope

An affine plane of order \(q\) has \(q^2\) point objects and \(q(q+1)\) line objects; each line has \(q\) points, each point lies on \(q+1\) lines, any two distinct points determine a unique line, and lines from different parallel classes intersect exactly once. There are \(q+1\) parallel classes of \(q\) pairwise disjoint lines, each class partitioning the points. The incidence graph has one vertex for each point and each line, with adjacency exactly at incidence.

For graph vertices \(u,v\), let \(I[u,v]=\{w:d(u,w)+d(w,v)=d(u,v)\}\), the union of vertices on every shortest \(u\)-to-\(v\) path. A set \(S\) is geodetic when \(\bigcup_{u,v\in S}I[u,v]=V(G_{\mathcal A})\). Inclusion-minimal means no proper subset is geodetic. For two equally large sets put \(\delta(S,T)=|S\setminus T|\). The threshold-\(t\) exchange graph joins distinct minimum sets when \(\delta(S,T)\le t\). Only endpoints of exchanges must be geodetic.

## Proof

**1. Point-cover localization.** Write a proposed geodetic set as \(S=A\cup B\), with \(a\) selected point-vertices and \(b\) selected line-vertices. Every point-vertex on a geodesic between selected endpoints either is itself in \(A\), or is incident with a line of \(B\). Indeed, a point-to-point geodesic has length two and no internal point; a point-to-line geodesic has length one or three, and its internal point (if any) lies on the selected line endpoint; and a line-to-line geodesic has length two for intersecting lines, or four for parallel lines, with all internal point-vertices on one of the two selected endpoint lines. Hence any geodetic \(S\) satisfies
\[
 q^2\le a+qb.\tag{1}
\]
Since \(q(a+b)\ge a+qb\), (1) implies \(|S|\ge q\).

**2. All minima.** If \(a+b=q\), equality in (1) forces \(a=0,b=q\), since \(q^2\le q^2-(q-1)a\) and \(q>1\). These \(q\) chosen lines must cover all \(q^2\) points, so they must be pairwise disjoint, hence constitute a full parallel class. Conversely, choose a parallel class \(\mathcal C\). For any point \(P\), choose its class line \(L\) and a different class line \(M\); a transversal line through \(P\) meets \(M\) at \(Q\), giving a shortest path \(L-P-N-Q-M\) of length four. For any line \(N\) outside \(\mathcal C\), its intersections with two different lines of \(\mathcal C\) give the same type of shortest path and place \(N\) on a geodesic between selected lines. Every line in \(\mathcal C\) is selected. Therefore \(\mathcal C\) is geodetic, and the \(q+1\) classes are all the minima.

**3. The near-minimum gap for \(q\ge3\).** Suppose \(a+b=q+1\). Inequality (1) becomes \(q^2\le q+1+(q-1)b\), hence the integer \(b\ge q\) for \(q\ge3\). There are only two cases.

If \(b=q,a=1\), first suppose at least two chosen lines lie in one parallel class, but that class is incomplete. Choose a missing line \(T\) of that class, and let \(s\ge2\) be the number of selected lines in that class. The selected lines outside the class meet \(T\) in at most \(q-s\) points in total; the single selected point adds at most one. Thus at most \(q-s+1<q\) points of \(T\) are geodetically covered, contradicting (1)'s necessary point cover. If instead no two selected lines are parallel, take one chosen line \(L\). Each of the other \(q-1\) chosen lines meets \(L\), so their union has at most \(q+(q-1)^2=q^2-q+1\) points. The extra selected point raises this to at most \(q^2-q+2<q^2\) for \(q\ge3\), again impossible. Therefore \(B\) is a complete parallel class.

If \(b=q+1,a=0\), and some two chosen lines are parallel but their class is incomplete, choose a missing line \(T\) and let \(s\ge2\) lines from its class be selected. Only \(q+1-s\le q-1\) other chosen lines can meet \(T\), leaving some point of \(T\) outside all chosen lines; contradiction. Thus any parallel pair forces a complete class. If no two chosen lines are parallel, every pair meets in one point, their shortest path has length two, and no unselected line-vertex lies on a geodesic between selected line endpoints. Since there are unselected line-vertices, this cannot be geodetic. Hence this case too contains a complete parallel class.

Every one-vertex extension of a geodetic basis is geodetic. Each of the \(q+1\) bases has \(q^2\) possible extra points and \(q^2\) possible extra nonclass lines. No extension of cardinality \(q+1<2q\) can contain two full parallel classes, so there is no double counting. Consequently there are \(2(q+1)q^2\) size-\(q+1\) geodetic sets, and none is inclusion-minimal.

**4. The exceptional two-point lines.** For \(q=2\), the twelve sets obtained by adding one point to a parallel class, and the twelve sets obtained by adding one nonclass line, are geodetic. A geodetic three-set with one selected line \(L\) and two selected points must have its two points outside \(L\) by the point-cover condition, hence they are exactly the points of the unique parallel mate \(M\). This set is geodetic: the two points have \(M\) as their joining line, while the four lines crossing \(L\) appear on shortest paths from either selected point to selected line \(L\). Its two chosen points and chosen line cover all four points; all six line-vertices are covered. There are exactly six such triples, one per \(L\), and they contain no two-line minimum geodetic set. No three-set with zero selected lines covers the fourth point; if two selected lines intersect, one further point cannot cover the sixth line-vertex, while if they are parallel the set already contains a basis; and three selected nonparallel lines cannot geodetically cover unselected line-vertices. This exhausts all cases and proves the exception.

**5. Exchange threshold.** Two distinct parallel classes are disjoint as sets of line-vertices, so \(\delta(\mathcal C,\mathcal C')=q\). Every threshold below \(q\) produces only isolated vertices, and at threshold \(q\) every pair is adjacent. This completes the stated exchange classification.

## Verification

The standalone Python 3 program `verify_affine.py` independently constructs \(\operatorname{AG}(2,q)\) for \(q\in\{2,3,4\}\) (including \(\mathbb F_4\)), builds the full incidence graph, computes all-pairs graph distances by breadth-first search, constructs geodetic intervals using the equality \(d(u,w)+d(w,v)=d(u,v)\), and examines every \(q\)-set and every \((q+1)\)-set of vertices. It checks the predicted minimum classes, all size-\(q+1\) counts, and the exceptional three-sets at order two. An independently implemented C++17 program `verify_affine_cpp.cpp` performs the prime-order \(q=2,3\) checks using a different coordinate enumeration and Floyd–Warshall distances. Recorded execution output is in `verify_output.txt`.

The checks are exhaustive only for these finite examples; the all-order theorem does not depend on the computation. No assertion is made about the existence of a finite affine plane at any particular unsupported order.

## Relationship to prior work

Harary, Loukakis and Tsouros introduced geodetic sets, and Chartrand, Harary and Zhang studied minimal and upper geodetic sets. Hon and coauthors studied geodetic numbers in specific graph classes, with an archived public preprint on 16 September 2015. A published result on **projective**-plane incidence graphs gives geodetic number \(2q\), flag-form bases and a different exchange threshold. Its statement and proof concern the graph containing the line at infinity and its points; deleting those vertices changes distances between parallel affine lines from two to four and does **not** preserve geodetic coverage. Thus projective bases do not imply the affine classification, the first minimal-set gap, or the order-two exception. A separate result on minimum domination in affine-plane incidence graphs studies closed-neighborhood coverage, not geodetic intervals.

Searches for affine-plane geodetic bases, resolvable-design geodetic sets, and near-minimum geodetic cardinalities revealed no exact theorem covering the present statements in the inspected material. This is not an assertion of absolute priority. Formal comparison details and residual search limitations are recorded in `AUDIT.json` and `REVIEW.md`.

## Limitations

The hypotheses require the full axioms of a finite affine plane, not arbitrary biregular incidence graphs or partial linear spaces. The first-gap theorem excludes size \(q+1\) inclusion-minimal sets for \(q\ge3\); it does not determine the entire higher minimal-set spectrum. The exchange rule permits simultaneous endpoint replacements, not a sequence through infeasible intermediate sets. All proof and computational checks are internal; no independent external validation has been performed.

## References

1. F. Harary, E. Loukakis and C. Tsouros, *The geodetic number of a graph*, Mathematical and Computer Modelling 17 (1993), 89–95; DOI `10.1016/0895-7177(93)90259-2`. Full text accessible via https://www.academia.edu/23671774/The_geodetic_number_of_a_graph.
2. G. Chartrand, F. Harary and P. Zhang, *Geodetic sets in graphs*, Discussiones Mathematicae Graph Theory 20 (2000), 129–138; https://geodesic.mathdoc.fr/item/DMGT_2000_20_1_a9/.
3. W.-K. Hon, T. Kloks, H.-H. Liu, H.-L. Wang and Y.-L. Wang, *Convexities in Some Special Graph Classes—New Results in AT-free Graphs and Beyond*, arXiv:1509.04944v1 (first public submission 2015-09-16), https://arxiv.org/abs/1509.04944.
4. *Geodetic bases of finite projective-plane incidence graphs: flag rigidity and a sharp simultaneous-exchange threshold*, publicly available full result at https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-geodetic-bases-of-finite-projective-plane-incidence-graphs-flag--25deca33c37d/.
