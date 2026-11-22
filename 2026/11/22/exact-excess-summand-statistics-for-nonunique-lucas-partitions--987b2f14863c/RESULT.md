# Exact excess-summand statistics for nonunique Lucas partitions

## Finding

Let \(L_0=2\), \(L_1=1\), and \(L_{i+2}=L_{i+1}+L_i\). For each integer \(m\ge3\), a *cutoff Lucas partition* of an integer is a set \(I\subseteq\{0,\ldots,m\}\) of nonconsecutive indices, with sum \(\sum_{i\in I}L_i\). Among integers with two different such partitions, call the partition containing the pair of indices \(\{0,2\}\) *redundant* and the other *canonical*. Define the *summand excess* \(\Delta\) to be the cardinality of the redundant index set minus the cardinality of the canonical set.

Every integer has at most two cutoff partitions, and any double-represented integer has exactly one partition of each kind. For each integer \(j\ge0\), the number of different positive integers with two cutoff partitions and \(\Delta=j\) is exactly

\[
N_m(j)=\begin{cases}
F_{m-2j-2},&0\le j\le\lfloor(m-3)/2\rfloor,\\
0,&\text{otherwise},
\end{cases}
\]
where \(F_0=0\), \(F_1=1\), and \(F_{r+2}=F_{r+1}+F_r\). Hence the complete weighted generating function is

\[
\sum_{m\ge3}\sum_{j\ge0}N_m(j)z^m u^j=\frac{z^3}{(1-z-z^2)(1-uz^2)}.
\]

The total number \(B_m=\sum_jN_m(j)\) of double-represented integers equals \(F_{m-1}\) if \(m\) is odd, and \(F_{m-1}-1\) if \(m\) is even. If one of these \(B_m\) integers is chosen uniformly, its excess converges, as \(m\to\infty\), to the geometric distribution
\[
\Pr(\Delta=j)=\varphi^{-(2j+1)}
=(1-\varphi^{-2})\varphi^{-2j}\quad(j\ge0),
\qquad\varphi=\frac{1+\sqrt5}{2}.
\]
In particular, the limiting mean is \(\varphi^{-1}\) and the limiting variance is exactly \(1\).

## Assumptions and scope

Indices are distinct and no consecutive indices are selected. The two initial Lucas terms have values \(2\) and \(1\), so the index order—not a numeric ordering of the terms—determines admissibility. The cutoff is on the *largest allowed index*, not on the represented integer's numerical value. A double-represented integer is counted only once, regardless of how many of its two partitions have a given number of terms. Excess \(0\) is allowed; indeed the first duplicated integer \(5\) has two summands in both partitions. This is not a statement about partitions with repeated terms, arbitrary positive recurrence sequences or all integer-value cutoffs.

## Proof

**1. Canonical uniqueness and range.** For any \(m\ge1\), impose the usual nonadjacency condition and additionally forbid simultaneous use of indices \(0\) and \(2\). Write \(C_m\) for the set of sums of these canonical subsets of \(\{0,\ldots,m\}\). For \(m=1\), these sums are exactly \(\{0,1,2\}=\{0,\ldots,L_2-1\}\), each once; for \(m=2\), the sums are \(\{0,1,2,3\}=\{0,\ldots,L_3-1\}\), again once. For every \(m\ge3\), subsets not using index \(m\) have the values \(C_{m-1}\); those using index \(m\) have the values \(L_m+C_{m-2}\). By induction these are the disjoint integer intervals \([0,L_m-1]\) and \([L_m,L_m+L_{m-1}-1]\), whose union is \([0,L_{m+1}-1]\). The induction also proves uniqueness. Thus every nonnegative integer has one global canonical partition, and one with indices at most \(m\) if and only if it is less than \(L_{m+1}\).

**2. Distinct redundant partitions give distinct sums.** Any nonconsecutive partition containing both indices \(0\) and \(2\) has a tail that is an independent subset of indices \(4,5,\ldots\). Let \(U_t\) be the maximal sum of such a tail using indices at most \(t\), with \(U_2=U_3=0\). For \(t\ge4\),
\[
U_t=\max\{U_{t-1},L_t+U_{t-2}\}.
\]
The base inequalities \(U_3=0<L_4\) and \(U_4=L_4<L_5\), together with the recurrence for \(L_t\), give \(U_t<L_{t+1}\) by induction. If two different tails have highest differing index \(r\ge4\), remove common terms; the side containing \(r\) then has remaining sum at least \(L_r\), while the other has remaining sum at most \(U_{r-1}<L_r\). Therefore the two sums differ. Every integer has at most one redundant representation; together with step 1 it has at most two representations.

**3. Unique initial even block.** Every redundant partition has a uniquely determined maximal initial block of even indices
\[
\{0,2,4,\ldots,2j+2\}\qquad(j\ge0),
\]
followed by an arbitrary nonconsecutive tail \(T\subseteq\{2j+5,\ldots,m\}\): index \(2j+4\) is absent by maximality, and the intervening odd indices up to \(2j+3\) are absent by nonadjacency. The exact recurrence identity
\[
\sum_{i=0}^{j+1}L_{2i}=1+L_{2j+3}
\]
is obtained by telescoping \(L_{2i}=L_{2i+1}-L_{2i-1}\) for \(i\ge1\) and using \(L_0=2\). Consequently the unique canonical partition of the same integer is
\[
\{1,2j+3\}\cup T.
\]
It is admissible, since its displayed initial indices are nonadjacent and every index in \(T\) is at least \(2j+5\). Its number of terms is \(2+|T|\), versus \(j+2+|T|\) for the redundant partition, so \(\Delta=j\). Both partitions lie below cutoff \(m\) exactly when \(m\ge2j+3\). If \(m=2j+2\), the canonical partition necessarily uses the forbidden index \(m+1\), and step 1 rules out any other canonical partition inside the cutoff. The injectivity in step 2 rules out another redundant partition.

