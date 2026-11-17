# Unbounded integral cup powers in cyclic quotients of graph-connectivity complexes

## Finding

For integers \(n\geq3\) and \(1\leq k<n\), let \(K_{n,k}\) be the simplicial complex on the edges of the complete graph with vertex set \(\mathbb Z/n\mathbb Z\), whose faces are the edge sets of spanning graphs that are **not** \(k\)-vertex-connected. Let \(C_n\) rotate vertex labels regularly. The action of \(C_n\) on \(|K_{n,k}|\) is free **if and only if** \(n\) is prime and \(k\in\{1,2\}\).

For every prime \(p\geq5\), put \(Q_p=|K_{p,2}|/C_p\) and \(d=2p-5\). The principal covering has a classifying map \(c_p:Q_p\to BC_p\). Write \(u=c_p^*(\eta)\in H^2(Q_p;\mathbb Z)\), where \(\eta\) is a generator of \(H^2(BC_p;\mathbb Z)\). The pullback is an **isomorphism of graded cohomology rings in all degrees strictly below \(d\)**. Consequently,

\[
H^{2j}(Q_p;\mathbb Z)=\langle u^j\rangle\cong\mathbb Z/p\mathbb Z
\quad(1\leq j\leq p-3),\qquad
H^{2j+1}(Q_p;\mathbb Z)=0\quad(0\leq2j+1<d),
\]

and \(u^{p-3}\neq0\) in degree \(2p-6\). In particular, the integral cup-length of \(Q_p\) is **at least** \(p-3\), so its normalized Lusternik–Schnirelmann category satisfies \(\operatorname{cat}(Q_p)\geq p-3\). No assertion is made about powers above this range or exact category.

Equivalently, in positive degrees below \(d\), \(H_i(Q_p;\mathbb Z)\cong\mathbb Z/p\mathbb Z\) for odd \(i\), and vanishes for even \(i\). In particular \(\pi_1(Q_p)\cong C_p\). These are integral quotient phenomena: the original \(|K_{p,2}|\) is a wedge of spheres, with all positive-degree cohomology concentrated in a single degree and with every product of two positive-degree classes zero.

## Assumptions and scope

All graphs are finite, undirected, simple, spanning on the specified labeled vertex set. \(k\)-vertex-connected means that deleting any set of fewer than \(k\) vertices leaves a connected graph. A nonempty simplex corresponds to a nonempty edge set. The geometric realization is the usual one (the empty face is not a point). \(C_n\) is the order-\(n\) cyclic rotation group, not the full symmetric group. Homology and cohomology are singular theories with integer coefficients unless explicitly indicated. The reference result on the cover is the 1997 homotopy classification of complexes of not two-connected graphs, applied exactly at \(n=p\).

For normalized \(\operatorname{cat}\), a contractible space has category zero. The cup-length counts the number of positive-degree factors in a nonzero cohomological product. The classification of freeness applies to all \(n\geq3\) and \(1\leq k<n\); the ring calculation applies only to primes \(p\geq5\) and \(k=2\). The case \(p=3\) is excluded from the ring statement because the covering complex is a circle, not simply connected.

## Proof

**Step 1: exact freeness criterion.** If \(n\) is composite, take a proper divisor \(a\) with \(1<a<n\) and the nonidentity rotation \(r^a\). The orbit of the edge \(\{0,a\}\) under this rotation is nonempty and uses only the proper subset \(\{0,a,2a,\dots\}\) of vertices. Its spanning graph is disconnected. The barycenter of the corresponding invariant simplex is a fixed point in \(|K_{n,k}|\) for every \(k\geq1\).

If \(n=p\) is prime, every nonidentity rotation acts transitively on the graph vertices. For any graph edge \(\{x,y\}\), its rotation orbit is the Hamiltonian undirected \(p\)-cycle obtained from the nonzero step \(y-x\). That cycle is two-vertex-connected, and every supergraph is also two-vertex-connected. If a geometric point of \(|K_{p,k}|\) were fixed by a nonidentity rotation, the nonempty support of its barycentric coordinates would be a union of full edge orbits. It would contain a Hamiltonian cycle and could not represent a graph failing \(k\)-connectivity for \(k=1\) or \(2\). Thus the action is free for these two \(k\)-values. For \(k\geq3\), the ordinary Hamiltonian cycle \(\{\{i,i+1\}:i\in\mathbb Z/p\mathbb Z\}\) itself is not three-vertex-connected; its invariant simplex has a rotation-fixed barycenter. This completes both directions.

**Step 2: universal-cover connectivity.** Theorem 3.1 of Babson, Björner, Linusson, Shareshian and Welker identifies \(|K_{p,2}|\) up to homotopy with \(\bigvee^{(p-2)!}S^{2p-5}\). Put \(d=2p-5\); for \(p\geq5\), the cover is simply connected, and its reduced integral cohomology vanishes in every degree below \(d\). By Step 1 its \(C_p\)-action is free, and the covering is regular with group \(C_p\), so \(\pi_1(Q_p)\cong C_p\).

