# Dihedral and layer-swap homology characters of cyclic-prism three-cut complexes

## Finding
Let \(n\ge5\) be an integer. For the circular ladder \(G_n=C_n\square K_2\), let \(X_n=\Delta_3(G_n)\) denote the **ordinary** three-cut complex. Its facets are the complements of disconnected induced triples. The dihedral group of the cycle and the interchange of the two layers act on the sole nonzero reduced rational homology group
\[
H_n=\widetilde H_{2n-4}(X_n;\mathbb Q),\qquad \dim H_n=B_n:=2n^2-8n+1.
\]
The following formulas determine its complete \(D_n\times C_2\)-character. Write \(r(i,j)=(i+1,j)\), \(s(i,j)=(-i,j)\), \(t(i,j)=(i,1-j)\), with indices modulo \(n\). Let \(0\le a<n\).

For **odd** \(n\), the character \(\chi_n\) is

| Symmetry | Homology trace |
| --- | --- |
| \(r^a\) | \(B_n\) for \(a=0\); \(1\) otherwise |
| \(r^a t\) | \(-1\) for every \(a\) |
| \(r^a s\) | \(4-n\) for every \(a\) |
| \(r^a st\) | \(n-2\) for every \(a\) |

For **even** \(n\), the character is

| Symmetry | Homology trace |
| --- | --- |
| \(r^a\) | \(B_n\) for \(a=0\); \(1-n\) for \(a=n/2\); \(1\) otherwise |
| \(r^a t\) | \(1-n\) for \(a=n/2\); \(1\) otherwise |
| \(r^a s\) | \(9-n\) for even \(a\); \(3-n\) for odd \(a\) |
| \(r^a st\) | \(1-n\) for even \(a\); \(3-n\) for odd \(a\) |

In particular the rational invariant subspace has the exact parity-sensitive dimension
\[
\boxed{\dim H_n^{D_n\times C_2}=
\begin{cases}(n-3)/2,&n\text{ odd},\\0,&n\text{ even}.\end{cases}}
\]
These formulas describe a representation refinement; the nonequivariant integral homology and homotopy dimensions are credited to previous work.

## Assumptions and scope
The graph has \(2n\) labeled vertices \((i,j)\), where \(i\in\mathbb Z/n\mathbb Z\) and \(j\in\{0,1\}\). An edge joins \((i,j)\) to \((i+1,j)\), or \((i,0)\) to \((i,1)\). All simplicial chains use increasing-vertex orientations. This is the ordinary three-cut complex, not the total three-cut complex. The group action is that of the named geometric automorphisms; no claim about additional exceptional automorphisms is made. Character formulas concern rational homology, although the underlying homology is free integral.

## Proof
**1. The Alexander dual and its homology.** Set \(K_n=X_n^\vee\) on the same \(2n\)-element ground set. A subset belongs to \(K_n\) precisely when each of its three-element subsets induces a connected graph. For \(n\ge5\), \(G_n\) is triangle-free and three-regular, so the connected induced triples are exactly its paths of length two. Thus \(K_n\) has a complete one-skeleton, exactly \(6n\) triangular faces (three at each of \(2n\) centers), and exactly \(n\) tetrahedra, one for each square \(Q_i=\{(i,0),(i+1,0),(i,1),(i+1,1)\}\). Indeed, if all triples in a four-set are connected, each triple has at least two edges, forcing at least four edges in the four-set; triangle-freeness forces exactly four, a square. Conversely all triples of a square are paths. A five-set with all its four-subsets squares would have \(5\cdot4=3e\), where \(e\) counts induced edges, which is impossible. Hence there are no larger faces.

