# Independent mathematical audit

## correctness

PASS

The least-significant-bit recursion follows by splitting n into 2j and 2j+1. For F_L(c)=Σ_{0≤n<2^L} ε(n)ε(7n+c), the recurrence is F_{L+1}(c)=(-1)^c[F_L(⌊c/2⌋)+F_L(⌊(c+7)/2⌋)], with F_0(c)=ε(c), retaining the terminal carry. It preserves F_L(6)=F_L(0)=C_L. Writing S_L=F_L(2)+F_L(4) and J_L=F_L(1)+F_L(5) gives C_{L+1}−C_L=F_L(3), F_{L+1}(3)=−J_L, S_{L+1}=S_L+J_L and J_{L+1}=−2C_L−S_L. Since S_0=−C_1, this gives S_L=−C_{L+1} and C_{L+3}−C_{L+2}=2C_L−C_{L+1}. Taking the sum of the two consecutive characteristic relations gives the order-four positive-coefficient recurrence, with initial data 1,2,2,2; induction proves strict positivity for all L≥0. From the generating function in RESULT.md lines 14–22, the reduced denominator modulo 1+z+z² is −2(z+1), proving coprimality and minimal order three. All roots of λ⁴=λ+2 have modulus less than 2, so the finite-block bias is sublinear. Independent carry reconstruction also confirmed the exact vector identity and direct enumeration through L=13. Replay with the recursion above or the certificate in RESULT.md lines 31–65. The frozen verifier was inspected, not executed; its documentation says Python 3.8+, but int.bit_count actually requires Python 3.10+. This version note does not affect the proof.

## originality

PASS

The supported exact fact is persistent positivity and an order-three reduced recurrence for multiplier seven, not the generic rationality of a finite-state statistic or historical priority for using carries. The closest exact indexed records do not cover its multiplier or correlation. A prior survey remains uninspected in full; priority is not guaranteed.

## value

PASS

This is the first positive multiplier of binary weight three and the next Mersenne multiplier after the oscillatory 3; it is outside the earlier two-one family. The signed finite-block discrepancy is the natural paired-parity diagnostic before doing any carry computation. Its sign at every scale, in contrast to 3, is useful as an exact benchmark for conjectures about multiplicative parity, and the order reduction shows why generic seven-state rationality is not the conclusion. The result does not assert persistent normalized bias, applications beyond that discrepancy, or a general Mersenne sign law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
