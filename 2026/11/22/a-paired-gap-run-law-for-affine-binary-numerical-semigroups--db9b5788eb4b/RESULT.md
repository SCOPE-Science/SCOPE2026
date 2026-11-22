# A paired gap-run law for affine binary numerical semigroups

## Finding

For every integer \(a\ge3\), let
\[
S_a=\left\langle a,(a+1)2^i-1:i\ge1\right\rangle.
\]
Let \(b_i=2^i-1\), and let \(c(r)\) be the minimum number of coins from \(\{b_i:i\ge1\}\) summing to \(r\), with \(c(0)=0\). A *gap run* is a maximal interval of consecutive positive integers not belonging to \(S_a\). Then, for every integer \(1\le\ell<a\), the number \(R_a(\ell)\) of gap runs of length \(\ell\) is exactly
\[
\boxed{R_a(\ell)=1+c(a-\ell)-c(a-\ell-1)\in\{0,2\}.}
\]
All longer lengths have frequency zero. Hence **every occurring gap length occurs exactly twice**, and the total number of maximal gap runs is \(a-1+c(a-1)\).

In the natural generalized-Thabit subfamily
\[
a=(2^s+1)2^n-1,\qquad s,n\ge1,
\]
there are exactly \(a+1\) runs, attaining exactly \((a+1)/2\) different lengths, twice each. Its number of isolated gaps (runs of length one) is exactly two when \(n=1\), and zero when \(n\ge2\). In particular, every member with \(n\ge2\) is *perfect* (has no isolated gaps).

The coin counts, and therefore the entire spectrum, are computable by the finite recurrence
\[
c(0)=0,\qquad c(r)=1+\min_{1\le i\le\lfloor\log_2(r+1)\rfloor}c(r-(2^i-1))\quad(r\ge1).
\]

## Assumptions and scope

All generators and coefficients are nonnegative integers; the infinite generating family is well-defined because only finitely many generators can contribute below a given bound. The integer \(a\) is the multiplicity, since the next generator is \(2a+1\), and \(\gcd(a,2a+1)=1\). Thus \(S_a\) is a numerical semigroup. The notion of a gap run includes runs at the beginning and end of the finite gap set, with a neighboring semigroup element on each side. The claim concerns maximal consecutive gap lengths, not Frobenius number or genus, which have been studied previously.

## Proof

**The Apéry thresholds.** A nontrivial representation by generators other than \(a\) uses \(C\) coins \(b_{i_j}\), whose sum is \(B\), and has numerical value
\[
\sum_{j=1}^C[(a+1)2^{i_j}-1]=a(B+C)+B.
\]
For a fixed residue \(0\le r<a\), this has \(B=r+ha\) with \(h\ge0\). When \(h=0\), the least possible value is \(r+a(r+c(r))\). For \(h\ge1\), its value is at least \(r+a(h(a+1)+r+1)\), which exceeds the candidate at \(h=0\), since \(c(r)\le r<a+1\). (At \(r=0\), the minimum is the empty representation, zero.) Thus every Apéry minimum is
\[
w_r=r+a\bigl(r+c(r)\bigr),\quad 0\le r<a.
\]
Consequently, writing \(k_r=r+c(r)\), an integer \(qa+r\) with \(q\ge0\) lies in \(S_a\) if and only if \(q\ge k_r\).

**Unit jumps.** For each \(r\ge1\), adding one coin of value \(1\) to an optimal representation of \(r-1\) proves \(c(r)\le c(r-1)+1\). Conversely, take an optimal representation of \(r\). If it contains a unit coin, deleting it gives a representation of \(r-1\) with one fewer coin. Otherwise, replace any coin \(b_i\), \(i\ge2\), by two coins \(b_{i-1}\). The identity \(b_i-1=2b_{i-1}\) produces a representation of \(r-1\) with one additional coin. Hence \(|c(r)-c(r-1)|\le1\). Since every coin \(b_i\) is odd, \(c(r)\equiv r\pmod2\), so equality holds:
\[
c(r)-c(r-1)\in\{-1,+1\},\qquad k_r-k_{r-1}\in\{0,2\}.
\]

