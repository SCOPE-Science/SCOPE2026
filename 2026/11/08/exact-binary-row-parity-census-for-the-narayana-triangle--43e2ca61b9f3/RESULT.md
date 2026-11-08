# Exact binary row-parity census for the Narayana triangle

## Finding

For integers \(n\ge1\) and \(1\le k\le n\), set
\[
N(n,k)=\frac1n\binom nk\binom n{k-1},\qquad A(n)=\#\{k:1\le k\le n,\ N(n,k)\text{ is odd}\}.
\]
Write \(s_2(n)\) for the number of ones in the binary expansion of \(n\). Then, for every \(n\ge1\),
\[
\boxed{ A(n)=\begin{cases}
2^{s_2(n)},&n\text{ even},\\
2^{s_2(n)-t}(2^t-1),&n\text{ odd},\quad t=\nu_2(n+1).
\end{cases}}
\]
This is a complete explicit formula for every term of the odd-entry-per-row counting sequence (OEIS A335965). More strongly, for every \(L\ge1\), the **complete multiset** of counts \(\{A(n):1\le n<2^L\}\) consists of the following contributions (coincident numerical values from different contributions are added): for each \(1\le s\le L-1\), exactly \(\binom{L-1}s\) occurrences of \(2^s\) from even indices; for every \(1\le t<L\) and \(0\le h\le L-t-1\), exactly \(\binom{L-t-1}h\) occurrences of \((2^t-1)2^h\) from odd indices; and one occurrence of \(2^L-1\) from \(n=2^L-1\). In particular,
\[
\boxed{\sum_{n=1}^{2^L-1} A(n)=\frac{5\cdot3^{L-1}-3}{2}}.
\]

## Assumptions and scope

Narayana numbers have the stated integral binomial definition and index range. The binary digit sum and \(2\)-adic valuation have their usual integer meanings. The multiset statement does not assert that the listed numerical values are all distinct. The summation starts at \(n=1\), not at an artificial row zero.

## Proof

Lucas's theorem implies that a binomial coefficient \(\binom ab\) is odd if and only if every one-bit of \(b\) is also a one-bit of \(a\).

**Even rows.** Suppose \(n\) is even. For odd \(k\), rewrite the Narayana number as
\[
N(n,k)=\frac1k\binom{n-1}{k-1}\binom n{k-1}.
\]
Because \(k\) is odd, this is odd if and only if both displayed binomial coefficients are odd. Put \(j=k-1\), which is even. By Lucas's theorem this happens precisely when the one-bits of \(j\) are contained in the intersection of the one-bit sets of \(n\) and \(n-1\). This intersection is obtained from the binary expansion of \(n\) by deleting its lowest one-bit, and has \(s_2(n)-1\) elements. All its subset indices \(j\) are even, so there are exactly \(2^{s_2(n)-1}\) admissible odd \(k\). The symmetry \(N(n,k)=N(n,n+1-k)\) interchanges odd and even \(k\) when \(n\) is even, doubling the count to \(2^{s_2(n)}\).

**Odd rows.** If \(n\) is odd, the denominator \(n\) is a \(2\)-adic unit. Thus \(N(n,k)\) is odd exactly when \(\binom nk\) and \(\binom n{k-1}\) are both odd. Let \(t=\nu_2(n+1)\ge1\) be the length of the terminal run of one-bits in \(n\). The integers \(j\) whose one-bits are subsets of the one-bits of \(n\) form exactly \(2^{s_2(n)-t}\) disjoint blocks of \(2^t\) consecutive integers: one block for each choice of the higher one-bits of \(n\). Distinct blocks are separated by at least one missing integer because bit position \(t\) of \(n\) is zero (unless \(n\) consists entirely of ones, where there is a single block). Each block contains precisely \(2^t-1\) adjacent pairs \((k-1,k)\), giving the odd-row formula.

**Entire dyadic-block spectrum.** For \(0<n<2^L\), an even index has a zero final bit and \(L-1\) freely chosen higher bits. Excluding zero, exactly \(\binom{L-1}s\) even indices have \(s\) one-bits. For an odd index with exactly \(t<L\) trailing ones, the next bit is zero and the remaining \(L-t-1\) bits are free; exactly \(\binom{L-t-1}h\) have \(h\) further one-bits. The all-ones index contributes the final singleton. Summing the even-row counts gives \(3^{L-1}-1\). Summing the odd-row contributions gives
\[
\sum_{t=1}^{L-1}3^{L-t-1}(2^t-1)+(2^L-1)
=\frac{3^L-1}{2}.
\]
Addition yields the displayed total. No asymptotic extrapolation or finite enumeration is used.

## Verification

Run `python3 verify.py` with the standard library. The checker evaluates the integer Narayana numbers directly for every \(1\le n\le128\), verifies each closed row formula, and reconstructs the entire predicted multiset and total for every \(1\le L\le7\). The unrestricted proof uses Lucas's theorem and explicit bit-block counting, not the finite tests.

## Relationship to prior work

The Narayana triangle is classical, and Lucas's theorem is classical. OEIS A335965 records the odd-entry count with a table of initial values and the special equality classification \(A(n)=n\), but its inspected entry gives no all-index formula, complete dyadic-block multiset, or exact dyadic total. Eu–Liu–Yeh study Lucas-congruence phenomena in related combinatorial numbers; their public abstract and bibliographic record do not state this full census, but the inaccessible article body leaves residual priority uncertainty. The contribution claimed here is the combined exact row formula and the complete distribution of its values over every dyadic block, not Lucas's theorem or the initial table.

## Limitations

This concerns parity, not valuation layers modulo \(4\) or higher powers of two, and the row statistic is not the count of arbitrary Catalan objects. The uninspected full body of the Eu–Liu–Yeh article and other unindexed literature are residual originality risks. No independent specialist assessment has been performed.

## References

1. S.-P. Eu, S.-C. Liu, and Y.-N. Yeh, *On the Congruences of Some Combinatorial Numbers*, Studies in Applied Mathematics 116 (2006), 135–144; first published 2005-12-20, doi:10.1111/j.1467-9590.2006.00337.x.
2. OEIS A335965, *Number of odd numbers in the n-th row of the Narayana triangle*, first recorded 2020-07-01, https://oeis.org/A335965.
3. OEIS A001263, the classical Narayana triangle, https://oeis.org/A001263.
