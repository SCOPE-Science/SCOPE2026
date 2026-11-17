# Exact first noninterleaving binary substring-composition census at length 23

## Finding

For binary linear words of length \(23\), the multiset of the compositions of **all** nonempty contiguous substrings yields exactly \(4{,}196{,}192\) distinct observations. Of their equivalence classes, exactly \(4{,}096\) contain one word, \(4{,}191{,}936\) contain two, and \(160\) contain four; no larger classes occur. Exactly \(152\) of the four-word classes consist of nontrivial interleaved words, while **eight** four-word classes consist entirely of words indecomposable under interleaving. These eight exceptional classes form four pairs under global bit complementation. Accordingly the maximum noiseless codebook size for the full substring-composition observation at blocklength \(23\) is exactly \(4{,}196{,}192\).

## Assumptions and scope

The objects are **indexed, linear** binary words \(w=w_1\cdots w_{23}\), not cyclic words or words modulo reversal. For each substring length \(1\le \ell\le23\) and number of ones \(0\le k\le\ell\), define the observed multiplicity

\[
M_w(\ell,k)=\left|\left\{ i: 1\le i\le24-\ell,\;\sum_{j=i}^{i+\ell-1}w_j=k\right\}\right|.
\]

Two words are equivalent precisely when every entry of this profile agrees. This is the standard full substring-composition multiset, with substring multiplicities retained and substring positions discarded. Reversal always preserves it. The *interleaving* operation is \(s\circ t=s\,t_1\,s\,t_2\cdots t_m\,s\) for a nonempty binary word \(s\) and \(t=t_1\cdots t_m\); a word is interleaving-decomposable if it admits such a representation with both factors nonempty. The classification below treats **every** one of the \(2^{23}=8{,}388{,}608\) indexed words.

## Proof

The theorem is a **finite exhaustive result with a complete replayable exact enumeration**, not an extrapolation from a smaller sample. Every binary word is represented once by an integer from \(0\) through \(2^{23}-1\), with integer bit \(i\) giving the \((i+1)\)-st symbol. The complete algorithm in `exact_census.cpp` loops through this entire integer interval.

For speed, it assigns the word an additive 64-bit fingerprint obtained by summing fixed 64-bit labels indexed by the substring length and number of ones for every contiguous substring. Equality of complete composition multisets **necessarily implies** equality of fingerprints, even with modular overflow; therefore sorting by fingerprints cannot separate genuinely equivalent words. Every hash bucket of size one is checked to be a palindrome, and every bucket of size two is checked to consist of mutual reversals. In those cases the exact profile agreement follows from reversal symmetry. All other buckets are partitioned by their **complete, exact integer multiplicity vectors**, with no reliance on collision resistance. Thus there are neither false separations nor false identifications, and the procedure exhausts every equivalence class. Its exact output is

| Class size | Number of classes | Number of words |
|---|---:|---:|
| \(1\) | \(4{,}096\) | \(4{,}096\) |
| \(2\) | \(4{,}191{,}936\) | \(8{,}383{,}872\) |
| \(4\) | \(160\) | \(640\) |

The word counts sum to \(8{,}388{,}608\). The program emits the **complete list** of \(160\) four-word classes. The second program, `independent_census.cpp`, computes substring weights from prefix sums rather than masked popcounts, uses different labels and a separate exact-profile implementation, and produces precisely the same three totals and all \(160\) four-word classes.

For interleaving, any nontrivial factorization of a \(23\)-bit word satisfies \((|s|+1)(|t|+1)=24\). Hence one can inspect all proper divisors \(d=|s|+1\) of \(24\): writing \(a=d-1\), the word is decomposable if and only if its contiguous length-\(a\) blocks at starting positions \(0,d,2d,\ldots\) all agree. The remaining symbols uniquely define \(t\). This is an exhaustive necessity-and-sufficiency check, not a heuristic. `verify.py` applies it separately to every one of the \(640\) words in the four-word classes and additionally computes closures under reversal and reversal of each available interleaving factor. The exact outcomes are \(152\) fully interleaved classes and eight entirely indecomposable classes. The eight full classes are provided in `FOUR_CLASSES.txt` (the verifier prints them in binary), and complementing all bits pairs them into four orbits. In particular, the known \(23\)-symbol noninterleaving example is not the complete census of such classes.

Finally, no two codewords may share an observation; selecting one representative from each observation class is both necessary and sufficient for a noiseless reconstruction code. Its maximum size is therefore exactly the number of classes counted above.

## Verification

Run `python3 verify.py --full` with a C++17 compiler such as `g++` installed. The script independently compiles both enumerators, checks each output against the explicit class-size totals, compares all \(160\) sorted four-word classes to each other and the embedded `FOUR_CLASSES.txt`, computes the complete exact composition signatures for the \(640\) ambiguous words, checks factorization and closure for every class, and verifies the complement orbit count. Expected final status: `TWO_INDEPENDENT_FULL_CENSUSES_OK` and `VERIFICATION_OK`. Plain `python3 verify.py` replays the detailed class classification using the embedded list without rerunning the entire universe census. The recorded full run passed both modes; all arithmetic and comparisons are exact.

## Relationship to prior work

Acharya, Das, Milenkovic, Orlitsky and Pan established the string-composition equivalence problem, polynomial factorization criteria, and interleaving methods. Their public manuscript and expanded article report that all confusable binary words through length \(22\) arise from interleaving and explicitly exhibit a **noninterleaving pair at length \(23\)**. That existence example and the earliest cutoff are **prior results**, not claimed here. The result here instead resolves the **complete distribution of all length-23 observation fibers**, the exact finite-length zero-error codebook cardinality, and the number and complement-orbit structure of **all** first-length noninterleaving fibers. The known general algebraic factorization theorem does not by itself state these finite counts. Gupta and Mahdavifar develop efficient reconstruction algorithms and construction-specific codebooks, but do not give this complete length-23 census. The literature comparison is qualified: a numerical table in another unexamined publication could still establish priority.

## Limitations

This is a finite exact enumeration for binary linear words of length \(23\) with noiseless, complete substring-composition data. It is **not** a formula for arbitrary lengths, larger alphabets, cyclic observations, sampling errors, or multiset corruption. The program's speed-up uses fingerprints but its exhaustiveness and equality decisions are exact, not probabilistic. No independent external scientific audit has been performed; historical priority is not independently certified.

## References

1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, *String Reconstruction from Substring Compositions*, first public version 10 March 2014, arXiv:1403.2439v1, https://arxiv.org/abs/1403.2439 . Relevant sections: definitions; interleaving and its theorem; first noninterleaving example at length 23.
2. Same authors, expanded openly accessible manuscript for *SIAM Journal on Discrete Mathematics*, https://people.ece.cornell.edu/acharya/papers/str_rcn_sidma.pdf . Relevant sections: polynomial factorization, Theorem 26, Corollary 31 and the 23-bit example.
3. U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955, https://arxiv.org/abs/2201.09955 . Relevant sections: reconstruction algorithms and construction-specific codebooks.
