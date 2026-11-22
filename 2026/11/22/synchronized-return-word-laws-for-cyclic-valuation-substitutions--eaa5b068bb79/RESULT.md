# Synchronized return-word laws for cyclic valuation substitutions

## Finding
For integers \(b\ge2\) and \(q\ge2\), define the one-sided word \(u=(u_t)_{t\ge1}\) over \(\mathbb Z/q\mathbb Z\) by \(u_t=\nu_b(t)\bmod q\), where \(\nu_b(t)\) is the greatest nonnegative integer \(j\) for which \(b^j\mid t\). For every letter \(r\in\{0,\ldots,q-1\}\), let \(B_r=u_1\cdots u_{b^r-1}\) (empty if \(r=0\)), and define
\[
R_{r,0}=rB_r,\qquad R_{r,s}=rB_r\,(r+s\bmod q)\,B_r\quad(1\le s<q).
\]
A return word to \(r\) runs from an occurrence of \(r\) to, but not including, its next occurrence. Its **complete distinct return-word set** is exactly \(\{R_{r,s}:0\le s<q\}\); it therefore has cardinality \(q\) for *every* letter and base. Labeling returns by \(s\), the resulting infinite sequences are **identical term by term for all \(r\)**. More precisely, put
\[
 h(a)=\begin{cases}0^{b-2}(a+1),&0\le a<q-1,\\0^b,&a=q-1.\end{cases}
\]
Then every letter's return-type sequence is \(h(u)\), with the label \(0\) for \(R_{r,0}\) and label \(s\) for \(R_{r,s}\). In these common sequences the limiting relative frequencies exist and equal
\[
\pi_s=\begin{cases}
 1-\displaystyle\sum_{j=1}^{q-1}b^{-j},&s=0,\\
 b^{-s},&1\le s<q.
\end{cases}
\]
Thus the same return-type distribution holds at every distinguished letter, even though return lengths are \(b^r\) or \(2b^r\). In particular, the mean return length is \(b^r(1+\sum_{j=1}^{q-1}b^{-j})\), the reciprocal of the occurrence density of letter \(r\).

## Assumptions and scope
All positions are positive integers and all words are one-sided, infinite and indexed from \(1\). The base \(b\) need **not** be prime; \(\nu_b\) means divisibility by integral powers of the full base, not a prime-adic valuation. The letter alphabet is the finite cyclic set \(\{0,1,\ldots,q-1\}\). Frequencies are limits of counts among the first \(N\) consecutive return words as \(N\to\infty\), not frequencies among all positions of the original word. There is no claim about return words to arbitrary longer factors.

## Proof
**1. Positions and gaps.** Let \(S=\{t\ge1:\nu_b(t)\equiv0\pmod q\}\). The occurrences of letter \(r\) are precisely \(b^r S\): indeed, \(\nu_b(b^r k)=r+\nu_b(k)\), and \(0\le r<q\). The complement of \(S\) consists only of positive multiples of \(b\), so no two successive positive integers lie outside \(S\). Accordingly, consecutive members of \(S\) differ by \(1\) or \(2\); a gap of \(2\) occurs exactly when the intervening integer has valuation residue \(s\in\{1,\ldots,q-1\}\).

**2. Exact return words.** If \(0<j<b^r\) and \(k\ge1\), then \(\nu_b(b^r k+j)=\nu_b(j)\). To see this even for composite \(b\), write \(j=b^h m\), where \(h<r\) and \(b\nmid m\); then \(b^r k+j=b^h(b^{r-h}k+m)\) and the factor in parentheses is not divisible by \(b\). Hence every open block of length \(b^r\) between consecutive multiples of \(b^r\) spells the same interior word \(B_r\). A gap \(1\) in \(S\) yields \(R_{r,0}\); a gap \(2\) with intermediate valuation residue \(s\) yields \(R_{r,s}\). These words are all distinct: one is shorter, and the \(q-1\) longer ones have pairwise different central letters. Every type occurs infinitely often, because a valuation-residue-\(s\) omitted position has both neighbors in \(S\), and there are infinitely many consecutive elements of \(S\) for the short type.

