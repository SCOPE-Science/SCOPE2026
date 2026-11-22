# Dichromatic polynomial rigidity, subunit roots, and monotonicity for oriented multi-theta networks

## Finding
Let \(P_T(x)\) count vertex assignments from \(x\) named colours in which no directed cycle is monochromatic, initially for positive integral \(x\). For the coherent, strongly connected directed multi-theta network described below, an explicit dichromatic polynomial recovers every path length, exhibits a sharp parity criterion for nontrivial real zeros below one, and is strictly monotone after normalization for every real \(x>1\).

**Theorem.** For \(r\ge2\), \(c\ge1\), and \(d_1,\ldots,d_r\ge1\), put \(D=\sum_{i=1}^r d_i\), \(N=c+D+1\). Then
\[
P_{T(c;d_1,\ldots,d_r)}(x)=x^N-x^{D+1}+x\prod_{i=1}^{r}(x^{d_i}-1).
\]
Within this family, the polynomial identifies \(c\) and the multiset of \(d_i\) uniquely. When \(r\) is even, the polynomial has one simple real root in \((0,1)\); when \(r\) is odd, none. The quotient \(P_T(x)/x^N\) is strictly increasing on \([1,\infty)\). In particular, this family satisfies the 2026 dichromatic monotonicity conjecture. The number of distinct polynomials of degree \(N\ge4\) represented by the family equals
\[
\sum_{D=2}^{N-2}(p(D)-1),
\]
where \(p(D)\) denotes the integer-partition function.

## Assumptions and scope
The digraph has two distinguished terminals \(s,t\), one directed return path \(t\to s\) consisting of \(c\) arcs, and \(r\) mutually internally disjoint directed forward paths \(s\to t\), with the \(i\)-th containing \(d_i+1\) arcs and \(d_i\) internal vertices. Every path is internally disjoint from every other path, and there are no other arcs. The conditions \(r\ge2\), \(c\ge1\), \(d_i\ge1\) make this a finite simple digraph without digons; the endpoints and path interiors give exactly \(N=c+1+D\) vertices. Every vertex lies on a directed cycle, so the digraph is strongly connected. The words *unique* and *reconstruct* below always mean **relative to the specified family**, not to arbitrary digraphs with the same dichromatic polynomial.

## Proof
**1. Exact polynomial.** Any directed cycle must traverse the complete return path and exactly one complete forward path. These are precisely the \(r\) simple directed cycles. Choose independently and uniformly \(q\) colours for all \(N\) vertices, with positive integral \(q\). The return path is monochromatic with probability \(q^{-c}\). Conditional on that event, every forward path is completely monochromatic with probability \(q^{-d_i}\); these latter events are independent because their internal vertices are disjoint. Therefore the probability of an invalid colouring is exactly
\[
q^{-c}\left(1-\prod_{i=1}^{r}(1-q^{-d_i})\right).
\]
Subtracting from one, multiplying by \(q^N\), and using \(N=c+D+1\) gives the stated formula for every positive integer \(q\), hence the polynomial identity for an indeterminate \(x\).

