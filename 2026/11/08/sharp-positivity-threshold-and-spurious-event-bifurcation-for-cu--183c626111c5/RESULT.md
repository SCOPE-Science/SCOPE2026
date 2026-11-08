# Sharp positivity threshold and spurious-event bifurcation for cubic Hermite exponential dense output

## Finding

There is a unique number \(z_*>0\) such that ordinary endpoint-value-and-derivative cubic Hermite interpolation of the exact positive decay solution \(y(t)=y_0e^{-\lambda t}\) is strictly positive throughout a step exactly when \(0\le\lambda h<z_*\). At \(\lambda h=z_*\), the cubic is nonnegative and has one interior double zero. For every \(\lambda h>z_*\), the cubic has exactly two simple, distinct interior zeros and is negative between them, although its exact endpoint values and derivatives are supplied and the true solution never vanishes.

Numerically, \(z_*=3.8693063362726609358291805688\ldots\). The double zero occurs at the unique \(s_*=0.6756948259267831194362816696\ldots\) in \((0,1)\). When \(\delta=z-z_*\downarrow0\), the spurious zeros obey
\[
 s_\pm(z)=s_*\pm K\sqrt{\delta}+O(\delta),\qquad
 K=0.3365508378245634255633860358\ldots.
\]
The square-root opening yields an exact local law for the appearance of a false pair of zero events.

## Assumptions and scope

Take \(y_0>0\), \(\lambda>0\), \(h>0\), and set \(z=\lambda h\), \(s=t/h\in[0,1]\). Construct the unique cubic polynomial \(H_z(s)\) with the *exact* values \(H_z(0)=1\), \(H_z(1)=e^{-z}\) and scaled derivatives \(H_z'(0)=-z\), \(H_z'(1)=-ze^{-z}\). Thus the dimensional approximation is \(y_0 H_z(t/h)\). The theorem concerns this unmodified cubic continuous extension, not an integrator's endpoint numerical error, clipped Hermite slopes, or arbitrary positive functions.

Define
\[
 A(z)=2-z-(2+z)e^{-z},\qquad
 B(z)=-3+2z+(3+z)e^{-z}.
\]
The cubic has the explicit formula
\[
 H_z(s)=1-zs+B(z)s^2+A(z)s^3.
\]
Define \(z_*\) intrinsically as the unique positive solution of
\[
 \min_{0\le s\le1}H_z(s)=0.
\]
Equivalently it is the unique positive value at which a zero of \(H_z\) occurs inside \((0,1)\) with zero derivative. At that point the polynomial discriminant vanishes:
\[
 B^2z^2+4Az^3-4B^3-27A^2-18ABz=0,
\]
where \(A=A(z)\) and \(B=B(z)\). **This discriminant equation alone is not asserted to have only one positive root:** the defining condition includes the interior, nonnegative tangency.

## Proof

**Exact interpolation.** With the standard cubic Hermite basis
\[
 h_{00}(s)=1-3s^2+2s^3,\quad
 h_{10}(s)=s(1-s)^2,\quad
 h_{01}(s)=3s^2-2s^3,\quad
 h_{11}(s)=s^3-s^2,
\]
write \(H_z=h_{00}-zh_{10}+e^{-z}h_{01}-ze^{-z}h_{11}\). Direct expansion gives the stated \(A,B\), endpoints and endpoint derivatives.

