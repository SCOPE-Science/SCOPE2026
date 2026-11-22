# A sharp three-prime obstruction for adjacent coprime pairs

## Finding

Let \(N\) be a positive odd integer with exactly three distinct prime factors, and define
\[
L(N)=\max_{a\in\mathbb Z}\max\{\ell\ge0:\gcd((a+i)(a+i+1),N)>1\text{ for }0\le i<\ell\}.
\]
Then \(L(N)\le14\), and equality holds if and only if \(\operatorname{rad}(N)=105\).
For any such \(N\) with radical \(105\), the complete set of starts attaining fourteen is
\[
a\equiv2\quad\text{or}\quad a\equiv89\pmod{105}.
\]
In particular exactly \(2N/105\) residue classes modulo \(N\) attain the bound, and for all other odd moduli with three distinct prime factors the maximum is at most thirteen.

## Assumptions and scope

Here \(\operatorname{rad}(N)\) is the product of distinct primes dividing \(N\). A start \(a\) is *good* if both \(a\) and \(a+1\) are individually coprime to \(N\), equivalently \(\gcd(a(a+1),N)=1\). The function \(L(N)\) counts the largest run of consecutive starts that are not good. Only odd positive \(N\) with exactly three distinct prime factors are considered. Prime powers are allowed. We make no assertion for even moduli or four or more distinct prime factors. As the condition depends only on \(\operatorname{rad}(N)\), the maximum is finite and periodic.

## Proof

**Local sieve.** Consider fourteen consecutive indices \(I=\{0,1,\ldots,13\}\). For any odd prime \(p\mid N\), the index \(i\in I\) has \(p\mid(a+i)(a+i+1)\) precisely if
\[
i\equiv-a-1\quad\text{or}\quad-a\pmod p.
\]
Consequently, if \(r\equiv-a-1\pmod p\), that prime covers the mask
\[
B_p(r)=\{i\in I:i\bmod p\in\{r,r+1\}\},\qquad 0\le r<p.
\]
By the Chinese remainder theorem, choices of \(r\) for distinct primes correspond bijectively to starts modulo their product. A bad run of fourteen exists if and only if the union of three corresponding masks equals \(I\).

**Reduction from infinitely many primes to twenty-six classes.** The primes below fourteen that can divide odd \(N\) are exactly \(3,5,7,11,13\). For any prime \(p\ge17\), since \(14<p\), its mask on \(I\) can only be empty, a singleton, or two neighboring indices. It is therefore contained in the *permissive* family
\[
\mathcal B_{\mathrm{large}}=\{\varnothing\}\cup\{\{i\}:0\le i<14\}\cup\{\{i,i+1\}:0\le i<13\}.
\]
Some members of this permissive family may not be attainable for a fixed large prime; this is an over-approximation used only to prove an upper bound. Every three-distinct-prime support is represented by an unordered three-class multiset from \(3,5,7,11,13,\mathrm{large}\), with each small prime occurring at most once, and with any number of large slots. There are exactly twenty-six such multisets.

**Exact exhaustive certificate.** Encode each local mask by its fourteen-bit indicator integer. For each of the twenty-six class multisets enumerate the Cartesian product of the respective local mask sets and compute the bitwise union. The table records the largest number of covered indices and the number of full fourteen-index coverings. For large slots these are upper bounds and potentially spurious coverings; for small-prime-only slots they are exact.

| Odd-prime classes | Largest covered subset of the 14-index window | Full coverings |
|:--|--:|--:|
| 3, 5, 7 | 14 | 2 |
| 3, 5, 11 | 13 | 0 |
| 3, 5, 13 | 13 | 0 |
| 3, 5, large | 13 | 0 |
| 3, 7, 11 | 13 | 0 |
| 3, 7, 13 | 13 | 0 |
| 3, 7, large | 13 | 0 |
| 3, 11, 13 | 12 | 0 |
| 3, 11, large | 12 | 0 |
| 3, 13, large | 12 | 0 |
| 3, large, large | 12 | 0 |
| 5, 7, 11 | 11 | 0 |
| 5, 7, 13 | 11 | 0 |
| 5, 7, large | 11 | 0 |
| 5, 11, 13 | 11 | 0 |
| 5, 11, large | 11 | 0 |
| 5, 13, large | 10 | 0 |
| 5, large, large | 10 | 0 |
| 7, 11, 13 | 10 | 0 |
| 7, 11, large | 10 | 0 |
| 7, 13, large | 9 | 0 |
| 7, large, large | 8 | 0 |
| 11, 13, large | 8 | 0 |
| 11, large, large | 8 | 0 |
| 13, large, large | 7 | 0 |
| large, large, large | 6 | 0 |

