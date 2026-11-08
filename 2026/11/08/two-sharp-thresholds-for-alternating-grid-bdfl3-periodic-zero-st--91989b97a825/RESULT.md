# Two sharp thresholds for alternating-grid BDFL3: periodic zero-stability versus stiff-stage solvability

## Finding

For the variable-step, second-order three-step BDFL method defined in Jensen–Lóczi–Ketcheson (2026, §6.2), prescribe positive step lengths alternating indefinitely between \(h\) and \(rh\), where \(h>0\) and \(r>0\). Put
\[
S_*:=\frac{5+\sqrt{221}}4,\qquad
R_*:=\frac{S_*+\sqrt{S_*^2-4}}2=4.75626832541521\ldots.
\]

The homogeneous recurrence on \(y'=0\) is zero-stable (every solution is bounded uniformly over arbitrarily many alternating steps) **if and only if**
\[
R_*^{-1}\le r\le R_*.
\]
The nonconstant two-step Floquet multipliers have modulus strictly below one in the open interval; at either endpoint one of them is the simple unit multiplier \(-1\), while the other is strictly inside the unit disk. Beyond either endpoint a real multiplier lies strictly below \(-1\).

Independently, every implicit scalar equation arising in the same alternating method on the decaying test equation \(y'=-\lambda y\), \(\lambda>0\), is uniquely solvable **for every** \(\lambda>0\) and \(h>0\) if and only if
\[
\frac14\le r\le4.
\]
Consequently the nonempty regions \(4<r\le R_*\) and \(R_*^{-1}\le r<1/4\) are periodically zero-stable yet possess a **positive-real stiff-stage pole**: for a suitable strictly positive \(\lambda h\), a step loses its nonzero leading coefficient. At \(r=9/2\), the two parasitic Floquet multipliers are strictly contractive, but one implicit coefficient equals \(-11/96\), so that step is singular at \(\lambda h=96/11\).

The second threshold is about algebraic well-posedness on the real negative test axis, **not** a claim of unconditional decay stability or \(A\)-stability.

## Assumptions and scope

All calculations use exact real arithmetic and the specific adaptive BDFL\(3_2\) coefficients in §6.2 of the cited paper. Let \(\omega_n=h_n/h_{n-1}>0\). At each step the recurrence is
\[
\alpha_0y_{n-2}+\alpha_1y_{n-1}-\frac32y_n+y_{n+1}
=h_n\beta y'_{n+1},
\]
where, with \(a=\omega_n\), \(b=\omega_{n-1}\),
\[
\begin{aligned}
\alpha_0(a,b)&=\frac{b^2(2a^2-2a-1)}{4b(a+1)+2},\\
\alpha_1(a,b)&=\frac{(-2a^2+2a+1)b^2+2(a+1)b+1}{4b(a+1)+2},\\
\beta(a,b)&=\frac{2a+b(2a^2+4a-1)-1}{2a(2b(a+1)+1)}.
\end{aligned}
\]
The ratios alternate between \((a,b)=(r,r^{-1})\) and \((r^{-1},r)\). Their phase choice only cyclically changes the two-step product and does not change its characteristic polynomial. Zero-stability here is power boundedness of the exact periodic homogeneous recurrence on \(y'=0\), including all three prescribed starting values. No claim is made about arbitrary, nonperiodic ratio sequences.

## Proof

**1. Two frozen coefficient matrices.** Define the homogeneous companion matrix
\[
M(a,b)=\begin{pmatrix}
\frac32&-\alpha_1(a,b)&-\alpha_0(a,b)\\
1&0&0\\0&1&0
\end{pmatrix}.
\]
Direct rational simplification yields
\[
\begin{array}{c|c|c|c}
(a,b)&\alpha_0&\alpha_1&\beta\\\hline
(r,r^{-1})&\dfrac{2r^2-2r-1}{2r(3r+2)}&\dfrac{r^2+4r+1}{2r(3r+2)}&\dfrac{(r+1)(4r-1)}{2r(3r+2)}\\[5pt]
(r^{-1},r)&-\dfrac{r^2+2r-2}{2(2r+3)}&\dfrac{r^2+4r+1}{2(2r+3)}&\dfrac{(4-r)(r+1)}{2(2r+3)}
\end{array}
\]
All displayed denominators are positive for \(r>0\).

**2. Exact Floquet polynomial.** The two-step monodromy is
\[
T(r):=M(r^{-1},r)M(r,r^{-1}).
\]
Its characteristic polynomial factors as
\[
\det(tI-T(r))=(t-1)\left(t^2+\frac{B(r)}{A(r)}t+\frac{C(r)}{A(r)}\right),
\]
where
\[
\begin{aligned}
A(r)&=4r(2r+3)(3r+2),\\
B(r)&=6r^4+2r^3-21r^2+2r+6,\\
C(r)&=-2r^4-2r^3+9r^2-2r-2.
\end{aligned}
\]
The root \(1\) represents constant solutions. The exact quadratic Schur conditions for both nonconstant roots to lie strictly within the unit disk are \(A+B+C>0\), \(A-B+C>0\), and \(A-C>0\), as \(A>0\). These simplify to
\[
\begin{aligned}
A+B+C&=4(r+1)^2(r^2+4r+1)>0,\\
A-C&=2r^4+26r^3+43r^2+26r+2>0,\\
A-B+C&=-2F(r),\\
F(r)&=4r^4-10r^3-41r^2-10r+4.
\end{aligned}
\]
Set \(s=r+r^{-1}\ge2\). Then
\[
F(r)=r^2(4s^2-10s-49),
\]
which is negative precisely for \(2\le s<S_*\). This is equivalent to \(R_*^{-1}<r<R_*\).

At either endpoint \(F(r)=0\), so one root of the quadratic is \(-1\). The inequalities \(A+B+C>0\) and \(A-C>0\) make the other root strictly between \(-1\) and \(1\), and also prevent \(1\) from being a repeated root. Thus all unit-circle roots of the full monodromy are simple, and every power of \(T(r)\) stays bounded. Outside the closed interval, the quadratic is negative at \(t=-1\) and positive as \(t\to-\infty\); hence it has a real root below \(-1\), proving exponential homogeneous growth for a suitable initial state. This proves the first threshold, including the endpoints.

**3. Scalar solvability threshold.** Insert \(y'=-\lambda y\). The step equation becomes
\[
(1+\lambda h_n\beta)y_{n+1}
=\tfrac32y_n-\alpha_1y_{n-1}-\alpha_0y_{n-2}.
\]
For every \(h_n,\lambda>0\), the leading coefficient is nonzero exactly when \(\beta\ge0\); if \(\beta<0\), it vanishes at the positive choice \(\lambda h_n=-1/\beta\). The two values of \(\beta\) in step 1 are simultaneously nonnegative exactly when \(r\in[1/4,4]\). Both are strictly positive in the open interval. This proves the second threshold and its sharpness.

**4. Nonempty separation.** Since \(R_*>4\) and \(R_*^{-1}<1/4\), both intervening bands exist. At \(r=9/2\), the strict Schur inequalities from step 2 hold, but the reverse-phase coefficient is \(\beta=-11/96\), producing a pole at \(\lambda h_n=96/11\). Starting data with a nonzero right-hand side make that scalar step inconsistent; e.g. independent history \((y_{n-2},y_{n-1},y_n)=(0,0,1)\) gives the right-hand side \(3/2\). Thus the pole is not merely a formally vanishing coefficient.

## Verification

The included `verify.py` uses exact symbolic rational algebra to reconstruct both sets of coefficients, the full monodromy characteristic polynomial, all three Schur identities and the sharp endpoint equations. It additionally verifies the rational witness at \(r=9/2\). Run `python verify.py` with Python and SymPy. No floating-point experiment is used in the proof. The decimals of \(R_*\) are explanatory approximations only.

## Relationship to prior work

Jensen, Lóczi and Ketcheson (2026, §6.2) define the adaptive three-step BDFL method studied here and (§6.3) derive a complete **frozen-coefficient** root-condition region. They explicitly note that frozen-coefficient analysis does not classify products along actual variable-step sequences. The present claim instead concerns the true two-step Floquet product on a periodic mesh and its interaction with the sign of the coefficient multiplying the new derivative. General variable-grid stability and the quadratic Schur criterion are standard ingredients; neither by itself evaluates the particular rational monodromy or discovers the distinct implicit-stage pole threshold.

## Limitations

The periodic mesh is fixed and alternates between precisely two positive step lengths; arbitrary adaptive step sequences are not classified. Power boundedness at the endpoints is zero-stability, not strict damping of all parasitic modes. The absence of a positive-real pole for ratios in \([1/4,4]\) is only a solvability statement, not absolute or \(A\)-stability. All claims concern exact arithmetic and scalar linear test equations; finite precision, nonlinear solves and error-control/rejection mechanisms are outside scope. Possible implication from older general product-stability results remains a historical-priority risk.

## References

1. T. Jensen, L. Lóczi and D. I. Ketcheson, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1, publicly posted 15 October 2026, especially §§6.1–6.3, https://arxiv.org/html/2610.22685v1.
2. R. D. Grigorieff, *Stability of multistep methods on variable grids*, Numerische Mathematik 42 (1983), 359–377, https://doi.org/10.1007/BF01389580. General historical framework; exact current coefficient specialization not attributed to this source.
