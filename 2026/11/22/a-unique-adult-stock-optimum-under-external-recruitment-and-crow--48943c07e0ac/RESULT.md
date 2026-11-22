# A unique adult-stock optimum under external recruitment and crowding-dependent mortality

## Finding

In a finite size-structured fish population with an externally prescribed juvenile input and uniform mortality increasing linearly with total population, increasing the input strictly increases total equilibrium abundance but **does not** increase the equilibrium number of mature individuals indefinitely. For every positive maturation cutoff below the upper size boundary, the mature abundance has exactly one strict global maximum as recruitment increases, and tends to zero at high recruitment. The exact optimizing input is determined by a unique scalar root for every positive parameter choice. When maturation is halfway through the size interval and baseline mortality vanishes, the optimum has a closed form using the principal Lambert function \(W_0\).

## Assumptions and scope

Fix \(L>0\), constant growth velocity \(\gamma>0\), crowding coefficient \(\alpha>0\), natural baseline mortality \(\mu_0\ge0\), and maturation displacement \(0<h<L\). Size \(\ell\in[0,L]\) measures displacement from the entry size, not physical age. Let \(x(t,\ell)\) be fish number per unit size, \(N(t)=\int_0^L x(t,\ell)\,d\ell\), and let \(p>0\) be constant exogenous entry flux. The unharvested transport model is

\[\partial_t x+\gamma\partial_\ell x=-(\mu_0+\alpha N(t))x,\qquad \gamma x(t,0)=p.\]

This is the constant-growth, constant-weight crowding and linearly crowding-dependent-mortality subfamily of the exogenously forced size-transport framework in Yu–Wang–Liang [1]. No endogenous reproduction, size-dependent weight, or harvesting is assumed. For a nonnegative steady solution \(x_p\), define total count \(N_p=\int_0^Lx_p\,d\ell\) and mature count \(A_h(p)=\int_h^Lx_p\,d\ell\).

Set \(\beta=h/L\in(0,1)\), \(t_0=\mu_0L/\gamma\), and \(t=(\mu_0+\alpha N)L/\gamma\). With \(H_\beta(t)=\beta-(1-\beta)/(e^{(1-\beta)t}-1)+1/(e^t-1)\), interpreted by continuity at \(t=0\), there exists exactly one \(t_*>t_0\) satisfying

\[(t_*-t_0)H_\beta(t_*)=1.\]

The unique recruitment level that maximizes mature count is obtained by setting \(N_*=(\gamma/(\alpha L))(t_*-t_0)\) and

\[p_*=\frac{N_*(\mu_0+\alpha N_*)}{1-e^{-t_*}}.\]

The result holds for *every* \(h\in(0,L)\), not merely a fitted cutoff. For \(\mu_0=0\) and \(h=L/2\), writing \(w=W_0(e^{-1})\),

\[N_*=\frac{2\gamma}{\alpha L}(1+w),\qquad A_h(p_*)=\frac{2\gamma}{\alpha L}w.\]

## Proof

**1. Unique stationary state and monotone total count.** At a fixed candidate total count \(N\), set \(q=(\mu_0+\alpha N)/\gamma\). The linear stationary transport equation and boundary flux imply uniquely

\[x(\ell)=\frac{p}{\gamma}e^{-q\ell}.\]

Integrating gives \(N=p(1-e^{-qL})/(\mu_0+\alpha N)\), hence

\[p(N)=\frac{N(\mu_0+\alpha N)}{1-e^{-(\mu_0+\alpha N)L/\gamma}}=\frac{\gamma}{L}N\frac{t}{1-e^{-t}},\qquad N>0.\]

For \(t>0\), \(d[t/(1-e^{-t})]/dt=[1-(1+t)e^{-t}]/(1-e^{-t})^2>0\), since \(e^t>1+t\). Since \(t=t_0+(\alpha L/\gamma)N\), the map \(N\mapsto p(N)\) is strictly increasing, with \(p(N)\to0\) as \(N\downarrow0\) and \(p(N)\to\infty\) as \(N\to\infty\). At \(t_0=0\), interpret \(t/(1-e^{-t})\) as \(1\) at zero. Thus every \(p>0\) has exactly one positive steady state and \(N_p\) increases strictly and without bound with \(p\).

**2. Adult fraction and a monotone logarithmic slope.** Direct integration of the same exponential profile yields

\[A_h(N)=N\,F_\beta(t),\qquad F_\beta(t)=\frac{e^{-\beta t}-e^{-t}}{1-e^{-t}}>0.\]

