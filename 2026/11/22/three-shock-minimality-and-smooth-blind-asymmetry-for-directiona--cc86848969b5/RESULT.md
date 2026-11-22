# Three-shock minimality and smooth blind asymmetry for directional tail Kendall concordance

## Finding

The ordered pair of directional tail Kendall coefficients need not identify exchange symmetry, even for positively tail-dependent bivariate max-stable laws. Within the class of strictly positive, normalized, finite-factor max-linear laws, **three factors are necessary and sufficient** for this failure: one or two factors satisfy the equivalence
\[
\tau_{X\to Y}=\tau_{Y\to X}\quad\Longleftrightarrow\quad (X,Y)\stackrel d=(Y,X),
\]
whereas three factors admit a nonexchangeable law with both coefficients equal to \(16/25\) and tail-dependence coefficient \(7/10\).

Moreover, there exist nonexchangeable, positively tail-dependent bivariate max-stable laws with **strictly positive, real-analytic spectral densities** for which the two directional coefficients are exactly equal. Thus the finite-factor blind spot persists after spectral smoothing and is not solely caused by atoms or singular finite-factor support.

## Assumptions and scope

Let \(G_1,\ldots,G_m\) be independent unit Fréchet random variables: \(\Pr(G_i\le x)=e^{-1/x}\) for \(x>0\). Fix \(m\ge1\) and strictly positive vectors \(p,q\in(0,1]^m\) with \(\sum_i p_i=\sum_i q_i=1\), and put
\[
 X=\max_i p_iG_i,\qquad Y=\max_i q_iG_i,\qquad r_i=q_i/p_i.
\]
The two margins are unit Fréchet, and \(\chi=\sum_i\min(p_i,q_i)>0\). Each directional tail Kendall coefficient is the limit of the Kendall sign expectation for two independent copies, conditioning *both* copies to exceed the same high quantile in the first named coordinate, as defined by Deidda, Engelke and De Michele (2023). These are population limiting coefficients, not empirical estimates or a claim about significance-test power.

For the smooth extension let \(Z>0\) be a random variable with \(\mathbb EZ=1\); the bivariate max-stable exponent is
\[
 \ell(s,u)=\mathbb E\max(s,uZ),\quad s,u\ge0,
\]
meaning \(\Pr(X\le x,Y\le y)=\exp\{-\ell(1/x,1/y)\}\) for positive \(x,y\). Exchangeability is equivalent to \(\ell(s,u)=\ell(u,s)\) for all arguments.

## Proof

