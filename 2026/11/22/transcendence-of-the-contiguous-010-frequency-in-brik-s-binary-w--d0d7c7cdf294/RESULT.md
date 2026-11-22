# Transcendence of the contiguous \(010\)-frequency in Brik’s binary word

## Finding
Let \(B_1=101\), let \(B_{n+1}=B_nB_n[n+1..|B_n|]\) for each integer \(n\ge1\), with 1-based indexing, and let \(\mathbf b=b_1b_2\cdots\) be the infinite binary word having all \(B_n\) as prefixes. For \(i\ge1\), define \(c_i=1\) if \(b_ib_{i+1}b_{i+2}=010\), and \(c_i=0\) otherwise; put \(a_i=b_i+c_i\). Because \(c_i=1\) forces \(b_i=0\), all \(a_i\) belong to \(\{0,1\}\). Then
\[
\boxed{\mu_{010}:=\lim_{N\to\infty}\frac{1}{N}\#\{1\le i\le N:b_ib_{i+1}b_{i+2}=010\}=2-2\sum_{i\ge1}a_i2^{-i}\quad\text{is transcendental}.}
\]
Numerically, \(\mu_{010}\approx0.12940314790518\). This is a three-letter cylinder-frequency result, not a reproof of the previously established transcendental frequency of the individual symbol \(1\).

## Assumptions and scope
All words are over the binary alphabet \(\{0,1\}\) and indexed from position one. The expression \(B_n[n+1..|B_n|]\) means the suffix obtained by deleting the first \(n\) letters of \(B_n\). Each \(B_n\) is a prefix of \(B_{n+1}\). Occurrences of \(010\) are contiguous and overlapping starts are counted. The frequency counts **start positions** up to \(N\), even if an occurrence's last two letters lie beyond position \(N\). The all-prefix limit exists by the factor-frequency theorem cited in [2], or by the elementary two-copy recurrence combined with its all-prefix argument. We use Shallit's exact length \(|B_n|=2^{n-1}+n+1\), suffix \(01\), recurrence and full factor language [1]. We use the established Adamczewski–Bugeaud stammering criterion in the form stated as Lemma 13 of [1].

## Proof
**1. An exact recurrence for the trigram count.** Let \(Q_n\) count starts of wholly contained copies of \(010\) in \(B_n\), and let \(q(s)=\sum_{i=1}^{s-2}c_i\) for \(s\ge2\). The appended copy \(B_n[n+1..|B_n|]\) contains all \(010\)-occurrences of \(B_n\) except those beginning in its first \(n\) positions. Exactly one new occurrence can straddle the join: it begins at the penultimate letter of the first copy, which ends in \(01\), and exists precisely when \(b_{n+1}=0\). (The other possible crossing start begins with the final symbol \(1\), so cannot form \(010\).) Thus for every \(n\ge1\),
\[
Q_1=0,\qquad Q_{n+1}=2Q_n-\sum_{i=1}^{n}c_i+(1-b_{n+1}).\tag{1}
\]
The correction in (1) is bounded in modulus by \(n+1\), so \(Q_n/2^{n-1}\) converges absolutely by telescoping. Since \(|B_n|/2^{n-1}\to1\), the limit is \(\mu_{010}\), using the established all-prefix frequency existence. Summing (1) after division by \(2^n\), and using \(Q_1=0\), gives
\[
\begin{aligned}
\mu_{010}&=\sum_{n\ge1}2^{-n}\left(1-b_{n+1}-\sum_{i=1}^{n}c_i\right)\\
&=2-2\sum_{i\ge1}b_i2^{-i}-2\sum_{i\ge1}c_i2^{-i}\\
&=2-2\sum_{i\ge1}a_i2^{-i}.\tag{2}
\end{aligned}
\]
The second equality uses \(b_1=1\), \(\sum_{n\ge1}2^{-n}=1\), and \(\sum_{n\ge i}2^{-n}=2^{1-i}\). Absolute convergence justifies rearranging sums.

**2. The three-block digit code retains long repetitions.** Put \(L_n=|B_n|-n=2^{n-1}+1\). By construction the beginning of \(\mathbf b\) is \(U_nV_nV_n\), where \(U_n=b_1\cdots b_n\), and \(V_n=b_{n+1}\cdots b_{n+L_n}\). Define the coded prefix \(A_n=a_1\cdots a_n\) and coded block \(W_n=a_{n+1}\cdots a_{n+L_n}\). For every \(1\le j\le L_n-2\), the consecutive triples starting at \(n+j\) and \(n+L_n+j\) lie wholly in the two identical copies of \(V_n\), so
\[
a_{n+j}=a_{n+L_n+j}.\tag{3}
\]
Consequently the infinite binary word \(\mathbf a=a_1a_2\cdots\) begins with \(A_nW_n^{\,2-2/L_n}\), in the fractional-power sense of a full first copy and the first \(L_n-2\) letters of a second copy. For all \(n\ge3\), \(L_n\ge5\), so this prefix contains \(A_nW_n^{3/2}\). Moreover \(|A_n|/|W_n|=n/L_n\le1\), and the lengths \(|W_n|=L_n\) strictly increase to infinity. The stammering criterion (Adamczewski–Bugeaud [3], quoted precisely in [1, Lemma 13]) therefore implies that
\[
\theta:=\sum_{i\ge1}a_i2^{-i}\quad\text{is rational or transcendental}.\tag{4}
\]
This applies to the **coded word**, not only to the original Brik word.

**3. The coded word is not eventually periodic.** Shallit's complete factor-language theorem [1, Theorem 7] ensures that \(\mathbf b\) contains \(1^k\) for every positive integer \(k\); because \(a_i\ge b_i\), so does \(\mathbf a\). Thus \(\mathbf a\) has unbounded lengths of consecutive ones. The word \(011\) occurs in \(\mathbf b\) by the same theorem, and recurs infinitely often by [1, Theorem 3]. At each such start \(i\), \(b_i=0\) but \(b_ib_{i+1}b_{i+2}\ne010\), hence \(a_i=0\). The coded word therefore also has infinitely many zero symbols. An eventually periodic binary word with infinitely many zeros has bounded runs of consecutive ones, so \(\mathbf a\) is not eventually periodic. Every rational number in \([0,1]\) has an ultimately periodic binary expansion; the explicitly given expansion for \(\theta\) does not. Thus \(\theta\) is irrational, and (4) forces it to be transcendental. Equation (2) now shows \(\mu_{010}=2-2\theta\) is transcendental. \(\square\)

## Verification
The standalone standard-library file `verify.py` reconstructs the first 19 finite words through length \(262164\), verifies the exact lengths, suffix and absence of \(00\), checks the count recurrence (1) for 18 stages, verifies the coded repetition identity (3) for 11 values \(3\le n\le13\), and checks sample runs/zero witnesses. It evaluates the exact 60-bit rational truncation of \(\theta\) with a tail bound less than \(2^{-60}\), and compares the resulting prediction with finite-prefix factor frequency. Run `python verify.py`; the actual recorded output appears in `verification_output.txt`. The finite runs do **not** prove convergence, the all-stage recurrence, or transcendence; these follow from the argument above and the cited theorem.

## Relationship to prior work
Shallit [1] proved that the **single-letter frequency** \(\mu(1)\) is transcendental, and established the full factor language and recurrence used here. That letter result does not give the \(010\) frequency: the periodic words \((110)^\omega\) and \((010111)^\omega\) both define stationary golden-mean measures of one-letter \(1\)-frequency \(2/3\), but their \(010\)-frequencies are respectively \(0\) and \(1/6\). Thus the three-letter correlation is not fixed by the marginal. The subsequently published factor-frequency theorem [2] establishes existence and positivity of every factor frequency (plus quantitative discrepancy) but no transcendence for a three-letter cylinder; the published Shannon-block-entropy theorem [4] supplies an entropy bound but not arithmetic restrictions on individual frequencies. Equation (2) and the local coding argument provide the missing frequency identity and irrationality-plus-stammering proof for the first genuine short-block correlation. Standard Adamczewski–Bugeaud transcendence theory is an essential cited input, not a new result.

## Limitations
No algebraic independence between \(\mu_{010}\) and \(\mu(1)\), or simultaneous transcendence of other cylinders, is asserted. This is specific to the displayed Brik recursion and to the contiguous factor \(010\). The proof relies on an existing transcendence criterion and two proved full-language/recurrence facts; their independent verification is not claimed. Search of accessible literature and published mathematical records cannot exclude an unindexed equivalent specialization or prior unpublished discovery. No independent audit has been performed.

## References
1. Jeffrey Shallit, *Brik’s sequence: a strange recursion*, arXiv:2605.07542v1, first public 2026-05-08, https://arxiv.org/html/2605.07542v1 . See Proposition 1, Theorems 3, 7, 10, 12 and Lemma 13.
2. *A full-support zero-entropy frequency law for Brik’s binary word* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-full-support-zero-entropy-frequency-law-for-brik-s-binary-word--8cf4c9f159c7 . See its `RESULT.md` for the all-cylinder frequency theorem.
3. B. Adamczewski and Y. Bugeaud, *On the complexity of algebraic numbers. I. Expansions in integer bases*, Annals of Mathematics 165 (2007), 547–565, Theorem 5 (criterion quoted in [1, Lemma 13]).
4. *Logarithmic Shannon block entropy for the Brik sequence* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-logarithmic-shannon-block-entropy-for-the-brik-sequence--8922a546c5b5 .
