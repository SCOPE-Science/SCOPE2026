# Upward-cone pair types detect Sackin balance in the universal homogeneous binary tree

## Finding
Let \((\mathbb S_2;<)\) be the countable existentially closed semilinear order, and let \(A\) be a nonempty, pointwise named finite antichain with \(n\) elements. Let \(T_A\) be its rooted, full binary leaf tree, recovered from the first-order definable ternary branching relation \(C\). Write \(S(T_A)=\sum_{a\in A}\operatorname{depth}_{T_A}(a)\), the classical Sackin index. In the definable positive upward cone
\[
U_A=\{x\in\mathbb S_2:\exists a\in A\ (a<x)\},
\]
let \(N_{<}(A),N_{>}(A),N_{\perp}(A)\) count complete types over \(A\) of ordered *distinct* pairs \((x,y)\in U_A^2\), according to whether \(x<y\), \(x>y\), or \(x\perp y\), respectively. Then
\[
\boxed{N_{<}(A)=N_{>}(A)=2S(T_A)+1,\qquad N_{\perp}(A)=2n(2n-1)-4S(T_A)-2.}
\]
The number of one-point types in \(U_A\) is \(2n-1\), and the total number of complete ordered-distinct pair types in \(U_A\) is \(2n(2n-1)\). Thus both unrefined counts are independent of the marked antichain's binary tree shape, whereas the three order-relation channels recover exactly its Sackin index.

The inequality \(N_{<}(A)\le n(n+1)-1\) is sharp, with equality exactly for caterpillar (comb) trees. Writing \(h=\lfloor\log_2 n\rfloor\), the sharp lower bound is
\[
N_{<}(A)\ge 2nh+4(n-2^h)+1;
\]
equality holds precisely for rooted binary trees whose leaf depths are \(h\) and \(h+1\) (with only depth \(h\) if \(n=2^h\)). These last extremal descriptions are classical consequences of the Sackin-index bounds, not newly claimed tree-index theorems.

If one chooses uniformly from these complete ordered-distinct pair types, the probability of comparable coordinates is
\[
\frac{N_{<}(A)+N_{>}(A)}{2n(2n-1)}=\frac{2S(T_A)+1}{n(2n-1)}.
\]
This probability can be as small as \(\Theta((\log n)/n)\) for optimally balanced trees, while for caterpillar trees it tends to \(1/2\). Thus the binary relational channels register a macroscopic change of logical-type balance that the total type count hides.

Different shape-dependent channel counts occur first for \(n=4\): a balanced rooted four-leaf tree has \((N_<,N_>,N_\perp)=(17,17,22)\), while a caterpillar has \((19,19,18)\), although both have 7 unary cone types and 56 ordered-distinct cone pair types.

## Assumptions and scope
A semilinear order has linearly ordered upper cone above every element and any two points have a common upper bound. We use the unique countable, dense, unbounded, nice, binary-branching semilinear order without joins. The definable expansion \((\mathbb S_2;\le,C)\) is homogeneous, with
\[
C(z,xy)\quad\Longleftrightarrow\quad x\perp y\ \wedge\ \exists u\,(x<u\wedge y<u\wedge u\perp z).
\]
This homogeneity identifies complete finite-parameter types with finite \((\le,C)\)-diagrams. Since \(A\) is an antichain, its rooted binary phylogenetic tree \(T_A\) has its old points as labelled leaves. The root and internal branch vertices are formal tree-combinatorial objects, not necessarily named elements of \(\mathbb S_2\). Each original tree vertex labels a nonempty clade of old leaves, and every clade is represented by a unique tree vertex. A formal stem above the root provides the edge associated with the root. All pair counts concern coordinates strictly above *at least one* old point and different from each other. No statement is made about pair types elsewhere in the structure.

## Proof
**Clade normal form.** For \(x\in U_A\), set \(B_x=\{a\in A:a<x\}\), which is nonempty. The semilinear property makes \(B_x\) a clade of \(T_A\). Indeed, a hypothetical old leaf lying inside the smallest rooted subtree spanning two members of \(B_x\), but not below \(x\), would contradict the rooted-triple relation \(C\) among those three leaves: \(x\) is a common upper bound of the first two, while the old rooted triple requires the third to join no later than one of them. Conversely, for every clade of \(T_A\) there is an upper point on the edge from that clade vertex toward its parent (using a stem above the root when necessary). It lies strictly above exactly the old leaves in that clade and is incomparable with all other named old leaves. This is realized by density, branching, no joins and the finite extension property. The complete \((\le,C)\)-diagram of \((A,x)\) is determined by this edge, and different clades are distinguished by \(B_x\). Thus there is exactly one cone one-type per vertex of \(T_A\), or \(2n-1\) one-types.

**Pair normal form.** Choose clades \(B_x,B_y\). If the clades are distinct, their edges in the rooted tree are distinct. An ordered pair of points placed on these two edges has exactly one possible \((\le,C)\)-diagram over \(A\). If \(B_x\subsetneq B_y\), semilinearity above any shared old point and set containment force \(x<y\). If \(B_y\subsetneq B_x\), they force \(y<x\). If the two nonempty clades are disjoint, \(x\perp y\) is forced. These possibilities exhaust the pairs of distinct clades because rooted-tree clades are laminar. When \(B_x=B_y\), the two distinct new points occupy the same ancestral edge; precisely two diagrams are possible, \(x<y\) and \(y<x\). Each is realizable by density. For different-edge choices, all \(C\)-relations with old points and among the new points are fixed by the expanded branching diagram. Homogeneity therefore excludes any further complete-type splitting.

