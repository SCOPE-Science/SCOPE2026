# Sharp inverse-list size for simultaneous deletions in ordered composite strands

## Finding

Consider an alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\), with \(q\ge2\). A two-row ordered composite word is a pair \((x,y)\in(\Sigma_q^n)^2\) satisfying \(x_j\le y_j\) in every column. Transmit the two labeled rows through channels which each delete **exactly one** letter, at independently chosen positions. For a received pair \((u,v)\) of two length-\(n-1\) strings, write \(L_{q,n}(u,v)\) for the number of **distinct** ordered composite source words consistent with the received pair; different deletion positions yielding the same source are not counted again.

**Theorem.** For all integers \(q\ge2\) and \(n\ge1\),

\[
\max_{u,v\in\Sigma_q^{n-1}}L_{q,n}(u,v)
=\bigl(1+n(q-1)\bigr)^2-\frac{nq(q-1)}2.
\]

For every \(n\ge2\), equality holds **if and only if** \(u=0^{n-1}\) and \(v=(q-1)^{n-1}\). At \(n=1\), the sole output is the pair of empty strings and the formula gives \(q(q+1)/2\) possible sources.

## Assumptions and scope

The row labels and source length are known. Each of the two channels deletes exactly one symbol, so both output lengths are \(n-1\). The order constraint is on original aligned columns only. The output rows need not be coordinatewise ordered, because their deletion locations can differ. The alphabet is linearly ordered, and no symbols are inserted or substituted.

Let \(I_q(w)\) be the set of distinct length-\(|w|+1\) words obtainable by inserting one alphabet symbol into a word \(w\). Then

\[
L_{q,n}(u,v)=\#\{(x,y)\in I_q(u)\times I_q(v):x_j\le y_j\ (1\le j\le n)\}.
\]

## Proof

**1. Distinct-supersequence partition.** If \(w=az\) is a nonempty word with first symbol \(a\), then the union

\[
I_q(az)=\{aX:X\in I_q(z)\}\;\dot\cup\;\{caz:c\in\Sigma_q,\ c\ne a\}
\]

is disjoint. Every insertion resulting in first symbol \(a\) belongs to the first part (including insertion of another \(a\) at the beginning); any result with a different first symbol must have inserted that symbol at the beginning. Starting with \(I_q(\varepsilon)=\Sigma_q\), induction yields

\[
|I_q(w)|=1+(|w|+1)(q-1).
\]

Set \(d=q-1\), \(T=1+(n-1)d\), and

\[
M_n=(1+nd)^2-\frac{nqd}{2}.
\]

For \(n=1\), the received rows are empty and \(L_{q,1}(\varepsilon,\varepsilon)=q(q+1)/2=M_1\).

**2. Inductive bound.** Assume \(n\ge2\). Let \(u=aU\) and \(v=bV\), where the tails \(U,V\) have length \(n-2\). Partition both supersequence sets as in Step 1. In the part where both supersequences begin with their respective original first letters, the count is at most \(M_{n-1}\) if \(a\le b\), and zero otherwise. If only one supersequence uses a newly inserted first letter, the remaining comparability test can have at most \(T\) solutions. If both do, there is at most one tail comparison for each possible pair of inserted first letters.

Suppose first that \(a\le b\), and write \(t=b-a\) (so \(0\le t\le d\)). The numbers of permitted newly inserted first letters in the two mixed cases are \(b\) and \(q-a-1\); their sum is \(d+t\). The number of pairs \((c,e)\) with \(c\ne a\), \(e\ne b\), and \(c\le e\) is

\[
P=\frac{q(q+1)}2-(q-a)-(b+1)+1=\frac{qd}2-t.
\]

Consequently,

\[
L_{q,n}(u,v)\le M_{n-1}+(d+t)T+\frac{qd}2-t.
\]

The last two terms are maximized at \(t=d\), since the difference from that value is \((d-t)(T-1)\ge0\). Direct expansion gives

\[
M_n-M_{n-1}=2dT+\frac{d(d-1)}2,
\]

