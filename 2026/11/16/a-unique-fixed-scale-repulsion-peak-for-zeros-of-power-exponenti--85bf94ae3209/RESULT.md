# A unique fixed-scale repulsion peak for zeros of power-exponential Gaussian analytic functions

## Finding
Let the Gaussian analytic entire function \(F_\beta\), for \(\beta>0\), have independent standard circular complex Gaussian Taylor coefficients as defined below. Its ordered two-zero intensity \(\rho_{2,\beta}\), evaluated at the origin and a second point at distance \(r\), has a quadratic collision law. There are two natural ways to describe its coefficient: using the fixed complex coordinate and using the inverse square root of the mean zero density at the origin. **These coefficients have sharply different global parameter behavior.**

Put \(s=2/\beta\). Define
\[
q_\beta=2\frac{\Gamma(2s)^3}{\Gamma(s)\Gamma(3s)^2},\qquad
R_\beta=2\left(\frac{\Gamma(2s)^2}{\Gamma(s)\Gamma(3s)}\right)^2.
\]
For every fixed \(\beta>0\),
\[
\frac{\rho_{2,\beta}(0,r)}{\rho_{1,\beta}(0)\rho_{1,\beta}(r)}
=q_\beta r^2+O_\beta(r^4)
=R_\beta\left(r\sqrt{\pi\rho_{1,\beta}(0)}\right)^2+O_\beta(r^4)
\quad(r\downarrow0).
\]
Here \(\rho_{1,\beta}\) is the ordinary planar zero intensity, and angular isotropy makes \(r\) a nonnegative real separation without loss of generality.

The dimensionless density-scaled coefficient \(R_\beta\) is **strictly increasing in \(\beta\)**, with exact range
\[
0<R_\beta<\frac98,\quad R_2=\frac12,\quad
\lim_{\beta\to\infty}R_\beta=\frac98,
\quad R_\beta\sim\frac32\left(\frac{256}{729}\right)^{2/\beta}
\quad(\beta\downarrow0).
\]
By contrast, the fixed-coordinate coefficient \(q_\beta\) increases strictly from zero to one unique global maximum and then decreases strictly to \(9/4\). Its maximizer is the unique \(\beta_*=2/s_*\), where \(s_*>0\) solves
\[
6\psi(2s_*)-\psi(s_*)-6\psi(3s_*)=0,
\]
with \(\psi\) the digamma function. Numerically,
\[
\beta_*=33.4696165996277\ldots,\qquad
q_{\beta_*}=2.28684093883297\ldots.
\]
Thus an apparent fixed-coordinate peak in zero repulsion disappears when separations are measured in units of the local mean zero spacing. The two assertions form a single complete parameter classification of the leading collision invariant in these two canonical scales.

## Assumptions and scope
For each \(\beta>0\) put \(s=2/\beta\) and
\[
F_\beta(z)=\sum_{n=0}^\infty \xi_n\frac{z^n}{\sqrt{\Gamma(s(n+1))}},\qquad z\in\mathbb C,
\]
where the \(\xi_n\) are independent standard circular complex Gaussian variables satisfying \(\mathbb E|\xi_n|^2=1\). Almost surely the series defines an entire function. Define \(a_n=1/\Gamma((n+1)s)>0\), and \(K(z,w)=\sum_{n\ge0}a_n(z\overline w)^n\). The intensity \(\rho_{1,\beta}(z)\) is the density of the expected number of zeros with respect to planar Lebesgue area; \(\rho_{2,\beta}(z,w)\) is the factorial second intensity of **ordered distinct zeros**, not the density of a zero conditional on another zero. For distinct arguments it is given by the complex Kac–Rice formula. The little- and big-O statements hold for each fixed finite \(\beta\) as \(r\to0\), not uniformly over all \(\beta\). The parameter \(r\) is in the original complex plane, with no large-hole conditioning.

## Proof
**First intensity.** The Edelman–Kostlan identity gives \(\rho_{1,\beta}(z)=\pi^{-1}\partial_z\partial_{\overline z}\log K(z,z)\). In particular
\[
\rho_{1,\beta}(0)=\frac{a_1}{\pi a_0}>0.
\]
Rotational symmetry yields \(\rho_{1,\beta}(r)=\rho_{1,\beta}(0)+O_\beta(r^2)\).

