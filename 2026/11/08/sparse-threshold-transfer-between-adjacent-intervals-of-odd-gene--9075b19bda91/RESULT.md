# Sparse threshold transfer between adjacent intervals of odd generators

## Finding
For an integer \(a\ge4\), define two generator sets
\[
A_a^- = \{2a+1,2a+3,\ldots,4a+1\},\qquad A_a^+=A_a^-\cup\{4a+3\}.
\]
Let \(r_A(n)\) count nonnegative multiplicity-vector representations of \(n\) by \(A\), including \(r_A(0)=1\). For \(p\ge0\), the **threshold-transfer set** is
\[
E_{a,p}=\{n\in\mathbb Z_{\ge0}:r_{A_a^-}(n)\le p<r_{A_a^+}(n)\}.
\]
For every \(0\le p\le\lfloor(a+1)/2\rfloor\), this set is *exactly*
\[
E_{a,p}=\begin{cases}
\{4a+3\},&p=0,\\
\{8a,8a+2,8a+4,8a+6\},&p=1,\\
\{6a+4\},&a\text{ odd and }p=(a+1)/2\ge2,\\
\{8a-4p+4,8a-4p+6\},&2\le p\le\lfloor(a+1)/2\rfloor\text{ otherwise.}
\end{cases}
\]
No larger integers or other residues are exceptional. In particular, the number of integers having at most \(p\) representations drops by only \(1\), \(4\), or \(2\) when the final generator is adjoined. At the maximal permitted threshold for odd \(a\), this drop is only \(1\). The sums of the lost integers are respectively \(4a+3\), \(32a+12\), \(6a+4\) at the odd endpoint, and \(16a-8p+10\) in the ordinary \(p\ge2\) case.

