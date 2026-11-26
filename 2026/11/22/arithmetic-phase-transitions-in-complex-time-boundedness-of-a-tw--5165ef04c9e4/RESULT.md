# Exact onset of imaginary-time slice periodicity for two-rate Gaussian semigroups

## Finding

Let \(1<p<\infty\), \(p\ne2\), and \(0<a<b\) with \(a/b\notin\mathbb Q\). On complex \(L^p(\mathbb R^2,\gamma_1\otimes\gamma_1)\), where \(\gamma_1\) is standard Gaussian probability measure, let
\[
L_{a,b}=a(-\partial_x^2+x\partial_x)+b(-\partial_y^2+y\partial_y).
\]
Define \(e^{-zL_{a,b}}\) first on the Hermite polynomial span, multiplying its basis element of bidegree \((j,k)\) by \(e^{-z(aj+bk)}\). At a fixed positive real time \(t\), let \(S_t\) consist of the \(s\in\mathbb R\) for which \(e^{-(t+is)L_{a,b}}\) extends boundedly. Write \(\operatorname{Per}(S_t)=\{\tau\in\mathbb R:S_t+\tau=S_t\}\). Put
\[
\kappa_p=\frac{2\sqrt{p-1}}{|p-2|},\qquad t_c=\frac{\operatorname{arsinh}(1/\kappa_p)}{c}\quad(c=a,b).
\]
Then the exact group of translations of the slice is
\[
\boxed{\operatorname{Per}(S_t)=\begin{cases}
\{0\},&0<t<t_b,\\
(\pi/a)\mathbb Z,&t_b\le t<t_a,\\
\mathbb R,&t\ge t_a.
\end{cases}}
\]
In the last regime \(S_t=\mathbb R\). In the middle regime the least positive period is \(\pi/a\), despite the incommensurability of the two rates. Thus a two-dimensional boundedness region without any nonzero imaginary translation can have nontrivially periodic fixed-real-time sections.

## Proof

By Epperson's one-dimensional theorem, the Gaussian Hermite multiplier at \(w\) is bounded precisely for \(|\sin(\operatorname{Im}w)|\le\kappa_p\sinh(\operatorname{Re}w)\), with norm one there [1,2]. On tensor Hermite polynomials, the two-rate operator is the product of the one-dimensional multipliers at \(az\) and \(bz\). Fubini gives a bounded extension when both factors are contractive. Conversely the restrictions to functions of either coordinate separately force both factors to be bounded. Consequently
\[
 S_t=\{s:|\sin(as)|\le\kappa_p\sinh(at),\quad |\sin(bs)|\le\kappa_p\sinh(bt)\}.
\]

Let \(u_c=\min(1,\kappa_p\sinh(ct))\) and \(I_c=\{\theta\in\mathbb R/\pi\mathbb Z:|\sin\theta|\le u_c\}\). Write \(F=\mathbf1_{I_a\times I_b}\). For \(0<t<t_b\) both windows are proper arcs of positive length, and \(\mathbf1_{S_t}(s)=F(as,bs)\) on the torus. Suppose \(\tau\) is a period of \(S_t\) and set \(w=(a\tau,b\tau)\bmod\pi\). The function \(F(\theta+w)-F(\theta)\) vanishes along the dense line \((as,bs)\bmod\pi\). It is locally constant off the boundaries of the two product sets, a closed set of Haar measure zero, and therefore vanishes almost everywhere. Integrating over the second coordinate and over the first coordinate, respectively, shows that each circle window is invariant almost everywhere under its own component of \(w\).

A proper arc \([-\delta,\delta]\) modulo \(\pi\), with \(0<\delta<\pi/2\), has nonzero first Fourier coefficient \(\sin(2\delta)/\pi\) for the character \(e^{2i\theta}\) in normalized Haar measure. Almost-everywhere invariance of its indicator under a translation therefore forces that translation to be zero modulo \(\pi\). Thus both \(a\tau\) and \(b\tau\) are in \(\pi\mathbb Z\), and irrationality gives \(\tau=0\).

For \(t_b\le t<t_a\), the \(b\)-window is the full circle and the \(a\)-window is still a proper arc of positive length. Invariance of the preimage under a shift is equivalent to invariance of the \(a\)-window under rotation by \(a\tau\), since \(s\mapsto as\bmod\pi\) is onto. This yields exactly \((\pi/a)\mathbb Z\). At and above \(t_a\) both inequalities hold for every \(s\). Saturation includes equality because the starting criterion is for boundedness, not just the open holomorphy domain.

## Prior work and scope

Complex Gaussian hypercontractivity supplies the boundedness test, while the cited two-rate result [3] already gives the intersection formula, its exact irrational density, the rational-versus-irrational small-time density exponent, and the imaginary-translation group of the **whole** boundedness region. Those are background, not claims of originality here. A trivial translation group of the whole region does not determine the symmetry group of any one slice. The new question is when a fixed-real-time section first becomes periodic and what its full translation group is; establishing the first regime requires ruling out accidental periods of the intersection, not just identifying the periods shared by the individual sine conditions. Historical priority beyond the inspected results is not asserted.

The claim concerns bounded extension on a product Gaussian space at positive real time for two positive incommensurate diagonal rates. It does not classify rational-ratio slices, non-diagonal drift, or finite-window discrepancy. The verification is analytic; density sampling does not test the absence of exact periods.

## References

1. J. B. Epperson, *The hypercontractive approach to exactly bounding an operator with complex Gaussian kernel*, J. Funct. Anal. **87** (1989), 1–30. https://doi.org/10.1016/0022-1236(89)90002-5
2. M. A. Perelmuter, *Semigroups with periodic complex-time boundedness and holomorphy regions*, arXiv:2611.15455v1, §§1.2 and 3.1. https://arxiv.org/html/2611.15455v1
3. *Arithmetic contact and density laws for two-rate Gaussian semigroups*, Finding and proof §§1–3. https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-arithmetic-contact-and-density-laws-for-two-rate-gaussian-semigr--c2e28fd7da99/RESULT.md
