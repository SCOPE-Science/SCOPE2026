# Eleven consecutive very triangular numbers at every triangular digit weight at least \(91\)

## Finding

Write \(T(n)=n(n+1)/2\) and let \(s_2(x)\) be the number of \(1\)s in the binary expansion of a nonnegative integer \(x\). A triangular number \(T(n)\) is **very triangular** when \(s_2(T(n))\) is itself a triangular number.

**Theorem.** For every integer \(t\ge 13\), put \(H=t(t+1)/2\). Then there are infinitely many positive integers \(N\) satisfying
\[
s_2(T(N+j))=H\qquad(0\le j\le 10).
\]
In particular, there are infinitely many blocks of eleven consecutive very triangular numbers with consecutive triangular indices, **at each prescribed triangular digit weight** \(H\ge91\).

The assertion is constructive. Put \(R=36{,}853{,}059\), and define \(L\) and \(q\) by
\[
(L,q)=\begin{cases}
((H-26)/2,\ 2^L-1),& H\text{ even},\\
((H-27)/2,\ 3(2^L-1)),& H\text{ odd}.
\end{cases}
\]
For every integer \(K\ge L+30\), one may take
\[
N=q\,2^K+R.
\]

## Assumptions and scope

Here \(t\) and \(K\) are arbitrary integers in the stated ranges, and \(j\) ranges over all eleven integers \(0,1,\ldots,10\). Every triangular integer \(H=t(t+1)/2\) with \(t\ge13\) is included. The two branches handle the parity of \(H\). In the odd branch \(L\ge32\); in the even branch \(L\ge47\). We do not claim eleven is maximal, that smaller triangular weights are impossible, or that blocks of arbitrary lengths exist.

## Proof

**Step 1: An exact eleven-term seed.** For \(r_j=R+j\), \(0\le j\le10\), the eleven exact integers \(T(r_j)\), in hexadecimal, are respectively

```
0x2699d3c61f266
0x2699d3e9447aa
0x2699d40c69cef
0x2699d42f8f235
0x2699d452b477c
0x2699d475d9cc4
0x2699d498ff20d
0x2699d4bc24757
0x2699d4df49ca2
0x2699d5026f1ee
0x2699d5259473b
```

Each listed number has exactly \(26\) set bits, as can be checked independently by counting the bits of each hexadecimal nibble. Thus
\[
s_2(T(r_j))=26\quad(0\le j\le10).
\]
Moreover, \(r_j<2^{26}\), \(2r_j+1<2^{27}\), and \(T(r_j)<2^{51}\).

**Step 2: Repunit weights.** For integers \(L\ge1\) and \(1\le A<2^L\), let \(B=2^L-1\). The exact disjoint-block identity
\[
AB=(A-1)2^L+(2^L-A)
\]
gives
\[
s_2(AB)=s_2(A-1)+s_2(2^L-1-(A-1))=L,
\]
because within exactly \(L\) bits the two summands' low-bit patterns are complementary. Taking \(A=B\) gives \(s_2(B^2)=L\).

For \(L\ge5\), there is also the exact identity
\[
9B^2=8\,2^{2L}+(2^L-18)2^L+9.
\]
The three terms have disjoint binary supports, and
\[
s_2(2^L-18)=L-s_2(17)=L-2.
\]
Consequently \(s_2(9B^2)=1+(L-2)+2=L+1\). Thus in the two branches
\[
s_2(q^2)=\begin{cases}L,&q=B,\\ L+1,&q=3B.\end{cases}
\]

**Step 3: Separate the binary blocks.** For any \(j\in\{0,\ldots,10\}\), write \(r=r_j\). Direct multiplication gives
\[
T(q2^K+r)=q^2 2^{2K-1}+q(2r+1)2^{K-1}+T(r).
\]
Since \(K\ge L+30\) and \(q<3\,2^L\), the seed bounds imply
\[
q(2r+1)<3\,2^{L+27}<2^{L+29}\le2^{K-1}<2^K,
\]
while \(T(r)<2^{51}<2^{K-1}\). Therefore the three displayed terms occupy disjoint binary blocks: the low block lies below position \(K-1\), the middle block occupies positions \(K-1\) through at most \(2K-2\), and the high block begins at position \(2K-1\). No binary carries occur between them. Hence
\[
s_2(T(q2^K+r))=s_2(q^2)+s_2(q(2r+1))+26.
\]

