# A sharp shade-gap transition for two sunflecks with induction and photodamage

## Finding

Consider a leaf exposed to two identical, fixed-length high-light episodes (sunflecks), separated by a variable shade interval. The leaf has both saturating photosynthetic induction and saturating photodamage, and realized light-period assimilation is the product of induced capacity and intact photochemical fraction. This model has an exact global scheduling classification.

Let \(a,b,c,d,\ell>0\) with \(d>b\). Define
\[
 C=\frac{1-e^{-c\ell}}{c},\quad
 D=\frac{1-e^{-(a+c)\ell}}{a+c},\quad
 X=1-e^{-a\ell},\quad Y=1-e^{-c\ell},
\]
\[
 P=DX,\qquad Q=(C-D)Y,\qquad R=DXY,
\]
and \(\Delta=-bP+dQ+(b+d)R\). The total modeled assimilation during the two sunflecks, as a function of the intervening shade length \(g\geq0\), is
\[
 \mathcal A(g)=2(C-D)+Pe^{-bg}-Qe^{-dg}-Re^{-(b+d)g}.
\]
If \(\Delta\leq0\), \(g=0\) is the **unique** global maximizer. If \(\Delta>0\), there is a **unique** positive global maximizer \(g_*\), characterized by
\[
 bP=dQe^{-(d-b)g_*}+(b+d)Re^{-dg_*}.
\]
With an imposed cap \(0\leq g\leq G\) (\(G\geq0\)), the unique maximizer is \(\min\{g_*,G\}\) when \(\Delta>0\), and zero otherwise.

A fully explicit pulse-length phase transition occurs for the natural nondimensional illustrative rate choice \(a=b=c=1\), \(d=2\). Put
\[
 u_c=\frac{\sqrt{57}-3}{6},\qquad \ell_c=-\log u_c=0.276668624779832\ldots.
\]
Then zero shade uniquely maximizes assimilation when \(\ell\leq\ell_c\). For \(\ell>\ell_c\), a positive optimal shade gap emerges, increases strictly with \(\ell\), and tends to \(\log3\) as \(\ell\to\infty\). Explicitly, writing \(u=e^{-\ell}\) and \(z=e^{-g_*}\), \(z\in(1/3,1)\) is the unique root of
\[
 1=2\frac{1-u}{1+u}z+3(1-u)z^2.
\]
At the threshold the positive branch emerges continuously and linearly, with right derivative
\[
 \left.\frac{dg_*}{d\ell}\right|_{\ell_c+}
 =\frac{u_c[4/(1+u_c)^2+3]}{(1-u_c)[2/(1+u_c)+6]}
 =1.887458608817688\ldots.
\]
For example, at \(\ell=1\), the optimal shade gap is \(g_*=0.649546035969512\ldots\), improving modeled two-fleck assimilation from \(0.373822536207754\ldots\) to \(0.483248394082746\ldots\), or \(29.2721\ldots\%\).

## Assumptions and scope

The initially uninduced and undamaged leaf starts at \((x,y)=(0,0)\), where \(x\in[0,1]\) is photosynthetic induction and \(y\in[0,1]\) is the photodamaged fraction. In each high-light interval of fixed duration \(\ell\), the equations are \(\dot x=a(1-x)\) and \(\dot y=c(1-y)\). In the intervening low-light interval of variable duration \(g\), the equations are \(\dot x=-bx\) and \(\dot y=-dy\). Only during high light is carbon gain counted, at instantaneous normalized rate \(x(1-y)\). The two high-light durations and their intensity are fixed. There is no payoff or cost assigned to the intervening shade interval itself, and no terminal carbon valuation. All rates and the pulse length are strictly positive; the global theorem requires damage recovery faster than induction loss, \(d>b\). The special-case claim uses dimensionless time units.

## Proof

During the first sunfleck, \(x(t)=1-e^{-at}\), \(y(t)=1-e^{-ct}\), so its gain is \(\int_0^\ell(1-e^{-at})e^{-ct}\,dt=C-D\). At the start of the second sunfleck, after shade \(g\), the states are \(x_0=Xe^{-bg}\) and \(y_0=Ye^{-dg}\). At time \(t\) into the second sunfleck,
\[
 x(t)=1-(1-x_0)e^{-at},\qquad 1-y(t)=(1-y_0)e^{-ct}.
\]
Thus the second gain is \((1-y_0)[C-D+Dx_0]\). Expanding and adding the first gives the asserted exact expression for \(\mathcal A(g)\).

