# A facilitated-hypercube model and sharp mobility geometry for double-pattern-avoiding permutations

## Finding

For each integer \(n\ge2\), let \(G_n\) have as vertices the permutations of \([n]\) avoiding the patterns \(231\) and \(321\), with an edge precisely when one transposition of adjacent **positions** remains in this class. There is a graph isomorphism from \(G_n\) to the binary graph on \(m=n-1\) bits \(x_1,\ldots,x_m\), where \(x_i\) can be flipped if and only if \(i=1\) or \(x_{i-1}=1\). Consequently

\[
|V(G_n)|=2^{n-1},\qquad |E(G_n)|=n2^{n-3},\qquad \operatorname{diam}(G_n)=2n-3.
\]

The multiplicity of degree \(d\) is exactly \(2\binom{n-2}{d-1}\) for \(1\le d\le n-1\). The graph has precisely two leaves. A recursively specified Hamilton path joins them, and for \(n\ge3\) no Hamilton cycle is possible.

## Assumptions and scope

Patterns are classical (not necessarily consecutive). Positions and permutation values are labelled, and moves exchange entries at positions \(j,j+1\) only. For \(n=2\), the graph is one edge, so \(n2^{n-3}=1\). No all-permutation or single-pattern avoidance claims are asserted. The graph has undirected edges.

## Proof

**1. Unique composition representation.** Let \(\pi\) be a permutation avoiding both patterns and write its first value as \(k\). Every smaller value must appear before every larger value, else \(k\), a larger value, and a smaller value form \(231\). The smaller values must be increasing, else \(k\) and a descending pair form \(321\). Thus the prefix is \((k,1,2,\ldots,k-1)\), and the remaining suffix, if present, is another such permutation after standardizing labels. Hence \(\pi\) is uniquely the direct sum of blocks \((a,1,2,\ldots,a-1)\) of arbitrary positive sizes \(a\) forming a composition of \(n\). Conversely these direct sums avoid both forbidden patterns (every block avoids them, and any cross-block triple is not \(231\) or \(321\)). The composition model and total \(2^{n-1}\) are established independently in earlier literature and are not claimed here as new.

**2. Exact move correspondence.** A swap within one block is permitted precisely when it exchanges that block's first two entries: it splits a block of size \(a\ge2\) into consecutive blocks of sizes \(1,a-1\). A swap between blocks is permitted precisely when the left block has size one: it merges sizes \(1,b\) to \(b+1\). To exclude the remaining cases, a swap of entries later than the first two within a block creates \(321\) with the block maximum; a swap over a boundary whose left block has size at least two creates \(231\) with the maxima of the two blocks and the last value of the left block. Assign cut bit \(x_i=1\) when a block ends after position \(i\), and declare the boundary bit \(x_0=1\). The two permitted operations toggle \(x_i\), precisely if \(x_{i-1}=1\); all other toggles are forbidden. Thus this is an exact graph isomorphism, including all adjacencies.

**3. Degrees and edge counts.** Every cut word has one always-available flip (the first bit), plus one flip for each one among its first \(n-2\) bits. Its final bit does not affect the degree. Therefore \(\deg(x)=1+\sum_{i=1}^{n-2}x_i\), giving exactly \(2\binom{n-2}{d-1}\) vertices of degree \(d\). The degree sum is \(n2^{n-2}\), so the undirected edge count is \(n2^{n-3}\). The two leaves have bit words \(0^{n-1}\) and \(0^{n-2}1\).

**4. Sharp diameter.** Put \(m=n-1\). Given any two cut words \(x,y\), first turn all the first \(m-1\) bits to one, processing left to right, using at most \(m-1\) legal flips; change the last bit to its target if necessary (at most one flip); then restore the first \(m-1\) bits to those of \(y\), processing right to left (at most \(m-1\) flips). Each restoration is legal because its immediate predecessor has not yet been restored and is still one. This proves connectivity and the upper bound \(2m-1\). From \(0^m\) to \(0^{m-1}1\), the final bit must flip. Immediately before its first flip the previous bit must be one, which itself requires the preceding bit to have been one earlier, recursively down to the first bit. Since these \(m-1\) preceding bits all begin and end zero, each must flip at least twice; the final bit must flip at least once. Thus distance at least \(2m-1\), proving exact diameter \(2n-3\).

