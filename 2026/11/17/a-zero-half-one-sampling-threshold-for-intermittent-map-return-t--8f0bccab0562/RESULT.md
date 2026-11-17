# A zero–half–one sampling threshold for intermittent-map return times

## Finding
For the explicit two-branch intermittent map of Li, independent uniformly sampled initial points on its return base give an unexpected three-way consistency transition for first-return means. With \(N_\delta=\lfloor\exp(c/\delta)\rfloor\) independent returns and the *exact* true mean \(\mu_\delta\), the normalized sample average converges in probability to
\[
\frac{1}{N_\delta\mu_\delta}\sum_{j=1}^{N_\delta}\tau_{\delta,j}
\xrightarrow{\mathbb P}
\begin{cases}0,&0<c<1,\\[2pt]1/2,&c=1,\\[2pt]1,&c>1.\end{cases}
\]
The critical value is *exactly one half*, not a nondegenerate random variable. Thus even though every mean is finite at fixed \(\delta>0\), exponentially many independent first-return observations are needed to estimate it accurately as intermittency becomes extreme.

## Assumptions and scope
For each \(0<\delta<1\), let \(a_\delta=\exp(1-2^\delta)\), \(Y_\delta=[a_\delta,1]\), and define the piecewise interval map
\[
T_\delta(x)=\begin{cases}
0,&x=0,\\
\exp\!\left(1-\big[(1-\log x)^{1/\delta}-1\big]^\delta\right),&0<x<a_\delta,\\
(x-a_\delta)/(1-a_\delta),&a_\delta\le x\le1.
\end{cases}
\]
These are precisely the branches in Proposition 4.22 of the cited source. Draw \(N_\delta=\lfloor\exp(c/\delta)\rfloor\) independent initial conditions from normalized Lebesgue measure on \(Y_\delta\). Let \(\tau_{\delta,j}=\min\{n\ge1:T_\delta^n(x_j)\in Y_\delta\}\), where exceptional boundary orbits of zero sampling measure may be ignored. Define \(\mu_\delta=\mathbb E\tau_{\delta,1}\). The limits concern independent restarts, *not* serial returns from one orbit, and only fixed \(c>0\).

## Proof
**Exact induced-return distribution.** The source's inverse-branch calculation uses \(x_m=\exp(1-(m+1)^\delta)\). After the first right-branch step, the image of a uniform point in \(Y_\delta\) is uniform on \([0,1]\). It needs more than \(n\) steps to return exactly when that image lies below \(x_n\), up to zero-measure endpoints. Therefore, for every integer \(n\ge0\),
\[
\mathbb P(\tau_{\delta,1}>n)=\exp\bigl(1-(n+1)^\delta\bigr).
\]
Write \(q=1/\delta\), let \(E\) have the unit exponential law, and set \(Z=1+E\), with density \(e^{1-z}\) for \(z\ge1\). The same exact integer survival function proves the distributional coupling
\[
\tau_{\delta,1}\ \overset{d}=\ \lfloor Z^q\rfloor.
\]
In particular, \(0\le Z^q-\tau_{\delta,1}<1\), and
\[
\mu_q^*:=\mathbb EZ^q=e\int_1^\infty z^qe^{-z}\,dz=e\,\Gamma(q+1,1),\qquad 0\le\mu_q^*-\mu_\delta<1.
\]
Here the second argument of \(\Gamma\) is the upper incomplete-gamma cutoff. As \(q\to\infty\), \(\mu_q^*\sim e\Gamma(q+1)\), which diverges. Consequently replacing all integer returns by independent \(Z_j^q\) changes the normalized sample average by at most \(1/\mu_\delta=o(1)\), uniformly in sample size.

**The tilted mass is a concentrated gamma law.** For \(b>1\), let \(F_q(b)=\mathbb E[Z^q\mathbf1_{Z\le b}]/\mu_q^*\). This equals the probability that a \(\Gamma(q+1,1)\) random variable lies in \([1,b]\), conditional on being at least \(1\). It follows from gamma concentration and its central limit theorem that for any fixed \(a<1<b\),
\[
F_q(aq)\to0,\quad F_q(bq)\to1,\quad
F_q(q\pm q^{1/4})\to\tfrac12,\quad
F_q(q+q^{1/4})-F_q(q-q^{1/4})\to0.
\]
The last assertions use that the gamma standard deviation is asymptotic to \(\sqrt q\).

