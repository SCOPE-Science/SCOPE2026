# A sharp 54-site gap and a renewal zeta for temporal five-cycles of Rule 22

## Finding

Let \(F_n\) be synchronous elementary cellular automaton Rule 22 on the labelled cyclic binary ring of length \(n\ge3\). Let \(C_5(n)\) count primitive *temporal* five-cycle orbits, with neither rotations nor reflections of the ring identified. Then

\[
\boxed{\sum_{n\ge1}C_5(n)z^n=\frac{11z^{11}+12z^{12}+13z^{13}}{1-z^{11}-z^{12}-z^{13}}.}
\]

In particular, \(C_5(n)>0\) exactly when \(n\) belongs to the additive semigroup \(\langle11,12,13\rangle\). This is the union of intervals \([11k,13k]\cap\mathbb Z\) for integers \(k\ge1\). Thus **54 is the largest circumference without a primitive temporal five-cycle**, and every circumference \(n\ge55\) admits one. The first three counts are \(C_5(11)=11\), \(C_5(12)=12\), \(C_5(13)=13\). Additional values are \(C_5(22)=11\), \(C_5(23)=23\), \(C_5(24)=36\), \(C_5(53)=C_5(54)=0\), and \(C_5(55)=11\).

The number of such orbits grows exponentially, with growth constant \(\lambda=1.09612898958\ldots\), the unique real \(\lambda>1\) solving \(\lambda^{13}=\lambda^2+\lambda+1\). No assertion is made about other temporal periods or their attraction basins.

## Assumptions and scope

A ring state is \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\) with \(x_i\in\{0,1\}\). The Rule 22 update is

\[
(F_n(x))_i=1\quad\Longleftrightarrow\quad x_{i-1}+x_i+x_{i+1}=1,
\]

where the sum on the right is ordinary integer addition. A configuration has primitive temporal period five if \(F_n^5(x)=x\) and \(F_n(x)\ne x\). Since five is prime, these two conditions characterize exactly the points of least period five. The orbit count divides the number of such configurations by five. Cells and spatial orientations remain labelled.

## Proof

**1. A finite space-time graph.** For a positive temporal height \(t\), let a column \(a=(a_0,\ldots,a_{t-1})\in\{0,1\}^{t}\) record the values of one site over a cyclic temporal history, with subscripts interpreted modulo \(t\). Define a directed graph \(G_t\) on the \(2^{2t}\) vertices \((a,b)\), putting an edge from \((a,b)\) to \((b,c)\) exactly when for every \(j\in\mathbb Z/t\mathbb Z\),

\[
b_{j+1}=\mathbf1_{\{a_j+b_j+c_j=1\}}.
\]

A labelled spatial ring configuration fixed by \(F_n^t\) determines a unique closed directed walk of length \(n\) in \(G_t\), with its starting vertex anchored at spatial index zero; conversely the overlapping columns of any such closed walk determine that complete space-time history. Therefore

\[
\#\operatorname{Fix}(F_n^t)=\operatorname{tr}(A_t^n),
\]

where \(A_t\) is the adjacency matrix of \(G_t\). Every closed walk lies in a strongly connected component containing a directed cycle.

**2. The complete finite component certificate.** For \(t=1\), the recurrent components are one isolated loop and one directed two-cycle; hence

\[
\#\operatorname{Fix}(F_n)=1+2\mathbf1_{2\mid n}.
\]

For \(t=5\), the graph has 1,024 vertices and 1,023 directed edges. Its full recurrent decomposition consists of one isolated loop, one directed two-cycle, and exactly five other strongly connected components. Each of these five components has 16 vertices, 18 edges and precisely three simple directed cycles, of lengths 11, 12 and 13. All three simple cycles share vertices; in fact their common intersection contains nine vertices. This entire finite claim is certified by the standalone program `verify_transfer.py`, which builds every edge from the displayed local rule, finds every strongly connected component, exhaustively enumerates simple cycles within each recurrent component and verifies their intersections. There are no additional recurrent components.

For any finite directed graph whose only simple cycles are three cycles that share a common vertex, the determinant expansion for \(\det(I-zB)\) has no nontrivial products of vertex-disjoint cycles. Thus, when the lengths are 11, 12, 13,

\[
\det(I-zB)=Q(z):=1-z^{11}-z^{12}-z^{13}.
\]

This identity applies separately to each of the five 16-vertex components. The closed-walk generating function for such a component is the standard formal identity

