# Sharp lattice Minkowski threshold for a fundamental pair of truncated Grassmannian polytopes

## Finding
For integers \(2\le d\le n-d\), let \(P_{d,n}=[d+1,n]\times[1,d]\) be the product poset. The generalized chain polytope integer sets \(S_m\) are defined below. For the two fundamental vectors \(e_2\) and \(e_d\), their lattice-point Minkowski decomposition satisfies the sharp criterion
\[
S_{e_2+e_d}=S_{e_2}+S_{e_d}\quad\Longleftrightarrow\quad d\le3\ \text{or}\ (d,n)=(4,8).
\]
Every \(d\ge4\) and \(n-d\ge5\) admits a counterexample, including the smallest example \((d,n)=(4,9)\). In that smallest example, the entire difference \(S_{e_2+e_4}\setminus(S_{e_2}+S_{e_4})\) consists of exactly **one** integer point: the indicator of the six cells
\[
(5,4),\ (6,3),\ (7,1),\ (7,4),\ (8,2),\ (9,1).
\]

## Assumptions and scope
Write \(h=n-d\ge d\). The elements of \(P_{d,n}\) are pairs \((i,j)\) with \(d+1\le i\le n\) and \(1\le j\le d\), ordered coordinatewise. For any subset \(Q\) of its cells, \(w(Q)\) is the maximum cardinality of a subset of pairwise incomparable cells. Set \(w(\varnothing)=0\). For \(m=(m_1,\ldots,m_d)\) with nonnegative integer entries, define
\[
S_m=\left\{x\in\mathbb Z_{\ge0}^{P_{d,n}}:\ \sum_{a\in Q}x_a\le\sum_{r=1}^d m_r\min(r,w(Q))\quad\text{for all }Q\subseteq P_{d,n}\right\}.
\]
Here \(e_r\) denotes the \(r\)-th coordinate unit vector. The set sum is the ordinary coordinatewise lattice-point sum, not equality of convex bodies or a statement about arbitrary weights. When \(d=2\), the two named vectors coincide and the expression is interpreted literally.

## Proof
**1. The fundamental sets and the height-two reduction.** Every \(x\in S_{e_r}\) is an indicator of an antichain with at most \(r\) cells. Indeed, width-one subsets give each coordinate at most one and prohibit any two comparable positive cells, while the full-poset inequality bounds support size by \(r\). Conversely, every such antichain indicator satisfies all defining inequalities. Thus \(S_{e_2}+S_{e_d}\) comprises sums of antichain indicators, the first of size at most two.

Fix \(x\in S_{e_2+e_d}\). Replace each cell \(a\) with \(x_a\) labeled copies, ordered so that all copies of the same cell form a chain and comparable cells have all their copies comparable. Every chain in this multiset poset has size at most two: otherwise its underlying cells, a width-one subposet, violate the defining bound \(\min(1,2)+\min(1,d)=2\). By the height-two antichain-partition theorem (Mirsky), all copies split into two antichains; their sizes sum to \(|x|=\sum_a x_a\le d+2\), where the latter inequality is the full-poset bound. If one antichain has size at most two, this produces the desired decomposition. For \(d\le3\), \(|x|\le5\), so one of the two classes necessarily has size at most two. This proves equality for \(d\le3\).

**2. Reduction of the exceptional four-column case to a six-point double star.** Let \(d=4\). A nondecomposable \(x\in S_{e_2+e_4}\) must have \(|x|=6\), since the argument above handles smaller sizes. Form the comparability graph \(G\) of its six labeled copies. It is bipartite by the height-two property. Every proper bipartition of \(G\) must have sizes \(3+3\); otherwise the smaller class, of size at most two, would give a decomposition. Flipping the coloring on any connected component then shows that every component has equally many vertices on each side.

If \(G\) is disconnected, every component has at most four vertices. A connected balanced bipartite graph on two or four vertices has a perfect matching. Taking these matchings across the components would give three disjoint comparable pairs. Their underlying cells form a subposet of width at most three, because they are covered by three chains; the six copies on it violate the width-three inequality \(6\le\min(3,2)+\min(3,4)=5\). Therefore \(G\) is connected, with bipartition \(3+3\), and it has no matching of size three.

By König's bipartite matching–vertex-cover theorem, \(G\) has a vertex cover of size at most two. A cover of size one would be a star and contradict the balanced bipartition, so a minimum cover has exactly two vertices. The two covering vertices lie on opposite sides: if they lay on one side, the third vertex of that side would be isolated, contrary to connectedness. All other vertices are leaves attached to one of the two covering vertices; connectivity forces those two vertices to be adjacent. The bipartition sizes then force two leaves at each center. Hence \(G\) is the six-vertex **double star**, the tree with degree sequence \((3,3,1,1,1,1)\). Its six cells must be distinct: a repeated cell would be adjacent to the same neighbors as its duplicate, creating a triangle if either copy had a neighbor, whereas \(G\) is a connected tree.