More concretely, \(K_n\) simplicially collapses to a connected graph in exactly \(6n\) elementary free-face pairs. Write each square in order \(A=(i,0),B=(i+1,0),C=(i,1),D=(i+1,1)\). First remove each tetrahedron with its face \(ABC\). Second, remove every horizontal length-two path triangle with its *private* endpoint-chord edge (there are \(2n\) such triangles; for \(n\ge5\) these chords are distinct and occur in no other triangle). For each square then remove the three remaining triangles, paired in order with \(AB\), \(AD\), and \(BC\): respectively \((ABD,AB)\), \((ACD,AD)\), and \((BCD,BC)\). At each step the indicated edge lies in precisely its displayed triangle; squares have disjoint mixed triangles and the preceding steps have deleted the other cofaces. The residual graph retains all rungs and is connected. It has \(2n\) vertices and \(\binom{2n}{2}-5n\) edges, and thus
\[
\widetilde H_1(K_n;\mathbb Z)\cong\mathbb Z^{\binom{2n}{2}-7n+1}=\mathbb Z^{B_n},
\]
with all other reduced homology zero. Equivariant combinatorial Alexander duality, and the original vertex permutation on the ambient simplex, identify the rational character of \(H_n\) with the sign twist of the dual first-cohomology character. The degree \(2n-4\) assertion and absence of other reduced homology also follow directly. Since \(X_n\) contains the entire \((2n-6)\)-skeleton of the ambient simplex and has dimension \(2n-4\), it is a wedge of \(B_n\) spheres of that dimension, consistent with previously established nonequivariant results.

**2. A uniform signed fixed-face formula.** For any symmetry \(g\), let \(T_j(g)\) be the trace of \(g\) on oriented simplicial \(j\)-chains of \(K_n\), for \(j=0,1,2,3\). Each \(T_j\) equals the sum, over setwise invariant \((j+1)\)-vertex faces, of the sign of the vertex permutation restricted to that face. Since \(K_n\) is connected and has rational homology only in degrees zero and one, the Hopf trace identity gives
\[
\operatorname{tr}(g\mid H_1(K_n;\mathbb Q))
=1-T_0(g)+T_1(g)-T_2(g)+T_3(g).
\]
Naturality of combinatorial Alexander duality twists this character by \(\operatorname{sgn}_{2n}(g)\), the sign of the permutation of all \(2n\) vertices. Here \(r\) and \(s\) both have even sign, whereas \(t\) has sign \((-1)^n\). Therefore
\[
\chi_n(g)=\operatorname{sgn}_{2n}(g)
\bigl(1-T_0(g)+T_1(g)-T_2(g)+T_3(g)\bigr).
\]

For transparency, the complete chain trace computation is given next. Entries are the four-tuples \((T_0,T_1,T_2,T_3)\); empty classes are excluded as indicated. For **odd** \(n\):

| Symmetry class | Trace tuple |
| --- | --- |
| \(1\) | \((2n,\binom{2n}{2},6n,n)\) |
| \(r^a\), \(a\ne0\) | \((0,0,0,0)\) |
| \(t\) | \((0,-n,0,n)\) |
| \(r^at\), \(a\ne0\) | \((0,0,0,0)\) |
| \(r^as\) | \((2,2-n,-2,1)\) |
| \(r^ast\) | \((0,-n,0,1)\) |

For **even** \(n\):

| Symmetry class | Trace tuple |
| --- | --- |
| \(1\) | \((2n,\binom{2n}{2},6n,n)\) |
| \(r^{n/2}\) | \((0,-n,0,0)\) |
| \(r^a\), \(a\notin\{0,n/2\}\) | \((0,0,0,0)\) |
| \(t\) | \((0,-n,0,n)\) |
| \(r^{n/2}t\) | \((0,-n,0,0)\) |
| \(r^at\), \(a\notin\{0,n/2\}\) | \((0,0,0,0)\) |
| \(r^as\), even \(a\) | \((4,8-n,-4,0)\) |
| \(r^as\), odd \(a\) | \((0,-n,0,2)\) |
| \(r^ast\), even \(a\) | \((0,-n,0,0)\) |
| \(r^ast\), odd \(a\) | \((0,-n,0,2)\) |