Since \(C>D>0\) and \(0<X,Y<1\), the coefficients \(P,Q,R\) are strictly positive. Differentiation gives
\[
 \mathcal A'(g)=e^{-bg}B(g),\qquad
 B(g)=-bP+dQe^{-(d-b)g}+(b+d)Re^{-dg}.
\]
For \(d>b\), \(B'(g)=-d(d-b)Qe^{-(d-b)g}-d(b+d)Re^{-dg}<0\) on \([0,\infty)\), while \(B(g)\to-bP<0\). Hence \(\mathcal A\) strictly decreases for every positive \(g\) when \(B(0)=\Delta\leq0\); otherwise it first strictly increases, then strictly decreases, crossing only at the unique root of \(B\). This proves global optimality and the capped version without relying on numerical optimization. The strictness also covers the boundary \(\Delta=0\).

In the special case, write \(u=e^{-\ell}\). Direct substitution yields
\[
 P=\tfrac12(1-u)^2(1+u),\quad Q=\tfrac12(1-u)^3,\quad R=\tfrac12(1-u)^3(1+u),
\]
\[
 \Delta=\tfrac12(1-u)^2(4-3u-3u^2).
\]
Since \(u\) strictly decreases from \(1\) to \(0\) as \(\ell\) increases, the quadratic factor changes sign exactly at \(u_c\), proving the unique sharp critical length. For \(\ell>\ell_c\), dividing the critical-point equation by \(P\) gives the stated strictly increasing quadratic in \(z=e^{-g_*}\). For each fixed \(z>0\), its right side strictly increases as \(\ell\) increases, forcing the unique positive root \(z\) to decrease; hence \(g_*\) strictly increases. As \(u\to0\), the equation becomes \(1=2z+3z^2\), with unique positive root \(z=1/3\). The derivative at the onset follows by implicit differentiation of the same quadratic, with nonzero \(z\)-derivative. This completes the proof.

## Verification

The included standalone `check_sunfleck.py` evaluates the formula against direct quadrature of both state trajectories, checks the classified maximizer against fine-grid competitors for 120 deterministic randomly selected positive parameter tuples with \(d>b\), checks the special-case transition and monotone branch, and reproduces the illustrative numbers. It reports 12,050 passed assertions in the current test configuration. The continuum and all-parameter conclusions come from the proof, not from finite test coverage. Run `python check_sunfleck.py` in an environment with Python and SciPy.

## Relationship to prior work

The broad phenomenon of light-induced activation, deactivation in shade, fluctuating carbon assimilation, and photoinhibition is long established. Thornley (1974) treats explicit first-order photosynthetic responses to fluctuating light. Gross (1982) constructs a dynamic single-enzyme-pool model and simulates carbon gain under fluctuating light, but its examined model and objective are different from the two-state product-gated, two-pulse gap optimization above. Sassenrath-Cole and Pearcy (1994) measure contrasting induction kinetics. Pearcy, Gross and He (1997) develop a more detailed dynamic C3 model and report simulated lightfleck carbon assimilation; the accessible abstract does not establish the present exact global scheduling result, though full-text comparison remains incomplete. Leakey, Press and Scholes (2003), and Leakey, Scholes and Press (2004), document ecophysiological tradeoffs of sunflecks and inhibition but do not, in the inspected full-text portions, provide these two-pulse analytic thresholds. The result does not claim novel physiology or a new general exponential-sum theorem; the subject is the exact structural law for this specified kinetic benchmark.

## Limitations

This is a deliberately minimal independent-state model, not a calibrated physiological or ecological prediction. The multiplicative assimilation gate, first-order kinetics and initial states are assumptions; real photosynthesis involves stomata, repair pathways, photorespiration, induction stages, post-illumination fixation, dark respiration, finite daylight and canopy constraints. The unrestricted-gap optimum allows the overall experiment to grow longer; a fixed experiment horizon is represented only by the explicit finite-gap cap. No claims are made for \(d\leq b\), unequal fleck lengths, more than two flecks, or direct fitness and plant growth. Novelty priority remains subject to broader mathematical optimization literature and complete inspection of some historical dynamic-photosynthesis sources.

## References

1. Thornley, J. H. M. (1974), *Light Fluctuations and Photosynthesis*, Annals of Botany 38, 363–373. https://doi.org/10.1093/oxfordjournals.aob.a084820 (public date 1974-03-01).
2. Gross, L. J. (1982), *Photosynthetic Dynamics in Varying Light Environments: A Model and Its Application to Whole Leaf Carbon Gain*, Ecology 63, 84–93. https://doi.org/10.2307/1937034.
3. Sassenrath-Cole, G. F. and Pearcy, R. W. (1994), *Regulation of Photosynthetic Induction State by the Magnitude and Duration of Low Light Exposure*, Plant Physiology 105, 1115–1123. https://doi.org/10.1104/pp.105.4.1115.
4. Pearcy, R. W., Gross, L. J. and He, D. (1997), *An improved dynamic model of photosynthesis for estimation of carbon gain in sunfleck light regimes*, Plant, Cell & Environment 20, 411–424. https://doi.org/10.1046/j.1365-3040.1997.d01-88.x.
5. Leakey, A. D. B., Press, M. C. and Scholes, J. D. (2003), *High-temperature inhibition of photosynthesis is greater under sunflecks than uniform irradiance in a tropical rain forest tree seedling*, Plant, Cell & Environment 26, 1681–1690. https://doi.org/10.1046/j.1365-3040.2003.01086.x.
6. Leakey, A. D. B., Scholes, J. D. and Press, M. C. (2004), *Physiological and ecological significance of sunflecks for dipterocarp seedlings*, Journal of Experimental Botany 56, 469–482. https://doi.org/10.1093/jxb/eri055 (public date 2004-12-13).
