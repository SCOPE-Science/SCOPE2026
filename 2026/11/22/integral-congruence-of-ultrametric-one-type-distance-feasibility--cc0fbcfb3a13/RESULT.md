# Integral congruence of ultrametric one-type distance-feasibility matrices

## Finding
Let \(r\geq1\), and let \(A\) be any nonempty finite ultrametric space whose nonzero distances belong to \(\{1,\ldots,r\}\). Individually name its points inside the countable universal homogeneous ultrametric space \(\mathbb U_r\) with this distance alphabet. For each \(j=1,\ldots,r\), let \(c_j\) count the equivalence classes of \(E_j(a,b)\), meaning \(d(a,b)\leq j\), on \(A\). In particular \(c_r=1\).

Write \(N=\sum_{j=1}^r c_j\). Index an integer symmetric matrix \(M_s\) by the \(N\) complete nonalgebraic one-point types over the individually named base \(A\), putting a one in position \((p,q)\) if distinct realizations of \(p,q\) can be at distance exactly \(s\) in \(\mathbb U_r\), and zero otherwise.

**Theorem.** There is an explicit unimodular integral congruence, for every \(s\in\{1,\ldots,r\}\), with
\[
M_1\cong_{\mathbb Z} I_N,
\]
and, for \(2\leq s\leq r\),
\[
\boxed{M_s\cong_{\mathbb Z}
\operatorname{diag}\left(
I_{c_s+\sum_{j=s+1}^{r}c_j},\ -I_{c_{s-1}},\ 0_{\sum_{j=1}^{s-2}c_j}
\right).}
\]
All empty sums and size-zero blocks are understood literally. Hence its nonzero Smith factors are **all one**; for \(s\geq2\), its rank over every field, nullity and real inertia are respectively
\[
\operatorname{rank}M_s=N-\sum_{j=1}^{s-2}c_j,\qquad
\operatorname{nullity}M_s=\sum_{j=1}^{s-2}c_j,
\]
\[
(n_+,n_-,n_0)=\left(c_s+\sum_{j=s+1}^{r}c_j,\ c_{s-1},\ \sum_{j=1}^{s-2}c_j\right).
\]
In particular, \(M_1\) and \(M_2\) are unimodular whenever \(M_2\) exists. For every \(1\leq j<r\), the number \(c_j\) is exactly the negative inertia index of \(M_{j+1}\). Thus the family of logical feasibility matrices recovers all levelwise partition counts of the old ultrametric space, without recovering its full tree shape.

## Assumptions and scope
A nonalgebraic one-point type is a complete type of a point unequal to every named member of \(A\), in the language naming all exact distance levels. Finite ultrametric extension and ultrahomogeneity imply that its data are precisely its distances to the named points. The universal space has the extension property for every finite ultrametric diagram with the indicated distance alphabet. The same matrix definition allows \(p=q\), but requires its two realizations to be *distinct*; this is crucial for its diagonal entries. Integral congruence means \(P^{\mathsf T}M_sP=D\) with \(P\in\operatorname{GL}_N(\mathbb Z)\), not ordinary similarity. For \(r=1\), only \(M_1=[1]\) occurs.

## Proof
**1. Complete type parametrization.** For an external point \(x\), put \(j=\min_{a\in A}d(x,a)\) and \(C=\{a\in A:d(x,a)=j\}\). Ultrametricity says that \(C\) is one \(E_j\)-class and that, fixing any \(a_0\in C\),
\[
d(x,a)=\begin{cases}j,&a\in C,\\ d(a_0,a),&a\notin C.\end{cases}
\]
Conversely every pair \((j,C)\) with \(C\) an \(E_j\)-class gives an admissible one-point extension; the finite-extension property realizes it. These pairs are distinct as named-distance vectors. Thus their number is \(N=\sum_j c_j\).

**2. Pairwise distance criterion.** Let \(p=(j,C)\) and \(q=(k,D)\), and fix \(a\in C\), \(b\in D\). If \(p\neq q\), the unique feasible mutual distance is
\[
h(p,q)=\max\{j,k,d(a,b)\}.
\]
The displayed number does not depend on the chosen representatives. Indeed, the cluster hierarchy shows that it is the level at which the two attachment nodes first merge; the two named-distance vectors differ at some old point, forcing the mutual distance to equal the larger of their two distances there. All three-point ultrametric inequalities then hold with this value. If \(p=q=(j,C)\), the feasible distances are exactly \(1\leq s\leq j\): the distance bound comes from an old point of \(C\), and every allowed value gives an admissible finite diagram. Since the latter diagram has two distinct new points at positive distance, the distinct-realization condition is satisfied.

**3. Blocks of a fixed matrix.** Fix \(s\geq2\). Any type \((j,C)\) with \(j>s\) contributes an isolated diagonal one, since it admits distance \(s\) with another realization of the same type and with no other type. There are \(\sum_{j>s}c_j\) such types. Every other type lies under a unique \(E_s\)-class \(U\), so the remaining matrix splits into independent blocks, one for each of the \(c_s\) classes.

Inside the block belonging to \(U\), write \(t=(s,U)\). Each \(E_{s-1}\)-class \(W\subseteq U\) contributes a nonempty family of descendant types \(\{(j,C):j\leq s-1,\ C\subseteq W\}\), containing its canonical representative \(u_W=(s-1,W)\). Entries within one such family are zero. Entries between two different families, between a family and \(t\), and at \((t,t)\) are all one. This is an exact classification of all entries, not merely a rank estimate.

