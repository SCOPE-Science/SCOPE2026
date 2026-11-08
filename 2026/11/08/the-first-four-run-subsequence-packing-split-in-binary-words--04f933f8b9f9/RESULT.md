# The first four-run subsequence-packing split in binary words

## Finding

Let \(c_p(w)\) be the number of indexed scattered-subsequence occurrences of a fixed binary pattern \(p\) in a finite binary word \(w\), and let \(M_{n,p}=\max_{|w|=n}c_p(w)\). Every *nonalternating* binary word of length five with four runs is equivalent, under reversal and bit complementation, to exactly one of `00101` and `01101`. These representatives have the complete shortest four-length maximum and optimizer-multiplicity profiles

| \(n\) | \(M_{n,\mathtt{00101}}\) | number of maximizers | \(M_{n,\mathtt{01101}}\) | number of maximizers |
|---:|---:|---:|---:|---:|
| 5 | 1 | 1 | 1 | 1 |
| 6 | 3 | 1 | 3 | 1 |
| 7 | 6 | 5 | 6 | 4 |
| 8 | 15 | 1 | 12 | 7 |

At length eight the unique `00101`-maximizer is `00010101`, which has six runs, whereas every four-run word has at most twelve `00101` occurrences. For `01101`, length-eight maximizers include `00111001`, which has four runs. Therefore the two nonalternating four-run classes have the same maximal counts for lengths five through seven, but first separate at length eight. In addition the first class violates log-concavity of its packing-maxima sequence: \(M_{7,\mathtt{00101}}^2=36<45=M_{6,\mathtt{00101}}M_{8,\mathtt{00101}}\).

## Assumptions and scope

The ambient alphabet is the labeled binary alphabet \(\{0,1\}\). An occurrence is a strictly increasing five-tuple of positions, *not* a contiguous factor or a distinct subsequence value. A run is a maximal constant-letter block. The maximum and multiplicity assertions are for all words of length \(n\in\{5,6,7,8\}\), with no balance or run restriction. The claim of a first split concerns the two symmetry classes of nonalternating *five-letter four-run patterns*, not all patterns or all lengths. No all-length extremal formula is asserted.

## Proof

**Symmetry classification.** A four-run word of length five has run-length composition a permutation of \((2,1,1,1)\), and there are two choices for its first bit. Consequently there are exactly eight such words. Reversal and complementation generate two disjoint four-element orbits: `00101`, `10100`, `11010`, `01011`; and `01101`, `10110`, `10010`, `01001`. Reversal of both pattern and host, and simultaneous complementation of both, bijectively preserve occurrences and optimal words. It suffices to check the two displayed representatives.

**Finite exhaustive recurrence.** For a pattern \(p=p_1\cdots p_5\) and prefix \(w\), write \(D_j(w)\) for the count of embeddings of \(p_1\cdots p_j\) into \(w\), for \(0\le j\le5\). Initially \(D_0(\epsilon)=1\) and \(D_j(\epsilon)=0\) for \(j>0\). Appending \(c\in\{0,1\}\) gives, with \(D_0=1\),

\[
D_j(wc)=D_j(w)+\mathbf1_{c=p_j}D_{j-1}(w),\qquad 1\le j\le5.
\]

This identity partitions occurrences according to whether their final chosen position is the appended position. Binary branching from the empty prefix generates *every* word of lengths five through eight, exactly once. At every leaf the final coordinate is \(c_p(w)=D_5(w)\). Taking the maximum and counting all leaves attaining it proves the table; the finite exhaustive traversal and an independent five-position-combination checker are given in `verify.py`. The traversal inspects \(2^5+2^6+2^7+2^8=480\) words per representative and is exhaustive by construction, rather than a sample of longer words.

**Explicit equality cases.** At length seven the five maximizers for `00101` are `0000101`, `0001001`, `0001011`, `0001101`, `0010101`; the four for `01101` are `0011101`, `0111001`, `0111011`, `0111101`. At length eight, `00101` has only `00010101` with fifteen embeddings. The seven maximizers for `01101` are `00111001`, `00111011`, `00111101`, `01110011`, `01110101`, `01111001`, `01111011`, all with twelve embeddings. The same exhaustive recurrence shows that the maximal value among length-eight words with at most four runs is twelve for `00101`. Independently, any such host containing `00101` must have exactly four runs in order \(0^a1^b0^c1^d\), where \(a\ge2\), \(b,c,d\ge1\), \(a+b+c+d=8\). Its occurrence count is exactly \(\binom a2 bcd\), whose maximum over these finite positive compositions is twelve; words with fewer or differently oriented runs contain no instance. This proves the sharp run boundary without relying solely on the exhaustive-word table.

The strict inequality \(36<45\) and the first numerical divergence at eight follow directly from the displayed exact maxima.

## Verification

Run `python3 verify.py` from the directory containing the file. The standalone checker (i) enumerates both symmetry orbits, (ii) recursively enumerates every binary word through length eight with the occurrence dynamic program, (iii) independently computes the occurrence count by choosing all five positions, (iv) compares exact maxima, multiplicities, and all length-seven/eight maximizers, (v) checks the four-run bound by direct positive-composition enumeration, and (vi) checks the log-concavity inequality. The recurrence is a mathematical proof of finite exhaustiveness; checks at greater lengths, if any, are not used as evidence for the statement.

## Relationship to prior work

Menon and Singh, *Subsequence frequency in binary words* (first posted 2023-06-13), define exactly the same occurrence statistic and show that at most three-run patterns admit run-preserving optimizers and log-concave packing maxima (Proposition 4.1, Corollary 4.2, Theorem 4.17). Their Section 4 explicitly notes that four-or-more-run **alternating** patterns can have extra-run optimizers, so an alternating counterexample is not new. The present finite classification concerns the two minimal **nonalternating** four-run classes, their first divergence, and their distinct optimizer profiles, none of which is stated by those general results. Burstein, Hästö and Mansour's *Packing patterns into words* develops general packing concepts and related asymptotic constructions; the inspected text does not state this specific two-class finite maximum/multiplicity profile. These comparisons are limited to checked sources and are not a universal novelty certification.

## Limitations

Only the four specified host lengths and the length-five nonalternating four-run patterns are classified. An all-length law, stability of maximizing run configurations at longer lengths, and a classification for longer four-run patterns remain open here. The result does not assert that the maximum itself is always attained by a four-run host. Other unindexed tables or equivalent finite calculations may already contain the same numerical profile. Independent audit is not performed.

## References

1. K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870v1, publicly posted 13 June 2023. https://arxiv.org/html/2306.07870v1
2. A. Burstein, P. Hästö and T. Mansour, *Packing patterns into words*, arXiv:math/0212343. https://arxiv.org/abs/math/0212343
