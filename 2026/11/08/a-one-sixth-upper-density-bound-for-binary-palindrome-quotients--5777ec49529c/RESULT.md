# A one-sixth upper-density bound for binary palindrome quotients

## Finding

Let \(\mathcal P_2\) be the set of positive integers whose ordinary binary expansions are palindromes. Let
\[\mathcal Q=\{N\in\mathbb Z_{>0}: N=A/B\text{ for some }A,B\in\mathcal P_2\}.\]
The upper natural density of \(\mathcal Q\) obeys the explicit unconditional bound
\[\boxed{\overline d(\mathcal Q)\le\frac{39829963}{240599040}<\frac16}.\]
Equivalently, \(\underline d(\mathbb Z_{>0}\setminus\mathcal Q)\ge200769077/240599040>5/6\). Here density means counting integers up to a real bound \(X\) and dividing by \(X\), using \(\limsup\) or \(\liminf\) respectively.

## Assumptions and scope

All integers are positive unless explicitly stated. Binary representations have no leading zeros, except that a fixed-width bit reversal does retain leading zeros. The claim concerns ratios \(A/B\) that are **integers**; it does not concern all rational numbers in the ratio set. No assumption is made about existence or number of representations. The inequality is an upper-density bound, not a claim of density zero and not an exact density formula.

## Proof

**Step 1: a necessary local condition.** Fix an integer \(k\ge3\), write \(H=2^{k-1}\), \(Q=2^k\), and let \(\rho_k\) reverse exactly \(k\) binary digits. For any odd \(N\) with at least \(k\) bits, define \(t\in[H,Q)\) to be its first \(k\) bits interpreted as an integer, and let \(r=N\bmod Q\), which is odd. Suppose \(N=A/B\) with palindromic positive integers \(A,B\), and suppose \(B\) has at least \(k\) bits. Let \(b\in[H,Q)\) be the initial \(k\)-bit integer of \(B\), and \(a\in[H,Q)\) the initial \(k\)-bit integer of \(A\). Because \(B\) and \(A\) are palindromes,
\[B\equiv\rho_k(b)\pmod Q,\quad A\equiv\rho_k(a)\pmod Q.\]
Using \(A=NB\) gives
\[a=\rho_k\big((r\rho_k(b))\bmod Q\big).\tag{1}\]
This determines \(a\) from \(r,b\). In particular the high bit of \(a\) is one because \(r\) and \(\rho_k(b)\) are odd.

If \(N\) and \(B\) have lengths \(m\) and \(\ell\), normalize them as \(N=2^{m-k}x\), \(B=2^{\ell-k}y\), where \(t\le x<t+1\) and \(b\le y<b+1\). Then \(tb\le xy<(t+1)(b+1)\). The product has either \(m+\ell-1\) or \(m+\ell\) bits. Accordingly its first \(k\) digits, \(a\), require that
\[\boxed{[tb,(t+1)(b+1))\cap\big([Ha,H(a+1))\cup[2Ha,2H(a+1))\big)\ne\varnothing.}\tag{2}\]
This is a **necessary** condition; replacing the product's attainable values by the entire interval only enlarges the allowed set, so causes no false exclusions.

Define \(\mathcal F_k\) as the pairs \((t,r)\) with \(H\le t<Q\), odd \(1\le r<Q\), for which **no** \(b\in[H,Q)\) satisfies (1) and (2). Every odd integer with at least \(k\) bits whose initial and final \(k\)-bit blocks give a pair in \(\mathcal F_k\) has no palindrome-quotient representation with a denominator of at least \(k\) bits.

**Step 2: an exhaustive integer certificate.** The attached standalone program `verify.cpp` implements (1)-(2), using only integer products, modulo powers of two, and exhaustive loops with explicit ranges. For each \(t\) it enumerates every possible \(b\); rather than iterate over all \(r\), it iterates the few possible \(a\)-intervals and inverts odd \(\rho_k(b)\bmod Q\) to mark the possible residues \(r\). The inversion is valid because \(\rho_k(b)\) is odd. The enumeration includes every possible pair and omits none.

