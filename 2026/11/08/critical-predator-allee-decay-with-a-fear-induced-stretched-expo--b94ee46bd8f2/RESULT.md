# Critical predator-Allee decay with a fear-induced stretched-exponential prey tail

## Finding

In the modified Leslie–Gower predator–prey model of Vinoth et al. (2021), the equality of the predator Allee and alternative-resource constants produces an algebraically decaying predator population. In a nonempty open wedge of strictly positive initial states where predation overwhelms prey birth at low prey-to-predator ratio, the prey population has a **sharp, positive-amplitude stretched-exponential extinction asymptotic**, including an explicit algebraic correction.

**Theorem.** Let \(r,e,b,p,a,k,s,n,c\) be strictly positive constants satisfying \(r>e\) and
\[
\mu:=e+\frac pa-r>0.
\]
Set \(m=c\). There are \(q,\delta>0\) such that every solution with
\[
0<y(0)<\delta,\qquad 0<x(0)<q\,y(0)
\]
is global, stays strictly positive, tends to the origin, and has the simultaneous sharp asymptotics
\[
y(t)=\frac{c}{\sqrt{2s}}t^{-1/2}+\frac{c}{2s}t^{-1}+O(t^{-3/2}),
\]
\[
\lim_{t\to\infty}\frac{x(t)e^{\mu t+rkc\sqrt{2/s}\sqrt{t}}}{t^{\sigma}}=L(x(0),y(0))\in(0,\infty),\qquad
\sigma=\frac{rkc(kc-1)}{2s}.
\]
In particular, changing the fear coefficient \(k\) changes both the universal \(\sqrt t\) exponent and the logarithmic power even though the ordinary exponential prey-decay rate \(\mu\) is independent of \(k\).

A completely rational example is \(r=1\), \(e=1/2\), \(b=p=a=n=s=c=m=1\), \(k=2\). One may take \(q=1/10\), \(\delta=1/4\). For every strictly positive initial state in this wedge,
\[
y(t)=\frac1{\sqrt{2t}}+\frac1{2t}+O(t^{-3/2}),\qquad
x(t)\sim L\,t\,e^{-t/2-2\sqrt{2t}},\qquad 0<L<\infty.
\]

## Assumptions and scope

The state variables \(x(t)\) and \(y(t)\) are respectively prey and predator densities, restricted to the strictly positive quadrant. The unforced continuous-time system is exactly
\[
\dot x=x\left(\frac r{1+ky}-e-bx-\frac{py}{x+ay}\right),\qquad
\dot y=s y^2\left(\frac1{y+m}-\frac1{nx+c}\right).
\]
All parameters are constants and positive. The parameter identity \(m=c\) is essential: the predator-only equilibrium \((0,c-m)\) collides with the origin there. The inequality \(\mu>0\) is an *extra* local low-prey-ratio condition; no claim is made about all initial states or all parameter ranges. The initial wedge is open and nonempty, not a single special orbit. The vector field is smooth on the strictly positive quadrant, even though the ratio-dependent term need not have a differentiable extension to the origin.

## Proof

**1. A forward-invariant extinction wedge.** Put \(z=x/y\). Fix a sufficiently small \(q>0\) with \(nq<1\) and
\[
r-e-\frac p{a+q}\le-\frac{3\mu}{4}.
\]
Such a choice is possible since the left side approaches \(-\mu\) as \(q\downarrow0\). Fix \(\delta>0\) so that \(s\delta^2/c^2<\mu/4\). On \(0<y\le\delta\), \(0<z\le q\),
\[
\frac{\dot x}{x}=\frac r{1+ky}-e-bx-\frac p{a+z}\le-\frac{3\mu}{4},
\]
while, using \(m=c\),
\[
\frac{\dot y}{y}=\frac{s y(nx-y)}{(y+c)(nx+c)}\in[-s\delta^2/c^2,0).
\]
Consequently \(\dot z/z\le-\mu/2\), so a trajectory that starts in the open wedge never reaches its lateral boundary. Both variables are bounded and remain positive for finite time; hence the solution exists for all \(t\ge0\). Moreover, \(x(t)\le x(0)e^{-3\mu t/4}\) and \(y\) decreases. With \(x\le qy\) and \(nq<1\), the equation for \(y\) yields constants \(C_1,C_2>0\) for which
\[
-C_2y^3\le\dot y\le-C_1y^3.
\]
Thus \(y(t)=\Theta(t^{-1/2})\), in particular \(y\to0\), and \(\int_0^\infty(x+x/y)\,dt<\infty\). The latter follows from exponential decay of \(x\) and the lower algebraic bound on \(y\).

