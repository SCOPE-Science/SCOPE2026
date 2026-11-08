# The sparse Stiefel graph of real codimension-one isometries

## Finding
For every integer \(n\ge2\) and real \(1\le p<\infty\), \(p\ne2\), let \(\mathcal I_{n,p}\) be the space, with its operator-norm topology, of **all real-linear isometric embeddings** \(T:\ell_p^{n-1}(\mathbb R)\to\ell_p^n(\mathbb R)\). Then \(\mathcal I_{n,p}\) is homeomorphic to the geometric realization of a connected, \(2(n-1)\)-regular finite graph. More precisely, the graph is the Cayley graph of the even-signed permutation group \(W(D_n)\) with generators that exchange the last and one other coordinate, either preserving both signs or reversing both signs.

The graph has exactly
\[
V_n=2^{n-1}n!,\qquad E_n=(n-1)2^{n-1}n!
\]
vertices and unoriented edges, respectively. Consequently,
\[
\mathcal I_{n,p}\simeq\bigvee^{\,1+(n-2)2^{n-1}n!}S^1,\qquad
\pi_1(\mathcal I_{n,p})\cong F_{\,1+(n-2)2^{n-1}n!},
\]
and its first integral homology is free abelian of the same rank. The rank is \(1\), \(25\), and \(385\) for \(n=2,3,4\), respectively. These spaces have the same homeomorphism type for all the stated \(p\).

There is also a canonical continuous **columnwise Euclidean normalization** map \(\mathcal I_{n,p}\to V_{n-1}(\mathbb R^n)\), where the target is the ordinary real Stiefel manifold. Its induced map on fundamental groups is surjective. For \(n\ge3\) the target group is \(\mathbb Z/2\mathbb Z\); for \(n=2\), normalization is a homeomorphism between circles.

## Assumptions and scope
The field is \(\mathbb R\), the norms are the unweighted coordinate \(\ell_p\) norms, and \(1\le p<\infty\), \(p\ne2\). The space includes all isometric embeddings with \(n-1\) nonzero columns, not operators with a deleted input coordinate. It carries the topology inherited from the finite-dimensional vector space of real \(n\)-by-\((n-1)\) matrices; any matrix norm induces the same topology.

Here \(W(D_n)\) means the group of signed permutation matrices in \(\mathbb R^{n\times n}\) with an even number of negative signs. For \(n=2\) this is understood as the even-signed permutation group of order four; no irreducibility convention for the root system is required. Let \(e_1,\ldots,e_n\) be the standard coordinate vectors. For each \(1\le i<n\), define two involutions \(s_i^+\) and \(s_i^-\) by fixing the other basis vectors and setting
\[
s_i^+(e_i)=e_n,\quad s_i^+(e_n)=e_i;
\qquad
s_i^-(e_i)=-e_n,\quad s_i^-(e_n)=-e_i.
\]
Both have an even number of sign changes, and their set of \(2(n-1)\) elements generates \(W(D_n)\). The Cayley graph in the finding is the undirected graph with edges \(\{g,gs_i^\pm\}\).

## Proof
**1. Support rigidity.** Write \(u_j=T e_j\), for \(1\le j<n\). Each column has \(\|u_j\|_p=1\). For distinct columns \(u_j,u_k\), isometry gives \(\|u_j+u_k\|_p^p=\|u_j-u_k\|_p^p=2\). The strict scalar Clarkson relation states, for real \(a,b\), that
\[
|a+b|^p+|a-b|^p-2|a|^p-2|b|^p
\]
has a fixed strict sign whenever \(ab\ne0\): positive if \(p>2\), negative if \(1\le p<2\), and zero if \(ab=0\). Summing the relation over rows yields zero by the preceding norm identities; hence each summand vanishes and distinct columns have disjoint supports. Conversely, \(n-1\) disjointly supported columns of \(\ell_p\)-norm one define an isometric embedding. This is the real full-isometry case of the finite-dimensional Lamperti theorem; a direct proof of its essential step has just been given.

**2. No cells of dimension above one.** Every one of the \(n-1\) columns has nonempty support, while their supports are disjoint subsets of \(n\) rows. Thus at most one column has two nonzero coordinates, and no column can have three. If every column has one nonzero entry, all entries equal \(+1\) or \(-1\); these are the zero-dimensional vertices. If one column has two nonzero entries, its two real coordinates \((a,b)\) satisfy \(|a|^p+|b|^p=1\), with both coordinates nonzero; once their signs are fixed they describe one open interval. The remaining columns are signed standard coordinate vectors. Each such interval closes up at precisely two vertices, at \((\pm1,0)\) and \((0,\pm1)\). Distinct interval interiors are disjoint. Attaching one closed interval for each sign choice to its two endpoint vertices gives a continuous bijection from a finite compact graph onto this matrix space; the target is Hausdorff, so the bijection is a homeomorphism. In particular there are no omitted higher-dimensional cells.

**3. Vertices, edges, and adjacency.** Vertices consist of injections of the \(n-1\) labeled columns into \(n\) rows, with independent signs. Hence \(V_n=2^{n-1}n!\). At a vertex there is exactly one unused row. For any of the \(n-1\) columns, moving its occupied coordinate into the unused row and prescribing either of two signs there gives one incident open interval. These \(2(n-1)\) possibilities are distinct and exhaustive. The handshaking identity gives \(E_n=(n-1)V_n\).

