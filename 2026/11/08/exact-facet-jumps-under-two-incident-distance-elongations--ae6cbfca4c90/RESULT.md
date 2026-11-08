# Exact facet jumps under two incident distance elongations

## Finding

Let \(N\ge4\). On a set \(M=\{a,b,c,z_1,\ldots,z_{N-3}\}\), set \(d_t(a,b)=d_t(b,c)=t\), and give every other distinct pair distance \(1\), for \(1\le t\le2\). The real Lipschitz-free space \(\mathcal F(M,d_t)\) has a full-dimensional \((N-1)\)-dimensional unit ball. Its **exact number of facets** is
\[
\boxed{F_N(t)=\begin{cases}
2^N-2,&t=1,\\[2pt]
7\cdot2^{N-2}-10,&1<t<2,\\[2pt]
2^N-4,&t=2.
\end{cases}}
\]
The formula is valid for every real parameter in the indicated intervals. All dual norming potentials (equivalently, every facet of the primal ball) are classified in the proof. The count is strictly larger in the open interval than at either endpoint, while the \(t=2\) count is precisely two less than the \(t=1\) count. The interior-to-equilateral facet ratio tends to \(7/4\) as \(N\to\infty\).

## Assumptions and scope

Throughout, the scalar field is real, \(N\) is an integer at least \(4\), and \(1\le t\le2\). The specified distances define a metric: the only possibly constraining triangle inequalities have the form \(t\le1+1\). Put \(m=N-3\ge1\). Normalize potentials by \(f(b)=0\). The dual unit ball is the polytope
\[
L_t=\{f:M\to\mathbb R:f(b)=0,\quad |f(x)-f(y)|\le d_t(x,y)\text{ for every }x,y\in M\}.
\]
The origin belongs to its interior in the \((N-1)\)-dimensional potential space. The primal unit ball is the polar of \(L_t\): it is the convex hull of normalized molecules \((\delta_x-\delta_y)/d_t(x,y)\). Accordingly, its facets are in bijection with vertices of \(L_t\). We count geometrically distinct facets, not oriented supporting inequalities with repetitions.

## Proof

**Tight-graph criterion.** For feasible \(f\), let \(H_f\) have vertices \(M\) and an edge \(xy\) precisely when \(|f(x)-f(y)|=d_t(x,y)\). Active rows of the defining inequalities of \(L_t\) are signed incidence vectors. After fixing \(f(b)=0\), they span dimension \(N-1\) exactly when \(H_f\) is connected. Thus \(f\) is an extreme point of \(L_t\) if and only if \(H_f\) is connected. Equivalently, a disconnected tight graph permits small independent shifts of one component, while a connected tight graph determines every potential value uniquely from its basepoint. This classical criterion is used, not claimed as new.

**Interior regime: no elongated edge is tight.** Fix \(1<t<2\). If \(H_f\) is connected and neither \(ab\) nor \(bc\) is tight, all edges of \(H_f\) have metric length \(1\). Consequently all potential differences along tight paths are integers, and every value is an integer because \(f(b)=0\). Every two distinct points have distance at most \(t<2\); the range of these integer values is therefore at most one. Nonconstancy and the normalization imply that the values lie in \(\{0,1\}\) or in \(\{-1,0\}\). It suffices to classify the positive binary assignments with values \(\{0,1\}\), because the negative ones are obtained by sign reversal.

Write \(u=f(a)\), \(v=f(c)\), and let the regular-point values \(f(z_j)\) lie in \(\{0,1\}\). Because \(ab\) and \(bc\) are not tight, connectivity gives the following exhaustive possibilities:

1. \((u,v)=(0,0)\): at least one regular value is \(1\), giving \(2^m-1\) assignments. Here the \(1\)-valued regular points connect both \(a,c\) to \(b\).
2. \((u,v)=(1,0)\) or \((0,1)\): at least one regular value is \(1\), giving \(2(2^m-1)\) assignments. The ordinary edge \(ac\) is tight and connects the distinguished vertices; a regular value \(1\) connects this component to \(b\).
3. \((u,v)=(1,1)\): both regular values \(0\) and \(1\) must occur, giving \(2^m-2\) assignments. The \(0\)-valued regular point connects \(a,c\), while a \(1\)-valued regular point connects \(b\), and their unit-distance edge joins these components.

In each listed case all vertices of the tight graph are connected, and in every excluded case at least one distinguished vertex or the basepoint component is isolated. There are \(4\cdot2^m-5\) positive binary vertices and equally many negatives. Hence the number of vertices of this type is \(8\cdot2^m-10\).

**Interior regime: a long edge is tight.** By sign reversal and exchanging \(a\) and \(c\), assume \(f(a)=t\) and \(f(b)=0\). The unit distances from both \(a\) and \(b\) to each regular point imply
\[
t-1\le f(z_j)\le1.
\]
Because the interval has width \(2-t<1\), no regular-regular unit edge can be tight. A regular point cannot have a tight edge to \(c\) unless \(f(c)=t\) and \(f(z_j)=t-1\), in which case that regular point is already tight to \(a\). Thus connectivity forces each regular point to satisfy \(f(z_j)=t-1\) (tight to \(a\)) or \(f(z_j)=1\) (tight to \(b\)). Also \(f(c)\in[t-1,t]\), by the unit edge \(ac\) and the long edge \(bc\). The only ways for \(c\) to have a tight incident edge are \(f(c)=t-1\) (edge \(ac\) tight) or \(f(c)=t\) (edge \(bc\) tight): for an intermediate value none of its edges to \(a,b\) or either regular level is tight. Conversely these endpoint choices and arbitrary independent regular choices in \(\{t-1,1\}\) make a connected tight graph. The distinct positive patterns are
\[
(f(a),f(c))\in\{(t,t),\ (t,t-1),\ (t-1,t)\},
\qquad f(z_j)\in\{t-1,1\}.
\]
The negative patterns are their sign reversals. There are therefore exactly \(6\cdot2^m\) vertices with an elongated tight edge, disjoint from the binary family. Adding both types gives
\[
(8\cdot2^m-10)+6\cdot2^m=14\cdot2^m-10
=7\cdot2^{N-2}-10.
\]

