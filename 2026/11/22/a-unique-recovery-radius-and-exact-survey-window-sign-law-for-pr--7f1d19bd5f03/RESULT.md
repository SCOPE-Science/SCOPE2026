# A unique recovery radius and exact survey-window sign law for predator-satiated seed survival

## Finding
Consider local seed arrival and predator density that decline exponentially with distance from an isolated parent, with seed disappearance governed by background mortality and a Holling-II functional response. The resulting equilibrium fraction of seeds escaping predation is either strictly increasing or has exactly one strict minimum, never a maximum. More precisely, write the seed-arrival exponent as \(d>0\), the predator-density exponent as \(n>0\), and the source seed equilibrium as \(S_0>0\). With attack coefficient \(a>0\), handling time \(h>0\), and \(y_0=ahS_0\), a minimum away from the parent exists **if and only if**
\[
0<n<d,\qquad y_0>\frac{n}{d-n}.
\]
In that regime there is also a **unique positive survey radius** \(R_c\) at which the survival fraction at radius \(R_c\) first returns to its source value. The exact, strictly increasing survey-cutoff function is
\[
Y(R)=\frac{1-e^{-nR}}{e^{-nR}-e^{-dR}}
     =\frac{e^{nR}-1}{1-e^{-(d-n)R}},\quad R>0,
\]
with \(R_c\) characterized by \(Y(R_c)=y_0\). The survival fraction at the survey endpoint is lower than at the parent precisely when \(0<R<R_c\), and higher precisely when \(R>R_c\). Thus **the direction of the source-to-endpoint survival comparison reverses once as survey extent grows**, despite the same fixed biological parameters. If the minimum criterion fails, survival instead increases with distance and there is no positive equal-endpoint radius. The statement concerns the exact defined model; it does not redefine the empirical recruitment classes used in prior studies.

## Assumptions and scope
Fix \(F_0,N_0,\mu,a,h,d,n>0\) and spatial distance \(r\ge0\). Define seed-arrival intensity \(F(r)=F_0e^{-dr}\) and predator density \(N(r)=N_0e^{-nr}\). The background seed mortality is \(\mu\); predator intake per individual follows \(aS/(1+ahS)\). For each \(r\), define the positive local steady-state seed density \(S(r)\) by
\[
 F(r)=\mu S(r)+\frac{aN(r)S(r)}{1+ahS(r)}.
\]
The seed-escape fraction is \(P(r)=\mu S(r)/F(r)\). All parameters are spatially constant except the specified exponential inputs. The model is local and equilibrium-based; predators do not respond dynamically to local seed densities and there are no edge boundaries, additional mortality mechanisms or subsequent seedling dynamics. For an isotropic planar exponential seed shadow, \(d^{-1}\) is the decay length and the seed-mass distribution in annuli is proportional to \(r e^{-dr}\).

The right-hand side of the equilibrium equation is strictly increasing from zero to infinity as a function of \(S\), since its derivative is \(\mu+aN/(1+ahS)^2>0\). Therefore there is one positive smooth equilibrium \(S(r)\) for each \(r\), and \(0<P(r)<1\) for finite \(r\).

