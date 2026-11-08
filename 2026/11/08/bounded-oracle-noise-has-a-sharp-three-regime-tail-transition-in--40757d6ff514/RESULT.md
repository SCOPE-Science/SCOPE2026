# Bounded-oracle noise has a sharp three-regime tail transition in two-point Anderson acceleration

## Finding

For fixed distinct scalar inputs to a strict affine contraction, unregularized depth-one Anderson acceleration has a sharp finite-support noise threshold. Below the threshold its one-step output is bounded. At the threshold its output has a quadratic tail (and infinite second moment) except for one exactly symmetric placement of the inputs around the fixed point, where it remains bounded. Above the threshold it has a first-order tail and no finite absolute moment of order at least one, despite bounded independent oracle errors. The leading tail constants and the logarithmic mean-square divergence approaching the threshold from below are explicit.

More precisely, let \(x_0<x_1\), \(\Delta=x_1-x_0>0\), \(\theta\in\mathbb R\), \(0<r<1\), \(k=1-r\), and \(\delta>0\). Observe independently perturbed values \(Y_j=\theta+r(x_j-\theta)+\varepsilon_j\), where \(\varepsilon_0,\varepsilon_1\) are independent uniform random variables on \([-\delta,\delta]\). Set \(f_j=Y_j-x_j\). The unsafeguarded, unregularized depth-one Anderson output \(Z\) is the affine combination of \(Y_0,Y_1\) whose corresponding affine combination of the two residuals vanishes, equivalently
\[
Z=\frac{x_0f_1-x_1f_0}{f_1-f_0}.
\]
The denominator is zero with probability zero.

Write \(a=x_0-\theta\), \(b=x_1-\theta\) and \(\delta_c=k\Delta/2\). Then:

1. If \(0<\delta<\delta_c\), \(Z-\theta\) is bounded, so all its absolute moments are finite. If \(a+b\ne0\), the approach to the threshold satisfies
\[
\lim_{\delta\uparrow\delta_c}\frac{\mathbb E(Z-\theta)^2}{\log\bigl(1/(1-\delta/\delta_c)\bigr)}=\frac{(a+b)^2}{4}.
\]
2. If \(\delta=\delta_c\) and \(a+b\ne0\), then
\[
\lim_{t\to\infty}t^2\Pr(|Z-\theta|>t)=\frac{(a+b)^2}{8}>0,
\]
and \(\mathbb E|Z-\theta|^p<\infty\) exactly for \(0<p<2\). If \(\delta=\delta_c\) and \(a+b=0\), instead \(|Z-\theta|\le|a|\) almost surely, so all absolute moments are finite.
3. If \(\delta>\delta_c\), put
\[
C_{\delta}=\frac{\Delta}{2\delta^2}\int_{-\delta}^{\delta-k\Delta}|ka-z|\,dz>0.
\]
Then \(\lim_{t\to\infty}t\Pr(|Z-\theta|>t)=C_\delta\), and \(\mathbb E|Z-\theta|^p<\infty\) exactly for \(0<p<1\).

## Assumptions and scope

This is a conditional one-step statement for two fixed, distinct inputs. The oracle perturbations are independent, identically distributed *bounded continuous* uniforms, rather than an unbounded Gaussian or an adversarial error. The algorithm uses the ordinary depth-one residual-cancelling affine combination, without coefficient clipping, safeguarding, ridge regularization or damping. It is not a theorem about an entire recursively generated Anderson trajectory. The fixed-point map is scalar and affine; the contraction factor is in \((0,1)\). The input ordering loses no generality since labels can be interchanged.

## Proof

Put \(D=f_1-f_0\) and \(N=a\varepsilon_1-b\varepsilon_0\). Direct cancellation of the exact affine residuals gives
\[
D=-k\Delta+\varepsilon_1-\varepsilon_0,\qquad Z-\theta=\frac ND.
\]
The denominator has an absolutely continuous distribution. Its range is \([-k\Delta-2\delta,-k\Delta+2\delta]\).

**Below the threshold.** For \(2\delta<k\Delta\), \(|D|\ge k\Delta-2\delta>0\) while \(|N|\le\delta(|a|+|b|)\), proving boundedness. For the sharp divergence, set \(s=k\Delta-2\delta>0\), \(u=\varepsilon_0+\delta\) and \(v=\delta-\varepsilon_1\). On the square \([0,2\delta]^2\),
\[
D=-(s+u+v),\qquad N=\delta(a+b)-bu-av.
\]
Consequently
\[
\mathbb E(Z-\theta)^2=\frac1{4\delta^2}\int_0^{2\delta}\!\int_0^{2\delta}\frac{[\delta(a+b)-bu-av]^2}{(s+u+v)^2}\,du\,dv.
\]
As \(s\downarrow0\) and \(\delta\uparrow\delta_c\), the only divergent contribution comes from \(u=v=0\). In a fixed small corner, replacing the numerator by \(\delta_c^2(a+b)^2\) changes the integral by \(O(1)\): the linear difference in the numerator is \(O(u+v+s)\), while the resulting integrable terms are bounded. For any fixed \(L>0\),
\[
\int_0^L\!\int_0^L\frac{du\,dv}{(s+u+v)^2}=\log(1/s)+O_L(1).
\]
The complement of that corner contributes \(O_L(1)\). After division by \(4\delta_c^2\), the coefficient is \((a+b)^2/4\). Using a fixed reference scale inside the logarithm gives the claimed dimensionless limit.