**Strict decrease of every interior sample.** Differentiation with respect to \(z\), *including the derivative of \(e^{-z}\)*, gives the identity
\[
 \frac{\partial H_z(s)}{\partial z}
 =-s(1-s)^2-e^{-z}s^2\bigl(2-s+z(1-s)\bigr)<0
 \quad(0<s\le1,\ z>0).
\]
Let \(m(z)=\min_{s\in[0,1]}H_z(s)\). It is continuous by compactness and continuity. At \(z=0\), \(m(0)=1\). For \(z>0\), \(H'_z(0)=-z<0\), hence the minimizing point is not \(s=0\); choosing any minimizer for \(z_1>0\) in the preceding strict inequality gives \(m(z_2)<m(z_1)\) whenever \(z_2>z_1>0\). Also \(m(z_2)<m(0)\), since \(H_{z_2}(1)=e^{-z_2}<1\). Finally, at \(s=1/2\),
\[
 H_z(1/2)=\frac12-\frac z8+e^{-z}\left(\frac12+\frac z8\right)
 \longrightarrow-\infty
 \quad(z\to\infty).
\]
Thus \(m(z)\) decreases continuously from \(1\) to \(-\infty\), crossing zero at one and only one \(z_*>0\).

**Multiplicity and sign classification.** Since \(H_z(0)=1\) and \(H_z(1)=e^{-z}>0\), any zero at the first loss of positivity must be interior. At \(z=z_*\), the minimum is zero at an interior \(s_*\), so \(H_{z_*}(s_*)=H'_{z_*}(s_*)=0\). An interpolating cubic cannot have two different interior double zeros. The stationary zero is not triple: a nonzero cubic with a triple interior root changes sign there, contrary to global nonnegativity; a lower-degree cubic also cannot have a triple root unless identically zero, contrary to its endpoint value. Therefore \(H''_{z_*}(s_*)>0\) and the zero has multiplicity exactly two. When \(z>z_*\), \(m(z)<0\) and both endpoints remain positive. By continuity at least two distinct interior sign-changing zeros exist; degree three and the positive endpoint signs exclude any further zero, counting multiplicity. Both roots are simple, and the cubic is negative strictly between them.

**Birth of two spurious events.** Taylor expansion near the double zero gives, for \(u=s-s_*\) and \(\delta=z-z_*\),
\[
 H_{z_*+\delta}(s_*+u)=
 \frac12H_{ss}(z_*,s_*)u^2+H_z(z_*,s_*)\delta
 +O\bigl(|u|^3+|u\delta|+\delta^2\bigr).
\]
Here \(H_{ss}>0\) from the multiplicity argument and \(H_z<0\) from the strict derivative formula. Rescaling \(u=\sqrt\delta\,v\), or applying the simple-root implicit-function theorem to the rescaled equation, gives two branches with
\[
 K=\sqrt{\frac{-2H_z(z_*,s_*)}{H_{ss}(z_*,s_*)}}>0.
\]
The two roots have the asserted \(O(\delta)\) corrections, and their separation is \(2K\sqrt\delta+O(\delta)\).

## Verification

The included `verify.py` reproduces symbolic Hermite identities, exact-rational positivity and negativity certificates, and numerical values at 80-digit precision. It reports 50 passing assertions. The executable uses `sympy==1.14.0` and `mpmath==1.3.0`; run `python verify.py` in the directory containing the files. The recorded output is in `verification_output.txt`.

In particular, the exact-rational exponential enclosure for positive rational \(z\) follows from truncating \(e^z=\sum_{k\ge0}z^k/k!\) after order 48 and bounding the positive remainder by a geometric majorant. Substituting the resulting *lower* rational bound for \(e^{-19/5}\) into the cubic, all 16 Bernstein coefficients on the four equal subintervals of \([0,1]\) are strictly positive. Consequently \(H_{19/5}(s)>0\) everywhere. Conversely, using the *upper* bound for \(e^{-39/10}\) gives the exact-rational strict inequality \(H_{39/10}(2/3)<0\). Therefore the exact transition lies in \((19/5,39/10)\), independently of numerical root-finding. The code additionally certifies positivity of \(H_{7/2}\) everywhere and a positive derivative at \(s=4/5\), so **loss of monotonicity can precede loss of positivity**. The printed long decimal constants are reproducible approximations, not independent interval-certified 80-digit enclosures; the mathematical theorem uses the exact implicit definition.

## Relationship to prior work

Cubic Hermite interpolation and general shape-preserving algorithms are classical. Dougherty, Edelman, and Hyman (1989) give Hermite construction formulas and derivative constraints sufficient for nonnegativity. Higham (1992) treats monotone Hermite interpolation for ODE plotting; his presentation of Fritsch–Carlson conditions supplies an important conceptual comparison. Ouermi, Kirby, and Berzins (2022) develop constrained positivity-preserving interpolation for different, ENO-type data. The present contribution is not a new interpolation formula or a general nonnegativity criterion: it specializes the *unmodified exact-derivative* cubic to positive exponential decay and obtains the globally sharp dimensionless parameter \(z_*\), the full exactly-two-spurious-zero classification, and the square-root false-event opening. These specific exponential-step assertions were not found in the inspected material; equivalent unindexed prior results remain possible.

## Limitations

This theorem is one-dimensional and uses exact, unmodified endpoint values and slopes. It does not establish a corresponding boundary for arbitrary stable integrators, high-order continuous extensions, perturbed derivative data, general stiff systems, or multidimensional positive cones. It concerns deterministic interpolation zeros, not event-detection software behavior in finite precision. Decimal values of \(z_*\), \(s_*\), and \(K\) are high-precision numerical evaluations of uniquely defined analytic quantities; the infinitely quantified theorem rests on the proof above rather than on the finite calculations.

## References

1. R. L. Dougherty, A. Edelman, and J. M. Hyman, *Nonnegativity-, monotonicity-, or convexity-preserving cubic and quintic Hermite interpolation*, Mathematics of Computation 52 (1989), 471–494. https://doi.org/10.1090/S0025-5718-1989-0962209-1 ; lawful full text: https://www.ams.org/mcom/1989-52-186/S0025-5718-1989-0962209-1/S0025-5718-1989-0962209-1.pdf
2. D. J. Higham, *Monotonic piecewise cubic interpolation, with applications to ODE plotting*, Journal of Computational and Applied Mathematics 39 (1992), 287–294. https://doi.org/10.1016/0377-0427(92)90205-C ; author full text: https://webhomes.maths.ed.ac.uk/~dhigham/Publications/P13.pdf
3. T. A. J. Ouermi, R. M. Kirby, and M. Berzins, *ENO-Based High-Order Data-Bounded and Constrained Positivity-Preserving Interpolation*, first made public 2022-04-13. https://arxiv.org/abs/2204.06168
4. F. N. Fritsch and R. E. Carlson, *Monotone piecewise cubic interpolation*, SIAM Journal on Numerical Analysis 17 (1980), 238–246. https://doi.org/10.1137/0717021
5. R. W. Brankin and I. Gladwell, *Shape-preserving local interpolation for plotting solutions of ODEs*, IMA Journal of Numerical Analysis 9 (1989), 555–566. https://doi.org/10.1093/imanum/9.4.555
