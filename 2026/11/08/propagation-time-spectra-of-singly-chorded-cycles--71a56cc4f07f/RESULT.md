# Propagation-time spectra of singly chorded cycles

## Finding
For every integer \(n\ge4\), fix a cycle on vertices \(0,1,\ldots,n-1\) in cyclic order, and add one chord \(\{0,a\}\), where \(2\le a\le n-2\). Set \(b=n-a\); the two original-cycle arcs joining the chord endpoints have lengths \(a\) and \(b\). Denote this graph by \(G_{a,b}\).

Under the standard simultaneous zero-forcing rule, the minimum forcing sets are exactly the \(n\) pairs of consecutive vertices on the original cycle. Index the \(a\) pairs on the first arc by \(i=0,\ldots,a-1\), corresponding to \(\{i,i+1\}\), and the \(b\) pairs on the second arc by \(j=0,\ldots,b-1\), corresponding to \(\{a+j,a+j+1\}\), with vertex labels reduced modulo \(n\). Their exact propagation times are
\[
 t_a(i)=\max\{i,a-1-i\}+\lfloor b/2\rfloor,
 \qquad t_b(j)=\max\{j,b-1-j\}+\lfloor a/2\rfloor.
\]
Consequently the propagation-time enumerator over all **minimum-cardinality** forcing sets is
\[
 H_{a,b}(z)=z^{\lfloor b/2\rfloor}B_a(z)
       +z^{\lfloor a/2\rfloor}B_b(z),
\]
where, for every integer \(m\ge1\),
\[
 B_{2m}(z)=2\sum_{r=m}^{2m-1}z^r,
 \qquad B_{2m+1}(z)=z^m+2\sum_{r=m+1}^{2m}z^r.
\]
In particular, the minimum and maximum propagation times are
\[
 \operatorname{pt}_{\min}(G_{a,b})=\lfloor a/2\rfloor+\lfloor b/2\rfloor,
\]
\[
 \operatorname{pt}_{\max}(G_{a,b})=
 \max\bigl\{a-1+\lfloor b/2\rfloor,\ b-1+\lfloor a/2\rfloor\bigr\}.
\]
Every integer between these extremes is realized by a minimum forcing set. The number of minimum forcing sets attaining the minimum propagation time is exactly
\[
 E(a,b)=2+\mathbf 1_{2\mid a}+\mathbf 1_{2\mid b}.
\]
Compared with the unchorded cycle, whose minimum propagation time is \(\lceil(n-2)/2\rceil\), the chord raises the minimum propagation time by exactly one when both \(a\) and \(b\) are even, and otherwise leaves it unchanged. In contrast, it reduces the number of efficient pairs from \(n\) to only \(2\), \(3\), or \(4\) depending on parity.

## Assumptions and scope
Graphs are finite, simple and undirected; only a **single non-cycle chord** is added. Both arc lengths are at least two. Starting from a set \(S\) of blue vertices, at each integer round, every blue vertex having precisely one white neighbor forces that neighbor blue. All forces available from the coloring at the start of a round happen simultaneously. A minimum zero-forcing set is one with the smallest possible number of initially blue vertices; here it has cardinality two. The propagation-time enumerator counts distinct unordered vertex pairs, **not** forcing schedules or larger minimal forcing sets. The auxiliary polynomial variable \(z\) is formal.

## Proof
**Step 1: Determine the minimum forcing sets.** Initially a singleton cannot force, since every vertex has degree at least two. A nonconsecutive pair on the original cycle also cannot force: each blue vertex has both of its cycle neighbors white, whether or not it is incident with the extra chord. Conversely, every consecutive original-cycle pair forces all vertices by the explicit propagation described next. Thus the zero-forcing number is two and its minimum sets are precisely the \(n\) original-cycle edges. This classification was already established in the zero-forcing-polynomial literature and is included here to fix the precise scope.

**Step 2: Analyze one arc.** Choose the pair at positions \(i,i+1\) on the length-\(a\) arc between the chord endpoints. Propagation along that arc starts in the two outward directions. The endpoint at position zero becomes blue after exactly \(i\) rounds; the endpoint at position \(a\) becomes blue after exactly \(a-1-i\) rounds. If either chord endpoint becomes blue earlier, it cannot force into the other arc: while the other endpoint is white, the earlier endpoint still has two white neighbors (the chord neighbor and its first neighbor on the other arc). It also has no white neighbor on the already-advanced direction of the first arc. Therefore the second arc remains wholly white until both chord endpoints are blue. This occurs precisely at
\[
T=\max\{i,a-1-i\}.
\]
By this time every vertex of the first arc is blue. In the next round each chord endpoint can force the neighboring vertex of the length-\(b\) arc; subsequent rounds advance two fronts toward one another. Its \(b-1\) internal vertices therefore become blue in exactly \(\lceil(b-1)/2\rceil=\lfloor b/2\rfloor\) additional rounds. This establishes \(t_a(i)\), including the smallest case \(b=2\), where both endpoints can force the same internal vertex. Interchanging the two arcs proves \(t_b(j)\).