If \(H\) is even then \(q=B\) and \(1\le 2r+1<2^L\), since \(L\ge47\). The repunit lemma gives \(s_2(q(2r+1))=L\). The total equals \(26+2L=H\).

If \(H\) is odd then \(q=3B\), \(L\ge32\), and \(1\le3(2r+1)<2^{29}<2^L\). Applying the same lemma with \(A=3(2r+1)\) gives \(s_2(q(2r+1))=L\). The total equals \(26+(L+1)+L=27+2L=H\).

This holds simultaneously for all eleven indices, as required. Finally, for fixed \(H\), the quantity \(N=q2^K+R\) increases strictly as the unbounded integer \(K\) increases. Thus each prescribed \(H\) yields infinitely many distinct blocks. \(\square\)

## Verification

The accompanying standalone `check.py` recomputes the eleven seed values using integer arithmetic, checks their binary weights and the displayed hexadecimal list, directly tests both repunit identities for sample \(L\), and evaluates the complete eleven-number construction for all triangular weights from \(t=13\) to \(t=26\). The infinite quantifiers are proved by the algebra above; the finite checks are not substituted for that argument.

For example, at \(H=91\) one has \(L=32\), \(q=3(2^{32}-1)\), and any \(K\ge62\) yields eleven consecutive triangular numbers all having exactly \(91\) set bits.

## Relationship to prior work

Baumheckel and Forgács, *An Exploration of Very Triangular Numbers* (first publicly posted 19 May 2021), study triangular numbers whose binary digit sum is triangular. Their Theorem 2.2 ensures isolated very triangular numbers at prescribed triangular weights, their Proposition 3.9 proves a digit-weight preservation mechanism over certain shifted binary-power indices, and Corollary 3.10 proves infinitely many blocks of **six** consecutive very triangular numbers. Their Conjecture 3.7 concerns arithmetic progressions of arbitrary length. The present theorem supplies explicit **eleven-term consecutive-index blocks at every triangular digit weight \(H\ge91\)**, which does not follow from the published six-term assertion or the isolated prescribed-weight theorem. The digit-block technique is related in spirit, but the explicit seed, two repunit branches and combined fixed-weight lifting are separately proved here.

The original paper and publicly visible mathematical-result records were compared by mathematical implication, not title similarity. No statement forcing eleven consecutive indices at all sufficiently large triangular weights was found in the material inspected. Absence from search results is not a proof of priority.

## Limitations

This is an existence theorem, not an optimal block-length theorem. It does not resolve arbitrary-length arithmetic progressions, arbitrarily long consecutive runs, the first occurrence of an eleven-block, or the optimal threshold for triangular digit weights. The constructed indices are extremely large. An equivalent theorem could be present in unindexed or otherwise inaccessible literature. The finite seed is independently checkable, while the infinite construction depends on the elementary repunit and no-carry identities in the proof. No independent audit has been performed.

## References

1. A. Baumheckel and T. Forgács, *An exploration of very triangular numbers*, arXiv:2105.10354, first posted 19 May 2021, revised 2023. https://arxiv.org/abs/2105.10354 ; full text https://arxiv.org/pdf/2105.10354 .
2. A. Baumheckel and T. Forgács, *An Exploration of Very Triangular Numbers*, PUMP, DOI:10.46787/pump.v6i0.3853, https://doi.org/10.46787/pump.v6i0.3853 .
3. OEIS A344603, sequence concerning very triangular numbers, https://oeis.org/A344603 . (Contextual sequence data; not a uniqueness or novelty certificate.)