**4. Explicit integral diagonalization.** In the free integral basis \(e_p\) indexed by types, replace the vectors of each \(U\)-block by
\[
e_t;\qquad e_{u_W}-e_t\quad(W\text{ a child of }U);\qquad
e_p-e_{u_W}\quad(p\neq u_W\text{ in the family of }W).
\]
These vectors form a unimodular basis: ordered by each rooted cluster, they are obtained from the original coordinate basis through elementary integer column subtractions. Their Gram matrix for \(M_s\) is exactly one positive unit for \(t\), one negative unit for each child \(W\), and a zero for every remaining descendant. Joining all blocks with the unchanged isolated positive units yields the displayed integral congruence. At \(s=1\), distinct types cannot realize distance one, while two distinct realizations of any one type can; hence \(M_1=I_N\).

**5. Consequences.** Unimodular congruence is a fortiori a unimodular row-column equivalence, and changing signs of negative units gives the stated Smith form. Its unit blocks remain nonsingular over every field, establishing the uniform rank. Sylvester's law gives the exact real inertia. The negative index of \(M_{j+1}\) is \(c_j\), so the matrices recover each threshold partition count.

## Verification
Run `python verify.py` from the directory containing this file. The standard-library program independently enumerates labelled finite ultrametrics on up to four old points for distance alphabets of sizes two through four, plus every five-point labelled ultrametric on three levels. It enumerates all admissible old-to-new distance vectors directly from triangle inequalities, independently compares all mutual-distance feasibility entries against the cluster-node criterion, constructs an explicit integer change-of-basis matrix and checks its determinant is \(\pm1\) by an exact Bareiss computation, verifies every entry of the resulting diagonal congruence, and checks ranks over the finite fields of characteristics two, three and five. The test covers 638 bases and 112842 matrix entries, ending with `VERIFICATION_OK`. These finite tests do not substitute for the all-size proof.

As a nonregular example, take four named points with one pair at distance one, a disjoint pair at distance two, and all cross distances four. For \(r=4\), \((c_1,c_2,c_3,c_4)=(3,2,2,1)\) and \(N=8\). The inertia triples for \(s=1,2,3,4\) are \((8,0,0),(5,3,0),(3,2,3),(1,2,5)\).

## Relationship to prior work
Nguyen Van Thé (2007), especially the tree/ultrametric correspondence and the homogeneous Urysohn construction, supplies the ambient hierarchy. Conant (first public version 2015), especially his ultrametric distance-monoid example, quantifier-free distance types and Proposition 4.2, supplies related model-theoretic distance constraints. Delhomme–Laflamme–Pouzet–Sauer (first public version 2015) present the nerve-of-balls tree and homogeneity framework. None of their inspected material states an integral congruence, Smith-form, inertia or old-cluster recovery theorem for the *distance-specific compatibility matrices on complete nonalgebraic one-point types*.

Relevant published results on colored-gap orbit profiles of ordered ultrametric expansions, finite-variable theories of homogeneous ultrametrics and distance-aware color refinement answer different questions: their objects are tuple orbits, logical indistinguishability of finite ultrametrics, and refinement of points, respectively. The current result works with the reduct without added orders and with matrices indexed by types **over an arbitrary named finite base**. A hierarchy/tree description by itself does not state the integral matrix diagonalization, though it is the starting input.

## Limitations
The alphabet is a fixed finite *chain* of positive distance values, and all finite diagrams must be ultrametric rather than general metric. The base is nonempty and individually named; there is no classification here of arbitrary generalized distance monoids, multivariate simultaneous realizability of three or more new points, or the ordinary eigenvalues. The Smith-form and inertia conclusions are independent of branching-shape details, but they do not recover the full ball tree. An equivalent formula may exist in older unindexed hierarchical-matrix or tree-incidence literature; historical priority is assessed against inspected accessible sources, not certified independently.

## References
1. L. Nguyen Van Thé, *Ramsey degrees of finite ultrametric spaces, ultrametric Urysohn spaces and dynamics of their isometry groups*, arXiv:0710.2347v1, first posted 2007-10-11, especially sections 2 and 5, https://arxiv.org/abs/0710.2347.
2. Gabriel Conant, *Neostability in countable homogeneous metric spaces*, arXiv:1504.02427, first posted 2015-04-09, especially Example 1.1, Section 4, Proposition 4.2, https://arxiv.org/abs/1504.02427.
3. C. Delhomme, C. Laflamme, M. Pouzet and N. Sauer, *On homogeneous ultrametric spaces*, arXiv:1509.04346, first posted 2015-09-14, especially Section 1 and the tree of balls, https://arxiv.org/abs/1509.04346.
4. *Colored-gap orbit profiles for minimal chain ultrametric expansions*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-colored-gap-orbit-profiles-for-minimal-chain-ultrametric-expansi--d80a1c925594/RESULT.md.
5. *Exact \(k\)-variable theories of finite homogeneous ultrametrics*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-k-variable-theories-of-finite-homogeneous-ultrametrics--752a3b45b841/RESULT.md.
6. *Distance-aware colour refinement on finite ultrametrics: two rounds suffice and eight points first defeat one*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-distance-aware-colour-refinement-on-finite-ultrametrics-two-roun--4e36345f61be/RESULT.md.
