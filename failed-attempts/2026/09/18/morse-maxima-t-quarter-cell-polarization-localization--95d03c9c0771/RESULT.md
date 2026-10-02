# Morse maxima force a t^{-1/4} localization law in the slow cell-polarization limit

## Result

Consider the infinite-cytosolic-diffusion slow-limit system of Niethammer--Roeger--Velazquez (arXiv:2609.20609v1) on a smooth closed two-dimensional membrane \(\Gamma\):

\[
\partial_t u=-(1-g)\xi+\alpha g,\qquad
u\ge 0,\quad 0\le \xi\le1,\quad u\xi=u,
\]

\[
\alpha(t)=\frac{\int_{\{u(\cdot,t)>0\}}(1-g)\,d\sigma}
{\int_{\{u(\cdot,t)>0\}}g\,d\sigma},
\qquad \int_\Gamma u(\cdot,t)\,d\sigma=1,
\]

with time-independent signal \(g\) and nonnegative \(u_0\in C(\Gamma)\). Write

\[
g_{\max}=\max_\Gamma g,\qquad
\alpha_* = \frac{1-g_{\max}}{g_{\max}},\qquad
h=\frac{g_{\max}-g}{g_{\max}}.
\]

Assume that \(h\) has exactly finitely many zeros \(x_1,\dots,x_M\), each a nondegenerate minimum, and let

\[
H_j=D_\Gamma^2h(x_j)>0,
\qquad
C:=\pi\sum_{j=1}^M (\det H_j)^{-1/2}.
\]

Then the long-time localization in the slow-limit dynamics has a sharp algebraic scale. If

\[
\varphi(t):=(\alpha(t)-\alpha_*)g_{\max},\qquad
A(t):=\int_0^t\varphi(s)\,ds,
\]

then, as \(t\to\infty\),

\[
\boxed{A(t)\sim \sqrt{\frac{t}{C}}},
\qquad
\boxed{\varphi(t)\sim \frac{1}{2\sqrt{Ct}}},
\qquad
\boxed{\alpha(t)-\alpha_*\sim \frac{1}{2g_{\max}\sqrt{Ct}}}.
\]

The concentration width is of order \(t^{-1/4}\), while the peak height is of order \(t^{1/2}\). More precisely,

\[
\boxed{u(x_j,t)\sim \sqrt{\frac{t}{C}}}
\]

for every maximum \(x_j\). In geodesic normal coordinates \(z\) centered at \(x_j\), the positivity set satisfies, for every \(\varepsilon>0\) and all sufficiently large \(t\),

\[
\left\{|H_j^{1/2}z|<(\sqrt2-\varepsilon)(Ct)^{-1/4}\right\}
\subset \{u(\cdot,t)>0\}
\]

locally near \(x_j\), while locally

\[
\{u(\cdot,t)>0\}
\subset
\left\{|H_j^{1/2}z|<(\sqrt2+\varepsilon)(Ct)^{-1/4}\right\}.
\]

Thus the shrinking support is asymptotically Hessian-elliptic with semiaxes proportional to \(t^{-1/4}\).

There is also a universal local profile. Define

\[
\tau(t):=t+A(t),\qquad q(t):=\frac{A(t)}{\tau(t)}.
\]

Then

\[
q(t)\sim \frac{1}{\sqrt{Ct}},\qquad \tau(t)q(t)^2\to \frac1C.
\]

For bounded \(y\in\mathbb R^2\), set

\[
z=\sqrt{q(t)}\,H_j^{-1/2}y.
\]

Then

\[
\boxed{
\frac{u(\exp_{x_j}z,t)}{\tau(t)q(t)}
\longrightarrow
\left(1-\frac{|y|^2}{2}\right)_+
}
\]

locally uniformly in \(y\). Equivalently, the rescaled local mass measure converges to

\[
\boxed{
\frac{1}{C\sqrt{\det H_j}}
\left(1-\frac{|y|^2}{2}\right)_+\,dy.
}
\]

