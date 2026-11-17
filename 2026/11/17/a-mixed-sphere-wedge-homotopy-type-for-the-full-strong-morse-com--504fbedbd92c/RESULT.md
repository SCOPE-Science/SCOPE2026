# A mixed sphere-wedge homotopy type for the full strong Morse complex of the ten-cycle

## Finding
Let \(C_{10}\) be the unfilled simplicial cycle with vertices \(\mathbb Z/10\mathbb Z\), and let \(\mathcal{SM}(C_{10})\) be the **full** complex of strong discrete-Morse matchings, defined as the downward closure of all matchings induced by injective vertex filtrations in the sense of Knudson and Owens-White. Then
\[
\boxed{|\mathcal{SM}(C_{10})|\simeq S^4\vee S^5\vee S^5.}
\]
In particular its only nonzero reduced integral homology is \(\widetilde H_4\cong\mathbb Z\) and \(\widetilde H_5\cong\mathbb Z^2\). The full complex has 6,480 nonempty simplices and admits an acyclic face-poset matching with one critical vertex, one critical four-simplex, and two critical five-simplices, whose signed integer degree matrix is \((0\ \ 0)\).

## Assumptions and scope
The graph is a one-dimensional abstract simplicial complex: it has graph edges \(e_v=\{v,v+1\}\), with indices modulo ten, **no** filled two-cells, and no extra chords. A strong gradient comes from a strict ordering of vertices by a real filtration; a graph vertex whose descending link is a one-point cone is paired with its incident edge toward its unique earlier neighbor. The full strong matching complex contains all subsets of all such gradients; it is neither the pure top-facet subcomplex nor the ordinary complex of arbitrary acyclic discrete-Morse matchings.

Index the twenty possible vertex-edge incidences by integers \(0,\ldots,19\): label \(2v\) means pairing vertex \(v\) with \(e_{v-1}\), and label \(2v+1\) means pairing \(v\) with \(e_v\). Represent each face by its nonzero 20-bit mask. Orient each simplex by increasing incidence label. The result concerns only this ten-vertex cycle, not all cycle lengths.

## Proof
**1. Complete face generation.** Orient each of the ten cycle edges forward (sign 1) or backward (sign 0). Exactly two orientations—both constant—form directed cycles, so the other \(2^{10}-2=1022\) orientations are acyclic and admit strict linear extensions. At a vertex \(v\), the descending link is a discrete set consisting of its earlier neighbors; it is a cone precisely when exactly one neighbor is earlier. In the edge-orientation word this happens precisely when the signs on \(e_{v-1}\) and \(e_v\) agree. Two signs 1 give incidence label \(2v\), and two signs 0 give incidence label \(2v+1\). Thus the displayed orientation algorithm generates *every* strong gradient and no extraneous one. Distinct acyclic orientations give 1,021 distinct gradients; taking all nonempty subsets yields exactly 6,480 faces, with face vector by dimensions zero through seven:
\[
(20,160,660,1520,2000,1470,560,90).
\]
An independent program enumerates all \(10!=3,628,800\) strict vertex orders, directly computes the unique-earlier-neighbor pairs, and checks equality of its 1,021 gradients with those from the orientation method. Therefore the face generation is exhaustive, not sampled.

**2. An explicit complete acyclic matching.** Process incidence-bit labels in this exact order:
```
19,1,13,9,10,8,3,6,12,15,17,16,4,18,0,11,5,2,7,14
```
Initially all 6,480 nonempty faces are unmatched. At a label \(b\), traverse the faces in increasing cardinality then numeric bit-mask order; when both \(F\) and \(F\cup\{b\}\) remain unmatched and \(b\notin F\), pair them and remove both from the unmatched set. This produces 3,238 disjoint cover pairs. The four critical masks, in increasing order, are
```
70689, 86097, 141864, 524288
```
with simplex dimensions four, five, five and zero, respectively. For **every** Hasse covering relation \(F\subset U\), \(|U\setminus F|=1\), direct the edge from \(U\) to \(F\), reversing it only if \((F,U)\) is a matching pair. The exhaustive checker builds all 31,840 directed covering edges and removes all 6,480 faces by a topological sort. Thus the matching is acyclic. This global check is essential: a greedy matching by itself would not be proof of acyclicity.

