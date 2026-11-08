# Stable fear-cost patterns at an exact first Turing threshold

## Finding

Consider the cost-of-fear, ratio-dependent predator–prey reaction–diffusion equations
\[
\begin{aligned}
\partial_t u&=\partial_{xx}u+\frac{4u}{1+\kappa v}-u-u^2-\frac{2uv}{u+v},\\
\partial_t v&=100\partial_{xx}v+v\left(-1+\frac{2u}{u+v}\right)
\end{aligned}
\]
with homogeneous Neumann boundaries on \(x\in[0,\pi\sqrt{10}]\), and \(\kappa\ge0\). This is a positive-parameter instance of the *random-diffusion, fear-cost-only, ratio-dependent* special case (81) in Wang–Zou [1].

Set
\[
h_c=42-\frac{\sqrt{43410}}5,\qquad
\kappa_c=\frac{2-h_c}{h_c(2+h_c)}\approx2.17310839659585.
\]
At \(\kappa_c\), a single real first-Neumann eigenvalue passes through zero while every other spectral value stays in the open left half-plane. The nonlinear bifurcation is **supercritical**: for all sufficiently small \(\mu=\kappa-\kappa_c>0\), there are two distinct, positive, spatially nonconstant, locally exponentially stable steady states interchanged by reflection of the habitat. In contrast, the homogeneous state is unstable for \(\mu>0\). Each patterned profile has the expansion
\[
\binom{u(x)}{v(x)}=\binom{h(\kappa)}{h(\kappa)}
\pm t\binom{1}{1/21}\cos\!\left(\frac{x}{\sqrt{10}}\right)+O(t^2),
\qquad
 t^2=-\frac{S}{C}\,\mu+O(\mu^2),
\]
where \(S>0\) and \(C<0\) are the exact center amplitude coefficients below. The remainder is in the Neumann \(H^2\) norm; this is a local theorem only.

## Assumptions and scope

All biological coefficients in the displayed equations are fixed, positive rational numbers. The only varied coefficient is the nonnegative fear/reproduction-cost parameter \(\kappa\); directed prey avoidance is absent, as allowed in [1, Eq. (81)]. Initial states and local steady states are strictly positive, with the denominator \(u+v\) bounded away from zero in the neighborhood studied. Boundary conditions are homogeneous Neumann for both species. The stability assertion is for the autonomous infinite-dimensional reaction–diffusion semiflow in a sufficiently small neighborhood of each steady state, with nonnegative smooth perturbations; no claim is made for general initial states.

## Proof

**Equilibrium and spectral isolation.** Every positive uniform equilibrium has \(u=v=h\), and the prey balance yields \((2+h)(1+\kappa h)=4\), or \(\kappa=(2-h)/[h(2+h)]\). The map from \(h\in(0,2]\) to \(\kappa\in[0,\infty)\) is strictly decreasing. Along this equilibrium curve the reaction Jacobian simplifies exactly to
\[
J(h)=\begin{pmatrix}1/2-h&-3/2+h^2/4\\1/2&-1/2\end{pmatrix}.
\]
Its trace is \(-h<0\) and determinant is \((4+4h-h^2)/8>0\). The Neumann wavenumbers are \(q_n=n^2/10\). The spatial mode \(n\) has matrix \(A_n=J(h)-q_n\operatorname{diag}(1,100)\), trace \(-h-101q_n<0\) and determinant
\[
D_n(h)=100q_n^2-\frac{99}{2}q_n+\frac12
 +\left(100q_n+\frac12\right)h-\frac{h^2}8.
\]
The first-mode equation \(D_1(h)=0\) is \(5h^2-420h+138=0\), whose only root in \((0,2)\) is \(h_c\). Since \(D_1\) is strictly increasing in \(h\) there, this is a simple crossing. At \(h_c\), \(D_2(h_c)>0\) (the unique second-mode threshold lies at \(0.0815<h<0.0816\)); for \(n\ge3\), \(D_n(0)>0\) and \(D_n'(h)>0\) on \((0,2)\). The uniform mode also stays strictly stable. Therefore the only center direction at \(\kappa_c\) is \(r\cos(x/\sqrt{10})\) with \(r=(1,1/21)^T\), and the rest of the spectrum has a negative gap. Since \(h'(\kappa)<0\), the first-mode eigenvalue increases through zero as \(\kappa\) increases.

