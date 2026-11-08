# Strict lunar divisor-count inequality in every base

## Finding
For every integer base \(b\ge 2\) and positive integer \(n\), define \(d_b(n)\) as the number of distinct positive lunar divisors of \(n\) and \(\sigma_b(n)\) as their lunar sum (digitwise maximum). Then
\[
d_b(n)\le\sigma_b(n),\qquad d_b(n)=\sigma_b(n)\ \Longleftrightarrow\ n=1.
\]
In particular \(d_b(n)<\sigma_b(n)\) for every \(n>1\) and every \(b\ge 2\), settling the base-ten statement formulated as Conjecture 5 in [1].

## Assumptions and scope
All inequalities between numbers, other than the expressly defined lunar operations, use their ordinary integer values. For base \(b\), write \(\beta=b-1\), and represent a positive integer by its usual finite base-\(b\) expansion with nonzero leading digit. Lunar addition is digitwise maximum with missing leading digits treated as zero. Lunar multiplication \(\otimes_b\) is digitwise convolution: if \(u=\sum_i u_i b^i\) and \(v=\sum_jv_jb^j\), the digit at position \(k\) of \(u\otimes_b v\) is \(\max_{i+j=k}\min(u_i,v_j)\). A *positive lunar divisor* of \(n\) is a positive integer \(u\) with \(u\otimes_bv=n\) for some positive integer \(v\); its collection is \(D_b(n)\). Thus \(d_b(n)=|D_b(n)|\) and \(\sigma_b(n)=\bigoplus_{u\in D_b(n)}u\). The one-digit number \(\beta\) is the multiplicative unit. The product of positive integers having respectively \(r\) and \(s\) base-\(b\) digits has exactly \(r+s-1\) digits: its leading digit is the positive minimum of the two leading digits. Hence \(D_b(n)\) is finite.

## Proof
**A general upper bound.** Every digit of a divisor \(u\in D_b(n)\) is at most the corresponding digit of \(\sigma_b(n)\) because this sum is a digitwise maximum. In ordinary integer order, \(1\le u\le\sigma_b(n)\). The \(d_b(n)\) distinct positive divisors therefore belong to the \(\sigma_b(n)\)-element set \(\{1,2,\ldots,\sigma_b(n)\}\). This gives \(d_b(n)\le\sigma_b(n)\).

**One-digit case.** If \(n=1\), its lunar divisors are exactly the one-digit numbers \(1,2,\ldots,\beta\): each multiplies lunarly by \(1\) to give \(1\), and the product-length law excludes longer factors. Thus \(d_b(1)=\beta=\sigma_b(1)\). If \(2\le n\le\beta\), a lunar factorization must have two one-digit factors, and \(u\) is a divisor precisely when \(n\le u\le\beta\). Accordingly \(d_b(n)=\beta-n+1<\beta=\sigma_b(n)\).

**At least two digits.** Suppose \(n\ge b\). Write its units digit as \(r\in\{0,\ldots,b-1\}\). Both \(n\) and \(\beta\) belong to \(D_b(n)\), since \(\beta\otimes_b n=n\). Hence every digit of \(n\) is bounded by the corresponding digit of \(\sigma_b(n)\), while the units digit of \(\sigma_b(n)\) is exactly \(\beta\).

Construct an integer of the same base-\(b\) length as \(n\) by changing only its units digit:
\[
w=\begin{cases}
n-r,&r>0,\\
n+1,&r=0.
\end{cases}
\]
The leading digit is unchanged and nonzero, so \(w>0\). Its higher digits coincide with those of \(n\); its units digit is \(0\) if \(r>0\) and \(1\) if \(r=0\). Therefore \(w\) is digitwise at most \(\sigma_b(n)\), so \(1\le w\le\sigma_b(n)\) in ordinary order.

We claim \(w\notin D_b(n)\). Indeed, if \(w\otimes_b v=n\) for some positive \(v\), the product-length law, and the equal lengths of \(w\) and \(n\), force \(v\) to have one digit. Then the units digit of \(w\otimes_b v\) is \(\min(w_0,v_0)=w_0\), because \(w_0\in\{0,1\}\) and \(v_0\ge1\). But \(w_0\ne r\), contradicting the units digit of \(n\). Thus \(w\) is absent from the integer interval \(\{1,\ldots,\sigma_b(n)\}\), despite every divisor lying within this interval. We conclude \(d_b(n)\le\sigma_b(n)-1\).

The one-digit and longer cases establish the theorem for every base and every positive integer. \(\square\)

## Verification
An independent exhaustive finite checker implements the minimum/maximum digit convolution and enumerates every factor pair whose product has at most three digits (or two digits in the larger tested bases). It compares the exact divisor set, its lunar sum, the strict inequality, and the explicit missing-integer witness for all 1019 tested inputs in bases 2 through 10, using 47489 factor-pair products and 974 tested witnesses. The command `python3 verify_lunar.py` reports:

`VERIFY_OK bases=2..10 inputs=1019 products=47489 missing_witnesses=974 all_strict_for_n_gt_one=PASS equality_only_n_one=PASS unit_divisor_sum=PASS`

These tests corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work
Applegate, LeBrun and Sloane [1, Section 7, Conjecture 5] explicitly conjectured the strict inequality for decimal lunar arithmetic. Their Theorem 20 determines when the lunar sum equals its argument and gives bounds on that sum, but does not compare the divisor count with the divisor sum. The present digit-flip witness supplies that comparison for every base and all positive inputs. Gross [2] proves maximal-divisor-count conjectures (Conjectures 2--4 of [1]) by studying additive decompositions; those results concern different extremal statements and do not imply the inequality here. OEIS [3,4] documents relevant sequences, not an unrestricted proof of this comparison.

## Limitations
The result concerns positive integers with standard leading-zero-free base representations and the ordinary integer comparison of \(d_b(n)\) and \(\sigma_b(n)\). It does not determine the exact size of their difference, nor maximal lunar divisor counts of fixed length. Search-based historical-priority assessment is not exhaustive; an unlocated later proof of the 2011 conjecture may exist.

## References
[1] D. Applegate, M. LeBrun and N. J. A. Sloane, *Dismal Arithmetic*, arXiv:1107.1130, first submitted 2011-07-06; especially Section 7, Theorem 20 and Conjecture 5. https://arxiv.org/abs/1107.1130

[2] G. Gross, *Maximally Additively Reducible Subsets of the Integers*, arXiv:1908.05220 (2019); *Journal of Integer Sequences* 23 (2020), Article 20.10.5. https://arxiv.org/abs/1908.05220

[3] OEIS A186442, binary lunar divisor-count versus divisor-sum excess. https://oeis.org/A186442

[4] OEIS A188548, binary lunar sum of divisors. https://oeis.org/A188548
