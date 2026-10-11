# Exact viability frontier for contaminated-forager return in a honey-bee colony map

## Finding
For the nonspatial pesticide-contamination model of Magal, Webb, and Wu, let \(p\in[0,1]\) be the fraction of contaminated foragers that successfully return to the hive, let \(\alpha>0\) be the daily contamination rate, and let \(\mu>0\), \(\beta>0\), and \(\chi>0\) be the paper's mortality, recruitment, and Allee parameters. Define
\[
B=\frac{\beta}{2\chi},\qquad E=e^{-\mu},\qquad y=e^{\alpha}.
\]
The threshold quantity in the paper's equation (14) is algebraically
\[
R_1(p,\alpha)=\frac{BE\,[1+p(y-1-E)]}{(y-E)(1-pE)}.
\]
Assume the uncontaminated baseline is viable:
\[
R_0=\frac{BE}{1-E}>1.
\]
Then the exact frontier in the \((p,\alpha)\)-plane is available in closed form.

Set
\[
\alpha_\star=\log(E(1+B)).
\]
Because \(R_0>1\) is equivalent to \(E(1+B)>1\), one has \(\alpha_\star>0\). For \(0<\alpha<\alpha_\star\), \(R_1(p,\alpha)>1\) for every \(p\in[0,1]\). At \(\alpha=\alpha_\star\), equality occurs only at \(p=0\). For every \(\alpha>\alpha_\star\), there is a unique
\[
p_c(\alpha)=\frac{y-E-BE}{E\left[B(y-1-E)+(y-E)\right]}\in(0,1)
\]
such that
\[
R_1<1\quad\Longleftrightarrow\quad p<p_c(\alpha),
\qquad
R_1>1\quad\Longleftrightarrow\quad p>p_c(\alpha).
\]
Furthermore, \(p_c(\alpha)\) is strictly increasing and
\[
\lim_{\alpha\to\infty}p_c(\alpha)=\frac{1}{E(1+B)}<1.
\]

For the parameter set used in the 2019 paper,
\[
\beta=2900,\qquad \chi=11000,\qquad \mu=0.1,
\]
the formulas give
\[
\alpha_\star\approx0.0238253501,
\qquad
p_c(0.03)\approx0.6768201795.
\]
Solving the same frontier for \(\alpha\) at \(p=0.8\) gives
\[
\alpha_c(0.8)\approx0.0361803281.
\]
These reproduce the transition values \(p\approx0.6768\) at \(\alpha=0.03\) and \(\alpha\approx0.0362\) at \(p=0.8\) shown numerically in Figure 5 of the source paper.

## Assumptions and scope
The claim concerns the two-dimensional, nonspatial daily map in Magal, Webb, and Wu (2019), with the paper's parameter meanings and \(p\in[0,1]\), \(\alpha>0\), \(\mu>0\), \(\beta>0\), \(\chi>0\). The baseline condition \(R_0>1\) is assumed.

The source paper proves that \(R_1<1\) gives global extinction, while \(R_1>1\) gives three equilibria and a bistable regime. Accordingly, the frontier above separates those two parameter regimes. It is not a statement that every initial condition persists whenever \(R_1>1\).

## Proof
The paper writes
\[
R_1=\frac{\beta[1+p\kappa_2]}{2\chi(e^{\mu+\alpha}-1)},
\qquad
\kappa_2=\frac{e^\alpha-1}{1-pe^{-\mu}}.
\]
Substitute \(B=\beta/(2\chi)\), \(E=e^{-\mu}\), and \(y=e^\alpha\). Since
\[
e^{\mu+\alpha}-1=\frac{y-E}{E},
\]
one obtains
\[
R_1(p,\alpha)=\frac{BE\,[1+p(y-1-E)]}{(y-E)(1-pE)}.
\]

Differentiate with respect to \(p\):
\[
\frac{\partial R_1}{\partial p}
=
\frac{BE(y-1)}{(y-E)(1-pE)^2}>0
\]
because \(y>1>E\).

