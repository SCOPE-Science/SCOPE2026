# Uniform sign recurrence and feedback-zero escape in a sigmoid-memory map

## Finding

Consider the integer-order endpoint of the three-function discrete system of Al-Taani, Abu Hammad, Abudayah, Diabi and Ouannas (2024):
\[
\begin{split}
x_{n+1}&=\frac{\sigma _1}{1+\exp(-\beta x_n)}+
 \sigma _2\sigma _3x_n(\eta |y_n|-1)(z_n^2-1),\\
y_{n+1}&=y_n+x_n,\\
z_{n+1}&=z_n+\sigma _2x_n(\eta |y_n|-1).
\end{split}
\]
All five parameters are real. Suppose \(\sigma _1\sigma _2\eta\ne0\); the parameters \(\beta\) and \(\sigma _3\) are unrestricted.

**Theorem (uniform sign recurrence and feedback-zero escape).** For \(R>0\), put
\[
\begin{split}
 B_R&=R+|\sigma _2|\bigl(|\eta|R^2/2+R\bigr),\\
 L_R&=|\sigma _1\beta|/4+|\sigma _2\sigma _3|(|\eta|R+1)(R^2+1),\\
 C_R&=\frac{32B_R(1+L_R^2)}{\sigma _1^2|\sigma _2\eta|},
 \qquad M_R=\lfloor C_R\rfloor+3.
\end{split}
\]
Every forward orbit contained in \([-R,R]^3\) visits **both** \(\{y>0\}\) and \(\{y<0\}\) within **every block of \(M_R\) consecutive times**. Consequently, every compactly supported invariant probability measure \(\mu\), supported in \([-R,R]^3\), satisfies
\[
\mu\{y>0\}\ge\frac1{M_R},\qquad
\mu\{y<0\}\ge\frac1{M_R}.
\]
In particular, no bounded forward orbit can eventually remain in either closed half-space \(y\ge0\) or \(y\le0\), and no compact invariant set can be contained in either half-space. There is no assumption of ergodicity, smoothness of an attractor, or existence of chaos.

Moreover, on the **zero-feedback parameter face** \(\sigma _3=0\), there is *no bounded forward orbit anywhere in* \(\mathbb R^3\). In fact, if
\[
 \delta=\frac{|\sigma _1|}{1+\exp(|\beta\sigma _1|)}>0,
\]
then all initial states obey
\[
\operatorname{sgn}(\sigma _1)(y_n-y_2)\ge\delta(n-2)
 \quad(n\ge2).
\]
Thus \(\sigma _3\ne0\) is a necessary, but not sufficient, condition for any compact recurrent dynamics. When additionally \(\sigma _2\eta\ne0\), the zero-feedback memory coordinate \(z_n\) escapes at least quadratically in magnitude for all sufficiently large \(n\).

## Assumptions and scope

The map is the ordinary first-order difference interpretation \({}^C\!\Delta^1 u_n=u_{n+1}-u_n\) of Equation (9) in the source article. Its first coordinate therefore equals the sigmoid plus the cubic coupling: the explicit \(-x\) in the difference equation cancels the \(+x\) from \(u_{n+1}-u_n\). The theorem does **not** concern genuinely noninteger-order memory kernels or the controlled variants of the map. The real state space has no imposed invariant box; \(R\) is an *a posteriori* bound for any selected compact orbit or invariant measure.

## Proof

**Step 1 (an exact signed quadratic coboundary).** Define the globally continuous, piecewise-quadratic function
\[
 H(y)=\frac\eta2y|y|-y,\qquad Q(x,y,z)=z-\sigma _2H(y).
\]
Whenever \(y_n,y_{n+1}\ge0\), the identity \(y_{n+1}-y_n=x_n\) gives
\[
 H(y_{n+1})-H(y_n)
 =(\eta y_n-1)x_n+\frac\eta2x_n^2.
\]
The third coordinate equation therefore yields the **exact** one-step relation
\[
 Q_{n+1}-Q_n=-\frac{\sigma _2\eta}{2}x_n^2.
\]
For \(y_n,y_{n+1}\le0\), instead
\[
 Q_{n+1}-Q_n=+\frac{\sigma _2\eta}{2}x_n^2.
\]
These identities hold at zero endpoints as well; they are consequences of the common quadratic branch, not of a Taylor approximation across the nonsmooth cusp. On \([-R,R]^3\), \(|Q|\le B_R\). Hence every string of \(N\) transitions with all \(N+1\) memory-phase values in the **same** closed half-line satisfies
\[
 \sum_{j=0}^{N-1}x_j^2\le\frac{4B_R}{|\sigma _2\eta|}.
 \tag{1}
\]
One may replace the origin of a string by any iteration index.

