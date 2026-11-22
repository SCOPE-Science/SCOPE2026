# Zero-free signed perfect-matchings and sharp inverse Walsh norms for the Desargues graph

## Finding

Let \(G\) be the Desargues graph, with 20 vertices and 30 edges, described equivalently as the generalized Petersen graph \(\operatorname{GP}(10,3)\) or the bipartite Kneser graph \(H(5,2)\). Let \(\mathcal M\) be its 60 perfect matchings, and write \(m\in\mathbb F_2^{E(G)}\) for the indicator of a matching. Define the unnormalized operator
\[
(Tf)(x)=\sum_{m\in\mathcal M}f(x+m),\quad x\in\mathbb F_2^{E(G)}.
\]
Its binary Fourier multipliers are \(W(s)=\sum_{m\in\mathcal M}(-1)^{s\cdot m}\).

**Theorem.** Every signing \(s\) satisfies \(W(s)\equiv4\pmod8\). Thus \(T\) is invertible on the full \(2^{30}\)-dimensional space. Its exact absolute Walsh spectrum, after reducing by the \(2^{19}\) vertex-switching symmetries, is

| \(|W|\) | Number of reduced frequencies |
|---:|---:|
| 4 | 1551 |
| 12 | 406 |
| 20 | 90 |
| 60 | 1 |

Each multiplicity is to be multiplied by \(2^{19}\) in the full Fourier space. Both signs of each magnitude occur equally often across all full frequencies. Hence
\[
\|T^{-1}\|_{\ell^2\to\ell^2}=\frac14,\qquad \kappa_2(T)=15.
\]
The unique inverse is convolution with a function supported on the affine set of all edge subsets having odd degree at all 20 vertices, of cardinality \(2^{11}\). Exactly 1343 entries of its kernel are nonzero. Its endpoint norms are exactly
\[
\boxed{\|T^{-1}\|_{\ell^1\to\ell^1}
=\|T^{-1}\|_{\ell^\infty\to\ell^\infty}=\frac{68}{15}.}
\]

## Assumptions and scope

The group is the binary edge cube \(V=\mathbb F_2^{30}\), with counting measure and unnormalized convolution. The edge set of \(\operatorname{GP}(10,3)\) has outer cycle edges \(\{i,i+1\}\), inner edges \(\{10+i,10+i+3\}\), and spokes \(\{i,10+i\}\), with all indices \(i\) read modulo ten. All matchings are unordered sets of ten pairwise vertex-disjoint edges covering all vertices. No random-signing assumption is made: the congruence holds for all \(2^{30}\) edge signings. The inverse norm is that of the unique inverse operator, not a projection onto a proper Fourier range.

## Proof

**Exact finite edge and pair counts.** Exhaustive enumeration of perfect matchings, by recursively choosing the least unmatched vertex and branching over its incident edges, produces 60 distinct matchings. This is an exhaustive combinatorial algorithm: every perfect matching has exactly one branch for the chosen vertex and is generated once, by induction on the remaining unmatched vertices. For each edge, exactly 20 perfect matchings contain it. Among the 375 pairs of nonincident edges, the numbers of perfect matchings extending the pair are respectively 4, 6, 8, or 10, with pair frequencies 75, 120, 60, and 120; incident edge pairs occur in none. These are finite statements certified using two independent representations and enumerations in `verify.py`.

**Uniform nonvanishing.** For a signing \(s\) and its set \(S\) of negative edges, expand
\[
W(s)=\sum_{M\in\mathcal M}\prod_{e\in M}(1-2\mathbf 1_{e\in S}).
\]
Modulo eight only the first three terms remain:
\[
W(s)\equiv60-2\sum_{e\in S}20
 +4\sum_{\{e,f\}\subseteq S}N_{ef}\equiv 4\pmod8,
\]
since every pair-extension count \(N_{ef}\) is even. Thus no signed sum vanishes. The magnitude values below additionally show the modulus four is sharp.

