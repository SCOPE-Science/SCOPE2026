# Global curvature-radius stability for the planar fractional-perimeter maximum

## Statement

Let \(0<s<1\), and let \(K\subset\mathbb R^2\) be a \(C^\infty\) strictly
convex body with positive curvature and
\[
\operatorname{Per}(K)=2\pi.
\]
Write \(\rho(\vartheta)>0\) for the radius of curvature, parametrized by tangent
angle \(\vartheta\in\mathbb T=\mathbb R/(2\pi\mathbb Z)\).  Then
\(\int_0^{2\pi}\rho(\vartheta)\,d\vartheta=2\pi\).  For a mean-zero periodic
function \(f\), use the convention
\[
 \|f\|_{\dot H^{-1}(\mathbb T)}^2
 :=
 \inf_{c\in\mathbb R}\int_0^{2\pi}|F(\vartheta)-c|^2\,d\vartheta,
 \qquad F'=f .
\]
This definition is independent of the chosen periodic primitive.

Then
\[
\boxed{
 P_s(B_1)-P_s(K)
 \ge
 \frac{(\pi-\frac23)\sin(\pi/8)}
      {2^{3+s}s(1+s)}
 \,\|\rho-1\|_{\dot H^{-1}(\mathbb T)}^2 .
}
\tag{1}
\]
Here \(P_s\) is the fractional \(s\)-perimeter in the normalization of
Lin--Yang--Yang--Yuan--Zhang, arXiv:2609.19052.  In particular, the deficit
vanishes only for a disk.

More generally, if \(R=\operatorname{Per}(K)/(2\pi)\) and
\(\widehat\rho=\rho/R\), scaling gives
\[
 P_s(B_R)-P_s(K)
 \ge
 \frac{(\pi-\frac23)\sin(\pi/8)}
      {2^{3+s}s(1+s)}
 R^{2-s}\,
 \|\widehat\rho-1\|_{\dot H^{-1}(\mathbb T)}^2 .
\tag{2}
\]

The underlying chord-functional estimate is also quantitative.  If
\(0<q<1\), \(C_q\) is the chord functional of arXiv:2609.19052, and
\(\operatorname{Per}(K)=2\pi\), then
\[
\boxed{
 C_q(B_1)-C_q(K)
 \ge
 \frac{q(\pi-\frac23)\sin(\pi/8)}
      {2^{4-q}(2-q)}
 \,\|\rho-1\|_{\dot H^{-1}(\mathbb T)}^2 .
}
\tag{3}
\]

The constants in (1)--(3) are explicit but are not claimed to be optimal.

## Context

Lin, Yang, Yang, Yuan and Zhang proved in arXiv:2609.19052 that for planar
domains the disk maximizes the fractional perimeter at fixed classical
perimeter.  Their convex-body proof factors through a chord functional, a
fractional Willmore-type inequality, a first-variation formula along outer
parallel bodies, and a large-parallel-body asymptotic.  Frank and Ivanisvili
independently proved the fixed-perimeter maximization for general planar sets
of finite perimeter in arXiv:2609.14513.

Quantitative stability was recently obtained by Alberti, Cozzi, Massaccesi and
Mirmina (arXiv:2605.07543) for a ratio of two genuinely fractional perimeters
\(P_t\) and \(P_s\), \(0<s<t<1\), near spherical sets.  The estimate here is
different: it treats the endpoint in which the upper-order perimeter is the
classical perimeter, is global within the stated smooth strictly convex class,
and controls a curvature-radius \(\dot H^{-1}\) deviation.

The disk-minimizing property of related fractional Willmore energies is also
known; see Döhrer--Dohmen, arXiv:2604.02042.  The contribution below is the
quantitative deficit that propagates through the specific fractional-Willmore
and outer-parallel-body mechanism of arXiv:2609.19052.

## Proof

Set
\[
 A_*:=\left(\pi-\frac23\right)\sin\frac{\pi}{8}.
\]

### 1. A quantitative fractional-Willmore deficit

