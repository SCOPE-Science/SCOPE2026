# The first two 29-adic valuation layers of the Franel numbers

## Finding

For every integer \(n\ge0\), let
\[
F_n=\sum_{j=0}^{n}\binom nj^3.
\]
Write its index in base \(29\) as \(n=\sum_{i\ge0}d_i29^i\), where \(d_i\in\{0,\ldots,28\}\) and all sufficiently high digits are zero. Put \(Z=\{12,14,16\}\), and let \(T(n)\) be the number of digits in \(Z\).

**Theorem.** The first two valuation layers are classified exactly by

1. \(\nu_{29}(F_n)=0\) if and only if \(T(n)=0\).
2. \(\nu_{29}(F_n)=1\) if and only if \(T(n)=1\), with unique exceptional digit at position \(j\), and neither \((d_j,d_{j+1})=(12,17)\) nor \((d_j,d_{j+1})=(16,11)\).
3. All other indices satisfy \(\nu_{29}(F_n)\ge2\).

If \(N_v(L)\) counts the indices \(0\le n<29^L\) having valuation \(v\), then for every \(L\ge2\),
\[
N_0(L)=26^L,\qquad
N_1(L)=3\cdot26^{L-1}+76(L-1)26^{L-2},\qquad
N_{\ge2}(L)=29^L-N_0(L)-N_1(L).
\]
For \(L=1\), the corresponding three counts are \(26,3,0\). The two forbidden pairs show that the first valuation shell is not determined solely by the number of base-\(29\) digits belonging to \(Z\).

## Assumptions and scope

The integer parameter is unrestricted except for \(n\ge0\), and all divisibility assertions refer to the rational prime \(29\). The \(29\)-adic valuation of any nonzero integer \(m\) is \(\nu_{29}(m)=\max\{e\ge0:29^e\mid m\}\). Each \(F_n\) is strictly positive. The assertions determine the valuations \(0\), \(1\), and \(\ge2\), not the exact valuation on the third stratum.

