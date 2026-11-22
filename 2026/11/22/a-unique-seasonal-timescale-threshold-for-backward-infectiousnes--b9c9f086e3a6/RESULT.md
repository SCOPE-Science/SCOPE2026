# A unique seasonal timescale threshold for backward infectiousness despite negative invasion growth

## Finding
Fix distinct positive removal hazards \(a\ne b\), a positive transmission rate \(\lambda\), and a half-season length \(h>0\). Set \(\gamma_h(t)=a\) for \(t\bmod 2h\in[0,h)\) and \(\gamma_h(t)=b\) for \(t\bmod 2h\in[h,2h)\). Define the calendar-time, **backward-looking infectious-survival kernel** and its mass by
\[
K_h(t,z)=\exp\!\left[-\int_{t-z}^{t}\gamma_h(s)\,ds\right],\qquad
A_h(t)=\int_0^\infty K_h(t,z)\,dz,\qquad
\mathcal J_h(t)=\lambda A_h(t),\quad z\ge0.
\]
These are respectively the probability that an infection acquired \(z\) time units before \(t\) is still infectious at \(t\), the integral of that probability over past ages, and the instantaneous *unnormalized backward-kernel mass*. Here \(\mathcal J_h\) is **not** asserted to be a universally valid epidemic invasion number or the expected future offspring of a newly infected case. Under a time-dependent kernel it agrees with the time-integral of the instantaneous renewal transmission kernel, not with a stationary duration substitution.

