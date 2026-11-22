# Punctured join-Grothendieck spaces have rigid spherical coordinate strata

## Finding

Let \(\mathcal S\) denote the monoid of isomorphism classes of finite abstract simplicial complexes under join, with identity the complex consisting only of the empty face. Its Grothendieck group \(G=K(\mathcal S)\) has the signed-divisor Alexandrov partial order introduced in [1]. Write \(I\) for the set of isomorphism classes of join-prime complexes. For any distinct \(i_1,\ldots,i_r\in I\), where \(r\ge1\), let \(G_J\) be the subgroup they generate and let \(P_J=G_J\setminus\{0\}\), with the induced partial order. Here the order complex \(\Delta(P)\) has nonempty finite chains of \(P\) as its simplices.

**Theorem.** For every such \(J\), the signed permutation group \(W_J\cong C_2^r\rtimes S_r\) acts on \(P_J\) by Alexandrov homeomorphisms and:

1. There is a \(W_J\)-equivariant homotopy equivalence of geometric realizations \(|\Delta(P_J)|\simeq S^{r-1}\), where the sphere is the boundary of the \(r\)-cross-polytope with its usual signed-coordinate action. Thus \(\widetilde H_{r-1}(|\Delta(P_J)|;\mathbb Z)\cong\mathbb Z\) and all other reduced integral homology groups vanish.
2. The **full** group of homeomorphisms of the Alexandrov space \(P_J\) is exactly \(W_J\). Its action on the top integral homology in (1) is the determinant character \(\det:W_J\to\{\pm1\}\).
3. The simultaneous-inversion quotient \(|\Delta(P_J)|/\{\pm1\}\) is homotopy equivalent to \(\mathbb{RP}^{r-1}\); in particular, for \(r=3\), the quotient has integral first homology \(\mathbb Z/2\mathbb Z\).
4. The order complex of the full punctured group \(G\setminus\{0\}\) is contractible, in contrast to the spheres of every finite positive rank.

In the topology on \(P_J\) itself, assertion (1) gives **weak** homotopy equivalence to the sphere, by McCord's comparison theorem; it does not identify the non-Hausdorff finite-space model with a Hausdorff sphere by an ordinary homotopy equivalence.

## Assumptions and scope

By the unique-factorization theorem [1, Theorem 3.14], \(G=\bigoplus_{i\in I}\mathbb Z e_i\). The order [1, Theorem 4.1] is not the additive order: for finite-support coordinate vectors \(x,y\),
\[
x\preceq y\iff\text{for every }i,\quad x_i=0\quad\text{or}\quad(x_i y_i>0\text{ and }|x_i|\le|y_i|).
\]
Thus \(0\) is a least element, and positive and negative directions in a coordinate are incomparable above it. Every element has finite support. The rank-\(r\) subgroups are formed by choosing distinct *prime factors*, not arbitrary integral linear combinations of them. All homotopy types of order complexes are those of their geometric realizations with CW topology. The quotient in (3) refers to this realization, not a homeomorphism assertion for the Alexandrov quotient space.

## Proof

**Step 0: an independent factorization check for the starting object.** For any finite abstract simplicial complex \(K\), form its *minimal-nonface hypergraph*: vertices are those of \(K\), and hyperedges are the inclusion-minimal subsets not in \(K\). Its connected components partition the vertex set, including isolated vertices. Every minimal nonface lies in one component, so a subset is a face of \(K\) exactly when each of its componentwise intersections is a face. Thus \(K\) is the join of its induced subcomplexes on these components. Conversely, if \(K=A*B\) is a nontrivial join, no minimal nonface meets both factor vertex sets, so each hypergraph component lies wholly in one factor. This proves the required uniqueness of the join-prime multiset independently of the cited unique-factorization theorem, including isolated single-vertex factors. Cancellation and the finite-support free-abelian Grothendieck coordinate description follow.

**Step 1: canonical signed-support retraction.** In coordinates \(J\), define \(s(x)_i=\operatorname{sgn}(x_i)\). For every \(x\in P_J\), \(s(x)\ne0\), \(s(x)\preceq x\), and \(s(s(x))=s(x)\). Comparability of \(x\preceq y\) implies \(s(x)\preceq s(y)\), so \(s\) is an order-preserving retraction onto the subposet \(B_J=\{-1,0,1\}^J\setminus\{0\}\). The comparison \(s\preceq\mathrm{id}\) supplies a natural transformation of poset maps, hence an equivariant simplicial homotopy between the maps induced on order complexes. This is an explicit \(W_J\)-equivariant homotopy equivalence.

**Step 2: identify the sphere and orientation action.** Interpret each nonzero sign vector as a nonempty collection of vertices from \(\{+e_i,-e_i:i\in J\}\), containing at most one vertex from each antipodal pair. These are exactly the nonempty proper faces of the cross-polytope \(C_r=\operatorname{conv}\{\pm e_i\}\). Therefore \(\Delta(B_J)\) is the barycentric subdivision of \(\partial C_r\), a triangulated \((r-1)\)-sphere. The cross-polytope boundary is the join of \(r\) copies of \(S^0\). Its integral fundamental cycle can be expressed as the oriented join \(\bigast_{i\in J}([+e_i]-[-e_i])\). Reversing one coordinate multiplies this cycle by \(-1\), and exchanging two coordinate factors contributes \(-1\) by graded commutativity of the oriented join. Hence the top-homology character is exactly the determinant of the signed permutation.

