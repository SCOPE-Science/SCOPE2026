# Reflection fixed loci of pure strong Morse complexes of cycles are two simplices

## Finding
For every integer \(n\ge6\), let \(X_n=\mathcal{SM}_{\mathrm{pure}}(C_n)\) be the pure strong discrete Morse matching complex of the unfilled cycle with vertices \(\mathbb Z/n\mathbb Z\). For each \(a\in\mathbb Z/n\mathbb Z\), let \(s_a(v)=a-v\) be a graph reflection. Its induced simplicial involution on \(X_n\) has geometric fixed-point set **PL-homeomorphic to the disjoint union of two simplices**:
\[
\boxed{
 |X_n|^{s_a}\cong_{\rm PL}\Delta^{d(n,a)}\sqcup\Delta^{d(n,a)},
\qquad
 d(n,a)=\begin{cases}
 (n-5)/2,&n\text{ odd},\\
 n/2-2,&n\text{ even and }a\text{ even},\\
 n/2-3,&n\text{ even and }a\text{ odd}.
 \end{cases}}
\]
In particular every reflection fixed-point space is homotopy equivalent to \(S^0\), and its reduced integral homology is \(\mathbb Z\) in degree zero and zero in all other degrees. The reduced rational Lefschetz number of **each reflection** is \(+1\). The latter equality alone is strictly weaker than the fixed-space classification.

## Assumptions and scope
An edge is \(e_i=\{i,i+1\}\), indexed modulo \(n\). A vertex of the matching complex is an incidence \((i,+)=(i,e_i)\) or \((i,-)=(i+1,e_i)\); we use the sign convention of the published cycle-facet classification. A face is a subset of a largest-cardinality strong matching, not an arbitrary discrete Morse matching or a face of the full strong complex. The geometric fixed-point set is taken in the ordinary affine realization, with equal barycentric coordinates on exchanged incidence vertices; it is not the subcomplex on individually fixed incidence vertices. The two distinguished types of reflections when \(n\) is even are those through opposite graph vertices (even \(a\)) and those through opposite edge midpoints (odd \(a\)). The empty simplex is not a point in the geometric realization.

## Proof
**1. The source's explicit maximal faces.** The facet classification for pure strong matchings on cycles (Knudson--Owens-White, Proposition 8.3, in its consecutive-edge-gap form) says that the facets of \(X_n\) are precisely the following \(n(n-1)\) incidence sets. Choose \(b\in\mathbb Z/n\mathbb Z\) and \(0\le j\le n-2\); omit the two consecutive edges \(e_b,e_{b+1}\). Reading the remaining edges \(e_{b+2},\ldots,e_{b+n-1}\) cyclically forward, choose \(+\) for the first \(j\) incidences and \(-\) for the remaining \(n-2-j\). Every face is a subset of one such facet. Hence, for any face containing both signs, their edge indices occur in cyclicly ordered contiguous sign blocks, with an interval of **two consecutive omitted edges** between the last negative and first positive incidence. In particular, four signs alternating in cyclic edge order cannot lie in one face.

**2. Orbit model for geometric fixed points.** The reflection sends the incidence \((i,+)\) to \((\rho_a(i),-)\) and \((i,-)\) to \((\rho_a(i),+)\), where \(\rho_a(i)=a-i-1\pmod n\). Every orbit of incidence vertices has two elements (the two incidence signs differ), and at most one incidence from a given graph edge can belong to a face. Invariant nonempty faces are thus exactly unions of allowable two-element orbits. The fixed simplex of one invariant face is the simplex on its incidence orbits, using their common barycentric weights. Gluing these fixed simplices realizes the orbit-face simplicial complex \(Y_{n,a}\) and gives a canonical piecewise-linear homeomorphism \(|X_n|^{s_a}\cong_{\rm PL}|Y_{n,a}|\).

**3. Precisely which incidence orbits are allowable.** Write \(P_i=\{(i,+),(\rho_a(i),-)\}\) and \(N_i=\{(i,-),(\rho_a(i),+)\}\). The orbit \(P_i\) occurs in a facet if and only if the positive-edge index \(i\) differs from the negative-edge index \(\rho_a(i)\) and, in the forward cyclic edge order, there are at least two edge indices strictly between \(\rho_a(i)\) and \(i\). Necessity follows because the two omitted consecutive edges must lie between the negative and positive positions. Conversely, choose any two consecutive edges in that gap as the omitted pair and put the single sign change elsewhere; the specified incidences then lie in the resulting facet. The same statement with the signs interchanged tests \(N_i\). A direct substitution of \(\rho_a(i)\), using the conjugation \(s_{a+2t}=r^t s_a r^{-t}\), gives exactly two **disjoint** allowable orbit families in each case:

