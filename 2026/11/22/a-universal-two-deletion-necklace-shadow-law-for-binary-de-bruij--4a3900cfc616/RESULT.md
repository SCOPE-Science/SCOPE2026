# A universal two-deletion necklace-shadow law for binary de Bruijn cycles

## Finding
Let \(W\) be any binary de Bruijn necklace of order \(n\ge3\), with \(N=2^n\) cyclic symbols. Form the set \(\mathcal D_2(W)\) of necklaces of length \(N-2\) obtained by deleting exactly two distinct cyclic positions, without identifying reflections or exchanging the alphabet letters. Partition the outputs by the numbers of deleted zeros and ones. Their respective cardinalities are
\[
\begin{array}{c|ccc}
\text{deleted composition}&(2,0)&(1,1)&(0,2)\\\hline
\text{distinct necklaces}&N^2/32&N^2/16-N/4&N^2/32.
\end{array}
\]
Consequently \(|\mathcal D_2(W)|=N(N-2)/8=2^{2n-3}-2^{n-2}\), independent of the de Bruijn cycle chosen. In particular this is a complete two-deletion output-composition spectrum, not merely an average over cycles.

## Assumptions and scope
A binary de Bruijn cycle of order \(n\) is a cyclic binary word in which every length-\(n\) binary factor occurs precisely once. Rotations, but not reversals or bit complements, are identified in output. Exactly two different source indices are deleted; the deletion choices need not be consecutive. The order restriction \(n\ge3\) is essential: order two has a different, short-word boundary behavior.

## Proof
Write \(m=N/4\). There are exactly \(m\) cyclic zero-runs and \(m\) cyclic one-runs, since each of `01` and `10` occurs \(2^{n-2}=m\) times. Among the runs of either symbol, precisely \(s=N/8=m/2\) have length one, since each of `101` and `010` occurs \(2^{n-3}\) times. Each symbol also has a cyclic run of length \(n\) (from its unique constant length-\(n\) factor), so there are non-singleton runs of both symbols.

**Run-choice collision rule.** Name the \(2m\) cyclic runs in alternating order. For same-color deletions, a possible pair of distinct runs yields one distinct output, and deleting twice from one run is possible precisely when that run has length at least two. For mixed-color deletions, initially name one zero-run and one one-run. Two such choices give the same output exactly when one may pass between them by the following local move: delete a singleton run of one color, and move the other deleted symbol from its neighboring run on one side to the neighboring run on the other side. There is one such identification for every singleton run. These statements can be checked directly in the ordered run-length representation. If no run disappears, the unchanged cyclic run order and decreased lengths recover the chosen runs. If a run disappears, only its two same-colored neighbors merge; the only choice not recovered from the remaining run lengths is which of these neighboring runs supplied the other deletion. When both chosen runs disappear, the two adjacent singleton possibilities apply successively. No change away from a deleted singleton can give an identical aligned run-length sequence.

The preceding local argument is valid with a common source coordinate frame. Here this is forced even though the output is considered only modulo rotation. Align two equal output necklaces as circular words and call an output length-\(n\) window *untouched* in one deletion representation if it contains no new adjacency introduced by either deletion. There are at most \(2(n-1)\) affected window starts in each representation. Thus the two representations have at least \(N-2-4(n-1)=2^n-4n+2>0\) window starts untouched in both when \(n\ge4\). Any such factor appears exactly once in the original de Bruijn cycle, so it synchronizes the two representations to the same original source coordinate, ruling out further coincidences caused solely by output rotation. The boundary order \(n=3\) is checked directly below. The same-color choices are therefore \(\binom m2+(m-s)=m^2/2\) in each class.

The graph on the \(m^2\) mixed run-pairs has one edge for each local singleton move. It is a subgraph of the alternating cyclic chain of adjacent run-pairs: moving across each singleton continues along this chain, while a run of length at least two breaks it. Since both colors have non-singleton runs, this graph is a forest, with exactly \(2s=m\) edges and thus \(m^2-m\) components. The total is \(m^2/2+(m^2-m)+m^2/2=2m^2-m=N(N-2)/8\). For \(n=3\), direct enumeration of the two order-three de Bruijn cycles gives \((2,2,2)\), agreeing with \(m=2\).

## Verification
The standalone `verify.cpp` builds de Bruijn circuits directly from all successor wiring tables, enumerates both-position deletions, canonicalizes each output under cyclic rotation, and separates them by deleted composition. Exhaustive verification gives the following (the middle three numbers count outputs deleting two ones, one of each, and two zeros respectively): order 3: 2 cycles, \((2,2,2)\); order 4: 16 cycles, \((8,12,8)\); order 5: 2048 cycles, \((32,56,32)\). A deterministic sample of 2000 order-six successor wirings contained 29 full cycles, each with \((128,240,128)\). Compile using `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. These finite checks supplement the all-order proof; they are not substituted for it.

## Relationship to prior work
The general linear two-deletion descendant count is given in Sloane, *On Single-Deletion-Correcting Codes*, Theorem 5.1, summarizing work with Rains. That result counts linear descendants and does not identify outputs up to cyclic rotation, restrict the source to a de Bruijn necklace, or give the composition-refined law above. Sawada, Williams and Wong give a universal construction of de Bruijn sequences, not their cyclic two-deletion output spectra. Related existing circular two-deletion calculations for a special elongated-run necklace family do not cover any general de Bruijn cycle. The claimed contribution is the invariant complete cyclic composition spectrum and its run-based explanation, not the classical linear deletion theorem or the elementary de Bruijn run statistics.

## Limitations
The theorem assumes exactly two deletions, a binary alphabet, and order at least three. It does not assert a result for arbitrary binary necklaces, for three deletions, for deletion-output probabilities weighted by the number of masks, or for quotienting by reversal. The originality comparison is based on accessible primary literature and indexed related statements; earlier equivalent work not found in those sources remains possible.

## References
1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197v1, 22 July 2002, especially Section 5 and Theorem 5.1. https://arxiv.org/html/math/0207197v1
2. J. Sawada, A. Williams and D. Wong, *A surprisingly simple de Bruijn sequence construction*, preprint dated 12 August 2015; *Discrete Mathematics* 339 (2016), 127–131. https://doi.org/10.1016/j.disc.2015.08.002
