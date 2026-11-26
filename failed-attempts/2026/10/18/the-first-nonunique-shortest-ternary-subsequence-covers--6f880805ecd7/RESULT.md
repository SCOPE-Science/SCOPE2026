# The first nonunique shortest ternary subsequence covers

## Finding

Let a subsequence cover (s-cover) of a nonempty finite word \(S\) be a nonempty word \(C\) such that every position of \(S\) lies in at least one subsequence occurrence of \(C\). Among all nonempty words over the alphabet \(\{0,1,2\}\), the least length admitting *two distinct shortest* s-covers is exactly \(11\). There are exactly six labeled words of that least length, all relabelings of `01012021010`. They are:

```
01012021010
02021012020
10102120101
12120102121
20201210202
21210201212
```

Each has exactly two shortest s-covers, both of length \(6\). For the displayed representative they are `010210` and `012010`; those for the remaining words are obtained by the same symbol permutations. No ternary word of length at most \(10\) has two distinct shortest s-covers. The statement includes words that use only one or two of the three allowed symbols.

## Assumptions and scope

Words are finite, nonempty, and indexed from zero. A subsequence occurrence consists of a strictly increasing tuple of positions, and distinct occurrences may overlap. Covering means that the *union of position sets* over all occurrences is all positions in the text. Covers are compared first by length, and distinct covers are distinct words, not distinct embeddings. The empty word is excluded as a cover. Exact enumeration is over all \(3^n\) labeled words at each length \(1\le n\le11\); permutations of symbols are not quotiented out in the count six.

## Proof

**1. Correct cover predicate.** Write \(m=|C|\), \(n=|S|\). For each \(0\le i\le n\), let \(P_i\) be the maximum length of a prefix of \(C\) embeddable in \(S[0:i]\). Let \(R_i\) be the maximum length of a suffix of \(C\) embeddable in \(S[i:n]\). Both are computed by the elementary left-to-right and right-to-left greedy scans. A position \(i\) is covered by a \(C\)-occurrence if and only if some \(0\le k<m\) satisfies all three conditions

\[
C[k]=S[i],\qquad k\le P_i,\qquad m-k-1\le R_{i+1}.
\]

Indeed these conditions say exactly that the letters before and after the chosen \(k\)th letter can be embedded strictly to the left and strictly to the right. The two greedy scans compute the maximum feasible prefix and suffix lengths, so they lose no occurrence. In addition, \(C\) can cover \(S\) only if \(C[0]=S[0]\) and \(C[m-1]=S[n-1]\), because an occurrence containing an endpoint must use it as its corresponding endpoint. The function `subsequence_cover` in `check.py` implements this exact predicate.

**2. Complete finite set of possible shortest covers.** Subsequence covers are transitive: if \(D\) s-covers \(C\) and \(C\) s-covers \(S\), compose the embeddings to see that \(D\) s-covers \(S\). Thus each shortest s-cover is *s-primitive*: it has no strictly shorter s-cover. Any word containing adjacent equal symbols is not s-primitive (replace the factor `aa` by `a` and keep the prefix/suffix of the original word to construct a shorter cover). More generally, if a factor has a shorter s-cover then so does its surrounding word, by the same prefix/suffix extension argument.

Enumerate, for lengths \(1\) through \(9\), all ternary words with no adjacent equal letters. Retain a word precisely when none of the previously retained shorter s-primitive words s-covers it, using the exact predicate from Step 1. By transitivity this tests primitivity without omissions: if any shorter cover exists, a shortest such cover is s-primitive and therefore already retained. This finite enumeration produces the following numbers of s-primitive words for lengths \(1\) through \(9\):

\[
3,\ 6,\ 12,\ 18,\ 30,\ 36,\ 30,\ 12,\ 0.
\]

The zero at length \(9\) and the factor extension lemma imply there are no longer ternary s-primitive words. Hence every shortest ternary s-cover is among the explicitly enumerated \(147\) candidates of lengths at most \(8\). This independently reproduces the published length-eight bound; the candidate-generation loop is a finite exhaustive proof, not a sample.

**3. Exact least length and the six extremal words.** For every \(1\le n\le11\), enumerate all \(3^n\) words and test every s-primitive candidate compatible with its endpoints and with length at most \(n\). Select *all* candidates attaining the minimum feasible length. Steps 1 and 2 guarantee that this finds exactly all shortest covers. The numbers of texts with more than one shortest cover, at lengths \(1,2,\ldots,11\), are exactly

\[
0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 6.
\]

The six recorded texts and their two length-six covers are explicitly listed in `check_output.txt`. They coincide with the six distinct alphabet permutations of the representative. This completes both the least-length proof and the complete labeled classification.

## Verification

Execute `python3 check.py` from the directory containing this result. The program uses only the standard library, performs the full \(3^n\) enumeration through length \(11\), and asserts the exact primitive counts and six witnesses. To guard against errors in the greedy predicate, it independently enumerates all index-tuple embeddings for \(127530\) small pattern/text pairs and checks agreement with the greedy predicate; it separately checks both covers and excludes *every* length-at-most-five candidate for each exceptional word by explicit index-tuple enumeration. The full captured output is `check_output.txt`, ending `VERIFY_OK`. These independently checked finite ranges are auxiliary safeguards; the proof of exhaustive completeness rests on the quantified finite loops and Steps 1–3.

## Relationship to prior work

Crochemore, Lecroq, and Rytter's 2025 text-algorithm problem collection, Problem 126, defines s-covers, notes that distinct shortest s-covers can occur, and states that the maximum ternary s-primitive length is eight; it gives no smallest ternary nonuniqueness length or complete length-eleven classification [1]. Charalampopoulos and coauthors [2] develop general cover algorithms and exhibit a **four-symbol**, length-\(15\) word with two shortest s-covers (Section 7), while proving the ternary s-primitive bound in Section 3. Their cited earlier SPIRE 2022 conference version is acknowledged; this result does not claim the s-cover notion, the length-eight bound, or nonuniqueness in general. The new assertion is the sharp first ternary nonuniqueness threshold \(11\), together with all six shortest examples and their cover pairs.

## Limitations

The theorem is a **finite sharp cutoff** for the first occurrence of nonuniqueness; it does not count ambiguous words at every greater length, nor bound their numbers of distinct shortest covers. The classification relies on an executable finite exhaustive proof rather than a short hand enumeration. Literature comparison was based on the accessible full 2025 expository problem and 2025 expanded article plus targeted searches; an equivalent result in unindexed or previously published work remains possible. No independent scientific audit is claimed.

## References

[1] M. Crochemore, T. Lecroq, W. Rytter, *25 Additional Problems—Extension to the Book "125 Problems in Text Algorithms"*, arXiv:2507.05770, first submitted 2025-07-08, Problem 126 (pages 1–3). https://arxiv.org/abs/2507.05770

[2] P. Charalampopoulos, S. P. Pissis, J. Radoszewski, W. Rytter, T. Waleń, W. Zuba, *Subsequence Covers of Words*, Theoretical Computer Science 1041 (2025), 115216, Sections 2, 3, and 7; earlier conference version SPIRE 2022. https://arxiv.org/abs/2509.05827 ; https://doi.org/10.1016/j.tcs.2025.115216