**4. The type-D Cayley description and connectivity.** The group \(W(D_n)\) acts on \(\mathcal I_{n,p}\) by left multiplication (signed permutations of output coordinates). The action on vertices is free: a group element fixing \(e_1,\ldots,e_{n-1}\) must also fix \(e_n\), because the number of sign flips is even. The action is transitive: a signed coordinate injection extends uniquely to an even-signed permutation by using the spare coordinate and choosing its sign to make the total number of negative signs even. Thus vertices are canonically identified with \(W(D_n)\), relative to the standard embedding. The neighbors of the standard vertex are exactly \(s_i^+\) and \(s_i^-\). Every unsigned permutation of the \(n\) labels can be generated by transpositions exchanging the spare label with an occupied label, and the two choices of signs in each move permit changing any of the occupied signs. Equivalently the displayed signed star-transpositions generate \(W(D_n)\). It follows that the graph is the stated connected Cayley graph.

**5. Homotopy and homology.** A connected finite graph with \(V\) vertices and \(E\) edges has a spanning tree with \(V-1\) edges. Collapsing that tree yields a wedge of \(E-V+1\) circles. Inserting the exact counts yields \(1+(n-2)2^{n-1}n!\); the fundamental and first homology groups follow.

**6. Comparison with the full Stiefel manifold.** For a matrix \(T\in\mathcal I_{n,p}\), define \(\Phi(T)\) by replacing each nonzero column \(u_j\) with \(u_j/\|u_j\|_2\). The supports are disjoint, so these Euclidean unit columns are orthogonal. This is a continuous map to \(V_{n-1}(\mathbb R^n)\). Keep columns \(e_2,\ldots,e_{n-1}\) fixed and let the first column traverse the full real \(\ell_p\) unit circle in the two-coordinate plane spanned by \(e_1,e_n\). This is a four-edge loop in \(\mathcal I_{n,p}\); its Euclidean normalization traverses the standard planar unit circle once. Completing the Euclidean frame to a determinant-one orthogonal matrix identifies the target Stiefel manifold with \(SO(n)\). The image of this loop is one full rotation in a coordinate plane, which generates \(\pi_1(SO(n))\): it is the generator of \(\mathbb Z\) when \(n=2\), and the nontrivial element of \(\mathbb Z/2\mathbb Z\) when \(n\ge3\). This proves surjectivity. In the \(n=2\) case the entire source and target are a single unit circle and radial normalization is a homeomorphism.

## Verification
The companion standalone script `check_sparse_frames.py` constructs the complete signed coordinate-injection graph for \(2\le n\le6\). It checks the exact vertex and edge counts, every degree, breadth-first connectedness, and the resulting cycle rank using integer arithmetic. Running `python check_sparse_frames.py` prints `SPARSE_REAL_FRAME_GRAPH_EXACT_OK` and gives the five pairs of graph counts. The general conclusions, for all integers \(n\ge2\), are proved combinatorially above, not by extrapolation from these computations.

## Relationship to prior work
Dalfollo-Daley, Delfín, Fernández, Mars, and Xia prove the classification of finite-dimensional restricted \(\ell_p\) isometries (Theorem 3.18) and determine the topology of **each fixed-support stratum** (Proposition 4.5). Their counting results enumerate support transformations and uniform isometries. The present theorem instead assembles *all* support strata at the first spare-output-coordinate boundary, computes the gluing graph, identifies its type-D symmetry and calculates the full fundamental group. Those conclusions do not appear in the source's Sections 3–4.

Classical Banach–Lamperti theory supplies disjoint-support rigidity but not this global topological computation. The ordinary permutation star graph uses the smaller group \(S_n\), unlike the signed type-D graph here. The ambient real Stiefel manifold, and literature on all Hilbert-space partial isometries, have different topology: for \(n\ge3\), their fundamental group is finite, whereas the sparse isometry space has a free group of factorially increasing rank. The moment-angle complex of injective words studied by Conceição has homology concentrated in positive even degrees in the cited model and is not identified with the one-dimensional graph computed here.

## Limitations
The theorem is for real, unweighted, finite-dimensional \(\ell_p\) spaces and precisely one spare output coordinate. At \(p=2\), columns need not have disjoint supports, so the graph description fails. In complex spaces, nonzero coordinate phases yield higher-dimensional cells. Two or more spare coordinates can also produce higher-dimensional cells. The theorem does not compute those other cases or the induced map's kernel. Claims about publication priority are necessarily provisional, and no independent mathematical audit has been performed.

## References
1. O. Dalfollo-Daley, A. Delfín, C. Fernández, C. Mars, and X. Xia, *Restricted isometries in finite-dimensional \(\ell^p\)-spaces*, arXiv:2610.32615v1 (first submitted 2026-10-23), especially Theorem 3.18, Corollary 3.21, Theorem 4.3, and Proposition 4.5. https://arxiv.org/abs/2610.32615
2. J. Lamperti, *On the isometries of certain function-spaces*, Pacific Journal of Mathematics **8** (1958), 459–466. https://msp.org/pjm/1958/8-3/pjm-v8-n3-p09-s.pdf
3. E. Gardella, *A modern look at algebras of operators on \(L^p\)-spaces*, Expositiones Mathematicae **39** (2021), 420–453. https://doi.org/10.1016/j.exmath.2020.10.003
4. L. G. Brown, *Some metric and homotopy properties of partial isometries*, arXiv:1603.07002 (2016). https://arxiv.org/abs/1603.07002
5. P. Conceição, *The homotopy type of the moment-angle complex associated to the complex of injective words*, arXiv:2603.09491v1 (2026). https://arxiv.org/abs/2603.09491
6. E. Khomyakova and E. V. Konstantinova, *Catalogue of the Star graph eigenvalue multiplicities*, Arabian Journal of Mathematics **10** (2021), 115–119. https://doi.org/10.1007/s40065-019-00271-z
