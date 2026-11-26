# Sharp eventual-sign boundary for optimized cubic truncated-trapezoidal convolution quadrature

## Finding

For the optimized degree-three truncated-trapezoidal convolution quadrature and the positive exponential kernel \(k(t)=e^{-at}\), the weights have a sharp **eventual coefficient-sign** transition at the dimensionless step \(x=ah=141/250\):

\[
0<x<\frac{141}{250}\quad\Longleftrightarrow\quad
\exists N\ \forall n\ge N:\ \omega_n>0.
\]

For every \(x\ge141/250\), infinitely many weights are strictly positive and infinitely many are strictly negative. At the equality case, three poles have equal modulus, but an exact residue-amplitude inequality makes the signs oscillate forever. The transition lies strictly above the BDF2 exponential-CQ eventual-positivity threshold \(1/2\), but unlike BDF2, the optimized cubic scheme can have negative finite-lag weights even below its own eventual-sign threshold.

## Assumptions and scope

Let \(a>0\) and \(h>0\). Consider causal convolution by \(k(t)=e^{-at}\), with Laplace transform \(K(s)=1/(s+a)\). Let the optimized degree-three truncated trapezoidal symbol, corresponding to the source's \(J=2\) and optimal parameter \(c_2=2/3\), be

\[
\delta(z)=(1-z)+\frac12(1-z)^2+\frac23(1-z)^3.
\]

The scalar CQ weights \(\omega_n\in\mathbb R\), indexed by every integer \(n\ge0\), are defined by the convergent Taylor expansion at \(z=0\):

\[
\sum_{n=0}^{\infty}\omega_nz^n=K\bigl(\delta(z)/h\bigr)
=\frac{h}{P_x(z)},\qquad
P_x(z)=x+\frac{13}{6}-4z+\frac52z^2-\frac23z^3,
\quad x=ah>0.
\]

Here **eventually strictly positive** means that some finite index \(N\), permitted to depend on \(x\), has \(\omega_n>0\) for every \(n\ge N\). This is not a statement that every finite-lag weight is positive. Statements are in exact arithmetic; the kernel, CQ symbol and parameter are fixed as displayed.

## Proof

**1. Pole classification.** Differentiate to obtain

\[
P_x'(z)=-4+5z-2z^2=-2\left(z-\frac54\right)^2-\frac78<0
\]

for all real \(z\). Since \(P_x(1)=x>0\) and \(P_x(z)\to-\infty\) as \(z\to+\infty\), there is a unique real simple zero \(R=R(x)>1\). Its two remaining zeros \(Z,\overline Z\) are nonreal and simple. Implicit differentiation gives \(R'(x)=-1/P'_x(R)>0\).

Vieta's identities yield

\[
R+Z+\overline Z=\frac{15}{4},\qquad
R(Z+\overline Z)+|Z|^2=6,
\]

and therefore

\[
|Z|^2-R^2=6-\frac{15}{4}R.
\]

In fact, \(|Z|^2=(R-15/8)^2+159/64>1\), so all poles lie outside the closed unit disk and the defining power series is analytic there. The real and complex pole moduli coincide exactly at \(R=8/5\). Substitution in \(P_x(R)=0\) gives the unique crossing \(x_*=141/250\). Thus \(R<|Z|\) for \(0<x<x_*\) and \(R>|Z|\) for \(x>x_*\).

**2. Residue representation and the strict regimes.** Set \(g_n=\omega_n/h\). Since the poles are simple, partial fractions give, for every \(n\ge0\),

