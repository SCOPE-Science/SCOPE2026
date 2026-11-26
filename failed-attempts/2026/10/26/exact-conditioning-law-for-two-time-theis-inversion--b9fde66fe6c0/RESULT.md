# Exact conditioning law for two-time Theis inversion

## Finding

For the ideal homogeneous Theis pumping model at a fixed observation radius, let
\[
E_1(x)=\int_x^\infty \frac{e^{-u}}{u}\,du,\qquad c=\frac{t_2}{t_1}>1,\qquad x=\frac{r^2S}{4Tt_1}.
\]
The two-time drawdown ratio is \(R(x)=E_1(x/c)/E_1(x)\). It is strictly increasing from \(1\) to \(\infty\), and its inverse has exact relative condition number
\[
\kappa_{\mathrm{rel}}(x)=\left|\frac{d\log x}{d\log R}\right|=\frac{1}{h(x)-h(x/c)},\qquad h(x)=\frac{e^{-x}}{E_1(x)}.
\]
As \(x\downarrow0\),
\[
\kappa_{\mathrm{rel}}(x)\sim\frac{(-\gamma-\log x)^2}{\log c}\sim\frac{\log c}{(R-1)^2}.
\]
Consequently, although the ideal two-time inverse is unique, it becomes relatively ill-conditioned when the later-time drawdown ratio is close to one.

## Assumptions and scope

Assume a homogeneous, isotropic, laterally infinite aquifer of constant thickness; constant known pumping rate \(Q>0\); known observation radius \(r>0\); exact drawdown data; and the Theis model
\[
s(t)=\frac{Q}{4\pi T}E_1\!\left(\frac{r^2S}{4Tt}\right),\qquad T>0,\ S>0.
\]
The observation times satisfy \(0<t_1<t_2\). The result concerns deterministic relative conditioning of the ratio inversion for \(x\), not a full noise model or a guarantee of field identifiability under heterogeneity, boundaries, wellbore storage, or uncertain pumping rates.

## Proof

Set \(c=t_2/t_1>1\) and \(x=r^2S/(4Tt_1)>0\). The common amplitude \(Q/(4\pi T)\) cancels, giving \(R(x)=E_1(x/c)/E_1(x)\). Define \(h(x)=e^{-x}/E_1(x)\). Differentiating and using \(E_1'(x)=-e^{-x}/x\) gives
\[
 h'(x)=h(x)\left(\frac{h(x)}{x}-1\right).
\]
Since
\[
E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du<\frac1x\int_x^\infty e^{-u}\,du=\frac{e^{-x}}x,
\]
we have \(h(x)>x\), so \(h'(x)>0\). A logarithmic derivative now yields
\[
\frac{d\log R}{d\log x}=h(x)-h(x/c)>0.
\]
Thus \(R\) is strictly increasing. The standard endpoint expansions of the defining integral give \(E_1(x)=-\gamma-\log x+O(x)\) as \(x\downarrow0\), so \(R(x)\to1\). As \(x\to\infty\), \(E_1(x)\sim e^{-x}/x\), whence \(R(x)\sim c\exp(x(1-1/c))\to\infty\). Therefore \(R\) maps \((0,\infty)\) bijectively onto \((1,\infty)\).

By the inverse-function rule,
\[
\kappa_{\mathrm{rel}}=\left(\frac{d\log R}{d\log x}\right)^{-1}=\frac1{h(x)-h(x/c)}.
\]
Write \(L=-\gamma-\log x\) and \(a=\log c\). The small-argument expansion gives \(h(x)=L^{-1}+o(L^{-2})\) and \(h(x/c)=(L+a)^{-1}+o(L^{-2})\); hence
\[
h(x)-h(x/c)\sim\frac{a}{L^2},\qquad \kappa_{\mathrm{rel}}(x)\sim\frac{L^2}{a}.
\]
Also \(R(x)-1\sim a/L\), yielding \(\kappa_{\mathrm{rel}}(x)\sim a/(R-1)^2\). This proves the stated asymptotic conditioning law.

## Verification

The derivative identity, strict inequality \(E_1(x)<e^{-x}/x\), monotonicity, endpoint limits, and inverse condition number are established analytically above. No finite numerical experiment is used as a proof. The asymptotic statements follow from the standard small- and large-argument expansions of the exponential integral. The formula is dimensionless and invariant under a common change of time units. The result does not quantify measurement-noise propagation beyond the specified relative condition number.

## Relationship to prior work

Theis's original pumping solution introduces the exponential-integral drawdown formula and explicitly notes that two drawdown observations theoretically suffice to compute transmissivity and storage. That source also cautions that heterogeneity and delayed drainage can undermine the practical calculation. Zech, Müller, Mai, Heße, and Attinger study inverse estimation for heterogeneous transmissivity fields and show that reliability depends on the spatial placement and number of observations. The inspected sources do not state the exact relative condition-number identity or its late-time asymptotic in the homogeneous one-radius ratio reduction. The finding is a quantitative conditioning refinement, not a claim that two-observation structural identifiability itself is new.

## Limitations

The model excludes aquifer heterogeneity, finite boundaries, partial penetration, delayed yield, wellbore storage, uncertain discharge, and observation noise. The asymptotic concerns \(x\downarrow0\), equivalently a late-time/small dimensionless-argument regime at fixed parameters; the ratio then approaches one. The condition number is relative-to-relative and should not be confused with a statistical variance, Fisher information, or a full experimental-design optimum. Absolute novelty beyond the inspected literature is not asserted; other hydrologic inverse-problem analyses may contain related sensitivity results.

## References

1. C. V. Theis, “The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well using ground-water storage,” *Transactions, American Geophysical Union* **16** (1935), 519–524. DOI: 10.1029/TR016i002p00519. Full text: https://water.usgs.gov/ogw/pubs/Theis-1935.pdf.
2. A. Zech, S. Müller, J. Mai, F. Heße, and S. Attinger, “Extending Theis’ solution: Using transient pumping tests to estimate parameters of aquifer heterogeneity,” *Water Resources Research* **52** (2016), 6156–6170. DOI: 10.1002/2015WR018509. https://doi.org/10.1002/2015WR018509.
