# Sharp cyclic quadratic-character correlations of Apéry numbers modulo seven

## Finding

Let the classical Apéry numbers be
\[
A(n)=\sum_{j=0}^{n}\binom nj^{2}\binom{n+j}j^{2}\qquad(n\ge0),
\]
and let \(\chi\) be the quadratic character modulo seven. For each integer \(r\ge1\), write \(N=7^r\), \(s_r(n)=\chi(A(n))\) for \(0\le n<N\), and define the **cyclic finite-block** signed correlation
\[
C_r(h)=\sum_{n=0}^{N-1}s_r(n)s_r((n+h)\bmod N),\qquad h\in\mathbb Z/N\mathbb Z.
\]
The modulo operation in the second index is part of the definition; this is not an unwrapped correlation sum.

**Complete correlation recursion.** With \(C_0(0)=1\), for every \(r\ge1\) and \(h=7q+b\), \(0\le b<7\), \(0\le q<7^{r-1}\),
\[
C_r(7q+b)=\alpha_b C_{r-1}(q)+\beta_bC_{r-1}(q+1),
\]
where the smaller argument is reduced modulo \(7^{r-1}\) and
\[
(\alpha_0,\ldots,\alpha_6)=(7,2,1,0,-1,-2,1),\qquad
(\beta_0,\ldots,\beta_6)=(0,1,-2,-1,0,1,2).
\]
Consequently every finite-block pair correlation is determined exactly by a two-branch integer recurrence, without a limiting operation.

**Sharp global extrema.** For every \(r\ge2\), among all nonzero shifts modulo \(N=7^r\),
\[
\boxed{\max_{1\le h<N}C_r(h)=3\cdot7^{r-1},\quad
 C_r(h)=3\cdot7^{r-1}\ \Longleftrightarrow\ h\equiv\pm7^{r-1}\pmod N,}
\]
and
\[
\boxed{\min_{1\le h<N}C_r(h)=-\frac{5\cdot7^{r-1}-2}{3},\quad
 C_r(h)=-\frac{5\cdot7^{r-1}-2}{3}\ \Longleftrightarrow\ h\equiv\pm5\pmod N.}
\]
At \(r=1\), \(C_1=(7,3,-1,-1,-1,-1,3)\); the maximal nonzero shifts are \(1,6\), and the minimal shifts are \(2,3,4,5\). For all \(r\ge1\), \(C_r(0)=7^r\) and \(C_r(1)=C_r(-1)=(7^r+2)/3\).

**Entire ordered sign-pair statistics.** The signs never vanish, and their one-point sum on the block is \(S_r=(-3)^r\). For \(\sigma,\tau\in\{-1,1\}\), the exact number of indices \(n\bmod N\) with \((s_r(n),s_r(n+h))=(\sigma,\tau)\) is
\[
\boxed{\frac{N+(\sigma+\tau)(-3)^r+\sigma\tau C_r(h)}4.}
\]
Thus the recurrence supplies every two-point character fiber, not only extrema.

## Assumptions and scope

All indices \(n\) are nonnegative integers, and \(r\) is a positive integer. The character is \(\chi(a)=0\) for \(7\mid a\), \(\chi(a)=1\) for square units \(a\equiv1,2,4\pmod7\), and \(-1\) otherwise. Because no Apéry number is divisible by seven, only \(\pm1\) occur. The domain of the correlation is the additive cyclic group \(\mathbb Z/7^r\mathbb Z\); no assertion here identifies the cyclicly wrapped values with \(s(n+h)\) at nonwrapped integer indices beyond the block.

## Proof

**1. Apéry's base-seven digit factorization.** For \(n=7m+d\) and \(0\le d<7\), write each summation index \(j=7k+e\), \(0\le e<7\). Lucas's binomial congruence gives \(\binom{7m+d}{7k+e}\equiv\binom mk\binom de\pmod7\), with zero contribution when \(e>d\). If \(e\le d\) but \(d+e\ge7\), the other factor \(\binom{7m+d+7k+e}{7k+e}\) vanishes modulo seven because its units digit is \(d+e-7<e\). If \(d+e<7\), Lucas's congruence gives \(\binom{m+k}k\binom{d+e}e\). Thus the binomial sum separates:
\[
A(7m+d)\equiv A(m)A(d)\pmod7.
\]
Direct exact evaluation for \(d=0,\dots,6\) gives
\[
(A(0),\ldots,A(6))\equiv(1,5,3,3,3,5,1)\pmod7.
\]
Iterating proves that every \(A(n)\) is a unit modulo seven and, if \(n=\sum_i d_i7^i\), then
\[
\chi(A(n))=\prod_i w_{d_i},\qquad w=(1,-1,-1,-1,-1,-1,1).
\]
Since \(\sum_{d=0}^6 w_d=-3\), summation independently over the \(r\) digits gives \(S_r=(-3)^r\).

**2. Exact carry recurrence.** Write \(n=7m+d\) and \(h=7q+b\) with \(d,b\in\{0,\ldots,6\}\). The new low digit is \((d+b)\bmod7\), and the carry into the high block is \(\lfloor(d+b)/7\rfloor\). Consequently
\[
C_r(7q+b)=\sum_{d+b<7}w_dw_{d+b}\,C_{r-1}(q)
+\sum_{d+b\ge7}w_dw_{d+b-7}\,C_{r-1}(q+1).
\]
The identity also holds across the top-block wrap because all high indices are reduced modulo \(7^{r-1}\). Evaluating these seven short finite sums yields precisely the displayed \(\alpha,\beta\) vectors. The base case \(C_0(0)=1\) yields \(C_1=(7,3,-1,-1,-1,-1,3)\). For \(h=1\) the recurrence gives \(C_r(1)=2\cdot7^{r-1}+C_{r-1}(1)\); solving from \(C_0(0)=1\) proves \(C_r(1)=(7^r+2)/3\). Symmetry \(C_r(-h)=C_r(h)\) follows by a cyclic change of summation variable.

