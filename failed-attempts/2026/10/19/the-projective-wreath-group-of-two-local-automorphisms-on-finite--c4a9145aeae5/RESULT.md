# The projective wreath group of two-local automorphisms on finite split square-zero algebras

## Finding
Let \(K=\mathbb F_q\) be a finite field, let \(n\ge1\), and put \(A=K\oplus V\), where \(V\) is an \(n\)-dimensional \(K\)-space and \((c,v)(d,w)=(cd,cw+dv)\). Thus \(A\) is a unital, commutative, split local algebra whose radical \(V\) has square zero. A *two-local automorphism* is an arbitrary set map \(\Delta:A\to A\) such that for each pair \(x,y\in A\), a single ordinary \(K\)-algebra automorphism \(T_{x,y}\) satisfies \(\Delta(x)=T_{x,y}(x)\) and \(\Delta(y)=T_{x,y}(y)\). Neither linearity nor bijectivity is assumed beforehand.

**Theorem.** Every two-local automorphism has a unique expression
\[
\Delta(c+v)=c+f(v),
\]
where \(f(0)=0\), \(f(av)=af(v)\) for all \(a\in K\), \(v\in V\), and the resulting map of one-dimensional subspaces \([v]\mapsto[f(v)]\) is a permutation of the projective point set \(\mathbb P(V)\). Here each nonzero line is mapped bijectively onto its target line, with a freely chosen nonzero scalar multiplier. Conversely, every such \(f\) defines a two-local automorphism. Write \(N=|\mathbb P(V)|=(q^n-1)/(q-1)\). Their composition group and count are
\[
\operatorname{2LocAut}_K(A)\cong (K^\times)^N\rtimes S_N,\qquad |\operatorname{2LocAut}_K(A)|=(q-1)^N N!.
\]
(The displayed group isomorphism requires choosing one vector on each line.) Ordinary automorphisms are exactly \(\mathrm{GL}_n(q)\), of order \(\prod_{i=0}^{n-1}(q^n-q^i)\). Equality between these two groups holds precisely when \(n=1\) or \((q,n)=(2,2)\); in every other case there are nonlinear two-local automorphisms.

## Assumptions and scope
All algebra automorphisms are unital \(K\)-linear algebra automorphisms. The field is an arbitrary finite field, including prime-power extensions and characteristic two. The two-local map itself is not assumed linear. The statement is not asserted for infinite base fields, for radical cube-zero rings, or for automorphisms that move the coefficient field.

## Proof
**(1) Ordinary automorphisms.** Invertible elements are exactly the elements with nonzero scalar component, hence the Jacobson radical \(V\) is characteristic. Every \(K\)-algebra automorphism fixes \(K\cdot1\) and restricts to an invertible \(K\)-linear map on \(V\). Conversely each member of \(\mathrm{GL}_K(V)\), extended by the identity on \(K\), preserves the displayed multiplication. This proves \(\operatorname{Aut}_K(A)\cong\mathrm{GL}_n(q)\).

**(2) Necessary two-local conditions.** For any \(c\in K\), comparison with any other point gives \(\Delta(c)=c\). For the pair \((v,c+v)\), their common witnessing automorphism sends the first point to a vector \(f(v)\) and the second to \(c+f(v)\), so \(\Delta(c+v)=c+f(v)\). For the pair \((v,av)\), the common witnessing \(K\)-linear automorphism yields \(f(av)=af(v)\). Each nonzero vector must have nonzero image. If \(v,w\) are linearly independent, their images under the common invertible witness are independent. Thus distinct projective lines have distinct image lines. There are finitely many of them, so the induced injection is a permutation. Within each line, homogeneity fixes the entire map from the choice of the nonzero image of one representative.

**(3) Sufficiency.** Suppose \(f\) is homogeneous and permutes projective lines as stated. For any pair \(c+v,d+w\), if \(v,w\) are linearly dependent, choose an invertible linear map sending a nonzero generator of their common line to its prescribed image; homogeneity makes it agree with \(f\) at both points. If \(v,w\) are linearly independent, their images are independent because the induced projective map is injective; extend \(v,w\) and \(f(v),f(w)\) to two bases of \(V\), obtaining an invertible linear map agreeing at the pair. Extend this linear map by the identity on \(K\). This supplies the required common algebra-automorphism witness for every pair.

