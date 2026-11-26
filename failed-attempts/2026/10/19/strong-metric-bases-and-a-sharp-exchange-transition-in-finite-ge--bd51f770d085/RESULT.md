# Strong metric bases and a sharp exchange transition in finite generalized quadrangles

## Finding

For every finite thick generalized quadrangle \(\mathcal Q\) of order \((s,t)\), where \(s,t\ge2\), let \(G\) be its point–line incidence graph, with point set \(P\) and line set \(L\). The strong resolving graph of \(G\) has two components: the point noncollinearity graph and the line skewness graph. Consequently,
\[
\operatorname{sdim}(G)=st(s+t+2).
\]
All minimum strong resolving sets, with no duplication, are
\[
B_{\ell,p}=(P\setminus\ell)\cup(L\setminus\mathcal L(p)),\qquad(\ell,p)\in L\times P,
\]
where \(\ell\) means its incident point set and \(\mathcal L(p)\) is the set of lines through \(p\). Their number is \((s+1)(t+1)(st+1)^2\), with no incidence requirement on the independently chosen \(\ell,p\).

For minimum bases \(B,B'\), define replacement cost \(c(B,B')=|B\setminus B'|=|B'\setminus B|\). For every fixed minimum basis, the exact cost enumerator, including its constant term, is
\[
\sum_{B'}z^{c(B,B')}=(1+t(s+1)z^s+st^2z^{s+1})(1+s(t+1)z^t+ts^2z^{t+1}).
\]
The graph connecting distinct bases with replacement cost at most \(k\) is connected **if and only if** \(k\ge\max\{s,t\}\). At the first connected threshold, it is isomorphic to
\[
\begin{cases}
H_L\square H_P,&s=t,\\
H_L\square K_{|P|},&s>t,\\
K_{|L|}\square H_P,&t>s,
\end{cases}
\]
where \(H_L\) joins intersecting lines, \(H_P\) joins collinear points and \(\square\) denotes the Cartesian graph product. Its diameter is exactly four for \(s=t\), and exactly three for \(s\ne t\).

## Assumptions and scope

A generalized quadrangle of order \((s,t)\) is a finite point–line incidence structure with exactly \(s+1\) points per line and \(t+1\) lines per point, unique line through at most one pair of distinct points, and the projection property: for every point \(x\) not on line \(m\), exactly one point of \(m\) is collinear with \(x\). The dual axiom also follows. Assume \(s,t\ge2\); this is a conditional statement about every **existing** such structure, not an existence claim for arbitrary parameters. A vertex \(w\) strongly resolves vertices \(u,v\) if either \(u\) lies on a shortest \(v\)-to-\(w\) path or \(v\) lies on a shortest \(u\)-to-\(w\) path. A strong metric basis is a minimum-cardinality strongly resolving set. Two vertices are mutually maximally distant (MMD) if no neighbor of either is farther from the other than their mutual distance. The strong resolving graph has the original vertices and precisely the MMD pairs as edges.

## Proof

**1. Distances and MMD edges.** The generalized-quadrangle axiom gives distance two between distinct collinear points and between intersecting lines, and distance four between noncollinear points and between skew lines. A point and line have distance one when incident and three otherwise. Hence the incidence graph has diameter four. Every distance-four pair is MMD. A distance-two pair is not MMD: at either endpoint one can choose an incident line, respectively point, away from their unique common line, respectively intersection point, producing a neighbor at distance three from the opposite endpoint. A nonincident point–line pair at distance three is not MMD: of the \(t+1\ge3\) lines through the point, exactly one meets the given line; any other neighbor is skew to it at distance four. Distance-one pairs are not MMD, since every vertex has degree at least three and an alternative neighbor is at distance two. Thus the MMD edges are **exactly** the distance-four pairs, exclusively within \(P\) or within \(L\).

**2. Exact basis equivalence.** Every strongly resolving set must hit both endpoints of each MMD pair: a vertex other than the two MMD endpoints cannot strongly resolve them, because any geodesic ending beyond an MMD endpoint would contradict maximality. Conversely, for any pair \(u,v\), extend a shortest path connecting them at both ends as long as possible while preserving its geodesic property; the resulting endpoints are MMD. Any endpoint in a vertex cover of the MMD graph strongly resolves the original pair. Thus strong resolving sets are exactly the vertex covers of the MMD graph (the standard strong-resolving-graph characterization).

**3. Maximum independent sets and all bases.** An independent set in the point noncollinearity graph consists of pairwise collinear points. Any three pairwise collinear points lie on the same line: if \(a,b\) determine \(m\) and \(c\notin m\), the projection axiom contradicts collinearity of \(c\) with both \(a,b\). Therefore such a set has size at most \(s+1\), and equality holds precisely for the complete point set of a line. Dually, the maximum independent sets in line skewness are precisely the \(t+1\) lines through an individual point. The components are disjoint, so complements of all their independent maxima give exactly the displayed sets \(B_{\ell,p}\). Since \(|P|=(s+1)(st+1)\) and \(|L|=(t+1)(st+1)\), subtraction of \(s+t+2\) gives \(st(s+t+2)\). Distinct choices give distinct omitted sets, establishing the enumerated count.

