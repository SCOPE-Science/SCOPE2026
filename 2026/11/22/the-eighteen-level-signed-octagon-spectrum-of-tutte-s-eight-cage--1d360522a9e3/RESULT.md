# The eighteen-level signed octagon spectrum of Tutte's eight-cage

## Finding

Let \(G\) be the Tutte–Coxeter graph (the duad–syntheme incidence graph of the Cremona–Richmond configuration), with 30 vertices and 45 edges. Let \(\mathcal O\) be its 90 unoriented simple cycles of length eight. Regard each cycle as its binary edge-incidence vector \(c\in\mathbb F_2^{45}\), and let \(T\) denote **unnormalized XOR convolution** on functions on \(\mathbb F_2^{45}\) by the indicator of \(\mathcal O\):

\[
(Tf)(x)=\sum_{c\in\mathcal O} f(x+c),\qquad
\Lambda(\sigma)=\sum_{c\in\mathcal O}(-1)^{\langle\sigma,c\rangle}.
\]

The **entire signed spectrum** consists of the eighteen values in the following table. Each multiplicity shown is the number of sign classes modulo vertex switching; the multiplicity in the full 45-coordinate Fourier space is the displayed number multiplied by \(2^{29}\).

| \(\Lambda\) | Quotient multiplicity | \(\Lambda\) | Quotient multiplicity |
|---:|---:|---:|---:|
| \(-30\) | 36 | \(2\) | 10,440 |
| \(-22\) | 450 | \(6\) | 8,520 |
| \(-18\) | 1,080 | \(10\) | 5,634 |
| \(-14\) | 2,520 | \(14\) | 1,440 |
| \(-10\) | 8,280 | \(18\) | 1,740 |
| \(-6\) | 11,580 | \(22\) | 1,440 |
| \(-2\) | 11,520 | \(30\) | 360 |
|  |  | \(34\) | 360 |
|  |  | \(42\) | 90 |
|  |  | \(58\) | 45 |
|  |  | \(90\) | 1 |

In particular, every multiplier is congruent to \(2\) modulo \(4\), so none vanish. The exact smallest multiplier magnitude is \(2\), the largest is \(90\), the unnormalized convolution condition number on \(\ell^2\) is \(45\), and its sharp inverse norm is \(\|T^{-1}\|_{\ell^2\to\ell^2}=1/2\). No endpoint projection is needed because the range is all functions.

## Assumptions and scope

The graph is the finite, simple, undirected bipartite incidence graph constructed from the fifteen two-element subsets (duads) of \(\{0,1,2,3,4,5\}\) and the fifteen perfect matchings of that six-point set (synthemes). Incidence means set membership. Every unoriented simple eight-cycle is counted once, not eight or sixteen times. Coordinate arithmetic is modulo two, character signs are real \(\pm1\), and convolution uses counting rather than probability normalization. The theorem covers this graph only and makes no assertion about other cages or generalized quadrangles.

## Proof

**Octagon enumeration and parity.** An octagon alternates between four distinct duads and four distinct synthemes, each adjacent pair of duads being contained in its unique common syntheme. This gives a finite, exact four-duad enumeration, independent of the graph's simple-path enumeration. Both produce precisely 90 edge-incidence vectors, and each of the 45 edges lies in precisely sixteen of these cycles. Thus, in \(\mathbb F_2^{45}\),

\[
\sum_{c\in\mathcal O}c=0.
\]

For any edge frequency \(\sigma\), put \(k(\sigma)=|\{c\in\mathcal O:\langle\sigma,c\rangle=1\}|\). Summing the parity of the 90 character exponents shows \(k(\sigma)\) is even. Therefore

\[
\Lambda(\sigma)=90-2k(\sigma)\equiv 2\pmod4,
\]

so all \(2^{45}\) Fourier eigenvalues are nonzero. This nonvanishing conclusion is a proof from edge incidences, not a numerical inference.

