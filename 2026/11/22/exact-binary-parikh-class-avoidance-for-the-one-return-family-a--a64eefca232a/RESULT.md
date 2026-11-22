# Exact binary Parikh-class avoidance for the one-return family \(a^r b a b\)

## Finding

Let \(r\ge2\), \(A,B\ge0\) be integers, and let \(P_r=a^r b a b\) be a *scattered* subsequence pattern. For every binary word \(w\) with exactly \(A\) copies of \(a\) and \(B\) copies of \(b\), let \(c(w)=\binom{w}{ab}\), the count of increasing-position pairs \(ab\). Define the avoidance polynomial

\[
F^{(r)}_{A,B}(z)=\sum_{\substack{|w|_a=A,\ |w|_b=B\\P_r\not\preceq w}}z^{c(w)}.
\]

The complete polynomial for **every** \(A,B\ge0\) and \(r\ge2\) is

\[
\boxed{F^{(r)}_{A,B}(z)=1+
\sum_{m=1}^{\min(A,r-1)} z^m {B+m-1\brack m}_z
+\sum_{m=r}^{A}\sum_{v=1}^{B}z^{mv}{B-v+r-1\brack r-1}_z.}
\tag{1}
\]

Here a Gaussian binomial with an invalid lower index is zero, and empty sums vanish. In particular, for \(A\ge r\), \(B\ge1\), the exact number of avoiding words of composition \((A,B)\) is

\[
\boxed{F^{(r)}_{A,B}(1)=\binom{B+r-1}{r-1}+(A-r+1)\binom{B+r-1}{r}.}
\tag{2}
\]

For \(A<r\), all \(\binom{A+B}{A}\) words avoid the pattern; for \(B=0\), the unique word avoids it. More strikingly, when \(A\ge r+1\) and \(B\ge2\), **every** word in the nonempty Parikh class with \(c(w)=AB-1\) contains \(P_r\), while the neighboring class at \(c(w)=AB\) contains no such word. The former class has the unique word \(a^{A-1}ba b^{B-1}\), and the latter has \(a^A b^B\).

For any \(0\le C\le AB\), the exact conditional probability of containing \(P_r\) in the binary Parikh class \(L_{A,B,C}\) is

\[
\boxed{\Pr(P_r\preceq W\mid W\in L_{A,B,C})
=1-\frac{[z^C]F^{(r)}_{A,B}(z)}{[z^C]{A+B\brack A}_z}.}
\tag{3}
\]

The denominator is positive for every indicated \(C\). At the first five-letter case \(r=2\), the unrefined avoidance count simplifies to \(B+1+(A-1)B(B+1)/2\) for \(A\ge2,B\ge1\); with \(A=B=4\) the avoidance polynomial has 35 words and its coefficients at \(C=11,14,15\) are zero.

## Assumptions and scope

Words are finite and linear on the labeled ordered alphabet \(\{a,b\}\); subsequences are scattered rather than contiguous. Exponents denote repeated letters. A Parikh class is determined by the three nonnegative integer observations \(A=|w|_a\), \(B=|w|_b\), \(C=\binom{w}{ab}\). It is nonempty precisely for \(0\le C\le AB\). The Gaussian binomial \({n\brack k}_z\) counts partitions fitting in a rectangle of height \(k\), width \(n-k\), by area. The parameter \(r\) is an integer at least two, not an asymptotic parameter; no claim is made for nonbinary alphabets, cyclic words, other patterns or simultaneous avoidance.

## Proof

**1. Exact word–partition correspondence.** If \(A\ge1\), enumerate the letters \(a\) from left to right and define \(\lambda_i\) to be the number of \(b\)'s after the \(i\)-th \(a\). Then

\[
B\ge\lambda_1\ge\cdots\ge\lambda_A\ge0,\qquad
\sum_{i=1}^A\lambda_i=c(w).
\tag{4}
\]

Conversely each such sequence defines exactly one word:

\[
w=b^{B-\lambda_1}a\,b^{\lambda_1-\lambda_2}a\cdots
b^{\lambda_{A-1}-\lambda_A}a\,b^{\lambda_A}.
\tag{5}
\]

The class-size generating polynomial is therefore the classical Gaussian \({A+B\brack A}_z\). This underlying correspondence is established prior mathematics and is not itself claimed as new.

**2. Necessary and sufficient containment criterion.** To embed \(a^r b a b\), choose \(r\) increasing occurrences of \(a\), with last index \(j\ge r\), then a \(b\) before a later \(a\) indexed \(k>j\), then a final \(b\). The needed conditions are precisely \(\lambda_j>\lambda_k\ge1\). Since the \(\lambda\)'s are nonincreasing, such indices exist if and only if some \(k>r\) satisfies \(\lambda_r>\lambda_k\ge1\). Put \(m=|\{i:\lambda_i>0\}|\). The pattern is therefore absent if \(m\le r\); if \(m>r\), it is absent exactly when

\[\lambda_r=\lambda_{r+1}=\cdots=\lambda_m.\tag{6}\]

