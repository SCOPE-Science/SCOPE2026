# Four-marker circular prefix-normality: an exact gap criterion and forbidden-necklace series

## Finding

Let \(W\) be a binary circular word of length \(n\ge4\) containing exactly four ones. Its four ones, read cyclically, determine nonnegative zero gaps \(g_0,g_1,g_2,g_3\) with \(\sum_i g_i=n-4\). A **prefix-maximal root** is a position at which a linearization of \(W\) begins whose prefix has the maximum possible number of ones among **all circular factors** of the same length, simultaneously for every length \(1\le \ell\le n\). Equivalently, the corresponding periodic infinite word is one-prefix-normal.

**Theorem.** The complete set of prefix-maximal roots consists precisely of the one positions indexed by
\[
\boxed{\{i\in\mathbb Z/4\mathbb Z:\quad g_i=\min_jg_j\ \text{and}\ g_{i-1}=\max_jg_j\}.}
\]
Consequently a prefix-maximal root exists if and only if a longest zero gap is immediately followed, in the cyclic order, by a shortest zero gap. This remains exact when gaps are zero, equal, or periodic.

Let \(B_n\) count oriented binary necklaces (rotation equivalence only, without identifying reversal or complement) of length \(n\) and weight four with **no** prefix-maximal root. Then
\[
\boxed{\sum_{n\ge4}B_nz^n=\frac{z^7}{(1-z)^4(1+z^2)(1+z+z^2)}.}
\]
The first failure occurs at length \(7\), with exactly one failing necklace, represented by `1110010`. The first values \(B_4,B_5,\ldots,B_{14}\) are \(0,0,0,1,3,5,8,13,19,26,35\). Among all weight-four necklaces of length \(n\), the failure proportion tends to \(2/3\) as \(n\to\infty\).

The extremal-gap adjacency rule also characterizes prefix-maximal roots for weights two and three; **four is the largest weight for which it universally suffices**. For every weight \(k\ge5\), the cyclic zero-gap tuple \((0,2,\underbrace{0,\ldots,0}_{k-3},3)\) has a shortest gap immediately after its unique longest gap yet no prefix-maximal root; at weight five this is `1100111000`.

## Assumptions and scope

Circles use the alphabet \(\{0,1\}\), with ones distinguished. Gap indices follow successive ones modulo the number of ones; a gap counts zeros between consecutive ones and may be zero. The enumeration counts rotation classes, not labeled phases, reversals, or complements. The full periodic prefix-normal comparison includes wrap-around circular factors, and is stronger than ordinary prefix-normality of a single linear rotation against its nonwrapping factors. The source date in the accompanying metadata pertains to the guiding published study of prefix normal forms, not to the date of this theorem.

For a circular word represented by \(u\), every length \(qn+r\) factor of \(u^\omega\), with \(0\le r<n\), contains exactly \(q\cdot4\) additional ones beyond its length-\(r\) remainder. The same holds for a prefix. Thus the finite circular comparison for lengths \(1\) through \(n\) is equivalent to prefix-normality of the entire periodic infinite word.

## Proof

**1. Prefix thresholds.** Any maximum-one circular factor of length \(\ell\ge1\) can be chosen to begin at a one. Indeed its maximum number of ones is positive. If a maximizing window begins at zero, shift its start forward to its first one, dropping only initial zeros and extending its right end by an equal number of positions. This cannot decrease the number of ones. Hence it suffices to compare roots at the four one positions.

For a root at the one preceding gap \(g_i\), the positions (counted starting at one) of its second, third and fourth ones are respectively
\[
\tau_{i,2}=2+g_i,\qquad
\tau_{i,3}=3+g_i+g_{i+1},\qquad
\tau_{i,4}=4+g_i+g_{i+1}+g_{i+2}=n-g_{i-1}.
\]
The number of ones in its length-\(\ell\) prefix is
\[
1+\mathbf1_{\ell\ge\tau_{i,2}}+\mathbf1_{\ell\ge\tau_{i,3}}+\mathbf1_{\ell\ge\tau_{i,4}}.
\]
A root is prefix-maximal for every length if and only if each of its three threshold values attains the minimum over all four one roots. Necessity follows by testing the earliest length at which any circular factor can contain respectively two, three and four ones; sufficiency follows since each of the three indicator functions is then pointwise maximal.