The finite operations can be reproduced by running `python3 verify_paired_sieve_14.py` (Python standard library only). The code explicitly computes every local mask from the displayed congruences, every permitted class triple, and every union; it asserts there are twenty-six cases and exactly two full coverings, both in the class \((3,5,7)\). This computation is logically exhaustive for **all** odd three-prime moduli by the reduction above, not a bounded experiment on moduli.

**Extremizers and maximality.** Direct enumeration of the full residue period \(0\le a<105\), using \(\gcd((a+i)(a+i+1),105)\) for \(i=0,\ldots,13\), yields exactly the starts \(a=2,89\). For both starts, the preceding and succeeding starts are good: \(\gcd((a-1)a,105)=\gcd((a+14)(a+15),105)=1\). Every hypothetical bad run of fifteen contains a bad run of fourteen; by the unique-class result its radical must be \(105\), but neither extremal run extends. Thus \(L(N)\le14\), with equality and the stated start multiplicities exactly as claimed. ∎

## Verification

The self-contained script `verify_paired_sieve_14.py` was executed successfully. It generated all twenty-six table rows, found exactly two full coverings in the \((3,5,7)\) class, independently scanned all \(105\) start residues, and verified that both extreme runs cannot be extended in either direction. As additional non-exhaustive checks, it directly scanned six sample prime supports. No sample scan is invoked to justify the theorem for arbitrary primes; the finite-mask reduction justifies that quantifier.

## Relationship to prior work

Ziller and Morack (arXiv:1706.00317v1, 1 June 2017) define a paired Jacobsthal function for progressions whose coordinate difference is **even** and consider the uniform maximum over such differences. Their companion computation (arXiv:1706.03668v1, 12 June 2017) tabulates that function for primorial moduli. Our pairs have the **fixed odd difference one** and our modulus is odd with exactly three distinct prime divisors; neither definition nor primorial table implies the sharp fourteen-window bound or the exact two extremizers.

Kalmynin and Konyagin (arXiv:2302.00459, first public 1 February 2023) study divisibility of \(x+f(i)\) under *additive output translation*. Our condition is divisibility of \((a+i)(a+i+1)\) under *input translation* and is not the same invariant. OEIS A072753 permits arbitrary pairs of forbidden classes for each prime, rather than requiring the two classes to be consecutive; its listed values do not directly determine our restricted three-prime extremal classification. Nguyen's 2026 finite-window CRT study treats symmetric pairs about a fixed center and finite lifted windows, not this universal adjacent-pair three-prime classification. A literature comparison does not constitute absolute proof of publication novelty.

## Limitations

The claim concerns only a fixed number (three) of distinct odd prime divisors and the adjacent pair offset one. The table is a complete finite exact certificate conditional on the elementary local-mask reduction; it is not a general formula for longer offsets or for more prime factors. The prime-class `large` is a deliberately permissive **superset**, not an assertion that every mask in it occurs for every large prime. The originality assessment covers sources inspected and known nearby results but cannot eliminate unindexed or inaccessible publications. Independent validation has not been performed.

## References

- M. Ziller and J. F. Morack, *Divisibility in paired progressions, Goldbach's conjecture, and the infinitude of prime pairs*, arXiv:1706.00317v1 (first posted 2017-06-01), https://arxiv.org/html/1706.00317v1.
- M. Ziller and J. F. Morack, *A short note on the computation of the generalised Jacobsthal function for paired progressions*, arXiv:1706.03668v1 (first posted 2017-06-12), https://arxiv.org/html/1706.03668v1.
- A. Kalmynin and S. Konyagin, *A polynomial analogue of Jacobsthal function*, arXiv:2302.00459 (first posted 2023-02-01), https://arxiv.org/html/2302.00459v2.
- OEIS A072753, *Maximum gap in two-stage prime-sieves*, https://oeis.org/A072753.
- T. T. K. Nguyen, *Finite-Window Noncovering on Primorial Wheels: Higher-Order CRT Bounds and Shift Correlations*, posted 2026-08-19, https://www.preprints.org/manuscript/202608.1299.
