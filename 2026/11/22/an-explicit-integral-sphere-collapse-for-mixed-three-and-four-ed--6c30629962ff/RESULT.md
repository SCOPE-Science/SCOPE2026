# An explicit integral sphere collapse for mixed three- and four-edge multitheta graphs

## Finding
For integers \(m,q\ge 1\) with \(m+q\ge3\), define \(T_{m,q}\) as the finite simple graph consisting of two nonadjacent poles \(u,v\), \(m\) internally vertex-disjoint paths \(u-a_i-b_i-c_i-v\) of length four, and \(q\) internally vertex-disjoint paths \(u-\alpha_j-\beta_j-v\) of length three, with no further edges. Set \(X_{m,q}=\operatorname{Ind}(T_{m,q})\), the simplicial complex whose faces are independent vertex sets.

**Theorem.** The entire complex \(X_{m,q}\) admits an explicit sequence of exactly
\[
N(m,q)=2^{m-1}+3^m2^q+\frac{3^q(5^m-3^m)}2
\]
elementary free-face collapses onto the crosspolytope boundary \(\bigast_{i=1}^{m}\{b_i,c_i\}*\bigast_{j=1}^{q}\{\alpha_j,\beta_j\}\). Consequently,
\[
X_{m,q}\searrow S^{m+q-1},\qquad \widetilde H_k(X_{m,q};\mathbb Z)=\begin{cases}\mathbb Z,&k=m+q-1,\\0,&k\ne m+q-1.\end{cases}
\]
The notation \(\searrow\) means a simplicial collapse onto the **specified simplicial triangulation** of the sphere, not merely an abstract homotopy equivalence.

The full graph automorphism group is \(S_m\times S_q\times C_2\): the symmetric factors permute the equal-length paths, and the last factor exchanges the poles, reversing every path. Its action on the unique reduced integral homology line is
\[
\widetilde H_{m+q-1}(X_{m,q};\mathbb Z)\cong \operatorname{sgn}_{S_m}\boxtimes\operatorname{sgn}_{S_q}\boxtimes\varepsilon_{C_2}^{\,q},\qquad \varepsilon_{C_2}(\tau)=-1.
\]
Equivalently, \((\sigma,\rho,\tau^e)\) acts by multiplication by \(\operatorname{sgn}(\sigma)\operatorname{sgn}(\rho)(-1)^{qe}\).

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple. The two poles are nonadjacent, distinct internal paths have no common internal vertex, and the listed edges are exhaustive. Vertices and simplicial faces are *unoriented*; their oriented chain representatives use increasing vertex labels only for computation. All statements about homology are over \(\mathbb Z\); the rank-one representation is integral. Each of \(m,q\) must be positive. The bound \(m+q\ge3\) ensures that the poles, of degree at least three, are intrinsically distinguishable from the degree-two internal vertices, so the stated group is the full automorphism group. No equivariant sequence of elementary collapses is claimed.

An elementary free-face collapse deletes one face \(F\) and its unique codimension-one coface \(F\cup\{z\}\); every deletion below is ordered by **decreasing cardinality** of \(F\), breaking ties arbitrarily. This ordering is part of the certificate and guarantees freeness.

## Proof
**1. Delete the doubly occupied pole sector.** An independent set containing both \(u,v\) can contain only the vertices \(b_i\); none of the short-path internal vertices or the end vertices \(a_i,c_i\) is allowed. The sector is exactly \(\{u,v\}*\Delta_{\{b_1,\ldots,b_m\}}\). For each face containing both poles but omitting \(b_1\), pair it with its \(b_1\)-extension. In descending face-size order this is an elementary free pair: a competing coface differing by any other \(b_i\) was removed earlier. The number of pairs is \(2^{m-1}\). Afterwards no face contains both poles.

**2. Delete the singly occupied pole sectors.** In the remaining complex, an independent face containing \(u\) cannot contain \(v\) or any \(a_i,\alpha_j\). Its internal part is a face of the join of \(m\) discrete pairs \(\{b_i,c_i\}\) and \(q\) singleton simplices on \(\beta_j\). In particular the vertex \(\beta_1\) may be adjoined to any such face not containing it. Pair all these faces with their \(\beta_1\)-extensions in descending size; all their other one-vertex cofaces have been removed earlier, and cofaces involving \(v\) were deleted in step 1. There are \(3^m2^{q-1}\) pairs. Similarly, using \(\alpha_1\), delete every face containing \(v\) in another \(3^m2^{q-1}\) free pairs. The remaining complex is exactly
\[
A=\operatorname{Ind}(T_{m,q}-\{u,v\})=\bigast_{i=1}^{m}\operatorname{Ind}(a_i-b_i-c_i)*\bigast_{j=1}^{q}\{\alpha_j,\beta_j\}.
\]
Each long-arm factor has faces \(\varnothing,\{a_i\},\{b_i\},\{c_i\},\{a_i,c_i\}\); each short-arm factor is a discrete two-vertex complex.

