# Complete census of binary order-five linear universal partial words with two wildcards

## Finding
A **linear universal partial word of order five** is a literal string over \(\{0,1,*\}\) in which each of the \(32\) binary strings of length \(5\) is compatible with exactly one contiguous length-five window; \(*\) matches either bit. Among such strings containing **exactly two** wildcards, there are exactly **\(1328\)** words, with lengths and counts

| Length | Number of words | Number of reversal/complement classes |
|---:|---:|---:|
| \(26\) | \(8\) | \(2\) |
| \(27\) | \(32\) | \(8\) |
| \(28\) | \(32\) | \(8\) |
| \(29\) | \(136\) | \(34\) |
| \(30\) | \(352\) | \(88\) |
| \(33\) | \(768\) | \(192\) |

No such word exists at any other length. Reversal and simultaneous interchange of \(0\) with \(1\) generate exactly **\(332\)** equivalence classes, each of size four. A complete machine-readable list of all \(1328\) words is provided in `upwords_order5.txt`.

## Assumptions and scope
Words are linear, not cyclic; their positions and endpoint orientation are distinguished when counting the \(1328\) strings. Every occurrence is an occurrence at a window-start position, not a choice of concrete substitution of the wildcard symbols globally. Two different windows may not cover the same binary target. Exactly two literal wildcard positions are required. The two symmetry operations are reversal of the entire word and global complementation of its nonwildcard bits; neither changes its length or wildcard count.

## Proof
For a candidate word of length \(L\), the number of length-five windows is \(L-4\). Since each window represents at least one binary word and all \(32\) distinct targets must occur exactly once, necessarily \(5\le L\le36\). Fix wildcard positions \(0\le a<b<L\). Write \(c_s\) for the number of these wildcard positions in the window beginning at \(s\), with \(0\le s\le L-5\). That window covers exactly \(2^{c_s}\) targets. Thus the necessary weight identity is

\[
\sum_{s=0}^{L-5}2^{c_s}=32.
\]

The exhaustive search in `verify.cpp` considers every integer \(L\) in the proved interval and every pair \(a<b\), discarding a pair only when this necessary identity fails. For every retained pair it recursively assigns both possible bits to **each** nonwildcard position and assigns \(*\) at precisely the selected positions. The rolling base-three state records the last four symbols. As soon as a fifth symbol is assigned, the new contiguous five-symbol window determines a \(32\)-bit mask of all binary strings compatible with it, computed by direct comparison against each of the \(32\) targets. The search discards a branch precisely if this new mask intersects the union of the masks of earlier completed windows. This condition is irreversible: once a target is covered by two windows, no choice of later symbols can restore unique coverage. Conversely, no branch representing a possible universal partial word is discarded, since its masks are necessarily pairwise disjoint.

At the final position, all \(L-4\) windows have been processed. The weight identity states that the sum of their individual mask cardinalities is \(32\), and pairwise disjointness states that their union has cardinality \(32\). As there are precisely \(32\) possible binary targets, the union is exactly the target set and each target occurs once. The program also verifies this full-union invariant explicitly before recording a word. Hence the accepted leaves are **exactly** the desired objects, with no probabilistic or unverified search heuristic. Every full string has a unique length, wildcard-position pair, and sequence of nonwildcard bits, so it appears only once.

This finite exhaustion produces counts \(8,32,32,136,352,768\) at lengths \(26,27,28,29,30,33\), and zero at the other tested lengths, which is the entire mathematically bounded domain. The second verifier `verify.py` directly regenerates all window matches, checking that each accepted word covers each of the \(32\) targets once. It independently forms the four symmetry transforms of each word and verifies that the complete list is invariant under them and partitions into \(332\) disjoint four-element orbits, with the claimed class counts by length.

## Verification
From a directory containing `verify.cpp`, `verify.py`, and `upwords_order5.txt`, use a C++17 compiler and Python 3:

```sh
g++ -O2 -std=c++17 -Wall -Wextra verify.cpp -o verify
./verify > enumerated.txt
python3 verify.py upwords_order5.txt enumerated.txt
```

An actual replay compiled and executed the shipped C++ source, traversed \(31{,}600{,}915\) search nodes, output the same \(1328\) sorted words, and reported `EXHAUSTIVE_OK`; the independent checker then reported `VERIFY_OK words=1328 orbits=332`. The complete output is included in the package, making comparison exact rather than relying on an aggregate count or log alone.

## Relationship to prior work
Chen, Kitaev, Mütze, and Sun introduce and study universal partial words, and their Table 2 provides **examples** for binary order five with two wildcards; the paper develops nonexistence criteria and an infinite family, but does not give this complete labeled or symmetry-reduced census. Follow-up work on nonbinary alphabets formulates the number of universal partial words as an enumeration problem. Enumeration of *cyclic* universal partial words or distinct ordinary de Bruijn sequences addresses different sets of objects and does not imply the linear two-wildcard counts here. The originality claim concerns the exact complete order-five census, its attainable-length spectrum, and its reversal/complement orbit decomposition, not the definition or existence of these partial words.

## Limitations
This is a finite but complete classification for order five only. It does not prove a formula for arbitrary orders or a universal asymptotic count. The proof of exact cardinalities is an exhaustive computational argument with transparent source, mathematical completeness/pruning invariants, a complete output list and an independent candidate-checking implementation, rather than a short symbolic expression for the counts. Published examples and established constraints may overlap with individual listed words. Other equivalent enumerations in unindexed or inaccessible historical material cannot be excluded by searches alone. No independent mathematical audit has been performed.

## References
1. H. Z. Q. Chen, S. Kitaev, T. Mütze, and B. Y. Sun, *On universal partial words*, arXiv:1601.06456, first public version 25 January 2016, https://arxiv.org/html/1601.06456v5; especially Table 2 and Section 4.
2. J. Goeckner et al., *Universal partial words over non-binary alphabets*, Theoretical Computer Science, https://doi.org/10.1016/j.tcs.2017.12.022; introductory definition and the later enumeration question.