**Subcritical samples.** Fix \(0<c<1\) and choose \(c<b<1\). Put \(N_q=\lfloor e^{cq}\rfloor\). The chance that any of the \(N_q\) samples exceeds the cutoff \(Z>bq\) is at most \(N_qe^{1-bq}\to0\). The expected normalized contribution from samples below the cutoff is \(F_q(bq)\to0\), hence Markov's inequality proves convergence to zero in probability.

**Supercritical samples.** Fix \(c>1\), and choose \(1<b<c\). The contribution from \(Z>bq\) has normalized expectation \(1-F_q(bq)\to0\), hence vanishes in probability. For the independent truncated weights \(U_j=Z_j^q\mathbf1_{Z_j\le bq}\), positivity gives \(U_j^2\le (bq)^qU_j\), whence
\[
\operatorname{Var}\!\left(\frac{\sum_{j=1}^{N_q}U_j}{N_q\mu_q^*}\right)
\le\frac{(bq)^q}{N_q\mu_q^*}
=\exp\big(q[\log b+1-c]+O(\log q)\big)\to0.
\]
The exponent is negative because \(\log b<b-1<c-1\). The truncated expectation tends to one, proving convergence to one in probability.

**The critical half.** Set \(N_q=\lfloor e^q\rfloor\), \(h_q=q^{1/4}\), and split the observations by \(Z\le q-h_q\), \(q-h_q<Z\le q+h_q\), and \(Z>q+h_q\). The gamma central limit theorem shows that the first group's normalized expectation tends to \(1/2\), while the middle group's tends to zero and therefore vanishes by Markov's inequality. For the first group, the preceding truncated variance estimate is
\[
\frac{(q-h_q)^q}{N_q\mu_q^*}
=\exp(-q^{1/4}+O(\log q))\to0.
\]
The probability of any observation in the third group is bounded by \(N_qe^{1-q-h_q}\to0\). Therefore the normalized complete sample average converges in probability to exactly \(1/2\). Passing back to integer return times using the uniform unit-error coupling completes all three regimes.

## Verification
The attached `verify.py` independently checks the exact tail-to-exponential coupling, numerical gamma mass partitions around the critical saddle, the exact mean up to unit rounding, and the signs of the variance and extreme-event exponents. It does not substitute for the concentration and variance proof above. The proof uses no sample-based extrapolation to infinite size.

## Relationship to prior work
Li, *Macroscopic return-time spectra and Hausdorff dimension transitions* (arXiv:2611.06416v1, first posted 2026-11-04), constructs the actual two-branch intermittent interval map, proves its first-return branch formulas, and studies Hausdorff dimensions of macroscopic return-time *sets along trajectories*. The present result instead analyzes statistical consistency from independently restarted one-point first returns when \(\delta\downarrow0\), with an exact critical sampling proportion. The proof uses familiar gamma concentration, exponentials and truncation inequalities; these standard ingredients are not claimed as new. The old general literature on thin-tail near-maxima and small-shape Weibull asymptotics is relevant context but does not by itself establish this particular three-way triangular-array law for Li's intermittent map.

## Limitations
Independent uniform initial seeds are essential: no assertion is made about successive return times on a single orbit or stationary mixing. The result is asymptotic for fixed sampling-exponent \(c\); it does not give a refined finite-window law when \(c\) approaches one as a function of \(\delta\). The exact lower-level return distribution was derived from Li's published inverse-branch geometry, not independently discovered. Historical priority of an unindexed general triangular-array half-limit remains a residual risk. Independent mathematical audit has not been performed.

## References
- Jinjun Li, *Macroscopic return-time spectra and Hausdorff dimension transitions*, arXiv:2611.06416v1 (2026-11-04), especially Proposition 4.22, its proof, and Corollary 4.23. https://arxiv.org/abs/2611.06416
- Anthony G. Pakes, *The number and sum of near-maxima for thin-tailed populations*, Advances in Applied Probability **32** (2000), 1100–1116, DOI 10.1017/S000186780001048X. Cited as nearby extreme-value context, not as a claim of the same theorem.