Let \(0<\alpha<1\), and let \(W_\alpha\) be the fractional Willmore-type
functional used in arXiv:2609.19052.  We first prove
\[
 W_\alpha(K)-W_\alpha(B_1)
 \ge
 \frac{\alpha A_*}{2^{4+\alpha}}\,
 D(K),
\tag{4}
\]
where, if \(\gamma\) is the unit-speed boundary parametrization and
\(\theta(s)\) is its increasing tangent-angle lift,
\[
 D(K):=\inf_{c\in\mathbb R}
 \int_0^{2\pi}|\theta(s)-s-c|^2\,ds.
\]

For \(w\in(0,2\pi)\), put
\[
 x_u:=\theta(u+w)-\theta(u),\qquad
 g(u):=\theta(u)-u.
\]
Convexity gives \(0<x_u<2\pi\), and periodicity of the tangent angle gives
\[
 \int_0^{2\pi}x_u\,du=2\pi w.
\tag{5}
\]
Let
\[
 \phi(x):=2\sin(x/2),\qquad
 I:=[\pi/2,3\pi/2],\qquad
 \sigma:=\frac{\sin(\pi/8)}8 .
\]
For every \(w\in I\) and \(x\in[0,2\pi]\),
\[
 \phi(w)+\phi'(w)(x-w)-\phi(x)
 \ge \sigma(x-w)^2.
\tag{6}
\]
Indeed, \(-\phi''(t)=\tfrac12\sin(t/2)\).  In the Taylor remainder, retain
only the half of the segment joining \(w\) to \(x\) that is adjacent to
\(w\).  That half lies in \([\pi/4,7\pi/4]\), where
\(\sin(t/2)\ge\sin(\pi/8)\); both the retained length and the linear Taylor
weight are at least \(|x-w|/2\).  This yields (6).

Integrating (6), the linear term vanishes by (5), and therefore
\[
 4\pi\sin(w/2)
 -
 \int_0^{2\pi}|\gamma'(u+w)-\gamma'(u)|\,du
 \ge
 \sigma Q_w,
\tag{7}
\]
where
\[
 Q_w:=\int_0^{2\pi}|g(u+w)-g(u)|^2\,du.
\]

Use the notation from the proof of the fractional-Willmore inequality in
arXiv:2609.19052:
\[
 r=\gamma(u+w)-\gamma(u),\quad R=|r|,\quad e=r/R,
\]
\[
 A(u,w)=
 \left|P_{e(u,w)}^\perp\bigl(\gamma'(u+w)-\gamma'(u)\bigr)\right|.
\]
Set
\[
 B_w:=\int_0^{2\pi}A(u,w)\,du,\qquad
 J(w):=\int_0^{2\pi}A(u,w)R(u,w)^{-1-\alpha}\,du.
\]
The source proof gives
\[
 \int_0^{2\pi}\frac{A}{R}\,du\ge2\pi
\]
and hence, by Hölder,
\[
 J(w)\ge(2\pi)^{1+\alpha}B_w^{-\alpha}.
\tag{8}
\]
Since \(A\le|\gamma'(u+w)-\gamma'(u)|\), (7) implies, for \(w\in I\),
\[
 B_w\le M_w-\sigma Q_w,\qquad
 M_w:=4\pi\sin(w/2).
\tag{9}
\]
The function \(x\mapsto x^{-\alpha}\) is convex, so (8)--(9) give
\[
 J(w)-J_{B_1}(w)
 \ge
 \alpha\sigma(2\pi)^{1+\alpha}M_w^{-1-\alpha}Q_w
 \ge
 \alpha\sigma\,2^{-1-\alpha}Q_w,
\tag{10}
\]
where \(M_w\le4\pi\) was used in the last step.  The source representation
\[
 W_\alpha(K)=\frac12\int_0^{2\pi}J(w)\,dw
\]
and its nonquantitative lower bound outside \(I\) yield
\[
 W_\alpha(K)-W_\alpha(B_1)
 \ge
 \alpha\sigma\,2^{-2-\alpha}\int_IQ_w\,dw.
\tag{11}
\]

