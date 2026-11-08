# Universal adjacent-run frequencies in generalized paperfolding words

## Finding

Let \(\epsilon=(\epsilon_0,\epsilon_1,\ldots)\in\{-1,+1\}^{\mathbb N_0}\) be **any** infinite instruction sequence. Define its one-sided generalized paperfolding word \(p_1p_2\cdots\) by writing each positive integer uniquely as \(n=2^k m\) with \(m\) odd, and setting
\[
p_n=\begin{cases}\epsilon_k,&m\equiv1\pmod4,\\-\epsilon_k,&m\equiv3\pmod4.\end{cases}
\]
Let \(r_1,r_2,\ldots\) be the lengths of its successive maximal constant-sign runs. Every run has length at most three. For all \(a,b\in\{1,2,3\}\), the limiting ordered adjacent-run frequency exists and is **independent of the entire instruction sequence**:
\[
\lim_{K\to\infty}\frac1K\#\{1\le j\le K:(r_j,r_{j+1})=(a,b)\}
=J_{ab},\qquad
J=\frac1{16}\begin{pmatrix}0&3&1\\3&2&3\\1&3&0\end{pmatrix}.
\]
Consequently the limiting marginal distribution of a run length is \((1/4,1/2,1/4)\), and the mutual information between successive run lengths, using logarithms to base two, equals
\[
I(r_j;r_{j+1})=\frac34\log_2(3/2)-\frac18
=0.3137218755\ldots\ \text{bits}.
\]
Here mutual information refers to the limiting joint distribution, not to a random choice of folding instructions.

## Assumptions and scope

The alphabet is exactly \(\{-1,+1\}\), and instructions may be arbitrary (not assumed random, periodic or automatic). Frequencies are natural densities of consecutive run pairs counted by their **run indices**, not by the indices of individual signs. The two exterior signs of each counted run pair exist because the word is infinite; the initial run contributes only a finite boundary exception. All quantifiers range over every infinite instruction sequence and every pair of lengths in \(\{1,2,3\}\). Nothing is asserted about longer blocks of run lengths.

## Proof

**1. Run-length bound.** At every odd position \(n\), the sign is \(\epsilon_0\) if \(n\equiv1\pmod4\) and \(-\epsilon_0\) if \(n\equiv3\pmod4\). Every four consecutive positions contain two odd indices two apart, whose signs differ. A constant run therefore has length at most three.

**2. An exact finite local model.** A complete pair of consecutive runs of lengths \(a\) and \(b\), starting after position \(t\), is characterized by the length-\((a+b+2)\) factor
\[
(-s)\,s^a\,(-s)^b\,s,\qquad s\in\{-1,+1\}.
\]
The factor's first and last signs show that both interior runs are maximal. Since \(a+b+2\le8\), this event is determined by an eight-sign window, and each actual adjacent pair determines one unique start position \(t\) except for the initial-run boundary.

In any block of eight consecutive positive positions there is exactly one index divisible by eight. The other seven signs depend only on the first three instructions \(\epsilon_0,\epsilon_1,\epsilon_2\) and the start residue \(t\pmod{16}\). The sign at the unique multiple of eight is asymptotically unbiased, conditional on that start residue, for **every** infinite instruction sequence. Indeed, at multiples \(8m\) with \(m\) odd, the signs alternate equally between the two odd residue classes modulo four. At multiples of sixteen the same reasoning applies recursively to the shifted instruction sequence. More explicitly, at valuation \(v_2(m)=j\), the odd quotient \(m/2^j\) is equally often \(1\) and \(3\) modulo four; summing the geometric valuation classes and bounding the tail proves limiting probabilities \(1/2,1/2\). Fixing the residue modulo sixteen only distinguishes the odd-\(m\) and even-\(m\) cases, both of which retain this balance. Thus the window's limiting distribution is the uniform mixture of the following thirty-two templates for each fixed triple \((\epsilon_0,\epsilon_1,\epsilon_2)\): choose \(t\pmod{16}\) and choose the multiple-of-eight sign independently as \(+1\) or \(-1\).

**3. Exact exhaustive residue count.** Normalize \(\epsilon_0=+1\), which changes no run lengths: reversing all signs is equivalent to changing all instructions' signs. For a residue \(u\in\{0,\ldots,15\}\) and an upper sign \(h\in\{-1,+1\}\), form an eight-sign template \(w_0,\ldots,w_7\) as follows. If \(8\mid(u+j)\), set \(w_j=h\). Otherwise write \(u+j=2^km\) with \(k\in\{0,1,2\}\) and \(m\) odd, and set \(w_j=\epsilon_k\) for \(m\equiv1\pmod4\), or \(-\epsilon_k\) for \(m\equiv3\pmod4\). This includes the residue \(u=0\), where the placeholder represents a sufficiently large positive multiple of sixteen. For each \(a,b\in\{1,2,3\}\), test whether the prefix of length \(a+b+2\) has the pattern in Step 2.

