# Sharp thermal reentrance of stationary trap-energy skewness in an isotropic run-and-tumble particle

## Finding

An isotropically tumbling particle in a harmonic well has a *negative-to-positive* stationary trap-energy skewness transition as its tumbling rate increases. In arbitrary integer spatial dimension, the zero-thermal-noise transition is unique, and the threshold decreases with dimension after dimension two. In dimension three, arbitrarily weak positive independent thermal noise reverses the low-tumbling sign and creates a bounded window with negative skewness. This reentrant window closes at one sharply defined, positive noise strength.

Set \(a=\gamma/\kappa\) and normalize the squared radius by \(Y=\|\kappa X/v\|^2\). For vanishing translational noise, its stationary third centered moment is

\[
\operatorname{cum}_3(Y)=\frac{8aP_d(a)}{d^2(a+1)^3(a+2)(a+3)(a+4)(a+5)},\qquad
P_d(a)=a^3+(3d+2)a^2+(4d^2-3d+1)a-2d(d+3).
\]

For every integer \(d\ge1\), the only positive root \(a_d\) of \(P_d\) separates negative and positive signs. Specifically, \(a_1=a_2=1\), while \(1/2<a_d<1\) when \(d\ge3\). Extending the root continuously to real \(d\ge2\) shows strict decrease to \(1/2\), with expansion

\[
a_d=\frac12+\frac{27}{16d}-\frac{9}{32d^2}+O(d^{-3}).
\]

In dimension three, independently add translational diffusion \(\sqrt{2D}\,dB_t\) and write \(h=\kappa D/v^2\). The normalized stationary squared radius \(E\) has third centered moment

\[
K(a,h)=\frac{8a(a^3+11a^2+28a-36)}{9(a+1)^3(a+2)(a+3)(a+4)(a+5)}
+\frac{8ha(a+4)}{(a+1)^2(a+2)(a+3)}
+\frac{24h^2}{a+1}+24h^3.
\]

There is one \(h_*>0\) such that for \(0<h<h_*\) exactly two positive tumbling rates produce zero energy skewness, with strictly negative skewness between the zeros and strictly positive skewness outside. At \(h=h_*\) they merge into one positive double zero; above it skewness is positive everywhere. Numerically,

\[
(a_*,h_*)=(0.139827482040041497\ldots,\ 0.019629776323575830\ldots).
\]

## Assumptions and scope

Let \(d\ge1\) be an integer, \(v,\kappa,\gamma>0\), and \(D\ge0\). Consider the stationary solution of

\[
dX_t=(-\kappa X_t+vN_t)\,dt+\sqrt{2D}\,dB_t,
\]

where \(B_t\) is standard \(d\)-dimensional Brownian motion and \(N_t\) is a unit heading, independently resampled uniformly from the unit sphere at all events of an independent rate-\(\gamma\) Poisson process. In dimension one the sphere consists of the two signs. The process exists with a unique stationary distribution for \(\gamma>0\): using a common stationary heading path and Brownian noise, differences between solutions decay as \(e^{-\kappa t}\). Define the dimensionless stationary energy variable \(E=\|\kappa X_t/v\|^2\). Physical harmonic potential energy is a positive multiple of \(E\), so it has the same skewness sign. Statements at \(\gamma=0\) are only limits from strictly positive switching.

## Proof

**Step 1: exact noiseless radial-energy moments.** Rescale time by \(\kappa\), position by \(\kappa/v\), and temporarily put \(D=0\). Let \(Y=\|X\|^2\in[0,1]\) and \(Z=X\cdot N\). Between orientation changes, \(\dot Y=-2Y+2Z\), \(\dot Z=1-Z\). At a refresh, \(Y\) is unchanged, and conditional on \(X\), odd moments of the new \(Z\) vanish, while

\[
\mathbb E[(X\cdot N_{\rm new})^{2j}\mid X]
=Y^j\frac{(2j-1)!!}{d(d+2)\cdots(d+2j-2)}.
\]

The stationary polynomial-generator identity for \(M_{p,q}=\mathbb E[Y^pZ^q]\), \(q>0\), is

\[
(2p+q+a)M_{p,q}=2pM_{p-1,q+1}+qM_{p,q-1}
+a\mathbf1_{2\mid q}\frac{(q-1)!!}{d(d+2)\cdots(d+q-2)}M_{p+q/2,0}.
\]

For \(q=0\), \(M_{p,0}=M_{p-1,1}\) when \(p\ge1\). Set \(M_{0,0}=1\). The recurrence is triangular in \(p+q\) and gives

\[
\begin{aligned}
\mathbb EY&=\frac1{a+1},\\
\mathbb EY^2&=\frac{ad+2a+6d}{d(a+1)(a+2)(a+3)},\\
\mathbb EY^3&=\frac{a^2d^2+6a^2d+8a^2+18ad^2+72ad+120d^2}{d^2(a+1)(a+2)(a+3)(a+4)(a+5)}.
\end{aligned}
\]

Consequently,

\[
\operatorname{Var}(Y)=\frac{2a(a+d+1)}{d(a+1)^2(a+2)(a+3)}
\]

and \(\operatorname{cum}_3(Y)=\mathbb EY^3-3\mathbb EY^2\mathbb EY+2(\mathbb EY)^3\) factors as stated.

**Step 2: unique zero and dimension ordering.** The constant coefficient of \(P_d\) is negative and every nonconstant coefficient is positive for \(d\ge1\). Hence \(P_d\) is strictly increasing on \(a>0\), crosses zero exactly once, and determines the sign. Direct substitution yields

