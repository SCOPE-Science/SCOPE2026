# Prime-order free symmetries and long cup products in separable-graph complexes

## Finding
Let \(\Delta_n^{(2)}\) be the simplicial complex whose vertices are the \(\binom n2\) edges of the complete graph on \(\mathbb Z/n\mathbb Z\), and whose faces are the edge sets of graphs that are *not* two-vertex-connected, retaining all \(n\) graph vertices. Let \(r\) rotate the graph vertices by \(v\mapsto v+1\), and let \(C_n=\langle r\rangle\).

**Theorem.** For every integer \(n\ge3\), the geometric action of \(C_n\) on \(|\Delta_n^{(2)}|\) is free if and only if \(n\) is prime. For every prime \(p\ge5\), write \(Y_p=|\Delta_p^{(2)}|/C_p\). Then
\[
\pi_1(Y_p)\cong C_p,\qquad
H_j(Y_p;\mathbb Z)\cong
\begin{cases}
\mathbb Z/p\mathbb Z,&1\le j\le2p-6\text{ odd},\\
0,&2\le j\le2p-6\text{ even}.
\end{cases}
\]
The classifying map \(c:Y_p\to BC_p\) induces an isomorphism of integral cohomology groups in all degrees \(0\le j\le2p-6\), compatibly with multiplication in this range. In particular, if \(u\in H^2(BC_p;\mathbb Z)\cong\mathbb Z/p\mathbb Z\) is a generator, then
\[
(c^*u)^k\ne0\quad (1\le k\le p-3).
\]
Consequently the integral cohomological cup-length is at least \(p-3\) and the unnormalized Lusternik–Schnirelmann category satisfies \(\operatorname{cat}(Y_p)\ge p-2\). All these assertions concern the ordinary geometric orbit space, not the homotopy quotient of a nonfree action.

## Assumptions and scope
The graph is simple, undirected, and always has all of \(\mathbb Z/n\mathbb Z\) as its vertex set, including isolated vertices. A graph is two-vertex-connected precisely when both it and each graph obtained by deleting one graph vertex are connected. The empty edge set is a face of the abstract complex but does not give a geometric point. Every assertion uses integral singular (co)homology unless specified otherwise. Freeness holds for all \(n\ge3\) exactly in the prime cases; the homological and cup-product claims are made only for primes \(p\ge5\), and only in the indicated degrees. No higher-degree integral homology or full homotopy classification of \(Y_p\) is asserted.

## Proof
**1. Freeness is equivalent to primality.** A fixed point of the geometric simplicial action has a unique minimal carrier simplex, which must be setwise invariant under the fixing group element. Conversely, the barycenter of any nonempty invariant face is fixed. For prime \(p\), every nonidentity element of \(C_p\) generates the whole group. An invariant nonempty edge set must contain a complete orbit of some edge \(\{a,a+d\}\), with \(1\le d\le(p-1)/2\). That orbit is a connected spanning \(p\)-cycle because \(\gcd(d,p)=1\). A cycle of length \(p\ge3\) remains connected after deleting any one vertex, so it is two-vertex-connected. Any graph containing it is also two-vertex-connected. Such an edge set therefore cannot be a face of \(\Delta_p^{(2)}\); the action is free.

Conversely, let \(n\ge4\) be composite and choose a proper divisor \(d\) with \(2\le d<n\). The rotation-invariant edge set \(E_d=\{\{v,v+d\}:v\in\mathbb Z/n\mathbb Z\}\) consists of \(\gcd(n,d)=d\) disjoint cycle components (with the length-two case interpreted as an edge), hence is disconnected. Thus \(E_d\) is a nonempty face of \(\Delta_n^{(2)}\), and its barycenter is fixed by \(r\). This proves the if-and-only-if assertion.

**2. Connectivity of the covering complex.** Babson, Björner, Linusson, Shareshian, and Welker, Theorem 3.1 of *Complexes of not \(i\)-connected graphs* (arXiv:math/9705219, first public version 1997-05-11), prove
\[
|\Delta_n^{(2)}|\simeq \bigvee^{(n-2)!}S^{2n-5}\qquad(n\ge3).
\]
For \(p\ge5\), the covering space \(X_p=|\Delta_p^{(2)}|\) is simply connected and has vanishing reduced integral homology in every degree below \(m=2p-5\). By Step 1, \(X_p\to Y_p\) is a regular covering with deck group \(C_p\), so it is the universal covering and \(\pi_1(Y_p)\cong C_p\).

