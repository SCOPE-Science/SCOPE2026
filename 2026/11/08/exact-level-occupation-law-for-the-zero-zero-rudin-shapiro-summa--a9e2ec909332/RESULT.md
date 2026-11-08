# Exact level-occupation law for the zero-zero Rudin–Shapiro summatory function

## Finding
For each nonnegative integer \(n\), let \(z(n)\) be the number of overlapping occurrences of the block \(00\) in its *canonical* base-two expansion, with \(z(0)=0\), and define
\[
b(n)=(-1)^{z(n)},\qquad B(n)=\sum_{j=0}^{n}b(j).
\]
For each integer \(K\ge1\), define the total level occupation count
\[
c_{00}(K)=\#\{n\in\mathbb Z_{\ge0}:B(n)=K\}.
\]
There is a unique nonnegative integer \(r\) with \(u=2^r\) and \(2u-1\le K\le4u-2\). The exact, *finite* occupation count is
\[
\boxed{c_{00}(K)=
\begin{cases}
u,&2u-1\le K\le3u-2,\\
4u-2-K,&3u-1\le K\le4u-3,\\
u,&K=4u-2.
\end{cases}}
\]
In particular, the level counts along \(K=7,8,9,10,11,12,13,14,15\) are \(4,4,4,4,3,2,1,4,8\).

