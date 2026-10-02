# Prime-power descent for Perrin pseudoprimes

## Result

Let `(P_n)_{n in Z}` be the doubly infinite Perrin sequence,

`P_0=3, P_1=0, P_2=2, P_n=P_{n-2}+P_{n-3}`,

with the recurrence extended to negative indices. For every prime `p` and every integer `k>=1`,

\[
P_{p^k}\equiv P_{p^{k-1}}\pmod{p^k},\qquad
P_{-p^k}\equiv P_{-p^{k-1}}\pmod{p^k}.
\]

Consequently, prime-power Perrin pseudoprimality is downward closed in the exponent:

1. If `p^k | P_{p^k}` for some `k>=2`, then `p^j | P_{p^j}` for every `1<=j<=k`.
2. If in addition `P_{-p^k}=-1 (mod p^k)`, then the same two-sided condition holds at every lower prime power `p^j`.
3. In particular,
   \[
   p^2\mid P_{p^2}\iff p^2\mid P_p,
   \]
   and `p^2` passes the minimal restricted Perrin test if and only if
   \[
   P_p\equiv0\pmod{p^2},\qquad P_{-p}\equiv-1\pmod{p^2}.
   \]

Combining this descent with the current exhaustive statement in OEIS A173656 that the only primes `p<10^10` satisfying `p^2|P_p` are `521` and `190699`, plus exact lift checks at these two primes, gives:

**Database-assisted finite classification.** Among composite prime powers `n<10^20`, the unrestricted Perrin pseudoprimes are exactly

\[
521^2=271441,\qquad 190699^2=36366108601.
\]

There is **no** prime power `n<10^20` passing the minimal restricted test

\[
P_n\equiv0\pmod n,\qquad P_{-n}\equiv-1\pmod n.
\]

Hence there is also no prime power below `10^20` passing either of the stronger Adams--Shanks or Grantham Perrin tests, since those tests impose the minimal restricted congruences among their conditions.

As a current-status check, OEIS A173656 now lists three primes

\[
521,\quad 190699,\quad 36944128783.
\]

Exact modular computation shows that all three have unrestricted prime-power height exactly two: their squares pass `P_n=0 (mod n)`, their cubes fail it, and none of their squares passes the minimal restricted test.

## Proof of the prime-power congruences

Set

\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}.
\]

The characteristic polynomial of `M` is `x^3-x-1`, and Cayley--Hamilton gives

\[
P_n=\operatorname{tr}(M^n)
\]

for every integer `n`; here `det(M)=1`, so `M^{-1}` is integral and the identity also holds for negative indices.

We use the classical matrix Gauss congruence: for every integral square matrix `A`, prime `p`, and `k>=1`,

\[
\operatorname{tr}(A^{p^k})\equiv
\operatorname{tr}(A^{p^{k-1}})\pmod{p^k}.
\]

For completeness, one short proof is as follows. Since

\[
\exp\!\left(\sum_{n\ge1}\frac{\operatorname{tr}(A^n)}n t^n\right)
=\frac1{\det(I-tA)}\in1+t\mathbb Z[[t]],
\]

write its unique Euler product as

\[
\prod_{m\ge1}(1-t^m)^{-b_m},\qquad b_m\in\mathbb Z.
\]

Comparing logarithmic coefficients gives

\[
\operatorname{tr}(A^n)=\sum_{d\mid n} d b_d.
\]

For `n=p^k`, subtracting the formula for `p^{k-1}` leaves exactly `p^k b_{p^k}`. Applying this first to `M` and then to the integral matrix `M^{-1}` proves both Perrin congruences.

If `p^k|P_{p^k}`, the first congruence implies `p^k|P_{p^{k-1}}`, hence certainly `p^{k-1}|P_{p^{k-1}}`; iteration gives descent. The negative congruence gives the two-sided descent identically. For `k=2`, the same congruences give the square criteria immediately.

There is also a useful cubic interpretation. Since the roots of `x^3-x-1` have product one,

\[
\chi_{M^n}(x)=x^3-P_nx^2+P_{-n}x-1.
\]

Thus the minimal restricted condition at `n` is exactly

\[
\chi_{M^n}(x)\equiv\chi_M(x)\pmod n.
\]

