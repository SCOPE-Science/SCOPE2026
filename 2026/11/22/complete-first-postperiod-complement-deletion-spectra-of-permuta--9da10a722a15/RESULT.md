# Complete first-postperiod complement-deletion spectra of permutation powers

## Finding

For integers \(q\ge3\) and \(n\ge2\), let \(P=c_0c_1\cdots c_{q-1}\) contain each of \(q\) distinct symbols once, let \(W=P^n\), and fix **any** deleted word \(u\in\{c_0,\ldots,c_{q-1}\}^{q+1}\). The complement set \(C(W,u)\) consists of all different **linear, rooted** words remaining when an increasing positional embedding of \(u\) is deleted from \(W\). If \(d(u)\) counts adjacent weak descents of \(u\) in the order \(c_0<\cdots<c_{q-1}\), put \(E=\binom{n+q-d(u)}{q+1}\), with \(\binom ab=0\) for \(a<b\).

For each \(r\in\{0,\ldots,q-1\}\), define the length-\(q\) cyclic permutation \(A_r=c_rc_{r+1}\cdots c_{r+q-1}\), indices reduced modulo \(q\). Partition all deleted patterns into four disjoint classes:

* **Class I:** the \(q\) words \(A_rc_r\).
* **Class II:** the \(q(q-1)\) words of either form \(A_rc_a\) with \(r<a\), or \(c_aA_r\) with \((r=0,0\le a<q-1)\) or \((r>0,0\le a\le r-2)\).
* **Class III:** the \(q(q-1)\) words of either form \(A_rc_a\) with \(r>a\), or \(c_aA_r\) with \(1\le r\le q-1\) and \(r\le a\le q-1\).
* **Class IV:** all remaining patterns (exactly \(q^{q+1}-q(2q-1)\) of them).

Then the **exact, all-parameter** number of different residual words is

\[
\boxed{|C(P^n,u)|=E-\Delta_{q,n}(u),\qquad
\Delta_{q,n}(u)=
\begin{cases}
(n-1)(n-2),&u\text{ in I},\\
\binom{n-1}{2},&u\text{ in II},\\
\binom{n-2}{2},&u\text{ in III},\\
0,&u\text{ in IV}.
\end{cases}}
\]

More strongly, the full **nontrivial output-fiber spectrum** (the number of deleted-position masks yielding a given residual word) is exact. In class I, precisely \(n-1\) outputs each have multiplicity \(n-1\). In class II there is exactly one output at each multiplicity \(2,3,\ldots,n-1\); in class III, exactly one at each multiplicity \(2,3,\ldots,n-2\). All other outputs have multiplicity one. A range with upper endpoint below two is empty; in particular, all classes have zero deficit at \(n=2\). Thus exactly \(q(2q-1)\) pattern types can ever exhibit collisions as \(n\) increases, and all other deleted patterns are collision-free for every \(n\).

For example, with \(P=012\), \(n=5\), the \(81\) four-letter patterns split into class sizes \(3,6,6,66\), with respective collision deficits \(12,6,3,0\). At a fixed pattern, this gives the exact number of distinguishable remnants, not merely the number of embeddings.

## Assumptions and scope

The input is a nonempty finite *linear* word \(P^n\) with \(q\ge3\), \(n\ge2\) and alphabet letters distinct inside \(P\). An embedding is a strictly increasing tuple of \(q+1\) source indices; a deletion mask is its selected-position set. Different embeddings can yield the same remaining word, which is counted once. The target \(u\) need not be embeddable: when it is absent the binomial coefficient and correction vanish. No rotation or letter relabeling identifies two outputs. All indices in the proof use positions \(0,1,\ldots,qn-1\), and all source letters are read cyclically modulo \(q\).

## Proof

**1. Known positional-embedding count, reconstructed.** Assign each selected letter of \(u=u_1\cdots u_{q+1}\) to a period number \(j_i\in\{0,\ldots,n-1\}\). The source order condition is precisely \(j_{i+1}-j_i\ge\mathbf1_{\{u_i\ge u_{i+1}\}}\). Subtracting these forced jumps produces a weakly increasing sequence of \(q+1\) period indices between zero and \(n-1-d(u)\). Stars and bars gives \(E=\binom{n+q-d(u)}{q+1}\). This embedding formula is **prior work**, not part of the new contribution.

