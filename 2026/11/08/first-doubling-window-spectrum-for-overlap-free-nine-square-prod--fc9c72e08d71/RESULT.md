# First doubling-window spectrum for overlap-free nine-square products

## Finding
For every integer \(n\) with \(0\leq n\leq 96\), let \(E_n\) be the set of binary words of length \(n\) that (i) have no factor \(axaxa\) with \(a\in\{0,1\}\) and \(x\in\{0,1\}^*\), and (ii) can be expressed as a concatenation of exactly nine nonempty squares \(u_1u_1\cdots u_9u_9\). Then
\[
|E_n|=\begin{cases}
2,&n\in\{48,76,92,96\},\\
4,&n=86,\\
0,&0\leq n\leq96\text{ otherwise}.
\end{cases}
\]
Consequently the entire first doubling window, from the minimum feasible length \(48\) to its first Thue–Morse doubled length \(96\), has only five feasible lengths and twelve labeled words. Each of these twelve words has exactly one ordered decomposition into nine nonempty squares. The file `census_96.tsv` gives all twelve words and the corresponding nine square-root lengths. The five counts include two pairs at \(48,76,92,96\) and two complementary pairs at \(86\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Words are linear, not necklaces or circular words. A square is \(uu\) for a nonempty binary word \(u\). Overlaps have the form \(axaxa\), including the three-letter overlap \(aaa\) when \(x\) is empty. A nine-square decomposition is an ordered list of nine blocks, each of which is a square; different decompositions of the same word are distinguished until uniqueness is established. Lengths \(n\) range over all integers from \(0\) through \(96\), inclusive. The doubling endpoint \(96=2\cdot48\) is natural because the Thue–Morse morphism \(\mu(0)=01\), \(\mu(1)=10\) preserves overlap-freeness and maps squares to squares.

## Proof
**Finite exhaustive lemma (square-block search).** If \(w\) has length at most \(96\) and is a concatenation of nine nonempty squares, each individual square has length at most \(96-8\cdot2=80\). Therefore its root has length at most \(40\). Every root of a square factor of an overlap-free word is itself overlap-free. Starting with the empty word, append each bit as long as no overlap is formed; when a word is extended by one bit, it suffices to check for an overlap ending at the new position. This generates *all* overlap-free binary words of each length at most \(40\), not a sample. For each root \(u\) retain \(uu\) exactly when it is overlap-free. There are exactly \(154\) distinct retained square blocks of length at most \(80\), with length-wise counts \(2,2,6,4,12,8,24,16,48,32\) at lengths \(2,4,6,8,12,16,24,32,48,64\) respectively.

Now build nine successive levels of distinct concatenations, retaining the ordered square-root-length recipes. At level \(k\), append every retained square block; discard a candidate only if its whole word contains an overlap, or if its current length plus the mandatory minimum \(2(9-k)\) for the remaining blocks exceeds \(96\). Inductively, this produces *every* overlap-free concatenation of \(k\) squares that can be extended to a nine-square word of length at most \(96\). The resulting numbers of distinct words (and equally of recipes) at levels \(k=1,\ldots,9\) are \(154,104,120,146,82,60,70,60,12\). At the ninth level the twelve words have respective lengths \(48\) (2 words), \(76\) (2), \(86\) (4), \(92\) (2), and \(96\) (2), with exactly one recipe per word. This is an exhaustive certificate for the stated domain. The program `verify_by_blocks.py` performs this search and compares the output with `census_96.tsv`.

**Independent length-prefix search.** Construct every overlap-free binary word through length \(96\) by one-bit extensions. Every newly created overlap must end at the new last symbol; thus for each period \(p\ge1\) with \(2p+1\le n\), the only forbidden suffix is equality of its first and last \(p+1\) symbols separated by \(p\). For an overlap-free word \(w\), let \(d_w(j)\) be the maximum number of nonempty square blocks concatenated to form its prefix of length \(j\); set \(d_w(0)=0\) and \(-\infty\) for impossible lengths. Exact dynamic programming gives
\[
d_w(j)=\max_{\substack{1\le h\le\lfloor j/2\rfloor\\w[j-2h:j-h]=w[j-h:j]}}\bigl(d_w(j-2h)+1\bigr).
\]
The published ten-square obstruction guarantees \(d_w(j)\le9\) for overlap-free \(w\), so \(d_w(j)\ge9\) is equivalent to the presence of an exact nine-block decomposition. The complete prefix census has \(416,722,856,960,1016\) overlap-free words at lengths \(48,76,86,92,96\), respectively. The number of those with a nine-square decomposition is \(2,2,4,2,2\); none of the other lengths through \(96\) has one. Explicit recursive splitting checks the uniqueness of each of the twelve optimal decompositions. Program `verify_by_words.py` is independent of the square-block generator and reproduces these counts.

Together, the two complete finite searches prove the claimed counts, exclusions, and decomposition uniqueness. No infinite extrapolation from this finite classification is asserted.

## Verification
Place `verify_by_words.py`, `verify_by_blocks.py`, and `census_96.tsv` in one directory and run `python3 verify_by_words.py` and `python3 verify_by_blocks.py`. Both use only the Python standard library. Each checks the complete census and hard-coded intermediate counts; either program fails with an assertion on disagreement. `verify_by_words.py` enumerates all linear binary words of the specified lengths via overlap-free prefix extension and uses a suffix-square dynamic program. `verify_by_blocks.py` independently enumerates all eligible square factors and their bounded concatenations. The manifest is the exact twelve-word output; it is not an input to restrict either search (only to compare final results).

## Relationship to prior work
Shallit proved that an overlap-free binary word cannot be a concatenation of ten squares and exhibited a nine-square example of length \(48\) (arXiv:2605.28570, Theorems 1 and 8). That known existence example and the general ten-square obstruction do not enumerate every nine-square word in the first doubling window, prove the long gap between feasible lengths, or determine the five exact fiber sizes and decomposition uniqueness in this window. The present result complements the extremal number-of-blocks theorem by classifying its feasible total lengths and multiplicities through the first morphic doubling scale. Minimum-length data at \(48\) are included for completeness, not treated as the novelty-bearing conclusion.

## Limitations
The classification ends at length \(96\), and no statement is made about a complete spectrum or all uniqueness phenomena at larger lengths. The finite exhaustive argument establishes the stated finite result exactly; it does not prove an infinite asymptotic law. The construction relies on the definitions of ordinary binary squares and ordinary overlap avoidance, not abelian or parameterized squares. Historical priority of the exact window spectrum is not independently established.

## References
Jeffrey Shallit, *Ten Squares Force an Overlap*, first posted 2026-05-27, arXiv:2605.28570v1, https://arxiv.org/abs/2605.28570 .