\[
P_d(1)=2(d-1)(d-2),\qquad P_d(1/2)=-9(6d-1)/8.
\]

At \(d=1,2\) the polynomial factors as \((a-1)(a+2)(a+4)\) and \((a-1)(a+4)(a+5)\), respectively. For real \(d>2\), the root lies strictly between \(1/2\) and \(1\). To show strict decrease, fix \(a\in(1/2,1)\) and rewrite

\[
P_d(a)=(4a-2)d^2+(3a^2-3a-6)d+a(a+1)^2.
\]

This is an upward-opening quadratic in \(d\), negative at \(d=2\), and tending to positive infinity, so at its sole zero above two the \(d\)-derivative is strictly positive. Since the \(a\)-derivative is positive, implicit differentiation gives \(da_d/dd<0\). At \(d=2,a=1\) the same derivative is strictly negative. Balancing powers of \(d\) proves the displayed limiting expansion.

**Step 3: exact thermal contribution.** The stationary linear system with Brownian noise decomposes as independent \(X=X^{(0)}+G\), where \(X^{(0)}\) is the noiseless active position and \(G\) is centered Gaussian with covariance \(hI_d\) in dimensionless units. Conditional on \(X^{(0)}\), the squared norm \(E=\|X^{(0)}+G\|^2\) is noncentral chi-square, with conditional mean \(Y+dh\), conditional variance \(2dh^2+4hY\), and conditional third cumulant \(8dh^3+24h^2Y\). The law of total cumulance therefore yields

\[
\operatorname{cum}_3(E)=\operatorname{cum}_3(Y)+12h\operatorname{Var}(Y)
+24h^2\mathbb EY+8dh^3.
\]

Specializing to \(d=3\) gives \(K(a,h)\) above. In particular, \(\partial_hK=12\operatorname{Var}(Y)+48h\mathbb EY+72h^2>0\) for \(a,h>0\).

**Step 4: the unique thermal coalescence.** For \(d=3\), multiply \(K\) by the strictly positive denominator \(9(a+1)^3(a+2)(a+3)(a+4)(a+5)/8\), giving a degree-seven polynomial in \(a\) with all coefficients of degrees \(2,3,4,5,6,7\) positive for every \(h>0\), positive constant term \(3240h^2(h+1)\), and linear coefficient \(13878h^3+10638h^2+720h-36\). Thus by Descartes' rule, there are at most two positive zeros counted with multiplicities. The endpoint limits are \(K(0^+,h)=24h^2(1+h)>0\) and \(K(+\infty,h)=24h^3>0\). At \(h=0\), \(K(a,0)<0\) on the nonempty interval \(0<a<a_3\), and each fixed \(a\) has strictly increasing \(K(a,h)\) for positive \(h\). Therefore a unique positive critical \(h_*\) separates the existence of a negative interval from universal positivity. At criticality the infimum is attained at an interior positive rate, and the polynomial has exactly one double positive root; below criticality it has exactly two simple positive roots, bounding the negative interval. The critical pair is characterized *exactly* as the unique solution with \(a_*,h_*>0\) to

\[
K(a_*,h_*)=0,\qquad\partial_aK(a_*,h_*)=0.
\]

The numerical values above come from solving these equations; the uniqueness is analytical and does not rest on root approximations.

## Verification

The standalone `verify_energy.py` reconstructs all radial moments from the two-variable stationary generator and cross-checks them against an independent coordinate-moment recurrence for 30 rational pairs of dimension and tumbling rate, through the sixth position order. It also checks the beta-distribution limits in dimensions one and two, all exact factorizations, the positive-coefficient pattern used in Descartes' rule, the thermal Gaussian cumulance identity, and the numerical double-zero point. Run `python verify_energy.py` with Python 3 and SymPy installed. This code is a finite computational consistency check; the infinite-parameter claims follow from the algebraic generator and sign arguments above, not the sample grid.

## Relationship to prior work

Frydel (2023), arXiv:2309.12537, derives dimension-dependent stationary moment recurrences for an isotropic run-and-tumble particle in a harmonic trap. Sun, Ye, and Podgornik (2024), arXiv:2409.00578, develop another all-moment framework, primarily for finite tumble durations. Guéneau, Majumdar, and Schehr (2026), arXiv:2602.08436, provide exact position distributions and an arbitrary-moment formula, together with independent Gaussian thermal convolution. These works provide the model, moments, or convolution ingredients. The present classification is the separate, global sign result for the squared-radius third centered moment, including its dimension ordering and the two-zero thermal reentrance/coalescence law. In particular, the raw moment formulas should not be claimed as new. General all-moment formulas might make the new phase boundaries accessible by further algebra; this is a substantial priority/derivability qualification.

## Limitations

The theorem concerns the third *centered* moment of stationary squared radius (potential energy), not radial-position skewness, entropy production, or all higher cumulants. The complete two-zero thermal phase classification is proved for dimension three; for other dimensions, the displayed expression gives an exact thermal cumulant but no analogous two-zero classification is asserted. The statements assume instantaneous uniform direction redrawing and harmonic drift. No result is claimed for finite-duration tumbles, anisotropic traps, finite times, or interacting particles. Physical and publication priority require independent examination; no independent audit has been performed.

## References

1. D. Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537, first posted September 21, 2023. https://arxiv.org/abs/2309.12537
2. A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578, first posted September 1, 2024. https://arxiv.org/abs/2409.00578
3. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436, first posted February 9, 2026. https://arxiv.org/abs/2602.08436