The complete residue count, with rows indexed by \(a\) and columns by \(b\), is:

| \((\epsilon_1,\epsilon_2)\) | Counts among the 32 templates |
|---|---|
| \((+1,+1)\) | \(\begin{pmatrix}0&3&1\\3&2&3\\1&3&0\end{pmatrix}\) |
| \((+1,-1)\) | \(\begin{pmatrix}0&3&1\\3&2&3\\1&3&0\end{pmatrix}\) |
| \((-1,+1)\) | \(\begin{pmatrix}0&3&1\\3&2&3\\1&3&0\end{pmatrix}\) |
| \((-1,-1)\) | \(\begin{pmatrix}0&3&1\\3&2&3\\1&3&0\end{pmatrix}\) |

These are at most \(4\cdot16\cdot2\cdot9=1152\) Boolean tests, wholly finite and independently reproducible using the standard-library program `verify.py`. Step 2 justifies the finite reduction; the enumeration does not extrapolate finite prefixes to an infinite theorem. Dividing by thirty-two proves that the natural **position density** of every complete pair of runs of lengths \((a,b)\) is the corresponding matrix entry divided by thirty-two.

**4. Conversion to run-index frequency.** The counts in the matrix sum to sixteen, so complete adjacent run pairs occur with position density \(16/32=1/2\). Every run after the first initiates exactly one such pair, and the first or final incomplete run in a finite prefix changes counts by at most a constant. Therefore the run count up to position \(N\) satisfies \(R(N)/N\to1/2\), and dividing each pair's position density by \(1/2\) gives exactly the displayed joint law \(J\). Its row and column sums are both \((1/4,1/2,1/4)\). The four entries \(3/16\) have independence ratio \(3/2\), the two entries \(1/16\) have ratio one, and the central entry \(2/16\) has ratio \(1/2\). The mutual-information formula follows by summing \(J_{ab}\log_2(J_{ab}/(p_ap_b))\) over the positive entries.

## Verification

Run `python3 verify.py` with Python 3 and no additional packages. Its first loop evaluates all \(8\cdot16\cdot2\) local templates, including both choices of the first instruction, and checks the asserted matrix. Its second loop compares the valuation definition of paperfolding with the finite reverse-complement folding recursion for all instruction sequences of lengths one through seven (\(254\) cases). Its final loop independently checks run-pair counts for eight explicit nonrandom instruction families on prefixes of length \(2^{16}\), allowing only bounded endpoint discrepancies. A successful run prints `VERIFY_OK symbolic_cases=256 fold_cases=254 prefix_cases=8` followed by the three count-matrix rows.

The symbolic residue verification and the valuation argument are the decisive proof. Finite-prefix data are supplemental checks, not proof of limiting behavior.

## Relationship to prior work

The 2012 study of Madill and Rampersad derives structural recurrences for the abelian complexity of the ordinary paperfolding word and gives the valuation/Toeplitz framework. Earlier work of Allouche and Bousquet-Mélou addresses canonical locations of finite factors. Bunder, Bates and Arnold (2024) identify the regular paperfolding run-length sequence with a continued-fraction sequence. Shallit's 2024 arXiv preprint (journal publication 2025/2026) proves synchronization, the length bound, allowable factors and subword complexity of run-length words for **all** instruction sequences. In particular, it implies the permitted two-letter run factors and provides a finite computational description of their locations, but does not state or evaluate their limiting joint-frequency law. The present result adds the instruction-independent frequency matrix and an exact dependence statistic. It does not claim the run-length alphabet, factor language, or automatic description as new.

## Limitations

The claimed limit concerns adjacent run lengths, not all higher-order dependencies. The method uses eight-sign windows and does not imply that frequencies of longer run-patterns are instruction-independent. No general finite-sample exact error formula is asserted. Novelty is subject to historical priority: the complete text of the 1994 canonical-positions paper was not accessible for decisive full-document comparison, and the published automaton description in the later run-sequence literature could yield this matrix after additional computation. No independent mathematical audit has been performed.

## References

1. Blake Madill and Narad Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856, first posted 2012-08-14. https://arxiv.org/abs/1208.2856
2. Jeffrey Shallit, *Runs in Paperfolding Sequences*, arXiv:2412.17930, first posted 2024-12-23. https://arxiv.org/abs/2412.17930
3. Martin Bunder, Bruce Bates and Stephen Arnold, *The Summed Paperfolding Sequence*, *Bulletin of the Australian Mathematical Society* 110 (2024), 189–198. https://doi.org/10.1017/S0004972724000169
4. Jean-Paul Allouche and Mireille Bousquet-Mélou, *Canonical positions for the factors in paperfolding sequences*, *Theoretical Computer Science* 129 (1994), 263–278. https://doi.org/10.1016/0304-3975(94)90028-0
