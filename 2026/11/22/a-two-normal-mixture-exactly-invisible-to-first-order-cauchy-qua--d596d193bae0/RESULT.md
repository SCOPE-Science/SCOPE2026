# A two-normal mixture exactly invisible to first-order Cauchy quantile-ratio calibration

## Finding

Fix the four population quantile levels used in the Cauchy goodness-of-fit construction of Pekgör (2023):
\[p=0.02217468,\qquad (p,1/4,3/4,1-p).\]
For a sample of size \(n\), let \(\widehat q_t\) be any sample-quantile definition satisfying the standard fixed-interior-quantile central limit theorem, and set
\[\widehat R_n=\frac{\widehat q_{3/4}-\widehat q_{1/4}}{\widehat q_{1-p}-\widehat q_p}.\]
Under every Cauchy location-scale distribution, its population target is \(r_C=\tan(\pi p)=0.0697767248877807\ldots\). **There exists a non-Cauchy mixture of only two centered Gaussian distributions**
\[F_{w,s}(x)=(1-w)\Phi(x)+w\Phi(x/s),\qquad 0.08<w<0.20,\quad s>1,\]
for which both the population ratio and its asymptotic variance equal those under Cauchy sampling. More precisely, for this mixture and for every Cauchy location-scale distribution,
\[\sqrt n\,(\widehat R_n-r_C)\ \xRightarrow{\ }\ N(0,V_C),\]
with the **same** strictly positive constant
\[ V_C=\frac{\pi^2}{4}\left[r_C^2+2p(1-2p)(1+r_C^2)^2-4pr_C(1+r_C^2)\right]
=0.1022632982267939\ldots.\]
Accordingly, the usual two-sided test rejecting when
\[\left|\sqrt n(\widehat R_n-r_C)\right|>\sqrt{V_C}\,z_{1-\alpha/2}\]
has rejection probability tending to \(\alpha\), rather than to one, under the indicated fixed non-Cauchy alternative, for every \(0<\alpha<1\). The same conclusion holds for deterministic two-sided null critical endpoints whose standardized limits are the standard normal \(\alpha/2\) and \(1-\alpha/2\) quantiles.

The mixture has a positive, real-analytic, even and strictly unimodal density, has a finite moment-generating function at every real argument, and is therefore substantially different from every Cauchy law. Within *centered Gaussian scale mixtures with at most two distinct scales*, two components are minimal for this simultaneous matching, since a single Gaussian has population index \(0.335437912974\ldots\ne r_C\). An approximate solution is \(w\approx0.09740138591345\), \(s\approx14.48443702536\); the existence theorem does not depend on treating these decimals as exact.

## Assumptions and scope

The observations are independent and identically distributed from either a Cauchy location-scale law or the displayed two-component centered normal scale mixture. The fixed probability \(p\) denotes exactly the eight-decimal value specified above. Under the mixture, let \(a>0\) and \(b>a\) solve \(F_{w,s}(a)=3/4\) and \(F_{w,s}(b)=1-p\), and let \(u=f_{w,s}(a)>0\), \(v=f_{w,s}(b)>0\). The population quantile ratio is \(r=a/b\). The theorem concerns the scalar four-quantile ratio and its Gaussian/null-quantile asymptotic calibration, not other Cauchy tests, arbitrary rejection regions, or finite-sample indistinguishability of entire samples.

## Proof

**1. Quantile fluctuation law.** For any symmetric distribution with positive continuous density at its four relevant quantiles, the joint sample-quantile central limit theorem gives a Gaussian vector. If \(I_n=\widehat q_{3/4}-\widehat q_{1/4}\) and \(J_n=\widehat q_{1-p}-\widehat q_p\), their centered \(\sqrt n\)-scaled limits have variance and covariance
\[\operatorname{Var}(I)=\frac{1}{4u^2},\qquad
\operatorname{Var}(J)=\frac{2p(1-2p)}{v^2},\qquad
\operatorname{Cov}(I,J)=\frac{p}{uv}.\]
Indeed, for nested intervals of uniform probability lengths \(1/2\) and \(1-2p\), the corresponding Brownian-bridge increment covariance is \((1/2)(2p)=p\). Applying the ratio delta method at \((2a,2b)\) yields
\[V(w,s)=\frac{1}{4b^2}\left[\frac{1}{4u^2}+\frac{2p(1-2p)}{v^2}\left(\frac ab\right)^2-\frac{2p}{uv}\left(\frac ab\right)\right].\tag{1}\]
For a standard Cauchy law, \(a=1\), \(b=\cot(\pi p)\), \(u=1/(2\pi)\), and \(v=1/[\pi(1+b^2)]\), which gives the stated \(r_C\) and \(V_C\). Affine invariance covers every Cauchy location and positive scale.