The tuples follow by fixed-subset counting, uniformly in \(n\): \(T_0\) is the number \(F\) of fixed vertices; for the *complete* one-skeleton, \(T_1=\binom F2-Q\), where \(Q\) is the number of transpositions in the full-vertex cycle decomposition (a transposed pair contributes sign \(-1\)). For \(T_2\) enumerate invariant length-two paths by their unique center and unordered pair of distinct neighbors, and assign the sign of the induced permutation on the three vertices. Reflections preserving layers fix two horizontal path triangles with orientation \(-1\) when \(n\) is odd; when \(n\) is even, vertex-axis reflections fix four such triangles with orientation \(-1\), and the edge-axis case fixes none. No other nonidentity class fixes a path triangle. For \(T_3\), enumerate squares \(Q_i\): the layer swap \(t\) fixes all \(n\) squares with positive orientation; for odd \(n\), a reflection with or without layer swap fixes one square positively; for even \(n\), edge-axis reflections with or without layer swap fix two squares positively. No other nonidentity classes fix squares. Combining these observations gives every entry of the tables by elementary congruences for \(i\) modulo \(n\). Substitution in the signed fixed-face formula proves the stated character tables for all \(n\ge5\).

**3. Invariant classes.** Over \(\mathbb Q\), averaging the character over the group gives the invariant dimension. Summing the odd-size table over all \(4n\) elements gives \(2n(n-3)\); summing the even-size table gives zero. Dividing by \(4n\) yields the displayed invariant dimensions. These are integer-valued and nonnegative for the specified range.

## Verification
The standalone `VERIFY.py`, using only Python's standard library, constructs the dual complex directly from its graph and verifies all \(6n\) free-face collapses for each \(5\le n\le16\). It computes all oriented chain traces for all \(4n\) group elements, checks the closed character tables, and verifies the dimensions of the invariants. This is \(504\) group-element checks and \(756\) elementary collapse checks. An independent second construction enumerates **every** nonempty simplex of the ordinary three-cut complex for \(5\le n\le8\) and compares its signed Lefschetz trace with the dual character for another \(104\) group elements. The actual machine output is embedded as `VERIFIER_OUTPUT.txt` and ends with `VERIFY_OK`. These finite checks corroborate, but do not substitute for, the preceding proof for arbitrary \(n\).

## Relationship to prior work
Bayer and collaborators introduced ordinary cut complexes and studied homology representations and the Cartesian prism over a **complete graph**, which is distinct from the circular ladder. Chauhan, Shukla and Vinayak subsequently conjectured exactly the nonequivariant rank \(B_n\) for ordinary three-cut complexes of circular ladders (Conjecture 4.6(ii)); they did not give this dihedral-and-layer-swap character. A subsequent published mathematical note, *Sphere-wedge topology of three-cut complexes of circular ladders* (2026), already established the nonequivariant integral wedge-of-spheres classification for all \(n\ge5\), explicitly leaving group representations untreated. The novelty claimed here is **only** the entire symmetry character and the parity-sensitive invariant-subspace dimension, not the rank, integral homology concentration, homotopy type, or the original conjecture.

## Limitations
The formulas treat only the natural action of \(D_n\times C_2\) on rational homology for \(n\ge5\), not the full integral module isomorphism class, homology of quotients with integral coefficients, other cut parameters, or the exceptional graph \(C_4\square K_2\). An equivalent formula in unindexed equivariant-topology literature remains an originality risk. The independent external scientific audit has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), https://arxiv.org/abs/2304.13675 .
2. P. Chauhan, S. Shukla, K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486 (first public 2025-12-04), especially Conjecture 4.6(ii), https://arxiv.org/abs/2512.04486 .
3. *Sphere-wedge topology of three-cut complexes of circular ladders*, previously published mathematical research note (2026-10-11). Its nonequivariant conclusion is expressly treated as prior work.