**Counting maximal runs.** In the block \([qa,(q+1)a-1]\), position \(qa\) belongs to \(S_a\). Since \(k_0\le k_1\le\cdots\le k_{a-1}\), the gaps in that block, if any, form the terminal interval with residues \(r,r+1,\ldots,a-1\), where \(r\) is the first residue for which \(q<k_r\). These intervals do not join between blocks, because each block begins with \(qa\in S_a\). For a fixed \(1\le r<a\), the run beginning in residue \(r\) occurs for exactly those nonnegative rows \(q\) with \(k_{r-1}\le q<k_r\). There are \(k_r-k_{r-1}\) such rows, and each run has length \(a-r\). This gives the formula and shows that every frequency is zero or two. Summing over \(r=1,\ldots,a-1\) telescopes to \(k_{a-1}-k_0=a-1+c(a-1)\).

**The sharp isolated-gap boundary.** In the specified subfamily set \(a=(2^s+1)2^n-1\). Then
\[
a-1=(2^{n+s}-1)+(2^n-1)=b_{n+s}+b_n.
\]
It cannot equal a single Mersenne coin because \(2^{n+s}+2^n-1\) is not a power of two; hence \(c(a-1)=2\). Thus the number of runs is \(a+1\), necessarily even, and each of \((a+1)/2\) lengths appears twice.

For \(n=1\), \(a-2=b_{s+1}\), giving \(c(a-2)=1\) and \(R_a(1)=2\). For \(n\ge2\), the identity \(a-2=b_{n+s}+2b_{n-1}\) gives \(c(a-2)\le3\). Here \(a-2\) is odd, so it cannot be a sum of two odd Mersenne coins; it is not itself a Mersenne coin (since \(a-1+1=2^{n+s}+2^n-1\) is not a power of two and \(a-2+1=2^{n+s}+2^n-2\) lies strictly between successive powers of two for \(s\ge1,n\ge2\)). Hence \(c(a-2)=3\), and \(R_a(1)=0\). This proves the asserted dichotomy.

## Verification

The included `CHECK.py` uses Dijkstra shortest paths independently of the coin calculation to obtain the entire Apéry set, constructs all membership values through the Frobenius number, and counts maximal gap runs directly. It checks every \(3\le a\le319\), then all 25 pairs \(1\le s,n\le5\). All assertions passed. These finite checks corroborate, but do not replace, the proof for unbounded parameters. Run `python3 CHECK.py` with Python 3 and no additional packages.

## Relationship to prior work

Gu, Li, and Huang (2022) studied special infinite subfamilies of \(\langle (a+1)2^i-1\rangle\), including monotone Apéry sequences and the Frobenius/genus problems. Liu, Xin, Ye, and Yin (2023) treated the more general affine-repunit generators \(\langle a,ba+d, b^2a+(b+1)d,\ldots\rangle\), which include this semigroup when \(b=2,d=1\); they established Apéry methods and Frobenius/genus formulas. The present theorem makes no claim to discover the Apéry method or those global invariants. Its proposed contribution is the exact multiplicity of **each maximal interval of consecutive gaps**, the universal zero-or-two phenomenon, and the sharp perfectness boundary of the specified two-parameter subfamily. These do not follow merely from a formula for Frobenius number or genus without further information about consecutive membership transitions. Published indexed work concerning isolated gaps of Proth semigroups uses the opposite \(+1\) sign and does not directly cover the present \(-1\) generator family.

## Limitations

The theorem applies to the specific binary affine generators, not to arbitrary affine-repunit bases or arbitrary numerical semigroups with monotone Apéry sets. The count formula is algorithmic through a finite coin-change recursion; it does not assert a simpler universal closed expression for every individual length. Prior full texts use related coin-change and Apéry normal forms; an unstated or unindexed exact gap-run classification could overlap this consequence. Independent mathematical review and publication-priority verification are not performed.

## References

- Z. Gu, D. Li, Y. Huang, *On the Numerical Semigroup Generated by \(\{(2^k-m)2^{n+i}-1:i\in\mathbb N\}\)*, Journal of Mathematics (2022), article 6590211, first published 2022-04-30, https://doi.org/10.1155/2022/6590211.
- F. Liu, G. Xin, S. Ye, J. Yin, *A Note on Generalized Repunit Numerical Semigroups*, arXiv:2306.10738v1, first posted 2023-06-19, https://arxiv.org/html/2306.10738v1.
- F. Liu, G. Xin, *A Generalization of Mersenne and Thabit Numerical Semigroups*, arXiv:2306.03459 (2023), https://arxiv.org/abs/2306.03459.
- J. C. Rosales and P. A. García-Sánchez, *Numerical Semigroups*, Springer (2009), general definitions of Apéry sets and gaps.
