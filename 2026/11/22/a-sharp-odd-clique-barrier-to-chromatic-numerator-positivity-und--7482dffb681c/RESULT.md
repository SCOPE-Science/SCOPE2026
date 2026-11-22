# A sharp odd-clique barrier to chromatic-numerator positivity under signed-tree attachment

## Finding

Let \(n\ge3\) be odd. Form a connected signed graph \(\Sigma_{n,r}\) by starting with the complete graph on \(n\) vertices, signing every clique edge negative, and adjoining \(r\ge0\) new vertices by \(r\) edges, all of which are bridges; the new edge signs are arbitrary. Equivalently, rooted trees may be attached to any clique vertices, with no cycles outside the clique. For \(N=n+r\), let \(Z_{n,r}(q)\) be the zero-free signed chromatic polynomial and define \(H_{n,r}(t)\) by

\[
\sum_{m\ge1}Z_{n,r}(m-1)t^m=\frac{H_{n,r}(t)}{(1-t)^{N+1}}.
\]

**Theorem.** The polynomial \(H_{n,r}(t)\) is coefficientwise nonnegative **if and only if**

\[
\boxed{n\in\{3,5\}\quad\text{and}\quad r\ge1.}
\]

In particular, for every odd \(n\ge7\), no finite number of signed-tree attachments can restore numerator positivity, even though each new edge is a balanced block. The obstruction is witnessed by the fourth coefficient for every \(r\ge1\):

\[
[t^4]H_{n,r}(t)=2^r Z_{n,0}(3)-2(n+r+1)<0.
\]

The boundary is sharp: with one new vertex,

\[
H_{3,1}(t)=2t^3+8t^4+14t^5,
\qquad
H_{5,1}(t)=2t^3+22t^4+162t^5+82t^6+452t^7.
\]

This is a classification only for **odd** all-negative clique cores with bridge-only attachments. No statement is made about even clique orders or arbitrary signed graphs.

## Assumptions and scope

An edge \(uv\) of sign \(\sigma\in\{+1,-1\}\) forbids a zero-free coloring \(c\) with \(c(u)=\sigma c(v)\). At every even positive integer \(q=2k\), the available colors are \(\{\pm1,\ldots,\pm k\}\). The unique polynomial agreeing with the resulting counts is \(Z(q)\). The characteristic polynomial convention is \(\chi(q)=Z(q-1)\), and \(H(t)\) is defined by the displayed rational series. A balanced block is a block whose signed cycles are all positive; every bridge is balanced.

The permitted trees may be of any shape, may attach at different clique vertices, and may have arbitrary edge signs. Each added edge must remain a bridge of the full graph. The integers \(n,r\) range over every odd \(n\ge3\) and every \(r\ge0\).

## Proof

**1. The exact signed-clique polynomial.** Let \(E_n(q)=Z_{n,0}(q)\). For a proper zero-free coloring of the all-negative clique, vertices with the same color form blocks of a set partition. Distinct blocks must receive distinct colors, none opposite to another. Choosing colors for \(j\) blocks therefore contributes \(\prod_{i=0}^{j-1}(q-2i)\); summing over set partitions gives

\[
E_n(q)=\sum_{j=1}^n\left\{\begin{matrix}n\\j\end{matrix}\right\}\prod_{i=0}^{j-1}(q-2i).
\tag{1}
\]

In particular, \(E_n(0)=0\) and \(E_n(2)=2\). Each bridge attaches a vertex with \(q-1\) available colors once its old endpoint is assigned a color, regardless of edge sign. Equivalently, signed block multiplication gives

\[
Z_{n,r}(q)=(q-1)^r E_n(q).
\tag{2}
\]

**2. The first diagnostic coefficients.** Write \(H_{n,r}(t)=\sum_i h_i t^i\). For \(r=0\), expansion of the denominator gives

\[
h_3=E_n(2)-(n+1)E_n(1)=2-(n+1)E_n(1).
\tag{3}
\]

For \(r\ge1\), the first two coefficients vanish, and the next relevant coefficient is

\[
h_4=2^r E_n(3)-(n+r+1)E_n(2)
=2^r E_n(3)-2(n+r+1).
\tag{4}
\]

**3. An exact exponential generating function and its signs.** For every positive integer \(k\), a color magnitude can be unused or assigned to one nonempty vertex subset with one of two signs. The exponential formula yields

\[
\sum_{n\ge0}E_n(2k)\frac{z^n}{n!}=(2e^z-1)^k.
\]

For each fixed coefficient of \(z\), the two sides are polynomials in \(2k\), so equality at all even nonnegative integers establishes the formal identity

\[
\sum_{n\ge0}E_n(q)\frac{z^n}{n!}=(2e^z-1)^{q/2}.
\tag{5}
\]

For \(q=1\), expand locally and absolutely near \(z=0\):

\[
E_n(1)=2^{1/2}\sum_{j\ge0}b_j(1/2-j)^n,
\quad b_j=(-1)^j\binom{1/2}{j}2^{-j}.
\]

Here \(b_0=1\) and \(b_j<0\) for every \(j\ge1\). For odd \(n\), the bases \(1/2-j\) are negative whenever \(j\ge1\), so **every summand is positive**. Thus \(E_n(1)>0\). Since it is an integer, (3) is strictly negative for every odd \(n\ge3\). No unattached core has nonnegative \(H\).