## Finite classification below `10^20`

Let `n=p^k<10^20` be a composite prime power, so `k>=2` and `p<10^10`. If `n` is an unrestricted Perrin pseudoprime, descent forces `p^2` to be one as well, equivalently `p^2|P_p`. The current OEIS A173656 entry states that below `10^10` the only such primes are `521` and `190699`.

For these primes, exact modular computations give

| `p` | `P_{-p} mod p^2` | target `p^2-1` | `P_{p^2}/p^2 mod p` |
|---:|---:|---:|---:|
| 521 | 154736 | 271440 | 508 |
| 190699 | 132154406 | 36366108600 | 35803 |

The last column is nonzero, so `p^3` fails the unrestricted test for both primes. By descent, every higher power fails as well. The middle columns show that neither square passes the minimal restricted test. The even prime is excluded directly since `P_2=2` is not divisible by `4`.

The verification artifact performs these computations by two independent exact modular representations: `3 x 3` matrix exponentiation and exponentiation in `(Z/mZ)[x]/(x^3-x-1)`. It also checks the newly listed third A173656 prime `36944128783`; its square passes only the unrestricted test, while its cube fails.

## Context and originality

The Perrin primality test goes back to Lucas and Perrin; Adams and Shanks found the first unrestricted pseudoprime `521^2` and developed stronger signature tests. Later work characterized and enumerated several restricted variants, and Grantham proved that unrestricted Perrin pseudoprimes are infinite. The prime-power trace congruence used above is classical matrix Gauss-congruence theory and is **not** claimed as new.

The contribution here is the explicit prime-power descent/lifting formulation for the Perrin unrestricted and minimal restricted tests, together with its finite consequence that the unrestricted prime powers below `10^20` are exactly the two squares above and that no prime power in that range passes the minimal restricted (hence stronger) tests. To the best of our knowledge, this formulation and finite classification were not found in the checked Perrin literature or current sequence records.

The main literature uncertainty is older specialized work on third-order recurrence pseudoprimes. Adams (1987) gives a broad characterization in terms of periods, and Adams--Shanks (1982) contains substantial arithmetic analysis of the Perrin test. Their bibliographic records and available descriptions were checked, but complete full text was not inspected here. Either could contain an equivalent prime-power consequence under different terminology. This residual risk is why originality is asserted only to the best of our knowledge.

## Limitations

- The `10^20` classification uses the explicit completeness statement in OEIS A173656 for primes below `10^10`; that large prime search was not independently repeated here.
- No claim is made that the three currently listed A173656 primes are all such primes globally.
- No classification is claimed for non-prime-power Perrin pseudoprimes.
- The matrix Gauss congruence is prior mathematics; only its Perrin pseudoprime consequences are at issue for originality.

## Reproducibility

Run `python3 artifacts/verify.py`. The deterministic output is stored in `artifacts/verification.txt`.

## References

1. W. W. Adams and D. Shanks, *Strong primality tests that are not sufficient*, Mathematics of Computation 39 (1982), 255--300. https://doi.org/10.1090/S0025-5718-1982-0658231-9
2. W. W. Adams, *Characterizing pseudoprimes for third-order linear recurrences*, Mathematics of Computation 48 (1987), 1--15. https://doi.org/10.1090/S0025-5718-1987-0866094-6
3. A. V. Zarelua, *On congruences for the traces of powers of some matrices*, Proceedings of the Steklov Institute of Mathematics 263 (2008/2009). https://doi.org/10.1134/S008154380804007X
4. H. Steinlein, *Fermat's Little Theorem and Gauss Congruence: Matrix Versions and Cyclic Permutations*, American Mathematical Monthly 124 (2017), 548--553. https://doi.org/10.4169/amer.math.monthly.124.6.548
5. Dana Jacobsen, *Perrin Primality Tests*. https://ntheory.org/primality/perrin.html
6. OEIS A173656, primes `p` such that `p^2` divides `P(p)`. https://oeis.org/A173656
7. OEIS A013998, unrestricted Perrin pseudoprimes. https://oeis.org/A013998
8. OEIS A018187, minimal restricted Perrin pseudoprimes. https://oeis.org/A018187
