# Independent mathematical audit

## correctness

PASS

Reconstructed the proof for uniform labelled GL_n(F₂). The independent vectors e_k² force the supports of images of distinct natural-basis vectors to be disjoint; invertibility makes the automorphism matrix monomial, hence a permutation over F₂. Preservation of squares is equivalent to commuting with the structure matrix. For a transposition write P=I+N with N a single rank-one nilpotent block, Nv=u and N zero on u and the n−2 complementary vectors. A commuting map sends u to au, v to bu+av+w, and a complement vector x to Dx+λ(x)u. Ordering the basis as u, complement, v gives block-triangular determinant a² det D, so the invertible count is 2^(2n−3)|GL_(n−2)(2)|. Dividing by |GL_n(2)| gives the stated probability, including n=2. In the full matrix space, an invariant matrix is constant on simultaneous ordered-pair orbits. For a permutation moving k letters in s nontrivial cycles, the codimension is at least 2(n−k)(k−s)+k²/2, since all orbits on moved–moved ordered pairs have size at least two. The union bound for 3≤k≤n/2 starts at n³2^(−9n/4), and for k>n/2 is bounded by n!2^(−n²/8); the positive lower bound on invertibility preserves negligibility. Two distinct transpositions imply a three-cycle or a double transposition, with respective codimensions 4n−6 and 4n−8 by counting the orbits on their three or four moved letters and the pairs with fixed letters. Thus O(n⁴) intersections are negligible in Bonferroni. This yields the stated leading probability and, conditionally, exactly one nonidentity element, a natural-basis transposition. The finite enumeration code was inspected, not executed.

## originality

FAIL

The distinct indexed record c0b936280b48 has the same sampling, exact transposition probability, and sharp rare-symmetry law. Its proof controls all nontranspositions, so the natural-basis-transposition conditional conclusion is also covered, not just the abstract C₂ isomorphism type. It additionally gives a sharper error estimate and a Burnside orbit-count correction. Its column convention is equivalent to the frozen row convention by transposition, which is a bijection on GL_n(F₂) and preserves every permutation commutation condition. The path dates do not settle priority; the assessment is demonstrated equivalent and stronger coverage, not a provenance finding.

## value

FAIL

The leading effect of conditioning on invertibility and the identification of transpositions are mathematically meaningful. But as a distinct finding, the frozen record reproduces exactly those facts from the indexed comparison, which already has a sharper estimate. Its coarser support-size proof and finite census do not supply a different invariant, stronger classification, or separate substantive conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
