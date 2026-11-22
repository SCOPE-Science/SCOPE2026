# Universal duration boundary for cumulative population under two switched logistic carrying capacities

## Finding

Consider a single unharvested population governed by the logistic law with a fixed intrinsic growth rate but two environmental carrying capacities. The total **population-time** over two equal-duration stages can prefer the *opposite environmental order* from the one giving the larger terminal population. This distinction has a sharp universal duration boundary, independent of either capacity.

**Theorem.** Fix \(r>0\), \(\tau>0\), \(N_0>0\) and \(K_H>K_L>0\). Let \(N_{HL}\) evolve at capacity \(K_H\) for \(0\le t<\tau\) and capacity \(K_L\) for \(\tau\le t\le2\tau\), and let \(N_{LH}\) use the reverse order. Set

\[
\mathcal B_{HL}=\int_0^{2\tau}N_{HL}(t)\,dt,\qquad
\mathcal B_{LH}=\int_0^{2\tau}N_{LH}(t)\,dt,
\qquad h=r\tau.
\]

Then, for **every** admissible choice of parameters, \(N_{LH}(2\tau)>N_{HL}(2\tau)\). Nevertheless:

1. If \(0<h\le h_c=\log(1+\sqrt 2)\), then \(\mathcal B_{HL}>\mathcal B_{LH}\) for all \(N_0>0\).
2. If \(h>h_c\), there exists exactly one \(N_*(h,K_H,K_L)>0\) with equal cumulative biomasses. For \(0<N_0<N_*\), \(\mathcal B_{LH}>\mathcal B_{HL}\); for \(N_0>N_*\), \(\mathcal B_{HL}>\mathcal B_{LH}\). There are no other ties.
3. The *instantaneous* ordering reverses exactly once, at \(t_*=\tau+r^{-1}\log(2-e^{-h})\), strictly between the midpoint and endpoint. For \(0<t<t_*\) the high–low population is strictly larger, while for \(t_*<t\le2\tau\) the low–high population is strictly larger. This crossing time depends only on the common growth rate and the stage duration.

For \(r=1\), \(\tau=\log3\), \(K_H=2\), \(K_L=1\), the crossover occurs at the **exact** initial population \(N_*=1/7\), with \(\mathcal B_{HL}=\mathcal B_{LH}=\log(16/7)\).

## Assumptions and scope

The state \(N(t)\) is a strictly positive real population density, continuous at the single change of environment, solving

\[
\dot N(t)=rN(t)\bigl(1-N(t)/K(t)\bigr).
\]

The same \(r\), positive initial density, and two positive capacity levels apply in both schedules. Each level lasts exactly \(\tau\), so the comparison fixes the set of environmental exposures and their lengths, changing only order. No pulses, harvesting, noise, migration or discounting are present. Biomass-time is the unweighted integral of abundance, not an asymptotic growth rate or terminal stock. No restriction that \(N_0\) be below either carrying capacity is necessary.

Write dimensionless time \(z=rt\), inverse initial abundance \(y=1/N_0\), \(E=e^h\), \(u=e^{-h}\), and inverse capacities \(a=1/K_H<b=1/K_L\). These quantities are well-defined throughout the theorem's domain.

## Proof

