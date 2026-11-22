# Exact two-sign Brownian-bridge occupation quadrature and a unique symmetric design

## Finding
Let \(B\) be the standard zero-to-zero Brownian bridge on \([0,1]\), and let \(A=\int_0^1\mathbf1_{\{B(u)>0\}}\,du\). Fix distinct deterministic interior times \(0<s<t<1\), observe only \(S_s=\operatorname{sgn}B(s)\) and \(S_t=\operatorname{sgn}B(t)\), and use unrestricted measurable squared-loss decoding. Put
\[
a(x)=\frac{\sqrt{x}+\sqrt{1-x}-1}{2},\qquad
r=\sqrt{\frac{s(1-t)}{t(1-s)}},\qquad c=\frac2\pi\arcsin r.
\]
The unique Bayes estimator, up to null events, and its **exact** unconditional mean-square risk are
\[
\widehat A=\frac12+\frac{a(s)-ca(t)}{1-c^2}S_s+
                   \frac{a(t)-ca(s)}{1-c^2}S_t,
\]
\[
R(s,t)=\frac1{12}-\frac{a(s)^2+a(t)^2-2c\,a(s)a(t)}{1-c^2}.
\]
In the natural reflection-symmetric two-site class \(t=1-s\) with \(0<s<1/2\), there is exactly one minimizing \(s=s_*\), numerically \(s_*=0.3367849667620045\ldots\). Its strictly positive value is characterized without numerical optimization assumptions by the unique zero on \((0,1/2)\) of
\[
\frac{1/\sqrt{s}-1/\sqrt{1-s}}{\sqrt{s}+\sqrt{1-s}-1}
=\frac{2}{\pi(1-s)\sqrt{1-2s}\,[1+(2/\pi)\arcsin(s/(1-s))]}.
\]
The optimal *symmetric-class* explained variance is \(0.0581730290109965\ldots\), or \(69.8076348132\ldots\%\) of \(\operatorname{Var}(A)\). No claim of globally optimal symmetric placement among all asymmetric pairs is made.

As an exactly evaluable benchmark, sampling the trisection points \(s=1/3,t=2/3\) gives three equally probable posterior mean estimates, with values \(\tfrac12-\tfrac32a(1/3)\), \(\tfrac12\), and \(\tfrac12+\tfrac32a(1/3)\). This recovers precisely
\[
\frac{3+\sqrt2-\sqrt3-\sqrt6}{4}=0.0581682530052599\ldots
\]
of the prior variance, i.e. \(69.8019036063\ldots\%\) of it.

## Assumptions and scope
The bridge is a real-valued continuous centered Gaussian process with \(\operatorname{Cov}(B(u),B(v))=\min(u,v)-uv\). Observation times are deterministic and chosen before the path is revealed. There is no observation noise; signs have zero thresholds, and the time-point values themselves are unavailable. Endpoints and coincident observations are not in the two-distinct-interior-time theorem. Squared error is measured for the full positive occupation proportion \(A\), not for the signed integral or the quadratic energy. Decoders may be arbitrary measurable functions of the two bits. Reflection symmetry is imposed **only** for the unique-site optimizer; the exact risk formula holds for every ordered interior pair.

