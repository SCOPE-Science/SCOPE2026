# Exact multi-deletion subcodes of repeated message blocks

## Finding
Fix a labeled alphabet \(\Sigma\) of size \(q\ge 2\), a block length \(m\ge 1\), a deletion budget \(t\ge 2\), and a repetition factor \(r\ge 2t+1\). Encode every \(U\in\Sigma^m\) as the linear word \(U^r\). Two different encoded words have a common *exactly-\(t\)-deletion* output if and only if their message blocks are rotations of one another by at most \(t\) positions in one of the two directions. This is a statement about **linear received words**, not necklaces obtained after deletion.

Let \(P_q(d)=d^{-1}\sum_{e\mid d}\mu(e)q^{d/e}\) be the number of primitive length-\(d\) necklaces; set
\[
k_d=\max\left\{1,\left\lfloor\frac{d}{t+1}\right\rfloor\right\},\qquad
h_d=\begin{cases}
d,&1\le d\le t,\\
\dfrac{d}{k_d}\binom{d-tk_d-1}{k_d-1},&d>t.
\end{cases}
\]
The maximum number of messages in an exactly-\(t\)-deletion-correcting subcode of this repeated-block family, and the number of labeled subcodes attaining it, are respectively
\[
K_q(m,t)=\sum_{d\mid m}P_q(d)k_d,\qquad
H_q(m,t)=\prod_{d\mid m}h_d^{P_q(d)}.
\]
For fixed \(q,t\), \(K_q(m,t)/q^m\longrightarrow 1/(t+1)\) as \(m\longrightarrow\infty\). In particular, adding arbitrarily many whole-message repetitions beyond \(2t+1\) does not remove the cyclic-phase confusability or increase the optimal code size within this family.

For \(q=2,t=2\), the first capacities \(K_2(m,2)\), at block lengths \(m=1,\ldots,8\), are \(2,3,4,6,8,23,38,66\). The result is an exact all-length statement, not an interpolation from these values.

## Assumptions and scope
Words are indexed linear strings. The channel deletes exactly \(t\) arbitrary individual symbol positions; it neither permutes surviving positions nor identifies their cyclic rotations. Each codeword is a power \(U^r\) of an arbitrary message word \(U\) of fixed length \(m\). A code corrects \(t\) deletions when the sets of all distinct length-\(rm-t\) descendants are disjoint for different codewords. Rotations of a message are distinct messages unless the rotation leaves its string unchanged; no quotient of messages by rotation is taken. Primitive means that a word has least circular period equal to its length; the least circular period \(d\) of a length-\(m\) word divides \(m\).

## Proof
**Step 1 — clean-block alignment.** Suppose \(U^r\) and \(V^r\) have a common word after exactly \(t\) deletions each. Fix one increasing positional alignment of the \(rm-t\) matched symbols. Mark any of the \(r\) consecutive length-\(m\) blocks of \(U^r\) containing a deleted position on the \(U\)-side. Also mark a block whenever the aligned image of two successive surviving symbols *within that same block* straddles a position deleted on the \(V\)-side. Each of the at most \(t\) deleted \(U\)-positions marks one block. Each deleted \(V\)-position lies between successive matched symbols in at most one such block, hence marks at most one additional block. Fewer than \(r\) blocks are marked because \(r\ge 2t+1\). Choose an unmarked block. All its \(m\) letters appear consecutively in \(V^r\), hence \(U\) is a cyclic rotation of \(V\).

If the corresponding matched positions in the two strings are \(i,j\) (both one-indexed), their displacement \(j-i\) is the number of deleted \(V\)-positions before the match minus the number of deleted \(U\)-positions before it, up to sign convention. Consequently \(|j-i|\le t\). Both original words have period \(m\), and the clean block therefore proves that \(V\) is a rotation of \(U\) by a signed displacement of absolute value at most \(t\). Conversely, if \(V\) is such a rotation by \(s\) positions with \(0\le s\le t\), the two length-\(rm\) powers have a common contiguous subsequence of length \(rm-s\): discard an initial \(s\)-letter prefix of one and a final \(s\)-letter suffix of the other. Delete a further \(t-s\) common symbols from each if necessary. Thus their exactly-\(t\) deletion shadows intersect. This establishes the exact pairwise confusability criterion.

