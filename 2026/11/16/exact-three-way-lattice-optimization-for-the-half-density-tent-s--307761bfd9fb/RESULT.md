# Exact three-way lattice optimization for the half-density tent spline in the first-alias regime

## Finding
Let \(g(t)=(1-|t-1|)_+\), and put \(a=1/(2b)\). In the range \(0<b\le 3/4\), the rectangular Gabor system \(\mathcal G(g,a,b)\) is a frame precisely for \(b>1/4\). The exact optimal frame bounds are
\[
A=\begin{cases}a(2-a)^2,&1/4<b\le1/2,\\2(1-d)\min\{(1+d)^2/2,4/5\},&1/2\le b\le3/4,\end{cases}
\quad
B=\begin{cases}2a,&1/4<b\le1/2,\\2(1-d)(1+4d^2),&1/2\le b\le3/4,\end{cases}
\]
where \(d=1-a\in[0,1/3]\) in the second range. At \(b=1/2\) both branches give \(A=1\) and \(B=2\).

Among all frame lattices with \(b\le3/4\), the **unique condition-number minimizer** is
\[
(a,b)=(3/4,2/3),\qquad A=75/64,\quad B=15/8,\quad \min B/A=8/5.
\]
The **unique upper-bound minimizer** is \((a,b)=(5/6,3/5)\), with \(B=50/27\). The **unique lower-bound maximizer** is \(a=2-\sqrt{8/5}\), \(b=1/(2a)\), with \(A=(8/5)(2-\sqrt{8/5})\). All three optimizing lattices differ.

## Assumptions and scope
The window is the integral-one, order-two cardinal B-spline supported on \([0,2]\); translating it to the centered hat does not change any frame bound. All \(b\) are positive real, \(ab=1/2\), and the time-frequency shifts use modulation \(e^{2\pi i mbt}\). The lower/upper bounds are respectively the largest/smallest constants in
\[
A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i mb(\cdot)}g(\cdot-na)\rangle|^2\le B\|f\|_2^2
\]
for every \(f\in L^2(\mathbb R)\). No window or frame-operator normalization is inserted. The restriction \(b\le3/4\) is structural: the Zak period \(L=1/b\) is at least \(4/3\); up to its endpoint, at most one of the two half-density Zak channels has overlapping window replicas. The next regime has simultaneous alias overlap, and is not covered by these formulas.

## Proof
**1. Exact two-channel diagonalization.** Set \(L=1/b=2a\) and define the unnormalized Zak sum
\[
Z_Lg(x,\theta)=\sum_{k\in\mathbb Z}g(x+kL)e^{ik\theta}.
\]
Unitarity of the Zak transform, Parseval over the modulation lattice, and the two cosets of the translation lattice modulo \(L\) give the exact frame-operator multiplier
\[
H(x,\theta)=L\bigl(|Z_Lg(x,\theta)|^2+|Z_Lg(x+a,\theta)|^2\bigr),\qquad 0\le x\le a,\quad0\le\theta\le2\pi.
\]
This is the scalar \(q=2\) Zibulski--Zeevi representation. The window is continuous and compactly supported, so its continuous fiber extrema are exactly the optimal essential lower and upper bounds.

**2. Non-overlapping Zak replicas.** If \(1/4<b\le1/2\), then \(1\le a<2\) and \(L=2a\ge2\), so every Zak sum has at most one nonzero term. Translation-periodic reduction gives
\[
H(x,\theta)=2a\sum_{n\in\mathbb Z}g(x-na)^2.
\]
Over any period, the sum of the squared tents has maximum \(1\), attained at a tent peak, and minimum \((2-a)^2/2\), attained halfway between adjacent peaks. This yields \(B=2a\) and \(A=a(2-a)^2\). If \(b\le1/4\), then \(a\ge2\). For \(a>2\), adjacent tent supports leave intervals of positive measure with no time-translated window. At \(a=2\), the supports just touch, and the squared sum has essential infimum zero. Hence no frame exists.

**3. First Zak-alias regime.** For \(1/2\le b\le3/4\), write \(d=1-a\in[0,1/3]\); then \(L=2(1-d)\). Explicitly summing every nonzero translate, for \(0\le x\le a\) one obtains
\[
Z_Lg(x,\theta)=x+(2d-x)_+e^{i\theta},\qquad
Z_Lg(x+a,\theta)=\begin{cases}1-d+x,&0\le x\le d,\\1+d-x,&d\le x\le a.\end{cases}
\]
Both coefficients in the first expression are nonnegative, so, at fixed \(x\), its maximum/minimum modulus occurs at \(\theta=0\) or \(\theta=\pi\), respectively; the second channel does not depend on phase.

For the maximum, on \([0,d]\) the first channel at phase zero equals \(2d\) and the second increases to \(1\). On \([d,2d]\) the first channel remains \(2d\) and the second decreases from \(1\). On \([2d,a]\) the sum of squared channels is \(x^2+(1+d-x)^2\), a convex quadratic; its endpoint maxima do not exceed \(1+4d^2\). Thus
\[
\max_{x,\theta}H/L=1+4d^2,
\]
with equality at \(x=d,\theta=0\) (and at other fibers in a boundary case).