**Reduction from 45 to 16 signs.** Vertex switching adds a cut vector to \(\sigma\) and does not change any character evaluated on a cycle. Since the graph is connected, its binary cut space has dimension \(30-1=29\). A fixed spanning tree contains 29 edges and has 16 cotree edges. Switching uniquely sets the tree-edge signs to positive, leaving one independent sign on each cotree edge. Hence the full spectrum is obtained by enumerating \(2^{16}=65,536\) cotree assignments, each occurring \(2^{29}\) times in the full dual group. The corresponding 90 projected cycle vectors have rank 16.

**Exact signed histogram.** The standalone file `verify_octagons.py` builds the duads, synthemes and incidence edges from their definitions, enumerates octagons twice, produces a deterministic breadth-first spanning tree, and projects each octagon to its sixteen cotree coordinates. It then (a) computes the complete sixteen-dimensional integer Walsh–Hadamard transform and (b) independently evaluates each of the 65,536 signed sums directly. The methods agree on every coefficient, and the resulting frequencies are precisely those in the displayed eighteen-level table. The values and multiplicities are finite exhaustive identities established by the included exact code; there is no claim of a separate symbolic closed form for the histogram.

A cotree sign mask \(85\), equivalently cotree bit positions \(0,2,4,6\) in the deterministically generated order, gives signed sum \(-2\), proving that the nonzero lower bound from the congruence is sharp. The trivial character gives \(90\). Fourier diagonalization of convolution, with either counting or normalized \(\ell^2\) inner product, proves the exact inverse norm and condition number.

## Verification

Run `python3 verify_octagons.py` (Python 3.10 or later, standard library only). The program tests 30 vertices, 45 edges, girth eight, both independent octagon enumerations, 90 cycles, sixteen occurrences per edge, sixteen-dimensional cycle span, each of the 18 signed histogram multiplicities, the modulo-four congruence, 65,536 direct-vs-transform signed sum comparisons, Parseval, character summation and the explicit minimum witness. It terminates with `PASS` only if all tests succeed. All arithmetic is exact integer arithmetic; no tolerance or random sampling is used.

The complete histogram requires an exhaustive finite computation; the parity nonvanishing theorem itself does not. No conclusion about other graph orders or infinite families follows from the computation.

## Relationship to prior work

The Tutte–Coxeter graph, its duad–syntheme description, its girth-eight and edge-transitivity properties, and the count of 90 octagons are established background, not new claims. Baez's detailed 2015 account gives the 90-count and a quadrangle interpretation. Farrokhi and Mohammadian's 2016 work describes the octagon families in generalized Tutte–Coxeter graphs and proves symmetry characterizations. MathWorld records the ordinary 30-vertex **adjacency** spectrum of this graph. None of those results supplies the present signed 45-edge Boolean-convolution spectrum: the ordinary adjacency operator and the convolution operator have different domains, and unsigned cycle counts do not imply 18 signed multiplicities.

## Limitations

The calculation is for exactly one finite graph; there is no extension to other cages. The signed histogram is an exhaustive computational theorem with an independently cross-checked program, whereas the modulo-four obstruction has a short conceptual proof. An unindexed earlier equivalent signed-octagon enumerator or coding-theory calculation remains possible; no historical-priority guarantee is asserted. This work has not undergone independent mathematical audit.

## References

1. John C. Baez, "Tutte–Coxeter Graph," *Visual Insight*, American Mathematical Society, 15 August 2015. https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/
2. John C. Baez, "Some Thoughts on the Number 6," 2 September 2015, especially the answers to puzzles 11–13 on the 90 octagons. https://math.ucr.edu/home/baez/six.html
3. M. Farrokhi Derakhshandeh Ghouchan and A. Mohammadian, "A characterization of Tutte-Coxeter graph," publicly posted 10 November 2016, arXiv:1611.03241. https://arxiv.org/abs/1611.03241
4. E. W. Weisstein, "Tutte 8-Cage," MathWorld. https://mathworld.wolfram.com/Tutte8-Cage.html
