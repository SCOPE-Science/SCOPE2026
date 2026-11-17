# The first Euclidean radial vertex shell of chainlink polytopes

## Finding
Let \(s\geq2\), \(\ell>0\), and \(a_1,\ldots,a_s\geq2\ell\) be real numbers. For the standard Euclidean chainlink polytope \(P=\mathrm{CL}(\mathbf a,\ell)\), its unique minimum enclosing sphere has center \(c=\mathbf a/2\) and squared radius \(R^2=\tfrac14\sum_i a_i^2\); exactly the two vertices \(0\) and \(\mathbf a\) touch it. Write \(b=\min_i a_i\) and \(m=\#\{i:a_i=b\}\). Among every other vertex \(v\), the sharp squared-radius deficit is
\[
\min_{v\in\mathrm{vert}(P)\setminus\{0,\mathbf a\}}\bigl(R^2-\|v-c\|^2\bigr)=\ell(b-\ell).
\]
The entire first interior radial vertex shell consists of exactly \(2m(s-1)\) vertices when \(b>2\ell\), and exactly \(ms\) vertices when \(b=2\ell\). The change at equality is a genuine collision of two different endpoint patterns, not a change in the radial gap formula.

## Assumptions and scope
The cyclic indices are modulo \(s\), and the polytope is in the inherited *ordinary* Euclidean coordinates:
\[
P=\bigl\{x\in\mathbb R^s:0\leq x_i\leq a_i,\quad x_i-x_{i+1}\leq a_i-\ell\ (1\leq i\leq s)\bigr\}.
\]
The link \(\ell\) and lengths \(a_i\) are arbitrary real numbers in the stated ranges; no integrality or symmetry is assumed. The result concerns the finite set of **vertices**, not all points of \(P\). The ambient dimension is \(s\), including \(s=2\).

For an explicit description of the first interior shell, choose an index \(j\) with \(a_j=b\) and an integer \(r\) between \(0\) and \(s-1\). Set \(v_{j-k}=a_{j-k}\) for \(1\leq k\leq r\), and set the remaining coordinates other than \(j\) to zero. Set \(v_j\) as follows:

- When \(b>2\ell\), take \(v_j=\ell\) with \(1\leq r\leq s-1\), or take \(v_j=b-\ell\) with \(0\leq r\leq s-2\).
- When \(b=2\ell\), take \(v_j=\ell=b-\ell\) with \(0\leq r\leq s-1\).

Each choice yields a distinct vertex, and these are all the first-shell vertices.

## Proof
**Outer sphere and its uniqueness.** The inclusion \(P\subseteq\prod_i[0,a_i]\) gives \(\|x-\mathbf a/2\|\leq\|\mathbf a\|/2\). Both \(0\) and \(\mathbf a\) belong to \(P\), so every enclosing ball has radius at least half their distance, with equality forcing center \(\mathbf a/2\). Equality in the box radius inequality forces every coordinate to equal either \(0\) or \(a_i\). A mixed cyclic binary selection contains a cyclic transition from \(a_i\) to \(0\), violating \(x_i-x_{i+1}\leq a_i-\ell\), since \(\ell>0\). Thus the two displayed vertices are the only sphere contacts.

**Universal lower bound.** Define the nonnegative radial deficit
\[
\Delta(x)=R^2-\|x-c\|^2=\sum_{i=1}^s x_i(a_i-x_i).
\]
A vertex other than \(0\) and \(\mathbf a\) has a coordinate strictly between its two box endpoints. Since an isolated such coordinate leaves fewer than \(s\) active box constraints, at least one cyclic difference constraint must be tight, say \(x_i-x_{i+1}=a_i-\ell\). Put \(t=x_{i+1}\). The box inequalities imply \(0\leq t\leq\ell\), and \(x_i=a_i-\ell+t\). Their two nonnegative contributions to \(\Delta\) total
\[
f(t)=(a_i-\ell+t)(\ell-t)+t(a_{i+1}-t).
\]
This is strictly concave with \(f''(t)=-4\); therefore
\[
f(t)\geq\min\{f(0),f(\ell)\}
=\ell\min\{a_i-\ell,a_{i+1}-\ell\}
\geq\ell(b-\ell).
\]
Every other coordinate contributes nonnegatively, proving the lower bound. Strict concavity shows equality requires \(t\in\{0,\ell\}\), a single non-box coordinate in an index \(j\) where \(a_j=b\), and box endpoints in every other coordinate. Its non-box coordinate is \(\ell\) or \(b-\ell\).

**Classification and attainment.** Feasibility prohibits any full-to-zero transition in the cyclic coordinates. Hence the full coordinates other than \(j\) must be one consecutive backward block of length \(r\), and all other coordinates zero, exactly as described above. If \(b>2\ell\), a vertex with the middle value \(\ell\) needs a full predecessor to make a cyclic difference facet tight, so \(r\geq1\). A vertex with the middle value \(b-\ell\) needs a zero successor, so \(r\leq s-2\). Conversely, each listed point meets the box constraints in \(s-1\) independent coordinates and meets an additional cyclic difference facet; it is feasible and is a vertex. If \(b=2\ell\), these two possible middle values coincide, while for every \(r\) there remains a tight difference facet (at the predecessor or successor). The listed points are again vertices. Their deficits are all \(\ell(b-\ell)\), giving equality. Counting \(s-1\) possibilities for each of two distinct middle values and each of \(m\) minimal indices gives \(2m(s-1)\); at the degeneracy, there are \(s\) possibilities per minimal index, giving \(ms\). All listed vertices have exactly one non-box coordinate, making these parametrizations injective. This proves both the metric and multiplicity claims.

## Verification
An independently implemented exact rational halfspace-intersection checker enumerates all vertices by solving every independent \(s\)-tuple of supporting hyperplane equations and checking all defining inequalities. It compares both the sharp deficit and the **complete set** of equality vertices against the formula. Running `python3 verify.py` returns `CHAINLINK_EXACT_INTERSECTION_PASS profiles=237`, across \(s=2,3,4\), links \(\ell=1,2\), both strict and degenerate regimes, and selected five-dimensional examples. A separate numerical halfspace computation was also run on 1,016 parameter profiles with dimensions up to six. These finite tests corroborate, but do not replace, the analytic all-real-parameter proof.

## Relationship to prior work
Kantarcı Oğuz, Özel, and Ravichandran introduced chainlink polytopes and proved their complementary-section Ehrhart equivalence. Their Section 6 gives the finite vertex-coordinate possibilities, a transfer-matrix total vertex count, and simplicity in the strict-link regime. Those results are useful for understanding feasible vertex patterns but do not explicitly classify the closest noncontacting vertices to the outer sphere, their sharp metric deficit, or the exact parameter-boundary collision. Existing studies of chainlink-section inradii, diameters, and global Minkowski asymmetry concern different invariants and do not state this first *full-polytope vertex* radial shell. The extremal formula and its equality classification are proved directly here rather than inferred merely from searches or titles.

## Limitations
This is the first nonouter **vertex** radial level only; it makes no claim about higher vertex shells, the radial distribution of uniform interior points, or distances along edges. The surrounding box supplies the trivial outer sphere, while the genuine classification concerns the sharp next shell and its change in multiplicity. The original paper's vertex encoding could support other derivations of this metric extremum, and unindexed equivalent work remains a priority risk. Independent mathematical validation is not asserted.

## References
1. E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1 (first public version November 15, 2022), especially Sections 1 and 6, https://arxiv.org/abs/2211.08382.
2. *Cyclic-interval formula and order-sensitive Minkowski asymmetry of chainlink polytopes*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-cyclic-interval-formula-and-order-sensitive-minkowski-asymmetry--b2f3468c4f4e.
3. *Six Euclidean inball phases of complementary chainlink sections*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-six-euclidean-inball-phases-of-complementary-chainlink-sections--c9e534b71133.
