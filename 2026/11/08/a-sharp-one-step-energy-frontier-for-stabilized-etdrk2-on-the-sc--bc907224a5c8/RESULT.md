# A sharp one-step energy frontier for stabilized ETDRK2 on the scalar Allen–Cahn reaction

## Finding

Consider the real scalar Allen–Cahn gradient equation
\[
\dot u=u-u^3=-E'(u),\qquad E(u)=\frac14(1-u^2)^2.
\]
For a nonnegative stabilization parameter \(\alpha\), the standard stabilized two-stage exponential time-differencing Runge–Kutta method (ETDRK2) is defined in the next section. **The following characterization is exact:**
\[
\boxed{\ \forall h>0\ \forall u\in[-1,1],\quad E(\Phi_{h,\alpha}(u))\le E(u)
\quad\Longleftrightarrow\quad \alpha\ge1.\ }
\]
For every \(0\le\alpha<1\), there is a sufficiently large finite time step and a starting point strictly between zero and one at which the original quartic energy increases. The forward implication is a **single-step guarantee on the indicated input interval**; no invariant-interval or all-future-step statement is asserted.

## Assumptions and scope

Everything is in exact real arithmetic. Let \(h>0\), \(\alpha\ge0\), and define
\[
g_\alpha(u)=(1+\alpha)u-u^3,\qquad
H=\begin{cases}(1-e^{-\alpha h})/\alpha,&\alpha>0,\\h,&\alpha=0,\end{cases}
\]
\[
B=\begin{cases}(\alpha h+e^{-\alpha h}-1)/(\alpha^2h),&\alpha>0,\\h/2,&\alpha=0.\end{cases}
\]
The two-stage method and its output map are
\[
v=u+Hu(1-u^2),\qquad
\Phi_{h,\alpha}(u)=v+B\bigl(g_\alpha(v)-g_\alpha(u)\bigr).
\]
This is the ETDRK2 scheme with linear part \(-\alpha u\), \(h\varphi_1(-\alpha h)=H\), and \(h\varphi_2(-\alpha h)=B\). No spatial diffusion or stochastic forcing is included. The input interval is closed and includes the equilibria \(0\) and \(\pm1\).

## Proof

**1. Reduction and coefficient bounds.** The update is odd; it suffices to work with \(u\in[0,1]\). Write \(z=u^2\) and \(q=H(1-z)\). Direct expansion gives \(v=u(1+q)\) and
\[
\Phi_{h,\alpha}(u)=uW_B,
\quad W_B=1+q\{1+B[\alpha+1-z(3+3q+q^2)]\}.
\]
For \(\alpha\ge1\), the exponential integral formulas imply \(0<B\le H\le1/\alpha\le1\). Therefore \(0\le q\le1-z\), and
\[
z(3+3q+q^2)\le z(7-5z+z^2)\le3,
\]
where the last inequality follows from \(z(7-5z+z^2)-3=(z-1)^2(z-3)\le0\). Consequently the braces in \(W_B\) are nonnegative: if \(1\le\alpha\le2\), they are at least \(1+B(\alpha-2)\ge2-2/\alpha\ge0\); if \(\alpha\ge2\), they are at least one. Hence
\[
\Phi_{h,\alpha}(u)\ge v\ge u\ge0.
\]

**2. Reduction to a polynomial positivity certificate.** Since \(W_B\) is affine in \(B\), its value for \(0\le B\le H\) lies between its values at \(B=0\) and \(B=H\). Both endpoints are nonnegative. At \(B=0\),
\[
v^2+u^2\le z[(2-z)^2+1]\le2,
\]
because \(z[(2-z)^2+1]-2=(z-1)^2(z-2)\le0\). We next prove the same inequality at \(B=H\).

Set \(t=1/\alpha\in(0,1]\), \(y=\alpha H=1-e^{-\alpha h}\in(0,1)\), \(q=ty(1-z)\), and define
\[
W=1+q\left[1+y\left(1+t-tz(3+3q+q^2)\right)\right],
\]
which is exactly \(W_H\). The polynomial \(2-z(1+W^2)\) is divisible by \(1-z\) over the rational polynomial ring \(\mathbb Q[z,y,t]\). Let
\[
P(z,y,t)=\frac{2-z(1+W^2)}{1-z}.
\]
An exact, reproducible finite algebraic certificate establishes
\[
P(z,y,t)\ge\frac18\qquad (z,y,t\in[0,1]).
\]
The certificate expands \(P\) in the tensor-product degree-eight Bernstein basis in its three variables. All \(9^3=729\) rational coefficients are at least \(1/8\); the smallest is attained at coefficient index \((1,8,8)\). The attached `verify.py`, relying only on Python's standard-library exact fractions, constructs \(P\) from the displayed formula, verifies division with zero remainder, establishes degree at most eight, and checks all 729 inequalities without floating-point arithmetic. Since Bernstein basis functions are nonnegative and sum to one on the cube, the coefficient bound proves the stated polynomial bound for the entire cube. Thus \(v^2+u^2\le2\) also at \(B=H\). By affine interpolation and nonnegativity, the actual output satisfies
\[
u^2+\Phi_{h,\alpha}(u)^2\le2.
\]

