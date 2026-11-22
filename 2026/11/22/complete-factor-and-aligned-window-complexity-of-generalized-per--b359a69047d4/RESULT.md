# Complete factor and aligned-window complexity of generalized period-doubling words

## Finding

For every integer \(q\ge 2\), define the infinite word \(u^{(q)}\) by \(u^{(q)}_j=\nu_2(j+1)\bmod q\), for every integer \(j\ge0\), where \(\nu_2\) denotes the binary valuation. Let \(P_q(n)\) count distinct length-\(n\) contiguous factors. Let \(W_q(n)\) count distinct length-\(n\) *aligned nonoverlapping windows* \(u^{(q)}_{jn}\cdots u^{(q)}_{(j+1)n-1}\), for \(j\ge0\).

For \(n=1\), set \(c(1)=0\). For \(n\ge2\), put \(k=\lfloor\log_2 n\rfloor\) and
\[
c(n)=\max\{2^{k-1},\ n-2^k\}.
\]
If \(\operatorname{odd}(n)=n/2^{\nu_2(n)}\), then the **complete factor and window complexity laws** are
\[
\boxed{P_q(n)=qn-c(n),\qquad W_q(n)=q\operatorname{odd}(n)-c(\operatorname{odd}(n))\quad (q\ge2,\ n\ge1).}
\]
In particular, \(W_q(n)=P_q(n)\) exactly when \(n\) is odd. At dyadic lengths \(2^r\), \(r\ge1\), the factor complexity is \((2q-1)2^{r-1}\), whereas the aligned-window complexity is exactly \(q\). Thus the windows exhibit a sharp oscillation as their size varies, with fixed bounded values on the dyadic subsequence but unbounded values on odd sizes.

## Assumptions and scope

The alphabet is the residue alphabet \(\{0,1,\ldots,q-1\}\), with \(q\) any integer at least two. The word is one-sided infinite; factors are *contiguous*, not scattered subsequences. Different starting positions giving the same length-\(n\) string are counted once. A window begins at a nonnegative integer multiple of its length, not at an arbitrary position. The symbol \(u^{(q)}_j\) is the integer residue of \(\nu_2(j+1)\) modulo \(q\). No regularity hypothesis beyond this definition is imposed. The result is exact for all integer lengths \(n\ge1\), not merely dyadic lengths.

The same word is the fixed point beginning with \(0\) of the length-two morphism \(\sigma_q(a)=0\,(a+1\bmod q)\). We denote by \(\tau_q\) the alphabet permutation \(a\mapsto a+1\bmod q\).

## Proof

**1. Morphic recursion.** The binary valuation gives \(u_{2j}=0\) and \(u_{2j+1}=\tau_q(u_j)\). Hence \(u=\sigma_q(u)\). Since \(\tau_q\) is bijective, the map \(\sigma_q\) is injective on finite words. In addition, every position congruent to one modulo four has symbol one: \(u_{4j+1}=1\). Any factor of length at least four therefore contains a symbol \(1\). But a symbol \(1\) never occurs at an even global index, because \(u_{2j}=0\) and \(q\ge2\). Thus an occurrence of a factor of length at least four determines the parity of its starting index from any local position occupied by a \(1\). In particular the families of factors starting at even and odd indices are disjoint for lengths at least four.

**2. Factor recurrences.** For \(m\ge2\), an even-start length-\(2m\) factor is \(\sigma_q(v)\) for a unique length-\(m\) factor \(v\). An odd-start length-\(2m\) factor is obtained by alternating \(\tau_q\)-images of the \(m\) symbols of a length-\(m\) factor with zeros, again injectively. Their disjointness from step 1 yields
\[
P_q(2m)=2P_q(m),\qquad m\ge2.
\]
Likewise, an even-start length-\((2m+1)\) factor is \(\sigma_q(v)0\), for a length-\(m\) factor \(v\), while an odd-start length-\((2m+1)\) factor is an injective alternating encoding of a length-\((m+1)\) factor, giving
\[
P_q(2m+1)=P_q(m)+P_q(m+1),\qquad m\ge2.
\]
The elementary initial counts are \(P_q(1)=q\) and \(P_q(2)=2q-1\). Indeed, the two types of digrams are \(0a\) and \(a0\) for all \(a\) in the alphabet, with only \(00\) counted twice. For length three the even-start factors are precisely \(0a0\), \(q\) of them; odd-start factors are \(a0b\), where \(ab\) runs over the \(P_q(2)\) factors after applying the inverse alphabet permutation. The two length-three types can intersect only in \(000\). The odd-start pattern \(000\) would force \(u_j=u_{j+1}=q-1\) in adjacent positions, impossible since one of the adjacent symbols is \(0\) and \(q-1\ne0\). Thus \(P_q(3)=3q-1\).

