# Three soil regions are minimal for two uptake peaks under nocturnal hydraulic redistribution

## Finding

In an equal-volume, lossless, root-connected nighttime exchange model with a single common positive exchange rate, **one or two regions cannot produce two distinct strict local maxima of next-morning saturating uptake potential as a function of exchange rate, but three regions can**. The three-region witness is an ordinary connected path with strictly positive uptake capacities and half-saturation parameters. Its response has **exactly two distinct strict local maxima at finite positive rates**, separated by a strict local minimum. This is a statement about the *number of stationary response peaks*, not about field-measured transpiration or total water use.

## Assumptions and scope

Each soil region has equal water-storage volume and moisture (dimensionless available water) \(x_i(t)\ge 0\). During a fixed night of duration \(T>0\), the only change is symmetric, nearest-neighbor exchange at rate \(\kappa\ge0\), without sources, sinks, uptake, or storage limitation beyond nonnegativity. In two regions, the exchange network is a single edge; in three, it is the path \(1-2-3\). Fix initial conditions independently of the exchange rate. Next-morning uptake **potential**, evaluated instantaneously rather than integrated over a day, is
\[
U(\kappa)=\sum_i \frac{a_i x_i(T;\kappa)}{K_i+x_i(T;\kappa)},\qquad a_i>0,\quad K_i>0.
\]
Each term is strictly increasing and strictly concave in local water amount; the parameters can differ between regions. The sole control is the common exchange rate \(\kappa\). No inference about general networks, other uptake functions, or actual transpiration is asserted.

For the explicit three-region witness take \(x(0)=(1,0,0)\), capacities \((a_1,a_2,a_3)=(23,1,7)\), and half-saturation values \((K_1,K_2,K_3)=(1,1/20,1/5)\). Then \(U\) has exactly two strict local maxima in \(0<\kappa<\infty\), at \(\kappa T\approx0.0661994572\) and \(\kappa T\approx0.7494616363\), with a strict intervening local minimum at \(\kappa T\approx0.1881674312\). The corresponding uptake-potential values are approximately \(11.7469950969\), \(11.9159636476\), and \(11.7118371427\), respectively. These values illustrate an exact rational-sign/root-count proof; decimals alone do not certify the theorem.

## Proof

**Two-region impossibility.** For arbitrary nonnegative initial states \(v_1,v_2\), write \(m=(v_1+v_2)/2\), \(\delta=(v_1-v_2)/2\), and \(z=e^{-2\kappa T}\in(0,1)\). The unique two-region solution is \(x_1=m+\delta z\), \(x_2=m-\delta z\). For \(H(z)=\sum_{i=1}^2 a_i x_i/(K_i+x_i)\), differentiation gives
\[
H''(z)=-2\delta^2\left(\frac{a_1K_1}{(K_1+m+\delta z)^3}+\frac{a_2K_2}{(K_2+m-\delta z)^3}\right).
\]
Every denominator is positive for \(z\in(0,1)\), because both states are nonnegative. If \(\delta\ne0\), \(H\) is strictly concave and hence has at most one interior local maximum; if \(\delta=0\), \(H\) is constant and has no strict maximum. Because \(z\) maps \(0<\kappa<\infty\) bijectively and monotonically to \(0<z<1\), the same at-most-one conclusion holds in \(\kappa\). A one-region model has no exchange-rate dependence.