This identifies the new structural restriction: all positive rows from index \(r\) onward have a single common length, although the preceding \(r-1\) rows may differ.

**3. Exact generating polynomial.** The all-zero partition contributes the initial \(1\). If \(1\le m\le\min(A,r-1)\) is the number of positive rows, no selected \(a^r b a b\) can occur. Subtracting one from these \(m\) positive row lengths gives an unrestricted partition in an \(m\)-by-\((B-1)\) rectangle, weighted by the factor \(z^m\). Its contribution is the first sum in (1).

If \(r\le m\le A\), equation (6) says the final \(m-r+1\) positive rows all equal an integer \(v\in\{1,\ldots,B\}\). Subtract \(v\) from the first \(r-1\) rows as well. Their excess lengths form a partition \(\mu\) in a rectangle of height \(r-1\) and width \(B-v\). The full area is \(mv+|\mu|\), and the contributions are exactly \(z^{mv}{B-v+r-1\brack r-1}_z\). Every avoiding partition is represented once and only once by its number of positive rows and, in this case, its smallest positive row length. This proves (1) for every boundary case, including \(A=0\) and \(B=0\).

**4. Exact totals and class probabilities.** Evaluating (1) at \(z=1\), the first sum is \(1+\sum_{m=1}^{r-1}\binom{B+m-1}{m}=\binom{B+r-1}{r-1}\) when \(A\ge r,B\ge1\). For each fixed \(m\ge r\), the second sum contributes \(\sum_{v=1}^{B}\binom{B-v+r-1}{r-1}=\binom{B+r-1}{r}\). There are \(A-r+1\) such values of \(m\), proving (2). If \(A<r\), the pattern has too many letters \(a\), and the full count is \(\binom{A+B}{A}\). Formula (3) follows from dividing the exact avoidance coefficient by the strictly positive full-class Gaussian coefficient.

**5. Sharp one-hole universal boundary.** For \(C=AB-1\), the rectangle has exactly one missing cell. The only partition is \(\lambda=(B,\ldots,B,B-1)\), corresponding to the sole word \(a^{A-1}ba b^{B-1}\). If \(A\ge r+1\) and \(B\ge2\), that word contains \(P_r\), taking \(r\) of its first \(A-1\) copies of \(a\), the intervening \(b\), its final \(a\), and a trailing \(b\). For \(C=AB\), the unique word \(a^A b^B\) has no \(a\) after any \(b\) and avoids \(P_r\). This is an exact nonmonotone containment boundary, not an asymptotic extrapolation.

## Verification

The two standalone Python 3 verification programs use only the standard library and can be run as `python3 verify_pattern_family.py` and `python3 verify_partition.py`. The former constructs literal words of all lengths up to 14, tests subsequence containment greedily, and compares their complete \(C\)-coefficient counts with a direct positive-row partition construction for \(r=2,3,4,5,6\). The latter independently enumerates every bounded Ferrers partition for \(0\le A,B\le8\), computes the restriction (6), and compares its polynomial with a separately implemented Gaussian-coefficient recurrence for \(2\le r\le7\). It checks the exact totals and the one-hole universal boundary. All checks pass, with recorded outputs in `CHECK_OUTPUT.txt`; the enumerations corroborate but do not establish the arbitrary-parameter proof in steps 1–5.

## Relationship to prior work

Fazekas, Huang and Mercaş (arXiv:2610.06717v1, first public 2026-10-05) introduce conditional fixed-subsequence containment in binary Parikh classes and prove general arithmetic universality criteria, avoidance bounds and additive approximation (particularly Section 5). Their inspected full text does not state the all-parameter, all-\(r\) polynomial (1) or the one-hole boundary. Richomme (arXiv:2510.07159v1) establishes the underlying Ferrers-partition description, but not this pattern-filtered enumerator. Related published enumerations concern the distinct three-run patterns \(ab^t a\), alternating \((ab)^k a\) (inversion-refined factorial moments), and the five-letter \(abbab\) pattern. Neither alphabet exchange, reversal nor a change of the run parameter turns their claims into (1): the first member \(aabab\) has a different reversal/complement orbit and its avoidance allows a freely varying initial part above a constant positive tail, rather than bounded differences among all positive parts or a bound on occupied interior gaps. The universal \(AB-1\) contrast further distinguishes the structure.

## Limitations

The theorem is restricted to the family \(a^r b a b\), \(r\ge2\). It gives exact coefficients but makes no polynomial-bitlength running-time claim for computing the entire polynomial when \(A,B\) are encoded in binary. The source partition bijection and general conditional probability framework were previously known. An overlooked older equivalent formula for this particular run family remains a historical-priority risk. Independent external validation has not been performed.

## References

1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717v1, first publicly submitted 2026-10-05, https://arxiv.org/abs/2610.06717.
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159v1, first publicly submitted 2025-10-08, https://arxiv.org/abs/2510.07159.
3. R. P. Stanley, *Enumerative Combinatorics*, volume 1, second edition, Section 1.7, for classical Gaussian partition enumeration.
