# Sharp Gini contraction of uniform boxcar averages on prime cycles

## Finding

For every odd prime \(p\ge5\) and every integer \(1\le m\le p-1\), define the width-\(m\) cyclic boxcar operator
\[
(B_{p,m} f)_i=\frac1m\sum_{j=0}^{m-1}f_{i+j}, \qquad i\in \mathbb Z/p\mathbb Z.
\]
For real input signals define the complete-pair Gini seminorm
\[
G_p(f)=\sum_{0\le i<j<p}|f_i-f_j|.
\]
Put \(d=\min\{m,p-m\}\) and \(Q=\lfloor p^2/4\rfloor=(p^2-1)/4\). Then the exact induced seminorm is
\[
\boxed{\|B_{p,m}\|_G=\frac{d}{m}\left(1-\frac{d^2-1}{3Q}\right).}
\]
The bound is attained by any indicator of a cyclic arc of length \((p-1)/2\), and its complements. In particular, for \(2\le m\le(p-1)/2\), the sharp contraction deficit is \(4(m^2-1)/(3(p^2-1))\). For widths exceeding half the cycle, the exact norm is obtained by the complementary-window factor \((p-m)/m\).

## Assumptions and scope

The cycle has odd prime cardinality, the averaging weights are equal and nonnegative, indexing is periodic, and the input is a real vector modulo additive constants. The norm refers to **one** boxcar-averaging step, not to the Lipschitz norm of differences between two nonlinear filters. No extension to composite cycle cardinalities or to nonuniform weights is claimed. Indicators of balanced arcs give norm-attaining witnesses; uniqueness is not claimed.

## Proof

**1. Coarea reduction.** Because \(B_{p,m}\) is positive and linear, for any real \(f\) subtract its minimum and write it as an integral of upper-level indicators. Then the triangle inequality gives
\[
G_p(B_{p,m} f)\le\int G_p(B_{p,m}\mathbf1_{S_t})\,dt,
\quad G_p(f)=\int |S_t|(p-|S_t|)\,dt.
\]
Consequently the seminorm equals the maximum of the ratios over nonempty proper binary cuts \(S\). The reverse inequality is immediate because binary indicators are permitted inputs.

**2. Rearrangement.** With \(I_m\) the cyclic interval of \(m\) points, the unnormalized output of a cut is the cyclic convolution \(h_S=\mathbf1_S*\mathbf1_{I_m}\), up to a reflection/translation of indices. Lev's set-rearrangement majorization theorem on prime cyclic groups says that convolution of two set indicators is majorized by the convolution of two consecutively supported rearranged indicators; its parity conventions permit opposite choices for two even supports. Hence \(h_S\prec h_{A_k}\), where \(A_k\) is some arc of length \(k=|S|\). The Gini functional \(G_p\) is symmetric and convex, hence Schur-convex, so \(G_p(h_S)\le G_p(h_{A_k})\). The ratio denominator depends only on \(k\). This invokes the cited prime-cyclic rearrangement theorem, not an unproved assertion about composite groups.

