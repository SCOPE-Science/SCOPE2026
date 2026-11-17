# Three-map phase transition for weighted disconnected graph-covering averages

## Finding
Let \(X\) be a finite connected topological graph and let \(p:Z\to X\) be a connected covering of degree \(d\ge2\). Put \(Y=X\sqcup Z\), with covering \(q=\mathrm{id}_X\sqcup p\). For every \(w\in[0,1]\), define the real Markov operator \(A_w:C(Y)\to C(X)\) by
\[
(A_w f)(x)=(1-w)f(x\text{ in the identity component})+\frac{w}{d}\sum_{z\in p^{-1}(x)}f(z).
\]
Let \(\mathcal E_3\) be all convex combinations of at most three composition operators \(C_h f=f\circ h\), where \(h:X\to Y\) is continuous and the convex weights are arbitrary nonnegative real numbers. Then the operator-norm distance is attained and equals
\[
\boxed{\operatorname{dist}(A_w,\mathcal E_3)=
\begin{cases}
2w(d-1)/d, &0\le w\le d/(d+1),\\
2/3, &d=2,\ d/(d+1)\le w\le1,\\
2-4w/d, &d\ge3,\ d/(d+1)\le w\le1.
\end{cases}}
\]
At the universal phase boundary \(w=d/(d+1)\), two distinct explicitly constructed families tie: one composition operator supported on the identity sheet together with two supported on \(Z\), versus three supported entirely on \(Z\). Away from the boundary the smaller of these two families gives the stated distance. No uniqueness of the minimizers is asserted.

## Assumptions and scope
A finite topological graph is a compact connected one-dimensional CW complex with finitely many edges (loops permitted). The covering \(p\) is unramified and its total graph \(Z\) is connected. Existence entails a base with a nontrivial fundamental group. Real \(C\)-spaces carry the supremum norm. In particular \(X\) is connected and the images of continuous \(h:X\to Y\) lie in one component of \(Y\). We allow repeated maps, zero convex coefficients and endpoint weights \(w=0,1\). We make no restrictions requiring the maps \(h\) to respect the covering.

Every operator in the convex hull is a Markov operator. For its representing probability measures \(\nu_x\) and the target probability measures \(\mu_x\), define the atomic overlap
\[
O_x=\sum_{y\in q^{-1}(x)}\min\{\mu_x(\{y\}),\nu_x(\{y\})\}.
\]
The total-variation and Riesz-representation formulas give \(\|A_w-R\|=2(1-\inf_{x\in X}O_x)\). Here the target fiber atoms have masses \(1-w\) on the identity component and \(w/d\) on each of the \(d\) points in \(Z\).

## Proof
**1. No section on the nontrivial component.** A section of the connected degree-\(d\) covering \(p:Z\to X\) would have a nonempty image that is both open and closed in \(Z\), contradicting connectedness and \(d\ge2\). Consequently each continuous map \(h:X\to Z\) misses the appropriate fiber at some base point.

**2. The lower bound when at most two approximating maps land in \(Z\).** If none or only one of the at most three maps lands in \(Z\), choose a point where the latter map misses the fiber (if present). At that point the overlap is at most \(1-w\), so the error is at least \(2w\). If exactly two maps land in \(Z\), select one and choose a point where it misses its fiber. At that point at most one remaining atom can cover any point of the nontrivial fiber, with overlap at most \(w/d\), while the identity component contributes at most \(1-w\). Thus the error is at least
\[
a_d(w)=2w(1-1/d).
\]
This bound remains true when some coefficients vanish.

**3. The lower bound when all three maps land in \(Z\).** Choose a term of maximal coefficient, at least \(1/3\), and a point where its map misses the fiber. The two remaining terms have combined mass at most \(2/3\) and can cover at most two distinct fiber atoms, each of target mass \(w/d\). Therefore \(O_x\le\min\{2/3,2w/d\}\), giving the lower bound
\[
b_d(w)=2\bigl(1-\min\{2/3,2w/d\}\bigr).
\]
The two cases imply \(\|A_w-R\|\ge\min\{a_d(w),b_d(w)\}\) for every \(R\in\mathcal E_3\).

**4. A one-fiber two-map covering lemma.** There exist two continuous maps \(h_1,h_2:X\to Z\) such that at every \(x\), at least one of \(h_1(x),h_2(x)\) lies in \(p^{-1}(x)\). Choose arbitrary points over each vertex for each map. On each oriented edge, track both corresponding lifts until an interior subinterval; keep the second map on a correct lift while transporting the first along a path in connected \(Z\) to its prescribed terminal sheet, and then keep the first on a correct lift while transporting the second. Each transport exists because the finite connected graph \(Z\) is path connected. The edgewise maps glue at their fixed vertex values. This proves the lemma for loops as well.

