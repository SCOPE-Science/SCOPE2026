# Exponential-integral closed forms for completely mixed cooperation thresholds
## Finding
For every \(Q>0\), the geometric-harmonic limits used by Pires and Broom in their large completely mixed cooperation thresholds satisfy \(L_1(Q)=\int_0^Q(1-e^{-x})x^{-1}\,dx=\gamma+\log Q+E_1(Q)\) and \(L_2(Q)=\int_0^Q(e^x-1)x^{-1}\,dx=\operatorname{Ei}(Q)-\gamma-\log Q\), with continuous values \(L_1(0)=L_2(0)=0\). Hence \(L_1\) grows as \(\log Q+\gamma\), while \(L_2(Q)=e^Q Q^{-1}(1+O(Q^{-1}))\), and their exact derivatives are \(L_1'(Q)=(1-e^{-Q})/Q\) and \(L_2'(Q)=(e^Q-1)/Q\).

These functions are the limiting quantities that enter the source article's cooperation conditions for large completely mixed populations. The closed forms turn the defining limits into standard special functions and make the density dependence explicit.

## Assumptions and scope
Let \(Q>0\) be fixed. Along integer pairs \((M,MQ)\) with \(M\to\infty\), define
\[
L_{1,M}(Q)=\sum_{i=1}^{MQ-1}\frac{1-(1-1/M)^i}{i},\qquad
L_{2,M}(Q)=\sum_{i=1}^{MQ-1}\frac{(1-1/M)^{-i}-1}{i}.
\]
These are algebraically the two source limits. Replacing \(MQ-1\) by \(\lfloor MQ\rfloor-1\) does not change the limit. The claim concerns these analytic functions and their consequences; it does not alter any payoff model or evolutionary-dynamics assumption in the source.

## Proof
Put \(r_M=M\log(1-1/M)\), so \(r_M\to-1\). For \(x\ge0\), extend continuously at \(x=0\) the functions
\[
f_{1,M}(x)=\frac{1-e^{r_Mx}}{x},\qquad
f_{2,M}(x)=\frac{e^{-r_Mx}-1}{x}.
\]
Because \(r_M\to-1\), both families converge uniformly on every compact interval \([0,Q]\) to
\[
f_1(x)=\frac{1-e^{-x}}{x},\qquad
f_2(x)=\frac{e^x-1}{x},
\]
where both limits take value \(1\) at \(x=0\). The defining sums are Riemann sums:
\[
L_{j,M}(Q)=\frac{1}{M}\sum_{i=1}^{MQ-1}f_{j,M}(i/M),\qquad j\in\{1,2\}.
\]
Uniform convergence therefore yields
\[
L_1(Q)=\int_0^Q\frac{1-e^{-x}}{x}\,dx,
\qquad
L_2(Q)=\int_0^Q\frac{e^x-1}{x}\,dx.
\]
Using the standard expansions of the exponential integral gives
\[
L_1(Q)=\gamma+\log Q+E_1(Q),
\qquad
L_2(Q)=\operatorname{Ei}(Q)-\gamma-\log Q.
\]
Termwise expansion at the origin gives
\[
L_1(Q)=Q-\frac{Q^2}{4}+\frac{Q^3}{18}+O(Q^4),\qquad
L_2(Q)=Q+\frac{Q^2}{4}+\frac{Q^3}{18}+O(Q^4),
\]
which also proves the continuous values at \(Q=0\). Differentiating the integral forms gives the displayed derivatives. Finally, \(E_1(Q)=O(e^{-Q}/Q)\), while the standard positive-axis asymptotic of \(\operatorname{Ei}\) yields
\[
L_1(Q)=\log Q+\gamma+O(e^{-Q}/Q),\qquad
L_2(Q)=\frac{e^Q}{Q}\bigl(1+O(Q^{-1})\bigr).
\]

## Verification
A standalone checker evaluates the convergent power series for the two closed forms and compares them with direct finite-\(M\) sums. It reproduces the source's quoted values, including \(L_1(1)\approx0.79660\), \(L_2(1)\approx1.31790\), \(L_1(20)\approx3.57295\), and \(L_2(20)\approx2.56156\times10^7\). The proof itself is analytic; these computations are consistency checks rather than evidence for the limit.

## Relationship to prior work
Pires and Broom define \(L_1\) and \(L_2\) by geometric-harmonic limits, give numerical values and qualitative growth statements, and use them directly in the large-population cooperation conditions. Their article also notes that the related geometric-harmonic series appears in Haq, Schimit and Broom for the special density case \(Q=1\). In the inspected source text and related-paper searches, no exponential-integral evaluation of the density-dependent pair was found. The identities above are classical once the Riemann-integral representation is recognized; the contribution is their exact identification for these cooperation-threshold functions and the resulting derivative and asymptotic formulas.

## Limitations
The result evaluates the source's limiting threshold functions; it does not by itself prove new fixation criteria beyond conditions already expressed using \(L_1\) and \(L_2\). The originality assessment is limited by the possibility that the same elementary special-function reduction appears in material not located by the searches. No claim is made that the exponential integral identities are new as standalone analysis facts.

## References
Pires, D. L. and Broom, M. (2026). “Multiplayer social dilemmas in completely mixed populations and networks of mixing communities.” *Journal of Mathematical Biology* 93, 51. DOI: 10.1007/s00285-026-02464-5.

Haq, H., Schimit, P. H. T. and Broom, M. (2024). “The effects of herding and dispersal behaviour on the evolution of cooperation on complete networks.” *Journal of Mathematical Biology* 89, 49. DOI: 10.1007/s00285-024-02148-y.
