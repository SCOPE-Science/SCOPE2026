# Unique maximal minimal-absent factor of dyadic paperfolding prefixes

## Finding
Let \(p_1p_2\cdots\) be the regular binary paperfolding word, with \(p_i=0\) when the odd part of \(i\) is congruent to \(1\pmod4\), and \(p_i=1\) when it is congruent to \(3\pmod4\). For every integer \(k\ge5\), let \(W_k=p_1\cdots p_{2^k}\) and \(m=2^{k-2}\). Split \(W_k=ABCD\) into four blocks of length \(m\). Then \(D=B\), and **the only repeated length-\(m\) factor is \(B\), occurring exactly at zero-based positions \(m\) and \(3m\)**. Every length-\(m+1\) factor occurs exactly once.

The unique longest *minimal absent contiguous factor* is
\[
X_k=C_{m}\,B\,C_1,
\]
where \(C_j\) denotes the \(j\)-th symbol of \(C\). Its length is exactly \(m+2=2^{k-2}+2\). Thus \(X_k\) does not appear in \(W_k\), but all its proper contiguous factors do, and no other minimal absent factor has length \(m+2\) or more.

## Assumptions and scope
All words are linear, over the alphabet \(\{0,1\}\), with ordinary **contiguous** factors, not scattered subsequences and not cyclic factors. Occurrences are positional, indexed from zero. A word \(x\) is minimal absent in \(w\) when \(x\) is not a contiguous factor, while its length-\((|x|-1)\) prefix and suffix are factors; this implies every proper factor occurs. Only regular folding and exactly dyadic lengths \(2^k\), \(k\ge5\), are asserted. Complementing all bits leaves the theorem unchanged with the correspondingly complemented expression.

## Proof
**1. A uniform synchronization lemma.** If two length-\(2^r\) factors of the *infinite* paperfolding word are equal, for \(r\ge3\), their zero-based starts are congruent modulo \(2^{r+1}\). For \(r=3\), the paperfolding formula gives exactly the following two possible eight-symbol factors for each starting residue modulo \(16\); the two choices depend on the symbol at the unique index divisible by eight. All 32 strings in the table are different.

| Start \(\bmod16\) | Two possible factors |
|---:|---|
| 0 | `00100110`, `00100111` |
| 1 | `01001100`, `01001110` |
| 2 | `10011000`, `10011100` |
| 3 | `00110001`, `00111001` |
| 4 | `01100011`, `01110011` |
| 5 | `11000110`, `11100110` |
| 6 | `10001101`, `11001101` |
| 7 | `00011011`, `10011011` |
| 8 | `00110110`, `00110111` |
| 9 | `01101100`, `01101110` |
| 10 | `11011000`, `11011100` |
| 11 | `10110001`, `10111001` |
| 12 | `01100010`, `01110010` |
| 13 | `11000100`, `11100100` |
| 14 | `10001001`, `11001001` |
| 15 | `00010011`, `10010011` |

For the inductive step, equality of length-\(2^r\) factors with \(r\ge4\) implies their first eight symbols agree, so their starts have the same parity by the base case. Extract the globally even-indexed (one-based) positions from each factor. The extracted factors have length \(2^{r-1}\), are equal, and are again factors of the *same* paperfolding word, because \(p_{2i}=p_i\). Their zero-based starts are the integer halves of the original starts, rounded down. The induction hypothesis makes those half-starts congruent modulo \(2^r\); equal parity then gives original starts congruent modulo \(2^{r+1}\). This proves synchronization for all \(r\ge3\).

**2. Four-block structure.** Put \(m=2^{k-2}\). For \(1\le j<m\), the odd part of \(j+tm\) is the odd part of \(j\), for each \(t\in\{0,1,2,3\}\), except when \(j=m/2\), where the odd parts have opposite residues modulo four between \(t=0\) and \(t=1\), but agree between \(t=1\) and \(t=3\). Directly from the odd-part formula, \(A\) and \(B\) differ *only* at their one-based position \(m/2\), while \(A\) and \(C\) differ *only* at their final position \(m\); also \(D=B\). In particular \(A\ne C\), and the final symbols of \(A\) and \(C\) differ.