**Step 2 (nonzero forcing prevents long one-sided strings).** Write \(S(t)=1/(1+e^{-t})\). Since \(S(0)=1/2\) and \(|S'(t)|\le1/4\) for every real \(t\), the first equation and the box bounds imply
\[
 \left|x_{j+1}-\frac{\sigma _1}{2}\right|\le L_R|x_j|.
\]
By Cauchy–Schwarz, for each step,
\[
 \frac{\sigma _1^2}{4}
 \le(1+L_R^2)(x_j^2+x_{j+1}^2).
\]
Apply this for \(j=0,\ldots,N-2\) within a same-sign string, then use (1):
\[
 \frac{(N-1)\sigma _1^2}{4(1+L_R^2)}
 \le 2\sum_{j=0}^{N-1}x_j^2
 \le\frac{8B_R}{|\sigma _2\eta|}.
\]
Thus
\[
 N\le1+C_R. \tag{2}
\]
A hypothetical block of \(M_R=\lfloor C_R\rfloor+3\) successive phase values all nonnegative would have \(N=M_R-1=\lfloor C_R\rfloor+2>1+C_R\), contradicting (2). The same holds for an all-nonpositive block. Every block therefore contains a strictly positive and a strictly negative phase value. A globally bounded forward orbit belongs to some box and obeys the same conclusion after every time shift.

**Step 3 (stationary probability and visit frequency).** Let \(\mu\) be any invariant Borel probability supported in the box. The map is continuous, so its compact support is forward invariant. For every point in the support and each sign \(s\in\{+,-\}\), the sum of the indicator of \(\{sy>0\}\) over the first \(M_R\) iterates is at least one. Integration against \(\mu\) and invariance give \(M_R\mu\{sy>0\}\ge1\). The same disjoint-block argument gives a lower asymptotic visit frequency \(1/M_R\) for each sign along any bounded orbit.

**Step 4 (zero-feedback escape).** If \(\sigma _3=0\), the first coordinate decouples:
\[
 x_{n+1}=\sigma _1S(\beta x_n).
\]
For every \(n\ge1\), it has the sign of \(\sigma _1\) and magnitude at most \(|\sigma _1|\). For \(n\ge2\), the sigmoid's positive lower bound on the interval \([-|\beta\sigma _1|,|\beta\sigma _1|]\) yields \(|x_n|\ge\delta\). Summing \(y_{n+1}-y_n=x_n\) proves the stated linear escape, independently of the initial condition. As \(|y_n|\) then grows at least linearly, \(\eta|y_n|-1\) has eventually the constant sign of \(\eta\) and grows at least linearly in magnitude. The increments \(\sigma _2 x_n(\eta|y_n|-1)\) of \(z_n\) consequently have one fixed nonzero sign and magnitude at least a positive multiple of \(n\). Their sum gives quadratic escape. This completes the proof.

## Verification

The standalone `check.py`, requiring only the Python standard library, verifies 93 exact rational test cases of the signed coboundary on both phase half-lines, including zero endpoints; it also exercises the explicit recurrence with the parameter values reported in the source and verifies sign visits for an illustrative bounded numerical trajectory. Additional zero-feedback tests cover both signs of the sigmoid offset and several gains. The proof of the uniform all-time and all-measure conclusions above is analytic; numerical trajectories are diagnostic only.

Run: `python3 check.py`.

## Relationship to prior work

The originating article introduces the Caputo-like three-function map and reports fixed-point absence, numerical bifurcation and entropy studies, plus stabilization controls. Its Equation (9) is used here solely at integer order; no structural half-plane coboundary, uniform finite return bound, stationary sign-mass inequality, or zero-feedback global escape result is stated in the inspected material. A subsequent paper by the same authors (2025) examines a **two-dimensional** fractional memristive sigmoid model with a different second equation and no quadratic absolute-value memory feedback, so it does not cover the present recurrence.

Similar ideas of sign constraints on compact recurrence occur in other vector fields, including the indexed analysis titled *One-sided stationary geometry and forced sign crossing in the Sprott E flow*. That is a continuous-time, different-equation result, and neither its statement nor the indexed two-cell sigmoid-spiking results imply these exact three-coordinate discrete bounds. The coboundary and explicit finite-block inequality are developed here for the indicated original recurrence; no novelty is asserted for the basic Cauchy–Schwarz inequality, compactness or invariant-measure integration arguments.

## Limitations

The constants \(C_R,M_R\) are explicit **valid upper bounds**, not proven optimal and potentially very conservative. The theorem neither proves the existence of bounded chaotic attractors nor assigns their physical basins. It does not transfer to fractional orders strictly below one without new arguments: the memory kernels destroy the present one-step coboundary. It addresses exact real arithmetic, not particular finite-precision implementations. Comparison with unindexed or inaccessible mathematically equivalent publications remains incomplete, and independent mathematical validation is not claimed.

## References

1. H. Al-Taani, M. Abu Hammad, M. Abudayah, L. Diabi and A. Ouannas, *Asymmetry and Symmetry in New Three-Dimensional Chaotic Map with Commensurate and Incommensurate Fractional Orders*, Symmetry **16** (2024), 1447, first public 2024-10-31. https://doi.org/10.3390/sym16111447. Equations (9), (10), Sections 3–6.
2. H. Al-Taani, M. Abu Hammad, M. Abudayah, L. Diabi and A. Ouannas, *On Fractional Discrete Memristive Model with Incommensurate Orders: Symmetry, Asymmetry, Hidden Chaos and Control Approaches*, Symmetry **17** (2025), 143, first public 2025-01-18. https://doi.org/10.3390/sym17010143. Equation (11), Sections 2–6.
