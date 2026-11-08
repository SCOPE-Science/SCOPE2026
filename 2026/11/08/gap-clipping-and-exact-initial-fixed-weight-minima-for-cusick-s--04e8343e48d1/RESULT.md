# Gap clipping and exact initial fixed-weight minima for Cusick's binary digit-sum bias

## Finding
Let \(s_2(n)\) be the sum of binary digits of \(n\ge0\), let
\[
c_t=\operatorname{dens}\{n\ge0:s_2(n+t)\ge s_2(n)\},\qquad
F(k)=\inf_{t\ge1,\ s_2(t)=k}\left(c_t-\frac12\right).
\]
For every \(k\ge1\), the infimum is a minimum. More precisely, for every shift \(t\) of weight \(k\), after deleting its trailing zero bits, write
\[
t=\sum_{i=0}^{k-1}2^{p_i},\quad 0=p_0<p_1<\cdots<p_{k-1},\quad d_i=p_i-p_{i-1}\ (1\le i<k).
\]
Replacing each gap \(d_i\) by \(\min(d_i,k+1)\) leaves \(c_t\) unchanged. Hence it suffices to inspect exactly \((k+1)^{k-1}\) odd shifts and the minimum is attained by an odd shift \(t<2^{k^2}\).

For \(1\le k\le8\), the exact minima and **all** minimizing shifts are as follows. The last column lists odd representatives; every minimizing positive shift is one of these multiplied by a nonnegative power of two.

| \(k\) | \(\min c_t\) | \(F(k)\) | odd minimizing shifts | canonical shifts examined |
|---:|---:|---:|---:|---:|
|1|\(3/4\)|\(1/4\)|1|1|
|2|\(5/8\)|\(1/8\)|5|3|
|3|\(19/32\)|\(3/32\)|11, 13|16|
|4|\(73/128\)|\(9/128\)|27|125|
|5|\(9/16\)|\(1/16\)|107|1296|
|6|\(567/1024\)|\(55/1024\)|219|16807|
|7|\(2239/4096\)|\(191/4096\)|439, 475|262144|
|8|\(8839/16384\)|\(647/16384\)|951|4782969|

## Assumptions and scope
The ambient digits are binary. Densities are natural densities of nonnegative integers and exist for each positive shift. The general gap-clipping theorem holds for *all* positive integers \(k\) without an asymptotic qualification. The exact table is claimed only for \(1\le k\le8\). No exact value is claimed for larger weights. The exact classification of minimizers at these eight weights follows from the same exhaustive enumeration and the fact that every canonical minimizer has all gaps less than \(k+1\).

## Proof
### Carry identity
Let \(\varepsilon_i\in\{0,1\}\) be the binary input digits of \(n\), \(\tau_i\) those of \(t\), and \(\gamma_i\in\{0,1\}\) the outgoing carry from column \(i\), with incoming carry initially zero. The column sum is \(\varepsilon_i+\tau_i+\gamma_{i-1}\), and the output digit is this sum modulo \(2\). Summing the column identities and accounting for the finite carry tail gives
\[
s_2(n+t)-s_2(n)=s_2(t)-C=k-C,
\]
where \(C\) is the total number of outgoing binary carries, including any after the last nonzero bit of \(t\). Thus \(c_t=\mathbb P(C\le k)\) for independent fair input bits; this probability is the natural density because cylinder events have the corresponding dyadic densities and arbitrarily long carry tails have geometrically decaying probability.

### Gap-clipping lemma
Process input bits from least to most significant, retaining only paths with at most \(k\) accumulated carries. Whenever an outgoing carry is one, at least one carry has already been counted. In a zero-bit column of \(t\), an incoming zero carry stays zero; an incoming one carry either dies or continues as an outgoing one, and every step where it continues adds one to the carry count. After \(k\) consecutive zero columns, no surviving path can have an outgoing carry one: such a path would have accumulated at least one earlier carry and \(k\) further carries, exceeding the budget. Additional zero columns then leave the conditional no-carry distribution unchanged (the next input bits are fair). Consequently, any consecutive run of at least \(k\) zero digits *between* nonzero digits may be shortened to exactly \(k\) zeros without changing \(\mathbb P(C\le k)\). A gap of length \(d_i\) contains \(d_i-1\) zeros, proving the clipping rule. Trailing zero bits of \(t\) do not affect the density, since \(c_{2t}=c_t\). The clipped odd shift has largest set-bit position at most \((k-1)(k+1)=k^2-1\), so it is strictly smaller than \(2^{k^2}\). Each of \(k-1\) gaps has exactly \(k+1\) possible clipped lengths, giving \((k+1)^{k-1}\) cases.

