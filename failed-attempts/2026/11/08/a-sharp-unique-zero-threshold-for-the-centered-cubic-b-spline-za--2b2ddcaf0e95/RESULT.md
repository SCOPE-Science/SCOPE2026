# A sharp unique-zero threshold for the centered cubic B-spline Zak transform

## Finding
Let \(B_4=B_1*B_1*B_1*B_1\), where \(B_1=\mathbf1_{[-1/2,1/2]}\), and let
\[
Z_\lambda B_4(x,\nu)=\sqrt\lambda\sum_{k\in\mathbb Z}B_4(\lambda(x-k))e^{2\pi i k\nu}.
\]
For every \(1/2\le\lambda\le1\), the zero set of \(Z_\lambda B_4\) in the half-open fundamental square \([0,1)^2\) consists of the single point \((1/2,1/2)\) **if and only if** \(4/7\le\lambda\le1\). For \(1/2<\lambda<4/7\), the zero set contains the nondegenerate segment
\[
\{(x,1/2):2(2-1/\lambda)\le x\le1-2(2-1/\lambda)\}.
\]
At \(\lambda=1/2\) the whole line \(\nu=1/2\) is zero. At the sharp transition \(\lambda=4/7\) the displayed interval shrinks to its midpoint.

## Assumptions and scope
The spline is the centered cardinal **order-four** (degree-three) compactly supported B-spline, not the quadratic order-three spline. All parameters are real, \(1/2\le\lambda\le1\), and zeros refer to exact complex values of the continuous Zak transform. The formula defines a finite sum at every point because \(B_4\) is supported on \([-2,2]\). The transform is periodic in \(\nu\), quasi-periodic in \(x\), and inherits reflection/conjugation symmetries from the real even spline. Its zero set is determined by its restriction to \([0,1/2]^2\).

For \(t\ge0\), the spline has the exact values
\[
B_4(t)=\begin{cases}(4-6t^2+3t^3)/6,&0\le t\le1,\\(2-t)^3/6,&1\le t\le2,\\0,&t\ge2.\end{cases}
\]

## Proof
**Interior and right boundary above the transition.** Put \(u=\lambda\), \(v=\lambda x\) and restrict initially to \(4/7\le u\le1\), \(0<x\le1/2\), \(0<\nu<1/2\). We have \(0<v\le u/2\), and the only possibly nonzero terms of the Zak sum correspond to \(-3\le k\le3\). For \(j=1,2,3\), let
\[
\Delta_j=B_4(ju-v)-B_4(ju+v)\ge0.
\]
The inequality holds because \(B_4\) is decreasing on the nonnegative half-line. Writing \(\theta=2\pi\nu\) and \(t=\cos\theta\in(-1,1)\), we obtain
\[
\operatorname{Im}\bigl(\lambda^{-1/2}Z_\lambda B_4(x,\nu)\bigr)
=\sin\theta\,[\Delta_1+2t\Delta_2+(4t^2-1)\Delta_3].
\]
The critical algebraic inequalities throughout the closed rational trapezoid
\(T=\{(u,v):4/7\le u\le1,\ 0\le v\le u/2\}\) are
\[
\Delta_2-4\Delta_3\ge0,\qquad
\Delta_1-2\Delta_2+3\Delta_3>0\quad(v>0).
\tag{1}
\]
The attached executable `CHECK.py` proves (1) by exact rational Bernstein coefficients, not sampling. It partitions \(T\) at all knot lines \(ju\pm v\in\{1,2\}\), for \(j=1,2,3\), into eight nonoverlapping rational polygons. Ten triangles cover these cells exactly; for both cubic expressions in (1), every degree-three Bernstein coefficient on every triangle is nonnegative. For all triangle vertices with \(v>0\), the respective pure-cube Bernstein coefficient is strictly positive. Thus both expressions are nonnegative everywhere; the second is strictly positive for \(v>0\), since every such point has positive barycentric weight at a vertex with \(v>0\). The checker asserts exact area conservation and prints the counts. This gives an independently reproducible finite certificate for the two polynomial inequalities over an *infinite continuum* of parameters, using exact arithmetic.

