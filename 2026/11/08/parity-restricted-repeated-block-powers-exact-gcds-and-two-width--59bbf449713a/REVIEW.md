# Mathematical review

## Correctness: PASS

The theorem fixes the base, repetition count, canonical-block coefficient range, and all odd/even positive widths. An entire width's permitted block coefficients have gcd one. The two-primary factorization of the repetition count makes every odd-width geometric sum divisible by \(H\); Kane–Sanna–Shallit's published unrestricted-base gcd lemma supplies the additional \(\gcd(t,U)\) factor without assuming the factors are coprime. Because \(U\) is odd, \(H\) is invertible modulo \(U\), and the widths \(1\) and \(t\) force the claimed exact gcd. Even widths reduce to base \(b^2\). Boundary cases \(t=1\), even and odd bases, and repetition count \(2\) are included. Executable finite checks are auxiliary, not substitutes for these arguments.

## Originality: PASS within inspected evidence

Kane–Sanna–Shallit (arXiv:1801.04483, Theorem 1) compute the unrestricted repeated-block gcd and explicitly treat all bases \(b\ge2\); the inspected full text already implies the odd-width result when \(k\) is odd, since its published witness widths \(1,k\) are then both odd. It does not give the even-\(k\) odd-width answer or widths \(1,t\) certificate. For even repetition count the unrestricted result does not imply the odd-width answer: base \(2\), four repetitions, has unrestricted gcd \(1\) versus odd-width gcd \(15\). The even-width identity follows directly from their base-general result and is attributed, not claimed as new. Targeted semantic and bibliographic searches did not find an equivalent classification. The remaining risk is an unindexed equivalent repunit divisibility statement; lack of a search result alone is not evidence of priority.

## Mathematical value: PASS

The parity of the canonical block width is a natural digit-system restriction of the exact GCD obstruction studied by the motivating paper. The complete odd-width classification, with new content for even repetition counts, identifies an arithmetic transition governed by the odd part of the repetition count. Its two-width certificate is valid for every integer base and every repetition count. In particular, a power-of-two repetition count yields an exponentially large common divisor at odd widths while the unrestricted binary family has gcd \(1\), a useful boundary for future parity-restricted Waring investigations. The scope is exact common divisors, not bounded-summand Waring theorems.

## Closest literature and residual limitations

D. M. Kane, C. Sanna, J. Shallit, *Waring's Theorem for Binary Powers*, arXiv:1801.04483v1 (2018-01-13), Section 2, Theorem 1, complete author-hosted PDF at https://cseweb.ucsd.edu/~dakane/waring.pdf . The computed parity-width gcds do not determine minimal numbers of summands or exact Frobenius numbers. A complete bibliographic priority guarantee would require additional literature coverage.

Self-review: passed. Independent audit: not yet performed.
