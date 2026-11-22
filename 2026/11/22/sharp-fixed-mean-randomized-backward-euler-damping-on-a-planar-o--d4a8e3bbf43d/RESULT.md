# Sharp fixed-mean randomized backward-Euler damping on a planar oscillator

## Finding
Let \(a>0\), \(b\ge0\), and consider the real planar linear system with generator
\[
A=\begin{pmatrix}-a&-b\\b&-a\end{pmatrix}.
\]
For any nonnegative random step \(H\), independent of the current vector, with finite prescribed mean \(\mathbb EH=h>0\), one backward-Euler stage acts as \(Z^+=(I-HA)^{-1}Z\). Define the sharp squared-norm amplification \(q(a,b,h)=\inf_{\mathbb EH=h}\mathbb E\|Z^+\|_2^2/\|Z\|_2^2\) for nonzero deterministic \(Z\). The infimum ranges over **all Borel laws supported on \([0,\infty)\)**; no moment condition beyond the prescribed mean is needed.

Put \(r=\sqrt{a^2+b^2}\). If \(b\le\sqrt3\,a\), then
\[
q(a,b,h)=\frac1{1+2ah+r^2h^2},
\]
and the **unique** optimal step law is the deterministic step \(H=h\).

If \(b>\sqrt3\,a\), put \(h_*=(r-2a)/r^2>0\). Then the complete solution is
\[
q(a,b,h)=\begin{cases}
1-\dfrac{r^2h}{2(r-a)},&0<h<h_*,\\[5pt]
\dfrac1{1+2ah+r^2h^2},&h\ge h_*.
\end{cases}
\]
For \(0<h<h_*\), the **unique** minimizing law has \(\mathbb P(H=h_*)=h/h_*\) and \(\mathbb P(H=0)=1-h/h_*\). For \(h\ge h_*\) the unique minimizing law is \(H=h\). At \(h=h_*\) both descriptions agree. If instead \(H>0\) almost surely is required, the same infimum holds but is **not attained** for \(b>\sqrt3a\) and \(0<h<h_*\); it is approached by strictly positive two-point laws.

The strict improvement by randomized step selection is therefore possible exactly for \(b>\sqrt3a\) and \(0<h<h_*\). For example, \(a=1\), \(b=\sqrt{99}\), \(h=1/25\) has \(h_*=2/25\): an equal mixture of \(H=0\) and \(H=2/25\) gives squared-norm amplification \(7/9\), versus \(25/31\) for the deterministic mean step.

## Assumptions and scope
The oscillator is autonomous, linear and strictly damped, with Euclidean norm. Each backward-Euler stage is computed exactly. The criterion is the **expected squared norm after one attempted stage at a fixed mean duration**, not error at a fixed deterministic physical time, and not overall computational cost. Zero-duration stages are allowed in the attaining class and can be interpreted as skipped updates; the strictly-positive class is treated separately. In repeated-step statements the step lengths are independent and identically distributed and independent of the initial vector. The result is valid for all \(a>0\), \(b\ge0\), \(h>0\) and all admissible distributions, including unbounded and discrete laws.

## Proof
Write \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), so \(A=-aI+bJ\), \(J^T=-J\), and \(J^TJ=I\). Hence for every \(t\ge0\),
\[
(I-tA)^T(I-tA)=\bigl((1+at)^2+b^2t^2\bigr)I.
\]
Therefore for every deterministic nonzero \(Z\),
\[
\frac{\mathbb E\|Z^+\|^2}{\|Z\|^2}=\mathbb E f(H),\qquad f(t)=\frac1{1+2at+r^2t^2}.
\]
The scalar reduction is exact in every initial direction. Direct differentiation gives
\[
f''(t)=\frac{2(3r^4t^2+6ar^2t+4a^2-r^2)}{(1+2at+r^2t^2)^3}.
\]
If \(r\le2a\), equivalently \(b^2\le3a^2\), this is nonnegative for all \(t\ge0\), and strictly positive for \(t>0\). Strict Jensen (including possible mass at zero) proves that the unique fixed-mean minimizer is \(H=h\).

