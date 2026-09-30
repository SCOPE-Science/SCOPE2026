# Outer-parallel deficit identity and smooth rigidity in planar fractional isoperimetry

## Statement

Let \(q\in(0,1)\), and let \(K\subset\mathbb R^2\) be a \(C^\infty_+\) convex body. Write
\[
R=\frac{\operatorname{Per}(K)}{2\pi},\qquad K_r=K+rB_1 .
\]
Let \(C_q\) denote the planar chord functional and \(W_\alpha\) the fractional Willmore-type quantity of Lin--Yang--Yang--Yuan--Zhang (arXiv:2609.19052). Then
\[
\boxed{
C_q(B_R)-C_q(K)
=
2q\int_0^\infty
\left[
W_{1-q}(K_r)-W_{1-q}(B_{R+r})
\right]\,dr .
}
\tag{1}
\]
The integrand is nonnegative. Moreover, it vanishes identically if and only if \(K\) is a disk (up to translation). Consequently,
\[
C_q(K)=C_q(B_1)
\left(\frac{\operatorname{Per}(K)}{2\pi}\right)^{q+1}
\]
holds in the \(C^\infty_+\) convex class if and only if \(K\) is a disk.

Equivalently, for \(s\in(0,1)\), let
\[
A_s=\frac{P_s(B_1)}{(2\pi)^{2-s}}.
\]
Since \(P_s(K)=[s(1-s)]^{-1}C_{1-s}(K)\) for convex \(K\), (1) gives the exact fractional-perimeter deficit formula
\[
\boxed{
A_s\,\operatorname{Per}(K)^{2-s}-P_s(K)
=
\frac{2}{s}\int_0^\infty
\left[
W_s(K_r)-W_s(B_{R+r})
\right]\,dr .
}
\tag{2}
\]
Hence the sharp planar fractional isoperimetric inequality of arXiv:2609.19052 has a unique equality case within the \(C^\infty_+\) convex class: the disk.

## Proof

### 1. Differentiate along the complete outer-parallel flow

Set
\[
H(r)=C_q(K_r)-C_q(B_{R+r}),\qquad r\ge0.
\]
The planar Steiner formula gives
\[
\operatorname{Per}(K_r)=\operatorname{Per}(K)+2\pi r
=2\pi(R+r),
\]
so \(K_r\) and \(B_{R+r}\) have the same perimeter for every \(r\).

Proposition 3.8 of arXiv:2609.19052 gives, for a smooth strictly convex body \(L\),
\[
\left.\frac{d}{dt}\right|_{t=0}C_q(L+tB_1)
=
2q\,W_{1-q}(L).
\]
Applying this formula to \(L=K_r\) and to \(L=B_{R+r}\) yields
\[
H'(r)
=
2q\left[
W_{1-q}(K_r)-W_{1-q}(B_{R+r})
\right].
\tag{3}
\]
Along this smooth normal variation the first-variation formula applies on every compact \(r\)-interval, so the fundamental theorem of calculus may be used in (3).

