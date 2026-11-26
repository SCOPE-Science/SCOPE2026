# A four-torsion Moore wedge from Kreweras complementation in type-\(B_4\)

## Finding

Let \(W\) be the rank-four signed-permutation Coxeter group, let \(T\) be its sixteen reflections, and take the Coxeter element \(c=(2,3,4,-1)\), in signed one-line notation. Let \(\ell_T\) denote reflection length and set
\[
P=\{w\in W:\ell_T(w)+\ell_T(w^{-1}c)=4\},\qquad
X=\Delta(P\setminus\{e,c\}).
\]
The generalized Kreweras complement \(K(w)=w^{-1}c\) is an order-reversing bijection of \(P\) of order eight; it acts simplicially on \(X\), reversing the order of the vertices of each image chain. The **ordinary geometric orbit space** has the complete homotopy classification
\[
\boxed{|X|/\langle K\rangle\simeq M(\mathbb Z/4\mathbb Z,1)\vee\bigvee^4 S^2,}
\]
where the Moore space means \(M(\mathbb Z/4\mathbb Z,1)=S^1\cup_{\deg4}e^2\). In particular,
\[
\pi_1(|X|/\langle K\rangle)\cong\mathbb Z/4\mathbb Z,\qquad
H_j(|X|/\langle K\rangle;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/4\mathbb Z,&j=1,\\
\mathbb Z^4,&j=2,\\
0,&j\ge3.
\end{cases}
\]
Thus the canonical rank-reversing symmetry creates genuine order-four fundamental-group torsion in a quotient of a torsion-free sphere-wedge complex.

## Assumptions and scope

Signed permutations are tuples \((w(1),w(2),w(3),w(4))\) with distinct absolute values \(1,2,3,4\), extended by \(w(-i)=-w(i)\). Multiplication is function composition, \(uv=u\circ v\). The sixteen reflections consist of the four single-coordinate sign changes and twelve signed exchanges. Reflection length is word length in this generating set; equivalently it is the real fixed-space codimension in the standard signed-permutation representation. Absolute order is \(u\le_T v\) precisely when \(\ell_T(u)+\ell_T(u^{-1}v)=\ell_T(v)\). A simplex of \(X\) is a strictly increasing chain of proper interval elements. For each such chain, \(K\) reverses the chain and hence induces an ordinary vertex-permutation simplicial action on the unoriented simplex.

The quotient is \(|X|/\langle K\rangle\) with its ordinary topology, not the Borel construction, a homotopy quotient, nor the order complex of the element-orbit poset. Because \(K\) reverses rank, the original triangulation has possible simplex inversions; all quotient cell calculations below use its barycentric subdivision, where simplex dimensions distinguish chain vertices. The statement concerns the single rank-four Coxeter type and does not assert uniformity in higher ranks.

## Proof

**1. Finite absolute interval and symmetry.** Exhaustive breadth-first search in the Cayley graph of the 384 signed permutations using all sixteen reflections agrees, at every group element, with the signed-cycle fixed-codimension formula. The Coxeter element has reflection length four. Testing \(\ell_T(w)+\ell_T(w^{-1}c)=4\) gives exactly 70 interval elements, with rank counts \((1,16,36,16,1)\). Hence the proper-part order complex has 68 vertices, 288 edges and 256 triangles. The formula \(K(w)=w^{-1}c\) preserves the interval and reverses absolute order. Direct composition gives \(K^2(w)=c^{-1}wc\); in this case \(K\) has order eight.

**2. Genuine quotient and presentation.** Passing to the barycentric subdivision, a vertex now corresponds to an original nonempty simplex; a simplex is a strictly dimension-increasing flag of such faces. The action cannot invert a flag, since it preserves the dimensions of original faces. There are 612 barycentric vertices, 2,112 edges and 1,536 triangles. Exhaustively forming orbits of all flags under the eight Kreweras powers produces a quotient delta-complex with 77 vertices, 264 edges and 192 triangles. Its characteristic maps may identify different boundary faces, so the computation uses orbit edge orientations and the full triangular attaching words, not a naive simplicial complex on vertex-orbits.

Choose a spanning tree of the quotient's one-skeleton; its 76 edges contract without changing homotopy type. The resulting two-dimensional presentation CW complex has one vertex, 188 one-cells and 192 two-cells. Orient each non-tree edge in the original strictly increasing face-dimension direction, and for a triangular flag \((a,b,c)\), use the boundary word traversing \((a,b)\), \((b,c)\), and \((a,c)\) backwards. The exact enumeration and this orientation convention are implemented in `verify.py`.

**3. One-cell and two-cell cancellations.** In a presentation two-complex, if a two-cell attaching word contains a given one-cell generator exactly once with exponent \(\pm1\), a change of free basis of the one-skeleton followed by a one-/two-cell cancellation eliminates that generator and two-cell, without changing the homotopy type. The words of the other attaching maps are updated by free-group substitution. This is stronger than merely deleting a generator from a presentation of the fundamental group.

The deterministic cancellation in `verify.py` performs **187** such moves, updating all remaining attaching words exactly and preserving empty words (null attaching circles). What remains has one one-cell, five two-cells, and the attaching degrees, up to signs and order, \((0,0,4,4,4)\). The program checks that every remaining word is freely reduced and contains only the surviving generator. For one circle, cellular two-cell slides (unimodular integer row operations on degrees, realizable by homotopy equivalences of these two-dimensional CW complexes) replace this degree vector by \((4,0,0,0,0)\). Four nullhomotopic two-cells give four wedged two-spheres; the remaining circle and degree-four two-cell form \(M(\mathbb Z/4\mathbb Z,1)\). This proves the asserted homotopy equivalence and its homotopy and homology consequences.

**4. Independent integral chain check.** The separate `verify_integral_chains.py` regenerates the orbit cells, constructs the signed integer boundary matrices of sizes \(77\times264\) and \(264\times192\), and checks \(\partial_1\partial_2=0\) entry by entry. Exact Smith forms give 76 unit factors in \(\partial_1\) and 187 units plus a single factor four in \(\partial_2\). Because \(\partial_1\) has a primitive image and both chain groups are free, this also gives \(H_1\cong\mathbb Z/4\) and \(H_2\cong\mathbb Z^4\) without relying on the presentation cancellation. This chain calculation independently corroborates the integral homology, whereas the explicit one-/two-cell cancellations certify the stronger homotopy type.

## Verification

Run `python3 verify.py` using Python 3 with no third-party dependencies; its success marker is `B4_KREWERAS_WEDGE_CERTIFICATE_OK`. The trace has 187 verified cancellable pairs and SHA-256 `25a49e9a4473dec46f0fb702aeefd74e8592fe12c16db58f84909ceec47c0f33`, computed from the ordered substitutions. Run `python3 verify_integral_chains.py` from the same directory with Python 3 and SymPy available; its success marker is `B4_KREWERAS_INTEGRAL_SMITH_OK`. The two checkers use the same explicit orbit-enumeration routines; one works with homotopy-preserving two-cell cancellations, while the other constructs and diagonalizes exact integer cellular boundaries. Both use exact operations. They are exhaustive for this rank-four complex; no finite evidence is extrapolated to an infinite family.

## Relationship to prior work

Reiner's type-\(B\) noncrossing-partition theory establishes the underlying shellable lattice structure and self-duality, but not the homotopy type of the specified quotient. Armstrong describes the generalized Kreweras map in absolute-order notation and its relation \(K^2(w)=c^{-1}wc\). Bessis and Reiner analyze cyclic sieving for Coxeter conjugation and also state a cyclic-sieving conjecture for the full Kreweras action, using the inverse generator \(w\mapsto c w^{-1}=K^{-1}(w)\). Their full-group conjecture concerns fixed-element enumeration and does not classify the ordinary geometric orbit space. These establish the naturality of the symmetry but do not specify quotient attaching maps or order-four torsion. A closely related published finite computation determines the **Coxeter-conjugation quotient**, with \(H_1\cong\mathbb Z/2\) and \(H_2\cong\mathbb Z^9\). That action is generated by \(K^2\), whereas the present quotient includes \(K\) itself and has \(\pi_1\cong\mathbb Z/4\) and four two-spheres. The old homology data do not imply this stronger quotient's homotopy type. No matching statement was found in the inspected sources; absence from searches cannot establish universal novelty.

## Limitations

The conclusion concerns exactly the ordinary Kreweras orbit space for type \(B_4\); it neither provides an integral equivariant homology representation for the covering complex nor extends automatically to other Coxeter types or ranks. Its proof depends on the correctly specified no-inversions barycentric orbit model, not on a free group action, and on exact finite cancellations rather than a general collapse theorem. Equivalent unpublished, unindexed or inaccessible prior calculations remain possible. No independent external mathematical audit is claimed.

## References

- V. Reiner, *Non-crossing partitions for classical reflection groups*, *Discrete Mathematics* **177** (1997), 195–222, https://doi.org/10.1016/S0012-365X(96)00365-2 ; lawful full text: https://personal.utdallas.edu/~nxw170830/docs/SLC93/papers/1997%20-%20Reiner%20-%20Non-crossing%20partitions%20for%20classical%20reflection%20groups.pdf (publicly dated 1997-12-01).
- D. Armstrong, *Generalized Noncrossing Partitions and Combinatorics of Coxeter Groups*, arXiv:math/0611106, first public version 2006-11-04, https://arxiv.org/abs/math/0611106.
- D. Bessis and V. Reiner, *Cyclic sieving of noncrossing partitions for complex reflection groups*, arXiv:math/0701792, first public version 2007-01-27, https://arxiv.org/abs/math/0701792.
- *Two-torsion in the Coxeter-rotation quotient of the type-\(B_4\) noncrossing partition complex*, public computation, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-two-torsion-in-the-coxeter-rotation-quotient-of-the-type-b-4-non--9b99f8f67a9a/RESULT.md.