For \(n=2m+1\) and \(a=0\), they are \(\{P_i:1\le i\le m-1\}\) and \(\{N_i:0\le i\le m-2\}\).

For \(n=2m\) and \(a=0\), they are again \(\{P_i:1\le i\le m-1\}\) and \(\{N_i:0\le i\le m-2\}\).

For \(n=2m\) and \(a=1\), they are \(\{P_i:2\le i\le m-1\}\) and \(\{N_i:1\le i\le m-2\}\).

All intervals in this paragraph are ordinary integer intervals; the reflection map itself is modulo \(n\). These are all allowable individual incidence orbits, not merely a selected subcollection.

**4. They are two simplices, with no mixed faces.** Every subset of either displayed family lies in a single maximal face of \(X_n\). For \(a=0\), all the \(P_i\) of the first family occur in the facet omitting \(e_{n-1},e_0\), and all the \(N_i\) of the second family occur in the facet omitting \(e_{m-1},e_m\). The same two omitted pairs work for the \(a=1\) families, with the families assigned in the same order. Thus each family spans a full simplex of \(Y_{n,a}\).

No face can contain an orbit from both families: choose the positive and negative representative edge indices \(i,j\) in their respective lower-half intervals. If \(i=j\), the mixed choice uses both incidences of the same graph edge, which a matching forbids. If \(i\ne j\), the lower-half incidences and their reflected upper-half partners have the cyclic sign pattern \(+,-,+,-\) or \(-,+,-,+\), contrary to Step 1. Therefore \(Y_{n,a}\) is the **disjoint** union of the two complete simplices. The displayed family sizes are respectively \(m-1,m-1,m-2\) in the three cases, giving dimensions \(m-2,m-2,m-3\). The conjugacy relation covers every \(a\). This proves the PL-homeomorphism and the integral homotopy and homology conclusions.

**5. Lefschetz consequence.** A reflection has exactly two contractible fixed components, hence ordinary fixed-point Euler characteristic two. The simplicial Hopf trace theorem, with orientation signs included, gives ordinary Lefschetz number two and reduced Lefschetz number one. Equivalently each invariant simplex consists of two-element incidence orbits and contributes with the alternating sign of its orbit count. This does not assume any concentration of the homology of \(X_n\).

## Verification
Run `python3 verify_pure_reflections.py` using only Python's standard library. The program independently builds **every** published-model facet, reflects every incidence, constructs orbit projections of all facets, checks maximal projected orbit sets against the two explicit proposed simplices for \(6\le n\le50\) (68 reflection-axis cases), and for \(n\le11\) additionally enumerates every original simplex and directly tests setwise reflection invariance instead of relying on facet projection. In the smaller cases it explicitly enumerates the fixed-orbit faces and checks the augmented signed Euler count. The recorded result is `ALL_VERIFY_OK checked_axes=68 n_min=6 n_max=50 fully_enumerated_fixed_faces=1242 full_invariant_axes=9`. Finite computations corroborate the theorem but do not prove its unlimited range; Steps 1--5 give the all-parameter proof.

## Relationship to prior work
Knudson and Owens-White's 2026 paper introduces these strong complexes and classifies the **nonequivariant** homotopy types of the pure cycle family. A previously published all-length computation describes the **rotation** homology characters of the same pure cycle complexes, but explicitly leaves reflection actions open. Another published dihedral calculation concerns the different **full** strong cycle complexes, not the pure ones. Here the subject is the precise geometric fixed-point *homotopy*, which is not determined even by a complete alternating rational character. The two-simplex model and parity-dependent dimensions are separate structural information.

## Limitations
The result concerns only pure strong matching complexes of unfilled cycles with \(n\ge6\) and geometric fixed points of single dihedral reflections. It does not classify fixed sets of combined symmetry subgroups, orbit-space homotopy types or integral dihedral representations on the homology of the ambient complex. The 2026 primary preprint's full text was not retrievable during the comparison; its first-public abstract and a later complete public mathematical proof of the exact same cycle facet list were examined. This leaves some residual unindexed or incidental-literature overlap risk; the result has no independent external certification.

## References
1. K. P. Knudson and A. Owens--White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first public September 6, 2026, especially Proposition 8.3 and Theorem 8.6. https://arxiv.org/abs/2609.06844.
2. *The threefold rotation character of pure strong Morse matching complexes of cycles*, published-finding corpus public mathematical record (2026), `2026/10/11/SCOPE-the-threefold-rotation-character-of-pure-strong-morse-matching-c--0dacd6b82f58`. Its full mathematical proof provides the explicit facet list and rotation-only comparison.
3. *Dihedral Euler characters of full strong Morse complexes of cycles*, published-finding corpus public mathematical record (2026), `2026/10/11/SCOPE-dihedral-euler-characters-of-full-strong-morse-complexes-of-cycl--4819a9d67705` (different full complex).