**3. Exact overlap profile.** First suppose \(m\le (p-1)/2\). By complementing \(S\), which reverses the output about a constant, take \(1\le k\le(p-1)/2\). Set \(a=\min\{m,k\}\), \(b=\max\{m,k\}\). As \(m+k\le p-1\), the arc-window intersection counts have no cyclic double wrapping. If \(c_t\) denotes the number of output positions for which \(h_{A_k}\ge t\), then for \(1\le t\le a\)
\[
c_t=m+k-2t+1,
\quad \sum_{t=1}^{a}c_t=mk,
\quad \sum_{t=1}^{a}c_t^2=ab^2+\frac{a(a^2-1)}3.
\]
The integer layer-cake identity for pairwise absolute differences is
\[
G_p(h_{A_k})=\sum_{t=1}^{a}c_t(p-c_t)
=p m k-ab^2-\frac{a(a^2-1)}3.
\]
Division by \(m\,k(p-k)\) yields
\[
R_{m,k}=\frac{G_p(B_{p,m}\mathbf1_{A_k})}{k(p-k)}=
\begin{cases}
\dfrac{m(p-m)-(k^2-1)/3}{m(p-k)},& k\le m,\\[5pt]
1-\dfrac{m^2-1}{3k(p-k)},&m\le k\le(p-1)/2.
\end{cases}
\]
Both pieces agree at \(k=m\). For \(k\le m\), differentiating the real interpolation shows that the derivative has the sign of \(3m(p-m)+k^2-2pk+1\); this quantity is decreasing on the interval and at \(k=m\) equals \(m(p-2m)+1>0\). For \(m\le k\le(p-1)/2\), the product \(k(p-k)\) is increasing, and so is \(R_{m,k}\). Thus the maximum occurs at the balanced size \(k=(p-1)/2\), where \(k\ge m\), giving \(1-(m^2-1)/(3Q)\).

**4. Complementary windows.** If \(m>(p-1)/2\), let \(d=p-m\). For every input, the sum of the \(m\) included consecutive entries is the total input sum minus the sum of the \(d\) omitted consecutive entries. Consequently the output is a constant minus \((d/m)\) times a shifted width-\(d\) output. Since \(G_p\) ignores constants, signs, and cyclic output shifts,
\[
G_p(B_{p,m}f)=\frac dm G_p(B_{p,d}f).
\]
This identity transfers the sharp norm and the balanced-arc equality witness from width \(d\). The cases \(m=1\) and \(m=p-1\) are included.

## Verification

The accompanying standalone Python checker uses exact rational arithmetic. It exhaustively evaluates every nontrivial binary cut for every width on prime cycles of sizes \(3,5,7,11,13\) (119,628 cut/window cases), checks 6,240 additional multilevel rational signals across five larger prime sizes, and checks balanced-arc witnesses and their finite formula through prime size \(41\). These finite checks corroborate, but do not replace, the all-prime proof above. Run with `python3 checker.py`.

## Relationship to prior work

The decisive non-elementary ingredient is the *known* prime-cyclic set-convolution majorization theorem of Lev, as carefully stated in Madiman, Wang and Woo, Lemma 6.3. Its conclusion is an ordering of convolution profiles, not the present sharp complete-pair Gini **operator seminorm**, closed width-dependent formula, or maximizing cut-size optimization. Gaubert and Qu study the Hopf oscillation/Dobrushin coefficient and its dual total-variation norm, which are different seminorms. Earlier exact cyclic two-tap and three-point Gini formulas are the low-width specializations; they do not imply the classification for every width. No assertion of historical uniqueness is made.

## Limitations

The prime-order restriction is used at the cited rearrangement step. Experiments for some composite orders are not a proof of any composite-order statement. Equality is established for balanced arcs, not classified among all real inputs. The result does not address arbitrary convolution kernels, multiple steps, nonlinear averaging, or weighted pairwise dispersion.

## References

1. V. F. Lev, “Linear equations over \(\mathbb F_p\) and moments of exponential sums,” *Duke Mathematical Journal* 107 (2001), 239–263, DOI:10.1215/S0012-7094-01-10722-9. An original prime-group rearrangement result; original full text was not accessible during this review.
2. M. Madiman, L. Wang, J. O. Woo, “Entropy Inequalities for Sums in Prime Cyclic Groups,” arXiv:1710.00812, especially Lemma 6.3 (HTML version 4); independently accessible full statement and discussion of Lev's theorem. https://arxiv.org/html/1710.00812v4
3. S. Gaubert, Z. Qu, “Dobrushin's ergodicity coefficient for Markov operators on cones,” arXiv:1307.4649, originally publicly submitted 17 July 2013; §§1–2 describe oscillation and dual total variation. https://arxiv.org/abs/1307.4649
