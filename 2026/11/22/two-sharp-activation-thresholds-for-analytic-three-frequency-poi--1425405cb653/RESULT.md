# Immediate second-harmonic activation in resonant analytic Poisson fourth moments

## Finding

Use normalized Haar measure on \(\mathbb T\), and let \(P_\rho e^{ikt}=\rho^{|k|}e^{ikt}\) for \(0<\rho\le1\). Fix an integer \(m\ge1\) and define the fourth power of the sharp norm on the analytic progression by
\[
\mathcal C_{m,2m}(\rho)=\max_{0\ne f\in\operatorname{span}_{\mathbb C}\{1,e^{imt},e^{i2mt}\}}
\frac{\|P_\rho f\|_4^4}{\|f\|_2^4},\qquad a=\rho^{2m}.
\]
For \(a\le1/2\) only nonzero constant functions attain the maximum, which is \(1\). For every \(a>1/2\), **all three coefficients of every maximizing function are nonzero**. Their phases obey
\[
\arg c_0+\arg c_{2m}\equiv 2\arg c_m\pmod{2\pi}.
\]
At onset, let \(\delta=a-1/2\downarrow0\) and \(x_j=|c_j|^2/\|f\|_2^2\). For sufficiently small positive \(\delta\), the maximizing magnitude profile is unique, and
\[
x_m=4\delta+O(\delta^2),\qquad x_{2m}=4\delta^2+O(\delta^3),\qquad
\mathcal C_{m,2m}=1+8\delta^2+O(\delta^3).
\]
In contrast, the known collision-free staircase [1] leaves the highest mode absent on a nonempty interval just above \(a=1/2\) for \(\{0,m,n\}\) with \(m<n\) and \(n\ne2m\). Its fourth-power excess there is \((16/3)\delta^2+O(\delta^3)\), so the resonant leading excess is larger by the factor \(3/2\).

## Assumptions and scope

The coefficients \(c_0,c_m,c_{2m}\) are complex and independently variable. The output norm is the normalized-circle \(L^4\) norm. The activation and phase assertions concern every maximizing function at every indicated radius, including \(\rho=1\); uniqueness of the magnitude profile is asserted only sufficiently close to onset or in the constant regime. No all-radius closed formula for the resonant norm is claimed.

## Proof

**1. Resonant fourth moment.** Normalize the input to \(\|f\|_2=1\) and set \(u=(c_0,\rho^m c_m,\rho^{2m}c_{2m})\). By Parseval applied to \((P_\rho f)^2\), the pair sums \(0+2m=m+m\) contribute the only phase-sensitive cross term, \(4\operatorname{Re}(u_0u_2\overline{u_1}^{\,2})\). Fixing the moduli allows this term to attain its upper bound. For aligned nonnegative input amplitudes \(X=|c_0|,\ Y=|c_m|,\ Z=|c_{2m}|\), with \(X^2+Y^2+Z^2=1\), the resulting fourth moment is
\[
R_a=X^4+a^2Y^4+a^4Z^4+4aX^2Y^2+4a^2X^2Z^2+4a^3Y^2Z^2+4a^2XY^2Z.
\]

**2. Sharp activation.** At \(a=1/2\), the gap is
\[
(X^2+Y^2+Z^2)^2-R_{1/2}
=\left(XZ-\tfrac12Y^2\right)^2+\tfrac12Y^4+\tfrac{15}{16}Z^4+\tfrac32Y^2Z^2.
\]
Only \(Y=Z=0\) gives equality, and every coefficient in \(R_a\) is nonnegative and nondecreasing in \(a\), proving the constant-only assertion throughout \(0<a\le1/2\).