Its total mass is

\[
\frac{\pi}{C\sqrt{\det H_j}}
=
\frac{(\det H_j)^{-1/2}}
{\sum_k(\det H_k)^{-1/2}},
\]

recovering the determinant weights identified in Section 4 of the source paper, but now as the integral of a full time-dependent local profile.

## Proof

The source paper introduces

\[
\varphi=(\alpha-\alpha_*)g_{\max},\qquad
h=\frac{g_{\max}-g}{g_{\max}},
\]

and obtains

\[
\partial_tu=(\varphi-h-\varphi h)\chi_{\{u>0\}},
\qquad
\varphi(t)=\frac{\int_{S(t)}h\,d\sigma}
{\int_{S(t)}(1-h)\,d\sigma},
\]

where \(S(t)=\{u(\cdot,t)>0\}\). Its representation formula therefore becomes exactly

\[
u(x,t)=\left[u_0(x)+A(t)-(t+A(t))h(x)\right]_+.
\]

With \(\tau=t+A\) and \(q=A/\tau\), this is

\[
\boxed{u(x,t)=\tau(t)\left[q(t)-h(x)+\frac{u_0(x)}{\tau(t)}\right]_+.}
\]

The source proves \(\alpha(t)\downarrow\alpha_*\), hence \(\varphi(t)\to0\). Consequently \(A(t)=o(t)\), \(\tau(t)\sim t\), and \(q(t)\to0\).

Let

\[
G(s):=\int_\Gamma(s-h)_+\,d\sigma.
\]

At a nondegenerate minimum, in normal coordinates,

\[
h(z)=\frac12 z^TH_jz+o(|z|^2).
\]

A quadratic change of variables gives

\[
G(s)=Cs^2+o(s^2),
\qquad
C=\pi\sum_j(\det H_j)^{-1/2}.
\]

Let \(M_0=\|u_0\|_\infty\). Mass conservation and \(u_0\ge0\) imply

\[
G(q(t))\le \frac1{\tau(t)}
\le G\left(q(t)+\frac{M_0}{\tau(t)}\right).
\]

The quadratic asymptotic for \(G\) first yields \(q(t)\asymp\tau(t)^{-1/2}\), so \(M_0/\tau=o(q)\). Applying the same squeeze again gives

\[
C\tau q^2\to1.
\]

Since \(t=\tau(1-q)\), it follows that \(\tau\sim t\),

\[
q(t)\sim(Ct)^{-1/2},
\qquad
A(t)=\tau q\sim\sqrt{t/C}.
\]

At every maximum \(x_j\), \(h(x_j)=0\), so the exact representation gives

\[
u(x_j,t)=u_0(x_j)+A(t)\sim\sqrt{t/C}.
\]

To obtain \(\varphi\), define the sublevel quantities

\[
L(s):=|\{h<s\}|,
\qquad
N(s):=\int_{\{h<s\}}h\,d\sigma.
\]

The same quadratic local calculation gives

\[
L(s)=2Cs+o(s),
\qquad
N(s)=Cs^2+o(s^2).
\]

From the representation formula,

\[
\{h<q\}\subset S(t)
\subset\left\{h<q+\frac{M_0}{\tau}\right\}.
\]

Because \(M_0/\tau=o(q)\),

\[
|S(t)|\sim2Cq,
\qquad
\int_{S(t)}h\,d\sigma\sim Cq^2.
\]

Hence

\[
\varphi(t)
=\frac{\int_{S(t)}h}{\int_{S(t)}(1-h)}
\sim\frac{Cq^2}{2Cq}
=\frac q2
\sim\frac{1}{2\sqrt{Ct}},
\]

which also yields the stated rate for \(\alpha-\alpha_*\).

Finally, put \(z=\sqrt q\,H_j^{-1/2}y\). Uniformly for bounded \(y\),

