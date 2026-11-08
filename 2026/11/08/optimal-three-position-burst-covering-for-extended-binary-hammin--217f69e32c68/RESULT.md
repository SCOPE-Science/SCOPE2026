# Optimal three-position burst covering for extended binary Hamming codes

## Finding

For each integer \(m\ge2\), put \(Q=2^m\) and let \(C_m\) be the binary extended Hamming code of length \(Q\), dimension \(Q-m-1\), and parity-check columns \((1,v)\), one for each \(v\in\mathbb F_2^m\). A *coordinate ordering* is a permutation of these \(Q\) columns. A syndrome is \(b\)-burst obtainable when it is a sum of columns supported in some interval of at most \(b\) consecutive coordinates; the cyclic version allows an interval to wrap around the endpoints. The zero syndrome is obtainable by the empty sum.

**Theorem.** In both noncyclic and cyclic conventions, the largest possible number of syndromes obtainable from intervals of at most two coordinates, optimized over all coordinate orderings, is exactly \(2Q-1\), one fewer than the \(2Q\) syndromes. Moreover, the smallest possible burst-covering radius, optimized over coordinate orderings, is exactly \(3\). A single explicit ordering simultaneously attains both sharp assertions in both conventions.

An optimal ordering comes from any primitive element \(\alpha\) of \(\mathbb F_{Q}\):
\[
 v_0=0,\qquad v_i=\alpha^{i-1}\quad(1\le i\le Q-1).
\]
For this ordering, the unique syndrome not obtainable in a two-coordinate burst is \((0,1+\alpha^{-1})\); it is obtainable within three consecutive coordinates.

## Assumptions and scope

All linear combinations and codes use the binary base field. The field \(\mathbb F_Q\) is identified with the \(m\)-dimensional vector space \(\mathbb F_2^m\) via any chosen binary basis. The code is the kernel of the \((m+1)\times Q\) binary matrix whose columns are \((1,v_i)\); because \(v_i\) ranges bijectively over \(\mathbb F_2^m\), this is an extended binary Hamming code regardless of their order. In a noncyclic \(b\)-burst the support is contained in \(\{i,\ldots,i+b-1\}\) with valid indices; the cyclic convention interprets indices modulo \(Q\). No restriction demands that every position inside the interval be nonzero. The theorem concerns the minimum over coordinate permutations, not every ordering.

## Proof

Let \(v_0,\ldots,v_{Q-1}\) be any permutation of \(\mathbb F_Q\) and \(h_i=(1,v_i)\). For a two-coordinate interval, a sum of zero, one, or two columns has respectively the forms \((0,0)\), \((1,v_i)\), and \((0,v_i+v_{i+1})\). There are precisely \(Q\) distinct odd-parity syndromes \((1,v_i)\). All even-parity nonzero syndromes arise from adjacent differences \(v_i+v_{i+1}\), which are nonzero because the \(v_i\) are distinct.

For noncyclic intervals, there are \(Q-1\) adjacent differences. If they were all distinct, they would constitute \(\mathbb F_Q^\times\). Their sum would be \(0\), since the sum of all elements of \(\mathbb F_Q\) is zero for \(m\ge2\). But telescoping gives
\[
 \sum_{i=0}^{Q-2}(v_i+v_{i+1})=v_0+v_{Q-1}\ne0.
\]
Thus at most \(Q-2\) distinct nonzero even-parity syndromes occur. Including zero and the \(Q\) odd-parity syndromes, the total is at most \(1+(Q-2)+Q=2Q-1\).

For cyclic intervals there are \(Q\) adjacent differences, including \(v_{Q-1}+v_0\). Suppose their set contained all \(Q-1\) nonzero field elements. Exactly one nonzero value would then occur twice, and all others once. Their sum would equal that repeated value (the sum of all nonzero elements vanishes). But the cyclic telescoping sum is zero, a contradiction. Thus at most \(Q-2\) different nonzero even-parity syndromes occur and again at most \(2Q-1\) syndromes occur in total. This proves that every ordering has burst-covering radius greater than two in either convention.