**2. Exact reconstruction.** Because \(r\ge2\), the product \(\prod_i(x^{d_i}-1)\) vanishes to order at least two at \(x=1\). Differentiating the polynomial identity at one yields \(P_T'(1)=N-(D+1)=c\). Thus \(c\), \(D=N-c-1\), and the integer polynomial
\[
R(x)=P_T(x)/x-x^D(x^c-1)=\prod_{i=1}^r(x^{d_i}-1)
\]
are all determined from \(P_T\) alone. Let \(e_j\) be the multiplicity of the cyclotomic polynomial \(\Phi_j(x)\) in \(R(x)\), \(j\ge1\). The standard factorization \(x^d-1=\prod_{j\mid d}\Phi_j(x)\) gives \(e_j=\#\{i:j\mid d_i\}\). Writing \(a_m=\#\{i:d_i=m\}\), the finite Möbius inversion formula
\[
a_m=\sum_{k\ge1}\mu(k)e_{km}
\]
recovers every \(a_m\); only \(km\le D\) can contribute. The unique terminals are respectively the vertex of outdegree \(r\) and the vertex of indegree \(r\), so the recovered multiset determines the directed isomorphism type. Conversely, equal parameters imply isomorphism. At fixed \(N\), choosing \(D\in\{2,\ldots,N-2\}\) determines \(c=N-D-1\), and the partitions of \(D\) into at least two positive parts number \(p(D)-1\). This proves the exact type count.

**3. Roots strictly between zero and one.** For \(0<x<1\), divide the formula by its positive factor \(x\):
\[
\frac{P_T(x)}x=-x^D(1-x^c)+(-1)^r\prod_{i=1}^r(1-x^{d_i}).
\]
If \(r\) is odd both summands are strictly negative, so there is no root. If \(r\) is even, the root equation is \(H(x)=1\), where
\[
H(x)=\frac{\prod_{i=1}^r(x^{-d_i}-1)}{1-x^c}>0.
\]
The function \(H\) is continuous, tends to \(+\infty\) as \(x\downarrow0\), and to \(0\) as \(x\uparrow1\), since \(r\ge2\). Its logarithmic derivative obeys
\[
x\frac{H'(x)}{H(x)}=-\sum_i\frac{d_i}{1-x^{d_i}}+\frac{cx^c}{1-x^c}\le-\frac{r}{1-x}+\frac{x}{1-x}<0.
\]
Here \(1-x^d\le d(1-x)\) and \(1+x+\cdots+x^{c-1}\ge cx^{c-1}\) prove the two displayed estimates. Thus the level \(H=1\) is crossed exactly once and transversely, making its corresponding polynomial zero simple.

**4. Strict normalized monotonicity.** For real \(x>1\), put \(B(x)=\prod_i(1-x^{-d_i})\). Then \(0<B(x)<1\) and \(B'(x)>0\) because every factor is strictly increasing. We have
\[
F_T(x)=\frac{P_T(x)}{x^N}=1-x^{-c}(1-B(x)),
\quad
F_T'(x)=cx^{-c-1}(1-B(x))+x^{-c}B'(x)>0.
\]
Since \(F_T\) is continuous at \(1\) with \(F_T(1)=0\), it is strictly increasing throughout \([1,\infty)\), a stronger family-specific conclusion than monotonicity only beyond \(N-1\).

## Verification
The accompanying standalone Python 3 standard-library file `verify.py` independently constructs the directed graphs, tests each colouring for directed cycles by a topological-sort algorithm on the same-colour arcs, and compares the exact count with the polynomial. It exhaustively checks 180 graph/palette cases (1,161,788 labelled assignments). It independently implements integer polynomial arithmetic, cyclotomic division, and Möbius inversion to verify 195 finite parameter configurations, together with strict rational sign brackets. Successful output ends `VERIFY_OK`. These finite checks corroborate, but are not substituted for, the preceding all-parameter proof.

## Relationship to prior work
Crew, Keller, Kuehr, Lin, Monroy Rodríguez, and Williams (2026, arXiv:2611.13273v1) develop the dichromatic polynomial, general inclusion–exclusion and root-density results, answer tournament dichromatic-uniqueness questions, and pose a monotonicity conjecture. Their general counting formula implies the first identity after specializing to our cycle family but does not state the cyclotomic inverse reconstruction, complete within-family isomorphism census, parity-specific root count, or family-specific strict monotonicity. Earlier work by González-Moreno, Hernández-Ortiz, Llano, and Olsen (2022) supplies general recurrences and studies dichromatic equivalence, not an identified covering classification of these networks. The latter paper's complete publisher text was inaccessible for full-text comparison; its abstract and accessible preview were examined, so the priority assessment is provisional. Related published work on *acyclic orientations of undirected multi-theta graphs* concerns a different invariant and does not imply any of these oriented-digraph coloring statements.

## Limitations
The digraph construction requires at least two distinct forward paths and each of them to have at least one internal vertex. The reconstruction claim is restricted to this class and must not be interpreted as global dichromatic uniqueness. The theorem establishes exactly the roots in \((0,1)\), not a complete description of all complex or real zeros. It verifies the monotonicity conjecture only on this infinite family, not for arbitrary digraphs. Searches do not establish historical priority conclusively, particularly without full access to the 2022 paper. The finite verification range does not itself prove the infinite statements.

## References
1. L. Crew, B. Keller, K. Kuehr, S. Y. Lin, M. I. Monroy Rodríguez, T. Williams, *Properties of the Dichromatic Polynomial*, arXiv:2611.13273v1 (first posted 2026-11-09), https://arxiv.org/html/2611.13273v1.
2. D. González-Moreno, R. Hernández-Ortiz, B. Llano, M. Olsen, *The Dichromatic Polynomial of a Digraph*, Graphs and Combinatorics 38, article 85 (2022), https://doi.org/10.1007/s00373-022-02484-0.
3. W. Hochstättler, J. Wiehe, *The Chromatic Polynomial of a Digraph*, arXiv:1911.09547 (2019), https://arxiv.org/abs/1911.09547.
