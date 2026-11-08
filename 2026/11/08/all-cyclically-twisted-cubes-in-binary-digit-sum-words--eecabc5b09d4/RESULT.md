# All cyclically twisted cubes in binary-digit-sum words

## Finding

Let \(N\ge3\), let \(\Sigma=\mathbb Z/N\mathbb Z\), and define the infinite word \(\mathbf t=t_0t_1\cdots\) by \(t_n=s_2(n)\pmod N\), where \(s_2(n)\) is the sum of the binary digits of the nonnegative integer \(n\). Let \(\sigma(a)=a+1\pmod N\) act letterwise on words. For each position \(s\ge0\) and each root length \(m\ge1\), call the length-\(3m\) factor starting at \(s\) a *cyclically twisted cube* if it has the form \(X\sigma(X)\sigma^2(X)\), for some word \(X\) of length \(m\).

**Theorem (complete root-length and occurrence classification).** A cyclically twisted cube beginning at \(s\) with root length \(m\) occurs if and only if \(m=2^e\) for some integer \(e\ge0\), and there are integers \(r\ge1\), \(j\ge0\) for which

\[
2^e\bigl(2^{Nr}(2j+1)-2\bigr)\ \le\ s\ \le\ 2^e\bigl(2^{Nr}(2j+1)-1\bigr).
\]

All bounds are inclusive, and all positions are zero-based. Consequently, the root lengths that occur are exactly the powers of two; for every such length there are infinitely many occurrences. The earliest occurrence for root length \(2^e\) is exactly

\[
s_{\min}(N,e)=2^e(2^N-2).
\]

The statement holds verbatim, up to relabeling letters, for the fixed point of \(\varphi(a)=a\sigma(a)\) on any \(N\)-letter alphabet with \(\sigma\) a cyclic permutation.

## Assumptions and scope

All words are one-sided and indexed beginning at zero. The alphabet symbols are residues modulo \(N\); a twisted cube requires *equality of the three consecutive whole blocks after the specified cyclic letter shift*, not an ordinary cube, not Abelian equivalence, and not the existence of a twisted subsequence. The theorem quantifies over every integer \(N\ge3\), every integer \(s\ge0\), and every integer \(m\ge1\). The length-\(3m\) factor is necessarily defined because the sequence is infinite. Define \(\nu_2(z)\) for positive \(z\) as the exponent of two dividing \(z\).

The binary-digit-sum construction is identical to the fixed point of \(\varphi(a)=a(a+1)\) because \(s_2(2n)=s_2(n)\) and \(s_2(2n+1)=s_2(n)+1\). Conjugating the cyclic permutation \(\sigma\) to the shift of residues transports all factors and preserves their starting positions.

## Proof

**1. A shifted-difference criterion.** For \(h\ge1\), put

\[
D_h(n)=s_2(n+h)-s_2(n)\pmod N.
\]

A length-\(3m\) factor at \(s\) is \(X\sigma(X)\sigma^2(X)\) if and only if

\[
D_m(n)=1\pmod N\qquad(s\le n\le s+2m-1).
\]

Indeed, this requires each letter of the middle block to be the corresponding first-block letter plus one and each letter of the last block to be the corresponding middle-block letter plus one. Conversely, those two sets of equalities reconstruct the displayed block decomposition.

**2. Odd-part obstruction.** Write \(m=2^e u\), where \(u\) is odd. By separating the low \(e\) binary digits, for \(0\le r<2^e\) one obtains the exact identity

\[
D_m(2^e q+r)=D_u(q).
\]

A run of \(2m=2^{e+1}u\) consecutive positions on which \(D_m=1\) contains at least \(2u-1\) entire, consecutive blocks of length \(2^e\). Hence \(D_u(q)=1\) on at least \(2u-1\) consecutive integers \(q\).

We now prove that when \(u\ge3\) is odd, \(D_u\) cannot equal one on five consecutive integers. Write \(u=2v+1\). For any \(h\ge0\), binary-digit identities give

\[
D_u(2h)=s_2(h+v)+1-s_2(h),\qquad
D_u(2h+1)=s_2(h+v+1)-1-s_2(h)\pmod N.
\]

If both expressions equal one, subtraction forces

\[
s_2(h+v+1)-s_2(h+v)=2\pmod N.
\]

For every nonnegative \(z\), the elementary carry identity \(s_2(z+1)-s_2(z)=1-\nu_2(z+1)\) therefore implies

\[
\nu_2(h+v+1)\equiv-1\pmod N.
\]

In particular, \(h+v+1\) must be even, because \(N\ge3\). But five consecutive integers contain two full aligned pairs \((2h,2h+1)\) with consecutive values of \(h\). The two required integers \(h+v+1\) would then be consecutive and hence could not both be even. Contradiction. If \(u\ge3\), then \(2u-1\ge5\), contradicting the required run. Thus every twisted-cube root length is \(m=2^e\).

