# Sharp zero-free phase boundary for real three-term weighted Bergman jets

## Finding

Let \(\alpha>-1\) be real, put \(h=\alpha+2\), and consider the weighted upper-half-plane Bergman space \(A^2_\alpha(\mathbb H)\), where \(\mathbb H=\{z:\operatorname{Im}z>0\}\). For arbitrary **real** coefficients \(a,b\), define the differential evaluation functional
\[
\Lambda_z f=f(z)+a f'(z)+b f''(z)
\]
and denote by \(B_{\alpha,a,b}(z,w)\) the canonical Hermitian Gram kernel of its Riesz representatives. Set
\[
Q_h=\sqrt{\frac{(h+2)(h+3)}{h(h+1)}}>1.
\]

**Theorem (sharp real-jet zero-free phase).** For every \(\alpha>-1\) and every \((a,b)\in\mathbb R^2\),
\[
\boxed{\ B_{\alpha,a,b}(z,w)\ne0\quad\text{for all }z,w\in\mathbb H
\ \Longleftrightarrow\ a^2\ge 2b+2Q_h|b|.\ }
\]
If the inequality fails, the kernel has **exactly two distinct attainable scalar zeros** in the variable \(t=z-\overline w\), both simple; if equality holds with \(b\ne0\), its two real boundary zeros are double and it has no interior zeros. For \(b=0\), the kernel is zero-free for all \(a\). The complete zero-free region for \(b>0\) is \(a^2/b\ge 2+2Q_h\), whereas for \(b<0\) it is \(a^2/|b|\ge 2Q_h-2\). In particular, adding the first-derivative term can restore zero-freeness to the otherwise non-zero-free value-plus-second-derivative functional.

## Assumptions and scope

The weighted Bergman norm is
\[
\|f\|_\alpha^2=\int_{\mathbb H}|f(x+iy)|^2y^\alpha\,dx\,dy.
\]
Derivative evaluation at every interior point is bounded. The Gram kernel is defined by applying \(\Lambda_z\) holomorphically and its coefficient-conjugated counterpart to the second variable of the classical reproducing kernel. Since \(a,b\) are real, no distinction arises between the coefficients and their complex conjugates. This is the canonical kernel associated with the finite differential sequence \(\xi=(1,a,2b,0,\ldots)\) in the normalization \(\sum_n\xi_n f^{(n)}(z)/n!\).

A *scalar zero* means a value of \(t=z-\overline w\) for which the kernel vanishes for some \(z,w\in\mathbb H\). It does not mean a single isolated pair in the two-variable domain. As \((z,w)\) vary over \(\mathbb H^2\), the scalar variable \(t\) ranges over the whole open upper half-plane; it is never zero. The theorem covers the full real two-parameter family and all \(\alpha>-1\), not arbitrary complex \(a,b\).

## Proof

**1. Kernel normalization and derivative formula.** The standard weighted Bergman reproducing kernel in this normalization is
\[
K_\alpha(z,w)=\frac{2^\alpha(\alpha+1)}{\pi}[-i(z-\overline w)]^{-h},\qquad h=\alpha+2>1.
\]
Here the complex power is defined using the principal logarithm of the right-half-plane quantity \(-i(z-\overline w)\). One direct verification uses the absolutely convergent Fourier–Laplace integral
\[
K_\alpha(z,w)=\frac{2^\alpha}{\pi\Gamma(\alpha+1)}\int_0^\infty s^{\alpha+1}e^{is(z-\overline w)}\,ds.
\]
Writing \(t=z-\overline w\), differentiation yields, for all nonnegative integers \(r,s\),
\[
\frac{\partial_z^r\partial_{\overline w}^{s}K_\alpha(z,w)}{K_\alpha(z,w)}
=(-1)^r(h)_{r+s}t^{-(r+s)},
\qquad (h)_j=h(h+1)\cdots(h+j-1).
\]

**2. Exact quartic numerator.** Apply the differential functional in the first variable and its conjugate in the second. The coefficients of \(t^{-1}\) and \(t^{-3}\) cancel in pairs because the same real coefficients occur on both sides. The result is
\[
\frac{B_{\alpha,a,b}(z,w)}{K_\alpha(z,w)}
=1+(h)_2(2b-a^2)t^{-2}+(h)_4b^2t^{-4}
=\frac{P(t)}{t^4},
\]
where
\[
P(t)=t^4+(h)_2(2b-a^2)t^2+(h)_4b^2.
\]
Both \(K_\alpha\) and \(t^{-4}\) are nonzero on \(\mathbb H^2\), so the kernel zeros are exactly the roots of \(P\) in \(\operatorname{Im}t>0\).

**3. Exact half-plane stability.** If \(b=0\), then \(P(t)=t^2[t^2-(h)_2a^2]\), and all roots are real; thus the Gram kernel is zero-free. Suppose \(b\ne0\). Write \(d=(h)_2>0\), \(D=(h)_4>0\), \(C=d(2b-a^2)\), and \(E=Db^2>0\). Then \(P(t)=t^4+Ct^2+E\). Since
\[
\sqrt D/d=Q_h>1,
\]
we have \(C<2\sqrt E\) for all \(a,b\): for \(b\le0\) it is immediate, and for \(b>0\), \(C\le2db<2\sqrt D b\).

