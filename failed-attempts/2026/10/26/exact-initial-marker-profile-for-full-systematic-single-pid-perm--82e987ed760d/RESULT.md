# Exact initial marker profile for full-systematic single-PID permutation codes

## Finding

Let \(R(n)\) be the minimum number of distinct marker symbols required by a full-systematic encoder of every \(n\)-symbol permutation, uniquely correctable after one permutation-invariant deletion (PID). Then

\[
R(1)=0,\qquad R(2)=1,\qquad R(3)=R(4)=2.
\]

Moreover, \(R(n)\ge2\) for every \(n\ge3\). These statements use *all* message permutations and exactly the order-preserving embedding required by full systematicity. The upper bounds are witnessed by concrete six-word and twenty-four-word codebooks. No upper bound for \(R(n)\) at \(n\ge5\) is claimed.

## Assumptions and scope

Write \(\mathfrak S_n\) for permutations of the labels \(1,\ldots,n\). A code with \(r\) markers is a map \(E:\mathfrak S_n\to\mathfrak S_{n+r}\) for which deleting labels above \(n\) from \(E(\sigma)\) recovers \(\sigma\), without changing its relative order. For a permutation \(\pi\) of length \(N\), let \(\operatorname{std}(\pi)\) replace the smallest entry by \(1\), the next smallest by \(2\), and so on. Its one-PID deletion shadow is

\[
\mathcal D(\pi)=\{\operatorname{std}(\pi_1\ldots\widehat{\pi_i}\ldots\pi_N):1\le i\le N\}.
\]

An encoder corrects one PID precisely when these shadows are pairwise disjoint over distinct messages. For *at most* one deletion, the zero-deletion outputs have a different length and the same property suffices. Markers are distinct labeled symbols \(n+1,\ldots,n+r\) inserted anywhere among the original entries. No assumption of linearity, efficient encoding, or a uniform formula across \(n\) is imposed.

## Proof

**Lower bounds.** With no marker and \(n\ge2\), all \(n!\) messages are codewords in \(\mathfrak S_n\), but the nonempty shadows lie in an alphabet of \((n-1)!\) possible permutations; disjointness is impossible.

For one marker, there are \(n!\) distinct codewords of length \(n+1\), but only \(n!\) possible received permutations of length \(n\). Thus pairwise disjoint, nonempty shadows would all have to be singletons. A permutation has singleton one-PID shadow if and only if it is increasing or decreasing: the deletion results at two adjacent positions coincide exactly when their entries are consecutive integers. Hence a singleton shadow forces all successive entries to differ in absolute value by one. A permutation using each integer once cannot reverse direction in such a path, so it must be monotone. There are only two monotone permutations. For \(n\ge3\), \(n!>2\), contradicting the needed \(n!\) singleton-shadow codewords. Therefore \(R(n)\ge2\) for \(n\ge3\).

**Matching constructions.** At \(n=1\), the unique one-letter word needs no marker. At \(n=2\), the two messages \(12,21\) can be encoded as \(123,321\), whose shadows are the disjoint singletons \(\{12\}\) and \(\{21\}\).

For \(n=3\), the following six five-letter codewords, written in message order, give one codeword for each of the six message permutations:

```
15234 14532 21435 42315 34512 54321
```

For \(n=4\), the following twenty-four six-letter words each include the full ordered message as their subsequence; together, they represent all \(24\) messages exactly once:

```
123456 125463 561324 134265 146523 146325
216345 261453 263514 623415 245613 243156
531246 316542 632154 653241 563412 346521
654123 641532 425163 425361 436152 453216
```

Checking the rank-standardized deletion shadows gives \(16\) distinct received permutations across the six words of length five, and \(97\) distinct received permutations across the twenty-four words of length six, with no output shared by distinct codewords. The complete direct checker in `VERIFY.py` implements the normalization, forms every shadow, asserts the one-codeword-per-message property and the absence of collisions, and returns `VERIFY_OK`. Thus \(R(3)\le2\) and \(R(4)\le2\), matching the lower bounds.

## Verification

Run `python3 VERIFY.py` using only the Python standard library. The program independently computes all rank-standardized one-deletion outputs of every displayed word, confirms exact complete message coverage and output disjointness, and exhaustively checks the singleton-shadow lemma for permutation lengths from \(2\) through \(7\). For the two nontrivial instances, it finds \(16\) and \(97\) received permutations, out of universes of sizes \(24\) and \(120\). These are finite certificate checks; the general lower bound follows from the preceding argument, not from finite experimentation. The recorded checker output is in `VERIFY.txt`.

## Relationship to prior work

Wu, Bui, Niu, Vu, and Wang (arXiv:2609.37578v1, September 29, 2026) define precisely this full-systematic permutation-code model, including PID rank standardization, and obtain asymptotic constructions; their Corollary 2 gives a four-marker single-PID construction for sufficiently large \(n\). It does not specify the exact two-marker finite-length profile here. Zhou, Jiang, and Bruck (ISIT 2012) consider the same systematic insertion-of-extra-labels object under Kendall distance, rather than the rank-standardized deletion channel. Their two-marker Kendall-distance-three construction does not itself imply disjoint PID deletion shadows: two permutations can have the same standardized one-deletion output while being separated by four or more adjacent swaps. Gabrys et al. (ISIT 2014) investigate the PID deletion model and ordinary (not full-systematic) permutation code cardinalities. Their single-deletion bounds and signature construction do not enforce a distinct codeword above each possible original message, and therefore do not directly imply the finite full-systematic profile. The present result only asserts the exact values for \(n\le4\), not a general improvement on the asymptotic construction.

## Limitations

The result does not determine \(R(n)\) for \(n\ge5\), classify all optimal encoders, provide an efficient family of encoders, or address two deletions. Its upper bounds rely on explicitly checkable finite codebooks; a small checked construction is not a claim of an infinite optimal family. A previously unindexed equivalent finite computation cannot be excluded,.

## References

1. Bolin Wu, Quan D. Bui, Kai Niu, Van Khu Vu, and Shuche Wang, *Order-Optimal Systematic Permutation Codes for Correcting t Deletions*, arXiv:2609.37578v1 (first public September 29, 2026), https://arxiv.org/html/2609.37578v1.
2. Ryan Gabrys, Eitan Yaakobi, Farzad Farnoud, Frederic Sala, Jehoshua Bruck, and Lara Dolecek, *Single-Deletion-Correcting Codes over Permutations*, Proceedings of ISIT 2014, pp. 2764–2768, DOI:10.1109/ISIT.2014.6875337, https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf.
3. Hongchao Zhou, Anxiao Jiang, and Jehoshua Bruck, *Systematic Error-Correcting Codes for Rank Modulation*, ISIT 2012, DOI:10.1109/ISIT.2012.6284106, https://people.engr.tamu.edu/ajiang/Publications/Systematic_ISIT2012.pdf.
