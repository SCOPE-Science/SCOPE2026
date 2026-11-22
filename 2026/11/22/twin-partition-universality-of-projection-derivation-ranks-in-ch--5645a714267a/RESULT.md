# Twin-partition universality of projection-derivation ranks in characteristic-two graph evolution algebras

## Finding
Let \(G=(V,E)\) be a finite connected simple undirected graph with at least two vertices. For a field \(k\) of characteristic two, define its graph evolution algebra \(A(G)\) with natural basis \((e_v)_{v\in V}\) by \(e_ve_w=0\) when \(v\ne w\) and \(e_v^2=\sum_{w\sim v}e_w\). Two vertices are *twins* if they have equal open neighborhoods; let \(\Pi(G)\) be the twin partition.

**Theorem.** Every ordinary \(k\)-linear derivation \(D:A(G)\to A(G)\) satisfying \(D^2=D\) is a block-diagonal matrix indexed by \(C\in\Pi(G)\), whose block \(P_C\) is symmetric, satisfies \(P_C\mathbf1_C=0\), and is idempotent; conversely every collection of such blocks gives exactly one such derivation. In particular every \(\operatorname{rank}D\) is even, and the family depends on the graph only through the sizes of its twin classes.

For \(k=\mathbb F_q\) with \(q=2^f\), set \(a_C=|C|\), \(h_C=\lfloor(a_C-1)/2\rfloor\), and \(\epsilon_C=1\) if \(a_C\) is even and \(0\) otherwise. Then the **complete labeled rank polynomial** is
\[
\boxed{\sum_{D\in\operatorname{Der}(A(G)),\ D^2=D}T^{\operatorname{rank}D}
=\prod_{C\in\Pi(G)}\left[\sum_{r=0}^{h_C}q^{2r(h_C-r)+2\epsilon_Cr}
{h_C\brack r}_{q^2}T^{2r}\right].}
\]
Here \({h\brack r}_{Q}=\prod_{j=0}^{r-1}(Q^{h-j}-1)/(Q^{r-j}-1)\), with the empty product equal to one. Every even integer between zero and \(2\sum_C h_C\) is attained. In particular the only idempotent derivation is zero exactly when every twin class has at most two vertices. The maximal rank equals \(\sum_C(a_C-1-\epsilon_C)\).

## Assumptions and scope
The graph is finite, simple, undirected, connected, and has at least two vertices. The field must have characteristic two; the classification of blocks holds over arbitrary such fields, while the enumeration requires a finite field \(\mathbb F_{2^f}\), \(f\ge1\). The word 'idempotent' refers to *composition of the derivation*, not to idempotent elements of the evolution algebra or algebra-homomorphism retractions. No restriction to invertible endomorphisms or natural-basis-preserving maps is made.

## Proof
**1. All derivations.** Write \(D(e_j)=\sum_i d_{ij}e_i\) and let \(N(j)\) be the set of neighbors of \(j\). The Leibniz identity on distinct basis vectors gives
\[
0=D(e_ie_j)=d_{ji}\sum_{u\in N(j)}e_u+d_{ij}\sum_{u\in N(i)}e_u\qquad(i\ne j).
\]
Every \(N(i)\) is nonempty by connectedness. The corresponding nonzero zero-one neighborhood vectors are proportional over a characteristic-two field only if their supports are equal: examining a coordinate in their support forces the scalar to be one. Thus for vertices in different twin classes, both off-block entries vanish. For vertices in the same class the displayed identity is exactly \(d_{ij}=d_{ji}\). The diagonal entries are unconstrained by this identity, so every block is symmetric.

The identity on a square, in characteristic two, is
\[
D(e_i^2)=D(e_i)e_i+e_iD(e_i)=0.
\]
Because each neighborhood is a union of whole twin classes and the block images are supported on disjoint classes, this implies \(D(\sum_{v\in C}e_v)=0\) for every twin class \(C\) neighboring \(i\). Every class has some neighboring vertex; hence \(P_C\mathbf1_C=0\) for all \(C\). Conversely, symmetry within blocks, zero cross-block entries and these zero-sum constraints verify the Leibniz identity on all pairs of basis elements. This independently recovers the characteristic-two specialization of the established general derivation equations.

**2. Idempotent blocks.** The block decomposition implies \(D^2=D\) if and only if \(P_C^2=P_C\) for all classes. Put \(a=|C|\) and \(B(x,y)=\sum_{i=1}^a x_i y_i\) on \(k^a\). Then \(P_C^T=P_C\) is self-adjoint for \(B\). Any self-adjoint projection has \(\ker P_C=(\operatorname{im}P_C)^\perp\) and a nondegenerate image \(W\). Conversely each nondegenerate subspace \(W\) determines a unique self-adjoint projection along \(W^\perp\). The condition \(P_C\mathbf1=0\) is exactly \(W\subseteq H:=\mathbf1^\perp\).