As additional exact consequences, writing \(g_p^\pm(a)=\#\{n\ge0:r_{A_a^\pm}(n)\le p\}\), one has
\[
(g_0^-(a),g_0^+(a))=(4a,4a-1),\qquad
(g_1^-(a),g_1^+(a))=(5a+10,5a+6).
\]

## Assumptions and scope
The parameter \(a\) is any integer at least \(4\), and \(p\) ranges over the explicitly stated integer interval. Representations are multisets of generators, equivalently nonnegative coefficient vectors; permutations of summands do not count separately. The zero integer has one empty representation. The threshold sets have finite complements in the nonnegative integers, although for \(p\ge1\) they need not contain zero.

Set \(b=2a+1\). Every residue modulo \(b\) is represented uniquely by \(2s\) for \(0\le s\le2a\). The least nonnegative member in the corresponding arithmetic progression is \(q_0(s)b+2s\), where \(q_0(s)=0\) for \(0\le s\le a\) and \(q_0(s)=-1\) for \(a+1\le s\le2a\).

## Proof
Write \(A_L=\{b+2t:0\le t\le L\}\), with \(L=a\) or \(L=a+1\). If \(qb+2s\) has a representation by exactly \(h\) generators, its indices satisfy
\[
2\sum_{i=1}^h t_i=(q-h)b+2s.
\]
Since \(b\) is odd and \(0\le s<b\), necessarily \(h\equiv q\pmod2\) and \(h\le q\). For \(q=1,2,3,4\), the representation counts are respectively: (i) at most one, arising from one index \(t=s\); (ii) the number \(P_{2,L}(s)\) of unordered pairs \(0\le t_1\le t_2\le L\) with sum \(s\); (iii) the number \(P_{3,L}(s)\) of unordered triples in \([0,L]\) summing to \(s\); (iv) the four-part count \(P_{4,L}(s)\), plus one extra two-part representation only for \(L=a+1\) and \(s\in\{0,1\}\). In the last case the added pair is \((a,a+1)\) or \((a+1,a+1)\), respectively. The \(q=0,-1\) candidates do not exceed one representation. All these descriptions follow from the displayed equation; in particular, the potential one-part contribution to \(q=3\) requires \(t=b+s>L\), hence is impossible.

For \(a+1\le s\le2a\), direct pair counting gives
\[
P_{2,a}(s)=a-\lceil s/2\rceil+1,\qquad
P_{2,a+1}(s)=a-\lceil s/2\rceil+2.
\]
Also, for every \(a\le s\le2a\), the triple count \(P_{3,a}(s)\) exceeds \(\lfloor(a+1)/2\rfloor\). Indeed, the coefficients of the \(3\)-by-\(a\) Gaussian binomial polynomial are symmetric and unimodal, so their minimum on this range is \(P_{3,a}(a)\). This is larger than \(\lfloor(a+1)/2\rfloor\): for even \(a\), its two-part subcount is already sufficient, while for odd \(a\ge5\) the partition \((a-2,1,1)\) supplies an additional three-part representation. Thus the \(q=3\) candidate always exceeds every permitted threshold in these upper residues, for both generator sets.

We also need a universal bound for the few small residues. For every \(0\le s\le a+1\), the count of representations of \(5b+2s\) by \(A_a^-\) exceeds \(\lfloor(a+1)/2\rfloor\). For \(0\le s\le a-1\), representations with five summands give all partitions of \(s\) into at most five parts, while representations with three summands correspond, by \(t_i\mapsto a-t_i\), to partitions of \(a-1-s\) into at most three parts. The two- and three-part subcounts give at least
\[
\left\lfloor\frac{s}{2}\right\rfloor+
\left\lfloor\frac{a-1-s}{2}\right\rfloor+2.
\]
For even \(a\), this already exceeds the stated threshold. For odd \(a\), equality in this lower bound is possible only with odd \(s\) and odd \(a-1-s\), and one of those two numbers is at least \(3\); a genuine three-part partition then raises the count strictly. For \(s=a\), two-part partitions of \(a\), together with a distinct three-part partition, suffice. For \(s=a+1\), the \(\lfloor(a+1)/2\rfloor\) allowed two-part partitions and the separate partition \((a-1,1,1)\) suffice. These are five-summand representations. Since \(A_a^-\subset A_a^+\), the same lower bound holds for \(A_a^+\).

Define \(q_{L,p}(s)\) to be the least \(q\ge q_0(s)\) for which \(r_{A_L}(qb+2s)>p\). Adding \(b\) to a representation injects the representation sets, so every larger \(q\) also exceeds \(p\). The preceding bounds ensure that \(q_{L,p}(s)\le5\) for every residue.

For \(p\ge2\), the two \(q\)-thresholds agree whenever \(0\le s\le a\): the counts for \(q=1,2,3\) agree, the sole difference at \(q=4\) adds just one representation to an existing single representation at \(s=0,1\), leaving both counts at most \(2\le p\); and the \(q=5\) counts already exceed \(p\). For \(a+1\le s\le2a\), both \(q=3\) candidates exceed \(p\), so the two thresholds differ by exactly one if and only if
\[
P_{2,a}(s)=p,\qquad P_{2,a+1}(s)=p+1.
\]
The pair formulas show that this occurs precisely when
\[
s\in\{2a-2p+1,\;2a-2p+2\}\cap[a+1,2a].
\]
Both positions are present except when \(a\) is odd and \(p=(a+1)/2\), in which case only the second is present. The unique integer gained in each such residue is \(2b+2s\), which yields the stated explicit exceptional values.

For \(p=1\), the first exceeding counts for \(s=0,1\) occur at \(q=4\) in \(A_a^+\) and \(q=5\) in \(A_a^-\). For \(2\le s\le2a-2\), both sets have at least two two-summand representations at \(q=2\). For \(s=2a-1,2a\), \(A_a^-\) has only one two-summand representation, \(A_a^+\) has two, and both have at least two at \(q=3\). Thus the gained integers are \(4b,4b+2,2b+4a-2,2b+4a\), exactly the four consecutive evens stated.

For \(p=0\), the single exceptional residue is \(s=a+1\): the additional generator \(b+2(a+1)=4a+3\) supplies one representation at \(q=1\), whereas the shorter progression first represents that residue at \(q=2\). All other residue thresholds agree.

Finally, there is exactly one gained integer in each shifted residue. Consequently the differences in the numbers and sums of excluded integers follow by counting or summing the displayed finite sets. At \(p=0\) the individual counts follow by summing the residue thresholds \(q_{L,0}(s)-q_0(s)\); at \(p=1\) the threshold arrays are \(q_{a,1}(0)=q_{a,1}(1)=5\), \(q_{a,1}(s)=2\) for \(2\le s\le2a-2\), \(q_{a,1}(2a-1)=q_{a,1}(2a)=3\), whereas \(q_{a+1,1}(0)=q_{a+1,1}(1)=4\) and all other entries equal \(2\). Summing again establishes the two individual \(p=1\) genus formulas.

## Verification
The companion script `verify.py` independently counts multiplicity-vector representations by dynamic programming, capped at the largest threshold needed. It compares the exceptional set against direct enumeration for every \(a=4,\ldots,150\) and every integer \(0\le p\le\lfloor(a+1)/2\rfloor\), over a range of \(20a+100\) integers. The direct count agrees in all \(5{,}843\) parameter instances. These finite tests are checks, not the proof of the universal statement; the residue-by-residue argument above covers all nonnegative integers and all admitted parameters.

Run `python3 verify.py` with standard Python 3; no external packages or files are required.

## Relationship to prior work
Komatsu, Hyun, and Song [1] (first made public August 14, 2026) study the two *same* odd-generator families, proving formulas for their \(p\)-Frobenius numbers for the range considered here. They do not state the complete set of integers whose representation threshold changes when the extra generator is adjoined, or the exact difference of the \(p\)-genera. Their partition-counting framework is related, but determining these sets requires a residue-wise comparison through the four- and five-summand layers and a special maximal-threshold boundary check. The general \(p\)-Apéry identity for genus in Komatsu [2] alone does not give these exceptional sets; the earlier consecutive-*integer* family studied by Komatsu and Pandey [3] differs from the two odd arithmetic progressions here. O'Hara's Gaussian-unimodality theorem [4] supplies the standard ingredient for the triple-partition lower bound.

## Limitations
The formulas assume \(a\ge4\) and \(p\le\lfloor(a+1)/2\rfloor\). They do not classify threshold transfer for larger \(p\) or for arbitrary shifted arithmetic progressions. Historical novelty has not undergone independent verification; an unindexed earlier identity or an unstated derivation in related literature remains possible. The main analytic proof is self-contained apart from standard Gaussian polynomial unimodality.

## References
[1] T. Komatsu, S. Hyun, K. Song, *\(p\)-numerical semigroup of the sequence of consecutive odd integers*, arXiv:2608.14053 (2026-08-14), https://arxiv.org/html/2608.14053 .

[2] T. Komatsu, *Arithmetic approach to \(p\)-numerical semigroups* (2023), https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2264-01.pdf . See its general \(p\)-Apéry/genus identity.

[3] T. Komatsu, R. K. Pandey, *\(p\)-numerical semigroup of the sequence of consecutive integers*, Bull. Korean Math. Soc. 62 (2025), 1397–1409.

[4] K. M. O'Hara, *Unimodality of Gaussian coefficients: a constructive proof*, J. Combin. Theory Ser. A 53 (1990), 29–52.