**4. Exact counts and generating function.** At \(m=2j+3\), the tail is empty, so there is exactly one such integer; this equals \(F_1\). For \(m\ge2j+4\), there are \(h=m-2j-4\) possible tail indices, and their admissible subsets are exactly independent sets on a path of \(h\) vertices. The path-independent-set count obeys \(P_h=P_{h-1}+P_{h-2}\), with \(P_0=1\), \(P_1=2\), hence \(P_h=F_{h+2}=F_{m-2j-2}\). Distinct tails yield different values by step 2; the normal form yields no other values. This proves the complete formula for \(N_m(j)\). Reindexing \(m=2j+3+h\) with \(h\ge0\) gives
\[
\sum_{m,j}N_m(j)z^mu^j
=z^3\left(\sum_{j\ge0}(uz^2)^j\right)
\left(\sum_{h\ge0}F_{h+1}z^h\right),
\]
which is the claimed rational function. Summing \(N_m(j)\) over \(j\) by the Fibonacci recurrence gives \(F_{m-1}\) for odd \(m\) and \(F_{m-1}-1\) for even \(m\).

**5. Limiting distribution and moments.** For fixed \(j\), Binet's formula implies
\[
\frac{F_{m-2j-2}}{B_m}\longrightarrow\varphi^{-(2j+1)}.
\]
These limiting masses sum to \(1\), since \(1-\varphi^{-2}=\varphi^{-1}\). In addition, the Fibonacci bounds \(F_n\le\varphi^{n-1}\) for \(n\ge1\) and \(B_m\ge c\varphi^m\) for all sufficiently large \(m\), with fixed \(c>0\), give a uniform exponential domination \(N_m(j)/B_m\le C\varphi^{-2j}\). Dominated convergence therefore applies to all moments. For a geometric distribution with ratio \(q=\varphi^{-2}\), the mean is \(q/(1-q)=\varphi^{-1}\) and the variance is \(q/(1-q)^2=1\). These are the asserted limiting moments.

## Verification

The standalone standard-library Python program `CHECK.py` exhaustively enumerates all nonconsecutive index subsets for every \(3\le m\le24\), groups them by their integer value, tests the existence and uniqueness of the redundant member of every double-representation pair, and checks the *entire* histogram against \(N_m(j)\), along with its total. At \(m=24\), it finds \(28{,}656\) different double-represented integers among \(167{,}762\) different represented values. The finite checker provides corroboration, not a proof for all \(m\); the unbounded proof consists of steps 1–5 above.

## Relationship to prior work

Brown (1969) established existence and uniqueness of a Lucas representation under the extra constraint forbidding simultaneous terms of indices \(0\) and \(2\). Chu, Luo, and Miller (first public arXiv version April 17, 2020; journal 2022) proved the at-most-two theorem and the exact unweighted doubly-represented-value set, including a Beatty-type enumeration and density. Their Section 5, especially Table 3, explicitly enumerates the *redundant* partitions, which the present analysis takes as its starting object. Shallit (arXiv 2023, Section 5, Theorem 5.2) gives an automaton-based identification of the same unweighted set with a base-\(\varphi\) digit property. The new claim concerns a different statistic: the exact **difference in the numbers of summands of the two partitions**, at every index cutoff, with a two-variable generating function and limiting geometric distribution. These are not stated in the inspected prior texts, though the derivation depends on their classical representation setting. The available database OEIS A342089 lists the unweighted double-represented integers rather than this paired summand-excess histogram.

## Limitations

The result is specific to nonconsecutive distinct indexed Lucas summands and an index cutoff; it does not classify duplicated representations in general recurrences. All partitions are counted by index sets rather than by arbitrary summand order. It is possible that an equivalent weighted statement is implicit in another source, an automaton computation, or an unpublished note; failure to locate one is not proof of worldwide priority. The proof has not been independently audited.

## References

- J. L. Brown, Jr., *Unique Representations of Integers as Sums of Distinct Lucas Numbers*, *Fibonacci Quarterly* 7 (1969), 243–252. https://www.fq.math.ca/Scanned/7-3/brown.pdf
- H. V. Chu, D. C. Luo, and S. J. Miller, *On Zeckendorf Related Partitions Using the Lucas Sequence*, arXiv:2004.08316 (first version April 17, 2020), *Fibonacci Quarterly* 60 (2022), 111–119. https://web.williams.edu/Mathematics/sjmiller/public_html/math/papers/Lucas_ChuLuoMiller10_FQ.pdf
- J. Shallit, *Proving Properties of \(\varphi\)-Representations with the Walnut Theorem-Prover*, arXiv:2305.02672 (first version May 4, 2023), especially Section 5, Theorem 5.2. https://arxiv.org/pdf/2305.02672
- The On-Line Encyclopedia of Integer Sequences, A342089, https://oeis.org/A342089.
