# Adjacency-sensitive sphere wedges from two forward shortcuts in a directed cycle

## Finding
Let \(n\ge6\), and let \(D_{n,d}\) have vertex set \(\mathbb Z/n\mathbb Z\), all coherently oriented rim arcs \(e_i:i\to i+1\), and precisely two additional arcs \(f_0:0\to2\) and \(f_d:d\to d+2\). Indices are reduced modulo \(n\), and \(1\le d\le\lfloor n/2\rfloor\). Let \(X(D)\) be the abstract simplicial complex whose vertices are directed arcs and whose faces are disjoint unions of directed paths (including isolated vertices). Then the complete **integral homotopy type** is
\[
X(D_{n,d})\simeq
\begin{cases}
S^{n-2}\vee\bigvee^2 S^{n-3},&d=1,\\
S^{n-2}\vee\bigvee^2 S^{n-3}\vee S^{n-4},&2\le d\le\lfloor n/2\rfloor.
\end{cases}
\]
The same distinction applies to any two distinct length-two shortcut starts: the first case means they are adjacent on the cyclic index set, and the second means they are nonadjacent. With either shortcut adjoined first, the inclusions of the original rim complex into the one-shortcut complex and then into the two-shortcut complex are **homotopy split inclusions** (after noncanonical wedge identifications). Thus the induced inclusions on integral homology are primitive split injections. No torsion occurs.

The new phenomenon is that the second shortcut creates an independent class of dimension \(n-4\) exactly when its starting position is nonadjacent to the first; adjacent starts only add a second class of dimension \(n-3\). For instance, at \(n=6\) the nonadjacent type is \(S^4\vee S^3\vee S^3\vee S^2\), while the adjacent type has no \(S^2\) summand.

## Assumptions and scope
All digraphs are finite and have no repeated arcs. A permitted arc subset has at most one outgoing and at most one incoming arc at each graph vertex, and no directed cycle; these conditions are equivalent to a spanning disjoint union of directed paths. The parameter restriction \(n\ge6\) ensures the link boundaries appearing below are ordinary nonempty spheres of nonnegative dimension. We consider exactly two forward, length-two shortcuts; no reverse arcs, additional shortcuts or metric operations are included. All homology groups have integer coefficients. A rotation exchanges the two marked starts, replacing \(d\) with \(n-d\); hence the displayed range represents all cyclic separations.

We write \(\Delta(W)\) for the full simplex on a finite vertex set \(W\), \(\partial\Delta(W)\) for its boundary and \(v*L\) for the cone on a simplicial complex \(L\) with new apex \(v\). As usual the boundary of a simplex on \(m\ge2\) vertices is \(S^{m-2}\).

## Proof
**First, the rim and one shortcut.** Put \(E=\{e_0,\ldots,e_{n-1}\}\). A rim subset is a union of directed paths exactly when it is not all of \(E\). Thus \(Y=X(\overrightarrow C_n)=\partial\Delta(E)\cong S^{n-2}\). A face containing \(f_0\) omits both \(e_0\) (same source) and \(e_1\) (same target). Among the remaining rim arcs, the unique forbidden combination is the entire return path \(e_2,e_3,\ldots,e_{n-1}\), which closes a directed cycle with \(f_0\). Consequently, setting \(B=E\setminus\{e_0,e_1\}\),
\[
K_1=X(\overrightarrow C_n+f_0)=Y\cup_{L_0}(f_0*L_0),\qquad L_0=\partial\Delta(B)\cong S^{n-4}.
\]
The inclusion \(L_0\to Y\cong S^{n-2}\) is nullhomotopic by dimension/connectivity. Attaching a cone along a nullhomotopic map yields \(K_1\simeq S^{n-2}\vee S^{n-3}\), with \(Y\) homotopy-split as a wedge summand. This also identifies the part of the one-shortcut theorem needed here.

**Second, the exact second-shortcut link.** Write \(K_2=X(D_{n,d})\) and \(L=\operatorname{lk}_{K_2}(f_d)\). The deletion of \(f_d\) is \(K_1\), hence \(K_2=K_1\cup_L(f_d*L)\). Faces of \(L\) not containing \(f_0\) consist of proper subsets of \(W=E\setminus\{e_d,e_{d+1}\}\), since these are exactly the rim arcs compatible with \(f_d\) and their full set is the directed return cycle. This part is \(A=\partial\Delta(W)\cong S^{n-4}\).

If \(d=1\), the two shortcuts jointly exclude exactly \(e_0,e_1,e_2\). Put \(U=E\setminus\{e_0,e_1,e_2\}\). No directed cycle can use both shortcuts: \(f_0\) ends at vertex \(2\), from which \(e_2\) is unavailable, while any path from the end of \(f_1\) to the start of \(f_1\) would require \(e_0\). Thus every subset of \(U\) is allowed when both shortcuts are present. It follows that
\[
L=A\cup_{\Delta(U)}\bigl(f_0*\Delta(U)\bigr),\quad \Delta(U)\subset A.
\]
The added simplex collapses onto its face \(\Delta(U)\); therefore \(L\simeq A\simeq S^{n-4}\).