## Proof
Let \(Q(r)=aN(r)/(1+ahS(r))>0\) and \(J(r)=\mu+aN(r)/(1+ahS(r))^2>0\). Differentiating the steady-state equation and using \(F'=-dF\), \(N'=-nN\) yields
\[
\frac{S'}{S}=\frac{-d\mu+(n-d)Q}{J}.
\]
Because \(P=\mu S/F\), this gives the exact sign identity
\[
\frac{P'}{P}=\frac{Q\,[n-(d-n)ahS]}{(1+ahS)J}.
\tag{1}
\]
All factors outside the square bracket are strictly positive. If \(n\ge d\), the bracket is strictly positive, so \(P\) increases for every finite distance. If \(0<n<d\), the first displayed derivative shows that \(S'<0\) everywhere. Furthermore \(0<S(r)\le F(r)/\mu\to0\), so \(ahS(r)\) decreases continuously and strictly from \(y_0=ahS_0\) to zero. Equation (1) then has at most one positive zero, necessarily a change from negative to positive, occurring exactly when
\[
ahS(r_*)=\frac{n}{d-n}.
\tag{2}
\]
Such a zero exists precisely under the stated strict inequality \(y_0>n/(d-n)\). Equality gives \(P'(0)=0\) and \(P'(r)>0\) for every \(r>0\); otherwise \(P\) increases strictly. Finally, from the steady-state equation
\[
 P(r)=\frac{\mu}{\mu+aN(r)/(1+ahS(r))}\longrightarrow1
\quad(r\to\infty),
\]
as \(n>0\) implies \(N(r)\to0\).

For the **endpoint law**, fix \(R>0\), let \(x=e^{-dR}\), \(z=e^{-nR}\), and \(S_0=S(0)\). By monotonicity of the steady-state right-hand side as a function of \(S\), the sign of \(S(R)-xS_0\), equivalently that of \(P(R)-P(0)\), is the sign of the arrival intensity at \(R\) minus the seed-loss expression evaluated at \(xS_0\). Cancelling strictly positive factors gives
\[
\operatorname{sgn}\bigl(P(R)-P(0)\bigr)
=\operatorname{sgn}\bigl[(1-z)+(x-z)y_0\bigr].
\tag{3}
\]
If \(n\ge d\) then \(x\ge z\), hence the bracket is positive. For \(0<n<d\), \(x<z\) and (3) is negative, zero or positive as \(y_0\) is respectively greater than, equal to or less than
\[
Y(R)=\frac{1-z}{z-x}.
\tag{4}
\]
To prove the cutoff is unique, observe
\[
\frac{d}{dR}\log Y(R)
=\frac{n}{1-e^{-nR}}-\frac{d-n}{e^{(d-n)R}-1}>0.
\]
The first summand exceeds \(1/R\) and the second is below \(1/R\), by \(1-e^{-u}<u<e^u-1\) for \(u>0\). Also \(Y(R)\to n/(d-n)\) as \(R\downarrow0\), whereas \(Y(R)\to\infty\) as \(R\to\infty\). Consequently \(Y(R)=y_0\) has one positive solution exactly in the one-minimum regime, with the sign order claimed. The unique radius \(R_c\) lies strictly beyond the minimum radius \(r_*\), since \(P\) decreases before \(r_*\) and first returns to its initial value after its strict minimum. This completes the classification, including boundary cases.

An equivalent directly measurable source-intensity threshold at a selected radius \(R\) follows by substituting \(S_0=Y(R)/(ah)\) into the source balance:
\[
F_0^{\dagger}(R)=\frac{Y(R)}{ah}
\left(\mu+\frac{aN_0}{1+Y(R)}\right).
\tag{5}
\]
For \(0<n<d\), \(P(R)<P(0)\) if and only if \(F_0>F_0^{\dagger}(R)\); equality and the opposite inequality give equality and \(P(R)>P(0)\). This follows because the source-balance right side is strictly increasing in \(S_0\). Equations (4)–(5) are exact, with no small-predation or long-distance approximation.

## Verification
For an exact illustrative parameter choice, take \(\mu=a=h=d=1\), \(n=1/2\), \(F_0=8\), and \(N_0=5\). The source steady state is \(S_0=4\), so \(P(0)=1/2\), \(y_0=4\), and the unique minimum satisfies \(S(r_*)=1\). Writing \(z_*=e^{-r_*/2}\), its balance equation becomes \(16z_*^2-5z_*-2=0\), hence
\[
z_*=\frac{5+\sqrt{153}}{32},\quad
r_*=-2\log z_*\approx1.2220613022,
\quad P(r_*)\approx0.4242721190.
\]
Since \(d=2n\), equation (4) reduces identically to \(Y(R)=e^{nR}\), giving the exact return distance
\[
R_c=2\log4\approx2.7725887222.
\]
The source-to-endpoint difference reverses there: \(P(2)\approx0.4464195167<P(0)\), while \(P(4.7438645184)\approx0.6920159049>P(0)\). The latter radius contains 95% of a planar radial-exponential seed shadow because \((1+R)e^{-R}=0.05\). It follows that a source-to-radius classification can change solely through the endpoint chosen, even though the unique interior trough is fixed.

The standalone `CHECK.py` uses only the Python standard library. Run `python3 CHECK.py`. It checks an exact rational source/return equality and 3,614 supplementary assertions for equilibrium identities, derivative-sign diagnostics, endpoint comparisons and illustrative parameters. These finite diagnostics do not prove the quantified theorem; the analytical identities and monotonicity arguments above do.

## Relationship to prior work
Nathan and Casagrandi (2004) introduced the exponential seed-shadow/predator model with Holling-II predation and derived a near-source criterion for a **unimodal establishment-density** pattern (their equation 8 and Appendix 1). They describe McCanny-type declining survivorship using finite survey windows and classify based on a source-to-95th-percentile comparison with a tolerance. The new result concerns the distinct **seed-escape fraction**, proves its global one-trough/no-trough classification, and gives an exact formula for the unique radius at which its endpoint comparison reverses, rather than an approximate window-based grouping. It does not claim to replace their model, their recruitment classes, or their established criterion.

Beckman, Neuhauser and Muller-Landau (2012) use finite-radius simulation classifications with clumped dispersal and insect/pathogen dynamics; their numerical results neither establish nor imply a closed-form survey-radius crossing theorem for the fixed exponential/Holling-II equilibrium stated here. Mari et al. (2008) and Mari, Gatto and Casagrandi (2009) consider explicitly mobile predator populations and central-place foraging, respectively, through coupled partial differential equations. Lawfully available full-text transcriptions of both studies were examined, including the models, main results and discussions; neither identifies the fixed-field source-to-endpoint cutoff theorem stated here. A focused literature and database comparison did not reveal this stated exact cutoff theorem; this search result is not a proof of novelty.

## Limitations
The result is exact only for the specified independent exponential spatial profiles, positive type-II saturation, constant nonpredation mortality and local steady-state closure. It does not predict where seedling establishment or mature recruits will be observed, since it omits germination, competition, pathogen mortality, subsequent predation and disperser behavior. It does not assert that a statistically significant or experimentally observable source-to-endpoint difference follows from a mathematical sign. Seed-mass quantiles depend on spatial geometry; the illustrative 95% radius assumes a planar isotropic shadow. The one-radius law may fail for other dispersal kernels, nonexponential predator fields, coupled predator movement, or extra mortality mechanisms. Publication priority is not independently certified, and related historical mathematical analyses beyond the sources inspected may contain equivalent results.

## References
- Nathan, R. & Casagrandi, R. (2004). *A simple mechanistic model of seed dispersal, predation and plant establishment: Janzen-Connell and beyond*. Journal of Ecology 92, 733–746. First published 2004-09-16. https://doi.org/10.1111/j.0022-0477.2004.00914.x
- Beckman, N. G., Neuhauser, C. & Muller-Landau, H. C. (2012). *The interacting effects of clumped seed dispersal and distance- and density-dependent mortality on seedling recruitment patterns*. Journal of Ecology 100, 862–873. First published 2012-04-30. https://doi.org/10.1111/j.1365-2745.2012.01978.x
- Mari, L., Casagrandi, R., Gatto, M., Avgar, T. & Nathan, R. (2008). *Movement strategies of seed predators as determinants of plant recruitment patterns*. American Naturalist 172, 694–711. https://doi.org/10.1086/591687
- Mari, L., Gatto, M. & Casagrandi, R. (2009). *Central-place seed foraging and vegetation patterns*. Theoretical Population Biology 76, 229–240. https://doi.org/10.1016/j.tpb.2009.08.001
