# Exact finite-sample multithreshold calibration of the paired exponential tail-ratio test

## Finding
For a predetermined pairing of \(2m\) independent observations from a common exponential distribution, the tail-ratio averages across **all sample-dependent pair-sum thresholds simultaneously** have a joint null law independent of the unknown rate. An explicit finite convolution recursion yields exact familywise-calibrated \(p\)-values after searching over any nonempty set of thresholds selected from the observed pair sums alone. For example, for four pairs, the joint probability that the averages of the largest \(2\), \(3\), and \(4\) pair-sum marks are all at most \(3/4\) is exactly \(5221/6144\), not a product of three marginal probabilities.

## Assumptions and scope
Let \(m\ge1\) be an integer. Under the null, the \(2m\) observations \(X_1,Y_1,\ldots,X_m,Y_m\) are independent and share the distribution \(\operatorname{Exp}(\lambda)\) for any unknown rate \(\lambda>0\). Pairs are fixed before observing the data or paired by a random mechanism independent of the data. Set \(S_i=X_i+Y_i\) and \(R_i=|X_i-Y_i|/(X_i+Y_i)\). Since pair sums are almost surely distinct, arrange them as \(S_{(1)}>\cdots>S_{(m)}\), and denote the corresponding ratio marks by \(Z_1,\ldots,Z_m\). For \(1\le k\le m\) set
\[
A_k=\frac1k\sum_{j=1}^k Z_j.
\]
Let \(K=K(S_{(1)},\ldots,S_{(m)})\) be any measurable, nonempty subset of \(\{1,\ldots,m\}\), depending only on the pair sums, and put \(M_K=\max_{k\in K} A_k\). Taking the threshold strictly between \(S_{(k)}\) and \(S_{(k+1)}\) selects exactly the largest \(k\) pair sums, so this is a multithreshold extension of the original fixed-threshold statistic.

## Proof
**1. Conditional independent uniforms.** In the coordinates \(s=x+y\) and \(t=x/(x+y)\), the joint density of one exponential pair is \(\lambda^2 s e^{-\lambda s}\,ds\,dt\) for \(s>0\), \(0<t<1\). Thus \(T=X/(X+Y)\) is uniform and independent of \(S\); \(R=|2T-1|\) is also uniform on \((0,1)\). Independence across the predetermined pairs implies that, conditional on the **entire labeled vector** of pair sums, the marks are independent uniforms. Ordering the sums merely permutes the marks by a permutation measurable with respect to those sums. Hence
\[
(Z_1,\ldots,Z_m)\mid(S_1,\ldots,S_m)\ \sim\ \operatorname{Unif}(0,1)^{\otimes m}.
\]
This proves simultaneously the rate-free null joint law and the validity of any sum-only selection \(K\).

**2. Exact joint CDF.** For any \(0<c<1\), start with the truncated density \(f_1(s)=\mathbf1_{(0,1)}(s)\mathbf1\{1\notin K\text{ or }s\le c\}\). For \(2\le j\le m\), recursively define
\[
f_j(s)=\mathbf1_{(0,j)}(s)\mathbf1\{j\notin K\text{ or }s\le jc\}
\int_{\max(0,s-1)}^{\min(j-1,s)} f_{j-1}(t)\,dt,
\]
with the integral interpreted as zero when its lower endpoint exceeds its upper endpoint. Convolution with the next independent \(\operatorname{Unif}(0,1)\) coordinate gives the density of the first \(j\) partial sums, restricted to each of the inequalities already imposed. Consequently
\[
F_{m,K}(c):=\Pr(M_K\le c\mid S_1,\ldots,S_m)=\int_0^m f_m(s)\,ds.
\]
The integrands are piecewise polynomials with rational breakpoints and rational coefficients whenever \(c\) is rational, so all such CDF evaluations are finite exact rational computations. For \(c\le0\) the CDF is zero; for \(c\ge1\) it is one.

