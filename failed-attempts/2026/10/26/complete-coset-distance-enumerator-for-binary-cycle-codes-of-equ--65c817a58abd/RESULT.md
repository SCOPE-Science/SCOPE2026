# Complete coset-distance enumerator for binary cycle codes of equal-arm book-graph 2-sums

## Finding

Let \(c\ge2\) and \(n\ge3\) be integers. Form a graph \(G_{c,n}\) by taking the \(2\)-sum of two book graphs \(B_{n,c}\) along their common-edge positions: equivalently, \(G_{c,n}\) consists of \(m=2c\) internally vertex-disjoint paths of common edge length \(L=n-1\), joining two endpoints. Let \(C_{c,n}\subseteq\mathbb F_2^{mL}\) be its binary cycle code, the kernel of its vertex-edge incidence matrix. For any coset \(u+C_{c,n}\), write \(\delta(u+C_{c,n})=\min_{v\in u+C_{c,n}}\operatorname{wt}(v)\), and define the complete coset-distance enumerator
\[
D_{m,L}(z)=\sum_{u+C_{c,n}\in\mathbb F_2^{mL}/C_{c,n}} z^{\delta(u+C_{c,n})}.
\]
Put \(h=\lfloor(L-1)/2\rfloor\) and
\[
F_j(z)=\sum_{a=0}^{j}\binom{L}{a}z^a\quad(0\le j\le h),\qquad F_{-1}(z)=0,
\]
\[
F(z)=F_h(z),\qquad G(z)=2F(z)+\mathbf1_{2\mid L}\binom{L}{L/2}z^{L/2}.
\]
Then, for **every** \(c\ge2,n\ge3\),
\[
\boxed{D_{m,L}(z)=2^{1-m}G(z)^m-F(z)^m+
\sum_{j=0}^{h}z^{L-2j}\bigl(F_j(z)^m-F_{j-1}(z)^m\bigr).}
\]
In particular, the covering radius and the number of cosets attaining it are
\[
\boxed{R_{m,L}=\begin{cases}mL/2,&L\text{ even},\\m(L-1)/2+1,&L\text{ odd},\end{cases}}
\]
\[
\boxed{[z^{R_{m,L}}]D_{m,L}(z)=
\begin{cases}2^{1-m}\binom{L}{L/2}^{m},&L\text{ even},\\
\binom{L}{(L-1)/2}^{m},&L\text{ odd}.
\end{cases}}
\]
For a binary symmetric channel of crossover probability \(0\le p\le1/2\), its exact maximum-likelihood **block success probability**, with any tie-breaking rule, is
\[
\boxed{P_{\mathrm{success}}(p)=\sum_{i=0}^{R_{m,L}}[z^i]D_{m,L}(z)\,p^i(1-p)^{mL-i}.}
\]
These last expressions are corollaries; the main classification is the **entire all-parameter coset-distance distribution**.

## Assumptions and scope

All codes and received words are binary; Hamming distance and Hamming weight are used. The construction assumes \(m=2c\ge4\) equal-length arms with \(L=n-1\ge2\); the two branch vertices are distinct and all internal path vertices are distinct. Cosets are counted as distinct subsets, not by the number of minimum-weight vectors they contain. The source is the first public version, dated October 3, 2026, of the book-graph code construction in the references; the theorem here concerns additional covering/decoding invariants, not the source's stated code parameters.

## Proof

**1. Code identification.** At each degree-two internal vertex of an arm, the binary incidence constraint forces its two consecutive edge coordinates to be equal. Thus every cycle-code word is constant on each of the \(m\) arms. The incidence constraint at either branch vertex says that the \(m\) arm constants have even sum. Conversely, these conditions imply every vertex constraint, so, after ordering coordinates by arm,
\[
C_{c,n}=\{(b_1\mathbf1_L,\ldots,b_m\mathbf1_L):b_i\in\mathbb F_2,\ \sum_i b_i=0\}.
\]
Consequently \(\dim C_{c,n}=m-1\) and each coset contains precisely \(2^{m-1}\) binary words.