For the minimum, the phase-\(\pi\) sum of squares is
\[
\frac{H(x,\pi)}L=
\begin{cases}
4(x-d)^2+(1-d+x)^2,&0\le x\le d,\\
4(x-d)^2+(1+d-x)^2,&d\le x\le2d,\\
x^2+(1+d-x)^2,&2d\le x\le a.
\end{cases}
\]
The last quadratic has its minimum \((1+d)^2/2\) at \(x=(1+d)/2\), which belongs to \([2d,a]\) since \(0\le d\le1/3\). The first two quadratics have critical points \(x=d-1/5\) and \(x=d+1/5\) in their respective closed intervals precisely when \(d\ge1/5\); both have value \(4/5\). For \(0\le d<1/5\), the first is minimized at \(x=0\) and the second at \(x=2d\); both minima equal \(1-2d+5d^2\), which exceeds \((1+d)^2/2\) by \((1-3d)^2/2\). Thus the global minimum is
\[
\min_{x,\theta}H/L=\min\{(1+d)^2/2,4/5\}.
\]
Multiplication by \(L=2(1-d)\) proves the two exact bounds, including their endpoint normalizations.

**4. Optimization over the entire low-alias family.** On \(1/4<b\le1/2\), \(B/A=2/(2-a)^2\ge2\), with equality only at \(b=1/2\). In \(0\le d\le1/3\), the lower-bound branch changes exactly at \(d_*=\sqrt{8/5}-1\), with \(1/4<d_*<1/3\). The condition number equals
\[
\kappa(d)=\begin{cases}
2(1+4d^2)/(1+d)^2,&0\le d\le d_*,\\
(5/4)(1+4d^2),&d_*\le d\le1/3.
\end{cases}
\]
On the first branch the derivative has the sign of \(4d-1\); on the second branch it is strictly positive except at zero, which lies outside that branch. Thus the unique minimum is at \(d=1/4\), giving \(\kappa=8/5\) and the stated sharp bounds.

The lower bound \(A=(1-d)(1+d)^2\) for \(d\le d_*\) is strictly increasing up to the crossover (derivative \((1+d)(1-3d)>0\)); the other branch \(A=(8/5)(1-d)\) strictly decreases thereafter. Its maximum is thus uniquely at \(d_*\). The upper bound \(B=2(1-d)(1+4d^2)\) has derivative \(2(-1+8d-12d^2)\) and its unique minimum on \([0,1/3]\) occurs at \(d=1/6\), with value \(50/27\). Earlier non-overlapping lattices have \(A\le1\) and \(B\ge2\), so neither improves these optima. This exhausts the promised parameter range.

## Verification
The standalone, standard-library-only script `CHECK.py` computes the finite Zak sums directly, checks the derived continuous-envelope formulas at rational and nonrational parameters, and compares the exact optimizer identities with a rational parameter mesh. In particular, it verifies the rational identities \(A(3/4,2/3)=75/64\), \(B(3/4,2/3)=15/8\), \(B(5/6,3/5)=50/27\), and \(\kappa=8/5\). Its finite checks are supplementary: the proof above establishes every real-parameter statement and uniqueness without discretization.

## Relationship to prior work
Stangl--Frederick (arXiv:2609.00481; first public August 31, 2026) and Hasannasab--Lemvig (arXiv:2609.13116; September 11, 2026) characterize qualitative Gabor frame membership for hat splines using Zak-zero methods. The accessible Stangl--Frederick theorem treats the different modulation range \(b\ge3/2\) and does not imply the sharp quantitative bounds for \(b\le3/4\). Faulhuber--Shafkulovska (arXiv:2204.02917, *Appl. Comput. Harmon. Anal.* 67 (2023)) analyze the three optimization objectives for other windows, without a triangular B-spline result. A published note, *Sharp Gabor frame bounds and quadratic collapse for the hat spline at half-density* (October 2026), gives an exact branch for \(3/2\le b\le7/4\); its full displayed proof is likewise outside the present range. Qualitative frame membership and the classical two-channel Zak representation are **not claimed as new**. The contribution here is the first-alias quantitative spectrum and the explicit three different optimizers.

## Limitations
This result covers only rectangular lattices \(ab=1/2\), the fixed normalized-height triangular window, and \(0<b\le3/4\). It makes no global lattice-optimization claim beyond that region, and no claim for other spline orders or general lattice shapes. An otherwise relevant September 2026 Zak-zero paper was accessible only through its abstract; full-text quantitative coverage in older specialized literature remains a publication-priority risk. The standalone numerical checks are not independent verification.

## References
1. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (first public 2026-08-31). https://arxiv.org/abs/2609.00481
2. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (2026). https://arxiv.org/abs/2609.13116
3. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, *Appl. Comput. Harmon. Anal.* 67 (2023), 101574; preprint arXiv:2204.02917. https://arxiv.org/abs/2204.02917
4. *Sharp Gabor frame bounds and quadratic collapse for the hat spline at half-density*, publicly available scientific note, October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-gabor-frame-bounds-and-quadratic-collapse-for-the-hat-spli--c8f151d17e5c
5. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, *Appl. Comput. Harmon. Anal.* 4 (1997), 188--221.
