# A directional-energy dichotomy for iterated planar Steiner ellipses

## Finding

**Theorem (exact directional-energy criterion).** Let \(H_1,H_2,\ldots\) be any prescribed sequence of unoriented lines through the origin in the Euclidean plane. For a centered, positive-area ellipse \(E_0\), define \(E_m=S_{H_m}E_{m-1}\), where \(S_H\) is Steiner symmetrization with respect to \(H\). Write \(\theta_m\) for any angular representative of \(H_m\) modulo \(\pi\), and define the intrinsic directional energy

\[
\mathcal E(H)=\sum_{m=2}^{\infty}\sin^2\bigl(2(\theta_m-\theta_{m-1})\bigr).
\]

Then the following statements hold.

1. If \(\mathcal E(H)=\infty\), **every centered ellipse** converges in Hausdorff distance to the centered disk of the same area. Let \(D>0\) denote the determinant of its positive-definite shape matrix. For \(m\geq1\), let \(x_m\) be its squared semiaxis along \(H_m\), and put

\[
u_m=\frac{x_m-\sqrt D}{x_m+\sqrt D},\qquad q_m=|u_m|<1.
\]

If \(q_1>0\), the explicit bound

\[
q_m\leq q_1\exp\!\left[-\frac{1-q_1}{2(1+q_1)}\sum_{j=2}^{m}\sin^2\bigl(2(\theta_j-\theta_{j-1})\bigr)\right]
\]

holds. If \(q_1=0\), all subsequent ellipses are exactly disks.

2. If \(\mathcal E(H)<\infty\), every centered ellipse still has a limiting semiaxis ratio, but **the limiting ratio is unequal to one unless a disk is reached at a finite stage**. For a fixed direction sequence, among centered noncircular initial ellipses with principal axes \(H_1,H_1^{\perp}\), the initial semiaxis ratios yielding finite-step circularization form an at most countable set. Thus no finite-energy sequence circularizes *every* centered ellipse in the limit.

Consequently, a direction sequence circularizes all centered ellipses precisely when its directional energy diverges. For \(m\geq2\), a **previously noncircular** iterate becomes a disk at step \(m\) exactly when

\[
\cos\bigl(2(\theta_m-\theta_{m-1})\bigr)=-u_{m-1}.
\]

The central formula, valid for arbitrary directions and every prior noncircular ellipse, is the exact signed-anisotropy evolution

\[
\boxed{\quad u_m=u_{m-1}\frac{u_{m-1}+\cos(2(\theta_m-\theta_{m-1}))}{1+u_{m-1}\cos(2(\theta_m-\theta_{m-1}))}.\quad}
\]

**Two explicit regimes.** Consecutive symmetry axes differing by exactly \(\pi/4\) give the double-exponential law \(u_m=u_1^{2^{m-1}}\) for all \(m\geq2\). In contrast, set \(\theta_1=0\) and \(\theta_m=\sum_{j=2}^{m}1/j\) for \(m\geq2\). The directions are dense modulo \(\pi\), yet \(\mathcal E(H)<\infty\). For every initially noncircular centered ellipse whose major axis is \(H_1\), the anisotropy converges to \(u_\infty>0\), while the unrotated ellipses have as their complete subsequential limit set the full rotation orbit of a noncircular ellipse.

## Assumptions and scope

Everything is in \(\mathbb R^2\). A centered ellipse is \(E(A)=\{z:z^{\mathsf T}A^{-1}z\leq1\}\) for a real symmetric positive-definite \(2\times2\) matrix \(A\), with determinant \(D\) and area \(\pi\sqrt D\). All lines pass through the origin. The angles are understood modulo \(\pi\), making every summand of \(\mathcal E(H)\) unambiguous. Hausdorff convergence is Euclidean; translations are not involved. The limiting disk has radius \(D^{1/4}\).

## Proof

**Steiner ellipse matrix identity.** In orthonormal coordinates \((e,f)\), with \(e\) along \(H\), let \(A=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)\). The half-length of the perpendicular chord at horizontal coordinate \(s\) is \(\sqrt{(\det A)/a}\sqrt{1-s^2/a}\); its center shift is linear in \(s\). After translating every chord to be centered on \(H\), the result is precisely \(E(\operatorname{diag}(a,\det A/a))\). Thus determinant and center are preserved, and the new principal axes are \(H\) and \(H^\perp\).

For \(m\geq2\), the prior matrix in its own axes is \(\operatorname{diag}(x_{m-1},D/x_{m-1})\). Rotating the next line by \(\delta_m=\theta_m-\theta_{m-1}\) gives

\[
x_m=x_{m-1}\cos^2\delta_m+\frac{D}{x_{m-1}}\sin^2\delta_m.
\]

Let \(t_m=x_m/\sqrt D=(1+u_m)/(1-u_m)\). Then \(t_m=t_{m-1}\cos^2\delta_m+t_{m-1}^{-1}\sin^2\delta_m\), which simplifies exactly to the displayed rational recurrence. The denominator \(1+u_{m-1}\cos 2\delta_m\) is strictly positive because \(|u_{m-1}|<1\).

**Exact loss identity and divergence direction.** For \(u_{m-1}\neq0\), write \(C_m=\cos2\delta_m\) and \(s_m=1-C_m^2=\sin^2 2\delta_m\). Squaring the rational recurrence and subtracting from one yields

\[
1-\left(\frac{u_m}{u_{m-1}}\right)^2
=\frac{(1-u_{m-1}^{2})s_m}{(1+u_{m-1}C_m)^2}.
\]

The right side belongs to \([0,1]\). In particular \(q_m\leq q_{m-1}\leq q_1\). Put \(\rho=q_1<1\). Uniformly over all subsequent iterates,