**5. Hamilton path.** Define a list of \(m\)-bit words recursively: \(H_1=(0,1)\), and \(H_m\) is the list of \(H_{m-1}\) with a zero appended, followed by the reversal of \(H_{m-1}\) with a one appended. Each within-half transition is legal by induction. The joining transition flips the last bit when the preceding bit is one, because the final word of \(H_{m-1}\) is \(0^{m-2}1\) for \(m\ge2\). The path visits every word once and has endpoints \(0^m\), \(0^{m-1}1\). For \(n\ge3\), the two leaves rule out a Hamilton cycle.

## Verification

The accompanying standalone `verify.py` uses Python's standard library and independently constructs the permutation graph by checking **all classical triple patterns**. It compares each permitted adjacent-position swap with its binary-model neighbor, evaluates the degree distribution and edge count, and computes all-pairs shortest-path diameters for every \(2\le n\le8\). In total, \(254\) distinct valid permutations were checked directly. It also independently validates the recursive Hamilton paths through \(n=14\). To repeat: `python3 verify.py`. These finite tests corroborate, but do not replace, the all-length proof.

## Relationship to prior work

Simion and Schmidt's composition characterization is reproduced in Janson's Section 6, Proposition 6.1, and the resulting enumeration is **previously known**. Baril's 2009 paper develops restricted permutation Gray codes, and Barcucci–Bernini–Pinzani (2022) construct adjacent-swap Gray codes for \(321,312\)-avoiding permutations with a further optional restriction; their class is related by inversion, which sends position swaps to value swaps rather than directly preserving the position-swap graph. These papers motivate the Hamilton-path corollary but are not asserted to have no related Gray codes. The separate graph on **all** \(321\)-avoiders is larger and does not determine distances in this induced graph. The established East-model local facilitation rule motivates the graph identification, but standard East-process studies concern stochastic dynamics rather than the present permutation-induced metric and degree spectrum.

## Limitations

The claim concerns exact undirected single-adjacent-position swaps in one doubly restricted permutation class, not arbitrary transpositions or the equivalent pattern classes under inverse mapping. A related or unpublished East-model graph metric or Gray-code construction could independently yield some of these conclusions; no assertion of absolute historical uniqueness is made. There has been no independent mathematical audit. No mixing-time statement is inferred from the graph distances.

## References

1. S. Janson, *Patterns in random permutations avoiding some sets of multiple patterns*, arXiv:1804.06071 (first posted 17 April 2018), Section 6, https://arxiv.org/abs/1804.06071 ; journal edition https://doi.org/10.1007/s00453-019-00586-5.
2. R. Simion and F. W. Schmidt, *Restricted permutations*, European Journal of Combinatorics 6 (1985), 383–406, Proposition 12, as cited in Janson.
3. J.-L. Baril, *More restrictive Gray codes for some classes of pattern avoiding permutations*, Information Processing Letters 109 (2009), 799–805, https://doi.org/10.1016/j.ipl.2009.03.025.
4. E. Barcucci, A. Bernini and R. Pinzani, *Strings from linear recurrences and permutations: a Gray code*, arXiv:2204.10069 (2022), https://arxiv.org/abs/2204.10069.
5. W. M. B. Dukes et al., *Combinatorial Gray codes for classes of pattern avoiding permutations*, https://arxiv.org/abs/0704.2048 (2007).
6. K. Klobas et al., *Exact pretransition effects in kinetically constrained circuits: Dynamical fluctuations in the Floquet-East model*, Physical Review E 110 (2024), L022101, https://doi.org/10.1103/PhysRevE.110.L022101.
