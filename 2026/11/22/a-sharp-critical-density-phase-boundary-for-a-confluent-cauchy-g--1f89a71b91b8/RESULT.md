# A sharp critical-density phase boundary for a confluent Cauchy Gabor window

## Finding
Fix \(a>0\) and a real parameter \(\lambda\). Define the rational window
\[
 g_{a,\lambda}(t)=\frac{1}{t+ia}+\frac{\lambda}{(t+ia)^2},\qquad t\in\mathbb R,
\]
and its integer-critical Gabor system
\[
 \mathcal G_{a,\lambda}=\{e^{2\pi i mt}g_{a,\lambda}(t-n):m,n\in\mathbb Z\}.
\]
Let
\[
 \lambda_c(a)=\frac{\sqrt{e^{4\pi a}-1}}{2\pi}.
\]
Then \(\mathcal G_{a,\lambda}\) is a frame, equivalently a Riesz basis, for \(L^2(\mathbb R)\) **if and only if** \(|\lambda|<\lambda_c(a)\). At either boundary value the Zak multiplier has a unique zero on the one-sided frequency boundary, and beyond the boundary it has exactly one simple zero in the open Zak cell. For every real \(\lambda\), including nonframe parameters, the system is complete and Bessel.

For the optimal squared lower frame bound \(A(a,\lambda)\) on the stable side, the sharp collapse is
\[
 \boxed{\lim_{|\lambda|\uparrow\lambda_c(a)}\frac{A(a,\lambda)}{\bigl(1-|\lambda|/\lambda_c(a)\bigr)^2}=4\pi^2.}
\]
The limiting coefficient is independent of the pole height \(a\). The statement gives a window-parameter boundary for the **fixed critical lattice**, not a classification of noncritical lattice frame sets.

## Assumptions and scope
The parameter \(a\) is any strictly positive real number and \(\lambda\in\mathbb R\). The window is not energy-normalized. A squared Gabor frame bound means a constant in
\[
 A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}\big|\langle f,e^{2\pi i mt}g_{a,\lambda}(\cdot-n)\rangle\big|^2\le B\|f\|_2^2
 \qquad(f\in L^2(\mathbb R)).
\]
When no positive lower bound exists, set \(A=0\). The critical Zak transform is defined in \(L^2\) by \(Zg(x,\omega)=\sum_{k\in\mathbb Z}g(x+k)e^{-2\pi i k\omega}\) for \(0<x,\omega<1\). Its frequency-boundary values below are always **one-sided limits**, not necessarily values of the conditionally convergent endpoint Fourier series. Completeness means the closed linear span of the Gabor system is the whole space; it does not assert stable reconstruction when \(A=0\).

## Proof
**1. Exact Zak multiplier.** For \(z=x+ia\) and \(0<\omega<1\), the classical partial-fraction identity is
\[
 \sum_{k\in\mathbb Z}\frac{e^{-2\pi i k\omega}}{z+k}
 =\frac{\pi e^{\pi iz(2\omega-1)}}{\sin(\pi z)}.
\]
The identity holds in the Zak \(L^2\) sense; differentiation in \(z\) is justified for the absolutely summable squared-denominator series. Differentiation and the minus sign in \(\partial_z(z+k)^{-1}=-(z+k)^{-2}\) yield
\[
 Zg_{a,\lambda}(x,\omega)=Z_1(x,\omega)\,F_{a,\lambda}(x,\omega),
\]
\[
 Z_1(x,\omega)=\frac{\pi e^{\pi i(x+ia)(2\omega-1)}}{\sin\pi(x+ia)},
 \qquad F_{a,\lambda}(x,\omega)=1+\pi\lambda\bigl(\cot\pi(x+ia)-i(2\omega-1)\bigr).
\]
Both factors have bounded one-sided continuous extensions to the compact rectangle \([0,1]\times[0,1]\), and \(Z_1\) has no zero. Standard critical-density Zak diagonalization identifies the Gabor frame operator with multiplication by \(|Zg|^2\); the optimal squared bounds are its essential infimum and supremum. This also establishes the Bessel property.

**2. The exact zero/no-zero boundary.** Put \(h=2\pi a\), \(C=\coth h\), \(R=\operatorname{csch}h\). The circle parametrized by \(c(x)=\cot\pi(x+ia)\), \(0\le x\le1\), has center \(-iC\), radius \(R\), and \(C^2-R^2=1\). Its upper arc lies above \(\operatorname{Im}c=-1\) precisely for
\[
 |\operatorname{Re}c|\le M,\qquad
 M=\sqrt{R^2-(C-1)^2}=\sqrt{2(C-1)}=\frac{2}{\sqrt{e^{4\pi a}-1}}.
\]
For \(\lambda\ne0\), the zero equation \(F_{a,\lambda}=0\) is equivalent to
\[
 \operatorname{Re}c(x)=-\frac1{\pi\lambda},
 \qquad 2\omega-1=\operatorname{Im}c(x).
\]
The imaginary part of \(c(x)\) is always negative, so the admissible frequency strip corresponds exactly to the upper circle arc. The real part takes every value in \([-M,M]\) once on that arc, with equality only on the one-sided boundary \(\omega=0\). Therefore zeros in the **closed one-sided cell** occur exactly when
\[
 |\lambda|\ge\frac1{\pi M}=\lambda_c(a).
\]
For strict inequality \(|\lambda|>\lambda_c(a)\), the corresponding zero is unique and lies inside the cell; its real two-dimensional Jacobian is nonsingular because \(\partial_\omega F=-2\pi i\lambda\ne0\) while \(\partial_x\operatorname{Re}F\ne0\) on the exposed arc. At equality the only zero is on \(\omega=0\). For \(\lambda=0\) there are no zeros. Continuity and compactness prove the stated if-and-only-if frame criterion. Since the multiplier has at most one zero in the open cell and no identically vanishing fiber, it is nonzero almost everywhere for every \(\lambda\). The critical Zak characters multiplied by a nonzero-almost-everywhere symbol have dense span, giving completeness, even beyond the frame boundary. At density one, a Gabor frame is a Riesz basis by the same Zak equivalence.

