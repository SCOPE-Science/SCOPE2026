# A quantitative log-curvature gap separates biphasic DNA loss from relaxing removal

## Finding
Consider five exact positive concentrations at equally spaced times, \(t_j=t_0+jh\), \(j=0,1,2,3,4\), with \(t_0\geq0\) and \(h>0\). Define the three logarithmic curvatures
\[
K_j=\log\!\frac{C(t_j)C(t_{j+2})}{C(t_{j+1})^2},\qquad j=0,1,2.
\]
For a genuine positive two-pool exponential profile
\[
C_{\mathrm{pool}}(t)=A\bigl(w e^{-\lambda t}+(1-w)e^{-\mu t}\bigr),
\quad A>0,\quad 0<w<1,\quad 0<\lambda<\mu,
\]
put \(q=e^{-(\mu-\lambda)h}\in(0,1)\) and \(s=((1-w)/w)e^{-(\mu-\lambda)t_0}>0\). Then all \(K_j\) are positive and the following explicit *strict quantitative* inequality holds:
\[
\boxed{\displaystyle
\log\frac{K_1^2}{K_0K_2}>
(\log q)^2\min_{z\in\{s,sq^2\}}
\frac{2qz}{(1+z)(1+q^2z)}>0.}
\tag{1}
\]
For a single population subject instead to an exponentially relaxing positive removal hazard,
\[
C_{\mathrm{relax}}(t)=A\exp\bigl[-at-\beta(1-e^{-\kappa t})\bigr],
\quad A,a,\beta,\kappa>0,
\]
all \(K_j>0\), but exactly \(K_1^2=K_0K_2\). Thus five equally spaced noiseless concentrations distinguish these two stipulated mechanism classes without fitting their unknown coefficients. The count five is minimal for a universal distinction under this equally spaced design: explicit admissible models in the two classes coincide at four consecutive observations.

## Assumptions and scope
Both profiles are strictly positive for all \(t\geq0\), sampled at equally spaced known times, with no continuing input, unmodeled dilution, transport-source mixing, additive background, or measurement error. The two-pool profile represents two fixed noninterconverting types with different first-order loss rates. The relaxing-hazard profile has instantaneous loss rate \(a+\beta\kappa e^{-\kappa t}\), a positive rate decreasing toward \(a\). Observed units and the unknown common multiplicative amplitude \(A\) cancel from \(K_j\). The distinction concerns these two functional classes, *not* all possible biphasic-loss mechanisms.