**1. Exact finite-factor formula.** Since \(\Pr(p_iG_i>x)=p_i/x+O(x^{-2})\), simultaneous exceedances by two distinct factors are \(O(x^{-2})\). Given \(X>x\), the scaled pair converges to \((P,Pr_I)\), where \(P\) is standard Pareto, independent of \(I\), and \(\Pr(I=i)=p_i\). The corresponding \(Y\)-exceedance representation uses probabilities \(q_i\) and slopes \(1/r_i\). Conditional sign limits follow because independent Pareto radial variables have continuous ratios and therefore the limiting pairwise comparison ties have probability zero. For two fixed positive slopes \(a,b\), integrating the ratio of two independent standard Pareto variables gives
\[
 \mathbb E\operatorname{sgn}\{(P-P')(aP-bP')\}
 =\min(a/b,b/a).
\]
Indeed \(\log(P/P')\) has the two-sided Laplace law, so the discordance probability is \((1-\min(a/b,b/a))/2\). Therefore
\[
 \boxed{\tau_{X\to Y}=\sum_{i,j}p_ip_jK_{ij},\quad
 \tau_{Y\to X}=\sum_{i,j}q_iq_jK_{ij},\quad
 K_{ij}=\min(r_i/r_j,r_j/r_i).}
\]
The general extremal-function expression underlying these formulas is due to the cited paper; the finite-atomic derivation here is included because its published theorem assumes a spectral density.

**2. One/two-factor rigidity.** With one factor \(p=q=(1)\), both coordinates coincide. For two factors write \(p=(a,1-a)\) and \(q=(b,1-b)\). If \(a=b\), again the coordinates coincide. By exchanging coordinates if needed suppose \(a>b\), and put \(\delta=a-b\). The formula above simplifies exactly to
\[
 \tau_{X\to Y}=1-2\delta\frac{1-a}{1-b},\qquad
 \tau_{Y\to X}=1-2\delta\frac ba.
\]
They coincide precisely when \(a(1-a)=b(1-b)\). Since \(a\ne b\), this says \(a+b=1\), i.e. \(q=(1-a,a)\) is a permutation of \(p=(a,1-a)\). Relabeling iid factors exchanges the coordinates without changing the law. The converse (exchangeability implies coefficient equality) follows directly from the definitions.

**3. A minimal exact counterexample.** Take
\[
 p=(2/5,3/10,3/10),\qquad q=(1/5,1/5,3/5),
 \qquad r=(1/2,2/3,2).
\]
The kernel formula gives \(\tau_{X\to Y}=\tau_{Y\to X}=16/25\), and \(\chi=7/10\). But
\[
 \ell(2,3)=\sum_i\max(2p_i,3q_i)=16/5,
 \qquad \ell(3,2)=\sum_i\max(3p_i,2q_i)=33/10.
\]
These values differ by \(1/10\), proving nonexchangeability. Combined with step 2, the factor count three is sharp **within this normalized positive max-linear class**.

**4. Positive-density robustness.** For \(t\in[1/4,7/20]\), set
\[
 p_1(t)=2/3-8t/9,\quad p_2(t)=t,\quad p_3(t)=1/3-t/9,
 \quad r=(1/2,2/3,2),\quad q_i(t)=p_i(t)r_i.
\]
All weights are strictly positive and both vectors sum to one. Direct substitution into the finite-factor formulas gives
\[
 \Delta(t,0):=\tau_{X\to Y}-\tau_{Y\to X}
 =\frac{2t(10t-3)}{81},
 \quad \ell_{t,0}(3,2)-\ell_{t,0}(2,3)=\frac t3.
\]
In particular, \(\Delta(1/4,0)=-1/324\), \(\Delta(7/20,0)=7/1620\), while the exponent asymmetry is uniformly at least \(1/12\).

Let \(I_t\) have probabilities \(p_i(t)\), let \(H\) be an independent standard Gaussian, and for \(\sigma>0\) define
\[
 Z_{t,\sigma}=r_{I_t}\exp(\sigma H-\sigma^2/2).
\]
Then \(\mathbb EZ_{t,\sigma}=1\). Its distribution is a finite mixture of lognormal laws, with a strictly positive real-analytic density on \((0,\infty)\). The exponent \(\ell_{t,\sigma}(s,u)=\mathbb E\max(s,uZ_{t,\sigma})\) defines a unit-Fréchet bivariate max-stable law, for example by a Poisson radial/spectral maximum construction.

For this model the forward coefficient is \(\mathbb E K(Z,Z')\), and the reverse coefficient is \(\mathbb E[ZZ'K(Z,Z')]\), where \(Z,Z'\) are independent with the above law and \(K(z,z')=\min(z/z',z'/z)\). The reverse formula uses the \(Z\)-size-biased spectral law. Since \(K\) is bounded and continuous on the positive quadrant and the lognormal factors converge in \(L^1\) to one as \(\sigma\downarrow0\), both coefficients are jointly continuous in \((t,\sigma)\) at \(\sigma=0\) on the indicated compact parameter interval (the second expectation follows by uniform integrability of the bounded-\(\sigma\) lognormal products). Therefore the opposite endpoint signs of \(\Delta\) persist for every sufficiently small positive \(\sigma\). By the intermediate value theorem, for each such \(\sigma\) there is a \(t_\sigma\in(1/4,7/20)\) with \(\Delta(t_\sigma,\sigma)=0\).

Finally, \(|\max(s,uZ_\sigma)-\max(s,uZ_0)|\le u|Z_\sigma-Z_0|\), so uniform \(L^1\) convergence over the compact weight interval preserves the strictly positive exponent gap. Thus these zero-contrast smooth laws are still nonexchangeable. Their upper tail dependence remains strictly positive because \(Z>0\) almost surely and \(\chi=\mathbb E\min(1,Z)>0\). This establishes the smooth assertion.

## Verification

Run the included standalone `checks.py` with Python 3. It checks the exact three-factor coefficients, tail overlap and nonsymmetric exponent, two endpoint signs, the entire \(t\)-family identities at 101 rational values, and two-factor equality equivalence on a 79-by-79 rational parameter grid. In the recorded execution, **6,652 exact rational assertions passed**. These checks corroborate algebra and boundary conditions; the factor-minimality argument, continuous-limit argument and existence of smooth alternatives are proved mathematically above, not by finite enumeration.

## Relationship to prior work

Deidda, Engelke and De Michele introduced directional tail Kendall concordances and proved the spectral extremal-function formula (their Theorem 4, Appendix B). Their formula and the implication from exchangeability to equality are prior results, not asserted here as new. Their inspected main text and appendix discuss Hüsler–Reiss and extremal Dirichlet illustrations, not a minimal finite-factor obstruction or a smooth nonexchangeable pair of exactly equal directional coefficients. The factor-exponent representation and Poisson spectral construction are standard max-stable methods. The assessed new claim is the sharp one/two/three-factor distinction, explicit rational asymmetry witness, and spectrally smooth persistence.

## Limitations

Minimality is asserted **only for normalized positive finite-factor max-linear pairs**, not for all max-stable copulas or all positive spectral laws. Smooth nonexchangeable zero-contrast examples are established by continuity and an intermediate value argument; no closed form for the corresponding positive smoothing parameter and tuned weight is claimed. The result does not establish detection power, error rates or finite-sample calibration. Mathematical priority remains subject to external independent assessment; a literature search cannot certify uniqueness.

## References

1. C. Deidda, S. Engelke and C. De Michele, *Asymmetric Dependence in Hydrological Extremes*, arXiv:2301.08764 (first posted January 20, 2023), *Water Resources Research* 59 (2023), DOI: 10.1029/2023WR034512. https://arxiv.org/abs/2301.08764 ; https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023WR034512 . In particular Sections 2.1–2.2 and Appendix B, Theorem 4.
2. J.-F. Mai, *Extreme-value copulas associated with the expected scaled maximum of independent random variables*, *Journal of Multivariate Analysis* (2018), DOI: 10.1016/j.jmva.2018.02.005. Background on max-stable spectral expectations, not a claim of the present minimality result.