## Proof
1. **Gaussian sign covariance.** For distinct \(u,v\) in \((0,1)\), normalize \(B(u),B(v)\) to variance one. Their correlation is \(\rho(u,v)=\sqrt{\min(u,v)(1-\max(u,v))/[\max(u,v)(1-\min(u,v))]}\). The standard bivariate normal quadrant identity yields \(\mathbb E[S_uS_v]=(2/\pi)\arcsin\rho(u,v)\). Since \(A-1/2=(1/2)\int_0^1S_u\,du\) almost surely, Fubini applies to the bounded integrands and gives
\[
\mathbb E[(A-1/2)S_s]=\frac1\pi\int_0^1\arcsin\rho(u,s)\,du.
\]
2. **Exact single-site integral.** Split the integral at \(u=s\). For the left portion the derivative of \(\arcsin\sqrt{u(1-s)/(s(1-u))}\) is \(\sqrt{1-s}/[2(1-u)\sqrt{u(s-u)}]\). Integration by parts followed by \(u=s\sin^2\theta\) and the elementary identity \(\int_0^{\pi/2}(1-s\sin^2\theta)^{-1}\,d\theta=\pi/[2\sqrt{1-s}]\) gives the left integral \(\pi(s-1+\sqrt{1-s})/2\). By \(u\mapsto1-u\), the right integral is \(\pi(\sqrt{s}-s)/2\). Their sum is \(\pi(\sqrt{s}+\sqrt{1-s}-1)/2\). Hence the cross moment equals \(a(s)\).
3. **Exact prior variance.** Applying the preceding arcsine integral twice,
\[
\operatorname{Var}(A)=\frac1{2\pi}\int_0^1\int_0^1\arcsin\rho(u,v)\,du\,dv
=\frac14\int_0^1[\sqrt v+\sqrt{1-v}-1]\,dv=\frac1{12}.
\]
Thus no external claim about the occupation-time distribution is needed to establish the variance.
4. **Unrestricted decoder.** Global sign reversal \(B\mapsto-B\) sends \((A-1/2,S_s,S_t)\) to its negative. Every function of two binary signs has a unique expansion in \(1,S_s,S_t,S_sS_t\); the conditional mean of the odd functional \(A-1/2\) therefore has no constant or product term. Write it \(\alpha S_s+\beta S_t\). Its two defining orthogonality conditions are \(\alpha+c\beta=a(s)\) and \(c\alpha+\beta=a(t)\). Since \(0<c<1\), the covariance matrix is nonsingular, giving the displayed decoder. Its explained variance is \((a(s)^2+a(t)^2-2ca(s)a(t))/(1-c^2)\). Orthogonal projection in \(L^2\) gives the exact risk and unique Bayes decoder.
5. **Strictly unique symmetric minimizer.** For \(t=1-s\), \(r=s/(1-s)\), \(a(t)=a(s)\), and the explained variance reduces to
\[
V(s)=\frac{2a(s)^2}{1+c(s)},\quad
c(s)=\frac2\pi\arcsin\frac{s}{1-s},\quad 0<s<\frac12.
\]
The function \(a(s)\) is strictly positive and strictly concave, so \(\log a(s)\) is strictly concave. To verify strict convexity of \(\log(1+c(s))\), set \(r=s/(1-s)\), \(g(s)=\arcsin r\), and \(k=2/\pi<1\). Direct differentiation gives
\[
\frac{g''(s)}{g'(s)^2}=\frac{2-r}{\sqrt{1-r^2}}>1,
\qquad (\log(1+kg))''=
\frac{k[(1+kg)g''-k(g')^2]}{(1+kg)^2}>0.
\]
Consequently \(\log V=2\log a-\log(1+c)\) is strictly concave throughout \((0,1/2)\). Its derivative tends to \(+\infty\) as \(s\downarrow0\) and \(-\infty\) as \(s\uparrow1/2\). There is exactly one zero and one global maximizer **within this symmetric class**, with the stated critical equation. Root values in the finding are numerical evaluations of this uniquely specified constant, not substitutes for the strict-concavity proof.
6. **Exact trisection decoder.** At \((s,t)=(1/3,2/3)\), \(r=1/2\), \(c=1/3\), and \(a(s)=a(t)=(1+\sqrt2-\sqrt3)/(2\sqrt3)\). The four sign outcomes have probabilities \((1+c)/4,(1-c)/4,(1-c)/4,(1+c)/4\), i.e. \(1/3,1/6,1/6,1/3\). The conditional means are the three displayed values with combined masses \(1/3\) each. Substitution yields the radical explained-variance expression. The one-midpoint-sign benchmark has explained variance \((3-2\sqrt2)/4\), strictly less than the trisection two-bit benchmark.

## Verification
The standalone `verify.py` uses arbitrary-precision arithmetic to check the independently integrated bivariate-Gaussian arcsine kernel against the closed single-site expression at multiple interior sites, exact trisection identities, numerical root bracketing and risks, and algebraic projection identities at many deterministic pairs. Run `python -m pip install -r requirements.txt` followed by `python verify.py` from this package directory. The accompanying `verification_output.txt` is the output from an actual execution of that packaged script. These numerical checks corroborate the formulas; the continuum claim and uniqueness rest on the explicit analytic arguments above.

## Relationship to prior work
Classical Gaussian arcsine correlations and bridge covariance are used, not claimed as new. Swanepoel (2017) studies Brownian and bridge areas and a bridge last-sign-change law, rather than optimal estimation of positive occupation from two fixed signs. Salminen and Stenlund (2019) develop occupation-time transform and moment methods for diffusions; those general formulas do not supply the two-bit decoder, its elementary closed risk, or the symmetric two-site optimizer. Fesl, Koller, and Utschick (2022) study one-bit conditional means for jointly Gaussian channel-estimation models, including exact linear cases, whereas the target here is the non-Gaussian occupation functional of a whole bridge. Related one-sign occupation sampling and two-sign estimation of *other* bridge integrals are distinct earlier results: the present contribution begins at the two-sign occupation risk and its symmetric design. The combination of standard sign identities is made explicit, and no claim is made that these identities themselves are new.

## Limitations
The symmetric optimization is **not** a proof that asymmetric placements are globally dominated; the exact all-pair risk formula permits separate optimization over arbitrary pairs. Only two fixed noiseless zero-threshold sign measurements are considered, not adaptive sites, noisy signs, arbitrary quantizer thresholds, or more bits. Numerical digits and finite code checks do not prove uniqueness outside the stated symmetric class. The novelty assessment is provisional, with possible earlier equivalent results under excursion/sojourn and arcsine-regression terminology. No independent mathematical audit has been performed.

## References
- J. W. H. Swanepoel (2017), “A note on Brownian areas and arcsine laws,” *South African Statistical Journal* 51, 127–138, https://doi.org/10.37920/sasj.2017.51.1.7 (public issue date 2017-03-31).
- P. Salminen and D. Stenlund (2019), “On occupation times of one-dimensional diffusions,” https://arxiv.org/abs/1911.10839 (first arXiv posting 2019-11-25).
- B. Fesl, M. Koller, and W. Utschick (2022), “On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems,” https://arxiv.org/abs/2212.04470 (first arXiv posting 2022-12-08).
