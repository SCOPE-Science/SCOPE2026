# Integral pendant-leaf transfer for Laplacian controllability and the sharp nine-vertex tree threshold

## Finding

Let \(G\) be any finite undirected graph on \(n\ge1\) labelled vertices, with integral symmetric edge conductances and Laplacian \(L\in\mathbb Z^{n\times n}\). Choose a controlled vertex \(r\) and write
\[
K(G,r)=\big[e_r,Le_r,\ldots,L^{n-1}e_r\big].
\]
For any positive integer \(t\), append a new leaf \(\star\) connected only to \(r\), of conductance \(t\); order the old vertices before \(\star\), and place the sole control input at \(\star\). Then
\[
\boxed{K(H,\star)\sim_{\mathbb Z}\operatorname{diag}(1,tK(G,r))},
\qquad
\boxed{\det K(H,\star)=t^n\det K(G,r)}.
\]
Here \(\sim_{\mathbb Z}\) means equivalence by invertible integer row and column operations. In particular for \(t=1\), the multiset of Smith invariant factors is preserved with one extra unit factor; the abelian cokernel, including all torsion, is unchanged. The determinant equality also holds for all real \(t>0\), without an integer Smith statement.

The sharp first unweighted-tree departure from unimodularity occurs at order nine: every full-rank rooted-tree matrix on at most eight vertices has determinant magnitude one. The nine-vertex tree with edges
\[
\{(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(3,7),(4,8)\}
\]
has \(|\det K|=2\) at controlled roots \(2\) and \(3\). It is the only unlabelled order-nine tree with any full-rank determinant of magnitude greater than one, and those two roots are equivalent by an automorphism. Applying the unit-leaf transfer repeatedly supplies a rooted tree of every order at least nine with determinant magnitude two.

For the order-nine witness controlled from vertex \(2\), reachable integer target states for \(x_{k+1}=-Lx_k+e_2u_k\), \(x_0=0\), \(u_k\in\mathbb Z\), in exactly nine steps are *precisely* the states with
\[
\boxed{x_0+x_5+x_6+x_7\equiv0\pmod2}.
\]
This distinguishes ordinary real controllability from exact finite-time controllability over the integer lattice.

## Assumptions and scope

The graph need not be a tree for the transfer theorem. Edge conductances are integers, nonnegative, and the new edge has positive integer conductance; loops, if present in a general symmetric Laplacian formulation, are excluded. The finite sharpness census concerns simple, unweighted, undirected trees with vertex counts from one to nine, with one standard-coordinate actuator at each candidate root. The reachability interpretation fixes zero initial state and exactly \(n\) integer-valued inputs in discrete time. The signs of \(L\) and \(-L\) change determinant sign at most, not invariant factors or the generated integer lattice.

## Proof

**Integral block transfer.** Partition the extended Laplacian and its control vector as
\[
\widetilde L=\begin{pmatrix}L+t ee^{\mathsf T}&-t e\\-t e^{\mathsf T}&t\end{pmatrix},
\qquad \widetilde e=(0,\ldots,0,1)^{\mathsf T},\qquad e=e_r.
\]
Write \(\widetilde L^j\widetilde e=(y_j,z_j)^{\mathsf T}\), with \(y_j\in\mathbb Z^n\) and \(z_j\in\mathbb Z\). Then \(y_0=0\), \(z_0=1\), \(z_1=t\), and directly from the block recurrence,
\[
z_{j+1}=t(z_j-e^{\mathsf T}y_j),\qquad
 y_{j+1}=Ly_j-ez_{j+1}.
\]
Induction gives
\[
y_j=-\sum_{k=1}^j z_kL^{j-k}e.
\]
Every \(z_k\) with \(k\ge1\) is divisible by \(t\). In the upper-right \(n\times n\) block of the extended Kalman matrix, whose columns are indexed by exponents \(j=1,\ldots,n\), we therefore obtain exactly \(-tK(G,r)U\), where
\[
U_{i,j}=\begin{cases}z_{j-i+1}/t,&1\le i\le j\le n,\\0,&i>j.\end{cases}
\]
The matrix \(U\) is integer upper unitriangular because \(z_1=t\), hence belongs to \(\mathrm{GL}_n(\mathbb Z)\). The first column of the extended Kalman matrix is the new-leaf coordinate vector. Subtracting the appropriate multiple of that column from each remaining column clears their last entries. Permuting the first column to the end and using \(U^{-1}\), along with sign changes, reduces the whole integer matrix to \(\operatorname{diag}(1,tK(G,r))\). Explicit determinant expansion with the old-then-new vertex ordering gives \(\det K(H,\star)=t^n\det K(G,r)\), with positive sign. The same determinant calculation works over the reals even if \(t\) is nonintegral.

For unit \(t\), unimodular equivalence of \(\operatorname{diag}(1,K)\) to \(K\) with an extra trivial invariant factor yields the claimed isomorphism of cokernels \(\mathbb Z^{n+1}/\operatorname{im}K(H,\star)\cong\mathbb Z^n/\operatorname{im}K(G,r)\). Hence real rank and the finer integer-lattice index are both preserved by adjoining a unit leaf at the controlled root.

**Sharp finite tree threshold.** Every tree with \(k\ge2\) vertices is obtained by adjoining a leaf to a tree with \(k-1\) vertices. The included checker iterates this construction, deduplicating rooted-by-centroid branch encodings: remove all current leaves until one or two centers remain, recursively encode the sorted multiset of each center's descendant branches, and use the sorted pair of center encodings in the bicentral case. The canonical code uniquely specifies a free unlabelled tree, so this generates each isomorphism type once. The resulting free-tree counts for orders \(1\) through \(9\) are \(1,1,1,2,3,6,11,23,47\), respectively. For each representative, every vertex root is tested using the exact integer Kalman matrix and fraction-free Bareiss determinant, with integral exact-division checks.

The counts of zero, unit-magnitude, and larger-magnitude determinants across all root positions of representatives are, respectively,
\[
\begin{array}{c|rrrrrrrrr}
k&1&2&3&4&5&6&7&8&9\\\hline
0&0&0&1&4&9&26&62&146&361\\
1&1&2&2&4&6&10&15&38&60\\
>1&0&0&0&0&0&0&0&0&2
\end{array}
\]
The two final entries of magnitude two are exactly the stated symmetry-related roots, establishing minimality within the entire finite domain, not a sample. The block transfer iterated with unit edges then proves the all-larger-orders existence claim analytically.

**Exact integer-state congruence.** At the nine-vertex witness and root \(2\), exact integer elimination gives \(|\det K|=2\), and direct multiplication modulo two shows the row vector supported on vertices \(\{0,5,6,7\}\) annihilates every column of \(K\). Thus the generated lattice is contained in the displayed parity-index-two sublattice. Since the determinant index is exactly two, the lattices coincide. The factor \(-L\) does not change the integer image of the Kalman matrix, since it changes alternate columns only by signs.

## Verification

Run `python3 verify.py` using only the Python standard library. The file reconstructs every tree through order nine by leaf extension and a centroid canonical code, checks exact integer determinants for all \(749\) tree-root instances, repeats the unit-leaf determinant transfer on \(326\) smaller instances, and directly checks the explicit nine-vertex witness and its parity obstruction. Additional exact block-column identities are checked with leaf conductances \(1,2,3\) on rooted trees through order six. A passing run ends in the line `VERIFY_OK tree_types_1_through_9=95 rooted_cases=749 leaf_invariance_tests=326 nonunit_min_size=9 magnitude=2 lattice_parity=verified`. These finite tests support the finite threshold; the arbitrary-order transfer is proved above, independently of the finite enumeration.

## Relationship to prior work

Parlangeli and Notarstefano (2011) give arithmetic necessary and sufficient reachability criteria for path and cycle Laplacian networks, not an integral Smith transfer on every graph. Hsu and Yang (2019), especially Corollary 3, prove that single-node Laplacian *rank controllability* survives attaching a leaf to the controlled vertex and relocating the input. That known rank-only statement is an immediate weaker consequence of the integral block transfer, and is not presented here as new. Parlangeli (2025) investigates rank observability and controllability for starlike trees, including tree construction. The present claim concerns exact integer unimodular equivalence, reachable-state lattice index, a full unrestricted nine-vertex tree cutoff, and a precise parity obstruction. The distinction is implication-based, not merely differences in terminology.

## Limitations

The Smith assertion requires integral edge conductances; for arbitrary positive real new edge weights only the determinant factorization is claimed. Tree minimality is an exhaustive finite computation through nine vertices with a fully specified reproducible generator, not a closed-form classification of all larger trees. The constructed order-nine root is rationally controllable but cannot reach all integer targets by integer inputs at minimal horizon. Historical originality has not been independently certified: equivalent Smith-module results could exist under different language, particularly in integral systems or graph walk-matrix literature.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, first public version 2011-09-16, https://arxiv.org/abs/1109.3556.
2. C.-C. Hsu and C.-H. Yang, *Generalising Laplacian controllability of paths*, IET Control Theory & Applications (2019), DOI 10.1049/iet-cta.2018.6214; compare Corollary 3, https://doi.org/10.1049/iet-cta.2018.6214.
3. G. Parlangeli, *Laplacian Controllability and Observability of Multi-Agent Systems: Recent Advances in Tree Graphs*, Algorithms 18 (2025), 239; DOI 10.3390/a18050239, preprint https://www.preprints.org/manuscript/202503.1438.