**3. Exact signed attaching degrees.** Give any face \(F\) its increasing-label orientation, so the cellular simplicial boundary is \(\partial F=\sum_j(-1)^j(F\setminus\{b_j\})\). For a lower matched face \(L\) paired upward with \(U\), eliminate \(L\) using the unit coefficient of \(L\) in \(\partial U\); its projection to critical faces is the negative, pivot-normalized sum of projections of the other facets of \(U\). An upper matched face projects to zero, and a critical face projects to itself. The directed acyclicity above makes this recursive integer elimination well-founded. Applying it to each critical five-cell produces the exact reduced Morse boundary from its two degree-five generators to its one degree-four generator:
\[
\partial^{\mathrm{Morse}}_5=\begin{pmatrix}0&0\end{pmatrix}.
\]
The provided script checks the actual integer coefficients, including orientation signs, not merely their reductions modulo a prime.

**4. Homotopy, not just homology.** Forman's discrete-Morse theorem supplies a CW complex with exactly one zero-cell, one four-cell and two five-cells. Its four-skeleton is \(S^4\). Each five-cell is attached by an element of \(\pi_4(S^4)\cong\mathbb Z\), determined by its integer degree. Both degrees vanish by Step 3, hence both attaching maps are nullhomotopic. The resulting CW complex is \(S^4\vee S^5\vee S^5\), establishing the asserted integral homotopy equivalence.

## Verification
The self-contained source files `enumerate_orders.cpp`, `verify_c10.py`, and `gradients.txt` reproduce the entire finite certificate. With a C++17 compiler and Python 3 standard library, run:
```
g++ -O2 -std=c++17 enumerate_orders.cpp -o enumerate_orders
./enumerate_orders gradients_regenerated.txt
python3 verify_c10.py gradients_regenerated.txt
```
The Python program independently generates gradients by all acyclic edge orientations, checks their equality with the order-generated text, builds all faces, executes the specified matching, verifies disjointness and all Hasse directions, proves acyclicity by full topological sorting, and evaluates the integral Morse attaching-degree matrix by exact recursion. It separately computes the original simplicial boundary ranks over \(\mathbb F_2\), yielding reduced Betti ranks one in degree four and two in degree five. The modular computation corroborates but does not replace the integral cellular-boundary argument. A recorded successful run appears in `verification_output.txt`. No nonstandard Python packages or external theorem-proving services are used.

## Relationship to prior work
Knudson and Owens-White (2026) define the full strong-Morse complex, classify the **pure** cycle complex homotopically, and give full-cycle **homology** for orders through 21. Their calculation already implies the two reduced Betti ranks for order ten but does not establish this full-complex homotopy equivalence. A subsequent all-length integral homology result determines the abstract torsion-free groups for every order, including ten, while expressly not classifying the higher attaching maps or asserting sphere-wedge homotopy types. A separate exact calculation gives the full complex's homotopy type for the nine-cycle; that is a different simplicial complex. The contribution here is the full ten-cycle homotopy decomposition from an explicit acyclic matching and exact integer attaching-degree computation, beyond the known homology.

## Limitations
The theorem is restricted to the **full** strong-Morse matching complex of the **unfilled ten-cycle**. No claim is made about other cycle lengths, the pure subcomplex, an equivariant integral decomposition, or a simplicial collapse onto a wedge. Exhaustive finite computations, together with the specified topology theorems, prove this finite case; finite-field ranks alone would not exclude torsion or establish homotopy type. An equivalent result might exist in literature not indexed by the sources examined. No independent mathematical audit has been performed.

## References
1. K. P. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first submitted 2026-09-06. https://arxiv.org/abs/2609.06844 ; relevant Sections 3–4 and 8 (definitions, cycle results and homology table).
2. *Uniform integral homology of full strong Morse matching complexes of cycles*, published mathematical record dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-uniform-integral-homology-of-full-strong-morse-matching-complexe--43f58158c288 (integral homology but not homotopy classification).
3. *Integral homotopy type of the full strong Morse matching complex of the nine-cycle*, published mathematical record dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-homotopy-type-of-the-full-strong-morse-matching-complex--e87f9e9fd5ee (nine-cycle case).
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (acyclic matchings and Morse CW complexes).