**3. Global extrema with equality cases.** Induct on \(r\). At \(r=1\), every nonzero correlation has absolute value at most three, and the four negative minimizers are as stated. Fix \(r\ge2\), put \(L=7^{r-1}\), and suppose the preceding depth satisfies \(\lvert C_{r-1}(q)\rvert\le3\cdot7^{r-2}\) for all nonzero \(q\), together with its sharp lower bound. For a nonzero shift divisible by seven, \(h=7q\) with \(q\ne0\), the recurrence is \(C_r(h)=7C_{r-1}(q)\). It is at most \(3L\) and is strictly greater than \(-(5L-2)/3\), since the preceding lower bound gives
\[
C_r(h)\ge-\frac{5L-14}{3}>-\frac{5L-2}{3}.
\]
Equality at the positive maximum in this divisible case occurs precisely when \(q\equiv\pm7^{r-2}\pmod L\), by induction.

Now take \(h=7q+b\) with \(1\le b\le6\). If \(1\le q\le L-2\), then both \(q\) and \(q+1\) are nonzero modulo \(L\). Every row satisfies \(\lvert\alpha_b\rvert+\lvert\beta_b\rvert\le3\) for \(b>0\), so
\[
\lvert C_r(h)\rvert\le9\cdot7^{r-2}<\frac{5L-2}{3}<3L.
\]
For the remaining boundary cases, set \(c=C_{r-1}(1)=(L+2)/3\). When \(q=0\) and \(b=1,\ldots,6\), the values are, respectively,
\[
2L+c,\ L-2c,\ -c,\ -L,\ -2L+c,\ L+2c.
\]
When \(q=L-1\) and \(b=1,\ldots,6\), they are
\[
2c+L,\ c-2L,\ -L,\ -c,\ -2c+L,\ c+2L.
\]
Since \(L\ge7\), every boundary value is strictly less than \(3L\) and at least \(-(5L-2)/3\), with the latter equality only at \((q,b)=(0,5)\) or \((L-1,2)\). These correspond to \(h=5\) and \(h=7^r-5\). This proves both sharp bounds and their complete equality cases; the new bounds imply the absolute-value induction hypothesis at the next depth.

**4. Pair counts.** Write \(N_{\sigma\tau}\) for the four ordered sign counts at lag \(h\). Cyclic shift preserves the two marginal sign sums, so \(\sum s_r(n)=\sum s_r(n+h)=S_r\). Together with \(\sum s_r(n)s_r(n+h)=C_r(h)\) and total count \(N\), inversion of the four sign equations gives
\[
N_{\sigma\tau}=\bigl(N+(\sigma+\tau)S_r+\sigma\tau C_r(h)\bigr)/4.
\]
All claims follow.

## Verification

The standalone file `CHECK.py` implements the original integer binomial sum, the base-seven sign word, the independent direct cyclic correlation sum, and the exact recurrence. Running `python3 CHECK.py` succeeds with `PASS: 3098 independent exact assertions; cyclic depths 1..6`. It compares original Apéry values at indices \(0\) through \(100\), direct cyclic correlations for complete blocks through depth four, all claimed extrema and equality sets through depth six, and the exact pair-count identities. These finite checks do not substitute for the induction in the preceding section.

## Relationship to prior work

Gessel's classical Lucas congruence for Apéry numbers (1982), restated and applied to the specific seven-digit vector by Malik and Straub (2015, especially their Example 6.1), supplies the digital starting point, but not cyclic correlations. Fan and Konieczny (2018) establish broad uniformity and existence/estimates of unwrapped correlations for multiplicative digit sequences; these results do not determine the finite cyclic maxima, minima or equality shifts at each depth. Related digit-carry correlation classifications for other arithmetic sequences use analogous general techniques but have different local sign vectors and do not imply the displayed seven-adic Apéry extremizers. The novelty claimed here is strictly the exact finite cyclic two-point and sharp all-shift classification for this Apéry sign sequence, not the earlier digit congruence or the general carry method.

## Limitations

This result concerns only quadratic characters of classical Apéry values modulo seven, not the full distribution of all six nonzero value classes, or congruences modulo \(7^2\). It also does not prove a theorem about arbitrary unwrapped index windows, nor an arithmetic limit theorem for all growing shifts outside the specified finite cyclic blocks. Historical priority against every implicit specialization of general digit-correlation results cannot be established by searches alone. No independent mathematical audit has been performed.

## References

- I. Gessel, *Some congruences for Apéry numbers*, Journal of Number Theory **14** (1982), 362–368, https://doi.org/10.1016/0022-314X(82)90071-3.
- A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297, first submitted 3 August 2015, https://arxiv.org/abs/1508.00297. Especially the Lucas congruence and Example 6.1.
- A. Fan and J. Konieczny, *On uniformity of q-multiplicative sequences*, arXiv:1806.04267, 2018, https://arxiv.org/abs/1806.04267. Especially the discussion of digit products and unwrapped correlation coefficients.
- OEIS A005259, *Apéry numbers*, https://oeis.org/A005259; numerical sequence reference, not a source of the new all-shift theorem.