**Switching reduction and spectrum.** Each perfect matching meets every vertex once, so negating all edges incident to one vertex negates \(W\). Vertex switchings form a 19-dimensional binary cut space \(C\) because \(G\) is connected. There are 11 remaining dimensions, represented by the non-tree edges of any spanning tree. For every signing, its vertex-switching orbit has a representative supported on these 11 chords. A direct exact-integer 2048-point Walsh–Hadamard transform of the histogram of the 60 matching restrictions to the chords gives the four-row spectrum in the theorem. A separate signed-permanent enumeration in the \(H(5,2)\) representation gives the same absolute histogram, and all 2048 individual signed sums equal the corresponding direct signed-permanent evaluations. The maximum magnitude is 60 at the unflipped signing and the minimum is 4; therefore the Hilbert claims follow from diagonalization.

**Exact endpoint inverse.** For every cut \(c\in C\), the character of any perfect matching on \(c\) equals \((-1)^{|U|}\), where \(c\) is the edge cut induced by a vertex subset \(U\). Consequently \(1/W(s+c)\) transforms by the same parity character. Fourier inversion forces the inverse convolution kernel to vanish unless its edge-indicator has odd degree at every vertex. Such indicators form an affine translate of the 11-dimensional cycle space, with one representative for each chord pattern. If \(W_q\) is the 2048-point switching-quotient multiplier vector and \(H\) denotes the unnormalized binary Walsh matrix, the inverse kernel on its allowed chord patterns is exactly
\[
k_x=\frac1{2048}\sum_{q\in\mathbb F_2^{11}}\frac{(-1)^{q\cdot x}}{W_q}
=\frac{(H(60/W))_x}{60\cdot2048}.
\]
Each \(W_q\) is one of \(\pm4,\pm12,\pm20,\pm60\), so \(60/W_q\) is integral. The exact integer transform has
\[
\sum_x |(H(60/W))_x|=557056,
\]
with 1343 nonzero entries. Hence \(\|k\|_1=557056/(60\cdot2048)=68/15\). As convolution by \(k\) has both \(\ell^1\)- and \(\ell^\infty\)-operator norm \(\|k\|_1\), and since the inverse is unique, both stated constants are sharp.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. It generates \(\operatorname{GP}(10,3)\) and \(H(5,2)\) independently; enumerates all perfect matchings; checks the first and second incidence moments; checks the full 2048-signing spectrum with exact integer Walsh transforms and direct sums; and computes the reciprocal transform as an exact rational. Output ends in `PASS`, reporting 60 matchings, the four magnitude multiplicities, minimum multiplier 4, inverse endpoint constant 68/15, and 1343 nonzero inverse-kernel coefficients. The 2048-point quotient is exhaustive by switching reduction, not a numerical sample of the larger cube.

## Relationship to prior work

The Desargues graph and its representation as \(H(5,2)\cong\operatorname{GP}(10,3)\) are classical; van Gans surveys its graph-theoretic structure, while Hong and Ismailescu give an archival public preprint on Euclidean embeddings. Wanless studies unrestricted all-\(\pm1\) matrix permanents and gives different existence results about zero permanents; the present family is a fixed sparse 10-by-10 support with signs assigned only on its 30 allowed entries. The earlier counted 60 Desargues matchings and their anti-forcing/reconfiguration properties are distinct from the complete signed-permanent spectrum and exact convolution inverse. Standard Fourier diagonalization and switching are tools used in the proof, not claimed new principles.

## Limitations

This is an exact result for one natural fixed graph, not a theorem for every generalized Petersen graph or all cubic bipartite supports. The 60-matching count and even pair extensions are certified by small exhaustive code rather than a separate conceptual counting formula. A historical equivalent in unindexed signed-graph or permanent literature cannot be ruled out by a bounded search. No independent mathematical audit has been performed.

## References

1. J. H. Hong and D. Ismailescu, *On the Euclidean dimension of graphs*, arXiv:1501.00204v1, first publicly submitted 2014-12-31, https://arxiv.org/abs/1501.00204v1 (Desargues graph realization, not this operator).
2. M. van Gans, *Topics in Trivalent Graphs*, PhD thesis, 2007, https://etheses.bham.ac.uk/id/eprint/103/ (Desargues graph structure and the bipartite Kneser description).
3. I. M. Wanless, *Permanents of matrices of signed ones*, Linear and Multilinear Algebra 53 (2005), 427–433, https://users.monash.edu.au/~iwanless/papers/wangconjLAMA.pdf (full text inspected; dense sign matrices).
4. *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html (graph equivalences).