**Theorem (sharp switching-time crossover).** For each \(h>0\), \(A_h\) is the unique positive periodic solution of \(A'_h(t)=1-\gamma_h(t)A_h(t)\) (away from switching times), and
\[
\boxed{\quad
\frac1{2h}\int_0^{2h}A_h(t)\,dt
=\frac12\left(\frac1a+\frac1b\right)
-\frac{(a^{-1}-b^{-1})^2}{2h}
\frac{(1-e^{-ah})(1-e^{-bh})}{1-e^{-(a+b)h}}.
\quad}
\]
The average is **strictly increasing** in \(h\) for all \(a\ne b\), with exact endpoints and sharp expansions
\[
\begin{aligned}
\overline A_h
&=\frac2{a+b}+\frac{(a-b)^2}{24(a+b)}h^2+O(h^4),&h&\downarrow0,\\
\overline A_h
&=\frac12\left(\frac1a+\frac1b\right)
-\frac{(a^{-1}-b^{-1})^2}{2h}
+O\!\left(\frac{e^{-\min(a,b)h}}h\right),&h&\to\infty.
\end{aligned}
\]
Therefore if
\[
\boxed{\quad \frac{2ab}{a+b}<\lambda<\frac{a+b}{2},\quad}
\]
there is exactly one \(h_*>0\) at which \(\overline{\mathcal J_h}=1\). Specifically, \(\overline{\mathcal J_h}<1\) for \(h<h_*\) and \(\overline{\mathcal J_h}>1\) for \(h>h_*\); the strict interval is nonempty precisely because \(a\ne b\). Yet the associated infection linearization
\[
I'(t)=[\lambda-\gamma_h(t)]I(t)
\]
has the **same negative Floquet exponent** \(\lambda-(a+b)/2<0\) for every \(h>0\), independently of the crossing. Thus a threshold rule based on the *period-average of this backward kernel mass* can falsely report persistence, even though the exact infection linearization decays exponentially.

If \(a<b\), within the \(a\)-season one has \(A_h(t)<1/a\) and within the \(b\)-season one has \(A_h(t)>1/b\), with strict inequalities even at the switching endpoints; hence the time-dependent kernel mass lags the two instantaneous frozen-hazard values in opposite directions. For \(a=b\), \(A_h\equiv1/a\), and no dependence on \(h\) remains.

## Assumptions and scope
The disease-free susceptible fraction is fixed at one and mixing is homogeneous. The linearized susceptible-infectious transmission intensity per infected host is \(\lambda>0\); no exposed class is present. Removal is memoryless *conditional on calendar time* but its rate switches deterministically between strictly positive \(a,b\). Individuals infected at any past time have experienced the same external calendar hazard thereafter. All quantities are periodic steady-state integrals over the indefinitely extended calendar, not integrals restricted to a finite outbreak starting at time zero. The mathematical conclusions are exact for positive real rates and \(h\); the positive-crossing assertion additionally requires the strict interval stated above. The renewal definition of \(\mathcal J_h\) is fixed explicitly and is not interchangeable with the forward-looking case reproduction number.

## Proof
**1. Periodic renewal identity.** Positivity of \(\min(a,b)\) makes \(A_h(t)\) finite, continuous and \(2h\)-periodic. Differentiating the moving-boundary survival integral, or using variation of constants, yields \(A'_h=1-\gamma_h A_h\) away from switches. The Poincaré map for this linear equation has contraction factor \(e^{-(a+b)h}\), giving a unique periodic solution. Put \(u=e^{-ah}\), \(v=e^{-bh}\), \(x_0=A_h(0)\), and \(x_1=A_h(h)\). Solving the two exact phase flows gives
\[
 x_1=\frac1a+\left(x_0-\frac1a\right)u,\qquad
 x_0=\frac1b+\left(x_1-\frac1b\right)v,
\]
and hence
\[
x_0-\frac1a=\left(\frac1b-\frac1a\right)\frac{1-v}{1-uv},\qquad
x_1-\frac1b=\left(\frac1a-\frac1b\right)\frac{1-u}{1-uv}.
\]
Integration of the two phase solutions gives
\[
2h\overline A_h=h\left(\frac1a+\frac1b\right)
+\frac{(x_0-1/a)(1-u)}a+\frac{(x_1-1/b)(1-v)}b
=h\left(\frac1a+\frac1b\right)
-(1/a-1/b)^2\frac{(1-u)(1-v)}{1-uv}.
\]
The boundary identities and scalar phase flows also prove the stated pointwise inequalities.

**2. Strict monotonicity.** Set
\[
Q(h)=\frac{(1-e^{-ah})(1-e^{-bh})}{1-e^{-(a+b)h}}
=\frac{2\sinh(ah/2)\sinh(bh/2)}{\sinh((a+b)h/2)}.
\]
It suffices to show \(Q(h)/h\) is strictly decreasing. Write \(x=ah/2\), \(y=bh/2\), \(H(z)=z\coth z-1\). Direct differentiation yields
\[
h\frac d{dh}\log\frac{Q(h)}h=H(x)+H(y)-H(x+y).
\]
For \(z>0\), \(H(z)/z=\coth z-1/z\) has derivative
\[
\frac{d}{dz}\left(\frac{H(z)}z\right)=\frac1{z^2}-\frac1{\sinh^2z}>0
\]
because \(\sinh z>z\). It follows that \(H(x)<xH(x+y)/(x+y)\) and \(H(y)<yH(x+y)/(x+y)\), hence \(H(x)+H(y)<H(x+y)\). Therefore \((Q(h)/h)'<0\), so \(\overline A_h\) increases strictly when \(a\ne b\).

**3. Limits and crossover.** Hyperbolic Taylor expansion gives \(Q(h)/h=ab/(a+b)-a^2b^2h^2/[12(a+b)]+O(h^4)\); substituting proves the small-season expansion. For \(h\to\infty\), \(Q(h)=1+O(e^{-\min(a,b)h})\). The limiting averages are \(2/(a+b)\) and \((a^{-1}+b^{-1})/2\). The strict monotonic continuous map \(\lambda\overline A_h\) crosses one exactly once iff \(\lambda\) lies strictly between their reciprocal values, namely \(2ab/(a+b)\) and \((a+b)/2\). The intermediate-value theorem proves uniqueness and the strict signs.

**4. Exact invasion verdict.** Over each period, \(I(2h)/I(0)=\exp[2h\lambda-h(a+b)]\). Its per-unit-time logarithmic growth exponent is \(\lambda-(a+b)/2\), strictly negative under the crossover hypotheses. This calculation distinguishes the periodic invasion criterion from averaging an instantaneous renewal kernel mass; it does not contradict a correctly defined nonautonomous next-generation operator.

## Verification
The supplied `checker.py` can be executed using Python with SymPy, NumPy, SciPy and mpmath. It checks the periodic-boundary identities exactly; separately solves the two linear ODE phases and compares numerical quadrature to the closed formula; samples monotonicity for several rate pairs; computes the example crossing; and checks the second-order limit with high precision. Numerical tests support, but do **not** replace, the universal hyperbolic inequality proved above. For \(a=1\), \(b=4\), \(\lambda=2\), the unique crossing is
\[
h_*=1.91906667452146\ldots,
\]
while the Floquet exponent is exactly \(-1/2\). At \(h=1\) the average kernel mass is approximately \(0.8985767662\) and at \(h=2\) it is approximately \(1.0068835911\), despite unchanged negative invasion growth.

## Relationship to prior work
Goldwasser, Tibshirani and Bilinski (2026) prove equivalence of instantaneous and mechanistic reproduction numbers under homogeneous mixing when infectious-period distributions are stationary (arXiv:2606.15397, §§2–3). They explicitly hold biological waiting-time rates constant while allowing time-varying transmission; their stationarity condition does not cover the calendar-dependent removal hazard here. The present claim is not that their theorem fails, but that a natural exact backward-age kernel acquires a switching-period-dependent mass when their stationary waiting-time hypothesis is removed. Pakkanen and coauthors (2023, *Journal of Mathematical Biology*) furnish a general time-varying branching/renewal framework that accommodates calendar-dependent kernels; its general representation is acknowledged, not claimed new. Greenhalgh and Dumas (2023) analyze the **forward** mean residual infectious waiting time in a periodic-hazard SIS model. Their mean residual life is based on survival *after* calendar time, whereas the kernel here integrates survival *from all earlier acquisition times to the present*; the two satisfy different differential identities and must not be conflated. Earlier periodic-demography epidemic theory treats the averaged scalar invasion exponent, already classical; the exact negative Floquet exponent above is likewise not claimed new. What is assessed here is the **strict global switching-period monotonicity, unique mean-kernel crossing, and their sharp separation from the unchanged Floquet stability criterion** for the explicit two-rate calendar. More general historical work on periodic survival and renewal equations may contain equivalent formulations; priority is not independently established.

## Limitations
The theorem does not show that a standard estimated \(R_t\) will cross one in observed data: the index is explicitly the unnormalized nonstationary backward kernel mass \(\mathcal J_h\). It is not a case reproduction number, nor a spectral next-generation threshold, nor a stationary substitution \(\lambda/\gamma_h(t)\). Biological and behavior rates are idealized, the infinite-past stationary kernel requires a fully periodic environment, and susceptible depletion, changing transmission, latency, stochastic extinction and heterogeneous mixing are excluded. The threshold crossing is about **an average of an index**, not the exact epidemic invasion threshold. Scientific novelty remains conditional on incomplete historical literature coverage; independent audit has not been conducted.

## References
- J. Goldwasser, R. J. Tibshirani, A. Bilinski (2026), *On the Equivalence of Instantaneous and Mechanistic Reproduction Numbers*, arXiv:2606.15397v1 (first public June 13, 2026), https://arxiv.org/abs/2606.15397 . Relevant material: §§2–3, especially stationary waiting times and equation defining instantaneous kernel mass.
- M. S. Pakkanen et al. (2023), *Unifying incidence and prevalence under a time-varying general branching process*, *Journal of Mathematical Biology* 87:35, DOI 10.1007/s00285-023-01958-w, https://pmc.ncbi.nlm.nih.gov/articles/PMC10393927/ . Relevant material: §§1–2, time-dependent reproduction kernels and incidence equations.
- C. Ward, G. D. Brown, J. J. Oleson (2023), *Incorporating infectious duration-dependent transmission into Bayesian epidemic models*, *Biometrical Journal* 65(3), DOI 10.1002/bimj.202100401, https://onlinelibrary.wiley.com/doi/full/10.1002/bimj.202100401 . Relevant material: §2.3, duration-dependent reproductive-number modeling.
- S. Greenhalgh and A. Dumas (2023), *A generalized ODE susceptible-infectious-susceptible compartmental model with potentially periodic behavior*, *Infectious Disease Modelling* 8(4), DOI 10.1016/j.idm.2023.11.007, https://pmc.ncbi.nlm.nih.gov/articles/PMC10709614/ . Relevant material: §2.2, the periodic **forward** mean residual lifetime, a different integral orientation.
- *The basic reproduction number in epidemic models with periodic demographics*, *Journal of Biological Dynamics* (earlier periodic-invasion literature), DOI 10.1080/17513750802304893. A complete source comparison was not possible; results about general periodic epidemic thresholds are not claimed new here.