## Assumptions and scope
The binary expansion is unpadded: leading zeros are not inserted, and \(n=0\) has the empty word. Blocks are overlapping. Every asserted count includes *all* indices \(n\ge0\), not just a finite prefix. Define the classical Rudin–Shapiro sign and summatory functions by
\[
a(n)=(-1)^{\#11\text{ in the binary expansion of }n},\quad
s(n)=\sum_{j=0}^{n}a(j),\quad s(-1)=0.
\]
All symbols in the following proof are integer-valued.

## Proof
**1. Complementing one binary block.** For every \(m\ge0\) and \(0\le j<2^m\), the \(m\)-bit complement of \(j\) is \(2^m-1-j\). The word for \(2^m+j\) begins with \(1\), so its occurrences of \(00\) are exactly the occurrences of \(11\) in that complemented suffix. Therefore
\[
b(2^m+j)=a(2^m-1-j).
\]
Write \(A_m=s(2^m-1)\). The classical block-end identity is
\[
A_m=2^{\lceil m/2\rceil}\qquad(m\ge0).
\]
This is the published special-value identity in Rampersad–Shallit, Theorem 13(b); it also follows from the Rudin–Shapiro block relations stated below. Since \(B(0)=1\) and the entire block of indices from \(2^h\) to \(2^{h+1}-1\) contributes \(A_h\), we obtain
\[
D_m:=1+\sum_{h=0}^{m}A_h=
\begin{cases}
4\cdot2^r-2,&m=2r,\\
6\cdot2^r-2,&m=2r+1.
\end{cases}
\]
Summing the complement identity only through \(j\), rather than through the full block, gives the exact reversal
\[
\boxed{B(2^m+j)=D_m-s(2^m-2-j)}.
\]
The last argument is \(-1\) precisely when \(j=2^m-1\).

**2. The two exact histograms of the classical sum.** Let
\[
H_m(v)=\#\{0\le t<2^m:s(t)=v\}.
\]
For every \(r\ge0\) with \(u=2^r\),
\[
H_{2r}(v)=\begin{cases}v,&1\le v\le u,\\2u-v,&u<v<2u,\\0,&\text{otherwise},\end{cases}
\]
and
\[
H_{2r+1}(v)=\begin{cases}v,&1\le v<2u,\\u,&v=2u,\\0,&\text{otherwise}.\end{cases}
\]
Here is an induction establishing these formulas. For \(r=0\), the two distributions are \(H_0(1)=1\) and \(H_1(1)=H_1(2)=1\). For \(r\ge1\), the standard four-block Rudin–Shapiro translation and reflection relations (Rampersad–Shallit, Theorem 11; stated in full below) give
\[
H_{2r+2}(v)=H_{2r}(v)+H_{2r}(v-u)+H_{2r}(v-2u)+H_{2r}(3u-v).
\]
Substituting the displayed triangular formula yields the same triangle with \(u\) replaced by \(2u\).

To obtain the odd distribution, split the first \(4^r\) indices into halves. Denote their histograms by \(L(v)\) and \(R(v)\). The first is \(L=H_{2r-1}\), and \(R=H_{2r}-L\). In the next block, the first half is translated by \(u\) and the second reflected around \(3u\). Consequently
\[
H_{2r+1}(v)=H_{2r}(v)+L(v-u)+R(3u-v).
\]
For \(1\le v\le u\), this equals \(v\); for \(u<v<2u\), it equals \((2u-v)+(v-u)+(v-u)=v\); and at \(v=2u\), it equals \(u/2+u/2=u\). All other values vanish. The induction is complete. To be explicit, the four-block relations used above are, for \(0\le t<4^r\),
\[
\begin{aligned}
s(t+4^r)&=s(t)+u&&\text{if }t<4^r/2,\\
s(t+4^r)&=3u-s(t)&&\text{if }t\ge4^r/2,\\
s(t+2\cdot4^r)&=s(t)+2u&&\text{for all }t,\\
s(t+3\cdot4^r)&=3u-s(t)&&\text{if }t<4^r/2,\\
s(t+3\cdot4^r)&=u+s(t)&&\text{if }t\ge4^r/2.
\end{aligned}
\]
The first two are Theorem 11 (16)–(17); the third and the two last follow by applying Theorem 11 (18)–(19) to the appropriate shifted argument. All these identities hold for \(r\ge1\). The initial case \(H_2=(1,2,1)\) follows by direct four-term evaluation.

**3. Counting each disjoint binary block.** Let \(C_m(K)\) count indices in \([2^m,2^{m+1})\) where \(B(n)=K\). The reversal in Step 1 replaces the histogram argument \(t=2^m-1\) by \(t=-1\). Since \(s(2^m-1)=A_m\) and \(s(-1)=0\), it follows exactly that
\[
C_m(K)=H_m(D_m-K)-\mathbf1_{K=D_m-A_m}+\mathbf1_{K=D_m}.
\]
Inserting the two histograms yields, for even blocks \(m=2r\), \(u=2^r\),
\[
C_{2r}(K)=\begin{cases}
K-2u+2,&2u-1\le K\le3u-3,\\
u-1,&K=3u-2,\\
4u-2-K,&3u-1\le K\le4u-3,\\
1,&K=4u-2,\\
0,&\text{otherwise};
\end{cases}
\]
and, for odd blocks \(m=2r+1\), \(u=2^r\),
\[
C_{2r+1}(K)=\begin{cases}
u-1,&K=4u-2,\\
6u-2-K,&4u-1\le K\le6u-3,\\
1,&K=6u-2,\\
0,&\text{otherwise}.
\end{cases}
\]
Empty ranges contribute nothing. For \(u=2^r\) with \(r\ge1\), on the level shell \(2u-1\le K\le3u-2\), the odd block \(m=2r-1\) plus the even block \(m=2r\) contribute exactly \(u\) together. For \(3u-1\le K\le4u-3\) only the even block contributes \(4u-2-K\). At \(K=4u-2\), the even block contributes \(1\) and the following odd block contributes \(u-1\), totaling \(u\). All other blocks have zero contribution on the same shell. Finally \(n=0\) contributes one at \(K=1\); the exceptional initial shell \(K=1,2\) gives one each by the same block formulas. These disjoint shells exhaust all positive levels and prove the theorem.

**4. Finiteness.** The smallest level in a block of length \(2^{2r}\) is \(2^{r+1}-1\), apart from the explicitly handled endpoint overlaps. These lower bounds tend to infinity with \(r\), so no fixed positive level can occur at arbitrarily late indices. This justifies the use of a full infinite occupation count.

## Verification
The accompanying `verify.py` computes both sign sequences directly from independent binary bit patterns, validates the complemented-coefficient identity for every \(m\le15\), verifies all histograms \(H_m\) for \(0\le m\le15\), checks each individual block occupancy formula through \(m=13\), and checks complete occupation counts at levels \(1\le K\le100\) against the closed formula through \(2^{17}\) terms. These finite checks corroborate, but do not replace, the algebraic proof.

## Relationship to prior work
Rampersad and Shallit (arXiv:2302.00405, first posted 1 February 2023) prove the standard Rudin–Shapiro block relations in Theorem 11, count the classical sum's level occupations in Theorem 27, and introduce the canonical-zero-zero analogue in Section 11. Their Theorem 33 describes that analogue's recurrences and extrema, not its *total level-occupation distribution*. The present exact piecewise law concerns the latter. The OEIS entry A360535 records the analogue's definition and initial terms but not this occupation law. The proof explicitly uses previously known block identities and does not claim to rediscover them.

## Limitations
The result concerns only the canonical binary \(00\)-pattern analogue; it does not classify other adjacent-word parity sums or location statistics for the occurrences. Its originality has not undergone independent expert validation, and unindexed equivalents may exist.

## References
1. N. Rampersad and J. Shallit, *Rudin-Shapiro Sums Via Automata Theory and Logic*, arXiv:2302.00405 (first posted 2023-02-01), especially Theorems 11, 27, and 33 and Section 11. https://arxiv.org/abs/2302.00405 . Full open-access article: https://link.springer.com/article/10.1007/s00224-025-10214-1 .
2. OEIS A360535, *Analog of Rudin-Shapiro sum sequence A020986, based on counting patterns 00 instead of 11*, https://oeis.org/A360535 .