**4. Exchange costs.** When \(\ell\ne m\) are lines, \(|\ell\setminus m|=s\) if they intersect and \(s+1\) if skew. When \(p\ne q\) are points, \(|\mathcal L(p)\setminus\mathcal L(q)|=t\) if collinear and \(t+1\) if noncollinear. The independent line and point coordinates contribute additively to the replacement cost. Through the \(s+1\) points of any line pass \(t\) other lines each, giving exactly \(t(s+1)\) intersecting other lines and \(st^2\) skew other lines. Dually, a point has \(s(t+1)\) other collinear points and \(ts^2\) noncollinear points. Multiplying the two single-coordinate enumerators proves the stated formula.

**5. Sharp threshold and diameter.** A change of line coordinate costs at least \(s\); a change of point coordinate at least \(t\). For \(k<\max\{s,t\}\) at least one coordinate cannot change, so the reconfiguration graph is disconnected. At \(k=\max\{s,t\}\), changing both coordinates costs at least \(s+t>k\). If \(s=t\), the permitted changes are exactly line intersections and point collinearities separately; if \(s>t\), the line coordinate permits intersections only while the point coordinate allows all pairs (because \(t+1\le s\)); the dual case is symmetric. This gives the three displayed Cartesian products. Every pair of lines intersects or admits a common intersecting line, and every pair of points is collinear or admits a common collinear point; therefore \(H_L,H_P\) are connected and have diameter two (there exist disjoint lines and noncollinear points since \(s,t\ge2\)). Complete graphs on these point and line sets have diameter one. Cartesian-product distances add, proving diameter four in the balanced case, three otherwise. Higher thresholds remain connected.

## Verification

Two reproducible finite checks accompany this proof. `verify_symplectic.py` independently constructs the symplectic generalized quadrangles of orders \((2,2)\) and \((3,3)\) over prime fields; it checks incidence axioms, all graph distances, MMD pairs, all proposed bases, pairwise exchange costs, threshold connectivity and graph distances. `verify_asymmetric.py` independently constructs the asymmetric generalized quadrangle \((2,4)\) using a 27-point double-six model; it uses separate clique enumeration and verifies the same assertions and the predicted diameter-three transition. Run either program using Python 3 standard library from a directory containing its packaged source; compare its JSON standard output with the corresponding packaged output file. The finite runs check particular geometries; the infinite-family assertion is proved by the preceding arguments.

For \((2,2)\), computations give 24-dimensional strong metric basis, 225 bases, and threshold diameter four. For \((3,3)\), these are 72, 1600 and four. For \((2,4)\), they are 64, 1215 and three. These are independent sanity checks, not claims that exhaustive finite testing establishes the theorem.

## Relationship to prior work

The equivalence between strong metric dimension and minimum vertex cover in the strong resolving graph is standard, originating in the work of Oellermann and Peters-Fransen and explicitly stated in the openly readable paper by Rodríguez-Velázquez, Yero, Kuziak and Oellermann (arXiv:1307.4722v1, 17 July 2013). The latter concerns graph products, not incidence graphs of generalized quadrangles. Bartoli, Héger, Kiss and Takáts (arXiv:1706.06583) study **ordinary** metric dimension of these incidence structures, a distinct resolving notion not implying the strong resolving graph, classification of strong metric bases, the exchange enumerator or the sharp exchange threshold. Search comparisons did not identify an antecedent covering the conjunction established here; this absence is not a formal proof of publication novelty.

## Limitations

The formulas apply only to finite thick generalized quadrangles satisfying the stated axioms. They do not assert existence of a generalized quadrangle for arbitrary integers \(s,t\). Reconfiguration is defined using simultaneous replacement of **up to** \(k\) selected vertices between two *minimum* strong metric bases; alternative token-sliding, intermediate-feasibility or labelled-token notions differ. The result uses established strong-resolution characterizations; the foundational 2007 paper's complete full text was not available for this comparison, and equivalences in unindexed literature or appendices cannot be excluded.

## References

1. O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, Discrete Applied Mathematics 155 (2007), 356–364, DOI: 10.1016/j.dam.2006.06.009.
2. J. A. Rodríguez-Velázquez, I. G. Yero, D. Kuziak and O. R. Oellermann, *On the strong metric dimension of Cartesian and direct products of graphs*, arXiv:1307.4722v1 (first posted 17 July 2013).
3. D. Bartoli, T. Héger, G. Kiss and M. Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, arXiv:1706.06583 (2017).