## Proof
Write \(t_j=t_0+jh\) and factor the slow exponential from \(C_{\mathrm{pool}}\). With \(s_j=sq^j\), direct cancellation of the affine part of the log gives
\[
K_j=H(s_j),\qquad H(z)=\log\frac{(1+z)(1+q^2z)}{(1+qz)^2}
=\log\left(1+\frac{(1-q)^2z}{(1+qz)^2}\right)>0.
\tag{2}
\]
Let \(u=\log z\), \(G(u)=\log H(e^u)\),
\[
U(u)=2\log(1-q)+u-2\log(1+qe^u),\qquad
F(v)=\log\log(1+e^v).
\]
Then \(G=F\circ U\). Writing \(y=e^v>0\), exact differentiation yields
\[
F'(v)=\frac{y}{(1+y)\log(1+y)}>0,\qquad
F''(v)=\frac{y[\log(1+y)-y]}{(1+y)^2[\log(1+y)]^2}<0,
\]
while \(U''(u)=-2qe^u/(1+qe^u)^2<0\). Thus \(G''(u)<0\) everywhere. More precisely, \(\log(1+y)<y\) implies \(F'(v)>1/(1+y)\), and hence
\[
-G''(u)>F'(U(u))[-U''(u)]
>\frac{2qe^u}{(1+e^u)(1+q^2e^u)}.
\tag{3}
\]
Set \(d=-\log q>0\) and \(u_1=\log(sq)\). The exact central-difference integral identity gives
\[
2G(u_1)-G(u_1-d)-G(u_1+d)
=\int_{-d}^{d}(d-|v|)[-G''(u_1+v)]\,\mathrm dv.
\]
The triangular weight integrates to \(d^2\). The function \(z/[(1+z)(1+q^2z)]\) increases up to \(z=1/q\) and decreases thereafter, since the sign of its derivative is that of \(1-q^2z^2\). Hence its minimum on \([sq^2,s]\) is achieved at one of the two endpoints. Inserting (3) proves the strict bound (1). In particular \(K_1^2>K_0K_2\).

For \(C_{\mathrm{relax}}\), the logarithmic curvature cancels the constant and linear terms, leaving
\[
K_j=\beta e^{-\kappa(t_0+jh)}(1-e^{-\kappa h})^2>0.
\]
This is a geometric progression in \(j\), so \(K_1^2=K_0K_2\) exactly.

To prove minimality, take \(h=1\), \(t_0=0\) and the two-pool parameters \(A=1\), \(w=1/2\), \(\lambda=\log2\), \(\mu=\log4\). Its first five concentrations are
\[
1,\quad\frac38,\quad\frac5{32},\quad\frac9{128},\quad\frac{17}{512}.
\]
Put \(k_0=\log(10/9)\), \(k_1=\log(27/25)\), \(r=k_1/k_0\), and choose the relaxing-hazard parameters
\[
\kappa=-\log r,\qquad \beta=\frac{k_0}{(1-r)^2},\qquad
a=\log(8/3)-\frac{k_0}{1-r},\qquad A=1.
\tag{4}
\]
Here \(0<r<1\), \(\kappa,\beta>0\), and \(a>0\): indeed \(k_0<1/9\), \(k_0-k_1=\log(250/243)>7/250\), whence
\[
\frac{k_0}{1-r}=\frac{k_0^2}{k_0-k_1}<\frac{250}{567}<\frac12<\log(8/3).
\]
The first log decrement and first two log curvatures in (4) are respectively \(\log(8/3)\), \(k_0\), \(k_1\), matching the two-pool values. They recursively determine the first four concentrations, so these are exactly identical. Five measurements must differ by (1), proving the asserted four-point obstruction and five-point sufficiency.

## Verification
The standard-library script `checker.py` checks the exact rational sample, reproduces the positive-parameter four-point alias using 75-digit decimal arithmetic, checks the positive five-point separation and the bound in (1), and performs 12,000 supplementary numerical parameter comparisons. Run `python3 checker.py` (Python 3.11 or later). The universal conclusions follow from the analytic proof above, not from the finite checks. For the displayed alias, \(K_1^2-K_0K_2\approx0.0008444035494341963\), and the logarithmic separation in (1) is about \(0.15380809\), against a lower bound of about \(0.09043821\).

## Relationship to prior work
Brouwer et al. (2017) established mechanistic representations and structural identifiability limits for environmental-pathogen biphasic loss; they did not establish the present quantitative log-curvature gap against the specified relaxing-hazard alternative. Augustine et al. (2024) demonstrated the ecological importance of decreasing eDNA removal rates and competing loss models. Zanni et al. (2026) modeled biphasic eDNA decay with separate fast/slow particle groups. Classical exponential-sum/Prony and Hankel-rank arguments already imply the qualitative five-observation distinction for a two-point exponential mixture versus the infinite positive exponential mixture represented by the relaxing-hazard model. **That qualitative rank distinction is not claimed as new**: the specific strict log-curvature inequality (1), its explicit parameter-dependent lower bound, and the positive-rate four-point alias are the mathematical contributions here. Full historical priority, particularly for inequalities equivalent to (1), remains open pending additional literature assessment.

## Limitations
This is an exact structural diagnostic, not a field-calibrated statistical test. The positive bound can be arbitrarily small as mixture weights become degenerate, rates coalesce, or the observation window becomes poorly placed. Unknown additive contamination, source input, transport dilution, unequal observation times, experimental noise, or more than two pools can invalidate the displayed comparison. Different mechanistic models may produce identical biexponential curves and are not distinguishable by this theorem. An earlier relevant statistical article by Faddy and Jones (1999) was identifiable through its abstract but its full text was not available in the present examination; its precise coverage remains a residual originality risk.

## References
1. Augustine, B. C., et al. (2024). *A hierarchical model for eDNA fate and transport dynamics accommodating low concentration samples*. BioRxiv preprint, DOI: 10.1101/2024.03.27.586987. Companion public dataset: DOI 10.5061/dryad.8gtht76wc (initial public version 2024-03-27).
2. Brouwer, A. F., et al. (2017). *Modeling Biphasic Environmental Decay of Pathogens and Implications for Risk Analysis*. Environmental Science & Technology, 51, 2186–2196. DOI: 10.1021/acs.est.6b04030.
3. Zanni, M. Y., et al. (2026). *Beyond Exponential Decay: How Biphasic and Delayed Decay Dynamics Shape Marine eDNA Dispersal*. Ecology and Evolution, 16, e72987. DOI: 10.1002/ece3.72987.
4. Faddy, M. F., and Jones, M. C. (1999). *Modelling and Analysis of Data that Exhibit Temporal Decay*. Journal of the Royal Statistical Society: Series C, 48, 229–237. DOI: 10.1111/1467-9876.00151 (abstract examined; full text not accessed).
