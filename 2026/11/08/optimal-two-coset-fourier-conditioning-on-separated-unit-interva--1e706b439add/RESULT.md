# Optimal two-coset Fourier conditioning on separated unit intervals

## Finding

For every integer \(m\ge1\), every \(0<\delta<1\), and \(d=m+\delta\), set
\[
 E_d=[0,1)\cup[d,d+1),\qquad
 \Lambda_\tau=\mathbb Z\cup(\mathbb Z+\tau),\quad 0<\tau<1.
\]
For finite coefficients \(a_k,b_k\in\mathbb C\), let
\[
 F(x)=\sum_{k\in\mathbb Z}a_ke^{2\pi ikx}
       +\sum_{k\in\mathbb Z}b_ke^{2\pi i(k+\tau)x},
 \qquad \|c\|^2=\sum_k(|a_k|^2+|b_k|^2).
\]
Define \(c_m(\tau)=\max\{|\cos(\pi m\tau)|,|\cos(\pi(m+1)\tau)|\}\). The **sharp** Riesz synthesis bounds in unnormalized Lebesgue measure are
\[
 \boxed{(2-2c_m(\tau))\|c\|^2\le\|F\|_{L^2(E_d)}^2
 \le(2+2c_m(\tau))\|c\|^2.}
\]
The system is a Riesz basis if and only if \(m\tau\notin\mathbb Z\) and \((m+1)\tau\notin\mathbb Z\). Among all two-coset shifts, the complete set of optimizers modulo \(1\) is
\[
 \boxed{\tau\equiv\frac1{2m+1}\ \text{or}\ -\frac1{2m+1}\pmod1.}
\]
The smallest attainable \(c_m\) is \(s_m=\sin(\pi/(4m+2))\); hence the best **ratio of upper to lower Riesz bounds** is
\[
 \boxed{\rho_m=\frac{1+s_m}{1-s_m}.}
\]
This ratio is constant as the fractional gap \(\delta\) varies over \((0,1)\). At an *integer* separation \(d=m\), in contrast, the two-coset system is an orthogonal basis for every \(\tau=(2j+1)/(2m)\), \(j=0,\ldots,m-1\), with both sharp bounds equal to \(2\). Thus the optimally conditioned ratio jumps from \(1\) at integer separations to \(\rho_m>1\) immediately to their right. This is a statement about an explicit **two-coset family**, not universal optimality among all frequency sets.

## Assumptions and scope

The domain consists of two disjoint half-open unit intervals with separation \(d>1\), and the norm is with respect to ordinary (not probability-normalized) Lebesgue measure. The frequency set contains two complete integer cosets. The Fourier conventions are \(e_\lambda(x)=e^{2\pi i\lambda x}\). Riesz synthesis inequalities are stated initially for finite sequences and extend by completion to all \(\ell^2(\mathbb Z)^2\). By a Riesz basis we mean a complete Riesz sequence. The condition number of the *synthesis operator* is the square root \(\sqrt{\rho_m}\), while \(\rho_m\) is the ratio of squared Riesz bounds.

## Proof

**Exact fiberization.** Write \(d=m+\delta\) with \(m\in\mathbb Z_{\ge1}\) and \(0<\delta<1\). Put \(A(y)=\sum_k a_ke^{2\pi iky}\), \(B(y)=\sum_k b_ke^{2\pi iky}\). On the first interval the synthesis is \(A(y)+e^{2\pi i\tau y}B(y)\). On the second, every \(x\in[d,d+1)\) is uniquely \(y+n(y)\), where \(0\le y<1\) and
\[
 n(y)=\begin{cases}m+1,&0\le y<\delta,\\m,&\delta\le y<1.\end{cases}
\]
The periodicity of \(A,B\), Parseval, and change of variables give
\[
 \|F\|_{L^2(E_d)}^2=\int_0^1
 \left\|
 \begin{pmatrix}1&e^{2\pi i\tau y}\\
 1&e^{2\pi i\tau(y+n(y))}\end{pmatrix}
 \begin{pmatrix}A(y)\\B(y)\end{pmatrix}
 \right\|_{\mathbb C^2}^2dy,
 \qquad \|c\|^2=\int_0^1(|A|^2+|B|^2)dy.
\]
For any integer \(n\), the matrix above, with \(n(y)=n\), has Gram matrix
\[
 \begin{pmatrix}
 2&e^{2\pi i\tau y}(1+e^{2\pi in\tau})\\
 e^{-2\pi i\tau y}(1+e^{-2\pi in\tau})&2
 \end{pmatrix}.
\]
Its eigenvalues are exactly \(2\pm2|\cos(\pi n\tau)|\). Since each of the two fiber types occupies positive Lebesgue measure, the essential extrema over \(y\) are exactly \(2\pm2c_m(\tau)\). Measurable eigenvectors supported inside either fiber type, approximated in \(L^2\) by finite Fourier sums, establish sharpness rather than merely bounds. The fiber matrix is invertible almost everywhere exactly when \(e^{2\pi im\tau}\ne1\) and \(e^{2\pi i(m+1)\tau}\ne1\). In that case its bounded inverse acts pointwise; the Fourier coefficient isomorphism makes synthesis onto \(L^2(E_d)\), proving completeness and the asserted Riesz-basis criterion. If either phase is \(1\), a positive-measure family of singular fibers prevents a lower Riesz bound.