**3. Simultaneous test calibration.** Given the sums, \(M_K\) is the maximum of finitely many nonconstant linear functions of an absolutely continuous uniform vector. For every \(a\), the event \(M_K=a\) lies in the finite union of zero-volume hyperplane slices \(\{A_k=a\}\); therefore its conditional distribution is continuous. The probability integral transform gives
\[
P_+=1-F_{m,K}(M_K)\mid(S_1,\ldots,S_m)\ \sim\ \operatorname{Unif}(0,1).
\]
Thus rejecting when \(P_+\le\alpha\) has exact conditional and unconditional size \(\alpha\) at every \(0<\alpha<1\), even for data-dependent choices of \(K\) measurable in the sums. The corresponding lower-tail scan follows by transforming each uniform mark \(Z_j\) into \(1-Z_j\). This proof concerns each one-sided scan separately, not an uncalibrated union of upper and lower scans.

**4. Finite-dimensional dependence.** For \(1\le k\le\ell\le m\), conditional independence yields
\[
\mathbb E(A_k\mid S)=\tfrac12,\qquad
\operatorname{Cov}(A_k,A_\ell\mid S)=\frac1{12\ell},\qquad
\operatorname{Corr}(A_k,A_\ell\mid S)=\sqrt{k/\ell}.
\]
These nonzero correlations explain why marginal calibrations cannot be multiplied as if independent.

## Verification
The included `CHECK.py` independently implements the finite rational convolution using piecewise polynomial integration. It verifies \(F_{2,\{1,2\}}(1/2)=3/8\), \(F_{2,\{1,2\}}(3/4)=23/32\), \(F_{3,\{1,2,3\}}(3/4)=17/24\), and \(F_{4,\{2,3,4\}}(3/4)=5221/6144\), plus elementary single-prefix cases. These are exact algebraic evaluations; correctness for arbitrary \(m\) follows from the conditional density and convolution induction above, not finite testing.

## Relationship to prior work
Asmussen and Lehtomaa (2017) introduced the conditional pair-sum contrast and threshold curve. Karagrigoriou et al. (2023), equations (10)–(13) and section 3.3, proposed fixed-threshold inference together with repeated pairings, asymptotic normal approximation, and empirical critical values. Iwashita and Klar (2023) established the gamma connection and studied the efficient U-statistic alternative and asymptotic variance. The independence of gamma sum and proportion is classical (Lukacs, 1955); we do not claim it as new. The additional mathematical result here is the *whole finite-sample joint law* of the nested, sum-ranked contrasts and its exact post-threshold-search calibration. The method uses **one fixed pairing**, not the repeated-data-dependent matching-average statistic; it does not claim the latter is covered.

## Limitations
The null must be a common-rate exponential sample. Pairing must not depend on observed values. The selected ranks \(K\) may depend on pair sums but must not be selected using the ratio marks. The exact recursion can incur computational cost with growing \(m\) and number of constraints; no complexity bound or power-optimality claim is made. The result is a test-construction and exact calibration statement, not a proof of consistency against every alternative or of a new characterization of exponentiality. The relevant independence and convolution ingredients are established classical facts, while priority for this particular combined threshold-scan calibration has not been independently certified.

## References
- S. Asmussen and J. Lehtomaa (2017), *Distinguishing Log-Concavity from Heavy Tails*, *Risks* 5(1), 10. https://doi.org/10.3390/risks5010010.
- A. Karagrigoriou, I. Mavrogiannis, G. Papasotiriou, I. Vonta (2023), *An Exponentiality Test of Fit Based on a Tail Characterization against Heavy and Light-Tailed Alternatives*, *Risks* 11(10), 169. https://doi.org/10.3390/risks11100169.
- T. Iwashita and B. Klar (2023, first published 17 August), *A gamma tail statistic and its asymptotics*, *Statistica Neerlandica*. https://doi.org/10.1111/stan.12316.
- E. Lukacs (1955), *A characterization of the gamma distribution*, *Annals of Mathematical Statistics* 26, 319–324.