**Step 3: Enumerate the times.** For integer \(\ell\ge2\), the list \(\max\{i,\ell-1-i\}\), as \(i\) runs from zero to \(\ell-1\), has values and multiplicities encoded by \(B_\ell(z)\) above: if \(\ell=2m\) each value from \(m\) to \(2m-1\) occurs twice; if \(\ell=2m+1\), the value \(m\) occurs once and each value from \(m+1\) to \(2m\) occurs twice. Shifting these lists by the second-arc completion times proves the enumerator.

**Step 4: Consequences.** Both shifted lists have the same minimum \(\lfloor a/2\rfloor+\lfloor b/2\rfloor\), and each takes every integer up to its own maximum. Their union is therefore a gapless interval, with the maximum stated above. At the common minimum, the first list has two attaining pairs if \(a\) is even and one if \(a\) is odd, and similarly for the second list. This proves the formula for \(E(a,b)\). Finally, direct parity evaluation of \(\lfloor a/2\rfloor+\lfloor b/2\rfloor-\lceil(a+b-2)/2\rceil\) gives one for two even arc lengths and zero otherwise.

## Verification
Two distinct executable implementations are included in `verification/check_python.py` and `verification/check_cpp.cpp`. Both construct each chorded cycle from its graph edges and simulate synchronous zero forcing without using the theorem as a transition rule. The Python program checks every chord placement and every original-cycle pair for \(4\le n\le50\), and independently tests all nonconsecutive two-sets for \(n\le12\). The C++ program uses bit masks and tests every two-element starting set for every chord placement with \(4\le n\le22\), including the gapless spectrum, efficient-set counts, and cycle comparison. Every assertion passed on the saved standalone sources. To replay, run `python3 verification/check_python.py`, then compile `verification/check_cpp.cpp` with a C++17 compiler and execute the resulting binary. These computations corroborate the general proof but are not its substitute.

As concrete checks, \(G_{4,4}\) has \(H_{4,4}(z)=4z^4+4z^5\), whereas \(G_{3,5}\) has \(H_{3,5}(z)=2z^3+4z^4+2z^5\). Both have eight vertices and the same minimum-forcing-set count as an ordinary eight-cycle, but distinct propagation-time distributions.

## Relationship to prior work
Chilakamarri, Dean, Kang and Yi introduced the iteration-index viewpoint and computed the cycle value \(\lceil(n-2)/2\rceil\). Hogben and coauthors formalized minimum and maximum propagation time, efficient forcing sets, and the propagation-time interval. Boyer and coauthors proved in Theorem 22, Claim 1 that adding one chord preserves **the entire family of zero forcing sets** of a cycle, and consequently preserves its zero-forcing polynomial; that prior theorem is explicitly used and not claimed as new. Ferrero and coauthors subsequently studied propagation-time intervals and fixed propagation time for general graph families. The present result instead gives a seed-resolved propagation-time formula, an exact time enumerator, a parity-dependent efficient-set count, and a sharp comparison for every single-chord cycle. These dynamic quantities are not supplied by the published zero-forcing-polynomial identity or the listed general definitions.

## Limitations
This theorem concerns ordinary parallel standard forcing on singly chorded cycles with at least four vertices. It does not characterize all larger **minimal** zero-forcing sets, multiple chords, other forcing variants, or asynchronous forcing schedules. The literature comparison covers the directly relevant available primary sources; a mathematically equivalent unindexed treatment cannot be ruled out without independent historical review. No independent scholarly audit has been performed.

## References
1. K. B. Chilakamarri, N. Dean, C. X. Kang and E. Yi, *Iteration Index of a Zero Forcing Set in a Graph* (first public arXiv version 2011-05-08), arXiv:1105.1492, https://arxiv.org/abs/1105.1492.
2. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker and M. Young, *Propagation time for zero forcing on a graph* (first public arXiv version 2014-10-15), arXiv:1410.4191, https://arxiv.org/abs/1410.4191.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph* (first public arXiv version 2018-01-26), arXiv:1801.08910, https://arxiv.org/abs/1801.08910.
4. D. Ferrero, H. T. Hall, L. Hogben, M. Hunnell and B. Small, *Zero forcing propagation time intervals and graphs with fixed propagation time* (first public arXiv version 2025-11-20), arXiv:2511.16335, https://arxiv.org/abs/2511.16335.