**2. Exact predator antiderivative.** Define
\[
H(y)=\frac{c}{sy}+\frac{c^2}{2sy^2}.
\]
Direct differentiation along the *full coupled system* gives the exact identity
\[
\frac{d}{dt}H(y(t))=1-\frac{nx(t)(y(t)+c)}{y(t)(nx(t)+c)}.
\]
The last term is nonnegative and absolutely integrable because \(x/y\in L^1([0,\infty))\). Hence \(H(y(t))=t+H_\infty+o(1)\) for a finite real constant \(H_\infty\). Completing the square gives
\[
\frac1{y(t)}+\frac1c
=\sqrt{\frac{2s}{c^2}(t+H_\infty+o(1))+\frac1{c^2}}
=\frac{\sqrt{2s}}c\sqrt t+O(t^{-1/2}).
\]
Expanding its reciprocal proves the two-term asymptotic for \(y\), including the \(O(t^{-3/2})\) error.

**3. Sharp prey extinction and the power correction.** Using \(z=x/y\), the prey equation gives an exact decomposition
\[
\frac{d}{dt}\log x=-\mu-rky+rk^2y^2+R(t),
\]
where
\[
R(t)=-bx+\frac{pz}{a(a+z)}-\frac{rk^3y^3}{1+ky}.
\]
Since \(x,z,y^3\) are integrable, so is \(R\). The predator expansion from Step 2 yields, with finite real constants \(B_1,B_2\),
\[
\int_0^t y(u)\,du=c\sqrt{\frac2s}\sqrt t+\frac{c}{2s}\log t+B_1+o(1),
\]
\[
\int_0^t y(u)^2\,du=\frac{c^2}{2s}\log t+B_2+o(1).
\]
Integration of the logarithmic prey identity now gives
\[
\log x(t)=-\mu t-rkc\sqrt{\frac2s}\sqrt t
+\frac{rkc(kc-1)}{2s}\log t+B_3+o(1)
\]
for finite \(B_3\). Exponentiating gives the asserted limit \(L=e^{B_3}\in(0,\infty)\).

**4. Explicit wedge.** In the rational example, take \(q=1/10\), \(\delta=1/4\). Then \(nq=1/10<1\), \(r-e-p/(a+q)=-9/22<-3/8\), and \(s\delta^2/c^2=1/16<1/8\). All strict wedge hypotheses hold, and substitution yields \(\mu=1/2\), \(rkc\sqrt{2/s}=2\sqrt2\), and \(\sigma=1\).

## Verification

The standalone `verify.py` checks the exact antiderivative identity, the exact logarithmic-prey remainder, the example's rational strict inequalities, and the formal cancellation in the two-term predator asymptotic. It also runs a numerical ODE diagnostic to illustrate convergence toward the proved asymptotic rates. Execute `python verify.py` with Python 3, SymPy, NumPy and SciPy installed. A diagnostic or finite-time plot is *not* used to prove an asymptotic limit; all infinite-time statements follow from the preceding inequalities and integrable remainder identities.

## Relationship to prior work

Vinoth et al. introduce this exact fear/Allee/ratio-dependent system, classify its equilibria and local bifurcations, and explicitly identify the collision of the predator-only equilibrium with the origin at \(m=c\) (Sections 2, 4, 5). Their paper does not provide the two-term algebraic predator tail, the full coupled integrability identity, or the positive-amplitude stretched-exponential prey tail with explicit logarithmic exponent. Mishra and Tiwari (2021) study a different fear/group-defense modified Leslie–Gower reaction–diffusion system with logistic predator growth and pattern instabilities; its equations do not imply this critical predator Allee normal form. Related critical slowing laws for other Leslie–Gower and Allee models do not cover the exact two-population fear-dependent correction for the model and assumptions above. The novel assertion is the **combined sharp asymptotic**, not the generic observation that cubic scalar decay can scale as \(t^{-1/2}\).

## Limitations

This is a local wedge theorem at the codimension-one equality \(m=c\) and under the additional strict predation dominance \(p/a>r-e\). It neither characterizes the entire basin, nor claims global coexistence/extinction, nor applies automatically to delayed, stochastic, or spatial variants. The positive amplitude \(L\) depends on the starting point and is not given as a closed elementary constant. Publication-priority uniqueness is not independently certified; unindexed prior equivalent analyses remain a possibility.

## References

1. S. Vinoth, R. Sivasamy, K. Sathiyanathan, B. Unyong, G. Rajchakit, R. Vadivel, N. Gunasekaran, *The dynamics of a Leslie type predator–prey model with fear and Allee effect*, Advances in Difference Equations **2021**, article 338, published July 16, 2021, https://doi.org/10.1186/s13662-021-03490-x.
2. P. Mishra and B. Tiwari, *Drivers of pattern formation in a predator–prey model with defense in fearful prey*, Nonlinear Dynamics **105** (2021), 2811–2838, published July 31, 2021, https://doi.org/10.1007/s11071-021-06719-2.
3. W. Kong and Y. Shao, *Bifurcations of a Leslie-Gower predator-prey model with fear, strong Allee effect and hunting cooperation*, AIMS Mathematics **9** (2024), 31607–31635, https://doi.org/10.3934/math.20241520. (Different model; metadata and abstract checked, full text not established.)
