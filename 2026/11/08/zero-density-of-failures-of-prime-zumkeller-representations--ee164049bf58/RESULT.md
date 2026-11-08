# Zero density of failures of prime–Zumkeller representations

## Finding

Call a positive integer **Zumkeller** if its positive divisors can be partitioned into two sets of equal sums. Let
\[
E(X)=\#\{1\le N\le X:\text{there are no prime }p\text{ and Zumkeller }z\text{ with }N=p+z\}.
\]
Then
\[
\boxed{\lim_{X\to\infty}\frac{E(X)}X=0.}
\]
Thus almost every positive integer, including almost every **even** integer, is a prime plus a Zumkeller number. This proves the **prime-summand assertion** of Somu–Kukla–Tran's Conjecture 4.21 (2023), not its separate square-summand assertion.

More precisely, write \(\gamma=1-3/\pi^2<1\). For every positive integer \(K\), there exist pairwise coprime **odd squarefree Zumkeller numbers** \(Z_1,\ldots,Z_K\), with an associated fixed union of residue classes \(\mathcal B_K\) of natural density at most \(\gamma^K\), such that every sufficiently large integer outside \(\mathcal B_K\) has a prime–Zumkeller representation.

## Assumptions and scope

The construction invokes the established squarefree prime-block Zumkeller lemma of Somu, Kukla and Tran (2023), Lemma 3.3. Specifically, write \(p_j\) for the \(j\)-th prime, let \(f(k)\) be the **least** index such that
\[
\prod_{j=k}^{f(k)}\left(1+\frac1{p_j}\right)\ge2,
\]
and set \(A_k=\prod_{j=k}^{f(k)}p_j\). The cited lemma proves that \(A_k\) is Zumkeller for every sufficiently large index \(k\); the prime-block definition and minimality are essential. We also use the unconditional classical prime number theorem in any fixed reduced arithmetic progression, and the Chinese remainder theorem. No explicit threshold is asserted.

## Proof

**1. Uniformly coprime odd Zumkeller blocks.** By the cited prime-block lemma, for every sufficiently large \(k\), the squarefree integer \(A_k\) is Zumkeller. Choose \(k\ge2\) in this guaranteed range, and abbreviate \(A=A_k\), \(P=\prod_{j=k}^{f(k)}(1+1/p_j)\). Minimality of \(f(k)\) gives
\[
2\le P<2\left(1+\frac1{p_{f(k)}}\right)\le\frac83,
\]
using \(p_{f(k)}\ge3\). On the other hand,
\[
\frac{\varphi(A)}A
=\prod_{j=k}^{f(k)}\left(1-\frac1{p_j}\right)
=\frac{\displaystyle\prod_{j=k}^{f(k)}(1-p_j^{-2})}{P}
>\frac{\displaystyle\prod_{p\text{ odd}}(1-p^{-2})}{8/3}
=\frac3{\pi^2}.
\]
The last Euler product equals \(8/\pi^2\). Thus every such odd squarefree Zumkeller block has coprimality density \(\varphi(A)/A>3/\pi^2\), uniformly in its starting prime.

Choose any \(k_1\) in the lemma's valid range; after selecting \(k_i\), take \(k_{i+1}>f(k_i)\) in the valid range and let \(Z_i=A_{k_i}\). Then \(Z_1,Z_2,\ldots\) are odd, squarefree, Zumkeller, pairwise coprime, and all satisfy \(\varphi(Z_i)/Z_i>3/\pi^2\).

**2. A fixed Zumkeller progression for each block.** If \(Z\) is Zumkeller and \(u\) is coprime to \(Z\), then \(Zu\) is Zumkeller: each divisor of \(Zu\) has a unique product decomposition, and lifting the two equal-sum divisor sets of \(Z\) across every divisor of \(u\) gives an equal-sum partition for \(Zu\). Consequently,
\[
\boxed{Z(1+Zt)\text{ is Zumkeller for every integer }t\ge0.}
\]
Fix any positive integer \(N\) coprime to \(Z\), and consider the class \(r=N-Z\pmod{Z^2}\). Since \(\gcd(r,Z^2)=\gcd(N,Z)=1\), the classical prime number theorem for the **fixed** modulus \(Z^2\) ensures a prime \(p\le N/2\) with \(p\equiv r\pmod{Z^2}\) for all sufficiently large \(N\); the threshold depends on \(Z\), not on \(N\). Then \(z=N-p\ge N/2>0\) is congruent to \(Z\pmod{Z^2}\). Because \(0<Z<Z^2\), necessarily \(z=Z(1+Zt)\) with \(t\ge0\), so \(z\) is Zumkeller. Therefore **every sufficiently large \(N\) coprime to any one fixed \(Z\) is representable**.