It remains to estimate the last integral.  If
\(g(u)=\sum_{k\in\mathbb Z}c_ke^{iku}\), Parseval gives
\[
 \int_IQ_w\,dw
 =
 4\pi\sum_{k\ne0}|c_k|^2
 \int_{\pi/2}^{3\pi/2}(1-\cos kw)\,dw.
\]
For \(k\ne0\),
\[
 \int_{\pi/2}^{3\pi/2}(1-\cos kw)\,dw
 \ge \pi-\frac23,
\]
with the minimum attained at \(|k|=3\).  Hence
\[
 \int_IQ_w\,dw
 \ge
 2\left(\pi-\frac23\right)
 \inf_c\int_0^{2\pi}|g-c|^2\,du.
\tag{12}
\]
Combining (11), (12), and
\(\sigma=\sin(\pi/8)/8\) proves (4).

### 2. Conversion to curvature radius along parallel bodies

Return to the normalized body \(K\), and let
\[
 h(\vartheta):=\int_0^\vartheta(\rho(t)-1)\,dt.
\]
Because \(\int(\rho-1)=0\), this is periodic up to an irrelevant additive
constant and
\[
 \mathcal E(K):=
 \|\rho-1\|_{\dot H^{-1}}^2
 =
 \inf_b\int_0^{2\pi}|h(\vartheta)-b|^2\,d\vartheta.
\tag{13}
\]

For \(r\ge0\), set \(K_r=K+rB_1\) and
\(\widetilde K_r=K_r/(1+r)\).  Then
\(\operatorname{Per}(\widetilde K_r)=2\pi\), and in tangent-angle
coordinates
\[
 \rho_r(\vartheta)=\frac{\rho(\vartheta)+r}{1+r},\qquad
 s_r(\vartheta)=
 \vartheta+\frac{h(\vartheta)}{1+r}.
\]
Consequently,
\[
 D(\widetilde K_r)
 =
 \frac1{(1+r)^2}
 \inf_b\int_0^{2\pi}|h-b|^2\rho_r(\vartheta)\,d\vartheta
 \ge
 \frac{r}{(1+r)^3}\mathcal E(K).
\tag{14}
\]

Let \(q\in(0,1)\) and put \(\alpha=1-q\).  The homogeneity
\(W_\alpha(\lambda K)=\lambda^{1-\alpha}W_\alpha(K)\), together with
(4) and (14), gives
\[
 W_{1-q}(K_r)-W_{1-q}(B_{1+r})
 \ge
 \frac{(1-q)A_*}{2^{5-q}}\,
 r(1+r)^{q-3}\mathcal E(K).
\tag{15}
\]

### 3. Integration of the chord-functional variation

Define
\[
 H(r):=C_q(K_r)-C_q(B_{1+r}).
\]
The first-variation formula of arXiv:2609.19052 gives
\[
 H'(r)=
 2q\bigl[
 W_{1-q}(K_r)-W_{1-q}(B_{1+r})
 \bigr].
\tag{16}
\]
The same source proves \(H(r)\to0\) as \(r\to\infty\).  Integrating
(15)--(16) and using
\[
 \int_0^\infty r(1+r)^{q-3}\,dr
 =\frac1{(1-q)(2-q)}
\]
yields
\[
 C_q(B_1)-C_q(K)
 =
 \int_0^\infty H'(r)\,dr
 \ge
 \frac{qA_*}{2^{4-q}(2-q)}\mathcal E(K),
\]
which is (3).

For a convex body the source identity is exact:
\[
 P_s(K)=\frac1{s(1-s)}C_{1-s}(K).
\]
Setting \(q=1-s\) in (3) proves (1).  Homogeneity of the fractional
perimeter and of the curvature radius then gives (2).

## Adversarial checks

