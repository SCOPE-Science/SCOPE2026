# A sharp two-to-one attenuation boundary for Poisson-optimal downstream DNA sampling

## Finding

A two-class downstream DNA transport signal with **known, unequal exponential attenuation rates** admits a unique Fisher-D-optimal downstream sampling distance when an independent source reference sample is available. If the slow-loss class is rare, the optimal distance remains bounded exactly when the fast attenuation rate is **less than twice** the slow rate; at equality it diverges with half the logarithmic slope found above the threshold.

Precisely, fix known \(0<\lambda<\mu\), positive known sampling efforts \(e_0,e_1\), and an unknown source copy intensity \(A>0\) and slow-class fraction \(0<p<1\). Set \(d=\mu-\lambda\) and \(r=\lambda/d\). Observe independent counts
\[
Y_0\sim\mathrm{Poisson}(e_0 A),\qquad
Y_x\sim\mathrm{Poisson}\!\left(e_1A\,[p e^{-\lambda x}+(1-p)e^{-\mu x}]\right),\quad x>0.
\]
For the parameter pair \((A,p)\), the Fisher-information determinant equals
\[
\det \mathcal I(x)=e_0e_1\frac{(e^{-\lambda x}-e^{-\mu x})^2}{p e^{-\lambda x}+(1-p)e^{-\mu x}}.
\]
Its unique maximizer \(x_*\) over \(0<x<\infty\) is \(x_*=-\log t_*/d\), where \(t_*\in(0,1)\) is the unique root of
\[
 r p+[r(1-2p)-1-p]t-(r+1)(1-p)t^2=0.
\]
The optimal distance strictly **decreases** as the slow-class fraction \(p\) increases, for fixed \(\lambda,\mu\). Its rare-class limit is sharply three-way:
\[
 x_* =\begin{cases}
 \dfrac{1}{\mu-\lambda}\log\!\dfrac{\mu-2\lambda}{\lambda p}+o(1),&\mu>2\lambda,\\[5pt]
 \dfrac{1}{2\lambda}\log\!\dfrac{2}{p}+o(1),&\mu=2\lambda,\\[5pt]
 \dfrac{1}{\mu-\lambda}\log\!\dfrac{\mu}{2\lambda-\mu}+o(1),&\lambda<\mu<2\lambda,
\end{cases}\qquad p\downarrow0.
\]
In the last case \(x_*\) tends to the displayed finite positive constant; the first two cases diverge. With a maximum accessible distance \(L>0\), the maximizer on \([0,L]\) is \(\min\{x_*,L\}\).

## Assumptions and scope

The two particle-size/decay classes are not interconverting, the source-to-downstream transfer obeys first-order spatial attenuation, and \(\lambda,\mu\) are fixed and calibrated independently. The unknown \(p\) is the class fraction **at the source**, not a downstream fraction. Sampling windows or aliquots are independently counted at steady concentration, with perfectly measured Poisson copy counts, a common fixed source intensity and fixed positive exposures. There is no contamination, background count, hydraulic change, particle transformation or spatially correlated observation error. The reference sample is fixed at \(x=0\); only the location of the second sample is optimized. The D criterion is local: its maximizing distance depends on a nominal \(p\), which is unknown in practice and must be supplied for design.

## Proof

Define \(f(x,p)=p e^{-\lambda x}+(1-p)e^{-\mu x}\) and \(g(x)=\partial_p f=e^{-\lambda x}-e^{-\mu x}\). For independent Poisson observations of means \(m_0=e_0 A\) and \(m_1=e_1 A f\), the standard score identity gives \(\mathcal I=\sum_j (\nabla m_j)(\nabla m_j)^\top/m_j\). In the order \((A,p)\), this is
\[
\mathcal I=\begin{pmatrix}
(e_0+e_1 f)/A & e_1g\\
e_1g & Ae_1g^2/f
\end{pmatrix}.
\]
Its determinant simplifies exactly to \(e_0e_1g^2/f\), independent of source strength \(A\). Set \(t=e^{-dx}\), so \(x>0\) corresponds bijectively to \(0<t<1\), with \(f=e^{-\lambda x}[p+(1-p)t]\) and \(g=e^{-\lambda x}(1-t)\). Up to the constant \(e_0e_1\), maximizing the determinant is therefore equivalent to maximizing
\[
F(t)=\frac{t^r(1-t)^2}{p+(1-p)t}.
\]
This tends to zero as \(t\downarrow0\) and as \(t\uparrow1\) because \(r,p>0\). Direct differentiation yields
\[
\frac{d}{dt}\log F(t)=\frac{P(t)}{t(1-t)[p+(1-p)t]},\qquad
P(t)=rp+[r(1-2p)-1-p]t-(r+1)(1-p)t^2.
\]
Here \(P(0)=rp>0\), \(P(1)=-2<0\), and the leading coefficient of this quadratic is strictly negative. Its roots have negative product, so exactly one is positive; that root lies in \((0,1)\). Thus \(F\) strictly increases then decreases and the stated point is the unique global maximum. Since the logarithmic derivative has a strict downward crossing at its root, and
\[
\frac{\partial}{\partial p}\left[\frac{d}{dt}\log F(t)\right]=\frac{1}{[p+(1-p)t]^2}>0,
\]
implicit differentiation shows \(dt_*/dp>0\), hence \(dx_*/dp<0\).

