# Exact dyadic factor and reflection complexity of cyclic period-doubling words

## Finding

For each integer \(m\ge 2\), let \(\mathbf{x}_m=(x_m(n))_{n\ge0}\) over \(\{0,1,\ldots,m-1\}\), where \(x_m(n)=\nu_2(n+1)\bmod m\). Write \(\rho_m(\ell)\) for the number of distinct contiguous factors of length \(\ell\), and \(r_m(\ell)\) for the number of their classes under reversal. For every integer \(k\ge1\),

\[
\rho_m(2^k)=(2m-1)2^{k-1},\qquad
r_m(2^k)=\begin{cases}m,&k=1,\\ (2m-1)2^{k-2},&k\ge2.\end{cases}
\]

The language of \(\mathbf{x}_m\) is closed under reversal **at every length**. Its number of palindromic factors of length \(2^k\) equals \(1\) at \(k=1\) and \(0\) at all \(k\ge2\).

More precisely, for \(L=2^k\) and \(0\le j<L\), \(0\le c<m\), form the length-\(L\) template

\[
T_{j,c}(i)=\begin{cases}c,&i=j,\\\nu_2(|i-j|)\bmod m,&0\le i<L,\ i\ne j.\end{cases}
\]

Every factor of length \(L\) occurs among these \(mL\) templates. The only pairs of *different* template parameters giving identical factors are

\[
(j,c)\sim(j+L/2,c),\qquad 0\le j<L/2,\quad c\equiv k-1\pmod m.
\]

In particular, there are exactly \(L/2\) two-element duplicate classes and no larger collision classes. The formulas hold also for \(m=2\) as a compatibility check; the new exact enumeration and collision classification are directed at the full family \(m\ge3\).

## Assumptions and scope

The valuation \(\nu_2(t)\) is the greatest integer \(e\ge0\) such that \(2^e\) divides the positive integer \(t\). Factors are consecutive symbols of the one-sided infinite word; no circular wraparound is used. Reversal identifies \(w\) and \(w^{\mathrm R}\), even if they begin at different positions. No claim is made about a closed formula for \(\rho_m(\ell)\) or \(r_m(\ell)\) at *non-dyadic* lengths. The word is the fixed point beginning in \(0\) of the length-two morphism \(a\mapsto 0(a+1\bmod m)\).

## Proof

**1. Exhaustive templates.** Index the infinite word from \(0\). A contiguous block of length \(L=2^k\) contains exactly one integer divisible by \(L\) among its positive-numbered positions. Let its offset be \(j\) and the corresponding positive integer be \(N\), divisible by \(L\). For any other offset \(i\ne j\), \(0<|i-j|<L\), so

\[
\nu_2(N+i-j)=\nu_2(|i-j|).
\]

The symbol at offset \(j\) is \(c=\nu_2(N)\bmod m\), giving \(T_{j,c}\). Conversely, for any \(j,c\), take \(N=2^e\) with \(e\ge k\) and \(e\equiv c\pmod m\), then start a block at the positive integer \(N-j\). Choosing \(e\) sufficiently large makes the start positive. This realizes every template.

