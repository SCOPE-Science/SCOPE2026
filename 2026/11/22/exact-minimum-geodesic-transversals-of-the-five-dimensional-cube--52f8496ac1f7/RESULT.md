# Exact minimum geodesic transversals of the five-dimensional cube

## Finding

Let \(Q_5\) be the graph with vertex set \(\{0,1\}^5\), with two vertices adjacent when they differ in one coordinate. A **geodesic transversal** intersects every inclusion-maximal shortest path. Then

\[
\operatorname{gt}(Q_5)=10.
\]

Moreover, the **complete family** of minimum geodesic transversals consists of exactly 32 distinct sets

\[
S_a=\{v\in\{0,1\}^5:d_H(v,a)=2\},\qquad a\in\{0,1\}^5.
\]

Each set \(S_a\) has ten vertices. Thus the minimum transversals form a single translation orbit; there are no exceptional configurations.

## Assumptions and scope

All graphs are finite, undirected and simple. Shortest paths are considered up to reversal, and their *vertex sets* suffice for transversal tests. The statement concerns **only** dimension five; no assertion is made for higher-dimensional cubes. Throughout, \(d_H\) denotes Hamming distance. A geodesic is maximal when it is not a proper subpath of another geodesic.

## Proof

**Step 1: characterization of maximal geodesics.** In a hypercube a shortest path changes each coordinate at most once. If fewer than five coordinates are changed, an unused coordinate can be flipped at the endpoint, extending the path to a longer shortest path. Hence the maximal geodesics are precisely the paths between antipodal vertices, obtained by flipping all five coordinates in some order. There are \(32\cdot5!/2=1920\) such undirected paths; all have six distinct vertices.

**Step 2: ten-vertex construction.** The weight-two layer \(S_0\) has \(\binom52=10\) vertices. Along any antipodal geodesic the Hamming weight starts at some integer \(r\), ends at \(5-r\), and changes by one at each step. Consequently the path reaches weight two. Therefore \(S_0\) is a transversal. XOR translation by any \(a\) is a graph automorphism, so every \(S_a\) is also a transversal of size ten.

**Step 3: exhaustive nine-vertex lower certificate.** The standalone `verify.cpp` computes the set of vertex masks of **all** maximal geodesics from the 32 starting vertices and the 120 coordinate-flip orders; it verifies that 1920 distinct six-vertex masks occur. Since XOR translation preserves all maximal geodesics, any nonempty transversal can be translated to contain vertex zero. The checker enumerates, without repetition, every set containing zero and eight other vertices: exactly

\[
\binom{31}{8}=7{,}888{,}725
\]

candidates. It tests their intersection against every maximal-geodesic mask not containing zero (1560 masks). None passes. A transversal with fewer than nine vertices would extend to one of size nine, so every transversal has at least ten vertices. This is a finite exhaustive proof, not an inference from sampled configurations.

**Step 4: complete classification.** The same exact checker enumerates every ten-vertex set containing zero, exactly

\[
\binom{31}{9}=20{,}160{,}075
\]

candidates. Precisely ten of them intersect every geodesic, and the program explicitly compares each against the ten predicted sets \(S_a\) with \(d_H(a,0)=2\). Conversely all 32 sets \(S_a\) are independently verified to hit all geodesics and be mutually distinct. Any minimum transversal can be translated to contain zero, and the exhaustive list proves it is a translate of one of those ten spheres, hence belongs to the claimed family. This completes the classification.

## Verification

Compile with a conforming C++17 compiler:

```sh
c++ -O2 -std=c++17 -Wall -Wextra -pedantic verify.cpp -o verify
./verify
```

Expected output:

```text
MAXIMAL_GEODESIC_SETS 1920 PASS
SHELL_CONSTRUCTIONS 32 DISTINCT ALL_HIT PASS
NORMALIZED_SIZE_9 tested=7888725 valid=0 PASS
NORMALIZED_SIZE_10 tested=20160075 valid=10 PASS
CLASSIFICATION_ALL_32_MINIMA_PASS
GT_Q5_10_PASS
```

The algorithm constructs paths directly from coordinate-flip permutations, represents each vertex subset by an exact 32-bit unsigned mask, and enumerates the appropriate combinations lexicographically. No floating-point optimization, random sampling, external solver, precomputed table or trusted binary is required.

## Relationship to prior work

Chen, Ma and Wu [1, Theorem 3.1] proved the general bounds

\[
\left\lceil\frac{2^n}{\lceil n/2\rceil+1}\right\rceil\le\operatorname{gt}(Q_n)\le\binom{n}{\lfloor n/2\rfloor},
\]

which give only \(8\le\operatorname{gt}(Q_5)\le10\). Their Remark 3.4 determines the values through dimension four. The present result proves the upper endpoint sharp in dimension five and classifies all minimizers. The previously recorded classification of forty minimum transversals for the four-cube [3] concerns a distinct dimension and does not imply this result.

Prabha, Sandhiya and Manuel [2, Theorem 10] state the incompatible general formula \(\operatorname{gt}(Q_n)=2^{n-1}\) for \(n>1\). At dimension five that formula yields 16, contradicting the already published upper bound of ten in [1]; the finite certificate above independently establishes the exact value. The conflicting formula is therefore not treated as valid covering prior art.

## Limitations

The lower bound and classification require an exhaustive finite computation, supplied in full as C++17 source, rather than a concise computer-free argument. No statement is made about the optimum or minimum-set structure in any other dimension. Historical originality remains subject to independently located literature not indexed in the sources searched. The computation has not received an independent external audit.

## References

1. S. Chen, X. Ma, T. Wu, *On two problems concerning the geodesic transversal number of graphs*, arXiv:2610.39298v1, 29 October 2026, Sections 2–3, Theorem 3.1 and Remark 3.4. https://arxiv.org/abs/2610.39298
2. R. Prabha, B. Sandhiya, P. Manuel, *Geodesic Transversal of Hypercube and Butterfly networks*, arXiv:2611.06107v1, 4 November 2026, Section 5, Theorem 10. https://arxiv.org/abs/2611.06107
3. *Forty minimum geodesic transversals of the four-dimensional cube*, 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-forty-minimum-geodesic-transversals-of-the-four-dimensional-cube--e937d60d04fd (indexed summary consulted; full underlying text not inspected).
