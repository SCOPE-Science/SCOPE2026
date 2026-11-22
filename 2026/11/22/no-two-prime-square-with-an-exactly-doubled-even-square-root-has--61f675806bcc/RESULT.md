# No two-prime square with an exactly doubled even square root has the delta property

## Finding

For every prime \(q\) and every integer \(b\ge1\), the perfect square
\[
  n=(2q^b)^2=4q^{2b}
\]
does **not** have the \(\Delta\) property: no three positive factor-pair differences \(n/d-d\), with \(1<d<\sqrt n\) and \(d\mid n\), have a relation in which one is the sum of the other two (with the two summands permitted to coincide). Thus this entire two-prime-root ray is excluded, including the exceptional prime \(q=3\) not addressed by the published dominating-prime criterion.

## Assumptions and scope

The \(\Delta\) property is defined as in Schvöllner's original paper, using a triple \(1<x<y\le z<\sqrt n\) of divisors of \(n\) satisfying
\[
  \frac n x-x=\left(\frac n y-y\right)+\left(\frac n z-z\right).
\]
The square root is exact and the minimum divisor \(x\) is strictly greater than one. The theorem concerns all primes \(q\), including \(q=2\), and all integer exponents \(b\ge1\). It does not assert the same statement for arbitrary two-prime-supported square roots.

## Proof

For \(q=2\), \(n\) is a pure power of two and is excluded by Theorem 5.5 of Schvöllner (2026). For every odd prime \(q\ge5\), apply Theorem 5.3 of the same paper with \(p=2\), exponent \(x=2\), and exponent \(y=2b\): the condition \(q>2^2\) holds, so \(4q^{2b}\) cannot possess a \(\Delta\)-triple. It remains to prove the exclusion for \(q=3\).

Suppose for contradiction that \(b\ge1\) is the *smallest* integer for which \(n=4\cdot3^{2b}\) has a \(\Delta\)-triple. Set \(M=3^{2b}\) and \(L=\sqrt n=2\cdot3^b\). The divisors \(d\) with \(1<d<L\) are precisely
\[
 3^j\ (1\le j\le b),\quad
 2\cdot3^j\ (0\le j<b),\quad
 4\cdot3^j\ (0\le j<b).
\]
Their positive differences are respectively
\[
 A_j=4\cdot3^{2b-j}-3^j,\quad
 B_j=2(3^{2b-j}-3^j),\quad
 C_j=3^{2b-j}-4\cdot3^j.
\]
All of these are divisible by three except precisely
\[
 B_0=2M-2\equiv1\pmod3,\qquad
 C_0=M-4\equiv2\pmod3.
\]
Moreover \(B_0\) is **strictly the largest positive difference**, because \(d\mapsto n/d-d\) decreases strictly with \(d>0\) and its least permitted divisor is \(d=2\). Also \(B_0> C_0>0\), and
\[
 B_0-C_0=M+2\equiv2\pmod3,\qquad B_0-2C_0=6\ne0.
\]

We now exclude a triple using \(B_0\) or \(C_0\). If exactly one occurrence comes from the exceptional pair, reducing the difference equation modulo three rules it out. If both occur as distinct differences, they cannot both appear on the right because their sum exceeds the largest difference \(B_0\), and \(C_0\) cannot occur on the left with \(B_0\) on the right. The sole ordering is \(B_0=C_0+D\), but \(D\) is divisible by three while \(B_0-C_0\) is not. If \(C_0\) appears twice on the right, the only possible ordering is \(B_0=2C_0\), contradicted by \(B_0-2C_0=6\); the other possibilities fail modulo three. No two copies of \(B_0\) can appear on the right because it is largest. Therefore all three divisors in a hypothetical triple must be divisible by three.

For these three divisors \(d\), their complements \(n/d\) are also divisible by three: the exponent of three in each \(d\) lies between \(1\) and \(b\), whereas \(\nu_3(n)=2b\). Dividing each factor pair by three therefore gives the same difference relation for \(n'=n/9=4\cdot3^{2(b-1)}\). The resulting divisors are strictly below \(\sqrt{n'}\) and retain their strict/weak order. If the least resulting divisor is greater than one, this is a \(\Delta\)-triple for \(n'\), contradicting minimality of \(b\). If it is one, its difference is \(n'-1\); Corollary 2.2 of Schvöllner (2026) excludes any \(\Delta\)-type additive relation involving this maximal factor difference. This also contradicts the assumed triple. The proof is complete.

## Verification

The companion standalone verifier enumerates all divisors strictly between one and the square root for a specified finite collection of primes and exponents; it checks the absence of additive triples by exact integer arithmetic. The infinite assertion is proven by the prime-dominance reduction, the modulus-three separation, and minimal-exponent descent above. Finite tests are diagnostic only and do not substitute for that argument.

## Relationship to prior work

Schvöllner's original 2026 treatment of the \(\Delta\) property proves a general dominating-prime obstruction (Theorem 5.3), pure-prime-power exclusion (Theorem 5.5), and the semiprime-square case (Lemma 5.6). These establish the present theorem for \(q=2\), all \(q\ge5\), and \(b=1\), respectively, but leave the infinite exceptional family \(4\cdot3^{2b}\) for \(b\ge2\). The present modular descent fills this remaining family and thereby yields a uniform all-prime statement. The November 2026 work by Golfieri and Schvöllner motivates the focus on squares and their arithmetic primitivity. This theorem is a boundary classification, not a claim about all two-prime-supported squares.

## Limitations

No universal classification for \(p^{2a}q^{2b}\) with unrestricted \(p,q,a,b\) is asserted. The proof uses a published ingredient excluding factor-difference relations with the unit factor. Priority remains subject to unpublished or unindexed equivalent arguments; no independent audit has been performed.

## References

1. V. N. Schvöllner, *The Δ property: a bridge between split graphs and number theory*, arXiv:2605.25264 (2026), especially Corollary 2.2, Theorems 5.3 and 5.5, and Lemma 5.6. https://arxiv.org/abs/2605.25264
2. M. Golfieri and V. N. Schvöllner, *Primitive squares with the Δ property*, arXiv:2611.11574 (first public preprint dated 2026-11-08). https://arxiv.org/abs/2611.11574
