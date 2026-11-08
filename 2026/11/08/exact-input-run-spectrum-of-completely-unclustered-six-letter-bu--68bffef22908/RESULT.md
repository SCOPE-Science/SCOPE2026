# Exact input-run spectrum of completely unclustered six-letter Burrows–Wheeler images

## Finding

Let \(q\ge1\) be an integer and let \(\Sigma_q=\{0<1<\cdots<q-1\}\). For a primitive necklace \([u]\) of length six, let \(\rho_\circ(u)\) count unequal cyclically adjacent letter pairs, and let \(\operatorname{BWT}([u])\) be the last column of the lexicographically sorted array of its six cyclic rotations. Let \(E_{q,r}\) be the number of such necklaces whose BWT has six ordinary runs (every two consecutive output symbols differ) and whose input has \(r\) cyclic runs.

The **complete input-run spectrum** is

\[
\begin{aligned}
E_{q,4}&=5\binom q3+14\binom q4,\\
E_{q,5}&=44\binom q4+72\binom q5,\\
E_{q,6}&=\binom q3+20\binom q4+108\binom q5+120\binom q6,\\
E_{q,r}&=0\qquad(r\notin\{4,5,6\}).
\end{aligned}
\]

Here \(\binom qt=0\) for \(t>q\). In particular, among all completely unclustered length-six BWT images, the exact number attaining the exceptional minimum of four input cyclic runs is \(5\binom q3+14\binom q4\). Such an extremizer uses **only three or four distinct symbols**. With \(T_q=\sum_r E_{q,r}\), the fraction attaining four input runs obeys

\[
\frac{E_{q,4}}{T_q}=\frac{7}{2q^2}+O(q^{-3})\qquad(q\to\infty).
\]

## Assumptions and scope

The alphabet is ordered, and the BWT uses sorted **cyclic rotations**, not an end-marker convention. A necklace is counted once modulo rotation, not once per linear representative. Its primitivity means that all six rotations differ. An output is completely unclustered when adjacent positions in the linear last column differ; no cyclic final-to-first condition is imposed on that output. We count all primitive necklaces, not just those using every letter of \(\Sigma_q\). The empty alphabet case is excluded.

## Proof

**Step 1: Exhaustive finite reduction.** A length-six word uses some number \(t\) of distinct letters, with \(1\le t\le6\). If those letters are the increasing \(t\)-element subset of \(\Sigma_q\), replace them in order by \(0,1,\ldots,t-1\). This operation preserves lexicographic comparisons, primitive necklaces, the BWT, and both run counts. Conversely, every accepted word over the normalized \(t\)-letter alphabet using all \(t\) letters has exactly \(\binom qt\) order-preserving lifts to \(\Sigma_q\). Thus it suffices to enumerate normalized primitive necklaces for \(1\le t\le6\).

**Step 2: Fully exhaustive finite certificate.** For each \(t\), enumerate the \(t^6\) length-six tuples over \(\{0,\ldots,t-1\}\); retain only those using all \(t\) letters. Of the six cyclic rotations, retain the lexicographically least tuple exactly when all rotations are distinct. These are precisely the primitive necklaces, each once. Sort its six rotations and read the last letter of each to compute the BWT. Discard it if two consecutive last-column entries agree. Count unequal cyclically adjacent input letters to obtain \(r\). There are no probabilistic choices or unbounded searches in this procedure.

The complete nonzero counts, grouped by the partition of six formed by the positive letter multiplicities of the input, are:

| Distinct letters \(t\) | Multiplicity partition | \(r=4\) | \(r=5\) | \(r=6\) |
|:--:|:--:|--:|--:|--:|
| 3 | \((3,2,1)\) | 4 | 0 | 0 |
| 3 | \((2,2,2)\) | 1 | 0 | 1 |
| 4 | \((3,1,1,1)\) | 0 | 8 | 0 |
| 4 | \((2,2,1,1)\) | 14 | 36 | 20 |
| 5 | \((2,1,1,1,1)\) | 0 | 72 | 108 |
| 6 | \((1,1,1,1,1,1)\) | 0 | 0 | 120 |