**Collision expansion.** Take \(r>0\). The two independent complex Gaussian constraints \(F_\beta(0)=0\) and \(Y_r=(F_\beta(r)-F_\beta(0))/r=0\) have variances \(a_0\) and \(a_1+O_\beta(r^2)\), respectively. Consequently the joint density of \((F_\beta(0),F_\beta(r))\) at zero is
\[
\frac{1}{\pi^2a_0a_1r^2}\bigl(1+O_\beta(r^2)\bigr).
\]
Let \(T_r=\sum_{n\ge2}\sqrt{a_n}\xi_n r^{n-2}\) and \(U_r=\sum_{n\ge2}(n-1)\sqrt{a_n}\xi_n r^{n-2}\). The condition \(Y_r=0\) implies the **exact** derivative identities \(F_\beta'(0)=-rT_r\) and \(F_\beta'(r)=rU_r\). Conditional on that constraint, both \(T_r\) and \(U_r\) converge in mean square to \(\sqrt{a_2}\xi_2\) as \(r\downarrow0\): conditioning changes their covariance by \(O_\beta(r^2)\), since their covariances with \(Y_r\) are \(O_\beta(r)\). For a circular complex Gaussian \(\xi_2\), \(\mathbb E|\xi_2|^4=2\). Complex Wick's formula therefore gives
\[
\mathbb E\bigl(|F_\beta'(0)F_\beta'(r)|^2\,\big|\,F_\beta(0)=F_\beta(r)=0\bigr)
=2a_2^2r^4+O_\beta(r^6).
\]
Here the \(O(r^6)\) follows because every relevant covariance is real analytic in \(r^2\); in particular the order-\(r^3\) cross covariances contribute only even powers to the fourth moment. The two-point complex Kac–Rice formula now yields
\[
\rho_{2,\beta}(0,r)=\frac{2a_2^2}{\pi^2a_0a_1}r^2+O_\beta(r^4).
\]
Dividing by the two one-point intensities and using the density-scaled separation \(t=r\sqrt{a_1/a_0}\) gives exactly the formulas for \(q_\beta\) and \(R_\beta\). The limiting coefficient depends on the first three Taylor variances but not on higher coefficients.