The needed general congruence is Straub's Gessel–Lucas theorem for the sporadic Apéry-like sequence \(F_n\). For every \(m\ge0\), \(0\le d<29\), it gives
\[
F_{29m+d}\equiv F_dF_m+29mF'_dF_m\pmod{29^2},
\]
where the formal derivative \(F'_d\) is integral at \(29\). Its reduction modulo \(29\) can be recovered from the displayed congruence at \(m=1\), because \(F_1=2\) is a unit modulo \(29\).

## Proof

**Step 1: exact finite base data.** The Franel recurrence is
\[
F_0=1,\quad F_1=2,\qquad
(n+1)^2F_{n+1}=(7n^2+7n+2)F_n+8n^2F_{n-1}\quad(n\ge1).
\]
Its exact integer evaluation at \(d=0,\ldots,28\) yields, in this order, the residues \(F_d\pmod{29}\):

```
[1, 2, 10, 27, 27, 19, 17, 9, 10, 3,
 13, 28, 0, 10, 0, 22, 0, 10, 25, 23,
 15, 8, 8, 24, 8, 23, 21, 7, 1]
```

Hence \(29\mid F_d\) exactly for \(d\in Z\). For those digits, write \(c_d=F_d/29\pmod{29}\), and put \(b_d=F'_d\pmod{29}\). The following table gives the exact residues (the fourth column is \(F_{29+d}\pmod{841}\)):

| \(d\) | \(F_d\pmod{841}\) | \(c_d\) | \(F_{29+d}\pmod{841}\) | \(b_d\) | Unique root of \(c_d+m b_d=0\pmod{29}\) |
|---|---:|---:|---:|---:|---:|
| 12 | 203 | 7 | 580 | 3 | 17 |
| 14 | 58 | 2 | 348 | 4 | 14 |
| 16 | 145 | 5 | 493 | 18 | 11 |

The derivative residues follow, without a numerical approximation, from
\[
b_d\equiv2^{-1}\frac{F_{29+d}-2F_d}{29}\pmod{29}.
\]
All entries are independently recomputed by `verify.py` with exact integer arithmetic and compared against the direct binomial sum for the first \(58\) indices.

**Step 2: one-step valuation reduction.** The cited Gessel–Lucas congruence and Lucas congruence give
\[
F_{29m+d}\equiv F_dF_m\pmod{29}.
\]
If \(d\notin Z\), the factor \(F_d\) is a unit modulo \(29\), so \(29\mid F_{29m+d}\) if and only if \(29\mid F_m\). If \(d\in Z\), the congruence modulo \(841\) specializes to
\[
F_{29m+d}\equiv29 F_m(c_d+m b_d)\pmod{841}.
\]
If \(29\mid F_m\), its right-hand side vanishes modulo \(841\). If \(29\nmid F_m\), then \(\nu_{29}(F_{29m+d})=1\) precisely when \(c_d+m b_d\not\equiv0\pmod{29}\); otherwise the valuation is at least two.

**Step 3: iterate over the base digits.** Repeated Lucas reduction proves that no digit in \(Z\) gives valuation zero, whereas at least one digit in \(Z\) gives positive valuation. If there are two or more such digits, peel digits from the least-significant end until the first digit from \(Z\) is reached. The remaining higher-index Franel factor is already divisible by \(29\), so the step-two identity forces divisibility by \(841\); subsequent lower digits not in \(Z\) multiply by units modulo \(29\) and preserve divisibility by \(841\) (the correction term is a multiple of \(29\) times the already divisible higher factor). If exactly one digit \(d_j\) lies in \(Z\), every digit of the higher quotient is outside \(Z\), so its Franel number is a unit modulo \(29\). The only possible extra cancellation is therefore
\[
c_{d_j}+d_{j+1}b_{d_j}\equiv0\pmod{29}.
\]
The table identifies the three potential pairs as \((12,17)\), \((14,14)\), and \((16,11)\). The middle pair cannot occur when exactly one digit lies in \(Z\), because both entries are \(14\). This gives exactly the asserted two exclusions, including the top-digit case by taking the next digit to be zero.

**Step 4: count the digit words.** With no digit in \(Z\), there are \(26\) choices in each of \(L\) positions, giving \(26^L\). If the unique \(Z\) digit is the most significant one, all three choices are allowed, giving \(3\cdot26^{L-1}\) words. At any of the other \(L-1\) positions, the ordered pair consisting of that digit and its higher neighbor has \(3\cdot26-2=76\) allowed possibilities; the remaining \(L-2\) digits independently have \(26\) possibilities. Adding gives the claimed formula for \(N_1(L)\). Complementation gives the remaining count. This completes the proof for all nonnegative indices and every digit length.

## Verification

Run `python3 verify.py` from the directory containing this result. Its all-integer computations verify the complete \(29\)-digit mod-\(29\) table, the three mod-\(841\) derivative residues, the classification for \(0\le n<2600\), the counts on \(0\le n<841\), and \(F_n=\sum_j\binom nj^3\) independently for \(0\le n<58\). The finite checks certify the concrete base tables and guard against mistakes, while the cited Gessel–Lucas theorem supplies the unrestricted congruence used in the proof. No claim of verification for every index by finite testing is made.

## Relationship to prior work

The 2014 MSRI-UP report by Schulte, VanSchalkwyk, and Yang proves digit criteria for primes \(5\), \(7\), and \(13\), and explicitly identifies \(29\) as a type-III prime using \(F_{12}\). This theorem starts from that naturally singled-out prime but supplies a complete mod-\(841\) first-shell language rather than the isolated type-III witness. Malik and Straub established Lucas congruences for sporadic Apéry-like sequences. Straub's 2023 preprint proves the general Gessel–Lucas congruence modulo \(p^2\), which is used as a premise here and is not presented as new. The finite residue table, its two nontrivial digit-pair obstructions, and the resulting all-length shell enumerator are the additional conclusions.

## Limitations

The statement does not classify valuations two or higher individually. No unconditional claim is made that an equivalent instance-specific \(29\)-adic classification has never been recorded in less searchable literature. The proof depends on the existing Gessel–Lucas theorem, and the finite table is independently reproducible by the accompanying code.

## References

- A. Straub, *Gessel–Lucas congruences for sporadic sequences*, arXiv:2301.12248 (first posted 28 January 2023), Theorems 1.2 and 1.3. https://arxiv.org/abs/2301.12248
- A. Schulte, S. VanSchalkwyk, A. Yang, *On the divisibility and valuations of the Franel numbers*, 2014 MSRI-UP Research Reports, Section 2.3.3, Example 2.57, and Theorems 2.44, 2.48 and 2.50. https://slmath-production-assets.sfo3.digitaloceanspaces.com/system/cms/files/81/files/original/Research_Reports_2014_MSRI-UP_(Single_File).pdf
- A. Malik, A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297 (first posted 3 August 2015). https://arxiv.org/abs/1508.00297