\[
\sum_{n\ge1}\operatorname{tr}(B^n)z^n=-\frac{zQ'(z)}{Q(z)}
=\frac{11z^{11}+12z^{12}+13z^{13}}{Q(z)}.
\]

**3. Exact temporal period.** The length-one and length-two components contribute \(1+2\mathbf1_{2\mid n}\) to the fifth-return trace, exactly as they do to the first-return trace. The five large components contribute five copies of \(\operatorname{tr}(B^n)\). Hence

\[
\#\operatorname{Fix}(F_n^5)-\#\operatorname{Fix}(F_n)=5\operatorname{tr}(B^n).
\]

Dividing by five proves the displayed generating function for primitive temporal five-orbits, with no spatial quotient.

**4. Sharp circumference cutoff.** Since \(Q(z)^{-1}=\sum_{k\ge0}(z^{11}+z^{12}+z^{13})^k\) has nonnegative coefficients, the generating function has a positive coefficient at \(z^n\) precisely when \(n\) is a nonempty sum of 11s, 12s and 13s. Exactly \(k\) summands attain every integer between \(11k\) and \(13k\), inclusive. The first five intervals are \([11,13]\), \([22,26]\), \([33,39]\), \([44,52]\), and \([55,65]\). For every \(k\ge5\), the interval \([11(k+1),13(k+1)]\) starts no later than the integer immediately following \(13k\), so all integers at least 55 occur. The numbers 53 and 54 occur in none of these intervals, proving sharpness. The positive Perron root of \(u^{13}-u^2-u-1\) gives the stated exponential growth rate by the standard aperiodic renewal expansion: the lengths 11, 12 and 13 have greatest common divisor one.

## Verification

The reproducible finite certificate is `verify_transfer.py`, a dependency-free Python 3 program. It establishes the 1,024-vertex transfer graph, the exact full list of recurrent component sizes and edges, and the complete simple-cycle lengths and common-vertex condition. It also independently checks the trace formula for all ring sizes up to 70 using explicit closed-walk propagation, without assuming the stated recurrence during those computations. The observed output is embedded as `transfer_output.txt`.

The independently implemented `verify_direct.cpp` builds Rule 22 directly on bit-packed cyclic configurations and exhaustively tests all \(2^n\) labelled configurations at every \(3\le n\le22\) for first and fifth return. It verifies the formula for every tested circumference; its output is `direct_output.txt`. These finite tests corroborate the result, while the complete transfer graph and determinant proof provide the all-circumference argument. Neither a random simulation nor a finite list of tested circumferences alone would establish it.

## Relationship to prior work

Wolfram's 2002 presentation of elementary cellular automata provides the archival Rule 22 setting. Martínez, Adamatzky, Hoffmann, Deserable and Zelinka's *On patterns and dynamics of Rule 22 cellular automaton* (published 2019, openly available as arXiv:2005.01480) studies finite-ring attractors and extended de Bruijn diagrams; its explicit examples include temporal period five at ring lengths 11, 12 and 13. Those examples are **not** claimed to be new. Its main analysis includes a broad survey of cycles up to 20 sites and a partial sampling of larger rings, rather than the present all-circumference exact period-five count and conductor 55. The transfer-graph method is established; the identified three-loop fifth-return structure and its exact counting consequences are the proposed contribution.

The exact temporal-four orbit census for the same automaton, when available, concerns a different return map and does not imply the fifth-return numerator, denominator or arithmetic existence classification. The two mathematical results are not presented as a single claimed general temporal-period theorem.

## Limitations

This theorem covers primitive temporal period five only, on finite labelled binary cyclic rings of circumference at least three, with simultaneous updates. It neither classifies all temporal periods nor determines transient basins. Earlier work already provides examples of the smallest length-eleven cycles, so novelty is confined to the exact all-length formula, sharp set of permitted circumferences, and growth law. Relevant older cycle atlases and some historical records may be incompletely indexed; independent historical-priority review is warranted.

## References

1. S. Wolfram, *A New Kind of Science*, Wolfram Media (first published 14 May 2002), https://www.wolframscience.com/nks/ and https://www.wolfram-media.com/products/nks/ .
2. G. J. Martínez, A. Adamatzky, R. Hoffmann, D. Deserable, and I. Zelinka, *On patterns and dynamics of Rule 22 cellular automaton*, *Complex Systems* 28(2) (2019), 125–174; publicly accessible manuscript https://arxiv.org/abs/2005.01480 (posted 4 May 2020).
3. AMS, *Mathematics Subject Classification 2020*, section 37B15, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=37B52 .