**2. Exact distance of an arbitrary received word.** Break \(y\in\mathbb F_2^{mL}\) into \(m\) consecutive blocks, and let \(w_i\) be the number of ones in block \(i\). Set \(a_i=\min(w_i,L-w_i)\), \(0\le a_i\le\lfloor L/2\rfloor\). If some block has exactly \(L/2\) ones, both possible constant words on that block have the same cost \(a_i\); its choice can enforce even parity, and therefore
\[
\delta(y+C_{c,n})=\sum_{i=1}^{m}a_i.
\]
Otherwise the unique preferred arm constant \(b_i\) is \(0\) for \(w_i<L/2\) and \(1\) for \(w_i>L/2\). If \(\sum_i b_i\) is even, all preferred constants are admissible, with cost \(\sum_i a_i\). If this sum is odd, at least one arm constant must flip. Flipping arm \(i\) costs an additional \(L-2a_i>0\), so the optimal choice flips exactly one arm with minimum extra cost. Hence in this case
\[
\delta(y+C_{c,n})=\sum_i a_i+L-2\max_i a_i.
\]
There is no benefit from three or more flips because every individual flip has positive additional cost.

**3. Enumerate by local costs.** For every \(0\le j\le h\) there are \(\binom Lj\) binary blocks of preferred constant \(0\), and equally many of preferred constant \(1\), each with local cost \(j\). A tied block, occurring only for even \(L\), contributes \(\binom L{L/2}\) blocks of cost \(L/2\). Thus the weight-generating polynomial for arbitrary words by summed local costs is \(G(z)^m\), whereas words with no ties have polynomial \((2F(z))^m\).

For every fixed vector of non-tied local costs, exactly half the \(2^m\) preferred-label choices have even parity and half have odd parity. After division by the coset size \(2^{m-1}\), the sum of contributions of the even-parity words with no ties is \(F(z)^m\). The tied words contribute
\[
2^{1-m}\left(G(z)^m-(2F(z))^m\right).
\]
For the odd-parity words without ties, group each local-cost vector according to its maximum \(j=\max_i a_i\). The polynomial of those vectors with maximum exactly \(j\) is \(F_j(z)^m-F_{j-1}(z)^m\); the added distance is \(L-2j\). Their contribution after dividing by \(2^{m-1}\) is therefore
\[
\sum_{j=0}^h z^{L-2j}\bigl(F_j(z)^m-F_{j-1}(z)^m\bigr).
\]
Adding these three disjoint classes yields the boxed polynomial identity. Each summand was obtained by counting actual received words and dividing by the exactly uniform coset size, so the coefficients are precisely the numbers of distinct cosets.

**4. Deepest cosets.** For even \(L=2s\), every local cost is at most \(s\). A tied block permits the cost \(\sum_i a_i\le ms\), with equality precisely when all blocks are tied. In the no-tie odd-parity case put \(t_i=s-a_i\ge1\); the cost is
\[
ms-\sum_i t_i+2\min_i t_i\le ms-(m-2)\min_i t_i<ms,
\]
using \(m\ge4\). The even-parity case with no ties is also strictly below \(ms\). Exactly \(\binom Ls^m\) received words have every block tied, yielding \(2^{1-m}\binom Ls^m\) deepest cosets.

For odd \(L=2s+1\), put \(t_i=s-a_i\ge0\). The even-parity cost is at most \(ms\). The odd-parity cost is
\[
ms+1-\sum_i t_i+2\min_i t_i\le ms+1-(m-2)\min_i t_i\le ms+1.
\]
For \(m\ge4\), equality requires all \(t_i=0\). Taking all \(a_i=s\) and an odd number of preferred-one blocks attains \(ms+1\). There are \(2^{m-1}\binom Ls^m\) such received words, hence \(\binom Ls^m\) deepest cosets. These arguments prove the radius and deepest-coset formulas exactly.