**3. Remove long-arm free pairs.** In the remaining complex, fix a long-arm index \(i\). For every face containing \(a_i\) but not \(c_i\), pair it with the face obtained by adjoining \(c_i\), again in descending cardinality. This is legal because an independent face containing \(a_i\) does not contain its neighbor \(b_i\), while \(c_i\) is nonadjacent to \(a_i\) and all vertices outside this arm. Any competing coface is already removed by the descending ordering. This deletes exactly the interval component \(a_i-c_i\) from the corresponding \(\operatorname{Ind}(P_3)\) factor, retaining \(\{b_i\},\{c_i\},\varnothing\). Process indices \(i=1,\ldots,m\). At stage \(i\) (one-based), the number of pairs is \(3^{i-1}5^{m-i}3^q\), since processed long factors have three faces each and unprocessed ones five. Thus the total number of long-arm collapse pairs is
\[
\sum_{i=1}^{m}3^{i-1}5^{m-i}3^q=\frac{3^q(5^m-3^m)}{2}.
\]
The final complex is a join of \(m+q\) discrete two-point complexes, the boundary of an \((m+q)\)-crosspolytope; it is homeomorphic to \(S^{m+q-1}\). Adding the counts of steps 1–3 gives \(N(m,q)\). The argument is a finite constructive proof for every allowed \(m,q\); no inference from finite test data is needed.

**4. Integral automorphism action.** The intermediate inclusion \(A\hookrightarrow X_{m,q}\) is natural under every graph automorphism: although the chosen collapse *sequence* is not equivariant, the pole-deleted subcomplex \(A\) is invariant and its inclusion induces an integral homology isomorphism. Each three-internal-vertex factor \(\operatorname{Ind}(P_3)\) has precisely two connected components, the isolated \(b_i\) and contractible edge \(a_ic_i\); the pole reversal fixes these components individually. Each two-internal-vertex factor \(\operatorname{Ind}(P_2)\) has two components interchanged by pole reversal, hence the latter acts as minus one on its reduced degree-zero homology. The Künneth join isomorphism, with no torsion, identifies the top reduced homology of \(A\) with the tensor product of the \(m+q\) reduced degree-zero lines, suspended by the joins. Interchanging two factors contributes Koszul sign \((-1)^{(0+1)(0+1)}=-1\), giving the two permutation signs. Reversing all paths contributes \((-1)^q\), giving the asserted integral character. Since the poles are precisely the vertices of degree \(m+q\ge3\), every automorphism either fixes or swaps them, and preserves the two families of paths by length, proving the full-group identification.

## Verification
The included Python 3 standard-library program `check_theta.py` constructs all independent faces, executes the ordered elementary free pairs, and checks every pair has exactly one codimension-one coface at removal. It verifies \(1\le m,q\le3\) exhaustively, including the boundary crosspolytope, the exact formula for pair counts and 21 signed reduced Lefschetz character checks for natural symmetry generators. The nine graph instances contain altogether 2,829 checked collapse pairs. Reproduce from the extracted package with `python3 check_theta.py`; `check_output.txt` records the expected output. The tests are finite corroboration only; the proof above supplies the all-parameter statement.

## Relationship to prior work
Kim's theorem on graphs without induced cycles of length divisible by three gives sphere-or-contractible homotopy type for its *ternary* graph class. Here, whenever \(q\ge2\), two length-three paths create an induced six-cycle, making that hypothesis inapplicable. The present result also supplies an explicit simple collapse and full integral symmetry action, neither provided by the ternary theorem for the stated graphs.

Przytycki–Silvero's Example 3.8 analyzes ordinary independence complexes of generalized **three-arm** theta graphs by subdivision reductions. It covers some special numerical cases of the homotopy type but not arbitrary \(m+q\), and does not state the integral automorphism character or the explicit all-parameter simple-collapse certificate. The closest published all-short-arm multitheta computation gives \(S^1\vee S^{p-1}\) and its integral character for \(p\) length-three paths; it does not cover the mixed family with \(m\ge1\). Related all-long-arm results about matching complexes and graph-metric Vietoris–Rips complexes concern different functorial objects and do not imply the present independence-complex claim.

## Limitations
The graphs must contain at least one path of each specified length; other arm lengths are not classified. The all-short-arm case behaves differently: a second circle homology class can survive. The collapse is not claimed equivariant, and no equivariant homeomorphism or equivariant CW wedge decomposition is inferred from the integral homology character. The verified examples end at \(m=q=3\), while the proof covers all allowed parameters. Independently unindexed equivalences remain a bibliographic risk; no independent external audit has been performed.

## References
1. J. Kim, *The homotopy type of the independence complex of graphs with no induced cycles of length divisible by 3*, first arXiv version 2021-01-18, arXiv:2101.07131, https://arxiv.org/html/2101.07131v3 (especially Theorem 1.1).
2. J. H. Przytycki and M. Silvero, *Khovanov homology, wedges of spheres and complexity*, first journal publication 2024-05-02, DOI:10.1007/s13398-024-01594-z, https://link.springer.com/article/10.1007/s13398-024-01594-z (Section 3.1, Example 3.8).
3. *Integral arm-permutation and pole-reversal homology of subdivided multitheta graphs*, published result `2026/11/8/SCOPE-integral-arm-permutation-and-pole-reversal-homology-of-subdivide--db96fec92047`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-arm-permutation-and-pole-reversal-homology-of-subdivide--db96fec92047 (all-length-three comparison).
4. *Integral branch-symmetry homology of four-edge theta matching complexes*, published result `2026/10/25/SCOPE-integral-branch-symmetry-homology-of-four-edge-theta-matching-co--256da9cb9f64`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-branch-symmetry-homology-of-four-edge-theta-matching-co--256da9cb9f64 (different complex).
