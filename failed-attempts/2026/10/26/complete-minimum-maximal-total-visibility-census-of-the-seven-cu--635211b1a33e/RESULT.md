# Complete minimum-maximal total-visibility census of the seven-cube

## Finding
Let \(Q_7\) be the binary seven-dimensional hypercube, with its \(128\) vertices individually distinguished. A subset \(S\) is **total mutual-visible** when every pair of cube vertices admits a shortest path whose internal vertices avoid \(S\). It is **maximal** when no vertex can be added while preserving this property. Let \(\mu_{\mathrm t}^{-}(Q_7)\) be the smallest size of such a maximal set.

Then
\[
\boxed{\mu_{\mathrm t}^{-}(Q_7)=8,\qquad
\#\{S:\ S\text{ is maximal total mutual-visible and }|S|=8\}=1{,}254{,}400.}
\]
Every set counted has exactly the following form, and every such choice qualifies. Partition the binary cube by coordinate-sum parity. In **each** parity class choose an affine two-plane of four points \(\{a,a+u,a+v,a+u+v\}\), with arithmetic in \(\mathbb F_2^7\), such that the three nonzero differences \(u,v,u+v\) have Hamming weights \(4,4,6\) in some order. Take the union of the independently chosen even and odd planes.

There are precisely \(1{,}120\) qualifying affine planes in either parity class. Thus the exact number of named minimum maximal sets is \(1{,}120^2\). These are configurations, not colorings or objects taken modulo cube automorphisms.

## Assumptions and scope
The graph is the simple undirected Cartesian power \(K_2^{\square7}\). Identify vertices with \(\mathbb F_2^7\); distance is Hamming distance, addition is coordinatewise modulo two, and the parity classes consist of the \(64\) vertices of even and odd weight. An affine two-plane here has **exactly four points**; it is not a Euclidean plane. The definition of maximality is by inclusion, not by largest cardinality. All counts distinguish cube vertices, with no symmetry quotient.

## Proof
**1. The distance-two criterion.** For any binary cube \(Q_n\), a set \(S\) is total mutual-visible exactly when no pair of its members is at Hamming distance two. For necessity, if selected vertices are opposite corners of a convex square, the other opposite pair has only the two selected intermediate vertices on its length-two geodesics. For sufficiency, induct on the distance between arbitrary endpoints. At distance at least two, at least two neighbors of the first endpoint decrease distance to the other; those two neighbors are at mutual Hamming distance two, so at least one avoids \(S\). Continue by induction from that neighbor. This also reconstructs the established Hamming-graph characterization in [2].

The distance-two condition operates separately within each parity class. Consequently a set is inclusion-maximal if and only if each of its even and odd parts is an inclusion-maximal independent set in the corresponding **halved cube**: the graph whose same-parity vertices are adjacent exactly when their Hamming distance is two. Write \(H\) for either of the two isomorphic \(64\)-vertex halved seven-cubes.

**2. A lower bound of four in each half.** A vertex \(x\) of \(H\) dominates the closed set
\[
B(x)=\{y:d_{\mathrm H}(x,y)\in\{0,2\}\},\qquad |B(x)|=1+\binom72=22.
\]
Distinct centers in an independent set of \(H\) have Hamming distance \(4\) or \(6\). If the distance is four, their closed neighborhoods intersect in exactly \(\binom42=6\) vertices: flip two of the four differing coordinates. At distance six, the closed neighborhoods are disjoint. In an independent set of at least three vertices, no center can have two partners at distance six: such partners would differ in exactly two coordinates. Hence any independent triple contains a distance-four pair. Its three closed neighborhoods together cover at most \(22+22-6+22=60<64\) vertices. No independent set of at most three is dominating. Therefore each maximal independent set in \(H\) has at least four members.

**3. Exactly which four-element sets dominate.** Let \(C\) be an independent four-subset of \(H\), and let \(r\) count its pairs at Hamming distance six. The distance-six pairs form a matching, hence \(r\in\{0,1,2\}\). Each distance-four pair contributes a six-element pairwise intersection of closed neighborhoods; distance-six pairs contribute none. A triple has a nonempty threefold intersection precisely when all three distances are four, and in that case the intersection has exactly one point. To see the latter, translate one center to zero; the other two are weight-four vectors with precisely two common supported coordinates, and their shared weight-two midpoint is the unique point at distance at most two from all three.

If \(r=0\), inclusion-exclusion gives a union of at most \(4(22)-6(6)+4=56\) vertices (the fourfold intersection, if any, can only reduce it). If \(r=1\), exactly two triples have all pairwise distances four, and no fourfold intersection is possible, giving \(4(22)-5(6)+2=60\). If \(r=2\), every triple contains a distance-six pair, so all higher intersections vanish; the union contains exactly \(4(22)-4(6)=64\) vertices. Thus \(C\) dominates \(H\) if and only if it has two disjoint distance-six pairs. Since it is independent, this also proves its maximality.

**4. Affine-plane rigidity.** Translate one center of a distance-six pair to \(0\) and call its partner \(b\), where \(b\) has weight six and a unique zero coordinate \(i\). Because all four cross-distances are four, each of the other two centers is a weight-four vector containing coordinate \(i\) and exactly three of the six support coordinates of \(b\). Those two three-element supports must be complementary to make the remaining pair have distance six. Therefore the two centers are \(c\) and \(b+c\). The four-set is the affine plane \(\{0,b,c,b+c\}\), with nonzero differences of weights \(6,4,4\). Reversing this argument shows that every plane of the stated type is independent and dominating.

**5. Counting.** Each of the \(64\) centers has \(7\) centers at distance six, so there are \(64\cdot7/2=224\) unordered distance-six pairs in \(H\). For a fixed such pair, the other distance-six pair arises from choosing \(c\) to contain the one missing coordinate and any three of the other six: \(\binom63=20\) ordered possibilities, or ten unordered complementary pairs \(\{c,b+c\}\). Every qualifying four-set is counted twice, once from either of its distance-six pairs. Consequently the number of minimum maximal independent sets in one parity class is
\[
\frac{224\cdot10}{2}=1{,}120.
\]
The two parity classes are independent under distance-two exclusion. Each contributes at least four points, and every pair of qualifying affine planes yields a maximal total mutual-visible set of size eight. The number is \(1{,}120\cdot1{,}120=1{,}254{,}400\), proving the theorem.

For a concrete witness, one may take the even plane \(\{0,15,113,126\}\), using seven-bit integer encodings, and translate it by toggling the first bit to obtain the odd plane \(\{1,14,112,127\}\). Their union is one of the claimed eight-vertex sets.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3.10 or later. The standalone verifier enumerates all independent dominating sets of cardinality at most four in the even halfcube for dimensions one through seven. For dimension seven it finds exactly \(1{,}120\) four-subsets, checks the common distance pattern \((4,4,4,4,6,6)\) and affine-plane parity identity, and confirms none of size at most three. An independent direct-geodesic test checks the concrete eight-vertex witness against all pairs of cube vertices and verifies that all \(120\) attempted one-vertex extensions fail. The recorded output is in \(\texttt{verification_output.txt}\).

These tests are finite corroboration; the classification and count above are established by the complete combinatorial proof, not by extrapolation. The script tests the precise labeled graph, not a sampled or symmetry-reduced surrogate.

## Relationship to prior work
Brešar and Yero [1], in their first public preprint of 6 July 2023, introduced the lower total mutual-visibility number and explicitly posed its determination for hypercubes (Problem 1). Bujtás, Klavžar and Tian [2] proved the equivalent prohibition on distance-two pairs for all Hamming graphs (Theorem 6). Both are essential foundations, **not** claimed as new.

The halved-cube domination-number table [3] already lists the scalar domination number \(\gamma(H)=4\) for the halved seven-cube. Together with a suitable independent witness, this supports the scalar lower-total-visibility value eight; that numerical value alone is **not** advanced as the originality of this work. The new assertion evaluated here is the exact complete classification of *all* optimum inclusion-maximal total-visibility configurations, the affine-plane rigidity, and the count \(1{,}254{,}400\), none of which is supplied by the scalar table. The subsequent hypercube visibility study [4] addresses maximum total mutual-visibility and not this minimum-maximal configuration census. A relevant published distance-limited mutual-visibility result studies a different requirement (visibility at bounded distance, not minimum-maximal total visibility), and does not imply this count.

## Limitations
The classification and \(1{,}254{,}400\) count apply only to \(Q_7\) and only to smallest inclusion-maximal total mutual-visibility sets. They do not enumerate larger maximal sets, solve the arbitrary-dimensional problem, or classify configurations up to automorphism. The halved-cube domination number four is prior known information. An equivalent enumeration under an unindexed coding-theory or distance-regular-graph formulation cannot be excluded without further bibliographic review; no claim of independent validation or exhaustive priority certification is made.

## References
[1] B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, first posted 2023-07-06, Problem 1. https://arxiv.org/abs/2307.02951

[2] C. Bujtás, S. Klavžar and J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168, first posted 2023-07-11, Theorem 6. https://arxiv.org/abs/2307.05168

[3] E. W. Weisstein, *Domination Number*, MathWorld, table entry for halved cube graphs (known scalar sequence). https://mathworld.wolfram.com/DominationNumber.html

[4] *Visibility in Hypercubes*, Graphs and Combinatorics, 2026, Section 4 (maximum total mutual-visibility bounds). https://doi.org/10.1007/s00373-026-03025-9