**3. The exact finite obstruction census.** Enumerate the six-element subsets of the \(h\times4\) product grid and retain those whose comparability graph is a double star (degree sequence \((3,3,1,1,1,1)\) with adjacent degree-three vertices). The attached exact-integer verifier, `verify.py`, checks all \(\binom{16}{6}=8008\) subsets in a \(4\times4\) grid and finds **zero** double stars. Step 2 proves that \(S_{e_2+e_4}=S_{e_2}+S_{e_4}\) for \((d,n)=(4,8)\).

For the \(5\times4\) grid, the verifier checks all \(\binom{20}{6}=38760\) six-subsets and finds **exactly one** double star, with row/column coordinates numbered from zero:
\[
(0,3),\ (1,2),\ (2,0),\ (2,3),\ (3,1),\ (4,0).
\]
This corresponds to the displayed cells after adding five to the row index and one to the column index. It has two degree-three centers, a matching of size two, and no matching of size three. Its indicator belongs to \(S_{e_2+e_4}\): any subset of its six cells of width \(k\) is covered by \(k\) chains (Dilworth), and the induced comparability graph has height at most two and matching number at most two. Consequently it contains no more than \(k+\min(k,2)\) cells, the exact required bound for \(k\le4\). Its balanced, connected bipartite comparability graph admits no proper two-coloring with a class of size at most two, so it does not lie in the lattice-point sum. Step 2 and the exhaustive six-subset census establish that this is the **only** missing lattice point for \((d,n)=(4,9)\).

**4. Uniform propagation.** The same six cells, interpreted in the initial five rows and first four columns of any product grid with \(h\ge5\) and \(d\ge4\), retain their order relations. For every subset of width \(k\), the preceding chain-cover argument yields no more than \(k+\min(k,2)\) points; this is at most \(\min(d,k)+\min(2,k)\) since the six-cell support has width four and \(d\ge4\). Thus its indicator belongs to \(S_{e_2+e_d}\) in every such grid. Nondecomposability follows again from the connected balanced double-star comparability graph. For \(d\ge5\) the standing hypothesis \(h\ge d\) already implies \(h\ge5\). These are precisely all remaining cases, completing the sharp classification.

## Verification
Run `python3 verify.py` with Python's standard library. It performs exact comparability and antichain tests, checks all subsets of the explicit witness against the polytope inequalities, exhaustively tries all splittings of the witness into a small and a complementary antichain, and checks the complete \(4\times4\) and \(5\times4\) double-star censuses. The expected final marker is `CERTIFICATE_OK`, followed by counts `0` and `1`. These checks certify the finite classification steps, while the preceding argument supplies the infinite-parameter proof. No numerical tolerance or sampled enumerations are used for the finite steps.

## Relationship to prior work
Feigin and Makhlin, *Truncated Grassmannians: polytopes, representations, and Cauchy formulas* (arXiv:2610.40891v1, October 29, 2026), introduce the generalized chain polytopes and relate their lattice points to monomial bases. Their Section 3 establishes additivity for the first/last fundamental-weight special case, while Example 4.4 demonstrates nonadditivity for the pair \(e_2,e_6\) at \((d,n)=(6,12)\). The present theorem determines the **sharp threshold for the specific pair** \(e_2,e_d\), proves the previously unlisted minimal obstruction at \((4,9)\), and completely classifies its single missing integer point. It does not assert additivity of other weight pairs or an entirely new family of polytopes. Earlier work on marked chain-order polytopes concerns a different construction and does not state this threshold.

## Limitations
This theorem concerns lattice-point Minkowski sums for the designated fundamental pair, not all weight vectors, and not an equivalence of arbitrary polytopal Minkowski sums. The exact \(4\times4\) and \(5\times4\) classifications use a fully reproducible finite exhaustion; their correctness is conditional on running the transparent checker, which has been tested with exact integers. Literature comparisons support priority only to the extent of the sources inspected, not exhaustive historical uniqueness; independent mathematical review has not been performed.

## References
- E. Feigin and I. Makhlin, *Truncated Grassmannians: polytopes, representations, and Cauchy formulas*, arXiv:2610.40891v1 (2026), Sections 3–4, especially Corollary 3.3 and Example 4.4; https://arxiv.org/abs/2610.40891.
- I. Makhlin, *Chain-order polytopes: toric degenerations, Young tableaux and monomial bases*, arXiv:2211.03499v4 (2024); https://arxiv.org/abs/2211.03499.
- Standard finite-poset results: Dilworth's chain-cover theorem, Mirsky's antichain-partition theorem, and König's bipartite matching/vertex-cover theorem.
