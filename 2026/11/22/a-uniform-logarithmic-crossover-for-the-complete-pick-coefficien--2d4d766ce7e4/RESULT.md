# A uniform logarithmic crossover for the complete-Pick coefficients of Dirichlet kernels

## Finding
For every real \(0<\alpha\leq1\), let
\[
K_\alpha(z,w)=\sum_{j=0}^{\infty}\frac{(z\overline w)^j}{(j+1)^\alpha},\qquad
1-\frac1{K_\alpha(t)}=\sum_{n=1}^{\infty}b_n(\alpha)t^n.
\]
All coefficients \(b_n(\alpha)\) are strictly positive, sum to one, and have the following uniform critical crossover. For every finite \(S>0\), with \(\Phi(s)=(s/(2\sinh(s/2)))^2\) for \(s>0\) and \(\Phi(0)=1\),
\[
\lim_{n\to\infty}\ \sup_{0\leq\varepsilon\leq S/\log n}
\left|n(\log n)^2b_n(1-\varepsilon)-\Phi(\varepsilon\log n)\right|=0.
\]
The endpoint and fixed-parameter consequences are
\[
b_n(1)\sim\frac{1}{n(\log n)^2},\qquad
b_n(\alpha)\sim\frac{(1-\alpha)\sin(\pi\alpha)}{\pi}\,n^{\alpha-2}\quad(0<\alpha<1\text{ fixed}).
\]
The uniform crossover, rather than positivity or either elementary fixed-parameter consequence alone, is the finding being assessed.

## Assumptions and scope
The coefficient sequence belongs to the normalized analytic radial reproducing kernel above, with \(0<\alpha\leq1\). The endpoint \(\alpha=0\) is excluded because there \(K_0(t)=(1-t)^{-1}\) and \(b_1(0)=1\), \(b_n(0)=0\) for \(n\geq2\). All limits are taken through positive integers \(n\); the parameter \(\varepsilon\) may depend on \(n\) subject to the stated range. The logarithm is natural.

The nonnegative reciprocal coefficients give the canonical radial complete Nevanlinna–Pick representation: the feature map can be taken to have coordinates \(\sqrt{b_n(\alpha)}z^n\). The coefficients describe its distribution over monomial degrees. The result quantifies the passage from algebraic to logarithmic tails as the smoothness approaches the Dirichlet endpoint.

## Proof
**1. Stieltjes representation and exact coefficient measure.** For \(0<\alpha\leq1\), put \(\mathrm{Li}_\alpha(z)=\sum_{k\ge1}z^k/k^\alpha\) on its principal slit continuation. For \(|z|<1\),
\[
K_\alpha(z)=\frac{\mathrm{Li}_\alpha(z)}z
=\frac1{\Gamma(\alpha)}\int_0^1\frac{(-\log t)^{\alpha-1}}{1-zt}\,dt.
\]
The integral extends analytically to \(\mathbb C\setminus[1,\infty)\) and has positive imaginary part in the upper half-plane. It is positive for real \(z<1\), hence has no zero in this slit domain. Along the upper side of the cut, for \(x>1\),
\[
\operatorname{Im}\mathrm{Li}_\alpha(x+i0)=\frac{\pi(\log x)^{\alpha-1}}{\Gamma(\alpha)}.
\]
Applying the keyhole Cauchy coefficient formula to \(1-z/\mathrm{Li}_\alpha(z)\) (the outer arc vanishes because it grows at most \(O(|z|/(\log|z|)^\alpha)\)) yields, for every \(n\ge1\),
\[
\boxed{\quad b_n(\alpha)=\frac1{\Gamma(\alpha)}\int_0^\infty
\frac{e^{-(n-1)u}u^{\alpha-1}}{|\mathrm{Li}_\alpha(e^{u+i0})|^2}\,du.\quad}
\]
Every integrand is strictly positive. Because \(K_\alpha(r)\to+\infty\) as \(r\uparrow1\) and all coefficients are positive, monotone convergence in the defining generating series gives \(\sum_{n\ge1}b_n(\alpha)=1\).

**2. Fixed interior smoothness.** For fixed \(0<\alpha<1\), the standard slit polylogarithm expansion implies
\[
\mathrm{Li}_\alpha(e^{u+i0})=\Gamma(1-\alpha)e^{i\pi(1-\alpha)}u^{\alpha-1}+O(1),\qquad u\downarrow0.
\]
Set \(v=nu\) in the integral. On every fixed positive \(v\)-interval the resulting normalized integrand converges to \(e^{-v}v^{1-\alpha}/[\Gamma(\alpha)\Gamma(1-\alpha)^2]\). The small-\(u\) expansion gives an integrable \(e^{-v/2}v^{1-\alpha}\) bound there; the \(u\) away from zero part is exponentially small. Thus
\[
n^{2-\alpha}b_n(\alpha)\longrightarrow
\frac{\Gamma(2-\alpha)}{\Gamma(\alpha)\Gamma(1-\alpha)^2}
=\frac{(1-\alpha)\sin(\pi\alpha)}\pi.
\]