The quadratic in \(u=t^2\) is \(u^2+Cu+E=0\). If \(C\le-2\sqrt E\), its two roots are **positive real**, allowing equality and a repeated positive root; the corresponding \(t\)-roots are exclusively real, hence inaccessible from \(\mathbb H^2\). Conversely, if \(C>-2\sqrt E\), the strict upper bound \(C<2\sqrt E\) makes the quadratic discriminant \(C^2-4E\) negative. Its two roots are distinct nonreal conjugates, each with exactly one square root in the open upper half-plane. Consequently exactly two distinct simple scalar zeros occur. The zero-free inequality \(C\le-2\sqrt E\) is precisely
\[
(h)_2(2b-a^2)\le-2\sqrt{(h)_4}\,|b|
\quad\Longleftrightarrow\quad
 a^2\ge 2b+2Q_h|b|.
\]
At the equality boundary with \(b\ne0\), \(P(t)=(t^2-\sqrt E)^2\), with two double real roots and no interior zeros.

**4. Realizability and sharpness.** Every \(t=x+iy\) with \(y>0\) equals \(z-\overline w\) upon taking \(z=x/2+iy/2\) and \(w=-x/2+iy/2\), both in \(\mathbb H\). Thus both off-boundary roots found in Step 3 actually occur as Gram-kernel zeros; no additional accessibility restriction changes their count. The strict inequality changes the count from two to zero, so the stated threshold is sharp.

**5. Sign asymmetry and weight limit.** The two signs of \(b\) yield the displayed positive- and negative-curvature thresholds. As \(h\to\infty\),
\[
Q_h=1+\frac2h+O(h^{-2}),
\]
so the threshold for \(b>0\) tends to \(a^2/b=4\), while that for \(b<0\) tends to \(a^2/|b|=0\), with leading rate \(4/h\). In the classical unweighted space \(h=2\), the exact coefficient is \(Q_2=\sqrt{10/3}\).

## Verification

The standalone standard-library script `CHECK.py` reproduces the quartic coefficients by summing all nine derivative pairs and checks roots and stability on a finite parameter grid across six weights, six nonzero second-derivative coefficients, and seven positions relative to the exact threshold, along with degenerate \(b=0\) cases and independent direct complex derivative evaluations. Running `python CHECK.py` prints `PASS 414 parameter or derivative-consistency configurations`. The script checks finite arithmetic consistency and is **not** used as a proof of the assertion for all weights and parameters; the proof is Steps 1–4. The script and this text use the same coefficient convention \(\Lambda f=f+af'+bf''\).

## Relationship to prior work

Gehlawat, Jain and Sarkar [1] introduced the canonical Gram kernel of differential evaluations and gave general derivative formulas on the unweighted half-plane (notably Theorem 4.1 and formula (4.6)), together with zero-free examples for pure jets and a factorial sequence (Theorem 4.11). The general formula is a prerequisite, but neither their explicit examples nor their zero-free theorem states the sharp real three-term stability region derived here.

A published **first-jet** classification [2] concerns the differential sequence supported on orders \(\{0,1\}\). A published **separated two-jet** classification [3] concerns only support \(\{p,q\}\), with \(q-p\ge2\), and shows that every such mixed kernel has zeros. These source statements give complementary boundary cases; neither contains the simultaneous three-term jet \(\{0,1,2\}\), which permits the newly identified zero-free phase. The structural point is that *adding* the order-one coefficient can eliminate the zeros of the order-zero/order-two kernel, with a sharp sign-dependent threshold.

## Limitations

The coefficient classification assumes **real** \(a,b\); arbitrary complex triples and higher-order differential sequences are not classified. The theorem does not assert zero-freeness for the distinct non-Hermitian off-diagonal extremal kernel. The two-zero statement counts distinct attainable scalar values of \(z-\overline w\), not isolated pairs of points; the boundary double roots occur only at limiting boundary configurations. Historical literature under alternate terms such as differential Gram stability, polynomial Hurwitz stability or jet-weighted Bergman kernels may contain an equivalent formulation. No independent scientific audit or publication-priority determination has occurred.

## References

[1] S. Gehlawat, A. Jain and A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the ξ-Bergman Kernel*, first publicly posted August 13, 2026, arXiv:2608.13193, https://arxiv.org/abs/2608.13193 (full text inspected, especially Section 4).

[2] *Exact two-jet Lu Qi-Keng phase for the canonical ξ-Bergman Gram kernel*, published mathematical record (October 11, 2026), public-result identifier `364c00673845` (full theorem and proof inspected).

[3] *Parity law for zeros of separated weighted Bergman jet Gram kernels*, published mathematical record (October 11, 2026), public-result identifier `48a4d84c1cc7` (full theorem and proof inspected).
