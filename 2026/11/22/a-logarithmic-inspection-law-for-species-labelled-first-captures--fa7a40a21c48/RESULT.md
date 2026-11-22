# A logarithmic inspection law for species-labelled first captures

## Finding

Consider \(k\ge3\) distinguishable species with independent homogeneous Poisson encounter streams of unknown positive intensities \(\lambda_1,\ldots,\lambda_k\) at each of many identical independent single-catch stations. A station is armed at time zero, records **only** whether it is empty at retrieval time \(t>0\) or the species identity of the first capture, and cannot record the capture time or capture more than one individual. Set \(r=\sum_{i=1}^k\lambda_i\) and \(x=rt\). The single-station Fisher-information determinant for the entire vector of species intensities is

\[
\det \mathcal I(\boldsymbol\lambda;t)
=\frac{t^2 r^{2-k}}{\prod_{i=1}^k\lambda_i}
 e^{-x}(1-e^{-x})^{k-2}.
\]

For each integer \(k\ge3\), there is exactly one locally D-optimal retrieval duration over all \(t>0\). It is \(t_k=x_k/r\), where \(x_k>2\) is the unique root of

\[
\frac2{x_k}-1+\frac{k-2}{e^{x_k}-1}=0.
\]

The dimensionless optimum \(x_k\) increases strictly with \(k\), independently of the unknown species proportions, and obeys

\[
x_k=\log k+\frac2{\log k}+O((\log k)^{-2})\quad(k\to\infty).
\]

At its optimum, the empty-station probability is asymptotic to \(1/k\). The species-intensity determinant at the optimal duration, divided by its time-independent factor \(r^{-k}/\prod_i\lambda_i\), is asymptotic to \((\log k)^2/(e k)\). If capture timestamps are retained for the **same** horizon \(t\), the ratio of the coarsened to time-resolved determinants is exactly

\[
\eta(x)=\left(\frac{x}{2\sinh(x/2)}\right)^2,
\]

independent of species intensities and species number. At \(t_k\), \(\eta(x_k)\sim (\log k)^2/k\).

## Assumptions and scope

The result is a *local* Fisher D-design, conditional on nominal positive rates \(\lambda_i\). At each independent station all species arrive as independent stationary Poisson processes with fixed rates; the first arrival closes the station. The species of the first captured animal is classified correctly, including a distinguishable no-capture category, but its time is not retained. Each station uses the same chosen duration, and the number of stations is fixed independently of \(t\). There is no repeated trapping, recapture, animal movement dependence, weather heterogeneity, competing device cost, or finite observation deadline. The model considers at least three species; a two-species boundary calculation is noted below as background.

D-optimality means maximizing the determinant of the expected Fisher information for all \(k\) unknown per-species intensity parameters, not maximizing the expected number of species captured or optimizing a marginal species alone. The optimum depends on the unknown total intensity through the local scaling \(r t\). Changing species number while holding total encounter intensity fixed makes optimal physical time increase; without fixing \(r\), only the dimensionless statement applies.

## Proof

**1. Competing Poisson arrivals and a full-rank parameterization.** Put \(q=1-e^{-rt}\) and \(\pi_i=\lambda_i/r\), so all \(\pi_i>0\) and their sum is one. The observed station category \(Y\in\{0,1,\ldots,k\}\) has probabilities

\[
P(Y=0)=e^{-rt},\qquad P(Y=i)=q\pi_i\quad(1\le i\le k).
\]

Thus \(Y\) separates into a Bernoulli captured/not-captured indicator and, conditional on capture, a categorical species label. The coordinate transformation from positive \(\boldsymbol\lambda\) to \((r,\pi_1,\ldots,\pi_{k-1})\) is smooth, invertible, and has Jacobian determinant of absolute value \(r^{-(k-1)}\).

**2. Exact Fisher determinant.** Independence of the two score components gives a zero off-diagonal information block. For \(r\), the Bernoulli Fisher entry is \(t^2 e^{-rt}/q\). The remaining \((k-1)\)-dimensional block is

\[
q\left[\operatorname{diag}(\pi_1^{-1},\ldots,\pi_{k-1}^{-1})+
\pi_k^{-1}\boldsymbol 1\boldsymbol1^{\mathsf T}\right].
\]

By the matrix determinant lemma, its determinant is \(q^{k-1}/\prod_{i=1}^k\pi_i\). Multiply by the scalar information entry and by the square \(r^{-2(k-1)}\) of the inverse-coordinate Jacobian. Since \(\prod_i\pi_i=(\prod_i\lambda_i)/r^k\), this is precisely the determinant displayed in the Finding. It is positive for every interior parameter and \(t>0\).

**3. Unique global duration.** For fixed parameters, ignoring its strictly positive constant factor, the objective is \(G_k(x)=x^2 e^{-x}(1-e^{-x})^{k-2}\). Its logarithmic derivative is

\[
\Psi_k(x)=\frac2x-1+\frac{k-2}{e^x-1}.
\]