**3. Exact positions for dyadic roots.** Let now \(m=2^e\). The low-digit identity reduces to

\[
D_m(n)=s_2(\lfloor n/m\rfloor+1)-s_2(\lfloor n/m\rfloor)
=1-\nu_2(\lfloor n/m\rfloor+1)\pmod N.
\]

Write \(s=mq+r\) with \(0\le r<m\). If \(r=0\), the \(2m\) positions in the criterion have quotient values \(q,q+1\); if \(r>0\), their quotient values are \(q,q+1,q+2\). In either case, each required \(\nu_2\) must be divisible by \(N\). Odd positive integers have valuation zero, while two consecutive even integers differ by two and cannot both have valuation divisible by \(N\ge3\).

For \(r=0\), exactly one of \(q+1,q+2\) is even. Thus the condition holds precisely when its \(2\)-adic valuation is a positive multiple of \(N\). For \(r>0\), the three numbers \(q+1,q+2,q+3\) must satisfy the condition: necessarily \(q\) is even (otherwise the first and last are even and cannot both qualify), and then precisely \(q+2\) must have valuation a positive multiple of \(N\).

It follows that each even nonnegative \(Q\) with \(\nu_2(Q+2)\in N\mathbb Z_{>0}\) contributes exactly the \(m+1\) consecutive starting positions

\[
mQ,mQ+1,\ldots,m(Q+1),
\]

with no other possibilities. The last endpoint \(m(Q+1)\) is the aligned case with odd quotient \(q=Q+1\). The valuation criterion is equivalent to

\[
Q+2=2^{Nr}(2j+1)\qquad(r\ge1,\ j\ge0),
\]

which proves the theorem and its inclusive interval formula.

**4. Sharp first occurrence.** The smallest admissible \(Q\) is \(2^N-2\), corresponding to \(r=1,j=0\), so the first position for \(m=2^e\) is exactly \(2^e(2^N-2)\). Conversely the interval with this \(Q\) supplies \(m+1\) occurrences, and increasing \(j\) supplies infinitely many further intervals. This also proves that every power of two occurs as a root length. \(\square\)

## Verification

The standalone file `check_twisted_cubes.py` independently builds the fixed point using the letterwise morphism and checks it against binary digit sums. It then compares a direct three-block twisted-cube test with the theorem's power-of-two and valuation criterion for every \(N\in\{3,\ldots,10\}\), every \(1\le m\le120\), and every \(0\le s<4096\): 3,932,160 comparisons. It also scans all positions before the proposed earliest start whenever the requested factor fits in a 16,384-symbol prefix. All checks pass.

These finite computations are consistency checks. The all-parameter proof rests on the carry identity and the odd-part obstruction above. To replay: `python3 check_twisted_cubes.py`.

## Relationship to prior work

Abdullah and Hamoud, *Novel Constructions of Words with Strong Avoidance Properties and their Combinatorial Analysis*, arXiv:2505.11403v1 (public May 16, 2025), introduce strongly twisted repetitions for the morphism \(a\mapsto a\sigma(a)\). Their Theorem 2.6 treats \(\delta=\sigma^j\) with \(j\not\equiv1\pmod N\); Section 3 explicitly singles out \(\delta=\sigma\) as a natural remaining case. The present theorem treats that excluded permutation and gives every length and starting position, without relying on their avoidance theorem.

Blondin-Massé, Brlek, Glen and Labbé, *On the critical exponent of generalized Thue–Morse words*, arXiv:0710.4031v1 (2007), determine ordinary powers and their critical-factor positions, not three successive blocks related by a nontrivial letter permutation. Allouche and Shallit, *Sums of Digits, Overlaps, and Palindromes* (2000), prove ordinary overlap avoidance, square existence and palindrome results for these digit-sum words. These statements do not imply the present twisted-cube occurrence classification.

## Limitations

The exact theorem concerns three blocks and the one-step cyclic letter shift, and requires \(N\ge3\). It does not classify twisted powers with four or more blocks, arbitrary permutations not conjugate to an \(N\)-cycle, or arbitrary base beyond binary. It does not claim a new classification of ordinary powers. The historical-literature comparison does not establish definitive global priority; unindexed or inaccessible equivalent results may exist. Independent mathematical validation has not been performed.

## References

1. D. Abdullah and J. Hamoud, *Novel Constructions of Words with Strong Avoidance Properties and their Combinatorial Analysis*, arXiv:2505.11403v1, May 16, 2025. https://arxiv.org/abs/2505.11403
2. A. Blondin-Massé, S. Brlek, A. Glen and S. Labbé, *On the critical exponent of generalized Thue–Morse words*, arXiv:0710.4031v1 (2007). https://arxiv.org/abs/0710.4031
3. J.-P. Allouche and J. Shallit, *Sums of Digits, Overlaps, and Palindromes*, Discrete Mathematics & Theoretical Computer Science 4 (2000), 1–10. https://doi.org/10.46298/dmtcs.282