\[
1-\left(q_m/q_{m-1}\right)^2
\geq\frac{1-\rho}{1+\rho}s_m
\]

until an iterate reaches zero, after which the result is immediate. Applying \(\sqrt{1-v}\leq e^{-v/2}\) iteratively proves the exponential energy bound. When \(\sum s_m=\infty\), it implies \(q_m\to0\). The two semiaxis lengths of \(E_m\) are \(D^{1/4}\sqrt{(1\pm q_m)/(1\mp q_m)}\), which both tend to \(D^{1/4}\) independently of orientation; the Hausdorff conclusion follows.

**Summable energy is insufficient unless an exact disk occurs.** Suppose \(\sum s_m<\infty\) and no \(u_m\) is zero. The exact loss \(a_m=1-(q_m/q_{m-1})^2\) obeys

\[
0\leq a_m\leq\frac{s_m}{(1-\rho)^2}.
\]

Therefore \(\sum a_m<\infty\). Each \(a_m<1\) under the no-circularization hypothesis, so the convergent infinite product \(\prod_{m=2}^{\infty}(1-a_m)\) is strictly positive. Consequently \(q_m\downarrow q_\infty>0\). The semiaxis ratio converges to \((1+q_\infty)/(1-q_\infty)>1\), though the major-axis line need not converge. If an iterate is a disk, Steiner symmetrization leaves it fixed. The recurrence shows a nonzero iterate reaches zero if and only if \(C_m=-u_{m-1}\).

**Countable exceptional aspect ratios.** Fix \((H_m)\) and consider initially aligned ellipses, so \(u_1=\rho\in(0,1)\) can vary freely with their aspect ratio. Each \(u_m\) is a real rational function of \(\rho\), analytic without poles on \((0,1)\). It is not identically zero: near \(\rho=0\), the transformation \(T_C(u)=u(u+C)/(1+Cu)\) has nonzero leading term \(Cu\) when \(C\neq0\), or \(u^2\) when \(C=0\); induction gives a nonzero leading term for every finite composition. Thus each condition \(u_m(\rho)=0\) has finitely many solutions, and their union over \(m\) is at most countable. In particular there are uncountably many aligned noncircular ellipses which do not approach a disk when \(\mathcal E(H)\) is finite.

**Dense rotating counterexample and quarter-turn angles.** If every \(\delta_m=\pi/4\) for \(m\geq2\), then \(C_m=0\), hence \(u_m=u_{m-1}^2\). For \(\delta_m=1/m\), \(m\geq2\), we have \(0<\cos(2/m)<1\) and \(\sum\sin^2(2/m)<\infty\). An initially positive \(u_1\) stays positive and converges to \(u_\infty>0\) by the preceding argument. The partial harmonic sums diverge with increments tending to zero; their residues modulo \(\pi\) approach every angle arbitrarily well. Because the signed anisotropy stays positive, the major axis is precisely \(H_m\), and the complete set of geometric subsequential limits consists of the rotated copies of the noncircular limiting semiaxis pair. This completes the proof.

## Verification

The proof is analytic and covers all positive-definite matrices, every infinite direction sequence, and every step, not just finite samples. The accompanying standalone Python script checks the Steiner matrix identity against independently constructed matrices, the rational recurrence and loss identity, the quarter-turn law, and the finite-horizon energy bound. These finite tests diagnose implementation mistakes; they do not establish the infinite-product or density arguments, which are proved above. Run with \(\texttt{python3 checker.py}\) in the extracted folder.

## Relationship to prior work

Kipp and Sagmeister's *Random convergence of generalized Steiner processes* (arXiv:2610.05113v1, first posted 2026-10-04), the motivating recent source, treats random directions and general \(\lambda\)-Steiner processes. The present theorem instead gives an exact if-and-only-if test for **every prescribed deterministic** planar direction sequence, restricted to centered ellipses.

Bianchi, Burchard, Gronchi and Volčič (arXiv:1206.2041) proved convergence in shape under square-summable angular increments and already demonstrated that dense directions need not force unrotated convergence. The dense-direction phenomenon itself is therefore not claimed as new; the explicit positive limiting elliptical anisotropy and the exact directional-energy criterion are the points of comparison.

Ulivelli's later *Iterated Steiner symmetrization of convex bodies always converges in shape* (arXiv:2611.21167v1, first posted 2026-11-16), Theorem 2.4 and §2.2, gives the all-sequence ellipse shape-convergence dichotomy and the same elementary ellipse-matrix transformation. The present result does not claim those prior statements. It gives a necessary-and-sufficient prescribed-direction test for convergence **to a disk**, exact exceptional finite-step cancellation, and a quantitative rate in the intrinsic angular energy; Ulivelli's classification does not state these.

## Limitations

The theorem concerns centered planar ellipses, not arbitrary convex bodies or off-center ellipses; the direction sequence need not circularize general bodies when its energy diverges. The quantitative constant in the displayed bound is not asserted to be globally optimal. For finite energy, the limiting nonzero anisotropy depends on the initial ellipse and the whole angle sequence, rather than only on the sum. A finite exact circularization can occur even when the total energy is finite. Historical priority of the exact criterion remains provisional pending independent literature verification.

## References

1. C. Kipp and Á. Sagmeister, *Random convergence of generalized Steiner processes*, arXiv:2610.05113v1, 2026-10-04. https://arxiv.org/html/2610.05113v1
2. G. Bianchi, A. Burchard, P. Gronchi and A. Volčič, *Convergence in shape of Steiner symmetrizations*, arXiv:1206.2041, 2012. https://arxiv.org/abs/1206.2041
3. J. Ulivelli, *Iterated Steiner symmetrization of convex bodies always converges in shape*, arXiv:2611.21167v1, 2026-11-16. https://arxiv.org/html/2611.21167v1
