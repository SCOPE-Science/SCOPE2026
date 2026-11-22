# Sharp zero-free radius and nodal birth for planar weighted harmonic Bergman kernels

## Finding
For \(\beta>1\), define
\[
\mathcal K_\beta(z,w)=(1-z\overline{w})^{-\beta}+(1-\overline{z}w)^{-\beta}-1,
\quad \rho_\beta=2^{1/\beta}-1.
\]
The binomial functions are defined by their power series in the unit disk. Then, for every pair \(z,w\in\mathbb D\) satisfying \(r=|z\overline{w}|\le\rho_\beta\),
\[
\mathcal K_\beta(z,w)\ge \frac{2}{(1+r)^\beta}-1\ge0.
\]
Equality at \(r=\rho_\beta\) holds if and only if \(z\overline{w}=-\rho_\beta\). Thus \(\rho_\beta\) is the sharp zero-free product-radius, with strict positivity below it. For each fixed \(\rho_\beta<r<1/\beta\), there are exactly two zeros on the scalar product circle \(|z\overline{w}|=r\):
\[
 z\overline{w}=r\exp(i(\pi\pm\delta_\beta(r))),\qquad 0<\delta_\beta(r)<\pi,
\]
where \(\delta_\beta(r)\) is unique, and
\[
 \delta_\beta(r)=\sqrt{\frac{2(1+\rho_\beta)}{\rho_\beta(1-\beta\rho_\beta)}}\,\sqrt{r-\rho_\beta}+O_\beta((r-\rho_\beta)^{3/2}).
\]
For the corresponding coefficient-defined harmonic kernel at \(0<\beta\le1\), there are no zeros anywhere in \(\mathbb D^2\).

## Assumptions and scope
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). When \(\beta>1\), equip complex-valued harmonic functions with the Hilbert-space norm from the probability measure
\[
 d\mu_\beta(z)=(\beta-1)(1-|z|^2)^{\beta-2}\frac{dA(z)}{\pi}.
\]
For \(n\ge1\), \(\|z^n\|^2= n!/(\beta)_n\), and the same norm holds for \(\overline z^n\). Different nonconstant analytic and anti-analytic monomials are mutually orthogonal; the constant function has norm one. Therefore the displayed \(\mathcal K_\beta\) is precisely the reproducing kernel. The same coefficient definition makes a positive definite reproducing kernel for \(0<\beta\le1\), but that continuation is **not** claimed to be a weighted area Bergman space. Since every complex number of modulus less than one is realized as \(z\overline w\) for some pair in \(\mathbb D\), scalar product zeros and genuine bidisk kernel zeros are equivalent.

## Proof
**Kernel calculation.** Orthogonality gives
\[
\mathcal K_\beta(z,w)=1+\sum_{n\ge1}\frac{(\beta)_n}{n!}\bigl((z\overline w)^n+(\overline z w)^n\bigr)
=2\operatorname{Re}(1-z\overline w)^{-\beta}-1.
\]

**Angular monotonicity lemma.** Write \(s=re^{i\theta}\) with \(0<r<1\) and \(0\le\theta\le\pi\), and put
\[
F_r(\theta)=\operatorname{Re}(1-re^{i\theta})^{-\beta},\qquad
\psi_r(\phi)=\arg(1+re^{i\phi}),\quad\phi=\pi-\theta.
\]
The argument is chosen continuously in \([0,\pi/2)\). Direct differentiation gives
\[
\psi'_r(\phi)=\frac{r(\cos\phi+r)}{1+2r\cos\phi+r^2},\qquad
\psi''_r(\phi)=-\frac{r(1-r^2)\sin\phi}{(1+2r\cos\phi+r^2)^2}<0
\quad(0<\phi<\pi).
\]
Concavity and \(\psi_r(0)=0\) yield \(\psi_r(\phi)\le r\phi/(1+r)\). A separate direct differentiation gives
\[
F'_r(\theta)=-\beta r|1-re^{i\theta}|^{-\beta-1}
\sin\bigl(\theta+(\beta+1)\psi_r(\pi-\theta)\bigr).
\]
Whenever \(\beta r\le1\), the angle in the sine lies strictly between zero and \(\pi\) for \(0<\theta<\pi\), since
\[
0<\theta+(\beta+1)\psi_r(\pi-\theta)
\le\theta+\frac{(\beta+1)r}{1+r}(\pi-\theta)\le\pi.
\]
It follows that \(F_r\) is strictly decreasing on \((0,\pi)\). By conjugation symmetry and the harmonic minimum principle applied to \(s\mapsto\operatorname{Re}(1-s)^{-\beta}\), the same conclusion gives the sharp whole-product-disk lower bound
\[
\operatorname{Re}(1-s)^{-\beta}\ge(1+|s|)^{-\beta}
\quad\text{if }\beta|s|\le1,
\]
with equality for nonzero \(s\) only when \(s<0\) is real. (In fact the fixed-circle argument already proves this bound without the minimum principle.)