Suppose \(r>2a\), set \(s=(r-2a)/r^2\), and introduce the affine function
\[
L(t)=1-\frac{r^2t}{2(r-a)}.
\]
The exact algebraic identity
\[
f(t)-L(t)=\frac{t(2a+r^2t-r)^2}{2(r-a)(1+2at+r^2t^2)}\ge0 \quad(t\ge0)
\]
has equality **only** at \(t=0\) and \(t=s\). In particular, \(L(s)=f(s)\), \(L'(s)=f'(s)\), and
\[
3r^4s^2+6ar^2s+4a^2-r^2=2(r-a)(r-2a)>0.
\]
The numerator of \(f''(t)\) is increasing for \(t\ge0\), so \(f\) is strictly convex on \([s,\infty)\). Consequently the piecewise function \(g(t)=L(t)\) for \(0\le t\le s\), and \(g(t)=f(t)\) for \(t\ge s\), is convex and obeys \(g(t)\le f(t)\) everywhere. For arbitrary admissible \(H\),
\[
\mathbb E f(H)\ge\mathbb E g(H)\ge g(\mathbb EH)=g(h).
\]
If \(h<s\), the claimed Bernoulli law attains the bound. Equality forces support in \([0,s]\) by strict convexity beyond \(s\), and support on the zero set \(\{0,s\}\) of \(f-g\); the mean then uniquely fixes the two masses. If \(h>s\), strict convexity of \(g\) at and beyond \(s\) forces deterministic \(H=h\), and at \(h=s\) the same conclusion follows from its mean and equality support. This proves the complete attainment and uniqueness classification.

For \(H>0\) a.s. and \(h<s\), the optimal law cannot be attained because it requires positive mass at zero. However, for any \(\varepsilon\in(0,h)\), take \(H\in\{\varepsilon,s\}\) with \(\mathbb P(H=s)=(h-\varepsilon)/(s-\varepsilon)\). This is strictly positive, has mean \(h\), and its objective tends to \(g(h)\) as \(\varepsilon\downarrow0\). For independent, identically distributed stages, scalar norm amplification gives \(\mathbb E\|Z_n\|^2=(\mathbb E f(H))^n\|Z_0\|^2\) by conditioning; no random physical-time claim follows.

## Verification
The standalone \(\texttt{verify.py}\) re-derives the exact tangent-gap identity, the derivative and tangency conditions using symbolic algebra, checks the exact rational example, and tests the derived global lower bound on 16,000 independently generated finite-support laws. Execute \(\texttt{python verify.py}\) with Python 3.9 or later and SymPy installed. The machine checks are supplementary: the proof above covers arbitrary Borel laws and does not rely on the finite trials.

## Relationship to prior work
Abdulle and Garegnani (arXiv:1801.01340, first submitted January 4, 2018) study random time-step Runge–Kutta schemes, with positive steps and a variance scaling used to maintain deterministic solver convergence. Their global weak and mean-square convergence theorems do not optimize a fixed-mean one-step damping functional over unrestricted step distributions. Eisenmann, Kovács, Kruse and Larsson (arXiv:1709.01018, first submitted September 4, 2017) randomize the **evaluation time of the vector field** at a fixed backward-Euler step, which for autonomous equations reduces to deterministic backward Euler. That is different from choosing a random step length. Closely related publicly indexed results concern implicit-midpoint scalar two-scale optimization, implicit-midpoint isotropization and random-step symplectic Euler; they do not imply the present backward-Euler complex-mode convex-envelope criterion. The general convex-envelope/Jensen method is classical and is not claimed as new; the contribution is the complete exact oscillation/damping threshold, optimizer and boundary nonattainment for this numerical integrator.

## Limitations
The result optimizes damping of numerical iterates, **not** accuracy of an approximation at fixed physical time. A zero-duration update can be omitted without computation, so the theorem does not imply a cost-normalized solver improvement. The fixed-mean laws need not satisfy small-variance assumptions of probabilistic numerical convergence theory; this is not a convergence-order theorem. No extension to nonnormal generators, nonlinear systems, adaptive timestepping or coupled stage lengths is established. Publication priority could be affected by older, differently phrased optimal-distribution results not found in the inspected sources.

## References
1. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340v1 (2018), https://arxiv.org/abs/1801.01340.
2. M. Eisenmann, M. Kovács, R. Kruse and S. Larsson, *On a randomized backward Euler method for nonlinear evolution equations with time-irregular coefficients*, arXiv:1709.01018v1 (2017), https://arxiv.org/abs/1709.01018.
