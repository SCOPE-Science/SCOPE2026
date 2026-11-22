# Complete optimal census for four-symbol permutation comma-free codes

## Finding
Let \(\Sigma=\{0,1,2,3\}\), and let \(\mathcal P\) be the set of all \(24\) length-four words in which each symbol occurs exactly once. A code \(C\subseteq\mathcal P\) is *comma-free* if, for every \(u,v\in C\) (also when \(u=v\)) and every shift \(k\in\{1,2,3\}\), the crossed factor \(u_{k+1}\cdots u_4v_1\cdots v_k\) does not belong to \(C\). Then:

1. The largest possible code size is \(6\).
2. Exactly \(2872\) labeled six-word codebooks attain that size.
3. Under the group of all \(24\) alphabet relabelings together with optional reversal of every word, the \(2872\) optimal codebooks form exactly \(73\) equivalence classes, comprising four orbits of size \(8\), two of size \(16\), seventeen of size \(24\), and fifty of size \(48\).
4. Exactly \(32\) of the optimal codebooks additionally have the stronger non-overlap property: for all \(u,v\in C\) and \(k\in\{1,2,3\}\), the length-\(k\) prefix of \(u\) differs from the length-\(k\) suffix of \(v\).

The accompanying `ORBIT_REPRESENTATIVES.tsv` gives exactly one canonical member of every equivalence class and its orbit size. The decimal figures are counts of **sets** of words, not ordered lists. The relabeling action preserves the four specified alphabet labels; the codebooks are considered different unless the stated equivalence relation is invoked.

## Assumptions and scope
The alphabet has exactly four distinguishable letters and each allowable codeword contains all four letters once. This is the constant-composition vector \((1,1,1,1)\), sometimes called the permutation-word layer. No reverse-complement closure, Hamming-distance requirement, or stronger prefix-suffix non-overlap is imposed in items 1–3. Ordinary comma-freeness is weaker than non-overlap. The only equivalences used in the orbit census are the permutations of the four alphabet names and a simultaneous coordinate reversal, not arbitrary coordinate permutations.

## Proof
**Capacity and existence.** The \(24\) permissible words partition into six cyclic-rotation classes of size four. Each comma-free code contains at most one representative from each class: if it contained a word \(w\) and one of its nontrivial cyclic rotations, the crossed factor of the concatenation \(ww\) at that shift would be a prohibited codeword. Hence \(|C|\le6\). The six words `0123`, `0132`, `0213`, `0231`, `0312`, `0321` all start in `0` and each remaining letter occurs exactly once in the suffix. Every crossed length-four window of a concatenation of two of these words starts in one of `1`, `2`, `3`, and therefore is not in the code. This attains six.

**Exact finite census.** Choose one representative from each of the six cyclic-rotation classes. There are exactly \(4^6=4096\) such unordered six-word sets; every potential optimum appears once, so this is exhaustive. Check all \(6^2\cdot3=108\) ordered crossed-window tests per set, including equal endpoint words. The direct finite enumeration in `verify_direct.py` counts exactly \(2872\) sets passing all tests. As an independent formulation, `verify_hypergraph.py` forms the complete family of forbidden subsets \(\{u,v,u_{k+1}\cdots u_4v_1\cdots v_k\}\), where the crossed word is a permutation. It then enumerates the same \(4096\) choices using forbidden-hyperedge containment, without using the direct comma-free predicate. It independently obtains \(2872\). These are complete finite enumerations, not statistical sampling or an inference from initial sequence terms.

**Equivalence classes.** Every alphabet permutation and simultaneous reversal preserves comma-freeness. The group has order \(24\cdot2=48\). The direct checker partitions the \(2872\) optima by complete group orbits, yielding \(73\) orbits with size multiplicities \(\{8:4,16:2,24:17,48:50\}\); the orbit-weighted total is \(4\cdot8+2\cdot16+17\cdot24+50\cdot48=2872\). An independent Burnside calculation enumerates fixed codes for all \(48\) group elements and obtains a fixed-point sum of \(3504\), so the number of orbits must be \(3504/48=73\). The fixed-point counts by alphabet-permutation cycle type and reversal flag are reproduced by `verify_hypergraph.py`. The attached canonical representative table also permits reconstructing the full optimum set by applying the \(48\) transformations to its \(73\) rows.

**Stronger non-overlap refinement.** Apply the prefix-suffix inequalities at all three proper lengths to every optimal six-word set. Exactly \(32\) satisfy the stronger restriction. This check is also exhaustive over the finite universe of \(2872\) sets and must not be confused with the main comma-free count.

## Verification
Run from the directory containing the four files:

```sh
python3 verify_direct.py
python3 verify_hypergraph.py
```

Both programs require only the Python 3 standard library and contain all finite candidate-generation details. The first reconstructs all six rotation classes, verifies the \(4096\)-case direct census and full orbit partition, checks all \(73\) tabulated representatives, and computes the \(32\)-code non-overlapping refinement. The second independently generates forbidden hyperedges, enumerates six-choice solutions, and calculates all \(48\) Burnside fixed-point contributions. Exact assertions enforce the stated integers. The source is small enough to inspect as a certificate; neither program relies on external tables or hidden optimization output.

## Relationship to prior work
Classical comma-free coding uses the same crossed-window definition and the rotation-class upper bound. Churchill's 2009 open-access treatment [1], including its length-four constructions and appendix, studies general and self-reflective codebooks without the present all-distinct-composition optimum census. Windsor's 2023 study [2] computes unrestricted comma-free maxima using automated methods: its companion public repository reports \(W(4,4)=57\) over the full \(4^4\)-word universe, rather than the six-word constant-composition layer here. Its accessible article abstract and repository overview do not establish the enumeration of \(2872\) restricted optimizers or \(73\) symmetry classes. The distinction is one of exact objects and quantifiers, not merely different terminology. The closely related published comparisons and available indexed mathematical findings were searched, but absence from search results does not prove historical novelty.

## Limitations
These results concern exactly one fixed alphabet size, one fixed word length and one fixed composition vector; they do not give an all-alphabet theorem or a general asymptotic. Counting is proved by small, transparent, exhaustive finite programs, rather than a symbolic closed formula. The stronger non-overlap refinement is only the \(32\)-case count and is not a classification under another symmetry group. The 2023 paper was available via abstract and an author-maintained code/repository description, not a fully readable primary article or preprint; an unindexed equivalent finite table remains a historical-priority risk. No independent external mathematical audit has been performed.

## References
[1] A. L. Churchill, *Restrictions and Generalizations on Comma-Free Codes*, Electronic Journal of Combinatorics **16** (2009), R25; published 20 February 2009. https://doi.org/10.37236/114 . Open PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r25/pdf/ .

[2] A. A. Windsor, *Computer-Aided Constructions of Commafree Codes*, Journal of Automated Reasoning **67** (2023), article 12. https://doi.org/10.1007/s10817-023-09662-6 . Author's public code and paper listing: https://github.com/aaw/commafree .

[3] S. W. Golomb, B. Gordon, and L. R. Welch, *Comma-Free Codes*, Canadian Journal of Mathematics **10** (1958), 202–209. https://doi.org/10.4153/CJM-1958-023-9 .