For \(Q(t)=\Delta_1+2t\Delta_2+(4t^2-1)\Delta_3\), (1) yields \(Q'(t)=2\Delta_2+8t\Delta_3\ge2(\Delta_2-4\Delta_3)\ge0\) for \(-1\le t\le1\). Consequently
\[
Q(t)\ge Q(-1)=\Delta_1-2\Delta_2+3\Delta_3>0\quad(v>0).
\]
The imaginary part cannot vanish in this region; hence the Zak transform has no zero there.

**Other boundary pieces.** At \(\nu=0\), the defining sum is strictly positive because its terms are nonnegative and at least one is positive. At \(x=0\), Poisson summation and \(\widehat B_4(\xi)=(\sin\pi\xi/(\pi\xi))^4\) show that, up to a strictly positive prefactor,
\[
Z_\lambda B_4(0,\nu)=\sum_{n\in\mathbb Z}\left(\frac{\sin(\pi(n+\nu)/\lambda)}{\pi(n+\nu)/\lambda}\right)^4>0
\quad(0<\nu<1).
\]
Indeed all terms are nonnegative; simultaneous zero of the terms for adjacent integers would force \(1/\lambda\) to be an integer. In \([1,7/4]\) it must then be \(1\), and the terms at nonintegral \(\nu\) are still positive. The continuous extensions cover the removable denominators.

**Midpoint frequency and sharpness.** The exact midpoint-frequency classification of Hasannasab–Lemvig (Proposition 4.3 and its aliasing lemma, cited below) gives
\[
Z_\lambda B_4(x,1/2)=0\iff
x\in\{1/2\}\cup[2\delta,1-2\delta],\qquad
\delta=2-1/\lambda,
\]
for \(1/2<\lambda\le1\), with an interval interpreted as empty when the left endpoint exceeds its right. When \(\lambda\ge4/7\), \(\delta\ge1/4\) and the sole zero is \(x=1/2\); below that threshold the interval has positive length. At \(\lambda=1/2\) the aliasing lemma yields identically zero midpoint-frequency slice. Symmetry extends the preceding exclusions to the fundamental square. This proves both directions and the unique-zero assertion.

## Verification
Run `python CHECK.py` with Python 3 and `sympy==1.14.0`. Expected exact output: `CHECK_OK cells=8 triangles=10 bernstein_coefficients=200 zero_coefficients=39 strict_vertex_tests=42`. The checker partitions the full two-variable parameter domain; it does not infer continuum inequalities from a sampled grid. The analytic reduction from (1) to nonvanishing and the published midpoint-frequency lemma remain necessary proof steps, and are displayed above.

## Relationship to prior work
Hasannasab–Lemvig, arXiv:2609.13116v1 (first public September 11, 2026), determine the full zero set for the order-two hat spline at all scales and for higher-order splines above unit scale; their Proposition 4.3 supplies the midpoint-frequency slice for higher orders. These results give the sharp **failure** below \(4/7\) but do not rule out off-line zeros at scales \(4/7\le\lambda<1\). Inequalities (1) are the new two-variable nonvanishing step. Lemvig–Nielsen, arXiv:1507.03982v3, treats Gabor frame-set obstructions associated with B-splines rather than the asserted complete cubic Zak zero set. Gröchenig, arXiv:1507.08432v1, gives partition-of-unity Gabor obstructions, not this classification. Existing uniqueness for order-three quadratic splines does not imply the degree-three case because the knot geometry and coefficients change.

## Limitations
No claim is made for \(0<\lambda<1/2\), for \(\lambda>1\) beyond previously established literature, for other spline orders, or for associated general Gabor frame sets. The proof of midpoint-frequency behavior invokes the stated, publicly available Proposition 4.3; an independent derivation of that previously published lemma is not claimed. The finite Bernstein certificate is exact but requires executing the attached SymPy script to replay all coefficients. Priority beyond the sources explicitly compared is not certified.

## References
1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116v1, September 11, 2026, https://arxiv.org/abs/2609.13116.
2. J. Lemvig and K. H. Nielsen, *Counterexamples to the B-spline conjecture for Gabor frames*, arXiv:1507.03982v3, https://arxiv.org/abs/1507.03982.
3. K. Gröchenig, *Partitions of unity and new obstructions for Gabor frames*, arXiv:1507.08432v1, https://arxiv.org/abs/1507.08432.