Let \(V(T_A)\) be the tree's \(2n-1\) vertices. The number of ordered pairs of vertices \((v,w)\) for which \(v\) is a descendant of \(w\), *allowing equality*, is
\[
H(T_A)=\sum_{v\in V(T_A)}(\operatorname{depth}(v)+1).
\]
The pair-normal-form count gives \(N_{<}(A)=H(T_A)\), since each strict clade inclusion gives one \(x<y\) type and each diagonal clade pair gives exactly one \(x<y\) type. Reversing coordinates gives \(N_>(A)=H(T_A)\). Every pair of distinct clades yields one type and each diagonal pair yields two, so the total is
\[
(2n-1)^2+(2n-1)=2n(2n-1).
\]
Consequently the incomparability count is the stated difference.

**Depth identity.** We prove \(H(T)=2S(T)+1\) for every full rooted binary tree by induction on its number of leaves. For one leaf both sides equal one. If the two root subtrees have \(a,b\) leaves and are \(T_1,T_2\), then each of their \(2a-1\), respectively \(2b-1\), vertices gains one ancestor when placed under the new root. Thus
\[
H(T)=1+H(T_1)+H(T_2)+(2a-1)+(2b-1)=H(T_1)+H(T_2)+2(a+b)-1.
\]
Meanwhile \(S(T)=S(T_1)+S(T_2)+a+b\). The induction hypothesis proves the identity. Substitution yields both channel formulas.

**Sharp extrema.** The standard external-path-length (Sackin) bounds for rooted full binary trees are
\[
nh+2(n-2^h)\le S(T)\le \tfrac12n(n+1)-1,\qquad h=\lfloor\log_2 n\rfloor.
\]
The lower equality criterion is all leaves at depth \(h\) or \(h+1\), and the upper equality criterion is the caterpillar tree; these follow from balancing/exchange of leaf depths and can also be read from the classical tree-index extremal results cited below. Substitution in \(N_<=2S+1\) gives the assertions. Every binary tree with at most three leaves has the same unlabeled shape, while the four-leaf balanced and comb trees have Sackin indices eight and nine. Hence four is the sharp first shape-sensitive base size.

## Verification
The attached standard-library program `verify.py` generates all 48 unlabelled rooted binary tree shapes having one through eight leaves. For every shape it inserts two labelled new points on every ordered pair of ancestral edges (including both orders if they use the same edge), constructs a discrete rooted witness, and computes the **entire** finite \((<,C)\)-signature on the old leaves and new points. It deduplicates complete diagrams and checks all three channel counts, the total count, and the sharp Sackin-extremal numerical bounds. Its recorded output is `verification_output.txt`; running `python3 verify.py` reproduces it. The finite program corroborates the classification but does not establish the all-size theorem: that follows from the clade normal form and induction.

## Relationship to prior work
Bodirsky, Bradley-Williams, Pinsker and Pongrácz (2014) give the defining binary-branching semilinear structure, the definable relation \(C\), and homogeneity of \((\mathbb S_2;\le,C)\), but their full-text classification does not state the upward-cone marked-antichain pair spectrum or its Sackin-channel identity. Fischer (2021), building on classical external-path-length theory, establishes the sharp Sackin bounds and equality cases, which are used **as prior results** here. The new proposed connection is that these index values occur exactly as the comparable-pair orbit counts in a natural definable region of \(\mathbb S_2\), despite shape-independent unrefined counts.

Published results about the universal homogeneous meet-tree and homogeneous branching leaf \(C\)- or \(D\)-structures count different tuple orbits: meet-trees have a meet operation, while pure leaf relations lack the semilinear order and its positive upward cone. Their full orbit-profile formulas do not imply the present channel identity. Related finite-base studies of the generic partial order likewise concern a different, nonsemilinear amalgamation class. This distinction is mathematical rather than a claim that those papers have disjoint vocabulary.

## Limitations
The result addresses only nonempty finite antichain bases and the definable upward cone. It does not give a full arbitrary-base or unrestricted-pair type spectrum, and the channel histogram reconstructs only the Sackin index, not the entire labelled rooted tree. The classical Sackin bounds are not new. Literature-search coverage cannot rule out an unindexed or differently formulated prior observation of this model-theoretic identity. Independent mathematical audit remains unperformed.

## References
1. M. Bodirsky, D. Bradley-Williams, M. Pinsker, A. Pongrácz, *The Universal Homogeneous Binary Tree*, arXiv:1409.2170, first public version 2014-09-07; especially Sections 2 and 3.1 (definable \(C\) and homogeneity).
2. M. Fischer, *Extremal Values of the Sackin Tree Balance Index*, Annals of Combinatorics 25 (2021), 515–541, DOI:10.1007/s00026-021-00539-2; especially Theorems 1 and 2.
3. *Greg-tree orbit profile of the universal homogeneous meet-tree*, published published-finding corpus finding, 2026-10-04, repository identifier `c94a218292fe` (comparison for the different meet-tree structure).
4. *Exact tuple-orbit profile of the homogeneous 4-branching D-set*, published published-finding corpus finding, 2026-10-04, repository identifier `95b0894cb649` (comparison for leaf-hull orbit enumeration).