**Step 3: multiplicative low-degree comparison.** The homotopy-fiber description of the principal covering yields \(|K_{p,2}|\to Q_p\xrightarrow{c_p}BC_p\). The integral Serre cohomology spectral sequence for this fibration has \(E_2^{s,t}=H^s(C_p;H^t(|K_{p,2}|;\mathbb Z))\). The rows with \(0<t<d\) vanish. A differential from the top row into the bottom row could first occur on page \(d+1\), and it would land in base degree at least \(d+1\). Thus the edge homomorphism \(c_p^*\) is an isomorphism in every degree \(<d\). Being a pullback, it preserves cup products. The standard integral cyclic-group cohomology ring is \(H^*(BC_p;\mathbb Z)=\mathbb Z[\eta]/(p\eta)\), with \(\deg\eta=2\), proving every stated group and nonzero product \(u^j\), \(1\leq j\leq p-3\). The category inequality follows from the standard cup-length bound.

**Step 4: integral homology check.** The homology spectral sequence for the same fibration similarly identifies \(H_i(Q_p;\mathbb Z)\) with \(H_i(C_p;\mathbb Z)\) for \(i<d\). The latter is cyclic of order \(p\) in positive odd degrees and zero in positive even degrees. This establishes the stated homology range without asserting the integral top-degree group. The previously established symmetric-group character determines the rational top rank; that character computation is not part of the claimed new contribution.

## Verification

A reproducible Python 3 standard-library program, `verify.py`, examines 167 prime-order edge-orbit tests for primes \(3,5,7,11,13\) and six explicit composite-order obstruction witnesses. Independently, for five vertices it enumerates all \(785\) non-two-connected nonempty edge sets, forms their \(157\) free \(C_5\)-orbits, builds signed cellular boundary matrices, checks all boundary compositions, and performs \(74\) integral unit-pivot cancellations. The residual boundaries have coefficients \(5\) in degree two and a \(2\)-by-\(2\) degree-four matrix with determinant \(-5\) and entries of greatest common divisor one. This yields \(H_1(Q_5;\mathbb Z)\cong H_3(Q_5;\mathbb Z)\cong\mathbb Z/5\mathbb Z\) and \(H_5(Q_5;\mathbb Z)\cong\mathbb Z^2\), with no other positive-degree homology. The expected low-degree instances agree with the general proof. The code does **not** calculate cup products or establish an infinite theorem; those follow from Steps 1–3 and the published cover theorem.

Run `python3 verify.py`; its observed output is in `verification_output.txt`.

## Relationship to prior work

Babson–Björner–Linusson–Shareshian–Welker (first public preprint May 11, 1997) prove the nonequivariant sphere-wedge type in their Theorem 3.1 and determine the symmetric-group top-homology character in Section 4, including the invariant cyclic multiplicity (Corollary 4.7). Those conclusions are **credited as known**; in particular, a rational top-Betti formula is not being presented as new. The present contribution concerns geometric freeness across the vertex-connectivity hierarchy and the **integral multiplicative cohomology** of the corresponding orbit spaces, which their cited homology-character results do not specify.

Cyclic-group cohomology and the cup-length category bound are standard tools and are also credited; the derived family-specific result is the sharp combinatorial freeness threshold together with its application to nonzero arbitrarily long integral cup products. Other published orbit-space torsion results concern distinct graph and directed-graph complexes and do not supply this conclusion for the not-two-connected graph complex.

## Limitations

No formula for the full integral cohomology ring in degrees \(\geq2p-5\), for the exact Lusternik–Schnirelmann category, or for the homotopy type of the orbit space is claimed. Inaccessible or unindexed equivalent literature remains an originality risk. The verification script checks finite cases only. The general low-degree ring statement depends on the precisely cited earlier sphere-wedge theorem and on standard covering-space and Serre-spectral-sequence results, not on finite enumeration. No independent mathematical validation has been performed.

## References

1. E. Babson, A. Björner, S. Linusson, J. Shareshian and V. Welker, *Complexes of not \(i\)-connected graphs*, arXiv:math/9705219, first public May 11, 1997. https://arxiv.org/abs/math/9705219 . See Theorem 3.1, Section 4, and Corollary 4.7.
2. K. S. Brown, *Cohomology of Groups*, Graduate Texts in Mathematics 87, Springer, 1982, DOI:10.1007/978-1-4684-9327-6. Standard periodic integral cohomology of finite cyclic groups.
3. O. Cornea, G. Lupton, J. Oprea and D. Tanré, *Lusternik–Schnirelmann Category*, Mathematical Surveys and Monographs 103, American Mathematical Society, 2003. Standard cup-length lower bound.