**3. Uniqueness of the long repeat.** Any two occurrences of a length-\(m\) factor within \(W_k\) begin in \([0,3m]\). The synchronization lemma at \(r=k-2\) implies that their starts differ by an integer multiple of \(2m\). Distinct starts therefore differ exactly by \(2m\); write them as \(u,u+2m\), with \(0\le u\le m\). At \(u=0\), these are the distinct blocks \(A,C\). For \(1\le u<m\), the first window crosses the final symbol of \(A\), and the second crosses the final symbol of \(C\), which differ, while their following symbols lie in equal blocks \(B,D\). At \(u=m\), both windows are \(B=D\). Hence the only repeated factor of length \(m\) is \(B\), occurring at exactly \(m\) and \(3m\). If any length-\(m+1\) factor repeated, its first \(m\) symbols would be \(B\); but the second occurrence of \(B\) ends at the end of \(W_k\), and the first is followed by \(C_1\). Thus no longer repeat is possible.

**4. Maximal absent obstruction.** For any finite word \(w\), every minimal absent word of length \(\ell\ge3\) has an interior factor of length \(\ell-2\) occurring **at least twice** in \(w\). Indeed, its prefix and suffix of length \(\ell-1\) both occur. If the interior occurred only once, its predecessor and successor from those occurrences would be adjacent, producing the purported absent word. Applying this to \(W_k\), no minimal absent word can have length exceeding \(m+2\). A minimal absent word at length \(m+2\) must have interior \(B\), the only repeated factor of length \(m\). The two occurrences of \(B\) have respective predecessors \(A_m\) and \(C_m\), which are different, and only the first has a successor, namely \(C_1\). The sole length-\(m+2\) word whose length-\(m+1\) prefix and suffix both appear but which itself does not is \(C_mBC_1\). It therefore is the unique longest minimal absent factor, as claimed.

## Verification
The included standalone Python 3 program `verify.py` constructs \(p_i\) directly from odd parts, checks the 32 distinct base strings, compares all length-\(m\) factors through \(k=11\), confirms the two predicted positions and the absence of longer repeated factors, and independently computes length-\(m+2\) minimal-absence sets. For \(k=5,6,7\) it additionally checks that no even longer minimal absent factor occurs, without using the general theorem. The local run reported `VERIFY_OK base_patterns=32 dyadic_k=5..11 longest_absence_checks=7`. These finite checks test the implementation; the preceding proof is valid for every \(k\ge5\).

## Relationship to prior work
The power-of-two paperfolding recurrence and dyadic factor structure are classical (Allouche 1992; Bates, Bunder and Tognetti 2010). The latter's Theorem 21 and Corollary 5 explicitly enumerate repetitions in the *fold-length* prefix \(S_k\) of length \(2^k-1\) and give longest repetition length \(2^{k-2}-1\) for \(k>4\). This is different from the **one-symbol-longer** prefix \(W_k\), where the one extra final symbol completes exactly one repeated block of length \(2^{k-2}\). The present claim also determines the unique longest *minimal absent* factor of \(W_k\), which is not stated by their repeated-factor theorem. General minimal-absent-word computation algorithms are established (Barton and collaborators 2014); these do not supply the stated explicit, all-dyadic formula. This is a narrow structural boundary result, not a claim of inventing the paperfolding recurrence or minimal-absence notion.

## Limitations
Only the extreme length layer of the minimal-absent-factor spectrum is classified; shorter minimal absent factors are not enumerated. The analysis does not apply as stated to arbitrary folding instructions, non-dyadic cuts, circular factors or scattered-subsequence absence. Literature comparison cannot exclude unindexed earlier derivations, particularly general finite-factor-position work; independent validation has not been performed.

## References
- J.-P. Allouche, *The Number of Factors in a Paperfolding Sequence*, Bulletin of the Australian Mathematical Society 46 (1992), 23–32, DOI: https://doi.org/10.1017/S0004972700011655 (online full text dated 2009-04-17).
- B. Bates, M. W. Bunder and K. Tognetti, *Mirroring and Interleaving in the Paperfolding Sequence*, Applicable Analysis and Discrete Mathematics 4 (2010), 96–118, DOI: https://doi.org/10.2298/AADM1000005B (issue online 2010-03-07).
- C. Barton, A. Heliou, L. Mouchard and S. P. Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array*, arXiv:1406.6341, first posted 2014-06-24; https://arxiv.org/abs/1406.6341.