**Step 2 — rotation components and optimal sizes.** Each message of least period \(d\mid m\) belongs to one rotation class of exactly \(d\) distinct messages; this class corresponds to a primitive necklace of length \(d\). The confusability criterion makes the induced component the radius-\(t\) power of the cycle of length \(d\), with no edges between different classes. When \(d\le t\), this component is complete, so its independent-set maximum is one. Otherwise, list the cyclic gaps between selected vertices; each is at least \(t+1\). Their sum is \(d\), giving at most \(\lfloor d/(t+1)\rfloor\) vertices. Selecting positions at spacings \(t+1\), with the final wraparound gap at least \(t+1\), attains the bound. Hence the maximum is exactly \(k_d\). The number of distinct primitive rotation classes of length \(d\) is \(P_q(d)\), obtained by Möbius inversion of \(q^d=\sum_{e\mid d}eP_q(e)\). Summing independent-set maxima over all classes gives \(K_q(m,t)\).

**Step 3 — number of maximizers.** For \(d\le t\), every singleton is optimal, giving \(h_d=d\). For \(d>t\), put \(k=k_d\). An optimal choice of \(k\) labeled positions on the circular \(d\)-cycle is uniquely specified, after choosing one of the selected positions as origin, by \(k\) ordered positive gaps at least \(t+1\), summing to \(d\). There are \(\binom{d-tk-1}{k-1}\) such gap vectors. There are \(d\) choices of the labeled origin but every selected set is counted \(k\) times. Therefore its count is \(h_d=(d/k)\binom{d-tk-1}{k-1}\), and multiplying independent choices across the disjoint rotation classes gives \(H_q(m,t)\).

**Step 4 — capacity fraction.** For fixed \(q\ge2\), the primitive necklace count is \(P_q(m)=q^m/m+O(q^{m/2})\), with other divisors contributing \(O(mq^{m/2})\) to the number of messages. Since \(k_m=m/(t+1)+O(1)\), their contribution gives \(K_q(m,t)=q^m/(t+1)+o(q^m)\).

## Verification
Run `python3 check.py` from this directory; it prints `VERIFY_OK` after independent exhaustive tests. The verifier enumerates distinct deletion outputs by position combinations and compares every unordered pair against the signed-rotation prediction for binary lengths through five and ternary lengths through three at deletion budgets one and two. For every tested family of at most 16 messages, it additionally enumerates all subsets of messages and independently computes both maximum code size and the number of maximizing codebooks, checking the two formulas. The code also prints representative exact capacities. These finite checks corroborate but do not replace Steps 1–4, which cover all stated integer parameters.

## Relationship to prior work
Sloane's 2002 survey develops deletion shadows, deletion distance, and independent-set formulations for deletion-correcting codes. Sala, Gabrys, Schoeny, and Dolecek (2016) give general extremal common-supersequence formulas and discuss deletion-channel reconstruction; these bounds do not by themselves identify the repeated-block confusability components or count all maximum restricted codebooks. The necklace enumeration uses classical primitive-period Möbius inversion. Dolecek and Anantharam's 2010 work concerns correcting *repetition errors* (local symbol duplication operations), not an encoder that repeats an entire block before arbitrary symbol deletions. The present result is restricted to the latter setting. No claim is made about the optimal code over all \(q\)-ary length-\(rm\) strings.

## Limitations
The sufficient repetition factor \(r\ge2t+1\) is not asserted to be minimal. The exact graph need not hold at smaller repetition factors. The statement concerns *exactly* \(t\) adversarial deletions; correcting up to \(t\) deletions follows here because a common shorter descendant can be shortened further, but output lengths are otherwise distinct. The counting formula is for labeled message strings and exact deletion decoding, not circular received strings or a code with variable-length messages. The originality comparison cannot exclude an unindexed earlier equivalent theorem, and the full text of one related repetition-error article was not available during this comparison.

## References
1. N. J. A. Sloane, "On Single-Deletion-Correcting Codes," arXiv:math/0207197v1, first posted July 22, 2002. https://arxiv.org/html/math/0207197v1
2. F. Sala, R. Gabrys, C. Schoeny, and L. Dolecek, "Exact Reconstruction from Insertions in Synchronization Codes," arXiv:1604.03000v1, first posted April 11, 2016. https://arxiv.org/abs/1604.03000
3. L. Dolecek and V. Anantharam, "Repetition Error Correcting Sets: Explicit Constructions and Prefixing Methods," SIAM J. Discrete Math. 23 (2010), 2120–2146. https://doi.org/10.1137/080730093