**3. Exact synchronization and transduction.** The \(k\)-th occurrence position of letter \(r\) is \(b^r\) times the \(k\)-th member of \(S\). Its gap type \(s\) is the same as for letter \(0\), proving the termwise equality. To calculate that common word, partition the positive integers into consecutive base-\(b\) blocks \(b(j-1)+1,\ldots,bj\). The first \(b-1\) members of each block belong to \(S\); the last member has symbol \(1+u_j\bmod q\). Within each block are \(b-2\) short returns. Crossing its final member contributes one long return of label \(1+u_j\) if nonzero, and contributes two short returns if zero. Concatenating these contributions is exactly \(h(u)\), including the boundary between successive blocks.

**4. Frequencies.** Natural density of integers with \(\nu_b(t)=j\) is \((b-1)b^{-j-1}\), by subtracting the densities of successive divisibility classes. Thus the density of letter \(s\) is
\[
 d_s=\sum_{m\ge0}(b-1)b^{-s-qm-1}=\frac{(b-1)b^{-s-1}}{1-b^{-q}}=b^{-s}d_0.
\]
Every nonzero-letter position \(s\in\{1,\ldots,q-1\}\) lies outside \(S\) and corresponds bijectively to a return of type \(s\) between successive members of \(S\). The number of returns before position \(X\) is \(d_0X+o(X)\); the number of type-\(s\) returns is \(d_sX+o(X)\). Consequently \(\pi_s=d_s/d_0=b^{-s}\) for \(s\ge1\), and \(\pi_0\) is the complement. Every \(\pi_s\) is strictly positive. The mean return length is then the given two-length weighted mean, which equals \(d_r^{-1}\) by direct substitution. This completes all assertions.

## Verification
Two independently organized Python programs, included with this note, were executed using Python 3. The direct enumerator checked \(140\) parameter triples with \(4{,}549{,}860\) consecutive returns against the exact predicted words and cross-letter type synchronization. The substitution/transduction checker compared \(5{,}107{,}077\) derived symbols across \(30\) parameter pairs and verified all rational normalization and reciprocal-density identities. Some long-return types are too rare to appear in a fixed prefix; the direct checker only asserts that observed returns belong to the predicted set. The proof, rather than those finite checks, establishes the presence of every type and all infinite limits. Run `python check_returns.py` and `python check_morphism.py` from the directory containing these scripts.

## Relationship to prior work
Return words and derived sequences are classical; Durand's characterization of primitive substitutive words via finiteness of derived sequences does not supply this explicit all-base, all-letter formula. Huang and Wen's study of return sequences in the classical binary period-doubling word is a stronger result **within that binary special case** and is not claimed anew here. Espinoza, Popoli and Stipulanti's 2026 analysis of factor balance and substitution dynamics uses return-word decomposition in a different generality and supplies motivation for an explicit induced-word computation; its results do not entail this arithmetic synchronization and frequency law. The present assertion concerns all bases, all cyclic alphabet sizes and every single-letter return system; it should not be interpreted as a new characterization of primitive substitutions.

## Limitations
The comparison is limited to the inspected literature and available searchable records; an unindexed or differently phrased exact formula may exist. Explicit work on return sequences of the classical binary case has priority there. The common coded sequence \(h(u)\) is not asserted to be independent of the base and modulus: only its equality across distinguished letters for a *fixed* pair \((b,q)\) is proved. The letter frequencies are natural densities, not a claim of independent or identically distributed return types. All computations are finite corroborations, not substitutes for the infinite proof.

## References
- B. Espinoza, P. Popoli and M. Stipulanti, *Factor-balancedness, linear recurrence, and factor complexity*, arXiv:2602.03746v1, first publicly submitted 2026-02-03, https://arxiv.org/html/2602.03746v1 (especially Sections 5.1 and 7.1).
- Y. Huang and Z. Wen, *Envelope Words and Return Words Sequences in the Period-doubling Sequence*, arXiv:1606.05150, 2016, https://arxiv.org/abs/1606.05150 (Sections 1–4).
- F. Durand, *A characterization of substitutive sequences using return words*, *Discrete Mathematics* **179** (1998), 89–101; publicly available preprint arXiv:0807.3322v1, https://arxiv.org/html/0807.3322v1 (Sections 2.3, 4–5).
