# Two curling-number outputs for all extremal ternary simultaneous overlap-free words

## Finding

Let \(\Sigma=\{0,1,2\}\). Among the length-\(84\) words \(w\in\Sigma^{84}\) for which both \(w\) and its direct-prefix curling-number transform \(C(w)\) are overlap-free, the transform \(C(w)\) takes **exactly two distinct values**:

```
112112212112122112212112211212211221211212212112211212211221211221121221211212211211
112112212112122112212112211212211221211212212112211212211221211221121221211212211212
```

These two outputs coincide in their first \(83\) positions and differ only in their last symbol. Exactly \(4032\) labeled inputs yield the output ending in \(1\), and exactly \(2016\) yield the output ending in \(2\). Thus every extremal input has the same square-suffix signature through its first \(83\) prefixes. The previously established maximum source length \(84\) and total count \(6048\) are not claimed as new.

## Assumptions and scope

An overlap is a factor \(axaxa\), where \(a\) is one letter and \(x\) may be empty. The curling number \(\kappa(u)\) of a nonempty finite word \(u\) is the maximum integer \(k\ge1\) for which \(u=yz^k\) for some possibly empty \(y\) and nonempty \(z\). The direct-prefix transform is \(C(w)[i]=\kappa(w[0..i])\) for \(0\le i<|w|\). The ternary alphabet is labeled, and its symbols are not quotient-identified in the counts.

## Proof

**Prefix recurrence.** Any overlap newly formed when a letter is appended must end at that last letter. For a prefix of length \(n\), it is therefore enough to examine each suffix of length \(2p+1\), \(1\le p\le\lfloor(n-1)/2\rfloor\), and reject the extension precisely when the two length-\(p+1\) portions starting at the beginning of that suffix and at offset \(p\) agree. This test is equivalent to the presence of a suffix \(axaxa\). An overlap-free word is cubefree, so its curling number belongs to \(\{1,2\}\); it equals \(2\) if and only if a nonempty square is a suffix. Thus the next symbol of \(C(w)\) is computed by checking all equal consecutive suffix blocks. The transform is itself prefix-compatible, so rejecting an extension upon forming an overlap in either source or transform loses no valid longer word.

**Alphabet normalization.** Relabeling all source symbols by any permutation preserves source equality tests and curling numbers. Each word has a unique representative in which the first new symbol is \(0\), the next unseen symbol is \(1\), and the third unseen symbol is \(2\). To enumerate these representatives, an admissible prefix whose symbols lie in \(\{0,\ldots,k-1\}\) is extended using just the symbols \(0,\ldots,\min(k,2)\). This is exhaustive modulo relabeling, including words using fewer than three letters.

**Finite exhaustion.** The complete recurrence in `verify_canonical.py` enumerates \(1008\) canonical admissible sources at length \(84\), all using exactly three letters. Their transform-output frequencies are \(672\) and \(336\) for the two explicitly printed outputs. Each canonical source corresponds to exactly \(3!=6\) labeled sources and the transform is permutation-invariant. Hence the labeled frequencies are \(4032\) and \(2016\), totaling \(6048\), and there are exactly two images. The enumerator finds no admissible word of length \(85\), corroborating the source's known sharp length. Independently, `verify_full.cpp` performs an unrestricted labeled-alphabet breadth-first search and computes each curling number from its defining maximal suffix-power test, obtaining the same images and frequencies. The programs enumerate *all* admissible words at the stated lengths, not samples. Since the two printed transforms have a common \(83\)-character prefix and distinct last symbols, the claimed rigidity follows.

## Verification

Run `python3 verify_canonical.py` and `c++ -O2 -std=c++17 verify_full.cpp -o verify_full && ./verify_full`. Expected stdout/stderr observations are recorded in `canonical_output.txt` and `full_output.txt`. The independent enumeration through length \(85\), image lengths, exact frequencies, and agreement of all but the last transform symbol can be reproduced from those files. The full program directly checks suffix powers without relying on the shortcut that every curling number is \(1\) or \(2\).

## Relationship to prior work

Caveney, Dong, and Shallit (first public version \(2026\)-\(08\)-\(16\), arXiv:2608.15670v1), Theorem 7, already establish that the maximum length is \(84\) and that \(6048\) labeled words achieve it; they exhibit one input and its transform. Section 2.3 and Appendix B describe exhaustive prefix search and checks of published witnesses. The published theorem supplies the domain cardinality, but does not give the complete image of the transform or its two unequal fiber sizes. The present claim is specifically that output-image classification. The classical curling-number references define the map but do not supply this restricted length-\(84\) image census.

## Limitations

The theorem concerns **only** the fixed ternary alphabet and source words of the established extremal length \(84\). It does not classify the \(6048\) input words individually, nor characterize transform fibers at other lengths or over other alphabets. The proof is an exhaustive finite calculation supported by two standalone checkers, not a closed-form noncomputational classification. The companion supplementary archive to the primary manuscript was not independently searched for an unpublished equivalent grouping, leaving a residual priority risk. An independent mathematical audit has not been performed.

## References

1. Geoffrey Caveney, Haoxuan Dong, Jeffrey Shallit, *Repetition Avoidance in Curling-Number Transforms*, arXiv:2608.15670v1, 16 August 2026, Theorem 7 and Appendix B. https://arxiv.org/html/2608.15670v1
2. F. J. van de Bult, D. Gijswijt, J. Linderman, N. J. A. Sloane, A. Wilks, *A slow-growing sequence defined by an unusual recurrence*, Journal of Integer Sequences 10 (2007), Article 07.1.2 (for the original curling-number setting).