\[
h(\exp_{x_j}z)
=q\left(\frac{|y|^2}{2}+o(1)\right),
\qquad
\frac{u_0}{\tau q}=o(1).
\]

Thus the normalized density tends locally uniformly to the parabolic cap
\((1-|y|^2/2)_+\). The surface element satisfies

\[
d\sigma=\frac{q}{\sqrt{\det H_j}}(1+o(1))\,dy,
\]

and \(\tau q^2\to1/C\), proving the rescaled mass-profile formula and the support inclusions.

## Relation to prior work

The source paper, arXiv:2609.20609v1, proves concentration of the support for the slow-time limit and characterizes subsequential limiting mass distributions. In its nondegenerate-minimum example it obtains the weights proportional to \((\det H_j)^{-1/2}\). It does not state a temporal localization rate, a \(t^{-1/4}\) support law, a \(t^{1/2}\) peak law, the \(t^{-1/2}\) multiplier gap, or the rescaled parabolic-cap profile.

A closely related 2026 preprint, arXiv:2605.03553v1, studies a different regime: the small-mass **stationary elliptic obstacle problem**. For Morse maxima it obtains an elliptic free-boundary scaling and a nontrivial obstacle profile; in the radial quadratic case that limiting profile is quartic inside its support. The result here concerns the **time-dependent zero-diffusion slow-limit dynamics** of arXiv:2609.20609v1. The Hessian-elliptic support geometry is therefore not claimed as new by itself; the claimed refinement is the explicit temporal scaling and the different parabolic-cap dynamical profile.

Earlier work established the obstacle-type model, well-posedness, stability of steady states, and qualitative interface properties. Those results and the general local Morse expansion are not part of the originality claim.

## Limitations

The theorem is for the \(D=\infty\) slow-limit system (equations (3.7)--(3.10) of arXiv:2609.20609v1), not the finite-cytosolic-diffusion system. It assumes a time-independent signal with finitely many isolated nondegenerate maxima and continuous bounded nonnegative initial data of unit mass. Degenerate maxima can have different exponents, as the source paper itself illustrates for limiting weights, and are not covered here.

The result concerns the limiting slow-time dynamics after the small-mass reduction; it is not a uniform-in-mass estimate for the original parabolic PDE at fixed positive mass. The originality claim is to the best of our knowledge and is source-specific.

## Reproducibility

`artifacts/verify_quadratic_cap.py` checks the constants in the exactly quadratic radial model. In that model the mass identity is \(C\tau q^2=1\), the time relation is \(\tau=t+\sqrt{\tau/C}\), and the exact multiplier is \(\varphi=q/(2-q)\). The script verifies these identities and the convergence of the normalized asymptotic ratios.

## References

1. B. Niethammer, M. Roeger, J. J. L. Velazquez, *Localization properties of a free boundary problem for cell polarization*, arXiv:2609.20609v1 (2026). https://arxiv.org/abs/2609.20609
2. S. Flores Sepulveda, B. Niethammer, J. J. L. Velazquez, *On the shape of the positivity region for a free boundary problem describing cell polarization*, arXiv:2605.03553v1 (2026). https://arxiv.org/abs/2605.03553
3. A. Logioti, B. Niethammer, M. Roeger, J. J. L. Velazquez, *A Parabolic Free Boundary Problem Arising in a Model of Cell Polarization*, SIAM J. Math. Anal. 53 (2021), 1214--1238. https://doi.org/10.1137/20M1349114
4. A. Logioti, B. Niethammer, M. Roeger, J. J. L. Velazquez, *Qualitative properties of solutions to a mass-conserving free boundary problem modeling cell polarization*, Commun. Partial Differential Equations 48 (2023), 1065--1101. https://doi.org/10.1080/03605302.2023.2247467
5. A. Logioti, B. Niethammer, M. Roeger, J. J. L. Velazquez, *Interface behavior for the solutions of a mass conserving free boundary problem modeling cell polarization*, arXiv:2402.03034; published 2025. https://arxiv.org/abs/2402.03034
