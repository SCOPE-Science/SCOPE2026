# Exact pair-sign laws and sharp autocorrelation extremizers for Domb numbers modulo five

## Finding

Define the Domb numbers and quadratic-character signs by
\[
D_n=\sum_{j=0}^{n}\binom nj^2\binom{2j}j\binom{2(n-j)}{n-j},\qquad
f(n)=\chi_5(D_n)\in\{-1,1\},\quad n\ge0,
\]
where \(\chi_5\) is the quadratic character modulo \(5\), with \(\chi_5(1)=\chi_5(4)=1\) and \(\chi_5(2)=\chi_5(3)=-1\). No Domb number is divisible by \(5\).

**Exact nearest-neighbor law.** For each integer \(r\ge1\), put \(N=5^r\). For any \(\sigma,\tau\in\{-1,1\}\), the exact number of indices \(0\le n<N\) with \((f(n),f(n+1))=(\sigma,\tau)\) is
\[
\boxed{\frac{5^r+(\sigma+\tau)3^r+\sigma\tau}{4}.}
\]
In particular, the two mixed-sign cells each occur \((5^r-1)/4\) times, while the two same-sign cells occur \((5^r+2\cdot3^r+1)/4\) and \((5^r-2\cdot3^r+1)/4\) times. These are counts of pairs beginning in the specified interval; \(f(N)\) is included as a possible second value.

**All-shift sharp spectrum.** For every fixed integer \(h\ge0\), the rational limit
\[
C(h)=\lim_{N\to\infty}\frac1N\sum_{0\le n<N}f(n)f(n+h)
\]
exists, and its finite-cutoff error is \(O_h(\log(2N))\). Write \(h=5q+a\), \(0\le a\le4\). The entire spectrum is uniquely specified by \(C(0)=1\), \(C(1)=0\), and
\[
\begin{aligned}
C(5q)&=C(q),\\
C(5q+1)&=\tfrac15C(q+1),\\
C(5q+2)&=\tfrac15(-C(q)+2C(q+1)),\\
C(5q+3)&=\tfrac15(2C(q)-C(q+1)),\\
C(5q+4)&=\tfrac15C(q).
\end{aligned}
\]
Here the first formula is used for \(q\ge1\); the remaining formulas hold for \(q\ge0\). For every \(h\ge1\),
\[
\boxed{-\frac15\le C(h)\le\frac25,}
\]
with lower equality **exactly** at \(h=2\cdot5^m\), and upper equality **exactly** at \(h=3\cdot5^m\), for integers \(m\ge0\). In particular \(C(2)=-1/5\), \(C(3)=2/5\), and \(C(4)=1/5\).

For fixed \(h\) and \(\sigma,\tau\in\{-1,1\}\), the limiting density of the sign pair \((\sigma,\tau)\) at positions \(n,n+h\) is
\[
\boxed{\frac{1+\sigma\tau C(h)}4.}
\]
Thus consecutive signs are asymptotically independent and balanced despite the exact positive finite-block same-sign bias, while shifts \(2\cdot5^m\) and \(3\cdot5^m\) are the unique maximally disagreeing and agreeing shifts.

## Assumptions and scope

All indices \(n,h\) are ordinary nonnegative integers, \(r\ge1\) in the exact block count, and the fixed-shift asymptotic holds as real \(N\to\infty\) through positive integers. Multiplication in the character is modulo \(5\), not in a \(5\)-adic square class. The result concerns arithmetic signs of the classical four-color multinomial-square Domb numbers. It does not assert correlations for other primes or the full Domb residues modulo higher powers of five.

## Proof