**Gamma-ratio monotonicity.** Write \(J(s)=\Gamma(2s)^2/[\Gamma(s)\Gamma(3s)]\). Gauss's duplication and triplication formulas imply the exact identity
\[
J(s)=\frac{\sqrt3}{2}\left(\frac{16}{27}\right)^s
\frac{\Gamma(s+\frac12)^2}{\Gamma(s+\frac13)\Gamma(s+\frac23)}.
\]
The trigamma \(\psi_1(x)=\psi'(x)=\sum_{n\ge0}(n+x)^{-2}\) is strictly positive and strictly convex on \((0,\infty)\), since \(\psi_1''(x)=6\sum_{n\ge0}(n+x)^{-4}>0\). Hence
\[
\frac{d^2}{ds^2}\log J(s)
=2\psi_1(s+\tfrac12)-\psi_1(s+\tfrac13)-\psi_1(s+\tfrac23)<0.
\]
The gamma expansion \(\Gamma(x)=x^{-1}-\gamma_{\rm E}+O(x)\) gives \(\lim_{s\downarrow0}(\log J)'(s)=0\). Strict concavity therefore forces \(J'(s)<0\) for all \(s>0\). As \(s\) decreases strictly with \(\beta\), \(R_\beta=2J(s)^2\) increases strictly with \(\beta\). Gamma limits at zero give \(J(0+)=3/4\); Stirling asymptotics give \(J(s)\sim(\sqrt3/2)(16/27)^s\) as \(s\to\infty\), proving the stated endpoint bounds and sharp asymptotics.

**Unique fixed-scale maximum.** The same multiplication identities give
\[
q(s)=3\sqrt\pi\left(\frac23\right)^{6s}
\frac{\Gamma(s+\frac12)^3}{\Gamma(s+\frac13)^2\Gamma(s+\frac23)^2}.
\]
Consequently,
\[
(\log q)''(s)=3\psi_1(s+\tfrac12)
-2\psi_1(s+\tfrac13)-2\psi_1(s+\tfrac23)
< -\psi_1(s+\tfrac12)<0,
\]
again by midpoint convexity of trigamma. The small-\(s\) gamma expansion yields \((\log q)'(0+)=\gamma_{\rm E}>0\), while Stirling's formula gives \((\log q)'(s)=-\log s+O(1)\to-\infty\) as \(s\to\infty\). Thus the derivative has exactly one zero \(s_*\), given equivalently by the displayed digamma equation. The derivative changes from positive to negative there, proving its unique global maximum. Since the change of variables \(s=2/\beta\) reverses order, \(q_\beta\) increases then decreases as \(\beta\) rises. Finally \(q(0+)=9/4\) and \(q(\infty)=0\), establishing its full endpoint behavior. The decimal brackets follow from straightforward high-precision one-variable evaluation and are not needed to prove uniqueness.

## Verification
Run \(\texttt{python CHECK.py}\) with the dependency in \(\texttt{requirements.txt}\). It separately reconstructs the complex Gaussian conditional covariance and evaluates the exact two-point Kac–Rice formula for seven values of \(\beta\), compares it with the predicted quadratic collision coefficient at three separations each, checks the Gauss multiplication identities, samples trigamma midpoint convexity, and isolates the unique critical parameter numerically. The saved test passes 199 finite assertions. The all-parameter monotonicity and uniqueness are proved by the strict trigamma-convexity argument above; numerical samples do not certify them.

## Relationship to prior work
Du, *Hole Phenomenon of Gaussian Analytic Functions with Power-exponential Weights* (arXiv:2602.24193, first publicly submitted 27 February 2026), fixes precisely this Gaussian analytic family and studies the distribution of its zeros conditioned on a large zero-free disk. Its theorems and proof concern large-disk hole probabilities, limiting zero measures, and constrained logarithmic energy. The cited source does not state a microscopic two-zero collision coefficient, its two normalizations, the fixed-coordinate unique-maximum law, or density-scaled monotonicity. Its macroscopic forbidden annulus has outer radius \(e^{1/\beta}\); increasing this radius corresponds to decreasing the dimensionless microscopic repulsion \(R_\beta\), a contrast of scales rather than an implication of the hole theorem.

Hough, Krishnapur, Peres and Virág, *Zeros of Gaussian Analytic Functions and Determinantal Point Processes* (2009), provides the established general Gaussian zero-intensity and Hammersley/Kac–Rice framework. The collision expansion above is a specialization of that general framework; **it is not claimed as a newly invented Kac–Rice formula**. The new mathematical assertion is the full-parameter comparative law and the distinct strict one-peak and monotone phase diagrams obtained by combining the collision coefficient with special-function analysis. The earlier reciprocal-Gamma boundary-layer study of the same family concerns zeros near an expanding logarithmic circle, not two-point collisions at the origin. This comparison is about statements and scales, not merely matching terminology.

## Limitations
The theorem concerns **unconditioned ordered two-point intensities at the origin** for independent circular Gaussian coefficients and power-exponential radial weights. It does not give whole-plane pair correlations, finite-separation distributions, the law of the nearest neighbor, or the probability of two or more zeros in a small disk. Neither the strict monotonicity nor the unique peak should be extrapolated to other radial weights without additional hypotheses. Prior general Hammersley formulas are acknowledged; equivalently parameterized special-function inequalities or other earlier exact specializations may remain a publication-priority risk. Independent mathematical and priority review have not been performed.

## References
1. Y.-H. Du, *Hole Phenomenon of Gaussian Analytic Functions with Power-exponential Weights*, arXiv:2602.24193v1 (27 February 2026), https://arxiv.org/abs/2602.24193 .
2. J. B. Hough, M. Krishnapur, Y. Peres and B. Virág, *Zeros of Gaussian Analytic Functions and Determinantal Point Processes*, AMS University Lecture Series 51 (2009), DOI:10.1090/ULECT/051 .
3. The classical Gauss multiplication formulas for \(\Gamma\) and the polygamma series identities (standard special-function facts, proved or recalled where used above).