**2. Complete collision classification.** Suppose \(T_{j,c}=T_{j',c'}\) for \(j<j'\). Write \(d=j'-j\) and \(t=\nu_2(d)\). If \(t\le k-2\), choose an offset \(i\in\{0,\ldots,L-1\}\) satisfying \(i\equiv j+2^{t+1}\pmod{2^{t+2}}\); such an \(i\) exists because the interval of length \(2^k\) contains representatives of every residue modulo \(2^{t+2}\). Necessarily \(i\ne j,j'\). Then

\[
\nu_2(|i-j|)=t+1,\qquad\nu_2(|i-j'|)=t.
\]

These symbols differ modulo \(m\) because \(m\ge2\). Hence \(t=k-1\) is necessary, forcing \(d=L/2\). At all offsets except \(j,j'\), the two templates coincide: subtracting \(L/2\) from an integer not divisible by \(L/2\) preserves its \(2\)-adic valuation. At offsets \(j\) and \(j'\), equality holds precisely when \(c=c'=(k-1)\bmod m\). Thus the only collisions are the stated \(L/2\) pairs. Subtracting them from the \(mL\) parameters yields \(\rho_m(L)=mL-L/2\).

**3. Reversal closure.** For any factor in positive-numbered positions \(a,a+1,\ldots,a+\ell-1\), choose a power \(Q=2^h>a+\ell-1\). For every \(1\le t<Q\), the identity \(\nu_2(Q-t)=\nu_2(t)\) holds. Therefore the symbols at the positive positions \(Q-(a+\ell-1),\ldots,Q-a\) occur in the reverse order and match the given factor exactly. Hence all factor sets are reversal closed. At dyadic length, the template calculation also gives \(T_{j,c}^{\mathrm R}=T_{L-1-j,c}\).

**4. Even palindrome count.** At dyadic length \(L\), every template has the symbol \(0\) at every offset \(i\ne j\) with \(i-j\) odd. Such offsets form exactly one parity class. Reversal of a word of even length interchanges the parity classes; if the word is a palindrome, its other parity class must also be all \(0\). But for \(L\ge4\), there exists an offset with \(\nu_2(|i-j|)=1\), carrying symbol \(1\), a contradiction. At \(L=2\), the sole palindrome is \(00\). Since every factor and its reverse appear, each two-element reversal orbit contributes two words and each palindrome contributes one, so \(r_m(L)=(\rho_m(L)+\operatorname{Pal}_m(L))/2\), which gives the stated values.

## Verification

`VERIFY.py` (Python 3, standard library only) enumerates every template and every collision class for \(2\le m\le8\), \(1\le k\le8\), compares factor counts and reversal orbits with the closed formulas, and checks palindromes. Independently, for \(2\le m\le5\), \(1\le k\le5\), it exhaustively compares templates with all blocks in an explicit prefix of the valuation word long enough to exhibit all templates. These finite checks supplement rather than replace the proof for all \(m,k\).

## Relationship to prior work

Allouche–Campbell–Li–Shallit–Stipulanti introduce reflection complexity and evaluate it for the **binary** period-doubling word \(x_2\) (Section 6.2, arXiv:2406.09302, first posted 2024-06-13); the case \(m=2\) of the formula above is not claimed as novel. Barro–Kaboré–Bognini analyze palindromic factors and palindromic factorizations of the generalized word (Australasian Journal of Combinatorics 83 (2022), 435–447); this gives relevant prior structural information, and the absence of even palindromes at these lengths is not advanced as an independent novelty. Bognini–Ammar examine generalized \(m\)-letter period-doubling words via kernel words and gap factorizations (arXiv:2511.20881, first posted 2025-11-25), including earlier palindromic factorizations, but the inspected statements are not an all-modulus dyadic factor/reversal census. Blažek–Dvořáková–Pelantová study group-generated generalized reflection complexity and binary examples (arXiv:2610.14637, first posted 2026-10-10); their definitions do not imply the enumerated \(m\ge3\) formulas without additional structure. The structural two-center collision classification is stronger than the count alone.

## Limitations

This is an exact statement at lengths that are powers of two, not a general-length classification. The result's bibliographic novelty remains conditional on literature coverage, especially possible unindexed formulas for generalized substitution factor complexity. The binary slice is already subsumed by published work. The supplied checks are finite and are not an independent audit; the infinite statement rests on the written proof.

## References

1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first public 2024-06-13), https://arxiv.org/abs/2406.09302.
2. K. E. Bognini, H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881 (first public 2025-11-25), https://arxiv.org/abs/2511.20881.
3. M. Barro, I. Kaboré, K. E. Bognini, *On the palindromic zl-factorization and c-factorization of the generalized period-doubling sequences*, Australasian Journal of Combinatorics 83(3) (2022), 435–447, https://ajc.maths.uq.edu.au/pdf/83/ajc_v83_p435.pdf.
4. A. Blažek, L. Dvořáková, E. Pelantová, *Generalized reflection complexity*, arXiv:2610.14637 (first public 2026-10-10), https://arxiv.org/abs/2610.14637.