**3. Integral homology below \(m\).** For this free finite-group action, the Cartan–Leray homology spectral sequence has
\[
E^2_{a,b}=H_a(C_p;H_b(X_p;\mathbb Z))\Longrightarrow H_{a+b}(Y_p;\mathbb Z).
\]
All entries with \(0<b<m\) vanish and \(H_0(X_p;\mathbb Z)\) is the trivial \(C_p\)-module \(\mathbb Z\). In total degrees \(j<m\), the only possible terms lie in row \(b=0\), and no differential reaches or leaves such a term in this range. Hence \(H_j(Y_p;\mathbb Z)\cong H_j(C_p;\mathbb Z)\) for \(0\le j<m\). The standard two-periodic free resolution over \(\mathbb Z[C_p]\), with alternating maps \(r-1\) and \(N=1+r+\cdots+r^{p-1}\), becomes the chain complex with alternating maps \(0\) and multiplication by \(p\) after tensoring with the trivial module. It gives \(H_j(C_p;\mathbb Z)=\mathbb Z/p\mathbb Z\) for positive odd \(j\), and zero for positive even \(j\), establishing the stated range.

**4. Integral cup products.** Since the action is free, the Borel construction is homotopy equivalent to \(Y_p\) and fits into a fibration \(X_p\to Y_p\xrightarrow{c}BC_p\) up to homotopy. The integral cohomology Serre spectral sequence has row \(b=0\) equal to \(H^*(BC_p;\mathbb Z)\), with every row \(0<b<m\) zero. Its edge homomorphism is consequently an isomorphism through degree \(m-1=2p-6\). As the map comes from a space map, it preserves products. The canonical periodic-resolution calculation gives \(H^*(BC_p;\mathbb Z)\cong\mathbb Z[u]/(pu)\) with \(|u|=2\), proving \((c^*u)^k\ne0\) for \(2k\le m-1\), i.e. \(k\le p-3\). The classical cup-length lower bound for the unnormalized category gives \(\operatorname{cat}(Y_p)\ge p-2\). \(\square\)

## Verification
The accompanying self-contained `verify.py` independently enumerates all edge subsets for \(n=3,4,5,6\), tests two-vertex-connectivity exactly, enumerates fixed nonempty faces for every nonidentity rotation, and compares the Euler characteristic with the cited wedge theorem. Its output verifies nonempty face totals \(6,53,785,21399\); Euler characteristics \(0,-1,-5,-23\); free actions at \(n=3,5\) and nonfree actions at \(n=4,6\). For \(n=5\), it finds no fixed nonempty faces under any of the four nonidentity rotations. It separately lists the cohomological degree ranges for \(p=5,7,11\). These finite checks do not replace the all-prime proof above; the latter uses the orbit-of-an-edge lemma and the cited general homotopy theorem. Run `python3 verify.py` using only the Python standard library.

## Relationship to prior work
The 1997 paper by Babson et al. proves the sphere-wedge homotopy theorem and computes the full symmetric-group character of its top homology; Section 4, Corollary 4.7 also computes cyclic-invariant **rational top-homology multiplicities**. Those results are explicitly used as premises and are not claimed as new. The result here instead isolates the exact prime/composite freeness boundary and the low-degree **integral cohomology ring and nonzero products** of the actual geometric orbit spaces. The former character formula does not itself specify the integral torsion or cup length of these orbit spaces. The classical Kahn–Saks–Sturtevant work treats monotone graph properties and group actions in evasiveness, but is not a calculation of these orbit-space cohomology rings. Related cyclic multipath and chessboard quotients have different underlying complexes and do not imply this statement.

## Limitations
This is a consequence of a previously established deep wedge theorem together with a new elementary symmetry observation and standard covering-space spectral-sequence methods; it does not purport to reprove the wedge theorem. Its novelty is specifically the combined orbit-space assertion, rather than the inputs or general-purpose spectral sequence. Work not indexed or not accessed may contain an equivalent consequence. No claim about the top or higher integral homology, exact category, higher attaching maps, or finite-dimensional CW models beyond the verified low-degree range is made. The finite enumeration is a sanity check, not an infinite certificate.

## References
1. E. Babson, A. Björner, S. Linusson, J. Shareshian, and V. Welker, *Complexes of not \(i\)-connected graphs*, arXiv:math/9705219, first public version 1997-05-11, Theorem 3.1 and Section 4, https://arxiv.org/abs/math/9705219.
2. J. Kahn, M. Saks, and D. Sturtevant, *A topological approach to evasiveness*, Combinatorica 4 (1984), 297–306, https://doi.org/10.1007/BF02579140.
3. Standard Cartan–Leray and cohomology Serre spectral sequences, two-periodic cyclic-group resolution, and the classical cup-length bound for Lusternik–Schnirelmann category (standard tools; no new claim of origin).