**(4) Group and size.** Choose one nonzero representative of each of the \(N\) projective lines. A two-local map freely permutes these \(N\) lines and chooses one of \(q-1\) nonzero scalings on each; every choice is valid by (3). Thus there are \((q-1)^N N!\) maps. Composition yields the ordinary permutation/scaling wreath product, with the displayed noncanonical decomposition. These maps are all bijections because their restrictions and projective permutations are bijective.

**(5) Sharp rigidity threshold.** When \(n=1\), every homogeneous map is scalar multiplication. When \((q,n)=(2,2)\), there are three nonzero vectors, each on a distinct line, and every permutation extends uniquely to \(\mathrm{GL}_2(2)\), which also has order six. For \(q>2\) and \(n\ge2\), scale only one selected projective line by a nonidentity scalar and fix all other vectors. A linear map fixing every vector outside one line would fix all of \(V\): there exist independent fixed vectors and enough other fixed vectors to span the space with cross-line sums (equivalently, the fixed-vector set of any nonidentity linear map is a proper subspace, whereas the complement of a single line cannot lie in one proper subspace). Thus this map is not linear. For \(q=2\) and \(n\ge3\), interchange two nonzero vectors and fix the others. It is a projective-line permutation, hence two-local. But a nonidentity linear map has at most \(2^{n-1}-1\) nonzero fixed vectors, whereas this transposition fixes \(2^n-3>2^{n-1}-1\) for \(n\ge3\). Therefore it is not linear. The stated alternatives are exhaustive.

## Verification
The attached `verify.py` enumerates all homogeneous projective-line permutations for \((q,n)=(2,2),(3,2),(2,3)\), computes the full general linear groups, checks the predicted cardinalities and indices, and directly checks the common-witness condition against actual invertible linear maps for every ordered pair in the two-dimensional cases and selected representatives in the binary three-dimensional case. It prints `VERIFY_OK`. These experiments check finite examples, not the unrestricted symbolic proof above.

## Relationship to prior work
Arzikulov, Khakimov and Qurbonov (arXiv:2511.17316, first posted 2025-11-21) classify linear local automorphisms and local derivations for certain five-dimensional naturally graded *nilpotent* associative algebras; their result neither specifies the unital radical-square-zero family nor classifies arbitrary nonlinear two-local maps. Arzikulov, Karimjanov and Umrzaqov (2024, DOI:10.13069/jacodesmath.v11i3.279; precursor arXiv:2305.13720) study null-filiform and filiform associative algebras, whose multiplication types differ from \(K\oplus V\) with \(V^2=0\). Ayupov and collaborators (arXiv:1911.03194) give conditional linearity statements and examples for two-local maps on finite-dimensional Jordan algebras, primarily under matrix-symmetry hypotheses; the general unrestricted \(\mathrm{GL}_n(q)\) projective permutation count here does not follow from the inspected statements. The theorem may also be described in linear-action language as a classification of pairwise-interpolable transformations; such an older equivalence cannot be categorically ruled out.

## Limitations
The classification is for finite fields and split local commutative algebras with square-zero radical only. The precise group isomorphism uses arbitrary projective representatives. The derivation is elementary linear algebra, but the global classification, precise finite-field count and exact rigidity boundary are not consequences of the cited results that were inspected. No independent historical priority or independent mathematical audit is claimed.

## References
1. F. Arzikulov, U. Khakimov, A. Qurbonov, *The relationship between local derivations and local automorphisms of some associative algebras*, arXiv:2511.17316 (first public 2025-11-21), https://arxiv.org/html/2511.17316v3.
2. F. N. Arzikulov, I. A. Karimjanov, S. M. Umrzaqov, *Local and 2-local automorphisms of null-filiform and filiform associative algebras*, Journal of Algebra Combinatorics Discrete Structures and Applications 11 (2024), DOI:10.13069/jacodesmath.v11i3.279.
3. Sh. Ayupov et al., *Description of 2-local derivations and automorphisms on finite dimensional Jordan algebras*, arXiv:1911.03194, https://arxiv.org/html/1911.03194v2.
4. Sh. Ayupov, K. Kudaybergenov, *2-local automorphisms on finite-dimensional Lie algebras*, arXiv:1602.05187, https://arxiv.org/html/1602.05187v1.