For \(q=3\), similarly put \(a_j=(-1)^j\binom{3/2}{j}2^{-j}\), giving

\[
E_n(3)=2^{3/2}\sum_{j\ge0}a_j(3/2-j)^n.
\tag{6}
\]

Here \(a_0=1\), \(a_1=-3/4\), and \(a_j>0\) for every \(j\ge2\). For odd \(n\), every summand except \(j=0\) is negative. The eight-term finite certificate needed for an **infinite** sign conclusion is

\[
\sum_{j=3}^{8}a_j\left(\frac{2j-3}{3}\right)^7
=\frac{731229629}{679477248}>1.
\tag{7}
\]

For each \(j\ge3\), the ratio \((2j-3)/3\) is at least one, so the sum on the left with exponent \(n\) remains greater than one whenever \(n\ge7\). Discarding all the other negative terms in (6) therefore proves \(E_n(3)<0\) for every odd \(n\ge7\). Equation (4) proves the claimed persistent fourth-coefficient obstruction.

**4. The two surviving clique orders.** Evaluation of (1), followed by the numerator transformation, gives exactly the two displayed polynomials \(H_{3,1}\) and \(H_{5,1}\), both nonnegative. To extend this to every \(r\ge1\), let \(H(t)/(1-t)^{N+1}\) be the series for any already-attached graph. A further bridge multiplies its shifted chromatic polynomial \(\chi(m)\) by \(m-2\). Its new numerator therefore satisfies

\[
\widetilde H(t)=t(1-t)H'(t)+((N+3)t-2)H(t).
\tag{8}
\]

If \(H(t)=\sum_i h_i t^i\), then

\[
[t^i]\widetilde H(t)=(i-2)h_i+(N+4-i)h_{i-1}.
\tag{9}
\]

Because \(h_1=0\), all coefficients in (9) are nonnegative when the old coefficients are nonnegative: for \(2\le i\le N+2\), both scalar multipliers are nonnegative, and the coefficient at \(i=1\) is zero. Thus positivity survives every further bridge. Together with steps 2–3, this proves the if-and-only-if theorem. \(\square\)

## Verification

Run `python3 verify.py` using the Python standard library. The program builds the signed-clique polynomial using exact Stirling-number arithmetic, checks signed color assignments directly for small even palettes, computes all numerator coefficients from finite differences, verifies the exact rational certificate (7), and replays bridge recurrences and the negative fourth coefficient on a finite sample. The infinite statements rest on the displayed proof, **not** on extrapolation from that sample.

The following are exact outputs of the checker:

```
DIRECT_SIGNED_COLOR_COUNTS n=3,4,5 q=2,4,6 PASS
LOW_ODD_CASES_AND_BRIDGE_RECURRENCE r=1..16 PASS
RATIONAL_EGF_SIGN_CERTIFICATE 731229629/679477248 PASS
ODD_SIGN_AND_NUMERATOR_CHECKS n=7..31 r=0..5 PASS
NO_BRIDGE_BASE_CASES PASS
VERIFY_OK
```

## Relationship to prior work

Higashitani, Kamata and Konoike (2026, Theorem 1.1) establish a positivity equivalence when a balancing vertex exists; their Example 4.3 gives an all-negative four-clique with one balanced pendant bridge and a nonnegative numerator, despite non-realizability as an ordinary chromatic polynomial. That example **does not** give the odd-clique sign classification or show that balanced-tree attachments can fail permanently. The present theorem isolates the first persistent odd-order obstruction at clique order seven and proves that no number or shape of bridge-only attachments can eliminate it. The positive five-clique case is likewise not part of their examples.

The signed-clique chromatic polynomial (1) was already known from Zaslavsky, and is also covered by Greaves, Syatriadi and Utomo (2024, Proposition 3.1). Its enumeration is **not** claimed as new. The new claim is precisely the all-odd-orders sign classification for the numerator after arbitrary bridge-only attachments, including the infinite sign certificate and the permanence of positivity under further tree attachments.

## Limitations

The theorem does not classify even clique orders, attachments containing nonbridge edges, arbitrary signs on the core, or whether every positive-numerator example is a chromatic polynomial of an unsigned graph. It establishes coefficientwise positivity, not real-rootedness. The exact rational inequality in step 3 is finite but proves a uniform infinite sign statement because all selected bases are at least one. Historical priority is based on the identified sources and searched records; an unindexed equivalent result is still possible. No independent mathematical audit has been performed.

## References

1. A. Higashitani, G. Kamata, M. Konoike, *Chromatic polynomials of signed graphs with a balancing vertex*, arXiv:2611.16458, first posted 2026-11-12, https://arxiv.org/abs/2611.16458 . In particular Theorem 1.1, Lemma 2.1 and Example 4.3.
2. G. R. W. Greaves, J. Syatriadi, C. I. Utomo, *Chromatic polynomials of signed graphs and dominating-vertex deletion formulae*, arXiv:2407.00883, first posted 2024-07-01, https://arxiv.org/abs/2407.00883 . In particular Proposition 3.1 and its attribution of the signed-clique formula.
3. T. Zaslavsky, *Chromatic invariants of signed graphs*, Discrete Mathematics 42 (1982), 287–312. The signed-clique formula is cited through reference 2; full text was not independently examined.