**1. Multinomial Lucas product.** By splitting four nonnegative summands into two pairs and applying Vandermonde's identity twice,
\[
D_n=\sum_{a+b+c+d=n}\binom{n}{a,b,c,d}^{\!2}.
\]
The multinomial Lucas congruence states that, for each prime \(p\), a multinomial coefficient vanishes modulo \(p\) when its summands add with a base-\(p\) carry and otherwise factors into the multinomials of the corresponding digits. Grouping the four-tuples according to their base-\(p\) digits therefore yields
\[
D_n\equiv\prod_j D_{n_j}\pmod p
\]
for every nonnegative integer \(n=\sum_jn_jp^j\). Directly \((D_0,D_1,D_2,D_3,D_4)=(1,4,28,256,2716)\); their characters modulo five are \((1,1,-1,1,1)\). Consequently
\[
f(n)=(-1)^{\#\{j:n_j=2\}},\qquad f(5m+a)=f(m)w_a,
\]
with \((w_0,w_1,w_2,w_3,w_4)=(1,1,-1,1,1)\). This also proves that \(f(n)\) never vanishes.

**2. Exact finite-block carry recursion.** Define
\[
C_r(h)=5^{-r}\sum_{0\le n<5^r}f(n)f(n+h),\quad r\ge0,
\]
so \(C_0(h)=f(h)\). Separating the units digit of \(n\) and its carry in \(n+h\) shows that \(C_r(5q+a)\) satisfies the five formulas in the Finding, with \(C\) replaced by \(C_r\) on the left and \(C_{r-1}\) on the right. In the order \(a=0,1,2,3,4\), the coefficients of \((C_{r-1}(q),C_{r-1}(q+1))\) before division by five are
\[
(5,0),\quad(0,1),\quad(-1,2),\quad(2,-1),\quad(1,0).
\]
They are simply the sums of the five products \(w_b w_{(b+a)\bmod5}\) separated according to whether \(b+a\ge5\). Because \(C_r(0)=1\) and \(C_r(1)=5^{-r}\), it follows that
\[
C_r(2)=-\tfrac15+2\cdot5^{-r},\quad C_r(3)=\tfrac25-5^{-r},\quad C_r(4)=\tfrac15\quad(r\ge1).
\]
In particular, \(\sum_{n<5^r}f(n)f(n+1)=1\) exactly for every \(r\ge1\).

**3. Existence, recursion, and errors.** For \(h=0\) the limit is constant. For \(h=1\), the preceding formula gives the limit zero and error \(5^{-r}\). For each \(h\ge2\), every shift \(q\) or \(q+1\) occurring in the carry recurrence is strictly smaller than \(h\), unless the coefficient of that term is zero. Strong induction therefore gives the existence of a rational limit \(C(h)\) and a constant \(B_h\) such that \(\lvert C_r(h)-C(h)\rvert\le B_h5^{-r}\) for every \(r\ge0\).

On any aligned block of \(5^r\) consecutive indices, write \(n=b5^r+a\), \(0\le a<5^r\). The product \(f(n)f(n+h)\) agrees with \(f(a)f(a+h)\) whenever \(a+h<5^r\), because the common high digits contribute \(f(b)^2=1\). On at most \(\min(h,5^r)\) remaining indices it can differ by at most two. Hence the block sum equals \(5^r C(h)+O_h(1)\). Every initial interval \([0,N)\) is a disjoint union of at most \(4(1+\lfloor\log_5 N\rfloor)\) aligned base-five blocks. Thus the claimed total error is \(O_h(\log(2N))\).

**4. Sharp bounds and uniqueness.** The initial values are \(C(1)=0\), \(C(2)=-1/5\), \(C(3)=2/5\), \(C(4)=1/5\). Inductively suppose \(-1/5\le C(q),C(q+1)\le2/5\) for \(q\ge1\). The outputs for final digits \(1\) and \(4\) lie in \([-1/25,2/25]\); for final digits \(2\) and \(3\) they lie in \([-4/25,1/5]\). Both are strict subintervals of \([-1/5,2/5]\). Appending a zero digit leaves the correlation unchanged. Thus equality is possible only at the leading digits \(2\) and \(3\), followed by any number of zero digits. This proves the claimed bounds and the exact extremizer families.

**5. Exact sign-pair counts.** The digit product gives \(\sum_{n<5^r}f(n)=3^r\). Since \(f(0)=f(5^r)=1\), the shifted sum \(\sum_{n<5^r}f(n+1)\) also equals \(3^r\). The adjacent product sum equals one by Step 2. Expanding
\[
\mathbf 1_{\{f(n)=\sigma, f(n+1)=\tau\}}=
\frac{(1+\sigma f(n))(1+\tau f(n+1))}{4}
\]
yields the exact four-cell formula. On arbitrary initial intervals the one-point sum is \(O(N^{\log_5 3})\), since each aligned block contributes \(\pm3^r\) and the base-five decomposition contains at most four blocks of a given length. Combining this with Step 3 gives the limiting pair densities.

## Verification

The accompanying `CHECK.py` computes Domb values directly from their defining binomial sum, independently of the digit-character formula, then checks their signs for 210 indices. It also verifies 384 complete-block correlations at depths one through six, 24 exact adjacent sign-pair cells and the lag-one/lag-two/lag-three identities at six depths, and the sharp bounds plus equality cases for the first 100,000 positive shifts. The checker uses only the Python standard library. Command: `python3 CHECK.py`. These finite checks are supplementary; the proof above establishes the infinite statements.

## Relationship to prior work

Osburn and Sahu (2012) develop Domb and generalized-Domb supercongruences, not an all-shift character correlation law. Rowland and Yassawi (2013) give general Lucas-product and automaton methods for combinatorial diagonals, but not the explicit Domb modulo-five pair-frequency identity or sharp all-shift correlation extremizers. Classical automatic-sequence/Thue–Morse correlation techniques motivate the carry method. Their general availability does not by itself calculate these Domb-specific extrema. Closest known electronic-result records concern central trinomial, Franel, and Apéry digit-residue correlations and shifted Domb supercongruences; those statements have different arithmetic sequences or objects and do not imply this Domb-character claim without further analysis.

## Limitations

This result is about the fixed prime five and the two-point quadratic-character sign, rather than squarehood in \(\mathbb Z_5\). The error constant for a fixed shift can depend on that shift. Its rational recursion is an effective specification, not a closed formula with bounded complexity independent of the shift. Historical priority remains uncertain against broad generalized-digit-correlation literature, although targeted primary-source and database comparisons found no explicit dominating theorem. No independent mathematical audit has been performed.

## References

1. R. Osburn and B. Sahu, *A supercongruence for generalized Domb numbers*, arXiv:1201.6195v1 (public 2012-01-30), https://arxiv.org/abs/1201.6195.
2. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635v1 (public 2013-10-31), https://arxiv.org/html/1310.8635v2.
3. M. Baake and U. Grimm, *The singular continuous diffraction measure of the Thue–Morse chain*, J. Phys. A 41 (2008), 422001, https://doi.org/10.1088/1751-8113/41/42/422001.
4. G.-S. Mao and M. J. Schlosser, *Supercongruences involving Domb numbers and binary quadratic forms* (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC10547664/.