**Nonlinear coefficient.** Write \(F=(f,g)^T\), and denote its second and third derivatives at \((h_c,h_c;\kappa_c)\) by bilinear \(H\) and trilinear \(Q\). Put \(A_0=J(h_c)\), \(A_2=J(h_c)-4\operatorname{diag}(1,100)/10\), and
\[
w_0=-\frac14 A_0^{-1}H(r,r),\qquad
w_2=-\frac14 A_2^{-1}H(r,r).
\]
The first-mode left nullvector, normalized by \(\ell^Tr=1\), is
\[
\ell=\frac{105}{101+10h_c}(1,\,2h_c-4/5)^T.
\]
Reflection \(x\mapsto\pi\sqrt{10}-x\) sends the critical cosine to its negative. Thus the one-dimensional center reduced vector field contains only odd powers of amplitude \(t\). Its linear unfolding coefficient and cubic coefficient are exactly
\[
\begin{aligned}
S&=\ell^T\frac{dJ(h(\kappa))}{d\kappa}\bigg|_{\kappa_c}r,\\
C&=\ell^T\left[H(r,w_0)+\frac12H(r,w_2)+\frac18 Q(r,r,r)\right].
\end{aligned}
\]
The factors \(1/4,1/2,1/8\) follow from \(\cos^2\theta=(1+\cos2\theta)/2\), \(\cos\theta\cos2\theta=(\cos\theta+\cos3\theta)/2\), and \(\cos^3\theta=(3\cos\theta+\cos3\theta)/4\). Exact symbolic differentiation and reduction modulo \(5h_c^2-420h_c+138=0\) give
\[
S=\frac{3(53521537h_c-17655030)}{187410h_c-63179},
\]
\[
C=-\frac{16(515234276817020h_c-169961218676239)}{2056513536(72313693080h_c-23853887351)}.
\]
The rational isolation interval \(0.329866810868002697<h_c<0.329866810868002700\) yields \(0.11322<S<0.11323\) and \(-0.60379<C<-0.60377\) by exact rational comparisons; in particular \(S>0\) and \(C<0\).

**Existence and stability.** Lyapunov–Schmidt reduction (equivalently the analytic parabolic center manifold) now gives the reflection-odd amplitude equation
\[
\dot t=S\mu t+Ct^3+O(\mu^2|t|+|\mu||t|^3+|t|^5),\qquad \mu=\kappa-\kappa_c.
\]
The implicit function theorem after dividing by \(t\) produces precisely two nonzero equilibria near the origin for small \(\mu>0\), with the claimed squared-amplitude expansion. Their center eigenvalue is \(-2S\mu+O(\mu^2)<0\), and the uniformly negative complementary spectrum persists. Hence both are locally exponentially stable; reflection exchanges them. Positivity follows from uniform proximity to the strictly positive equilibrium. For small \(\mu<0\), no nearby nonconstant branch is present, and the homogeneous state is linearly asymptotically stable.

## Verification

The accompanying standalone `verify.py` differentiates the original rational reactions, reconstructs the Hessian and third-order tensor, solves the two harmonic correction equations, computes the cubic normal-form coefficient and reduces it modulo the exact threshold polynomial. Its independent interval-sign checks use rational endpoints, not floating point proofs. Run `python verify.py` with SymPy installed. The exact derivative and modal relations are mathematical identities, while the interval tests certify the requisite signs.

## Relationship to prior work

Wang and Zou [1], notably the fear-cost-only specialization (81) and its discussion, derived linear Turing-instability conditions and illustrated fear-dependent spatial patterns numerically. The onset of a potentially unstable spatial mode is therefore **not** claimed as new. The result here classifies the nonlinear *first-mode bifurcation*: it supplies an exact cubic sign, two positive patterned equilibrium branches, and their local asymptotic stability, none of which follows solely from the source's linear instability inequalities. Song and Zou [2] studied weakly nonlinear Turing–Hopf dynamics for a *different, cost-free* ratio-dependent system, so their normal form is not an evaluation for [1, Eq. (81)].

## Limitations

The theorem applies to one fixed, positive-parameter, one-dimensional Neumann specialization. Stability is local; no global patterned-state attraction or persistence under arbitrary perturbations is proved. The sign certificate derives from exact algebraic specialization and does not claim a universal cubic sign over all fear-cost models. The literature comparison is best-knowledge, not a proof of publication priority; structurally equivalent calculations outside the checked sources may exist. Independent external verification has not been performed.

## References

[1] X. Wang and X. Zou, *Pattern formation of a predator-prey model with the cost of anti-predator behaviors*, Mathematical Biosciences and Engineering 15 (2018), 775–805, https://doi.org/10.3934/mbe.2018035 (publisher lists publication date 2018-06-01).

[2] Y. Song and X. Zou, *Spatiotemporal dynamics in a diffusive ratio-dependent predator-prey model near a Hopf–Turing bifurcation point*, Computers & Mathematics with Applications 67 (2014), 1978–1997, https://doi.org/10.1016/j.camwa.2014.04.015.