At \(k=14\) the certificate gives \(H=8192\), \(Q=16384\), and
\[T:=|\mathcal F_{14}|=45362298.\]
For \(0\le q\le H\), put
\[P_q=\#\{(t,r)\in\mathcal F_{14}:H\le t<H+q\}.\]
The same exact enumeration proves that the minimum over every \(q\in\{0,\ldots,H\}\) is
\[\min_q\frac{T+P_q}{Q(H+q)}
=\frac{80469557}{240599040},\]
achieved at \(q=6493\), where \(P_q=35107259\). The entire finite minimization is recomputed by `verify.cpp`; `expected_output.txt` gives its actual output for widths \(3\) through \(14\). `crosscheck.py` independently enumerates all possibilities for widths \(3\) through \(8\) by the direct forced-prefix test and checks 200 reproducible samples at width \(14\). These spot checks do not replace the exhaustive width-14 certificate.

**Step 3: turn local obstructions into density.** For each binary length \(m\ge2k\), every prescribed pair \((t,r)\) of the leading \(k\) bits and last \(k\) bits occurs in exactly \(2^{m-2k}\) integers of length \(m\). Thus the integers in these forbidden cylinders number \(T2^{m-2k}\) in each complete length-\(m\) shell. At a boundary after the first \(q\) of its \(H\) leading-block intervals, the count from all smaller lengths plus the current partial shell is
\[(T+P_q)2^{m-2k}+O_k(1),\]
while the endpoint is \((H+q)2^{m-k}\). Within any one leading-block interval the count is affine up to \(O_k(1)\), because residue classes modulo \(Q\) occur with a uniformly bounded discrepancy. The quotient of an affine count by the endpoint coordinate has its minimum at one of the interval endpoints. Hence the lower natural density of the forbidden-cylinder set is exactly
\[\min_{0\le q\le H}\frac{T+P_q}{Q(H+q)}.
\]
In particular, the bound above is \(80469557/240599040\) for \(k=14\).

There is one remaining issue: a quotient may have a denominator \(B\) of fewer than \(k\) bits. There are only finitely many such \(B\). For each fixed \(B\), if \(N\le X\) and \(NB\) is a binary palindrome, then \(NB\le BX\), and there are only \(O_B(\sqrt X)\) binary palindromes up to \(BX\). The union over all \(B<2^{k-1}\) therefore contributes \(O_k(\sqrt X)=o(X)\) possible quotients. Subtracting these has no effect on lower density. Every even positive integer is also excluded from \(\mathcal Q\), because binary palindromes are odd. Adding their density \(1/2\) yields
\[\underline d(\mathbb Z_{>0}\setminus\mathcal Q)
\ge\frac12+\frac{80469557}{240599040}
=\frac{200769077}{240599040}>\frac56.\]
Taking complements gives the stated upper-density inequality. This finishes the proof.

## Verification

Run `c++ -O3 -std=c++17 verify.cpp -o verify`, then `./verify`, and compare the printed lines to `expected_output.txt`; run `python3 crosscheck.py` to reproduce `crosscheck_output.txt`. The C++17 certificate counts \(45362298\) forbidden 14-bit cylinders and checks all \(8193\) prefix boundaries. All intermediate unsigned products in the program are below \(2^{32}\), and all cross-multiplied density comparisons are below \(2^{64}\). This supplies an exact finite certificate, not a statistical estimate.

## Relationship to prior work

Bai, Meleshko, Riasat, and Shallit (2022), Theorem 8 and Corollary 9, give an explicit three-bit obstruction and a lower-density \(1/40\) certificate for a subset of odd nonrepresentable integers, and Remark 10 invites strengthening. Their Conjecture 2 asks whether the representable integers have density zero. The present result gives a new quantitative upper bound below \(1/6\) using a complete 14-bit local obstruction; it does not resolve the conjecture. The earlier three-bit obstructions, even when combined, are quantitatively weaker and do not imply the new constant. Independently, general algorithms for deciding individual quotient membership do not give the present uniform density bound without an additional counting argument.

## Limitations

The 14-bit local predicate is only necessary, not sufficient, for representability. Thus the rational bound is a certified inequality, not an exact density or a characterization of all quotients. The finite search over width 14 neither proves nor disproves the density-zero conjecture. Independent external audit and exhaustive literature coverage have not been performed.

## References

1. J. H. Bai, J. Meleshko, S. Riasat, and J. Shallit, *Quotients of Palindromic and Antipalindromic Numbers*, arXiv:2202.13694v1 (first public release 2022-02-28); *INTEGERS* 22 (2022), A96. https://arxiv.org/html/2202.13694v1
2. MaRDI portal, *Quotients of palindromic and antipalindromic numbers*, bibliographic record Q5042439 and MSC classification (11A63). https://portal.mardi4nfdi.de/wiki/Quotients_of_palindromic_and_antipalindromic_numbers
