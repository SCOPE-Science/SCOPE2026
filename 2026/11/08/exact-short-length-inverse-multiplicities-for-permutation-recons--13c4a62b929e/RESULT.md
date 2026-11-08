# Exact short-length inverse multiplicities for permutation reconstruction from ordered differences

## Finding

For every integer \(n\ge 2\), let \(S_n\) be the permutations of \(\{1,\ldots,n\}\). Define the *ordered absolute-difference record*
\[
\Delta(\pi)=\bigl(|\pi_2-\pi_1|,\ldots,|\pi_n-\pi_{n-1}|\bigr)
\]
and its inverse multiplicity \(r_n(d)=|\{\pi\in S_n:\Delta(\pi)=d\}|\). Let \(R_n=\max_d r_n(d)\), maximizing only over realizable records.

The exact maxima at lengths \(2\) through \(10\) are
\[
(R_2,R_3,R_4,R_5,R_6,R_7,R_8,R_9,R_{10})=(2,2,6,4,8,8,30,12,24).
\]
There are respectively \(1,3,1,6,3,5,1,20,5\) maximizing ordered records. Thus the worst inverse multiplicity falls from \(30\) to \(12\) as the length increases from \(8\) to \(9\), then returns to \(24\) at length \(10\).

At length \(8\), the unique maximizing record is
\[
d_*=(4,2,4,1,4,2,4),\qquad r_8(d_*)=30.
\]
The \(30\) permutations with this record form exactly eight orbits under value-complementation \(c(\pi)_i=9-\pi_i\) and positional reversal, with orbit sizes \(4,4,4,4,4,4,4,2\). In particular, there are \(15\) reconstructions modulo complementation.

## Assumptions and scope

The order of differences is part of the observation; its entries may repeat. Permutations are labeled lists, not cyclic words, and both a permutation and its value complement are counted as separate reconstructions. No graceful-permutation assumption is made. The theorem concerns exactly \(2\le n\le10\); it makes no assertion about the value of \(R_n\) for larger \(n\).

## Proof

**Exhaustive inverse classification.** The C++ verifier `verification/enumerate.cpp` begins with \((1,\ldots,n)\) and iterates `std::next_permutation` through all \(n!\) permutations, for each \(2\le n\le10\). By the standard lexicographic successor property, this lists every permutation exactly once. It encodes each adjacent-difference record as \(n-1\) consecutive base-16 digits. Since \(1\le|\pi_{i+1}-\pi_i|\le n-1\le9\), this encoding is injective for all lengths checked. A map accumulates the exact fiber cardinalities. Every realizable record appears because its defining permutation was enumerated; no unrealizable record can have a nonempty fiber. Thus the maximum map entry is exactly \(R_n\), and the number of entries attaining that maximum is exactly the maximizing-record count, not merely an observed lower bound. The verifier additionally checks \(\sum_d r_n(d)=n!\).

The exhaustive map produces the values and maximizing-record counts stated above. It finds \(15{,}788\), \(160{,}222\), and \(1{,}528{,}045\) realizable records at \(n=8,9,10\), respectively. The corresponding full fiber-size histograms are reproduced in `verification/enumerate.cpp` output. At length \(8\), decoding the sole maximizing base-16 key yields exactly \(d_*\), ruling out any other record with \(30\) preimages.

**Independent reconstruction check.** The Python verifier `verification/inverse_verify.py` re-enumerates the record-frequency maps using a different implementation and, for every maximizing record at lengths \(8,9,10\), independently reconstructs all permutations from each of the \(n\) possible initial values and every admissible choice of signed increments \(\pm d_i\), excluding repeated and out-of-range values. These are exactly all possible solutions: any solution determines its initial value and, because \(d_i>0\), the sign of every step; conversely a signed trajectory that visits every label once is a solution. The inverse search reproduces multiplicities \(30\), \(12\) for each of the twenty length-nine maxima, and \(24\) for each of the five length-ten maxima.

**Orbit classification and parity.** Complementation preserves every absolute difference and has no fixed permutation for \(n\ge2\), hence all fibers have even size. The record \(d_*\) is palindromic, so positional reversal also preserves its fiber. The Python checker explicitly forms each orbit under these two commuting involutions, verifies its four candidate images lie in the fiber, and removes each orbit once. The sizes consist of seven four-element orbits and one two-element orbit, accounting for all \(30\) solutions. This proves the classification without identifying fibers merely up to symmetry in the original count.

## Verification

From the directory containing the two source files, run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verification/enumerate.cpp -o enumerate
./enumerate
python3 verification/inverse_verify.py
```

Both programs terminate with `VERIFY_OK` when their exact assertions pass; neither requires a third-party solver or a downloaded data table. The C++ program verifies all nine finite maxima and the exact totals \(n!\), while the Python program independently checks the three largest lengths, direct inverse reconstruction, the parity property, and the length-eight symmetry orbit census. Both were executed successfully on the embedded source files.

## Relationship to prior work

Al-Turkistany posed the ordered difference-reconstruction question publicly on July 7, 2013 (MathOverflow question 135968). De Biasi's 2014 paper, *Permutation Reconstruction from Differences* (DOI:10.37236/4086; arXiv:1410.6396), defines this reconstruction problem and proves NP-completeness. Its Section 5 and conclusion do not provide the finite unrestricted maximum-fiber table or the unique length-eight extremal record. OEIS A398093, A398094 and A398095 study the *graceful* restriction, in which the ordered difference record contains each number from \(1\) through \(n-1\) exactly once. That condition excludes \(d_*\), with four occurrences of \(4\) and repeated occurrences of \(2\), and therefore does not determine this theorem. The exact classification here is subject to further historical-priority review.

## Limitations

The proof is exact finite exhaustive computation, not an all-length asymptotic or polynomial-time reconstruction algorithm. The statement uses ordered records; an unordered multiset of differences is a different problem. The observed nonmonotonicity need not describe any unknown later lengths. Independent mathematical and historical-priority audits have not been performed.

## References

- M. Al-Turkistany, *How hard is reconstructing a permutation from its differences sequence?*, MathOverflow, July 7, 2013, https://mathoverflow.net/questions/135968/how-hard-is-reconstructing-a-permutation-from-its-differences-sequence.
- M. De Biasi, *Permutation Reconstruction from Differences*, Electronic Journal of Combinatorics 21(4) (2014), P4.3, https://doi.org/10.37236/4086; https://arxiv.org/abs/1410.6396.
- OEIS A398093, *Number of distinct ordered difference sequences of graceful permutations*, https://oeis.org/A398093.
- OEIS A398094, *Reconstruction-multiplicity spectrum for graceful ordered difference sequences*, https://oeis.org/A398094.
- OEIS A398095, *First occurrence of graceful reconstruction multiplicities*, https://oeis.org/A398095.