**3. Uniform critical crossover.** Write \(\alpha=1-\varepsilon\), \(0\le\varepsilon\le S/\log n\), and \(s=\varepsilon\log n\). For \(\varepsilon>0\), uniformly as \(u\downarrow0\) in this range,
\[
\mathrm{Li}_{1-\varepsilon}(e^{u+i0})=
\Gamma(\varepsilon)e^{i\pi\varepsilon}u^{-\varepsilon}
+\zeta(1-\varepsilon)+O(u).
\]
The singular parts of \(\Gamma(\varepsilon)\) and \(\zeta(1-\varepsilon)\) cancel. At \(\varepsilon=0\) one uses the exact formula \(\mathrm{Li}_1(e^{u+i0})=-\log(e^u-1)+i\pi\). Thus, for \(v\) in any compact subinterval of \((0,\infty)\), uniformly in \(s\in[0,S]\),
\[
\frac{\mathrm{Li}_{1-\varepsilon}(e^{v/n+i0})}{\log n}
=\frac{e^s-1}{s}+o(1),
\quad\text{where the quotient at }s=0\text{ is }1,
\]
while \((v/n)^{-\varepsilon}/\Gamma(1-\varepsilon)=e^s+o(1)\). These formulas give the pointwise uniform limiting density
\[
\frac{e^{-v}e^s}{((e^s-1)/s)^2}.
\]
For completeness, the required uniform integrability follows directly from the same polylogarithm expansion. If \(0<u\le n^{-1/2}\), its real part is bounded below by a positive constant times
\[
H_\varepsilon(u)=\begin{cases}(u^{-\varepsilon}-1)/\varepsilon,&\varepsilon>0,\\\log(1/u),&\varepsilon=0,\end{cases}
\]
for all sufficiently large \(n\), uniformly in the stated range. Since \(H_\varepsilon(u)\ge\tfrac12\log n\), the normalized integral on \(0<v\le\sqrt n\) is bounded by \(C_S e^{-v/2}(1+v^{-1/4})\). For \(v>\sqrt n\), use the exact imaginary part \(|\operatorname{Im}\mathrm{Li}_{1-\varepsilon}(e^{u+i0})|=\pi u^{-\varepsilon}/\Gamma(1-\varepsilon)\), which bounds the integrand by an exponentially integrable polynomial and makes this tail negligible after multiplying by \(n(\log n)^2\). Uniform dominated convergence now gives
\[
n(\log n)^2 b_n(1-\varepsilon)=
\frac{e^ss^2}{(e^s-1)^2}+o(1)=\Phi(s)+o(1)
\]
uniformly for \(s\in[0,S]\), as required.

## Verification
`check_coefficients.py` computes finite reciprocal coefficients from the exact convolution recurrence and checks positivity for a range of parameters, the exact first coefficients, and the slow approach of the critical normalizations to \(\Phi\). It is diagnostic only; the uniform infinite-\(n\) statement is proved by the integral representation and dominated convergence above. To run: `python3 check_coefficients.py` (Python standard library only).

## Relationship to prior work
The recent theorem of Luo and Rydhe (arXiv:2611.12778v1) proves the complete Pick property for concave analytic shifts and motivates examining finer quantitative information in canonical kernels; it does not state this coefficient crossover. General positivity of reciprocal coefficients for Dirichlet-type kernels and the complete Pick criterion appear in the 2022 work *Totally null sets and capacity in Dirichlet type spaces*, §2.1. The fixed endpoint \(\alpha=1\) is related to classical Gregory/reciprocal-logarithm coefficients, and the fixed-\(\alpha\) constant follows from established polylogarithm singular analysis. These component facts are not claimed as new in isolation. The focus is their **uniform two-parameter transition**, including its exact function \(\Phi\). Relevant existing complete-Pick polynomial-defect and fractional-power-kernel calculations concern different reciprocal kernels and do not imply this parameter-uniform law without additional analysis.

## Limitations
No statement is made for \(\alpha>1\), for multivariate nonradial kernels, or for the distinct extreme \(\alpha\downarrow0\) scale. The proof does not provide a uniform error rate in \(n\). Existing general uniform Tauberian theorems could give another derivation of the crossover; locating a verbatim earlier formulation is a remaining bibliographic risk.

## References
- S. Luo and E. Rydhe, *Concave shifts and the complete Nevanlinna–Pick property*, arXiv:2611.12778v1 (first public 2026-11-09), https://arxiv.org/html/2611.12778v1.
- N. Chalmoukis and M. Hartz, *Totally null sets and capacity in Dirichlet type spaces*, Journal of the London Mathematical Society (2022), §2.1, https://doi.org/10.1112/jlms.12617.
- NIST Digital Library of Mathematical Functions, §25.12, Polylogarithms, https://dlmf.nist.gov/25.12.
- *Gregory coefficients*, historical reciprocal-logarithm coefficients, https://en.wikipedia.org/wiki/Gregory_coefficients.