**Three-region example.** In the path network, the initial condition and rate equation are
\[
\frac{d}{dt}\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}
=\kappa\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix}
\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix},\qquad x(0)=(1,0,0).
\]
Set \(q=e^{-\kappa T}\in(0,1)\). The eigenvalues of the negative path Laplacian are \(0,-1,-3\), and direct substitution into the differential equation with \(q(0)=1\) gives the **exact** water fractions
\[
x_1(q)=\frac13+\frac q2+\frac{q^3}{6},\qquad
x_2(q)=\frac{1-q^3}{3},\qquad
x_3(q)=\frac13-\frac q2+\frac{q^3}{6}.
\]
All three are nonnegative for \(0\le q\le1\), sum to one, and tend to \(1/3\) as \(q\downarrow0\). With the stated positive rational uptake parameters, exact symbolic differentiation and cancellation yield
\[
\frac{dU}{dq}=\frac{108P(q)}{(20q^3-23)^2(q^3+3q+8)^2(5q^3-15q+16)^2},
\]
where
\[
\begin{aligned}
P(q)={}&40625q^{14}-180000q^{12}+188200q^{11}+122750q^{10}-800q^9\\
 &+262155q^8-1120200q^7+972015q^6-1652360q^5\\
 &+2122305q^4-1078800q^3+1117802q^2-1121480q+321632.
\end{aligned}
\]
The denominator is strictly positive on \([0,1]\): \(20q^3-23\le-3\), \(q^3+3q+8\ge8\), and \(5q^3-15q+16\ge6\). Applying the Euclidean Sturm sequence to this *integer polynomial* gives sign-variation counts \(V(0)=9\), \(V(1)=6\); the exact polynomial gcd satisfies \(\gcd(P,P')=1\). Consequently \(P\) has precisely \(9-6=3\) distinct simple roots in \((0,1)\), counted without numerical root estimates. The exact rational signs at \(q=1/10,7/10,9/10,19/20\) are respectively \(+,-,+,-\), and these four abscissae are increasing. These sign observations combined with the exact three-root count force the sign pattern \(+,-,+,-\) between consecutive roots, and therefore two strict maxima (first and third roots in increasing \(q\)) separated by one strict minimum. A smooth monotone reparametrization from \(q\) to \(\kappa\) preserves maxima and minima. No other stationary point is possible. This completes the proof of minimality and the explicit three-region witness.

## Verification

The standalone `checker.py` independently reconstructs the three-region linear-system solution, the uptake formula, the exact derivative identity, the rational sign comparisons, the polynomial gcd and Sturm variations, and the analytic two-region second derivative. It additionally integrates the original three-region ODE with a fourth-order Runge–Kutta method at seven selected exchange rates and compares the numerical states to the closed form; those finite computations are supplementary diagnostics only. Run with `python checker.py` after installing the standalone requirement specified in `requirements.txt`. The reference execution completed **48 assertions**, with Sturm variations \((9,6)\) and three counted roots. The exact Sturm calculation and symbolic identities, not finite experiments or the numerical optimizer, are the proof certificates.

For reference, the increasing \(q\) roots are approximately \(0.472620926216786\), \(0.828475982879140\), and \(0.935944164875624\). Since \(\kappa T=-\log q\), the associated rates in **increasing** order are about \(0.066199457195\), \(0.188167431215\), and \(0.749461636291\). The exact statements hold for every \(T>0\).

## Relationship to prior work

Root-mediated nocturnal redistribution across moisture gradients and its impact on uptake and transpiration are established phenomena. Amenu and Kumar introduced a coupled soil-root hydrologic model, publicly discussed in October 2007; Guswa investigated root compensation and redistribution under spatial moisture variation; Wang and colleagues and Quijano and Kumar studied conductance sensitivity using more realistic ecohydrologic simulations. The present result **does not claim** to introduce root redistribution, concave uptake laws, diffusion on paths, or numerical conductance sensitivity. It isolates a specific idealized mathematical question: how many strict stationary maxima in **next-morning instantaneous uptake potential** can arise while varying a single positive symmetric exchange rate, with all positive saturating-response parameters. The two-versus-three impossibility/witness pair and the exact Sturm certificate were not found in the inspected references or matching indexed claims. This is a best-knowledge comparison, not an exhaustive historical-priority guarantee.

## Limitations

All sites have equal volumes and the same intersite conductance. Water potentials, changing soil conductivity, capillary effects, nocturnal uptake, diurnal dynamics, plant regulation, and weather are omitted. Uptake potential is evaluated once at dawn, not integrated through a growing season. The rational parameter values are a mathematical example, not calibrated to a plant or soil. Only *existence of two strict finite-rate local maxima* is established, not that both are global, robust to all parameter changes, or measurable in field data. It does not follow that increasing root conductance will reduce observed transpiration under realistic field conditions. Broader work on semigroup response curves might imply equivalent results in a different language; historical priority requires independent checking.

## References

1. G. G. Amenu and P. Kumar, *A model for hydraulic redistribution incorporating coupled soil-root moisture transport*, Hydrology and Earth System Sciences 12 (2008), 55–74. DOI: 10.5194/hess-12-55-2008. Preprint discussion first public on 2007-10-04: https://hess.copernicus.org/articles/12/55/2008/hess-12-55-2008-discussion.html .
2. A. J. Guswa, *Canopy vs. Roots: Production and Destruction of Variability in Soil Moisture and Hydrologic Fluxes*, Vadose Zone Journal 11 (2012). DOI: 10.2136/vzj2011.0159.
3. J. C. Quijano and P. Kumar, *Numerical simulations of hydraulic redistribution across climates: The role of the root hydraulic conductivities*, Water Resources Research 51 (2015), 8529–8550. DOI: 10.1002/2014WR016509.
4. G. Wang et al., *Assessing the potential hydrological impacts of hydraulic redistribution in Amazonia using a numerical modeling approach*, Water Resources Research 47 (2011). DOI: 10.1029/2010WR009601.
5. Q. de Jong van Lier et al., *Macroscopic Root Water Uptake Distribution Using a Matric Flux Potential Approach*, Vadose Zone Journal 7 (2008). DOI: 10.2136/vzj2007.0083.