**At the threshold.** Now \(s=0\) in the same coordinates and \(D=-(u+v)\). If \(a+b\ne0\), let \(c=\delta_c(a+b)\ne0\). Near the unique singular corner \((u,v)=(0,0)\), \(N=c+O(u+v)\). For any fixed \(\eta>0\), sufficiently close to the corner \(|N|\) is squeezed between \(|c|-\eta\) and \(|c|+\eta\). The triangle \(u+v<z\) has area \(z^2/2\). Squaring the bounds and dividing by the square area \((2\delta_c)^2\), then letting \(\eta\downarrow0\), proves
\[
\lim_{t\to\infty}t^2\Pr(|N/D|>t)=\frac{c^2}{8\delta_c^2}=\frac{(a+b)^2}{8}.
\]
Away from the corner the quotient is bounded. If \(a+b=0\), then \(N=-bu-av=a(u-v)\), so \(|N|\le|a|(u+v)=|a||D|\), proving the exceptional bounded case.

**Above the threshold.** The zero set of \(D\) crosses the interior of the error square on the segment \(\varepsilon_0=z\), \(\varepsilon_1=z+k\Delta\), with \(-\delta\le z\le\delta-k\Delta\). On that segment,
\[
N=a(z+k\Delta)-bz=\Delta(ka-z).
\]
For fixed \(z\), the allowed interval in \(\varepsilon_1\) in the event \(|N/D|>t\) is, to first order in \(1/t\), an interval centered at \(z+k\Delta\) of length \(2|\Delta(ka-z)|/t\). Boundary clipping affects only a vanishing end strip. By dominated convergence in the coordinates \((z,D)\), using the bounded square and the fact that \(|N|\) is Lipschitz, integration with density \(1/(4\delta^2)\) gives exactly
\[
\lim_{t\to\infty}t\Pr(|N/D|>t)=\frac{\Delta}{2\delta^2}\int_{-\delta}^{\delta-k\Delta}|ka-z|\,dz.
\]
The interval has positive length; its integrand is not zero almost everywhere, hence the constant is strictly positive. Finally, for every nonnegative random variable \(T\) and \(p>0\), \(\mathbb ET^p=p\int_0^\infty t^{p-1}\Pr(T>t)\,dt\). Applying this identity to the proven positive tail constants yields both exact moment thresholds.

## Verification

The standalone `verify.py` uses exact rational arithmetic for the Anderson cancellation identity across 243 parameter combinations, deterministic one-dimensional integration for the two tail benchmarks, direct rational-form testing of the symmetry cancellation, and one-dimensional integral checks of the subcritical second moment. It passes 10,452 assertions in the recorded environment. In particular, for \(x_0=\theta=0\), \(x_1=1\), \(r=1/2\), at \(\delta=1/4\) the tail is **exactly**
\[
\Pr(|Z|>t)=\frac1{8t(t+1)}\quad(t\ge1),
\]
which independently verifies the critical constant \(1/8\). At \(\delta=1/2\), the positive-tail calculation yields \(\lim_{t\to\infty}t\Pr(|Z|>t)=1/4\). These numerical checks do not substitute for the asymptotic proof.

## Relationship to prior work

Anderson acceleration and residual-minimizing coefficients are classical. Ouyang et al. (arXiv:2006.02559, first publicly submitted 2020-06-03) study globalization and regularization, noting possible instability of the unregularized method. Wei, Bao and Liu (arXiv:2110.01543, first publicly submitted 2021-10-04) introduce damped, adaptively regularized stochastic Anderson mixing to control inaccurate stochastic residual matrices. Toth et al. (DOI:10.1137/16M1080677) analyze inaccurate evaluations and bounded or unbounded disturbances. Their full public preprint, especially Algorithm 1, Assumption 1.2 and Theorems 2–3, presupposes a uniform bound on the Anderson coefficient sum and derives local improvement and stagnation estimates; it does not establish a bounded-uniform exact coefficient-failure tail law when that bound fails. The new assertion is **not** the classic instability warning or the general denominator mechanism. It is the full exact bounded-uniform threshold, the distinct interior/corner tail exponents, the symmetric critical cancellation, the positive leading constants, and the logarithmic approach-to-threshold coefficient. Previous Gaussian two-point Anderson calculations already cover first-order tails when the denominator density is everywhere positive; that statement cannot yield a bounded-support threshold or the exceptional critical behavior.

## Limitations

This is a one-step conditional, scalar, uniform-independent-oracle analysis. It does not provide global convergence results, guarantees for correlated or discrete perturbations, or stability for safeguarded Anderson implementations. The primary inaccurate-evaluations preprint was inspected, including its bounded-coefficient hypothesis and theorems; independent publication-precedence assessment has not been performed. The analytic conclusions hold under the stated assumptions.

## References

- Ouyang, Tao, Milzarek and Deng, *Nonmonotone Globalization for Anderson Acceleration via Adaptive Regularization*, arXiv:2006.02559 (public 2020-06-03). https://arxiv.org/abs/2006.02559
- Wei, Bao and Liu, *Stochastic Anderson Mixing for Nonconvex Stochastic Optimization*, arXiv:2110.01543 (public 2021-10-04). https://arxiv.org/abs/2110.01543
- Toth et al., *Local Improvement Results for Anderson Acceleration with Inaccurate Function Evaluations*, SIAM J. Sci. Comput. 39(5), 2017; lawful author/preprint full text https://www.osti.gov/servlets/purl/1408509 and https://doi.org/10.1137/16M1080677
- Garner, Lerman and Zhang, *Improved Convergence Factor of Windowed Anderson Acceleration for Symmetric Fixed-Point Iterations*, arXiv:2311.02490 (public 2023-11-04). https://arxiv.org/abs/2311.02490