**Equilateral endpoint.** At \(t=1\), all distinct distances equal \(1\). The tight graph is connected precisely for nonconstant binary potentials after a common translation. There is one potential for every nonempty proper choice of an upper-level subset, hence \(F_N(1)=2^N-2\).

**Graph-metric endpoint.** At \(t=2\), the ordinary-tight-only argument still yields the same \(8\cdot2^m-10\) vertices: if all tight edges have length one, potential values are integers and an integer range of two would force one of the only distance-two pairs \(ab,bc\) to be tight. If a long edge is tight, normalize as above. Now all regular points are forced to have the common value \(1\), while \(f(c)\) can connect to the tight graph only at its endpoints \(1\) or \(2\). Exactly the six signed distinguished-pair configurations listed above remain, with one regular choice each. Their count is \(6\), producing
\[
F_N(2)=8\cdot2^m-10+6=8\cdot2^m-4=2^N-4.
\]
This direct classification also verifies that no extra endpoint vertices arise. Polar duality completes the facet count.

Finally, the strict jump sizes are \(F_N(t)-F_N(1)=3\cdot2^{N-2}-8>0\) and \(F_N(t)-F_N(2)=3\cdot2^{N-2}-6>0\) in the open parameter interval when \(N\ge4\). The three distinct regimes are therefore exhaustive. \(\square\)

## Verification

The standalone pure-Python file `check_adjacent_stretch.py` independently enumerates every feasible normalized integer-half-step potential for \(N=4,5,6\) and parameters \(t=1,3/2,2\), then tests tight-graph connectivity without using the closed facet formula to generate candidates. Every extreme point has a tight spanning tree, and all edge lengths in these tests are integers or half-integers, so the finite grid is mathematically exhaustive for each tested case. The checker reports `EXACT_VERTEX_ENUMERATION_PASS: 9 cases` and `ALL_ADJACENT_STRETCH_CHECKS_PASSED`. The argument above, not the finite enumeration, proves the universal count for every \(N\ge4\) and all real \(t\) in the indicated ranges.

## Relationship to prior work

Gordon and Petrov, *Combinatorics of the Lipschitz Polytope* (first arXiv version 2016-08-24), establish the general primal–dual polytope framework, tight-graph face dimension, and generic-metric face-number formula. Their generic-face count does not apply to the present highly symmetric nongeneric metric, and their general connectivity criterion does not itself give this explicit family-wide enumeration. Godefroy (online 2016-05-25) provides foundational Lipschitz-free Banach-space background.

The published *Sharp facet jumps for interpolated complete-multipartite Lipschitz-free balls* treats elongated pairs **inside disjoint equivalence classes**, which require transitivity of the long-pair relation. Here the two long edges share a vertex while the third pair \(ac\) remains short, so their long-edge graph is a three-vertex path, not a disjoint union of cliques. The published *Facet enumeration for equilateral metrics with independently shortened pairs* requires disjoint **shortened** pairs; it is not a covering parameterization. The published two-part snowflake facet formula concerns complete bipartite long-distance classes, likewise not this path family. A published inball-contact theorem for symmetric edge polytopes with degree-two deleted graphs concerns Euclidean insphere-tangent facets at the \(t=2\) graph endpoint, not the complete interior facet count.

The tight-edge method and endpoint graph-polytope framework are known. The contribution is the exhaustive two-incident-edge interior classification and its exact nonadditive three-regime facet law. The endpoint values are included for sharp comparison, not asserted to be previously unknown in isolation.

## Limitations

The result concerns finite real Lipschitz-free spaces with precisely two incident elongated pairs of **equal** length, all other distances one, and \(1\le t\le2\). It counts facets, not all face dimensions, Euclidean volumes, Banach–Mazur distances, or higher-dimensional face lattices. It does not cover independent unequal elongations, more than two elongated pairs, or arbitrary weighted metrics. Known general polyhedral criteria and limited finite computations are not presented as proofs of novelty. Equivalent results in unindexed combinatorial or transportation-polytope literature remain a bibliographic risk. No independent mathematical audit has been performed.

## References

1. G. Godefroy, *A survey on Lipschitz-free Banach spaces*, Comment. Math. 55(2) (2015), first verified online 2016-05-25, doi:10.14708/cm.v55i2.1104. https://pldml.icm.edu.pl/pldml/element/bwmeta1.element.ojs-doi-10_14708_cm_v55i2_1104
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848v1, first publicly posted 2016-08-24, https://arxiv.org/abs/1608.06848 . Original paper's Lemma 1 and Sections 1–2 establish the framework and generic/non-generic distinction.
3. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (2018). Background on finite-metric free-space structure.
4. K. Bredies, J. Chirinos Rodríguez and E. Naldi, *On extreme points and representer theorems for the Lipschitz unit ball on finite metric spaces* (2024), Section 2, for the general connected-tight-graph extremality method.