**3. An exponentially shrinking finite-modulus obstruction envelope.** For any fixed \(K\), let \(\mathcal B_K\) consist of the positive integers \(N\) satisfying \(\gcd(N,Z_i)>1\) **for every** \(i=1,\ldots,K\). This set is periodic modulo \(M_K=\prod_{i=1}^K Z_i\) and has exact natural density, by coprimality and the Chinese remainder theorem,
\[
\delta_K=\prod_{i=1}^K\left(1-\frac{\varphi(Z_i)}{Z_i}\right)
<\left(1-\frac3{\pi^2}\right)^K=\gamma^K.
\]
Outside \(\mathcal B_K\), some \(Z_i\) is coprime to \(N\), so Step 2 makes every sufficiently large such \(N\) representable. Hence for each fixed \(K\),
\[
\limsup_{X\to\infty}\frac{E(X)}X\le\delta_K\le\gamma^K.
\]
Since \(K\) is arbitrary, the limsup is zero. Nonnegativity gives the asserted limit. \(\square\)

## Verification

`check_density.py` and its recorded output numerically check the exact rational minimal-prime-block inequalities at eleven starting indices, including the uniform lower bound on the corresponding totient ratios. They also independently verify by divisor subset-sum calculation that the classic odd Zumkeller seed \(945\), and twenty-one of its coprime progression multiples, have equal-divisor-sum bipartitions. These experiments do **not** prove the cited prime-block Zumkeller lemma for all large indices, the fixed-modulus prime theorem, or the infinite density conclusion; the proof uses those established results explicitly.

## Relationship to prior work

Somu–Kukla–Tran (2023), Lemma 3.3, provides infinitely many **nonoverlapping squarefree prime-block Zumkeller numbers**. Their Lemma 2.1 gives the coprime-multiplier closure used in Step 2. Their Conjecture 4.21 proposes zero density both for integers lacking a prime–Zumkeller decomposition and separately for integers lacking a square–Zumkeller decomposition. The present argument establishes the former, by combining fixed-modulus primes with independent coprimality obstructions. These cited lemmas individually do **not** state the additive prime-density theorem. Related structural classifications of two-prime-support Zumkeller numbers do not dominate the all-integer density result. A previously obtained quantitative theorem covering all sufficiently large **odd** integers does not address even integers and therefore does not imply this density conclusion; the new argument covers the even part in natural density one.

## Limitations

The result proves a density limit, not an absolute threshold beyond which every integer is representable. It does not settle the square-summand part of Conjecture 4.21, does not provide an effective decay rate for \(E(X)/X\), and does not identify the (possibly infinite) even exceptional set. The proof relies on the published prime-block Zumkeller lemma and fixed-modulus prime distribution. Finite checks cannot certify these infinite statements. An equivalent proof may exist in unindexed literature; no independent audit has occurred.

## References

1. S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149 (first posted 2023-10-22), especially Lemmas 2.1, 3.1–3.3, Conjectures 4.20–4.21. https://arxiv.org/abs/2310.14149
2. Classical prime number theorem in a fixed reduced arithmetic progression (a consequence of nonvanishing of Dirichlet \(L\)-functions at 1). For modern distribution background: J. Thorner and A. Zaman, *Refinements to the prime number theorem for arithmetic progressions*, arXiv:2108.10878 (2021). https://arxiv.org/abs/2108.10878
3. P. Mahanta, M. Saikia, D. Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory 217 (2020), pp. 218–236, for related two-prime-support structural results. https://orca.cardiff.ac.uk/id/eprint/134550/