**3. Energy descent.** For \(w=\Phi_{h,\alpha}(u)\), the preceding conclusions give \(w^2\ge u^2\) and \(w^2+u^2\le2\). The exact factorization
\[
4[E(w)-E(u)]=(w^2-u^2)(w^2+u^2-2)
\]
therefore yields \(E(w)\le E(u)\). Oddness handles negative initial values.

**4. Necessity and sharpness.** All three equilibria, including \(u=1\), are preserved. Differentiating the update at \(u=1\) gives
\[
\Phi'_{h,\alpha}(1)=1-2H[1+B(\alpha-2)].
\]
For \(0<\alpha<1\), as \(h\to\infty\), this derivative tends to \((1-2/\alpha)^2>1\). For \(\alpha=0\), the derivative equals \(1-2h+2h^2>1\) whenever \(h>1\). Thus, for any \(\alpha<1\), some finite \(h\) makes the fixed point \(u=1\) locally repelling from below: there are initial values \(u<1\) arbitrarily close to one with \(0<\Phi_{h,\alpha}(u)<u<1\). Because \(E\) is strictly decreasing on \((0,1)\), these starts satisfy \(E(\Phi_{h,\alpha}(u))>E(u)\). This completes the if-and-only-if proof.

## Verification

Run `python3 verify.py` in the directory containing this document. The exact algebraic certificate prints `BERNSTEIN_CERTIFICATE_OK` with 46 nonzero monomial coefficients and minimum rational Bernstein coefficient \(1/8\), then `VERIFY_OK`. The script also tests 20,000 seeded parameter/step/input triples and seven illustrative failure cases with \(\alpha<1\); these numerical tests are ancillary to the exact polynomial proof and the analytic fixed-point derivative.

## Relationship to prior work

Quan, Zheng and Zhou (arXiv:2610.11532; first public version 8 October 2026) analyze original-energy dissipation for equilibrium-preserving ETDRK methods through general time-step conditions and discuss stabilized ETDRK2. Fu, Shen and Yang (arXiv:2402.15142; later *Science China Mathematics*) give the same ETDRK2 stage formulas in their equations (2.10)–(2.11) and a general sufficient stabilization criterion involving a Lipschitz constant and a matrix positivity requirement (Theorem 2.2). Fu and Yang (2022) established energy descent for suitably stabilized ETDRK2 under broader phase-field assumptions. The present assertion is the exact **minimal scalar one-step stabilization** for the untruncated quartic potential when the *input* is in \([-1,1]\); it does not assert a stronger PDE or multistep result than these papers. Full text of the 2022 paper was not accessible for direct theorem-by-theorem priority comparison; possible implicit coverage remains a historical-priority risk.

## Limitations

The theorem is scalar, exact arithmetic, and confined to a single step from \([-1,1]\). It is **not** a maximum-bound principle: at \(\alpha=1\), \(u=1/2\), and \(h\to\infty\), the output tends to \(553/512>1\), even though energy decreases. Therefore this one-step result cannot be iterated indiscriminately to assert indefinite energy decrease without proving subsequent inputs remain in range. No spatially coupled Allen–Cahn equation, PDE discretization, error estimate, or full-step trajectory is certified. The numerical checks are illustrative; the infinite-domain proof relies on exact rational arithmetic and analysis.

## References

1. C. Quan, P. Zheng, and Z. Zhou, *A unified framework for original energy dissipation of equilibrium-preserving exponential Runge–Kutta methods for \(L^2\) gradient flows*, arXiv:2610.11532, first posted 2026-10-08. https://arxiv.org/abs/2610.11532
2. Z. Fu, J. Shen, and J. Yang, *Higher-Order Energy-Decreasing Exponential Time Differencing Runge–Kutta Methods for Gradient Flows*, arXiv:2402.15142, first posted 2024-02-23. Author-hosted full text: https://www.math.purdue.edu/~shen7/pub/SCM24.pdf
3. Z. Fu and J. Yang, *Energy-decreasing exponential time differencing Runge–Kutta methods for phase-field models*, *Journal of Computational Physics* **454** (2022), article 110943, https://doi.org/10.1016/j.jcp.2022.110943 (full text unavailable for direct comparison).