Differentiating first with respect to \(y\) gives
\[
\frac{\partial R_1}{\partial y}
=
\frac{BE(p-1)}{(1-pE)(y-E)^2}.
\]
Hence
\[
\frac{\partial R_1}{\partial \alpha}
=
y\frac{\partial R_1}{\partial y}
=
-\frac{BE(1-p)y}{(1-pE)(y-E)^2}<0
\]
for \(p<1\). For \(p=1\), cancellation gives
\[
R_1(1,\alpha)=\frac{BE}{1-E}=R_0,
\]
so the threshold is independent of \(\alpha\) on that boundary, exactly as noted numerically in the source.

At \(p=0\),
\[
R_1(0,\alpha)=\frac{BE}{y-E}.
\]
Therefore \(R_1(0,\alpha)=1\) exactly when
\[
y=E(1+B),
\]
which defines \(\alpha_\star=\log(E(1+B))\). Since \(R_0>1\) is equivalent to \(BE>1-E\), it is also equivalent to \(E(1+B)>1\), so \(\alpha_\star>0\).

For \(0<\alpha<\alpha_\star\), the minimum over \(p\in[0,1]\) occurs at \(p=0\), and that minimum exceeds one. At \(\alpha=\alpha_\star\), the minimum equals one only at \(p=0\).

For \(\alpha>\alpha_\star\), one has \(R_1(0,\alpha)<1\), while
\[
R_1(1,\alpha)=R_0>1.
\]
Strict monotonicity in \(p\) therefore gives a unique root in \((0,1)\). Solving \(R_1=1\) for \(p\) gives
\[
p_c(\alpha)=\frac{y-E-BE}{E\left[B(y-1-E)+(y-E)\right]}.
\]
Since \(\partial R_1/\partial p>0\) and \(\partial R_1/\partial\alpha<0\) at every interior frontier point,
\[
p_c'(\alpha)
=
-\frac{\partial R_1/\partial\alpha}{\partial R_1/\partial p}>0.
\]
Finally, dividing numerator and denominator of \(p_c\) by \(y\) yields
\[
\lim_{\alpha\to\infty}p_c(\alpha)
=
\frac{1}{E(1+B)}.
\]
The baseline condition gives \(E(1+B)>1\), so this limit lies below one.

## Verification
`verify.py` symbolically checks the simplified expression for \(R_1\), both derivative identities, the cancellation at \(p=1\), the closed-form solution of \(R_1=1\), and the large-\(\alpha\) limit. It also evaluates the source parameter set and reproduces the paper's numerical transition values to the displayed precision.

## Relationship to prior work
Magal, Webb, and Wu (2019) derive \(R_1\), prove the extinction/bistability alternatives, and plot \(R_1(p,\alpha)\). Their Figure 5 reports the numerical transition values \(p\approx0.6768\) at \(\alpha=0.03\) and \(\alpha\approx0.0362\) at \(p=0.8\), but the article does not state the closed-form frontier, its strict monotonicity, the contamination floor \(\alpha_\star\), or the asymptotic return threshold.

The spatial follow-up by the same authors (2020) reproduces the same \(R_1\) formula in the spatially homogeneous \(q=0\) reduction and invokes the 2019 analysis; it likewise does not state this closed-form frontier. The present result is therefore a sharpening of the parameter-threshold geometry of the published model, not a new biological mechanism and not a replacement for the source's global dynamical analysis.

## Limitations
The formula is specific to the homogeneous nonspatial map and to the particular Allee recruitment function used in the source. It does not cover spatial heterogeneity, memory of foraging locations, stochastic effects, seasonal forcing, parameter uncertainty, or alternative recruitment laws. The parameter \(p\) is a model-level return fraction, not a direct policy variable.

The source's implication \(R_1>1\) is bistability with positive equilibria, not persistence for every initial condition; the exact frontier should be interpreted accordingly.

## References
1. P. Magal, G. F. Webb, and Y. Wu, “An Environmental Model of Honey Bee Colony Collapse Due to Pesticide Contamination,” *Bulletin of Mathematical Biology* 81 (2019), 4908–4931. DOI: 10.1007/s11538-019-00662-5.
2. P. Magal, G. F. Webb, and Y. Wu, “A spatial model of honey bee colony collapse due to pesticide contamination of foraging bees,” *Journal of Mathematical Biology* 80 (2020), 2363–2393. DOI: 10.1007/s00285-020-01498-7.