Proposition 3.3 of the same paper gives the fixed-perimeter fractional Willmore inequality
\[
W_{1-q}(K_r)\ge W_{1-q}(B_{R+r}),
\tag{4}
\]
and therefore \(H'(r)\ge0\).

### 2. Use the large-parallel-body asymptotic

The proof of the sharp convex chord inequality in arXiv:2609.19052 establishes, after normalizing the perimeter, that the chord-functional difference between an outer parallel body and the equal-perimeter disk tends to zero as the parallel radius tends to infinity; in fact the displayed remainder there is \(O(r^{q-1})\). Scaling from the normalized perimeter to \(R=\operatorname{Per}(K)/(2\pi)\) gives
\[
\lim_{r\to\infty}H(r)=0.
\tag{5}
\]

Integrating (3) from \(0\) to \(T\) and using (5),
\[
-H(0)
=
\lim_{T\to\infty}\int_0^T H'(r)\,dr.
\]
Because the integrand is nonnegative by (4), the improper integral converges and
\[
C_q(B_R)-C_q(K)
=
2q\int_0^\infty
\left[
W_{1-q}(K_r)-W_{1-q}(B_{R+r})
\right]\,dr,
\]
which is (1).

### 3. Rigidity of the integrand

Döhrer--Dohmen (arXiv:2604.02042, Theorem 1.3) prove that for every \(\alpha\in(0,1)\) and \(p\ge1\), disks are the unique minimizers of their fractional Willmore energy among planar convex sets with fixed perimeter.

For \(p=1\), their energy agrees with \(W_\alpha\) above up to a positive normalization constant. Indeed, with their inward normal \(n=-\nu\),
\[
\langle n(y),x-y\rangle
=
\langle \nu(y),y-x\rangle,
\]
so the boundary kernel is the same as the one used in the fractional mean-curvature representation underlying \(W_\alpha\). Convexity makes the relevant pointwise curvature nonnegative, so the absolute value in the \(p=1\) energy introduces no discrepancy in the equality class.

It follows that equality in (4) occurs if and only if \(K_r\) is a disk. If \(K_r\) is a disk for some \(r\), then the support-function identity
\[
h_{K_r}=h_K+r
\]
shows that \(h_K\) is also the support function of a disk. Thus a non-disk \(K\) has
\[
W_{1-q}(K_r)>W_{1-q}(B_{R+r})
\qquad\text{for every }r\ge0.
\]
Therefore the right-hand side of (1) is strictly positive for every non-disk \(K\), proving the equality characterization.

### 4. Fractional perimeter

Set \(q=1-s\). For convex bodies, Proposition 2.1 of arXiv:2609.19052 gives the exact identity
\[
P_s(K)=\frac{1}{s(1-s)}\,C_{1-s}(K).
\]
Dividing (1) by \(s(1-s)\) yields
\[
A_s\,\operatorname{Per}(K)^{2-s}-P_s(K)
=
\frac{2}{s}\int_0^\infty
\left[
W_s(K_r)-W_s(B_{R+r})
\right]\,dr,
\]
which is (2).

## Interpretation

The sharp chord and fractional-perimeter deficits are not merely controlled by a curvature excess: in the smooth strictly convex class they are exactly the accumulated fractional-Willmore excess along the entire outer-parallel flow. The large-radius asymptotic closes the identity at infinity, while fractional-Willmore rigidity turns the representation into a strict equality characterization.

This separates two ingredients that are already present in the literature from the new conclusion. The first-variation formula, the Willmore lower bound used in the monotonicity proof, and the large-parallel-body asymptotic come from arXiv:2609.19052. The uniqueness of the fractional-Willmore minimizer is prior work of Döhrer--Dohmen, arXiv:2604.02042. The contribution here is the exact integrated deficit representation (1)--(2), together with the resulting uniqueness of the disk for the new sharp chord/fractional-perimeter inequality in the \(C^\infty_+\) convex class.

## Relation to prior literature and originality scope

Lin, Yang, Yang, Yuan and Zhang prove the sharp planar inequality and state that equality is attained by the disk. Their proof of the convex chord inequality uses monotonicity of
\[
C_q(K+rB_1)-C_q(B_{R+r})
\]
and its decay to zero at infinity, but the exact integral representation of the deficit and an equality classification are not stated in the inspected version (arXiv:2609.19052v1).

Döhrer and Dohmen prove a stronger rigidity statement for the fractional Willmore energy itself: disks uniquely minimize every fractional Willmore energy in the convex planar class. That theorem is treated here as prior art and is used only to identify the zero set of the integrand in (1).

Searches for the exact identity, synonymous outer-parallel deficit formulas, and a stated uniqueness theorem for the chord inequality did not locate an earlier matching result. The originality claim is therefore limited to the integrated outer-parallel deficit identity and the equality consequence for the sharp chord/fractional-perimeter inequality, to the best of our knowledge.

## Limitations

- The exact identity and equality classification above are asserted for \(C^\infty_+\) convex bodies, where the first-variation formula along the outer-parallel family applies directly.
- No equality classification is claimed here for arbitrary \(C^1\) domains or for nonsmooth convex bodies.
- No quantitative lower bound in terms of Fraenkel asymmetry, Hausdorff distance, or another geometric distance to disks is proved.
- The fractional-Willmore rigidity used in the proof is not new.
- The principal source paper is recent, so a simultaneous or not-yet-indexed observation remains possible.

## References

1. Xiaosheng Lin, Dachun Yang, Sibei Yang, Wen Yuan, Yangyang Zhang, *A Sharp Planar Fractional Isoperimetric Inequality*, arXiv:2609.19052v1, 2026. https://arxiv.org/abs/2609.19052
2. Elias Döhrer, Alexander Dohmen, *A Fenchel Theorem for the Gauss maps and uniqueness of minimizers of nonlocal curvature energies*, arXiv:2604.02042v1, 2026. https://arxiv.org/abs/2604.02042