Now choose a primitive \(\alpha\in\mathbb F_Q\) and take \(v_0=0\), \(v_i=\alpha^{i-1}\) for \(1\le i\le Q-1\). Noncyclic neighboring differences are
\[
 1,\qquad (1+\alpha)\alpha^j\quad(0\le j\le Q-3).
\]
Because \(\alpha\) has multiplicative order \(Q-1\), the latter set consists of all nonzero field elements except
\[
 u=(1+\alpha)\alpha^{Q-2}=1+\alpha^{-1}.
\]
Since \(u\ne1\), adding the initial difference \(1\) changes no element of this set: the distinct neighboring differences are exactly \(\mathbb F_Q^\times\setminus\{u\}\). The additional cyclic neighboring difference \(v_{Q-1}+v_0=\alpha^{-1}\) also belongs to this same set, since \(\alpha^{-1}\ne u\). Hence the ordering attains the sharp value \(2Q-1\) for both noncyclic and cyclic two-coordinate bursts. Its unique missing syndrome is \((0,u)\).

To obtain that remaining syndrome within a three-coordinate interval, consider the differences between positions two apart among the nonzero powers:
\[
 v_{j+1}+v_{j+3}=\alpha^j(1+\alpha^2)
 =\alpha^j(1+\alpha)^2,\qquad0\le j\le Q-4.
\]
The equation \(\alpha^j(1+\alpha)^2=u\) is equivalent to
\[
 \alpha^j=[\alpha(1+\alpha)]^{-1}.
\]
The unique exponent \(j\) modulo \(Q-1\) cannot be \(Q-3\) or \(Q-2\). Indeed, those choices would respectively force \(\alpha(1+\alpha)=\alpha^2\) or \(\alpha(1+\alpha)=\alpha\), both impossible for nonzero \(\alpha\) in characteristic two. Therefore \(0\le j\le Q-4\), and the pair of columns \(h_{j+1}+h_{j+3}=(0,u)\) lies within three consecutive positions. Every other syndrome was already obtainable from two positions. Consequently three-position bursts cover all syndromes, and the previously proved obstruction at two positions establishes the optimum exactly.

## Verification

The standalone Python program `checker.py` constructs a primitive binary polynomial for every degree from \(2\) through \(11\), verifies that powers of its residue class enumerate every nonzero field element, and directly enumerates attainable syndrome sums from consecutive length-two and length-three windows in both conventions. It checks exactly \(2Q-1\) and \(2Q\) attainable syndromes, respectively, and checks the predicted missing even syndrome. It also exhaustively evaluates every \(8! =40320\) coordinate ordering of the length-eight code to independently confirm that no order attains all sixteen syndromes from two-coordinate windows. Run `python3 checker.py` from the directory containing this file. This finite validation supplements, and does not replace, the general proof above.

## Relationship to prior work

Sac Himelfarb and Schwartz, *On the Burst-Covering Radius of Binary Cyclic Codes*, arXiv:2601.00435 (first submitted January 1, 2026), define the burst-covering radius by consecutive parity-check columns (Definition 14), emphasize coordinate-order dependence (Remark 15), and exhibit a length-eight extended Hamming ordering with burst-covering radius three (Example 16). Their Theorems 17 and 18 give general parameter lower bounds, and their conclusion explicitly asks for exact burst-covering radii of additional code families. The present theorem supplies an explicit optimal ordering for **every** extended binary Hamming length \(Q=2^m\), proves a universal two-burst impossibility, and proves the sharp maximal two-burst syndrome coverage. The length-eight instance overlaps their example and is not claimed as new by itself. The paper's primitive cyclic-code LFSR formulas do not provide this noncyclic extended-code ordering theorem. Finite-group terrace/near-sequencing literature is conceptually adjacent, but its known abstract formulations do not by themselves certify historical priority for the coding claim.

## Limitations

The code family is extended binary Hamming and the channel has one short burst of flips, with the location unrestricted. A different ordering may have larger burst-covering radius. Nothing is asserted for arbitrary binary linear codes, for deletion channels, for multiple bursts, or for nonbinary analogues. The explicit construction is independent of the chosen field basis but depends on the chosen primitive element. Full historical priority remains subject to the possibility of unindexed equivalent ordering results. Independent external mathematical validation has not been performed.

## References

1. G. Sac Himelfarb and M. Schwartz, *On the Burst-Covering Radius of Binary Cyclic Codes*, arXiv:2601.00435, first submission January 1, 2026, https://arxiv.org/html/2601.00435v3 (Definition 14, Remark 15, Example 16, Theorems 17 and 18, Section VIII).
2. M. A. Ollis, *Terraces for Small Groups*, arXiv:1603.01496, March 4, 2016, https://arxiv.org/abs/1603.01496 (context on group-ordering/terrace terminology; no theorem from this paper is used).
