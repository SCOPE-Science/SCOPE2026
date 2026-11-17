# Independent mathematical audit

## correctness

PASS

For q>=2 distinct letters each occurring in exactly one positive-length cyclic run, a two-letter boundary transition identifies the run phase uniquely. An interior run in a common factor must therefore be the full run of the same letter in both periodic words; no unequal run may occur internally. Between consecutive mismatches i,j, the word F_i uses the suffix of the shorter i-run, all equal interior runs, and prefix of the shorter j-run; it appears in each word. Every common factor must be a factor of some such interval, including constant-letter factors; each F_i cannot extend at either end because immediately across its boundary the shorter and longer profiles show distinct next/previous letters. Since F_i begins with distinct letter c_i, words are different and give exactly |D| maximal common factors. One mismatch case j=i traverses a complete period and D empty is separately excluded (infinite common language). Independent brute word-factor enumeration on 1542 profile pairs found exact language equality, maximal words and no missing factors through L+1; source checker covers 2684 cases. Infinite theorem uses transition proof, not finite sample.

## originality

PASS

The exact finite mismatch-gap basis for *all inclusion-maximal common words* of two infinite cyclic-run words has distinct content from finite dynamic locally maximal occurrence factors, circular factors, or generic LCS algorithms. Originality remains best-of-knowledge due to broad unindexed word-combinatorics literature.

## value

PASS

The exact structure and size of the antichain of maximal common factors under a natural shared cyclic run-order hypothesis gives a concise basis and explicit LCS length for all positive run profiles, a reusable fact for compressed periodic strings. Neither an arbitrary numeric slice nor routine relabeling; transition-phase structure underlies proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