**Step 3: rigidity of homeomorphisms.** As a \(T_0\) Alexandrov space, \(P_J\) has homeomorphisms exactly its order automorphisms. Its minimal elements are precisely the \(2r\) signed atoms \(\pm e_i\). Two different atoms have no common upper bound if and only if they are \(e_i,-e_i\) for one \(i\). Thus every automorphism must permute the \(r\) opposite pairs, choosing an optional swap within each: it induces an element of \(W_J\). Compose with the inverse of that signed permutation to fix all atoms. Every higher element \(x\) has immediate predecessors \(x-\operatorname{sgn}(x_i)e_i\) for all nonzero coordinates \(i\), discarding the zero vector. This predecessor set determines \(x\) uniquely: with at least two nonzero coordinates it reconstructs each signed coordinate by its maximal absolute value among the predecessors, while with exactly one nonzero coordinate it is the unique axis element covering its predecessor. By induction on \(\sum_i|x_i|\), an order automorphism fixing atoms fixes every element. Conversely, all signed permutations preserve the stated order. So \(\operatorname{Homeo}(P_J)=W_J\).

**Step 4: quotient.** Simultaneous inversion \(x\mapsto-x\) commutes with the retraction of Step 1. Its geometric action on \(\partial C_r\) is antipodal. The induced equivariant homotopies descend to the order-complex orbit spaces; hence their quotients are homotopy equivalent, giving \(|\Delta(P_J)|/\{\pm1\}\simeq \partial C_r/\{\pm1\}\cong\mathbb{RP}^{r-1}\). In rank three, \(H_1\cong\mathbb Z/2\mathbb Z\). The action is free on the geometric realization: a fixed point in the interior of a chain simplex would force an order-preserving involution to preserve a chain and hence fix its vertices, which nonzero inversion never does.

**Step 5: the unrestricted group.** The set \(I\) is countably infinite, since there are countably many finite complexes and the discrete complexes on \(n\ge1\) vertices are infinitely many distinct join primes [1, Example 3.8]. The same signed-support retraction identifies the full punctured order complex, up to homotopy, with the order complex of all nonempty finite signed partial subsets of \(I\). It is the filtered union of finite cross-polytope boundaries. Every finite subcomplex lies in one finite-coordinate boundary. Adjoining an unused coordinate places that boundary inside its suspension, with nullhomotopic inclusion (it lies in the cone over one new apex). Every sphere map into this CW complex therefore becomes nullhomotopic after enlarging the coordinate set. By Whitehead's theorem for CW complexes, the order complex is contractible. This is a statement about its order complex (and weak homotopy type as an Alexandrov space), not an unverified strong deformation retract of the whole infinite Alexandrov space.

## Verification

The executable `check_puncture.py` enumerates all nonzero signed integer vectors of magnitude at most three in ranks one and two, and magnitude at most two in ranks three and four. It checks order preservation and comparison of the sign retraction, injectivity of higher-element predecessor signatures, recognition of antipodal atom pairs, and exact group orientation multipliers for every signed permutation in those ranks. It independently computes reduced mod-two homology ranks of the cross-polytope boundary chain complexes. Expected sphere Betti vectors were obtained at ranks one through four, and all tests passed. Execute: `python3 check_puncture.py`. These finite tests are not substituted for the all-rank proof above.

## Relationship to prior work

Chocano and Prieto-Martínez [1] establish join-prime unique factorization, the Grothendieck coordinate group, its Alexandrov order, and contractibility of the unpunctured global space. Their Theorems 3.14 and 4.1 provide the input structure used here; Theorem 4.2 concerns the unpunctured space, and neither it nor their universality Theorem 4.8 determines the topology of these **specific punctured coordinate subspaces**, their complete homeomorphism groups, or their antipodal quotients. The present result explicitly extracts that topology and rigidity. The general finite-space/order-complex weak-equivalence theorem is McCord's [2]. Standard cross-polytope topology is used as a known input, not claimed as newly discovered. Equivalent formulations in signed-vector poset terminology remain a literature-priority risk.

## Limitations

No classification is asserted for arbitrary non-coordinate free-abelian subgroups, arbitrary deleted points, or the ordinary non-Hausdorff homotopy type of the infinite punctured Alexandrov space. The quotient result is for geometric realizations of order complexes. The finite-space sphere equivalence is weak, not an ordinary homeomorphism. The findings do not determine negative-dimensional homology invariants defined by formal join inverses. Unindexed stronger signed-poset results could cover the assertions and independent mathematical validation has not been performed.

## References

[1] P. J. Chocano and L. F. Prieto-Martínez, *Negative-Dimensional Simplicial Complexes via the Grothendieck Group of the Join Monoid*, arXiv:2611.14300v1, first public 2026-11-10, https://arxiv.org/abs/2611.14300. Specifically Theorems 3.14, 4.1, 4.2 and 4.8.

[2] M. C. McCord, *Singular homology groups and homotopy groups of finite topological spaces*, Duke Math. J. **33** (1966), 465–474, DOI:10.1215/S0012-7094-66-03352-7. Specifically Theorems 2 and 3 on order complexes and Alexandrov spaces.