**3. Nondegenerate boundary geometry and sharp constant.** By reflection \(x\mapsto1-x\), the squared Zak modulus at \(-\lambda\) has the same range as at \(\lambda\); it suffices to let \(\lambda\uparrow\lambda_c(a)\) through positive values. Set \(\delta=\lambda_c(a)-\lambda>0\), and let \(x_*\in(1/2,1)\) be the unique solution
\[
 \cot\pi(x_*+ia)=-M-i.
\]
At this point the critical zero occurs at the one-sided coordinate \(\omega=0\). A direct evaluation gives
\[
 |Z_1(x_*,0)|^2=\frac{4\pi^2}{1-e^{-4\pi a}}.
\]
Using \(\partial_x\cot\pi z=-\pi(1+\cot^2\pi z)\), \(\pi\lambda_c M=1\), and the Taylor expansion in \(X=x-x_*\), \(\omega\ge0\), we obtain
\[
 F_{a,\lambda}(x,\omega)
 =\pi M\delta-\pi(M+2i)X-\frac{2i}{M}\omega
 +O_a\bigl((|X|+\omega+\delta)^2\bigr).
\]
The real-linear map in \((X,\omega)\) has nonzero Jacobian (its real and imaginary components are independent), so at \(\delta=0\) the zero is isolated and coercive. Compactness away from it and a trial point with \(|F|=O_a(\delta)\) force every global minimizer for small \(\delta\) to satisfy \(|X|+\omega=O_a(\delta)\). Consequently its squared-leading-order minimization reduces rigorously to the half-plane quadratic problem
\[
 \min_{X\in\mathbb R,\ \omega\ge0}
 \left|\pi M\delta-\pi(M+2i)X-\frac{2i}{M}\omega\right|^2.
\]
This strictly convex expression is minimized at
\[
 \omega=0,\qquad X=\frac{M^2\delta}{M^2+4},
\]
and has value \(4\pi^2M^2\delta^2/(M^2+4)\). The neglected terms contribute \(o_a(\delta^2)\) uniformly along such minimizers. As
\[
 \frac{M^2}{M^2+4}=e^{-4\pi a},\qquad
 \lambda_c(a)^2=\frac{1-e^{-4\pi a}}{4\pi^2e^{-4\pi a}},
\]
multiplication by \(|Z_1(x_*,0)|^2\) gives
\[
 A(a,\lambda)=4\pi^2\bigl(\delta/\lambda_c(a)\bigr)^2
 +o_a(\delta^2).
\]
This proves the height-independent sharp quadratic coefficient on both sides.

## Verification
Run `python3 checker.py` from this directory, using only the Python standard library. The program tests the explicit Zak identity against truncated lattice sums, the cotangent circle geometry, predicted zero locations, and the small-defect lower-bound coefficient at several pole heights. The recorded run printed `PASS 188 finite formula/circle/root/onset/truncation checks`. These finite tests cannot prove the all-parameter theorem; the proof is the analytic Zak-circle argument and the constrained local minimization above.

## Relationship to prior work
Belov, Kulikov, and Lyubarskii (2021) established critical Gabor frame machinery for rational Cauchy windows, including positive simple-pole mixtures; their paper remarks that repeated poles can be approached with similar methods, but the inspected statements and sections do not give this explicit real confluent-pole threshold or its universal sharp stability coefficient. Their 2022 work treats the **single simple Cauchy pole** and exact critical Zak bounds. The repeated-pole perturbation studied here is a signed derivative-of-pole direction, neither a positive simple-pole measure nor a fixed pair of distinct poles.

Related precise results for signed two-distinct-pole windows establish separate protected stability intervals and optimal lower bounds; those statements assume separated pole heights and do not directly imply the confluent threshold and the height-independent collapse. The use of the Zak transform, circle parametrization, and critical-density frame criterion is classical and not claimed as novel. The candidate contribution is the **complete parameter threshold together with its sharp universal lower-bound onset** for this fixed, natural double-pole perturbation. Historical priority beyond the inspected literature is provisional.

## Limitations
The theorem does not cover complex \(\lambda\), arbitrary higher-order poles, noncritical time-frequency lattices, upper frame-bound optimization, or normalized-by-energy conditioning. Completeness in the nonframe regime gives no uniform stability. The proof supplies an exact asymptotic coefficient but no claimed global closed form for \(A(a,\lambda)\) away from the threshold. No independent external mathematical audit or exhaustive historical priority verification has been performed.

## References
1. Y. Belov, A. Kulikov and Y. Lyubarskii, *Gabor frames for rational functions*, first public 16 March 2021, arXiv:2103.08959, especially Sections 1, 2 and the discussion of multiple poles; *Inventiones mathematicae* 231 (2023), 431–466, DOI: 10.1007/s00222-022-01151-8. https://arxiv.org/abs/2103.08959
2. Y. Belov, A. Kulikov and Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, first public 17 December 2022, arXiv:2212.08915, especially the critical Zak transform and bounds. https://arxiv.org/abs/2212.08915
3. K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser, 2001, Chapter 8 (standard critical Zak criterion).