**2. Collision localization.** Put \(t=q+1\), \(N=qn\), and \(L=N-t\). Suppose two different deleted masks have the same residual word and their retained-index lists are \(x_1<\cdots<x_L\) and \(y_1<\cdots<y_L\). Equal letters in \(P^n\) have indices congruent modulo \(q\); therefore \(x_i-y_i\) is a multiple of \(q\). The difference between matching retained indices is the difference between the numbers of preceding deletions, hence has absolute value at most \(t\); thus \(x_i-y_i\in\{-q,0,q\}\). Append common sentinels \(x_0=y_0=-1\), \(x_{L+1}=y_{L+1}=N\). The difference cannot jump directly from \(q\) to \(-q\) or vice versa: that would force a gap of at least \(2q\) deletions between two consecutive retained positions in one list, greater than \(t\). Choose a maximal nonzero-difference interval, say \(x_i-y_i=q\). At its left boundary, \(y_i,\ldots,y_i+q-1\) are all deleted in the first mask, since its previous retained index is the same as in the second mask. At its right boundary, \(y_j+1,\ldots,y_j+q\) are all deleted in the second mask, since its next retained index is shared. Consequently **both masks contain a contiguous block of \(q\) deletions**. The case of difference \(-q\) is symmetric.

**3. Parametrization of all collision candidates.** Removing any \(q\) consecutive source positions starting at \(s\in\{0,\ldots,q(n-1)\}\) leaves the identical linear word \(P^{n-1}\). A mask with such a block and one additional deletion is represented by a pair \((s,j)\), where \(j\in\{0,\ldots,q(n-1)-1\}\) is the index of the additionally removed symbol in \(P^{n-1}\). The original mask is
\[
M_{s,j}=\{s,s+1,\ldots,s+q-1\}\cup
\begin{cases}\{j+q\},&s\le j,\\\{j\},&s>j.\end{cases}
\]
The remnant is \(v_j\), the word obtained from \(P^{n-1}\) by deleting its symbol at position \(j\). All \(v_j\) are different because \(P^{n-1}\) has only singleton equal-letter runs (the elementary one-deletion collision criterion). The deleted pattern of \(M_{s,j}\) is \(A_{s\bmod q}c_{j\bmod q}\) for \(s\le j\), and \(c_{j\bmod q}A_{s\bmod q}\) for \(s>j\). The sole duplication in the pair representation is \(M_{j,j}=M_{j+1,j}\), a contiguous \((q+1)\)-position mask. These two representations both yield the cyclic length-\((q+1)\) word \(A_{j\bmod q}c_{j\bmod q}\). Any collision class is made entirely of masks of this displayed type by Step 2.

**4. Exact multiplicity calculation.** Write \(j=qk+a\), with \(0\le k\le n-2\) and \(0\le a<q\). For prefix-cyclic deleted words \(A_rc_a\), the number of possible block starts \(s\le j\), \(s\equiv r\pmod q\), is \(k+1\) if \(r\le a\), and \(k\) if \(r>a\). For suffix-cyclic deleted words \(c_aA_r\), the number of starts \(s>j\), \(s\equiv r\pmod q\), is \(n-1-k\) if \(r=0\) or \(r>a\), and \(n-2-k\) if \(r>0\) and \(r\le a\). A word can have both a cyclic first \(q\)-block and a cyclic last \(q\)-block **only** if it belongs to class I; in that case the two counts add to \(n\), and subtracting the one duplicated representation gives constant multiplicity \(n-1\) for each of its \(n-1\) possible \(j\)'s. For the other cyclic-prefix or cyclic-suffix patterns, the formulas give respectively multiplicities \(k+1\), \(k\), \(n-1-k\), or \(n-2-k\), as stipulated by classes II and III. Hence their multisets of multiplicities greater than one are exactly \(\{2,\ldots,n-1\}\) and \(\{2,\ldots,n-2\}\). No mask for a class-IV pattern has the consecutive \(q\)-block required by Step 2 for collisions.