**2. Four-gap extremal rigidity.** Minimizing \(\tau_{i,2}\) requires \(g_i=\min g\); minimizing \(\tau_{i,4}\) requires \(g_{i-1}=\max g\). Assume both. The consecutive pair sums to be minimized for the third-one threshold are
\[
g_i+g_{i+1},\quad g_{i+1}+g_{i+2},\quad
g_{i+2}+g_{i-1},\quad g_{i-1}+g_i.
\]
The first is no larger than the second because \(g_i\le g_{i+2}\); it is no larger than the fourth because \(g_{i+1}\le g_{i-1}\); and it is no larger than the third because both inequalities hold simultaneously. Thus it also minimizes \(\tau_{i,3}\). This proves both directions and the exact set of roots, including every tied case.

**3. Counting forbidden necklaces.** A cyclic four-tuple of nonnegative gaps gives exactly one weight-four necklace, and conversely. A forbidden tuple is one in which no maximum gap is immediately followed by a minimum gap. Any tuple fixed by a nonidentity cyclic shift is constant or alternating. Either has such a maximum-to-minimum transition, so **every forbidden tuple has four distinct cyclic gap rotations**.

Classify forbidden tuples by their ordered distinct gap values, from smallest to largest. With three distinct values, the level multiplicities \((2,1,1)\), \((1,2,1)\), and \((1,1,2)\) have respectively \(4,8,4\) forbidden arrangements around four labeled positions. With four distinct values there are \(16\): fix the largest position in four ways, choose the smallest in either of the two positions not immediately following it, and arrange the two middle levels in two ways. With one or two distinct values none are forbidden, because a cyclic two-level word necessarily has a high-to-low transition.

For multiplicities \((s_1,\ldots,s_k)\) of increasing distinct nonnegative values, put \(u_j=s_{j+1}+\cdots+s_k\). Writing the lowest level as an arbitrary nonnegative integer and each consecutive level increment as a positive integer gives the gap-sum generating function
\[
\frac1{1-z^4}\prod_{j=1}^{k-1}\frac{z^{u_j}}{1-z^{u_j}}.
\]
Dividing the four forbidden-arrangement counts by their orbit size four, the generating function by total **zero-gap sum** \(t=n-4\) is
\[
\begin{aligned}
H(z)=\frac1{1-z^4}\biggl(&\frac{z^3}{(1-z^2)(1-z)}+
\frac{2z^4}{(1-z^3)(1-z)}\\
&+\frac{z^5}{(1-z^3)(1-z^2)}+
\frac{4z^6}{(1-z^3)(1-z^2)(1-z)}\biggr)\\
=\frac{z^3}{(1-z)^4(1+z^2)(1+z+z^2)}.
\end{aligned}
\]
Multiplication by \(z^4\) converts the gap-sum series to the length series in the theorem. Its numerator starts at degree seven with coefficient one, proving the sharp first failure and its uniqueness.

**4. Asymptotic fraction.** The only pole of order four of \(H(z)\) lies at \(z=1\), where its leading singular term is \(1/[6(1-z)^4]\); all other unit-circle poles have smaller order. Hence \(B_{t+4}=t^3/36+O(t^2)\). By Burnside's lemma the total number of weight-four necklaces with gap sum \(t\) is exactly
\[
N_{t+4}=\frac14\left[\binom{t+3}{3}+\mathbf1_{2\mid t}(t/2+1)+2\mathbf1_{4\mid t}\right]
=\frac{t^3}{24}+O(t^2).
\]
Their ratio tends to \((1/36)/(1/24)=2/3\).