For the rare-class limit, write the stationary polynomial as \(P(t)=rp+[r-1+O(p)]t-[r+1+O(p)]t^2\). If \(r<1\), positivity and uniqueness force \(t_*\to0\), and balancing linear and constant terms gives \(t_*/p\to r/(1-r)\). If \(r=1\), the exact form \(P(t)=p-3pt-2(1-p)t^2\) gives \(t_*/\sqrt p\to1/\sqrt2\). If \(r>1\), the unique positive root tends to \((r-1)/(r+1)\). Substituting \(x_*=-\log t_*/d\), and using \(r<1\iff\mu>2\lambda\), proves all three asymptotic formulas. Unimodality gives the bounded-river restriction immediately.

## Verification

The attached standalone `checker.py` independently checks the symbolic Fisher determinant, the derivative polynomial, the sign and parameter derivative identities with exact algebra; performs 4,000 seeded positive-parameter local maximum comparisons; and checks the three small-fraction limits numerically. Execution command: `python checker.py` with Python, SymPy and the standard library. Output on the present artifact was `PASS: symbolic Fisher determinant and derivative; 4000 numerical local-optimum comparisons; rare-mixture asymptotics`. Numerical tests complement the symbolic proof and do not establish the quantified theorem by themselves. For example \(\lambda=1,\mu=2,p=1/2\) gives \(t_*=(\sqrt{17}-3)/4\) and \(x_*\approx1.2701966331\).

## Relationship to prior work

Pont (2024) models downstream fish-DNA attenuation using particle settling and degradation, and explicitly motivates spatial sampling choice. This finding instead analyzes a **two-class mixture of known removal rates under independent Poisson counts**, optimizing information about a source mixture fraction **jointly with unknown amplitude** and extracting the exact rare-fraction threshold. Lambert and Ellner (2025) study spatial D-optimal eDNA designs for species-environment regression on stream networks using Gaussian concentration errors and stochastic ecological variation, without the stated two-class Poisson distance law. Dette, Melas and Wong (2006) establish broader classical design results for homoscedastic Gaussian sums of exponentials with unknown exponential rates and amplitude parameters; those are not the present two-parameter, fixed-rate Poisson design or its rare-fraction threshold. General Poisson Fisher-information and local-D-design machinery are established and not claimed as new.

## Limitations

The result is a **local** Fisher-optimal design, not a claim about all estimator finite-sample risks, classification, or posterior-optimal designs. It holds only when the source sample position is fixed and both sampling efforts are fixed independently of downstream distance. At extremely low surviving counts, exact parameter estimation may be poor despite formal Fisher-optimality. The result does not apply unchanged with unknown attenuation rates, background contamination, detection saturation, correlated samples, site-dependent collection costs, non-exponential removal or more than two particle classes. The rare-class limit is taken at strictly positive \(p\), not at a regular interior model with \(p=0\). Historical literature coverage is not exhaustive and independent validation is not asserted.

## References

- Pont, D. (2024). "Predicting downstream transport distance of fish eDNA in lotic environments." *Molecular Ecology Resources*, 24(4), e13934. First online 2024-02-06. https://doi.org/10.1111/1755-0998.13934
- Lambert, T. D., and Ellner, S. P. (2025). "SDM meets eDNA: optimal sampling of environmental DNA to estimate species–environment relationships in stream networks." *Ecography*, e07644. https://doi.org/10.1111/ecog.07644
- Dette, H., Melas, V. B., and Wong, W. K. (2006). "Locally D-optimal designs for exponential regression models." *Statistica Sinica*, 16, 789–803. https://doi.org/10.17877/DE290R-15075
- Brandão-Dias, P. F. P., et al. (2023). "Suspended Materials Affect Particle Size Distribution and Removal of Environmental DNA in Flowing Waters." *Environmental Science & Technology*. https://doi.org/10.1021/acs.est.3c02638