**2. A one-dimensional exact matching locus.** Let \(a(w,s)=F_{w,s}^{-1}(3/4)\), \(b(w,s)=F_{w,s}^{-1}(1-p)\), and \(r(w,s)=a(w,s)/b(w,s)\). For each fixed \(w\in[0.08,0.20]\), \(r(w,1)=\Phi^{-1}(3/4)/\Phi^{-1}(1-p)>r_C\). Implicit differentiation of the mixture quantile equation yields, for \(q>0\),
\[\frac{\partial}{\partial s}\log q(w,s)=
\frac{w}{s^2\left[(1-w)\exp\{-\frac{q(w,s)^2}{2}(1-s^{-2})\}+w/s\right]}.\tag{2}\]
For \(s>1\), the right side is strictly increasing in \(q\). As \(b>a\), \(r(w,s)\) is strictly decreasing in \(s\). As \(s\to\infty\), \(a(w,s)\) stays bounded since \(w<1/2\), while \(b(w,s)\to\infty\) since \(w>2p\). Thus for every such \(w\) there is exactly one \(s(w)>1\) with \(r(w,s(w))=r_C\). Formula (2) and positive mixture densities make \(s(w)\) continuous.

**3. A rigorously certified variance crossing.** The accompanying `certify.py` evaluates Gaussian distribution functions and densities using enclosing exact rational series and normal-tail inequalities, and brackets the unique ratio roots and their variances without floating-point comparisons. It proves
\[s(0.08)\in(17.9,18.0),\qquad
0.1915680<V(0.08,s(0.08))<0.2001835,\]
\[s(0.20)\in(10.0,10.1),\qquad
0.0244888<V(0.20,s(0.20))<0.0277288,\]
while \(0.1022<V_C<0.1024\). The rational computations also strictly bracket \(r_C\) between the endpoint ratios at each displayed \(s\) interval. Therefore the continuous function \(w\mapsto V(w,s(w))-V_C\) changes sign. The intermediate value theorem gives a \(w_*\in(0.08,0.20)\) with exact matching of *both* \(r\) and \(V\), and \(s_*=s(w_*)\).

**4. Test consequence and structure.** The same scalar normal weak limit under the Cauchy null and mixture alternative, combined with continuity of the limiting normal distribution at the two Gaussian critical values, gives asymptotic rejection probability \(\alpha\) under either distribution. For \(x>0\), differentiating the mixture density gives
\[ f'_{w,s}(x)=-x\left[(1-w)\varphi(x)+\frac{w}{s^3}\varphi(x/s)\right]<0,\]
so the mixture is strictly unimodal, positive and real analytic. Gaussian mixtures have moment-generating function \((1-w)e^{t^2/2}+we^{s^2t^2/2}\), finite for every real \(t\), unlike a Cauchy law. One Gaussian cannot match even the population ratio, proving two-component minimality in the specified Gaussian scale-mixture class.

## Verification

Run `python3 certify.py` (Python standard library only). It constructs rational bounds for \(\pi\) by Machin's arctangent identity, for \(\Phi\) and \(\varphi\) on the interval \([0,2]\) by alternating series, and beyond \(10\) by elementary Mills-tail bounds. A quantile bisection retains exact rational enclosures, and all root and variance signs are evaluated as strict rational inequalities. The checker exited successfully and printed the crossing certificate. A separate high-precision floating-point root solve gave \(w\approx0.09740138591345\), \(s\approx14.48443702536\), which is **illustrative rather than part of the logical proof**.

## Relationship to prior work

Pekgör (2023) introduced the four-quantile Cauchy goodness-of-fit index, gave its asymptotic null law, and chose the outer quantile levels by separation from a *single* normal law. Its tables already show that nearby index values can have low finite-sample power. The present claim is different: a fixed, strictly unimodal, all-moments-finite **two-normal** mixture matches not only the population index but the *entire first-order scalar null distribution*, forcing nominal asymptotic power for Gaussian-calibrated testing. The parameter construction and rational variance-crossing certificate are essential; qualitative overlap of a few quantiles alone would not give this power conclusion.

Rublík (2001) studies a different fitted-parameter quadratic quantile statistic and sample-size-dependent extreme ranks; Ebner, Eid and Klar (2022) develop a Fourier–Stein characterization test, not the present scalar quantile ratio. Classical quantile central limit theorems and the delta method are used as standard tools, not claimed as new.

## Limitations

The conclusion holds for the specified fixed quantile levels and scalar asymptotically Gaussian calibration. It does not claim that the *joint four-vector* of sample quantiles, the entire sample, or a more informative Cauchy goodness-of-fit procedure has the same distribution under the mixture. It does not establish exact finite-sample size or power for simulation-based highest-density intervals at a fixed \(n\). The decimal solution is approximate, whereas exact existence follows from the certified strict inequalities and continuity. Historical priority beyond inspected sources has not been independently established.

## References

1. Pekgör, A. (first public 14 March 2023), “A Novel Goodness-of-Fit Test for Cauchy Distribution,” *Journal of Mathematics*, Article 9200213. https://doi.org/10.1155/2023/9200213
2. Rublík, F. (2001), “A quantile goodness-of-fit test for Cauchy distribution, based on extreme order statistics,” *Applications of Mathematics* 46, 339–351. https://dml.cz/dmlcz/134472
3. Ebner, B., Eid, L., and Klar, B. (published online 22 December 2022), “Cauchy or not Cauchy? New goodness-of-fit tests for the Cauchy distribution,” *Statistical Papers*. https://doi.org/10.1007/s00362-022-01382-0
4. Serfling, R. J. (1980), *Approximation Theorems of Mathematical Statistics*, Wiley. Standard empirical-quantile asymptotics.