**5. Channel probability.** For \(p\in[0,1/2]\), the most likely error within a fixed coset has minimum Hamming weight; all minimum-weight ties have equal probability. Maximum-likelihood syndrome decoding chooses any one such representative. The all-zero codeword may be assumed sent by channel and code symmetry. Summing the probabilities \(p^{\delta}(1-p)^{mL-\delta}\) for the chosen representative in each coset proves the block-success formula. For \(p=1/2\), every representative has equal probability and the same identity holds.

## Verification

A standalone exact-arithmetic verifier, `verify_coset.py`, constructs the codewords directly as binary masks, enumerates **every** received word for the parameter pairs \((m,L)=(4,2),(4,3),(4,4),(6,2)\), and independently computes coset distances by minimizing Hamming distance to the full code. These independent spectra match the closed polynomial coefficient by coefficient:
\[
\begin{aligned}
D_{4,2}(z)&=1+8z+13z^2+8z^3+2z^4,\\
D_{4,3}(z)&=1+12z+66z^2+163z^3+189z^4+81z^5.
\end{aligned}
\]
The verifier also evaluates the closed formula at all \(m\in\{4,6,8,10\}\), \(2\le L\le12\), checking integer nonnegative coefficients, the identity \(D_{m,L}(1)=2^{mL-m+1}\), the radius, and the predicted deepest-coset multiplicity. It prints `VERIFY_OK`. To reproduce: run `python3 verify_coset.py` using Python 3 standard library. These finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Barbosa, Marquezino, and La Guardia (arXiv:2610.04617v1, 2026, Section 3.2) introduce the book-graph \(2\)-sum construction and prove its code length, dimension and minimum distance, including several optimum-distance examples. Their stated result does not enumerate all coset distances, the number of deepest cosets, or the exact BSC maximum-likelihood block-error law. The reduction to an even-parity repetition-block code is established explicitly here and is not presented as a new generic code construction.

Solé and Zaslavsky (1993) relate graph-cycle-code covering radius to minimum \(T\)-joins, provide general bounds and solve examples. A radius identity by itself does not imply the full polynomial of coset counts, and this work claims no priority for a radius statement that might be covered by their theory. The full text of that plausible earlier source was not accessible for comparison, so equivalent enumerator coverage remains a research risk. General coset-leader enumeration algorithms, including the 2000 IEEE conference contribution cited below, provide computational methods; an algorithm for arbitrary binary codes does not by itself state this closed, all-parameter spectrum. No historical noncoverage or independent priority certification is inferred from searches alone.

## Limitations

The result is binary and assumes a complete equal-arm \(2\)-sum with \(m\ge4\); irregular arms, arbitrary incidence codes, nonbinary Hamming decoding, and channels with asymmetric symbol errors are not covered. A published all-parameter coset-distance enumeration equivalent to this one may exist in older literature not fully inspected, especially in work on graph-cycle codes or concatenated parity/repetition codes. No claim is made that the covering-radius corollary alone is new or that these codes outperform competing designs. The channel formula concerns optimal block decoding, not the complexity or measured speed of a decoder.

## References

1. A. S. Barbosa, F. de L. Marquezino, and G. G. La Guardia, *New Methods for Constructing Classical and Quantum Codes from Graphs and Matroids*, arXiv:2610.04617v1 (public October 3, 2026), Section 3.2, https://arxiv.org/html/2610.04617v1.
2. P. Solé and T. Zaslavsky, *The covering radius of the cycle code of a graph*, Discrete Applied Mathematics 45 (1993), 63–70, https://doi.org/10.1016/0166-218X(93)90140-J.
3. *An algorithm for computing weight distribution of coset leaders of binary linear block codes*, IEEE International Symposium on Information Theory (2000), https://doi.org/10.1109/ISIT.2000.866523.