Logarithmic differentiation gives \(-F_\beta'(t)/F_\beta(t)=H_\beta(t)\), so

\[\frac{d}{dN}\log A_h(N)=\frac1N-\frac{\alpha L}{\gamma}H_\beta(t)=\frac{1-(t-t_0)H_\beta(t)}{N}.\]

To prove the strictly increasing nature of the second factor, observe that \(H_\beta(t)\to\beta/2>0\) as \(t\downarrow0\), and, with \(a=1-\beta\in(0,1)\),

\[H_\beta'(t)=\frac{a^2}{4\sinh^2(at/2)}-\frac1{4\sinh^2(t/2)}>0,\qquad t>0.\]

The inequality follows because \(s\mapsto s/\sinh s\) is strictly decreasing on \((0,\infty)\): its derivative has numerator \(\sinh s-s\cosh s<0\), whose derivative is \(-s\sinh s<0\). Therefore \(H_\beta\) is strictly positive and increasing on \([0,\infty)\), with limit \(\beta\) as \(t\to\infty\).

The product \((t-t_0)H_\beta(t)\) increases strictly from zero at \(t=t_0\) to infinity at large \(t\). It therefore equals one at exactly one \(t_*>t_0\). The logarithmic slope of \(A_h\) is strictly positive below this root and strictly negative above, establishing unique strict global maximization. Since \(F_\beta(t)\sim e^{-\beta t}\), mature abundance vanishes as \(N\to\infty\), whereas \(A_h\to0\) as \(N\downarrow0\). The maximum is nondegenerate: \(d^2\log A_h/dN^2=-(\alpha L/\gamma)[H_\beta+(t-t_0)H_\beta']/N<0\) at the root.

**3. Exact midpoint calibration.** With \(\beta=1/2\) and \(\mu_0=0\), \(F_{1/2}(t)=1/(1+e^{t/2})\) and \(t=\alpha LN/\gamma\). Set \(z=\alpha LN/(2\gamma)\); the stationarity equation becomes \((z-1)e^z=1\). Therefore \(z=1+W_0(e^{-1})\). Substitution proves the announced \(N_*\), adult optimum and \(p_*\). For \(\gamma=\alpha=L=1\), \(N_*=2.556929085522\ldots\), \(p_*=7.087466207986\ldots\), and \(A_*=0.556929085522\ldots\).

**4. Severity of high-input decline.** At high input, \(p\sim\alpha N_p^2\), hence \(N_p\sim\sqrt{p/\alpha}\) and

\[\lim_{p\to\infty}\frac{\log A_h(p)}{\sqrt p}=-\frac{h\sqrt\alpha}{\gamma}<0.\]

This gives a quantitative stretched-exponential collapse of mature count even while total count diverges.

## Verification

The standalone script `CHECK.py` evaluates the stationarity residual, direct abundance integrals, strict comparisons on both sides of the unique root, the midpoint Lambert-function numeric calibration (computed by bisection without external libraries), and representative parameter sweeps. Run with `python3 CHECK.py`. The proof above is analytic for the entire parameter domain; finite numerical sweeps are supporting diagnostics only.

## Relationship to prior work

Yu, Wang and Liang [1, Sections 2 and 3] formulated the exogenous-influx, crowding-coupled size-transport model and obtained a positive stationary profile and a scalar closure equation. The present theorem takes an explicit natural subfamily and varies the **external inflow**, contrasting total population with abundance above **every** maturation cutoff; this all-cutoff unique-optimum classification is not asserted in the inspected source. Density-dependent fish survival and broader impacts of crowding on fisheries are well documented [2–4]; the qualitative possibility of crowding losses or dome-shaped stock–recruitment response is not presented as a new phenomenon. The contribution here is the exact, all-parameter uniqueness, monotonicity and high-input asymptotic result for externally supplied recruitment under a specified mortality closure, including its explicit midpoint Lambert-function optimum.

## Limitations

The theorem is a statement about **stationary solutions**. It does not establish global dynamical stability or convergence from arbitrary initial conditions. Constant size-growth and size-independent death within a given population, with crowding entering death linearly, are substantive assumptions. Mature *number* is not biomass or harvested yield, and external input is not endogenous reproduction. No claim is made that high stocking produces a universal decline in wild populations or that the computed optimum is an empirical management prescription. Earlier literature not available in full may contain analogous special-case formulas; historical priority remains bounded by inspected sources.

## References

1. J. Yu, L. S. Wang, Y. Liang, *Size-Selective Threshold Harvesting under Nonlocal Crowding and Exogenous Recruitment*, arXiv:2603.27368 (first public version 2026-03-28), https://arxiv.org/abs/2603.27368 ; version 2 https://arxiv.org/pdf/2603.27368 ; *International Journal of Differential Equations* 2026, article 2523535, https://doi.org/10.1155/ijde/2523535.
2. K. Lorenzen, *Allometry of natural mortality as a basis for assessing optimal release size in fish-stocking programmes*, *Canadian Journal of Fisheries and Aquatic Sciences* 57 (2000), 2374–2381; https://www.gov.uk/research-for-development-outputs/allometry-of-natural-mortality-as-a-basis-for-assessing-optimal-release-size-in-fish-stocking-programmes.
3. J. G. K. Harris, *The effect of density-dependent mortality on the shape of the stock and recruitment curve*, *Journal du Conseil* 36 (1975), 144–149, https://doi.org/10.1093/icesjms/36.2.144.
4. *The consequences of density-dependent individual growth for sustainable harvesting and management of fish stocks*, *Fish and Fisheries* (2023), https://doi.org/10.1111/faf.12736.