**5. Exact small-weight boundary.** For weight two, choose the one followed by the shorter gap. For weight three, the second-one and third-one thresholds force the same minimum-gap/preceding-maximum-gap rule; this is also the established three-marker classification. Thus the rule works for weights two, three and four. For each weight \(k\ge5\), take the \(k\) cyclic gaps \((0,2,\underbrace{0,\ldots,0}_{k-3},3)\). The only possible extremal-gap root is the one after the unique longest gap \(3\); its length-three prefix is `110`, whereas the run of \(k-2\ge3\) consecutive ones after the gap of length two produces a circular factor `111`. It therefore fails, and no other root can satisfy both necessary extremal-gap conditions. At \(k=5\) this is `1100111000`. This establishes failure for every larger weight and proves the sharp universal four-to-five boundary.

## Verification

Run `python3 verify.py` in the same directory with a standard Python 3 interpreter. The script directly enumerates every four-gap tuple of total gap sum from zero through twenty-two, computing all circular window maxima and all actual prefix-maximal roots without using the proof's threshold or rank formulas. It checks all \(14{,}950\) such tuples against the asserted **exact sets of roots**, divides the number of forbidden tuples by four, and independently checks the first twenty-three coefficients of the displayed rational generating function by its integer polynomial recurrence. The five-marker counterexample is tested directly. The program reports `VERIFY_OK` on success. These finite tests are not a substitute for the unbounded proof above.

## Relationship to prior work

The established prefix-normal form framework and its jumbled-pattern-matching motivation are developed by Burcsi, Fici, Lipták, Ruskey and Sawada (2016). Cicalese, Lipták and Rossi (2018/2021) treat infinite and periodic prefix-normal words. Those sources provide definitions and general tools, not the above exact four-marker circular-root criterion and enumeration.

A previously indexed three-marker circular-root result gives the same extremal adjacency condition at weight three and a different necklace series, whereas the present four-marker proof must additionally eliminate the third-one pair-sum obstruction. An indexed four-**run** cyclic result treats a different family: it allows arbitrary one-run lengths but only two one-runs, while the present weight-four family includes circles with four isolated ones (eight runs). An indexed finite-linear-cut result concerns comparisons with nonwrapping factors and does not imply the periodic circular comparison here. General prefix-normal forms may reorder the input and do not ensure that a suitable **rotation** exists. No theorem of the same four-marker scope was found in the compared source texts and indexed records; this is a best-knowledge comparison, not an independent priority certification.

## Limitations

The complete count concerns weight exactly four and rotations only. The five-marker example refutes sufficiency of the adjacency rule but does **not** classify all five-marker circles. The limiting fraction is among fixed-weight-four necklaces, not all binary necklaces. Tied gaps and periodic circles are included; absence of a suitable circular prefix-maximal root does not imply absence of an ordinary linear prefix-normal cut. Equivalent earlier work not indexed or accessible in the compared sources cannot be excluded; no independent mathematical audit has been performed.

## References

1. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017v1, first public version 2016-11-28. https://arxiv.org/html/1611.09017v1
2. F. Cicalese, Z. Lipták and M. Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273, first public version 2018-11-15; published in *Theoretical Computer Science* 859 (2021), 134–148. https://pmc.ncbi.nlm.nih.gov/articles/PMC8219218/
3. *First circular prefix-normal obstructions and the complete three-one classification*, published mathematical record (2026), identifying the weight-three circular-root problem and its distinct generating function.
4. *Prefix-normal rotations of four-run binary cycles: a sharp run-order obstruction and an exact necklace census*, published mathematical record (2026), covering cyclic words with exactly two one-runs.
5. *The sharp cyclic prefix-normal representative obstruction*, published mathematical record (2026), concerning finite linear prefix-normal cuts rather than circular-factor comparison.