**Global shift optimization.** The problem is to minimize \(c_m(\tau)\) on \(\tau\in[0,1]\). For \(0\le\varepsilon<1/2\), the pair of inequalities \(|\cos(\pi m\tau)|,|\cos(\pi(m+1)\tau)|\le\sin(\pi\varepsilon)\) is equivalent to the existence of integers \(k,l\) with
\[
 |m\tau-(k+\tfrac12)|\le\varepsilon,
 \qquad |(m+1)\tau-(l+\tfrac12)|\le\varepsilon.
\]
Subtracting gives \(|\tau-(l-k)|\le2\varepsilon\). To rule out \(\varepsilon<\varepsilon_*:=1/(4m+2)\), note that \(\tau\in[0,1]\) and \(2\varepsilon<1/3\) force \(l-k\in\{0,1\}\). If \(l-k=0\), then \(0\le\tau\le2\varepsilon\), while proximity of \(m\tau\ge0\) to a half-integer yields \(m\tau\ge\frac12-\varepsilon\). Thus \(2m\varepsilon\ge\frac12-\varepsilon\), contradicting \(\varepsilon<\varepsilon_*\). The case \(l-k=1\) follows by replacing \(\tau\) with \(1-\tau\), since proximity of \(m\tau\) to a half-integer implies the same for \(m(1-\tau)\). At equality, these inequalities force respectively \(\tau=2\varepsilon_*=1/(2m+1)\) or \(\tau=1-2\varepsilon_*\). Both attain the proposed \(c_m=\sin(\pi\varepsilon_*)\). Therefore the minimax value and all optimizers are exact. Since \((1+c)/(1-c)\) increases strictly for \(0\le c<1\), the same shifts minimize the Riesz-bound ratio.

**Integer-separation boundary.** If \(\delta=0\), the second fiber has only \(n(y)=m\) almost everywhere. Therefore the bounds simplify to \(2\pm2|\cos(\pi m\tau)|\); they are both \(2\) precisely when \(m\tau\) is a half-integer. The discontinuity as \(\delta\downarrow0\) is genuine: the small fiber region \([0,\delta)\) still has positive measure, and the sharp lower bound is an essential infimum, not an average. For the normalized probability measure \(\frac12\mathbf1_{E_d}dx\), all displayed frame bounds are halved and their ratio is unchanged.

## Verification

`CHECK.py` implements exact integration of finite exponential sums, an independent discretized fiber representation, the analytical candidate bounds, and exhaustive-grid/random checks of the minimax inequality for \(1\le m\le8\). Its deterministic run completed with `TWO_INTERVAL_RIESZ_CHECKS_PASSED 14808`. This is a finite consistency check; the infinite-dimensional assertions, sharpness and universal parameter optimization are proved by the preceding fiber and arithmetic arguments. To reproduce, execute `python CHECK.py` with Python 3 standard library; no third-party packages are required.

## Relationship to prior work

The qualitative spectrality distinction is already established by Ting Zhou, *Spectrality of convolution and product measures: a block decomposition approach*, arXiv:2610.33987v1 (2026), Corollary 2.7: the convolution of the uniform unit interval and two equally weighted point masses at separation \(d\) is spectral only when \(d\) is integral. That work does not assert the current exact nonorthogonal Riesz bounds or optimize the two-coset shift.

Multi-tiling Riesz constructions and fiber-matrix criteria are standard and are explicitly acknowledged: M. Kolountzakis (2015); C. Frederick and K. Okoudjou, *Finding duality for Riesz bases of exponentials on multi-tiles* (2021); A. Caragea and D. G. Lee (2021/2022); and Y. Belov and M. Mironov (2022/2024). The present conclusion is not the existence of a two-coset Riesz basis, nor the general fiber method. Its content is the complete sharp arithmetic minimax, two optimal shifts, all exact bounds, and the gap-independent, discontinuous conditioning profile. A general matrix criterion permits this computation but does not itself determine the optimizer or stair-step law. Priority beyond the inspected works is not independently certified.

## Limitations

The optimization is only over frequency sets of the indicated form \(\mathbb Z\cup(\mathbb Z+\tau)\), not all Riesz spectra. It applies to equal-length disjoint intervals; overlapping intervals, unequal lengths, nonuniform weights, and more than two frequency cosets are not classified. The sharp norms are \(L^2\) quantities: they do not imply pointwise robustness or a reconstruction-noise model without additional assumptions. An equivalent computation might have appeared in specialized earlier multi-tile literature under other conventions.

## References

1. Ting Zhou, *Spectrality of convolution and product measures: a block decomposition approach*, arXiv:2610.33987v1, first posted 2026-10-25; Corollary 2.7.
2. Christina Frederick and Kasso Okoudjou, *Finding duality for Riesz bases of exponentials on multi-tiles*, Applied and Computational Harmonic Analysis 51 (2021), 104–117; arXiv:1910.09257.
3. Yurii Belov and Mikhail Mironov, *Exponential Riesz bases in \(L^2\) on two intervals*, International Mathematics Research Notices 2024(7), 5403–5433; arXiv:2212.02313v1.
4. Andrei Caragea and Dae Gwan Lee, *A note on exponential Riesz bases*, arXiv:2110.07988v2 (2021).
5. Mihail N. Kolountzakis, *Multiple lattice tiles and Riesz bases of exponentials*, Proceedings of the American Mathematical Society 143 (2015), 741–747; arXiv:1305.2632.