The sign is consistent with the fixed-perimeter theorem: the disk maximizes
\(P_s\), while the fractional Willmore quantity used in the parallel-body
variation is minimized by the disk.  The parallel-body deficit \(H(r)\) is
nonpositive and increasing to zero, so
\(C_q(B_1)-C_q(K)=\int_0^\infty H'(r)\,dr\).

The Fourier constant in (12) is explicit:
for even \(k\) the integral equals \(\pi\); for odd \(k\) it is
\(\pi\pm2/|k|\), with the minimum \(\pi-2/3\) at \(|k|=3\).
The quantitative tangent estimate (6) uses only a compact central window
\(w\in[\pi/2,3\pi/2]\), avoiding endpoint degeneracy of the sine concavity.

Finally, \(\mathcal E(K)=0\) forces \(\rho\equiv1\), hence \(K\) is a unit
disk up to translation.  The metric is independent of the initial tangent
angle because changing the angular origin translates the periodic primitive
and adds a constant, both absorbed by the infimum in (13).

## Originality assessment

To the best of our knowledge, the explicit global estimate (1), and the
chord-functional estimate (3) from which it follows, are not contained in the
located literature.

The closest recent works have distinct scopes:

- Lin--Yang--Yang--Yuan--Zhang, arXiv:2609.19052, proves the sharp
  fixed-classical-perimeter inequality and supplies the chord/Willmore/parallel
  body identities used above, but does not state a quantitative deficit.
- Frank--Ivanisvili, arXiv:2609.14513, independently proves the planar
  fixed-perimeter maximization in a much larger class, but no quantitative
  curvature-radius deficit was located there.
- Alberti--Cozzi--Massaccesi--Mirmina, arXiv:2605.07543, proves local
  quantitative stability for nearly spherical sets for a ratio of two
  fractional perimeters with \(0<s<t<1\).  The classical-perimeter endpoint
  \(t=1\) is not their stated theorem.
- Döhrer--Dohmen, arXiv:2604.02042, proves disk minimality for fractional
  Willmore energies in the convex planar class, but no estimate equivalent to
  (4) was located.
- Blatt--Giacomin--Scheuer--Schikorra, arXiv:2306.16941, contains stability
  results for different fractional curvature energies in a subcritical
  regime; its stability theorem concerns closeness to a sphere under a
  different curvature defect and does not supply (1)--(4).

Searches were made using the exact recent source identifiers and combinations
of “fixed perimeter”, “fractional perimeter”, “quantitative stability”,
“curvature radius”, “H^{-1}”, “chord functional”, “outer parallel bodies”,
and “fractional Willmore”.  No equivalent global convex endpoint estimate was
located.  Because the fixed-perimeter papers are very recent, an unindexed
concurrent refinement remains a residual originality risk.  A non-obvious
limiting consequence of other stability frameworks also cannot be ruled out.

## Limitations

The theorem is proved only for \(C^\infty\) strictly convex planar bodies with
positive curvature.  No extension to arbitrary finite-perimeter sets, general
\(C^1\) domains, polygons, or convex bodies with flat pieces is claimed.

The controlled quantity is a curvature-radius \(\dot H^{-1}\) distance.  No
Fraenkel-asymmetry, Hausdorff-distance, or optimal-transport stability bound is
deduced.  The explicit constants are not optimized, and no optimality claim
for the metric or constant is made.  The result is a quantitative refinement
of the convex mechanism behind the recent fixed-perimeter inequality, not a
replacement for the more general qualitative theorem.

## References

1. X. Lin, D. Yang, S. Yang, W. Yuan, Y. Zhang,
   *A Sharp Planar Fractional Isoperimetric Inequality*,
   arXiv:2609.19052, https://arxiv.org/abs/2609.19052
2. R. L. Frank, P. Ivanisvili,
   *Sharp comparison between the perimeter and its fractional analogue in two dimensions*,
   arXiv:2609.14513, https://arxiv.org/abs/2609.14513
3. G. Alberti, G. Cozzi, A. Massaccesi, J. Mirmina,
   *Stability of the ball in isoperimetric inequalities between two fractional perimeters*,
   arXiv:2605.07543, https://arxiv.org/abs/2605.07543
4. E. Döhrer, A. Dohmen,
   *A Fenchel Theorem for the Gauss maps and uniqueness of minimizers of nonlocal curvature energies*,
   arXiv:2604.02042, https://arxiv.org/abs/2604.02042
5. S. Blatt, G. Giacomin, J. Scheuer, A. Schikorra,
   *A fractional Willmore-type energy functional -- subcritical observations*,
   arXiv:2306.16941, https://arxiv.org/abs/2306.16941