\[
g_n=C_RR^{-n}+2\operatorname{Re}(C_ZZ^{-n}),\qquad
C_\rho=-\frac{1}{\rho P'_x(\rho)},
\]

where \(C_R>0\) and \(C_Z\ne0\). If \(x<x_*\), the real-pole term dominates exponentially, so \(g_n=C_RR^{-n}(1+o(1))>0\) for all sufficiently large \(n\).

If \(x>x_*\), write \(Z=|Z|e^{i\theta}\) with \(0<\theta<\pi\), and let \(C_Z=|C_Z|e^{i\phi}\). Then

\[
|Z|^ng_n=2|C_Z|\cos(\phi-n\theta)+o(1).
\]

The cosine orbit has infinitely many values bounded away from zero with each sign: for irrational \(\theta/(2\pi)\) this follows from density of rotations, while for rational \(\theta/(2\pi)\) it follows from the zero period mean and positive period mean square, since \(\theta\notin\{0,\pi\}\). Consequently infinitely many \(g_n\) are positive and infinitely many are negative.

**3. Exact boundary.** At \(x=x_*\), factor the denominator exactly:

\[
P_{x_*}(z)=-\frac{(5z-8)(100z^2-215z+256)}{750}.
\]

Its roots are \(R=8/5\) and \(Z=(43+i\sqrt{2247})/40\) together with its conjugate. All have modulus \(8/5\). Residues satisfy

\[
C_R=\frac{125}{224},\qquad
\frac{4|C_Z|^2}{C_R^2}=\frac{128}{107}>1,
\qquad \cos\theta=\frac{43}{64}.
\]

The angle is incommensurable with \(\pi\): if \(\theta/\pi\) were rational, then \(2\cos\theta=43/32\), being a sum of roots of unity, would be an algebraic integer; a rational algebraic integer must be an integer, a contradiction. Thus \(n\theta\) is dense modulo \(2\pi\). The exact normalized coefficient

\[
R^ng_n=C_R+2|C_Z|\cos(\phi-n\theta)
\]

has infinitely many positive and negative values because \(2|C_Z|>C_R\). This proves both signs even at equality and completes the classification.

**4. Quantified distinction from all-lag positivity.** Coefficient comparison in \(P_x(z)\sum_{n\ge0}g_nz^n=1\) yields

\[
\left(x+\frac{13}{6}\right)g_n
=4g_{n-1}-\frac52g_{n-2}+\frac23g_{n-3},
\]

with \(g_0=(x+13/6)^{-1}\) and \(g_{-1}=g_{-2}=g_{-3}=0\). At \(x=11/20<x_*\), exact rational evaluation gives

\[
g_6=-\frac{1843765644000}{3057125241215467}<0.
\]

Hence eventual positivity does not imply all-lag positivity. Moreover, at the critical parameter there are negative weights arbitrarily far out. By continuity of any individual coefficient in \(x\), for each prescribed index bound there is an \(x<x_*\) sufficiently near the boundary having a negative coefficient beyond that bound. Thus no uniform eventual-positivity index exists throughout \(0<x<x_*\).

## Verification

The standalone \(\texttt{verify.py}\) checks the exact symbol, pole factorization, crossing root, residue-amplitude ratio and recurrence identities using exact rational/symbolic arithmetic. It independently reconstructs the poles and evaluates both the recurrence and residue representation in high precision for multiple parameters on both sides of the transition and at equality. The output also checks the comparisons with BDF2 and the trapezoidal rule. These finite checks support reproducibility; the infinite-sign assertions follow from the analytical proof, not from numerical enumeration.

## Relationship to prior work

Ferrari's 2026 study derives the optimized A-stable truncated trapezoidal family, including \(c_2=2/3\), and establishes error/stability properties. It does not give the scalar exponential-kernel eventual-sign boundary established here in the inspected full text. Banjai's 2022 construction and analysis of truncated trapezoidal CQ address stability and convergence in wave problems. Karaa's 2024 positivity results concern positive definiteness of convolution quadratic forms, a different property from individual nonnegative weights.

For comparison, the standard BDF2 symbol is \(\delta_{\mathrm{BDF2}}(z)=(1-z)+\frac12(1-z)^2\), whose exponential resolvent denominator changes from two positive real poles to a complex pair at \(x=1/2\). Thus its weights are eventually strictly positive for \(0<x\le1/2\) and take both signs infinitely often for \(x>1/2\). For trapezoidal CQ, the positive-lag weights are

\[
\frac{\omega_n}{h}=\frac{4}{(x+2)^2}\left(\frac{2-x}{2+x}\right)^{n-1},\qquad n\ge1,
\]

which have positive tails for \(x<2\), zero tails at \(x=2\), and alternating tails for \(x>2\). These known generating functions give context rather than an additional originality claim. Stability of a symbol, positivity of a quadratic form and positivity of each coefficient are not interchangeable.

## Limitations

The classification applies only to the displayed optimized cubic \(J=2\) symbol and to the positive single-exponential kernel. It does not establish positivity for arbitrary completely monotone kernels, general parameter choices, higher-degree truncated trapezoidal rules, multidimensional operators, or every individual weight below the boundary. In finite precision, exponentially small weights may have unreliable computed signs. Historical priority cannot be proved by finite database searches; analogous older cubic rational-sequence classifications are a residual possibility.

## References

1. Matteo Ferrari, *Convolution quadrature based on a truncated trapezoidal rule*, first public version July 13, 2026, arXiv:2607.11422v1. https://arxiv.org/abs/2607.11422
2. Lehel Banjai, *Implicit/explicit, BEM/FEM coupled scheme for acoustic waves with the wave equation in the second order formulation*, arXiv:2203.00986v1 (March 2, 2022). https://arxiv.org/abs/2203.00986
3. Samir Karaa, *Positivity of convolution quadratures generated by nonconvex sequences*, *Comptes Rendus Mathématique* 362 (2024), 1627–1634, https://doi.org/10.5802/crmath.669
4. Christian Lubich, *Convolution Quadrature Revisited*, *BIT Numerical Mathematics* 44 (2004), 503–514, https://doi.org/10.1023/B:BITN.0000046813.23911.2d