**Zero-free radius.** For \(\beta>1\), strict convexity of the function \(t\mapsto 2^t\) on \((0,1)\) yields \(2^{1/\beta}<1+1/\beta\), so \(\beta\rho_\beta<1\). Apply the angular lemma for \(r\le\rho_\beta\), and observe that \(2(1+\rho_\beta)^{-\beta}-1=0\). The exact equality condition is as stated. For \(0<\beta\le1\), every \(0<r<1\) satisfies \(\beta r<1\), and \(2(1+r)^{-\beta}-1>0\).

**Exactly two incipient zero products.** If \(\rho_\beta<r<1/\beta\), strict angular monotonicity continues to hold. At \(\theta=0\) the kernel is positive, whereas at \(\theta=\pi\) it is negative. Thus there is exactly one zero on the upper semicircle and, by reflection, exactly one on the lower semicircle. They cannot occur on the positive or negative real radius.

**Sharp opening law.** Put \(\varepsilon=r-\rho_\beta\) and \(\theta=\pi-\delta\). Taylor expansion at the point \((\rho_\beta,0)\) of the real-analytic expression \(2\operatorname{Re}(1+r e^{-i\delta})^{-\beta}-1\) gives
\[
-\frac{\beta}{1+\rho_\beta}\varepsilon
+\frac{\beta\rho_\beta(1-\beta\rho_\beta)}{2(1+\rho_\beta)^2}\delta^2
+O_\beta(\varepsilon^2+|\varepsilon|\delta^2+\delta^4).
\]
The coefficient of \(\delta^2\) is positive. The analytic implicit-function theorem in \(\delta^2\) therefore yields \(\delta^2=2(1+\rho_\beta)\varepsilon/[\rho_\beta(1-\beta\rho_\beta)]+O_\beta(\varepsilon^2)\), and taking the positive square root proves the displayed law and the claimed error term.

## Verification
All equalities and inequalities above are symbolic, valid for the stated continuous ranges. `CHECKER.py` independently evaluates the angular derivative, the first zero product, and the predicted square-root scaling at multiple parameter values using standard-library arithmetic. It is a diagnostic supplement rather than an exhaustive or infinite proof. Run `python3 CHECKER.py` with Python 3.9 or later.

## Relationship to prior work
El Aïdi's 2023 weighted harmonic Bergman interpolation article supplies the natural reproducing-kernel and interpolation context, but its main theorem is a sufficient sequence-interpolation criterion, not a zero-locus classification. The related 2025 radially weighted interpolation article likewise discusses interpolation rather than this sharp planar kernel sign threshold. Miao's 1998 paper treats harmonic Bergman reproducing kernels on balls; it is a potential historical antecedent for the kernel representation, but no accessible complete text was available to settle priority for the precise radial zero threshold and square-root onset. Higher-dimensional fixed-weight real harmonic-kernel nodal analyses have different objects and do not imply the planar all-weight result.

## Limitations
The sharp threshold is for the scalar product \(|z\overline w|\), not separately for each site, and the nodal pair count is proved only for \(\rho_\beta<r<1/\beta\); no complete outer-radius nodal census is claimed. The \(\beta\le1\) regime is a coefficient-defined harmonic kernel and not a weighted area Bergman norm. Kernel off-diagonal vanishing does not imply singularity of Gram matrices of distinct evaluations. Historical priority is best-knowledge and remains subject to comparison with inaccessible older kernel literature. No independent mathematical audit has been performed.

## References
- M. El Aïdi, *On an Interpolation Problem for the Classical Weighted Harmonic Bergman Space*, first publicly published 12 December 2023, https://doi.org/10.1007/s11785-023-01446-5.
- M. El Aïdi, *On an interpolation problem on a class of a radially weighted harmonic Bergman space*, published 20 August 2025, https://doi.org/10.1186/s13660-025-03304-8.
- J. Miao, *Reproducing kernels for harmonic Bergman spaces of the unit ball*, Monatshefte Math. 125 (1998), 25–35, https://doi.org/10.1007/BF01489456.