**5. A two-distinct-fiber three-map covering lemma.** There exist three continuous maps \(g_1,g_2,g_3:X\to Z\) such that, for each \(x\), at least two of the points \(g_j(x)\) belong to \(p^{-1}(x)\) and are distinct. Here is a finite combinatorial proof of the required guarded transport. Label the \(d\) lifts above an edge by \(\{1,\ldots,d\}\). Consider ordered triples of labels with at least two distinct entries. Permit changing one coordinate precisely when the two unchanged coordinates are distinct. This move graph is connected: the six nonconstant triples on any fixed pair of labels form a connected cycle; triples with three distinct labels connect to one of these cycles in one move; and cycles for pairs sharing a label connect through two moves, for example \((a,b,a)\to(a,b,c)\to(a,a,c)\). The pair graph is connected, so all allowed triples communicate. At each vertex choose an arbitrary triple with at least two distinct points over it. Along each oriented edge, route its initial triple to the required terminal triple through guarded changes of sheet labels. During a change only one map leaves its correct lift and travels along a path in connected \(Z\); the other two track distinct correct lifts. Since each edge has finitely many changes, the three continuous maps glue on \(X\). This proves the lemma for every \(d\ge2\).

**6. Matching upper bounds.** For the identity-sheet strategy, take the exact inverse section of the identity component with coefficient \(1-w\), together with the two maps from step 4, each of coefficient \(w/2\). At every \(x\), the nontrivial fiber receives at least one atom of mass \(w/2\ge w/d\). Thus the overlap is at least \(1-w+w/d\), and the error is at most \(a_d(w)\). For the all-nontrivial strategy, average the three maps from step 5 with coefficients \(1/3\). At least two distinct fiber points carry approximating mass \(1/3\), so the overlap is at least \(2\min\{w/d,1/3\}\), and the error is at most \(b_d(w)\). Both constructions use exactly three or fewer global continuous composition maps.

Combining with steps 2–3 proves the sharp formula \(\delta_d(w)=\min\{a_d(w),b_d(w)\}\) and attainment. When \(d\ge3\), \(w/d\le1/3\), so \(b_d(w)=2-4w/d\); it crosses \(a_d(w)\) at \(w=d/(d+1)\). When \(d=2\), \(a_2(w)=w\), while \(b_2(w)=2\max\{1-w,1/3\}\); their minimum is \(w\) below \(2/3\) and \(2/3\) above. This completes the proof.

## Verification
The analytical proof establishes all degrees, all weights, and all graph-covering topologies under the hypotheses; it does not rely on finite experiments. The standalone Python 3 program `checker.py` tests the guarded-move graph connectivity for degrees \(2\) through \(9\), verifies exactly 4,214 rational phase identities in degrees \(2\) through \(15\), and checks equality of the two branches at the critical mass. The executed output was `THREE_MAP_COVER_CHECK_OK 4214 phase identities; guarded triple graph connected for d=2..9`. These computations are finite consistency checks, not exhaustive proof of the infinite parameter and topology claims.

## Relationship to prior work
Duru, İlter and Bilgin [1, Theorems 1.1–1.2] determine arbitrary- and equal-weight \(m\)-term distances for a **single connected covering with uniform fibers**. Their fiber-overlap identity and atomic-transport approach motivate the present problem, but those results do not evaluate a mixture involving an identity component and a nontrivial covering component. The published *Exact two-map approximation of componentwise-weighted disconnected covering averages* [2] gives a complete **two-map** formula for general component decompositions; it expressly leaves three or more maps outside its scope. The present three-map theorem is therefore not its two-map formula under parameter substitution: it involves a new two-distinct-sheet guarded construction and a topology-dependent switch in optimal support allocation. The three-map case is the first budget at which two persistent fiber witnesses can coexist while another approximation atom moves.

## Limitations
The theorem concerns one identity component and one connected nontrivial component, with componentwise constant weights and a budget of three extreme maps. It does not settle arbitrary disconnected coverings, budgets of four or more, base-dependent fiber probabilities, or uniqueness of minimizing mixtures. Earlier nonindexed formulations of continuous-map Markov approximation may be relevant to publication priority; the 1966 paper of Brown [3] and the 1972 paper of Kim [4] are bibliographic risks and are not claimed to have been exhaustively checked here.

## References
[1] H. Duru, S. İlter, and A. Bilgin, *Sharp Norm Approximation of Covering Markov Operators*, arXiv:2610.35575v1 (first submitted 2026-10-26), https://arxiv.org/html/2610.35575v1.

[2] *Exact two-map approximation of componentwise-weighted disconnected covering averages* (public research record, 2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-map-approximation-of-componentwise-weighted-disconnect--25459b8578e0.

[3] J. R. Brown, *Approximation theorems for Markov operators*, Pacific Journal of Mathematics (1966), https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-16/issue-1/Approximation-theorems-for-Markov-operators/pjm/1102994822.full.

[4] K. C. Kim, *Approximation theorems for Markov operators* (1972), https://doi.org/10.1007/BF00538394.