If \(2\le d\le\lfloor n/2\rfloor\), the four excluded rim arcs \(e_0,e_1,e_d,e_{d+1}\) are distinct. Put \(U=E\setminus\{e_0,e_1,e_d,e_{d+1}\}\), so \(|U|=n-4\) and \(U\subset W\). A directed cycle using only one shortcut is impossible because its return path contains a rim arc excluded by the other shortcut. With both shortcuts, the **only** possible directed cycle is
\[
0\xrightarrow{f_0}2\to3\to\cdots\to d\xrightarrow{f_d}d+2\to\cdots\to n-1\to0,
\]
whose rim arcs are precisely all of \(U\) (with empty intervening stretches allowed). Therefore
\[
L=A\cup_{\partial\Delta(U)}\bigl(f_0*\partial\Delta(U)\bigr),\qquad
A=\partial\Delta(W)\cong S^{n-4},\quad
\partial\Delta(U)\cong S^{n-6}.
\]
Since \(S^{n-4}\) is \((n-5)\)-connected, the attaching map \(S^{n-6}\to S^{n-4}\) is nullhomotopic. Consequently \(L\simeq S^{n-4}\vee S^{n-5}\).

**Third, split off the second cone.** In both cases \(L\) has dimension at most \(n-4\). The previously determined complex \(K_1\simeq S^{n-2}\vee S^{n-3}\) is \((n-4)\)-connected. By cellular approximation, *every* map from \(L\) to \(K_1\), including the actual link inclusion, is nullhomotopic. Thus
\[
K_2=K_1\cup_L(f_d*L)\simeq K_1\vee\Sigma L.
\]
In the adjacent case \(\Sigma L\simeq S^{n-3}\); in the nonadjacent case \(\Sigma L\simeq S^{n-3}\vee S^{n-4}\). Combining with the first step proves the stated homotopy types. The wedge models can be chosen relative to each successive included subcomplex, giving split homotopy inclusions and hence primitive split integral homology injections. Switching the order of the shortcuts produces the same argument after rotation, proving order independence. \(\square\)

## Verification
The standalone script `verify_pair_shortcuts.py` constructs faces from source/target degree restrictions and direct directed-cycle detection, without invoking the link formulas. For every \(6\le n\le12\) and every \(1\le d\le\lfloor n/2\rfloor\), it independently checks the exact second-shortcut link, inclusions and reduced Euler characteristic at all three filtration stages: 90 cases and 166,469 accumulated augmented faces. For \(6\le n\le10\) it also builds signed boundary matrices and verifies all reduced Betti ranks over both \(\mathbb F_2\) and \(\mathbb F_3\): 114 stage/field cases. It prints `VERIFY_OK` on success. The integral wedge and inclusion assertions follow from the explicit proof, not from finite-field calculations.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith [1] develop multipath complexes for oriented polygons and other directed families; their coherently oriented cycle is the original boundary sphere. Caputi, Collari and Smith [2] study bidirected polygons, whose arc sets contain every rim reversal and are not the two-shortcut digraphs. Deshpande and Sawant [3] provide a conflict-hypergraph formulation for directed-linear-forest complexes and ask for explicit homotopy types in broader families with directed cycles, but do not give this two-shortcut classification. A public 2026 result [4] establishes the one-forward-shortcut dichotomy and its relative collapse, and explicitly does **not** assert a multiple-shortcut theorem. The present classification identifies the additional nonadjacent interaction term \(S^{n-4}\) and all integral inclusion splittings. General deletion/link identities and the one-shortcut formula alone do not state this gap-sensitive outcome; the exact two-shortcut link and its new directed cycle must be analyzed.

## Limitations
This concerns exactly two forward length-two shortcuts on one coherently oriented cycle, for \(n\ge6\). It does not address three or more shortcuts, longer chords, other orientations, the three-to-five vertex boundary cases, or equivariant maps under the full cyclic group. The wedge splittings exist but are not canonical in the presence of additional symmetries. The prior-work comparison is a targeted rather than exhaustive priority search; an unindexed equivalent theorem remains possible. Independent mathematical validation has not been performed.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first public 2022-08-09), https://arxiv.org/abs/2208.04656.
2. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first public 2026-01-09), https://arxiv.org/abs/2601.05670.
3. P. Deshpande, R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936 (first public 2026-02-16), https://arxiv.org/abs/2602.14936.
4. *A sharp shortcut-length transition in directed-cycle multipath complexes*, public research note dated 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-sharp-shortcut-length-transition-in-directed-cycle-multipath-c--bafb14ca69f1/RESULT.md.
