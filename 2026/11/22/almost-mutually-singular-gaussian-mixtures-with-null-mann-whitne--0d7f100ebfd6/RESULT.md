# Almost mutually singular Gaussian mixtures with null Mann–Whitney and niche-overlap effects

## Finding

Let \(\Phi\) be the standard normal CDF and let \(\mathcal N(\mu,s^2)\) be the normal law with mean \(\mu\) and variance \(s^2\). For \(s>0\), define
\[
q_s=\Phi(1/(\sqrt{2}s))-\tfrac12,\qquad r_s=\Phi(3/(\sqrt{2}s))-\tfrac12,\qquad w_s=\frac{q_s}{q_s+r_s}.
\]
Set
\[
F_s=\tfrac12\mathcal N(-1,s^2)+\tfrac12\mathcal N(1,s^2),\qquad
G_{s,w}=(1-w)\mathcal N(0,s^2)+\tfrac w2\mathcal N(-2,s^2)+\tfrac w2\mathcal N(2,s^2),\qquad G_s=G_{s,w_s}.
\]
These laws have strictly positive real-analytic densities and are symmetric about zero. At \(w=w_s\) they have distinct variances, \(1+s^2<4w_s+s^2\), but their Mann–Whitney effect \(\Pr(X<Y)\) and **both orientations** of median-split niche overlap are exactly \(1/2\), for independent \(X\sim F_s\) and \(Y\sim G_s\). For every fixed \(s>0\), \(w_s\) is the unique \(w\in[0,1]\) giving null overlap in either orientation, and \(1/4<w_s<1/2\).

Nevertheless,
\[
1-4\Phi\bigl(-1/(2s)\bigr)\le d_{\mathrm{TV}}(F_s,G_s)<1,
\qquad \lim_{s\downarrow0}d_{\mathrm{TV}}(F_s,G_s)=1.
\]
Thus the supremum of total variation in the joint null-effect fiber is one even when restricted to strictly positive real-analytic densities. The displayed bound is approximately \(0.9999988533937125\) at \(s=0.1\).

For the joint effect vector normalized as in Section 5.1 of Beck–Langthaler–Bathke's open preprint, a test using the radial Gaussian null cutoff at a fixed level \(0<\alpha<1\) is not consistent against these pairs at any fixed \(s>0\) when both sample sizes grow in a fixed positive ratio. This assertion specifies the radial calibration and does not concern other tests or a limit with \(s\) changing with the sample sizes.

## Definitions and scope

For atomless CDFs \(A,B\) with unique medians \(m_A,m_B\), write
\[
J(A,B)=2\left(\int_{m_B}^{\infty} A(y)\,dB(y)-\int_{-\infty}^{m_B} A(y)\,dB(y)\right).
\]
Thus the integral is with respect to the **second** argument and split at its median. With \(X\sim F\), \(Y\sim G\), the notation of arXiv:2311.17564v1, Definition 2.2, is \(I_2=J(G,F)\) and \(I_1=J(F,G)\). The statement about both effects does not depend on these labels. This overlap is a rank functional, not the integral of the minimum of the two densities. Total variation here is \(\sup_E|F(E)-G(E)|\). For the inference claim the samples are independent and observations are iid within each sample.

## Proof

**Symmetry and orientation.** Let \(F,G\) be symmetric about zero with positive densities. The distribution of \(X-Y\) is symmetric and atomless, so \(\Pr(X<Y)=1/2\). Since \(G(0)=1/2\), reflecting the negative-half integral gives
\[
J(F,G)=4\int_0^\infty F(y)\,dG(y)-1
=\int_0^\infty (2F(y)-1)\,2dG(y)=\Pr(|X|<|Y|).
\]
Here \(2F(y)-1=\Pr(|X|<y)\) for \(y>0\), and \(2dG(y)\) on the positive half-line is the law of \(|Y|\). The corresponding reverse probability is \(J(G,F)=1-J(F,G)\) because the magnitudes have no ties. In particular, nullity of either orientation is equivalent to nullity of both for these families.

**Gaussian evaluation.** For independent \(U\sim\mathcal N(a,s^2)\) and \(V\sim\mathcal N(b,s^2)\), \(V-U\) and \(V+U\) are independent: they are jointly Gaussian and their covariance is \(s^2-s^2=0\). Put \(p=\Phi((b-a)/(\sqrt2s))\) and \(h=\Phi((b+a)/(\sqrt2s))\). Then
\[
\Pr(|U|<|V|)=\Pr((V-U)(V+U)>0)=ph+(1-p)(1-h).
\]
The absolute value of \(X\sim F_s\) has the same law as the absolute value of \(\mathcal N(1,s^2)\). At \(a=1,b=0\) the displayed formula gives \(A_s=1/2-2q_s^2\), and at \(a=1,b=2\) it gives \(B_s=1/2+2q_sr_s\). The sign of the center in the symmetric pair at \(\pm 2\) has no effect on its absolute value. Consequently
\[
J(F_s,G_{s,w})=(1-w)A_s+wB_s=\tfrac12+2q_s\big[w r_s-(1-w)q_s\big].
\]
Since \(q_s,r_s>0\), this has a unique crossing at \(w_s\); the reverse orientation has the same unique null weight. Since \(t\mapsto\Phi(t)-1/2\) is increasing and strictly concave for \(t>0\) and vanishes at zero, \(q_s<r_s<3q_s\), so \(1/4<w_s<1/2\). Positivity and analyticity follow from the Gaussian densities and positive weights. Symmetry gives zero means, hence the variances are \(s^2+1\) and \(s^2+4w_s\) and are distinct.