For \(a>1/2\) the best \(\{0,m\}\) pair is mixed: with \(s=Y^2\) its objective is \(1+(4a-2)s+(a^2-4a+1)s^2\), with derivative positive at \(s=0\) and the value at \(s=1\) at most one. Its maximum bounds every two-mode support: the \(\{0,2m\}\) pair replaces \(a\) by \(a^2\le a\) in the nonnegative fourth-moment terms, and the \(\{m,2m\}\) norm to the fourth power is \(a^2\) times that of \(\{0,m\}\). Starting from a mixed maximizing \(\{0,m\}\) pair \((X,Y,0)\), add \(Z=z>0\) and multiply \(X,Y\) by \(\sqrt{1-z^2}\). The gain is \(4a^2XY^2z+O(z^2)>0\) for sufficiently small \(z\). Thus no two-mode or one-mode support is globally maximizing. With all amplitudes nonzero, attaining the phase-term upper bound requires the stated phase congruence.

**3. Near-threshold profile.** Put \(t=Y^2,\ z=Z\) and \(X=\sqrt{1-t-z^2}\). The strict maximum at \(a=1/2\) and compactness force all maximizing profiles to \((t,z)=(0,0)\) as \(\delta\downarrow0\). In an open neighborhood of \((\delta,t,z)=(0,0,0)\), the formula for \(R_{1/2+\delta}\) has a real-analytic extension in \((\delta,t,z)\), with expansion
\[
R_{1/2+\delta}=1+4\delta t-\tfrac34t^2+tz-z^2
+O\bigl(|\delta|(t^2+z^2+|tz|)+(|t|+|z|)^3\bigr).
\]
The Hessian in \((t,z)\) at the origin is \(\begin{pmatrix}-3/2&1\\1&-2\end{pmatrix}\), hence invertible and negative definite. The implicit-function theorem gives a unique critical point nearby, and the linear stationarity equations give \(t=4\delta+O(\delta^2)\), \(z=2\delta+O(\delta^2)\). For \(\delta>0\), all maximizers are interior by Step 2 and converge to this neighborhood, so this is their unique magnitude profile. Thus \(z^2=4\delta^2+O(\delta^3)\), and substitution gives \(R_a=1+8\delta^2+O(\delta^3)\).

**4. Collision-free comparison.** Reference [1] supplies the separate activation radii for nonresonant \(\{0,m,n\}\); on the first supercritical interval the problem is the \(\{0,m\}\) pair. Maximizing the quadratic in Step 2 gives the excess \((2a-1)^2/(4a-1-a^2)=(16/3)\delta^2+O(\delta^3)\). This yields the claimed relative enhancement without asserting the nonresonant staircase as a new result.

## Verification

The supplied package's `checker.py` can be run with the packages in `requirements.txt`. It checks the resonant Fourier convolution, the sum of squares and the onset expansion, along with nonresonant diagnostic comparisons. The all-radius activation and near-onset uniqueness use the exact proof above; these are not conclusions of finite tests.

## Relationship to prior work

The collision-free activation staircase [1] covers the full nonresonant three-character problem as a specialization. It assumes unique unordered pair sums, excluding \(\{0,m,2m\}\). The unweighted finite-cyclic classification [2] already identifies the midpoint collision, its phase constraint and the corresponding endpoint constant; it does not optimize the weighted problem as \(a\downarrow1/2\). Classical analytic circle hypercontractivity [3] gives context for the first contraction radius; the contribution here is strict activation of the second harmonic in every supercritical optimizer and the sharp quantitative onset. In the real zero-mean two-tone fourth moment, persistence instead comes from the \(1{:}3\) collision [4], not the midpoint term above.

## References

1. [A complete Poisson activation staircase on finite and infinite \(B_2\) Fourier spectra](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-complete-poisson-activation-staircase-on-finite-and-infinite-b--58c46c248a92/RESULT.md).
2. [Exact \(\Lambda(4)\) constants for every three-character subset of a cyclic group](https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-lambda-4-constants-for-every-three-character-subset-of-a-c--5562292e7127/RESULT.md).
3. F. B. Weissler, *Logarithmic Sobolev inequalities and hypercontractive estimates on the circle*, J. Funct. Anal. 37 (1980), 218–234. [DOI](https://doi.org/10.1016/0022-1236(80)90042-7).
4. [Resonant persistence and sharp mode selection for two-frequency circular Poisson smoothing](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-resonant-persistence-and-sharp-mode-selection-for-two-frequency--ebfd25bec609/RESULT.md).