exactly the value for \(t=d\). Thus the desired bound follows in this case.

If instead \(a>b\), put \(t=a-b\ge1\). The main-main part is empty, the two mixed-case first-letter counts sum to \(q+1-t\), and the both-new-first-letter count is \(qd/2+t-1\). Therefore

\[
L_{q,n}(u,v)\le(q+1-t)T+\frac{qd}2+t-1
\le qT+\frac{qd}2.
\]

For all \(n\ge2\),

\[
M_n-\left(qT+\frac{qd}2\right)
=\frac{d(n-1)(2dn-d+1)}2>0.
\]

This completes the upper-bound induction for all received pairs, including pairs violating coordinatewise order.

**3. Attainment and uniqueness.** Let \(u=0^{n-1}\), \(v=d^{n-1}\). The \(1+nd\) supersequences of \(u\) are the all-zero word and the \(nd\) words with one nonzero entry; the supersequences of \(v\) are the all-\(d\) word and those with one entry smaller than \(d\). An incompatible source pair must have both exceptional entries at the same coordinate and their values \(c>e\). There are \(n\sum_{c=1}^{d}c=nqd/2\) such pairs. Thus precisely \((1+nd)^2-nqd/2=M_n\) valid source pairs produce this output.

For uniqueness when \(n\ge2\), the \(a>b\) case is strictly smaller. In the \(a\le b\) case, \(T-1=(n-1)d>0\), so equality forces \(t=d\), or \(a=0\), \(b=d\). It also forces the shorter pair \((U,V)\) to attain \(M_{n-1}\). By induction, \(U=0^{n-2}\) and \(V=d^{n-2}\) when \(n\ge3\); when \(n=2\) both tails are empty. Therefore the extremizer is unique as claimed. \(\square\)

## Verification

The accompanying `verify.py` independently enumerates all valid aligned source columns \((a,b)\) with \(a\le b\), enumerates distinct outputs from deleting one coordinate of each row, and tabulates the inverse-list sizes for each received pair. It verifies the formula and unique maximizer for all \(1\le n\le8\) when \(q=2\), all \(1\le n\le5\) when \(q=3\), all \(1\le n\le4\) when \(q=4\), and \(1\le n\le3\) when \(q=5,6\). Run `python3 verify.py` in a directory containing this file. These finite tests are consistency checks, not substitutes for the all-parameter induction above.

## Relationship to prior work

Dollma, Elishco and Yaakobi introduce the ordered composite channel and analyze single-deletion error correction in Section V of their 2025 manuscript [1], where the deletion affects one of two channels. Ye, Li, Lan and Ge study arbitrary row-specific deletion parameters and multiple affected rows in their 2026 manuscript [2], including the two-row deletion model underlying this theorem. Their deletion sections focus on code-cardinality bounds and constructions, rather than the sharp **reverse** ambiguity of one deletion in **each** row. The familiar \(q\)-ary one-insertion supersequence count is used as a starting point; the order-constrained comparison and its maximizing output are proved above. No assertion of a new general code-size bound or a coding construction is made.

## Limitations

The result is an unencoded worst-case inverse-list statement, not a maximum code-size theorem. It assumes exactly one deletion per labeled row, known source length, the componentwise order constraint and a common alphabet of size \(q\). It does not address multiple deletions per row, unknown channel labels, unequal alphabets, stochastic decoding or higher-resolution composite letters with more than two rows. An independently conducted mathematical review and exhaustive historical-priority determination have not been performed.

## References

[1] B. Dollma, O. Elishco, E. Yaakobi, *Coding for Ordered Composite DNA Sequences*, arXiv:2509.26119, first posted 30 September 2025, https://arxiv.org/abs/2509.26119 (Sections II and V and appendices in v3).

[2] Z. Ye, Y. Li, Z. Lan, G. Ge, *Bounds and Constructions of Codes for Ordered Composite DNA Sequences*, arXiv:2602.16406, first posted 18 February 2026, https://arxiv.org/abs/2602.16406 (Sections II-B, IV-B, V-B).