Every omitted partition has zero admissible necklaces. Summing across partitions gives exactly \(384\) normalized admissible necklaces, with the \((t,r)\) counts \((3,4):5\), \((3,6):1\), \((4,4):14\), \((4,5):44\), \((4,6):20\), \((5,5):72\), \((5,6):108\), and \((6,6):120\). The full list of all \(384\) last columns and their unique lexicographically least input rotations is given in `census.tsv`. The exact, executable enumerator is `rotation_enumerator.py`.

**Step 3: Independent completeness check.** Alternatively, for each candidate normalized BWT last column \(L\), form its stable last-to-first permutation: its \(i\)-th occurrence of a symbol is mapped to the position of that occurrence in the sorted first column \(F=\operatorname{sort}(L)\). This is a six-cycle precisely for a primitive-necklace BWT image. Furthermore, \(\rho_\circ(u)=\#\{i:F_i\ne L_i\}\): each sorted-rotation row compares the letter at its starting position with the letter immediately preceding it cyclically, so the mismatches count all input cyclic transitions once. The independent `cycle_enumerator.py` enumerates all candidate last columns, tests this permutation criterion, and reproduces exactly the same eight nonzero histogram cells. Both methods are checked by `verify.py`, which also compares the complete normalized census.

**Step 4: Lift to every alphabet.** Multiply each fixed \((t,r)\) count by \(\binom qt\), as proved in Step 1, and sum. This yields the stated formulas for every positive \(q\), without extrapolating from finitely many alphabet sizes. The four-run cases occur only for \(t=3,4\), proving the alphabet-support restriction. The asymptotic ratio follows from the leading terms \(E_{q,4}\sim(7/12)q^4\) and \(T_q\sim(1/6)q^6\).

## Verification

Run `python3 verify.py` with `cycle_enumerator.py`, `rotation_enumerator.py`, and `census.tsv` in the same directory. The verifier independently enumerates valid normalized BWT images and primitive necklace representatives, checks exact set equality and all input-run counts, verifies the ten multiplicity-partition cells and all \(384\) census rows, and directly enumerates labeled outputs for \(q\le4\) to check the lifting formulas. Expected result: `BWT_LENGTH_SIX_CENSUS_OK 384 8_HISTOGRAM_CELLS 10_PARTITION_CELLS`. The table is a finite exhaustive certificate, not a sample.

## Relationship to prior work

Kumallagov (arXiv:2606.01267v1, publicly submitted May 31, 2026), Proposition 6.1, establishes the exceptional minimum \(U_q(6)=4\) and gives individual witnesses, with Appendix A providing an algorithm to rule out three-run sources. That minimum alone does not specify how many such sources exist, how their input run counts are distributed, or which input multiplicity partitions occur. The present statement supplies the complete enumeration at that exceptional boundary. Fici, Gabory, Romana and Sciortino (arXiv:2508.20879; CPM 2026) prove existence in every length and give general lower counts, not this exact length-six input-run enumerator. A targeted literature and record comparison found no stronger result implying the displayed coefficient table; historical priority is not independently certified.

## Limitations

This is a complete classification **only at length six**. It does not classify completely unclustered BWT images at other lengths, nor describe their analogous generating functions. The exact counts follow from an exhaustively proved finite search space and reproducible programs; no claim is made of an independent audit or a mechanized theorem-prover certificate. Unindexed equivalent enumerations may exist.

## References

- D. Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267v1, May 31, 2026. https://arxiv.org/abs/2606.01267
- G. Fici, E. Gabory, G. Romana, M. Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, arXiv:2508.20879, August 28, 2025; published as *Totally Unclustered BWT Images of Any Length over Non-Binary Alphabets*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.13. https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.13/LIPIcs.CPM.2026.13.html
