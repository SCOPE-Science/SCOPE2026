# The shortest overlap-free nine-square binary words are unique up to complementation

## Finding
A binary word is *overlap-free* when it has no factor of the form \(axaxa\), where \(a\in\{0,1\}\) and \(x\) is any binary word, possibly empty. A *square* is \(uu\) for nonempty \(u\). Among overlap-free binary words admitting a concatenation into **nine nonempty squares**, the shortest length is exactly \(48\). There are exactly **two** length-\(48\) words, related by exchanging all zeros and ones:

`001001101001011010011001011001101001011010011011`

`110110010110100101100110100110010110100101100100`

Each has exactly one nine-square factorization, with factor lengths \((6,4,4,4,12,4,4,4,6)\). This refines the existence of a nine-square overlap-free word established by Shallit (2026); its published length-\(48\) witness already supplies the matching upper bound, but not this minimum-length and uniqueness classification.

## Assumptions and scope
Words are finite, over exactly the labeled alphabet \(\{0,1\}\), with nonempty square roots. The nine square factors are contiguous, in order, and exhaust the word; no restriction on their root lengths is imposed. Overlaps mean factors \(axaxa\) with \(x\) allowed empty (including cubes of one letter). The classification concerns literal words, not factorizations up to symmetry; its two optimizers form one orbit under global complementation. It does not classify longer nine-square words.

## Proof
The argument is an exact finite exhaustive proof using the prefix-tree recurrence reproduced in `verify_shortest.py`. First, a binary word \(v\) of length \(n\) is overlap-free if and only if its \((n-1)\)-letter prefix is overlap-free and there is no positive integer \(p\) with \(2p+1\le n\) such that the last \(2p+1\) letters have period \(p\). Indeed, any new forbidden factor in a one-letter extension must end at the newly appended final letter, while a length-\(2p+1\) period-\(p\) factor is exactly an overlap \(axaxa\) with \(|x|=p-1\). Testing all possible periods is therefore necessary and sufficient; no other words are discarded.

For any word \(v\) of length \(n\), define \(B_v(0)=0\) and, for \(1\le j\le n\), let \(B_v(j)=-\infty\) unless some prefix ending at \(j\) is a concatenation of nonempty squares. Precisely,
\[
B_v(j)=\max_{\substack{1\le h\le\lfloor j/2\rfloor \\ v[j-2h:j-h]=v[j-h:j]}}\bigl(B_v(j-2h)+1\bigr),
\]
where a maximum over an empty set equals \(-\infty\). Here slices use zero-based, left-closed/right-open indexing. Every nonempty square at the end of a square factorization has length \(2h\), so removing that last square yields an earlier square factorization, and conversely every candidate in the maximum appends a valid square. Induction on \(j\) proves that \(B_v(j)\) is the exact maximum number of square factors in any full factorization of the first \(j\) letters (and \(-\infty\) if none exists).

Starting from the sole empty word, exhaustively extend each surviving overlap-free prefix by **both** binary symbols, discarding extensions exactly by the preceding period test, and compute \(B_v(n)\) by this recurrence. Induction on \(n\) shows that the generated layer is **all** overlap-free words of length \(n\), with no omissions. The standalone verifier enumerates every such layer for \(1\le n\le48\). None of the layers \(1,\ldots,47\) contains a word with \(B_v(n)\ge9\); layer \(48\) contains precisely \(416\) overlap-free words and exactly two have \(B_v(48)\ge9\), the two words displayed above. This proves the lower bound and complete equality classification. A separate explicit recursive partition test counts exactly one factorization into nine squares for each of the two words, giving the factor-length vector. Thus the theorem is complete.

## Verification
Run `python3 verify_shortest.py` with a standard Python 3 interpreter. It generates all overlap-free binary words at lengths \(1\) through \(48\) by complete two-child extension; tests every possible new overlap; evaluates the full square-decomposition dynamic programming recurrence; confirms that the only two nine-square words through length \(48\) are the stated complements; and exhaustively counts each optimizer's nine-square partitions. The final line is `NINE_SQUARES_MIN_LENGTH_AND_UNIQUENESS_OK`. Independently run `python3 verify_bits.py`; it uses integer bit masks and a separate square-decomposition recurrence, obtaining `INDEPENDENT_INTEGER_OVERLAP_CHECK_OK`. The recorded first-verifier output is in `verify_shortest.log`.

This is a **finite mathematical proof by an exhaustive, explicitly justified enumeration**, not evidence for an unexamined infinite generalization. The proof's exhaustive domain includes all binary words of lengths up to \(48\), compactly searched by prefix pruning. Integer and string representations offer an independent implementation cross-check.

## Relationship to prior work
Jeffrey Shallit, "Ten Squares Force an Overlap", arXiv:2605.28570v1 (first public 2026-05-27), Sections 1–3, especially Theorem 1 and its explicit nine-square witness. Shallit proves that no binary overlap-free word is a product of ten nonempty squares and explicitly displays a length-\(48\) example of nine squares. That result supplies the existence bound, but does **not** state that \(48\) is the minimum possible length or that the minimum-length words are unique up to complement. The present claim is a structural refinement of the extremal nine-square case, not a rediscovery of its count bound. A search of available word-combinatorics literature and mathematical research records did not identify the same minimum-length-and-uniqueness statement. A failed search alone is not a proof of novelty.

## Limitations
The claim is exact only for binary words and exactly nine square factors. It does not classify arbitrary lengths or larger alphabets and does not offer a purely handwritten structural lower-bound proof independent of the exhaustive finite recurrence. Exhaustiveness hinges on the stated prefix and factorization recurrences, which are explicit and independently reproducible. A pre-existing implicit equivalent enumeration cannot be entirely excluded; independent expert validation has not been performed.

## References
- Jeffrey Shallit, "Ten Squares Force an Overlap", arXiv:2605.28570v1 (first public 2026-05-27), Sections 1–3, especially Theorem 1 and its explicit nine-square witness.
- MSC2020, 68R15, Combinatorics on words (Mathematical Reviews / Zentralblatt classification, https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=68R15).
