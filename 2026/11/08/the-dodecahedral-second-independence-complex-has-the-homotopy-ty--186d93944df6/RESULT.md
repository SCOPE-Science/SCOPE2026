# The dodecahedral second independence complex has the homotopy type of \(S^6\)

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph. Its second independence complex is homotopy equivalent, **integrally**, to a single six-sphere:

\[
\operatorname{Ind}_2(D)\simeq S^6.
\]

Here \(\operatorname{Ind}_2(D)\) is the simplicial complex of vertex subsets whose induced connected components have at most two vertices. This result gives a homotopy type, not just homology or an Euler characteristic. The complex has simplices of dimension eleven, so the sphere is not obtained from a dimensional purity argument.

## Assumptions and scope

Use the explicit dodecahedral graph \(D\) on the twenty vertices \(u_0,\ldots,u_9,v_0,\ldots,v_9\), with indices interpreted modulo ten and edge set

\[
\{u_i u_{i+1},\ u_i v_i,\ v_i v_{i+2}:0\le i<10\}.
\]

A face is a subset \(\sigma\) of these vertices such that every connected component of \(D[\sigma]\) has at most two vertices. Equivalently, \(\sigma\) contains no pair of adjacent edges of \(D\). Thus the forbidden sets are the sixty three-vertex paths centered at a vertex of degree three. This interpretation also identifies the complex as the \(P_3\)-devoid (or dissociation) complex of \(D\).

For machine representation, the bit indexed \(i\) encodes \(u_i\) for \(0\le i<10\), while bit \(10+i\) encodes \(v_i\). The empty face is bitmask zero. Every count and every Morse pair below refers to precisely this encoding.

## Proof

**1. Exhaustive face description.** For each integer bitmask \(s\) from zero to \(2^{20}-1\), define \(F(s)\) to mean that no forbidden triple is contained in \(s\). This is an exhaustive, decidable test of the complex: the center vertex of a connected induced component with at least three vertices has two distinct neighbors in the component, and conversely a selected length-two path gives a connected component of size at least three. Hence the test is equivalent to the defining face condition. An independently implemented recursive test, inserting the least indexed vertex of each bitmask, gives the same result at every one of the \(2^{20}\) masks.

The face counts for sizes \(0,1,\ldots,12\) are, respectively,

\[
(1,20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5).
\]

There are no larger faces. Thus the complex has \(63{,}143\) faces including the empty face, and \(63{,}142\) nonempty faces.

**2. Exact discrete-Morse matching.** Process the pivot vertices in the order

\[
u_0,v_0,u_1,v_1,\ldots,u_9,v_9.
\]

At each pivot \(w\), scan the nonempty face bitmasks in increasing numerical order. If a face \(\sigma\) does not contain \(w\), and both \(\sigma\) and \(\sigma\cup\{w\}\) are currently unmatched faces, match this pair. Never pair the empty face. This deterministic prescription makes \(31{,}569\) matching pairs. It leaves one critical vertex, two critical six-dimensional faces with bitmasks \(26312\) and \(420992\), and one critical seven-dimensional face with bitmask \(406098\). It leaves no other nonempty critical face.

Orient every face-poset covering relation from the larger face to the smaller face, except reverse the matched relations. The attached standalone checker constructs all \(410{,}520\) covering relations and topologically sorts the resulting directed graph. Exactly \(63{,}143\) nodes are removed. Thus the matching is acyclic, rather than merely conjecturally so. Forman's discrete-Morse theorem supplies a homotopy-equivalent CW complex with one zero-cell, two six-cells and one seven-cell.

**3. Integral attaching degree.** Order every simplex by increasing bit index, and give its boundary the usual alternating signs. For each six-face \(b\) paired upward with a seven-face \(a\), the incidence coefficient \(\epsilon(a,b)\) is \(\pm1\). Solving its cellular relation expresses \(b\) as the negative of the other signed six-faces in \(\partial a\), divided by that unit. Recursively apply these relations along the verified acyclic gradient graph. A six-face paired downward with a five-face contributes zero; a critical six-face contributes its standard basis vector. Applied to the boundary of the unique critical seven-face, this exact integer recursion gives

\[
\partial^{\mathrm{Morse}}_7=\begin{pmatrix}1\\1\end{pmatrix}.
\]

The attached verifier checks each recursion and every integer addition for overflow, and verifies both entries. The displayed boundary is primitive: its coefficients have greatest common divisor one.

**4. Homotopy conclusion.** The Morse CW complex has six-skeleton \(S^6\vee S^6\), and one seven-cell attached along a map whose degree vector is \((1,1)\). Because \(S^6\vee S^6\) is five-connected, the Hurewicz isomorphism identifies \(\pi_6(S^6\vee S^6)\) with \(\mathbb Z^2\). An integral change of basis takes this primitive degree vector to \((1,0)\); the associated seven-cell cancels one six-sphere. The remaining homotopy type is \(S^6\). This proves the claim over the integers; no assumption of torsion-freeness from finite-field homology is needed.

## Verification

The standalone source files `verify_morse.cpp` and `verify_mod2.cpp` are compilable with a C++17 compiler (for example, `g++ -O3 -std=c++17`). Run the corresponding binaries without command-line arguments. The recorded outputs are `verification_morse.txt` and `verification_mod2.txt`. The first verifier exhausts all \(2^{20}\) subsets in two representations, checks the face vector, all face-poset covering relations, acyclicity and the signed integer Morse boundary. The second independently reduces the augmented simplicial chain boundaries over \(\mathbb F_2\), obtaining reduced Betti number one in dimension six and zero elsewhere. The finite chain calculation corroborates the proof; it does not replace the integral attaching-map calculation.

## Relationship to prior work

Taylan's 2015 paper develops matching trees for devoid complexes and computes such complexes for paths, cycles and forests; the dodecahedral graph is not among the classified families. Deshpande and Singh's higher-independence homotopy classification covers complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect rooted trees, not the dodecahedral graph. The second independence complex is not the ordinary independence complex or the edge matching complex of \(D\), and their known homotopy types do not imply this conclusion. The dodecahedral graph is an antipodal double cover of the Petersen graph, but this graph covering is not a covering equivalence of their second independence complexes. Thus an exact calculation for the Petersen graph does not determine the present homotopy type.

## Limitations

The theorem is for the single explicitly specified graph \(GP(10,2)\) and the parameter two. It makes no claim about homeomorphism to a six-sphere, equivariant structure, other generalized Petersen graphs, or the induced maps between higher-independence stages. The computation is finite but exhaustive for this graph; it is not a general classification of cubic graphs. Publication priority remains subject to possible unindexed equivalent results. The result has not undergone independent mathematical validation.

## References

- Demet Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754 (first public version 2015-01-27), particularly the definitions and path/cycle/forest results.
- Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first public version 2020-01-15), especially the listed graph-family classifications and the discrete-Morse method.
- Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete-Morse theorem).
- Derek A. Waller, *Double covers of graphs*, Bulletin of the Australian Mathematical Society 14 (1976), 233–248, for the dodecahedron-to-Petersen antipodal covering (context only, not used to deduce the theorem).