In characteristic two, \(B(x,x)=(\sum_i x_i)^2=0\) for every \(x\in H\). Thus \(B|_H\) is alternating. As \(B\) is nondegenerate, \(H^\perp=k\mathbf1\). If \(a=2h+1\) is odd, \(B(\mathbf1,\mathbf1)=1\), so \(H\) is a nondegenerate symplectic space of dimension \(2h\). If \(a=2h+2\) is even, \(\mathbf1\in H\) and \(\operatorname{rad}(B|_H)=k\mathbf1\); the quotient \(H/k\mathbf1\) is symplectic of dimension \(2h\).

In the odd case the permitted rank-\(2r\) images are exactly the nondegenerate \(2r\)-subspaces of a symplectic \(2h\)-space. In the even case they project injectively onto nondegenerate \(2r\)-subspaces of \(H/k\mathbf1\), with exactly \(q^{2r}\) distinct graph lifts into \(H\): sections differ by one arbitrary linear map from a \(2r\)-dimensional space to the radical line. Nondegeneracy is unaffected because the radical is orthogonal to \(H\). In either case ranks are necessarily even, and the bounds on \(r\) are sharp.

**3. Counting.** The symplectic group acts transitively on nondegenerate \(2r\)-subspaces of a \(2h\)-dimensional symplectic space (extend a symplectic basis). The stabilizer preserves the orthogonal direct-sum decomposition and has order \(|\operatorname{Sp}_{2r}(q)|\,|\operatorname{Sp}_{2(h-r)}(q)|\). Using
\[
|\operatorname{Sp}_{2h}(q)|=q^{h^2}\prod_{i=1}^h(q^{2i}-1)
\]
gives exactly \(q^{2r(h-r)}{h\brack r}_{q^2}\) subspaces. The even-size lift contributes \(q^{2r}\). Multiplication across independent twin blocks proves the displayed polynomial and the sharp rank assertions.

## Verification
An independent, finite computational check is provided as `check_projection_derivations.py`. It enumerates every symmetric zero-row-sum block and tests idempotence over \(\mathbb F_2\) at sizes one through six, over \(\mathbb F_4\) at sizes two through four, and over \(\mathbb F_8\) at sizes three and four. It additionally constructs the full derivation linear-equation system from the original products (without assuming the twin-block description) and enumerates its idempotents for both non-bipartite graphs and \(K_{3,4}\). These finite checks are consistency tests; the proof above establishes the arbitrary-order result.

For example, with \(q=2\), the twin sizes \((3,4)\) give \(1+5T^2+4T^4\) and ten idempotent derivations. The same rank polynomial occurs for a non-bipartite graph built from a triangle by attaching three leaves at one triangle vertex and four leaves at another: its twin sizes are \((1,1,1,3,4)\). The direct defining-equation computation agrees. For \(q=2\) a single class of size six contributes \(1+80T^2+16T^4\).

## Relationship to prior work
Reis and Cadavid (arXiv:2006.11934, first posted 2020-06-21) characterize derivations of graph evolution algebras in arbitrary characteristic by the twin partition. Their Theorem 3.1 contains the underlying block and skew-symmetry conditions and is fully credited here; it does not present the composition-idempotent rank census or its symplectic counting formula. Cadavid, Rodiño Montoya and Rodriguez (arXiv:1807.02493, 2018-07-06) give a characteristic-zero counterpart and complete multipartite examples, but explicitly assume characteristic zero. Cabrera Casado and collaborators (arXiv:1912.06925, 2019-12-14) consider spaces of derivations for evolution algebras associated with graph data. The present theorem concerns the nonlinear projection condition inside those known derivation spaces, counts every rank, and identifies graph-independent universality at fixed twin-class sizes.

Related indexed research on square-zero derivations of one-dimensional-square evolution algebras, and on idempotent derivations of graph Lie algebras, involves different identities or underlying multiplications; neither statement implies this result. The nondegenerate symplectic-subspace formula is standard linear algebra and is not claimed as new in isolation.

## Limitations
The claim is restricted to finite connected simple undirected graphs over characteristic-two fields. Disconnected graphs with isolated vertices are excluded because the block argument changes there. No assertion is made in other characteristics. The symplectic counting step is established by the standard symplectic-group orbit-stabilizer argument, not by the finite tests. Independent audit and exhaustive global publication-priority certification have not been performed; other unpublished or unindexed equivalent classifications may exist.

## References
1. T. Reis and P. Cadavid, *Derivations of Evolution Algebras associated to graphs over a field of any characteristic*, arXiv:2006.11934 (first submission 2020-06-21), https://arxiv.org/abs/2006.11934.
2. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodriguez, *Characterization theorems for the spaces of derivations of evolution algebras associated to graphs*, arXiv:1807.02493 (first submission 2018-07-06), https://arxiv.org/abs/1807.02493.
3. Y. Cabrera Casado, P. Cadavid, M. L. Rodiño Montoya and P. M. Rodriguez, *On the characterization of the space of derivations in evolution algebras*, arXiv:1912.06925 (2019-12-14), https://arxiv.org/abs/1912.06925.