**Total variation.** Let \(E=[-3/2,-1/2]\cup[1/2,3/2]\) and \(u_s=\Phi(-1/(2s))\). For each component of \(F_s\), the interval of radius \(1/2\) centered at its mean lies in \(E\), so \(F_s(E)\ge 1-2u_s\). Each component of \(G_s\) has its mean at distance at least \(1/2\) from \(E\); thus \(G_s(E)\le 2u_s\). The difference gives the lower bound, and the integral of the pointwise minimum of the two densities is positive for finite \(s\), giving \(d_{\mathrm{TV}}<1\). The normal tail vanishes as \(s\downarrow0\), proving the supremum.

**Consequence for the fixed-level radial test.** Let \(n,m\) be the sample sizes from \(F_s,G_s\), with \(n/m\to\nu\in(0,\infty)\). Theorem 3.2 in the open preprint gives an asymptotically centered Gaussian law after scaling the estimation error of the two effect coordinates by \(\sqrt n\). The ROC integral \(\int G_s\,dF_s=\Pr(Y<X)\) is the complement of \(\Pr(X<Y)\) for continuous laws; both equal \(1/2\) here. Complementing the estimated first coordinate only changes the sign of that centered coordinate and does not change the radial statistic. The theorem's ROC-slope condition uses \(g_s(F_s^{-1}(t))/f_s(F_s^{-1}(t))\) on compact subintervals of \((0,1)\). This holds: \(F_s^{-1}\) sends any such closed subinterval to a finite compact interval, where the two densities are continuous and the denominator has a positive minimum.

The Section 5.1 null normalization is \(\sigma^2=(1/n+1/m)/12\); under distribution equality the centered vector divided by \(\sigma\) has a standard bivariate normal limit. For the radial implementation, reject when this normalized vector centered at \((1/2,1/2)\) has Euclidean norm greater than \(r_\alpha=\sqrt{\chi^2_{2,1-\alpha}}>0\). At the tuned alternative the population vector is still exactly \((1/2,1/2)\), and \(\sqrt n\,\sigma\to\sqrt{(1+\nu)/12}>0\), so the normalized vector converges to a centered finite Gaussian vector. Every centered Gaussian law has positive mass inside a ball of positive radius, even if its covariance is singular; a sphere of positive radius has measure zero for such a law. Therefore the rejection probability converges to a value strictly less than one. The assertion is about the specified radial rule and does not depend on the exact alternative covariance. It does not assert the same behavior for omnibus tests or the separate adjusted test of Section 5.2.

## Verification and prior scope

The accompanying `verify.py` uses Python 3, NumPy and SciPy. It checks numerically at six specified positive widths: it integrates both orientations in the explicit \(J\) convention, the Mann–Whitney effect, and the total variation, and compares with the formulas and the event lower bound. These are finite quadrature diagnostics. The analytic arguments above prove the claims for every \(s>0\) and do not depend on the quadrature.

Beck–Langthaler–Bathke already identify their joint effects and the test's non-omnibus nature. Their effect-region theorem constrains the achievable effect coordinates, not distances between pairs with the same coordinates; the construction in their preprint's Appendix C uses uniform distributions to establish attainability. Parkinson-Schwarz–Bathke give earlier overlap-based tests. The distinct contribution here is the explicit all-width Gaussian mixture tuning and the total-variation supremum on this null-effect fiber in the everywhere-positive analytic class; equal-median reciprocity, asymptotic normalization and general non-omnibus behavior are not claimed as new. The literature comparison is bounded and does not establish historical priority.

## References

1. J. Beck, P. B. Langthaler, A. C. Bathke, *Combining stochastic tendency and distribution overlap towards improved nonparametric effect measures and inference*. Open preprint: [arXiv:2311.17564v1](https://arxiv.org/abs/2311.17564v1), Definition 2.2, Theorems 3.1–3.2, Sections 5.1–5.2 and Appendix C. Journal DOI: [10.1111/sjos.12783](https://doi.org/10.1111/sjos.12783).
2. J. H. Parkinson-Schwarz, A. C. Bathke, *Testing for equality of distributions using the concept of (niche) overlap*, *Statistical Papers* 63 (2022), 225–242. [DOI:10.1007/s00362-021-01239-y](https://doi.org/10.1007/s00362-021-01239-y).