**1. Explicit inverse dynamics and the crossing.** Put \(Y(z)=1/N(z/r)\). In either constant environment, \(Y'=-Y+v\), with \(v=a\) or \(v=b\), hence

\[
Y(z_0+s)=e^{-s}Y(z_0)+(1-e^{-s})v.
\]

The two histories have the same initial \(Y(0)=y\). Subtraction yields

\[
Y_{LH}(z)-Y_{HL}(z)=(b-a)D_h(z),
\qquad
D_h(z)=\begin{cases}
1-e^{-z},&0\le z\le h,\\
(2-u)e^{-(z-h)}-1,&h\le z\le2h.
\end{cases}
\]

Since \(2-u<E\) whenever \(E>1\), the unique zero after the origin is \(z_*=h+\log(2-u)\), with \(h<z_*<2h\). Taking reciprocals preserves the sign of the displayed difference in the direction \(N_{HL}-N_{LH}\). At the final time, \(D_h(2h)=-(1-u)^2\), proving strict terminal superiority of low-then-high for every initial population.

**2. A strictly monotone ratio of late to early contributions.** Define positive, strictly increasing functions

\[
H_j(z)=\int_0^z e^s v_j(s)\,ds,
\qquad Y_j(z)=e^{-z}(y+H_j(z)),
\]

where \(j\in\{HL,LH\}\) and \(v_j\) is its piecewise constant inverse capacity. Thus the cumulative difference, multiplied by \(r\), is

\[
r(\mathcal B_{HL}-\mathcal B_{LH})=(b-a)
\int_0^{2h}D_h(z)W_y(z)\,dz,
\qquad
W_y(z)=\frac{e^{2z}}{(y+H_{HL}(z))(y+H_{LH}(z))}.
\]

Let \(P(y)=\int_0^{z_*}D_h(z)W_y(z)\,dz>0\) and \(Q(y)=-\int_{z_*}^{2h}D_h(z)W_y(z)\,dz>0\). Their ratio \(R(y)=Q(y)/P(y)\) is strictly increasing in \(y>0\): for \(y_2>y_1\), the weight ratio \(W_{y_2}(z)/W_{y_1}(z)\) is strictly increasing with \(z\), because

\[
\frac{d}{dz}\log\frac{W_{y_2}(z)}{W_{y_1}(z)}
=\sum_{j\in\{HL,LH\}}
\frac{(y_2-y_1)H'_j(z)}{(y_1+H_j(z))(y_2+H_j(z))}>0
\]

away from the single switching point (and by continuity at it). Every point of \(Q\)'s integration interval is later than every point of \(P\)'s, so the strict increase of the relative weight implies \(Q(y_2)/Q(y_1)>P(y_2)/P(y_1)\). In particular \(R\) is continuous and strictly increasing.

**3. Both endpoint limits and exact sharp duration.** As \(y\downarrow0\), \(H_{HL}(z)\sim az\), \(H_{LH}(z)\sim bz\), and \(D_h(z)\sim z\) near the origin. Consequently \(P(y)\to\infty\) logarithmically while \(Q(y)\) approaches a finite positive limit; therefore \(R(y)\to0\).

As \(y\to\infty\), dominated convergence after multiplying by \(y^2\) gives \(y^2W_y(z)\to e^{2z}\). The difference between limiting early and late contributions is exactly

\[
A(h)=\int_0^{2h}e^{2z}D_h(z)\,dz
=-\frac{(E-1)^2(E^2-2E-1)}2.
\]

Its sign is positive for \(1<E<1+\sqrt2\), zero at \(E=1+\sqrt2\), and negative thereafter. Hence \(R(+\infty)\le1\) precisely when \(h\le\log(1+\sqrt2)\), and \(R(+\infty)>1\) when \(h\) exceeds that threshold. Because \(R\) is **strictly increasing**, the first regime has \(R(y)<1\) for every finite positive \(y\); the second has exactly one crossing of \(1\) by continuity. Translating back by \(N_0=1/y\) gives the unique population threshold and all asserted strict inequalities.

**4. Exact computation without numerical integration.** In a constant-capacity stage, starting at inverse population \(y>0\), define

\[
L_K(y)=K\log\left(1+\frac{E-1}{Ky}\right),
\qquad M_K(y)=u y+\frac{1-u}{K}.
\]

Integration of the explicit solution gives the exact formula

\[
r\mathcal B_{HL}=L_{K_H}(y)+L_{K_L}(M_{K_H}(y)),\qquad
r\mathcal B_{LH}=L_{K_L}(y)+L_{K_H}(M_{K_L}(y)).
\]

At the example \(E=3\), \(K_H=2\), \(K_L=1\), \(y=7\), the first formula reduces to \(2\log(8/7)+\log(7/4)\), and the second to \(\log(9/7)+2\log(4/3)\); both equal \(\log(16/7)\). The monotonic-ratio proof gives global uniqueness, rather than just a root of this equality.

## Verification

The independent implementation in `verify.py` reproduces the exact rational tie using fractions, checks the limiting polynomial identity with rational arithmetic, tests the inverse-trajectory comparison over a parameter grid, compares exact stage integrations with numerical quadrature, confirms the final-state ranking, and checks numerical monotonicity of the late/early contribution ratio. It performs 144,156 deterministic assertions with standard Python 3. It is not an exhaustive enumeration of continuous parameters; steps 1–3 establish the infinite-domain result analytically.

For the exact crossover example, the code obtains: \(h_c=0.881373587019543\); at \(N_0=0.1\), \(\mathcal B_{HL}\approx0.6259384309<0.6286086594\approx\mathcal B_{LH}\); at \(N_0=0.5\), \(\mathcal B_{HL}\approx1.9095425049>1.8123787564\approx\mathcal B_{LH}\).

Reproduce with `python3 verify.py`; no nonstandard dependencies are required.

## Relationship to prior work

Shepherd and Stojkov (2007) analyze the classic logistic population equation with time-varying carrying capacity using multiple scales for *slow* variation; their model motivates the present study but their investigated parameter regime and conclusions do not supply a theorem for two abrupt equal-duration capacities or the cumulative-ordering boundary. Hasanbulli, S. P. Rogovchenko and Y. V. Rogovchenko (2013) analyze positive periodic solutions and periodic yield harvesting under fluctuating conditions, not a finite unharvested two-stage population-time comparison. Castilho and Srinivasu (2006 online; 2007 volume) study infinite-horizon harvesting-revenue optimization; only their abstract was accessible, so broader conclusions from their full text were not excluded.

The continuous-time one-dimensional problem differs from published comparisons involving seasonal discrete Ricker and Beverton–Holt maps, multistage projection matrices, or nonlinear predator-control schedules. More general temporal rearrangement or integral-functional ordering results could imply a special case without using the same terminology, so historical priority is provisional pending broader literature review.

## Limitations

The theorem concerns an exactly equal-duration, two-capacity, unharvested single-species logistic differential equation with constant intrinsic growth and no measurement noise. Different stage durations, variable intrinsic growth, density-dependent harvesting, transient switching costs, and stochastic demography are unproved. The upper/lower *schedule* is compared only for a fixed two-stage multiset; no arbitrary multi-stage global scheduling result is claimed. Integrated abundance is a specific ecological proxy, not economic profit, ecosystem productivity, or a validated field-management prescription. A self-review is not independent verification; some potentially relevant historical full texts were not accessible.

## References

1. Shepherd, J. J. and Stojkov, L. (2007). “The logistic population model with slowly varying carrying capacity.” *ANZIAM Journal* 47, C492–C506. Published 4 January 2007. DOI: 10.21914/anziamj.v47i0.1058. https://journal.austms.org.au/ojs/index.php/ANZIAMJ/article/view/1058
2. Hasanbulli, M., Rogovchenko, S. P., and Rogovchenko, Y. V. (2013). “Dynamics of a Single Species in a Fluctuating Environment under Periodic Yield Harvesting.” *Journal of Applied Mathematics*, 167671. Published 27 March 2013. DOI: 10.1155/2013/167671. https://onlinelibrary.wiley.com/doi/10.1155/2013/167671
3. Castilho, C. and Srinivasu, P. D. N. (2007 volume, available online 23 September 2006). “Bio-economics of a renewable resource in a seasonally varying environment.” *Mathematical Biosciences* 205, 1–18. DOI: 10.1016/j.mbs.2006.09.011. PMID: 17087978. https://pubmed.ncbi.nlm.nih.gov/17087978/