**3. Closed factor formula.** Let \(d_q(n)=qn-P_q(n)\). The preceding equations imply
\[
d_q(1)=0,\quad d_q(2)=d_q(3)=1,\quad d_q(2m)=2d_q(m),\quad d_q(2m+1)=d_q(m)+d_q(m+1)\quad(m\ge2).
\]
The explicitly defined \(c(n)\) satisfies the same initial values and recurrences. To check this without analytic assumptions, partition the integers by \(2^k\le n<2^{k+1}\) and consider the two intervals \(2^k\le n\le3\cdot2^{k-1}\) and \(3\cdot2^{k-1}\le n<2^{k+1}\). On the first, \(c(n)=2^{k-1}\); on the second, \(c(n)=n-2^k\). Doubling preserves the corresponding branches, while in the odd case adding the adjacent half-length branch values gives the same expression, including both transition endpoints. An induction on \(n\) therefore proves \(d_q(n)=c(n)\) for all positive integers, equivalently \(P_q(n)=qn-c(n)\).

**4. Odd-length windows see every factor.** Suppose \(n\) is odd, and let a length-\(n\) factor begin at position \(s\ge0\). Choose \(J\) strictly larger than all binary valuations \(\nu_2(s+i)\) for \(1\le i\le n\). Then every integer \(t\equiv s\pmod{2^J}\) has \(\nu_2(t+i)=\nu_2(s+i)\) for all \(1\le i\le n\), since adding a multiple of a higher power of two does not change a smaller finite valuation. Since \(n\) is coprime to \(2^J\), the Chinese remainder theorem gives arbitrarily large nonnegative \(t\) satisfying simultaneously \(t\equiv s\pmod{2^J}\) and \(t\equiv0\pmod n\). Therefore the factor also occurs at an aligned window. Every aligned window is of course a factor, so \(W_q(n)=P_q(n)\) for all odd \(n\).

**5. Doubling leaves window counts unchanged.** For every integer \(n\ge1\), the \(j\)-th aligned length-\(2n\) window begins at \(2nj\). The morphic recursion from step 1 identifies it with \(\sigma_q\) of the \(j\)-th aligned length-\(n\) window. Since \(\sigma_q\) is injective, the distinct-window counts satisfy \(W_q(2n)=W_q(n)\). Repeated division by two and step 4 yield \(W_q(n)=P_q(\operatorname{odd}(n))\) for every positive \(n\).

Finally, the closed formula gives \(P_q(n+1)-P_q(n)\in\{q,q-1\}\), for \(n\ge1\), and this is positive for \(q\ge2\). Therefore \(P_q(n)=P_q(\operatorname{odd}(n))\) exactly when \(n\) is odd. Substituting powers of two into \(c(n)\) proves the stated dyadic contrast. On odd \(n\to\infty\), \(W_q(n)=P_q(n)\to\infty\), whereas \(W_q(2^r)=q\), as required.

## Verification

Two standalone Python programs in `checks/` provide complementary finite verification, not substitutes for the unrestricted proof. `exact_residue_checker.py` constructs the full factor set of the infinite word by exhaustive residue classes, accounting for the unique high-valuation position in each short interval; it checked 576 exact parameter cases with \(2\le q\le7\) and \(1\le n\le96\), as well as 17,982 recurrence identities through length 3,000. Independently, `prefix_window_checker.py` generates 32,768 symbols by the substitution and compares literal substring sets and nonoverlapping window sets for 120 parameter pairs, \(2\le q\le6\), \(1\le n\le24\). Outputs appear in `checks/exact_residue_output.txt` and `checks/prefix_window_output.txt`. Run both scripts with a standard Python 3 interpreter; neither needs third-party packages.

## Relationship to prior work

Cassaigne and Kaboré, *On modulo-recurrence and window complexity in infinite words* (arXiv:2606.13744, first public June 11, 2026), relate window and factor complexity for the Thue–Morse word. Their result motivates asking for an exact law for a different uniform substitution. Bognini and Ammar (arXiv:2511.20881) define and investigate this generalized period-doubling substitution via kernel-word and gap factorizations. Binary period-doubling factor complexity is already covered in the classical literature, including OEIS A275202; it is not presented as novel here. A published classification indexed as *Exact dyadic factor and reflection complexity of cyclic period-doubling words* determines the factor count at powers of two for the nonbinary case; its dyadic statement is consistent with our formula and is not claimed as new. The newly derived portion is the uniform all-length expression for the nonbinary factor counts, together with the exact all-length aligned-window law for the generalized family.

## Limitations

No claim is made that the binary factor-complexity specialization or previously established dyadic nonbinary factor counts are new. A highly relevant indexed earlier dyadic analysis was available through its published abstract/summary but not as inspectable full text, so a stronger unindexed implication cannot be excluded solely by these comparisons; the historical-priority determination remains open to independent literature verification. The proof concerns these particular valuation words and *nonoverlapping aligned windows*; it does not classify arbitrary generated morphic words, arbitrary arithmetic progressions, or different window boundary conventions. Independent mathematical review has not yet been performed.

## References

1. J. Cassaigne and I. Kaboré, *On modulo-recurrence and window complexity in infinite words*, arXiv:2606.13744, https://arxiv.org/abs/2606.13744 (first public June 11, 2026).
2. K. E. Bognini and H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881, https://arxiv.org/abs/2511.20881 (first public November 25, 2025).
3. OEIS A275202, *Subword complexity of the period-doubling sequence*, https://oeis.org/A275202 (binary prior comparison).
4. *Exact dyadic factor and reflection complexity of cyclic period-doubling words*, indexed scientific record dated November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dyadic-factor-and-reflection-complexity-of-cyclic-period-d--c8d7b40c0705 (relevant previously established dyadic special case; available indexed summary only).