For \(k\ge3\), \(\Psi'_k(x)=-2/x^2-(k-2)e^x/(e^x-1)^2<0\) for every \(x>0\). Also \(\Psi_k(0+)=+\infty\), \(\Psi_k(\infty)=-1\), and \(\Psi_k(2)>0\). Hence there is exactly one root \(x_k>2\), with \(G_k\) strictly increasing below it and decreasing above it. The endpoint limits \(G_k(0+)=G_k(\infty)=0\) establish a unique global maximum, not merely a stationary point.

**4. Species-number monotonicity and asymptotics.** Since \(\Psi_{k+1}(x)-\Psi_k(x)=1/(e^x-1)>0\), the unique roots are strictly increasing. The root equation rearranges to

\[
e^{x_k}=1+\frac{k-2}{1-2/x_k}.
\]

For sufficiently large \(k\), substitution of \(\log k\) and \(\log k+1\) in \(\Psi_k\) gives opposite signs, so \(x_k=\log k+O(1)\). Taking logarithms of the preceding identity and expanding \(-\log(1-2/x_k)\) then yields \(x_k=\log k+2/\log k+O((\log k)^{-2})\). Consequently \(ke^{-x_k}\to1\), \((1-e^{-x_k})^{k-2}\to e^{-1}\), and \(G_k(x_k)\sim(\log k)^2/(e k)\). These asymptotics are uniform in the species composition because the dimensionless optimizer does not use it.

**5. Exact information cost of forgetting timestamps.** In the richer experiment, the first-arrival time is recorded if a capture occurs. In \((r,\boldsymbol\pi)\) coordinates the conditional categorical block stays unchanged. The scalar information in \(r\) becomes \(q/r^2\), since the stopped exponential survival score has expected information \(\mathbb E[\min(T,t)]/r=q/r^2\). Dividing the coarsened scalar block \(t^2e^{-x}/q\) by this value yields \(x^2 e^{-x}/q^2=[x/(2\sinh(x/2))]^2\). The common categorical block and coordinate-Jacobian factors cancel from the determinant ratio. Substitution of the asymptotic optimum gives \(\eta(x_k)\sim(\log k)^2/k\).

## Verification

A standalone Python checker, `check.py`, independently forms the category-probability Jacobian and the multinomial Fisher matrix by centered differences for randomly selected positive rate vectors and compares its determinant with the analytic formula. It also checks root equations, strict optimality against nearby designs, rate-composition invariance, the monotonic species-number trend, the asymptotic expansion at large \(k\), and the information-loss formula. These numerical tests are diagnostics; the universal conclusions are proved above.

For example, \(x_3=2.26281012919696\ldots\), \(x_{10}=3.13805785104799\ldots\), and \(x_{100}=5.09022171193079\ldots\). With a fixed total mean encounter rate \(r\), a three-species study should set \(t\approx2.26281/r\), whereas a ten-species study should set \(t\approx3.13806/r\), under the stated Fisher D criterion.

## Relationship to prior work

Wu and Huang (2014) derive Fisher information and discuss numerical D-optimal choices of inspection intervals under *progressive interval censoring* with exponential competing risks, principally for two causes, and describe a computational extension to more risks. Their general framework and the competing-risks likelihood are prior art. The claimed result here is narrower in observation structure (one terminal species-labelled capture status, no time stamp) but sharper as an all-\(k\) analytic theorem: a unique continuous inspection time, strict cross-species-count monotonicity, logarithmic large-\(k\) law, and a closed information-loss identity. The general matrix framework alone does not state these global conclusions, though closely related general results remain a priority risk.

Distiller and Borchers (2015) analyze single-catch ecological trapping with capture-time information and spatially explicit likelihood, rather than the one-terminal-category experiment or its closed-form all-species inspection duration. Zhou et al. (2026) study general discrete-time survival models with competing risks and principally optimize treatment allocation, numbers of predetermined inspection intervals, and cost-normalized criteria. Their multinomial formulation is shared background, not claimed new. The public mathematical finding titled *A two-visit occupancy experiment breaks equal-effort optimality* studies a different two-visit occupancy/detectability split with an unobserved occupancy state rather than a single species-labelled first-capture competition experiment.

## Limitations

The locally D-optimal time requires a nominal total rate \(r\); uncertainty in this rate can motivate Bayesian or maximin designs that are not treated here. Species encounter intensities are assumed constant and independent, a strong approximation for many trapping deployments. There is no monetary penalty for longer trapping duration and no time cap. The exact Fisher determinant concerns repeatable stations and large-sample information, not realized finite-sample error. No claim is made for timestamped experiments, per-species c-optimality, or full spatial capture-recapture models. The originality comparison does not amount to exhaustive historical certification; interval-censored reliability and competing-risks optimal-design literature provide a residual risk of equivalent formulations.

## References

- Wu, S.-J., and Huang, S.-R., *Planning Progressive Type-I Interval Censoring Life Tests With Competing Risks*, IEEE Transactions on Reliability 63(2), 511–522 (2014). DOI: 10.1109/TR.2014.2313708. First electronically published 2014-04-03.
- Distiller, G., and Borchers, D. L., *A spatially explicit capture–recapture estimator for single-catch traps*, Ecology and Evolution 5(21), 5075–5087 (2015). DOI: 10.1002/ece3.1748. First published 2015-10-19.
- Zhou, X.-D., Wang, Y.-J., Yue, R.-X., and Wong, W. K., *Optimal designs for discrete-time survival models with competing risks*, Lifetime Data Analysis 32, article 17 (2026). DOI: 10.1007/s10985-026-09695-0. First published 2026-02-28.