**5. Distinct-output totals and exhaustiveness.** If a fixed deleted pattern has \(E\) embeddings and nontrivial residual fibers of sizes \(m_1,\ldots,m_s\), its distinct-output count equals \(E-\sum_i(m_i-1)\). For classes I, II and III those sums are respectively \((n-1)(n-2)\), \(\sum_{m=2}^{n-1}(m-1)=\binom{n-1}{2}\), and \(\sum_{m=2}^{n-2}(m-1)=\binom{n-2}{2}\). For class IV the sum is zero. To count patterns, the prefix and suffix constructions give \(2q^2\) words with cyclic length-\(q\) boundary blocks, of which precisely the \(q\) class-I words have been counted twice. Classes II and III each contain \(q(q-1)\) distinct words by the inequalities in the statement. This gives exactly the displayed partition and finishes the proof. \(\square\)

## Verification

The standalone Python 3 standard-library program `verify_direct.py` independently enumerates all \((q+1)\)-position deletion masks, partitions them by their **actual deleted word and actual remaining word**, and checks the predicted cardinality, correction and **every nontrivial fiber multiplicity**. It checks \(13\) parameter pairs covering \(q\in\{3,4,5,6\}\), totaling \(107{,}355\) masks and \(44{,}870\) nonempty fixed-pattern profiles. The separate program `verify_gap.py` constructs block-and-extra-deletion masks through the source indices and checks the computed nontrivial multiplicities for \(100\) parameter configurations \(3\le q\le12\), \(2\le n\le11\), encompassing \(61{,}125\) source-position/fiber entries. Both were run successfully; their exact outputs are embedded separately. These finite checks corroborate the proof but do not establish the arbitrary-parameter result without Steps 1–5.

## Relationship to prior work

Adamson, Fleischmann and Huch [1] introduce complement scattered factors \(C(w,u)\), prove general enumeration and reconstruction algorithms, and exhibit collision examples. Their inspected full text does not give this exact cyclic-power, fixed-deleted-pattern classification. The already published permutation-power embedding law [2] gives the known \(E\) term in Step 1, but an embedding count does not determine how embeddings cluster into equal residuals. The published general run-pattern result [3] gives an **injectivity threshold**, not this full first-postthreshold collision-fiber spectrum. The published circular-necklace classification [4] treats **rotation-classes of outputs** with at most \(q\) deletions; it does not imply a rooted linear classification with \(q+1\) deleted positions. A published arbitrary-host two-letter complement formula [5] covers the two-letter domain, which is explicitly excluded here. Li, Wang and Fu [6] investigate unconditioned nonbinary deletion spheres and extremal run constraints; the accessible abstract does not determine the specified deleted-pattern fibers here. These distinctions concern mathematical implication and not just titles or different notation.

## Limitations

The theorem requires at least three **distinct alphabet letters per period**, an exact power with \(n\ge2\), and exactly one more deleted letter than the period length. It does not give the complete collision spectrum at deletion lengths above \(q+1\), nor does it classify aperiodic or mixed-period sources. The previous positional-embedding formula and first-collision threshold are not claimed as new. The available 2026 nonbinary deletion paper was not inspected in full; a previously unindexed equivalent cannot be excluded and historical priority is not independently certified. The numerical verification is finite and separate from the all-parameter proof.

## References

1. Duncan Adamson, Pamela Fleischmann, Annika Huch, *(Sets of) Complement Scattered Factors*, arXiv:2603.20790v1, first public 2026-03-21, https://arxiv.org/html/2603.20790v1.
2. *Exact embedding-multiplicity spectrum of cyclic permutation powers*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-embedding-multiplicity-spectrum-of-cyclic-permutation-powe--bcaf0c227997.
3. *Exact run-pattern collision thresholds and short-deletion extremal counts*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-run-pattern-collision-thresholds-and-short-deletion-extrem--2036e6f8e3be.
4. *Short-deletion necklaces of permutation powers: exact orbit counts and the first phase-wrap collision*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-short-deletion-necklaces-of-permutation-powers-exact-orbit-count--16ccfbf22eda.
5. *A run-pair formula for two-letter complement scattered factors*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-run-pair-formula-for-two-letter-complement-scattered-factors--3b99e07a61fe.
6. Han Li, Xiang Wang and Fang-Wei Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493, first public 2026-01-10, https://arxiv.org/abs/2601.06493.
