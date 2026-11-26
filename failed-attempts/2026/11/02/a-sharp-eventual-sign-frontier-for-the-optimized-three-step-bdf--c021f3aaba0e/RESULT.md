# A sharp eventual-sign frontier for the optimized three-step BDF-like Green sequence

## Finding

Consider the second-order, three-step A-stable and L-stable BDF-like formula
\[
y_{n+3}=\frac32y_{n+2}-\frac35y_{n+1}+\frac1{10}y_n+\frac35h f_{n+3},
\]
called BDFL\(3_2\), or BDF2OPT(4), in the cited literature. For the scalar decay equation \(y'=-\lambda y+\lambda v\), with \(\lambda>0\), \(h>0\), and \(\mu=h\lambda\), its zero-prehistory causal Green coefficients satisfy
\[
G_{-2}=G_{-1}=0,\quad G_0=1,\quad
G_n=\frac{15G_{n-1}/2-3G_{n-2}+G_{n-3}/2}{5+3\mu}\quad(n\ge1).
\]
The following is an exact infinite-index classification:
\[
\boxed{\text{\(G_n\) is strictly positive for all sufficiently large \(n\)}
\quad\Longleftrightarrow\quad 0<\mu<\frac{15}{16}.}
\]
At every \(\mu\ge15/16\), infinitely many coefficients are strictly positive and infinitely many strictly negative. The endpoint is included in the oscillatory regime, not in the eventual-positive regime.

There is a distinct, nonempty open interval of transient sign failure *below* the eventual-sign boundary. At \(\mu=187/200<15/16\),
\[
G_6=-\frac{1262437317590000}{14468297105020833361}<0,
\]
although all sufficiently late coefficients are positive. Define the normalized causal convolution gain
\[
\Lambda(\mu)=\frac{3\mu}{5+3\mu}\sum_{n=0}^{\infty}|G_n|.
\]
It is finite for all \(\mu>0\), and at \(\mu=187/200\) it is strictly greater than one despite eventual positivity. Indeed \(\Lambda(\mu)>1\) whenever any \(G_n<0\), including throughout the oscillatory regime.

## Assumptions and scope

All parameters and coefficients are real and evaluated in exact arithmetic. The formula is used at constant step \(h\), with the scalar dissipative test mode \(\lambda>0\). Zero prehistory means that the causal response to \(v_n\) is \(y_n=(3\mu/(5+3\mu))\sum_{j=0}^n G_jv_{n-j}\) with earlier values set to zero. This is a forcing Green sequence, not an arbitrary three-value starter for the homogeneous multistep recurrence. Eventual positivity means existence of a parameter-dependent integer \(N\) such that \(G_n>0\) for every integer \(n\ge N\). The theorem does not assert that all coefficients are positive for every \(0<\mu<15/16\).

## Proof

**1. Stable cubic and its roots.** Put \(s=5/(5+3\mu)\in(0,1)\). The Green generating function and characteristic polynomial are
\[
F(z)=\sum_{n\ge0}G_nz^n=\frac{1}{1-\frac32sz+\frac35sz^2-\frac1{10}sz^3},
\qquad
P_s(X)=X^3-\frac32sX^2+\frac35sX-\frac1{10}s.
\]
The cubic discriminant equals
\[
\operatorname{disc}(P_s)=-\frac{27s^2}{500}(10s^2-14s+5)<0,
\]
since the last quadratic is \(10(s-7/10)^2+1/10\). There is one positive real root \(R\) and one nonreal conjugate pair \(u,\overline u\), with \(m=|u|\). Substitution of \(R\) into \(P_s(R)=0\) gives
\[
s=\frac{10R^3}{15R^2-6R+1},\qquad
\frac{ds}{dR}=\frac{10R^2(15R^2-12R+3)}{(15R^2-6R+1)^2}>0.
\]
Consequently \(R\) runs strictly from zero to one as \(s\) runs from zero to one. Vieta's product yields
\[
m^2=\frac{s}{10R}=\frac{R^2}{15R^2-6R+1}.
\]
All three characteristic roots are strictly inside the unit circle: \(R<1\), and \(15R^2-6R+1-R^2=14R^2-6R+1>0\), hence \(m<1\). This also justifies absolute convergence of \(F(1)\) and of \(\sum |G_n|\).

**2. Exact dominant-modulus crossing.** The sign of \(m/R-1\) is governed by
\[
(15R^2-6R+1)-1=3R(5R-2).
\]
Thus \(R>m\) for \(R>2/5\), and \(m>R\) for \(R<2/5\). The equality \(R=2/5\) corresponds to \(s=16/25\), equivalently \(\mu=15/16\). Since the poles are simple and nonzero, partial fractions give
\[
G_n=A R^n+B u^n+\overline B\,\overline u^{\,n},\quad
A=\frac{R^2}{|R-u|^2}>0,\quad
B=\frac{u^2}{(u-R)(u-\overline u)}\ne0.
\]
When \(0<\mu<15/16\), \(R>m\), so \(G_n/R^n\to A>0\) and eventual strict positivity follows.

**3. Infinitely many sign changes above the boundary.** When \(\mu>15/16\), write \(u=me^{i\theta}\) with \(0<\theta<\pi\). The dominant term is \(2m^n\operatorname{Re}(Be^{in\theta})\), while \(AR^n=o(m^n)\). If \(\theta/(2\pi)\) is irrational, phase density supplies infinitely many indices in positive and negative arcs bounded away from zero. If the angle is rational, the nonconstant periodic real sequence \(\operatorname{Re}(Be^{in\theta})\) has mean zero and is not identically zero (because \(B\ne0\) and \(\theta\notin\{0,\pi\}\)); it therefore has both signs in every period. Hence both signs occur infinitely often in \(G_n\).

**4. The equal-modulus endpoint.** For \(\mu=15/16\), the roots are exactly
\[
R=\frac25,\qquad u=\frac{7+i\sqrt{51}}{25},\qquad \overline u=\frac{7-i\sqrt{51}}{25}.
\]
The real-mode coefficient equals \(A=5/3\), while the oscillatory amplitude obeys
\[
\left(\frac{2|B|}{A}\right)^2=\frac{20}{17}>1.
\]
Here \(\cos\theta=7/10\). If \(\theta/\pi\) were rational, \(e^{i\theta}\) would be a root of unity, forcing \(2\cos\theta=7/5\) to be a rational algebraic integer, hence an integer. This is impossible. Thus the endpoint phases are dense, and the oscillatory component exceeds the positive real component on infinitely many negative as well as positive subsequences. The endpoint also has infinitely many coefficients of each sign.

**5. A strict transient-versus-eventual gap.** Applying the recurrence exactly six times gives
\[
G_6(\mu)=\frac{1296\mu^4-154656\mu^3+1440720\mu^2-2997300\mu+1667125}{64(5+3\mu)^6}.
\]
At \(\mu=187/200\), this is the strictly negative rational value in the Finding. Since \(187/200<15/16\), Step 2 proves that the same sequence eventually becomes strictly positive. Strict inequalities and continuity give a nonempty open interval of parameters with both properties. Finally, summing the convergent generating series gives
\[
F(1)=\frac{5+3\mu}{3\mu},\qquad
\frac{3\mu}{5+3\mu}\sum_{n\ge0}G_n=1.
\]
Replacing signed coefficients by absolute values strictly increases the sum whenever any coefficient is negative. This proves the convolution gain claim.

## Verification

The standalone script `verify.py` reproduces the cubic discriminant, real-root parameterization, equal-modulus factorization, endpoint amplitude ratio, the exact sixth Green coefficient and rational witness, and the total-mass identity. It also checks the scalar coefficient recurrence and several representative root configurations using numerical computations. Execute `python3 verify.py` with SymPy installed. The exact algebraic identities and the preceding analytic arguments, not finite numerical samples, establish the infinite-index assertions.

## Relationship to prior work

Jensen, Ketcheson, and Lóczi (2026) establish the displayed BDFL\(3_2\) coefficient formula, its optimal second-order local error constant \(-1/6\), and A-/L-stability; their analysis addresses root-location stability, optimized local error, and adaptive implementation, not the sign of the causal forced Green coefficients. Vatsa, Carpenter, and Lockard (2010) earlier studied BDF2OPT(4), distinguishing A-stability from the instability of a different coefficient choice. Neither analysis implies coefficientwise eventual positivity merely from A-stability. For context, the classical BDF2 causal Green sequence has an eventual-sign boundary at \(\mu=1/2\), obtained from the real-versus-complex transition of its quadratic characteristic polynomial. The optimized three-step scheme's \(15/16\) boundary is therefore larger by a factor of \(15/8\). General eventual-positivity criteria for recurrences explain the usefulness of a unique dominant positive root, but do not supply the present method-specific endpoint amplitude or transient-gain witness.

## Limitations

This is a scalar, constant-step, zero-prehistory result for one optimized second-order three-step scheme. It does not classify all-index positivity, positivity under arbitrary starters, positivity preservation for nonlinear equations, or variable-step schemes. In particular, eventual positivity alone is not a guarantee of a nonnegative forced response at all times. A previously unlocated specialized treatment of this exact Green sequence remains a possible historical-priority risk.

## References

1. T. Jensen, D. I. Ketcheson, L. Lóczi, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1, first publicly posted October 15, 2026. https://arxiv.org/html/2610.22685v1
2. V. N. Vatsa, M. H. Carpenter, D. P. Lockard, *Re-evaluation of an Optimized Second Order Backward Difference (BDF2OPT) Scheme for Unsteady Flow Applications*, AIAA 2010-0122 (2010), NASA NTRS 20100002944. https://ntrs.nasa.gov/citations/20100002944
3. A. Sootla, *Properties of eventually positive linear input–output systems*, IET Control Theory & Applications 13 (2019), 891–897. https://doi.org/10.1049/iet-cta.2018.5231
4. Z. Li, *Positivity of arbitrary-order P-recursive sequences with a unique dominant root*, arXiv:2605.17013 (2026). https://arxiv.org/abs/2605.17013