### Exact arithmetic for the finite census
For a fixed bit prefix of length \(L\), let \(v_c(j)\) be the integer number of \(L\)-digit inputs producing carry state \(c\in\{0,1\}\) and exactly \(j\) carries, with \(0\le j\le k\). Start with \(v_0(0)=1\) and all other entries zero. For a zero digit of the shift, update simultaneously by
\[
v'_0(j)=2v_0(j)+v_1(j),\qquad v'_1(j+1)=v_1(j).
\]
For a one digit, use
\[
v'_0(j)=v_0(j),\qquad v'_1(j+1)=v_0(j)+2v_1(j).
\]
Entries with index above \(k\) are discarded. These formulas count the two possible input bits for each incoming state. After processing the highest one bit of \(t\), a final zero outgoing carry contributes probability one, while a final one carry with \(j\) previous carries survives with conditional probability \(1-2^{-(k-j+1)}\): the carry dies on the first zero input bit, with a geometric number of additional carries. Therefore the exact density is
\[
c_t=2^{-L}\sum_{j=0}^k\left(v_0(j)+v_1(j)\left(1-2^{-(k-j+1)}\right)\right).
\]
All terms are rational powers of two, so comparison over the finite canonical set uses integer numerators at shared denominator \(2^{k^2+k+1}\). The companion C++17 program `verify_extrema.cpp` enumerates every clipped gap tuple at each weight one through eight, computes its exact common-denominator value, asserts every row of the table, and lists *all* canonical optimizers. Its output is included in `VERIFICATION.md`. The separate Python `reference_check.py` uses `fractions.Fraction` and distinct transition code to exhaust weights one through five, cross-check random gap clipping through eight, and validate explicit binary digit counts.

No clipped optimizing tuple in the table has any gap equal to \(k+1\). Therefore an unbounded original gap (which clips to \(k+1\)) cannot be an optimizer. Together with invariance under leading powers of two, this proves the claimed *complete* set of minimizers.

## Verification
The exact finite census covers \(1+3+16+125+1296+16807+262144+4782969=5063361\) canonical gap patterns. The primary enumerator uses exact 128-bit unsigned integer counts (sufficient for all tested weights) and no floating point. A second implementation reconstructs the carry probability by independently updating rational weighted states, exhaustively checks \(1441\) patterns for weights one through five, runs \(210\) gap-clipping spot checks at larger weights, and directly compares nine finite digit-sum frequencies. Both programs are deterministic, need no external data, and can be rerun from the two included standalone files.

Compile and run `verify_extrema.cpp` using `g++ -O2 -std=c++17 verify_extrema.cpp -o verify_extrema && ./verify_extrema`. Run the independent checker using `python3 reference_check.py`. Finite exact enumeration proves the table *only because* the gap-clipping lemma reduces the originally unbounded optimization to these finite cases. Finite digit-frequency checks alone are not a proof of a natural density or an unrestricted minimization result.

## Relationship to prior work
Kaimin Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899v1 (public 2026-08-26), defined the same fixed-weight extremal problem and proved its sharp large-weight asymptotic. That asymptotic does not identify exact minima or optimizer sets at the first eight weights. Cheng's *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398v1, proves a universal lower bound but not the present exact finite profile. Drmota, Kauers and Spiegelhofer, *On a conjecture of Cusick concerning the sum of digits of \(n\) and \(n+t\)*, arXiv:1509.08623v2, give recurrences to evaluate \(c_t\) for any fixed \(t\) and list individual values including \(c_{11}=c_{13}=19/32\). **No novelty is claimed for those individual rational evaluations, the general carry identity, or fixed-shift recurrences.** The additional results here are the uniform finite gap-clipping reduction, global attainment/cutoff and complete eight-weight extremal classification, whose implications are not furnished by the inspected earlier results.

## Limitations
An equivalent gap-clipping result might have appeared in unindexed earlier literature. The exact table ends at weight eight. No formula for general \(F(k)\) beyond the finite optimization bound, no asymptotic improvement, and no new proof of Cusick's general inequality are asserted. Exact computations use finite word lengths only after the mathematically proved reduction.

## References
1. K. Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899v1 (2026-08-26), https://arxiv.org/abs/2608.25899.
2. K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398v1 (2026-06-22), https://arxiv.org/abs/2606.23398.
3. M. Drmota, M. Kauers and L. Spiegelhofer, *On a conjecture of Cusick concerning the sum of digits of \(n\) and \(n+t\)*, arXiv:1509.08623v2 (2016), https://arxiv.org/pdf/1509.08623.
